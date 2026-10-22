// Lesson player: sidebar, markdown rendering, tiny highlighter, code checks.
// No dependencies -- everything here is browser-native.

const state = {
  lessons: [],
  chapters: [],
  index: 0,
  done: new Set(),
};

const el = {
  nav: document.getElementById('lesson-nav'),
  body: document.getElementById('lesson-body'),
  crumb: document.getElementById('crumb'),
  progressText: document.getElementById('progress-text'),
  progressPct: document.getElementById('progress-pct'),
  progressFill: document.getElementById('progress-fill'),
  exercise: document.getElementById('exercise'),
  prompt: document.getElementById('exercise-prompt'),
  files: document.getElementById('exercise-files'),
  hints: document.getElementById('hints'),
  hintBtn: document.getElementById('hint-btn'),
  solutionBtn: document.getElementById('solution-btn'),
  solutionModal: document.getElementById('solution-modal'),
  solutionCode: document.getElementById('solution-code'),
  solutionCopy: document.getElementById('solution-copy'),
  solutionUse: document.getElementById('solution-use'),
  solutionClose: document.getElementById('solution-close'),
  solutionDismiss: document.getElementById('solution-dismiss'),
  code: document.getElementById('code'),
  output: document.getElementById('output'),
  runBtn: document.getElementById('run-btn'),
  submitBtn: document.getElementById('submit-btn'),
  resetBtn: document.getElementById('reset-btn'),
  prevBtn: document.getElementById('prev-btn'),
  nextBtn: document.getElementById('next-btn'),
  menuBtn: document.getElementById('menu-btn'),
  sidebar: document.getElementById('sidebar'),
};

const STORAGE_KEY = 'learn-python-progress';

// ---------- persistence ----------

function loadProgress() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) state.done = new Set(JSON.parse(raw));
  } catch { /* corrupt storage is not worth crashing over */ }
}

function saveProgress() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify([...state.done]));
  } catch { /* private mode: progress just won't persist */ }
}

// ---------- tiny markdown renderer ----------

function escapeHtml(text) {
  return text.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
}

const PY_KEYWORDS = /\b(def|return|if|elif|else|for|while|in|not|and|or|is|None|True|False|import|from|as|with|try|except|finally|raise|class|lambda|yield|pass|break|continue|global|nonlocal|assert|del)\b/g;

function highlight(code) {
  // Split on strings and comments first so their contents are never re-tokenized.
  const parts = code.split(/(#[^\n]*|"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')/g);
  return parts.map((part, i) => {
    if (i % 2 === 1) {
      return /^#/.test(part)
        ? `<span class="tok-com">${escapeHtml(part)}</span>`
        : `<span class="tok-str">${escapeHtml(part)}</span>`;
    }
    let out = escapeHtml(part);
    out = out.replace(PY_KEYWORDS, m => `<span class="tok-kw">${m}</span>`);
    out = out.replace(/\b(\d+(?:\.\d+)?)\b/g, m => `<span class="tok-num">${m}</span>`);
    out = out.replace(/([A-Za-z_]\w*)(?=\()/g, m => `<span class="tok-fn">${m}</span>`);
    return out;
  }).join('');
}

function inline(text) {
  return escapeHtml(text)
    .replace(/`([^`]+)`/g, (_, c) => `<code>${c}</code>`)
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/(^|[^*])\*([^*]+)\*/g, '$1<em>$2</em>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
}

function renderMarkdown(md) {
  const lines = md.replace(/\r\n/g, '\n').split('\n');
  const out = [];
  let i = 0;

  const flushList = (tag, items) => {
    if (items.length) out.push(`<${tag}>${items.map(x => `<li>${x}</li>`).join('')}</${tag}>`);
    items.length = 0;
  };

  let ul = [], ol = [], table = [];

  const closeBlocks = () => { flushList('ul', ul); flushList('ol', ol); flushTable(); };

  function flushTable() {
    if (!table.length) return;
    const rows = table.filter(r => !/^\|[\s:|-]+\|$/.test(r.trim()));
    if (rows.length) {
      const cells = r => r.trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim());
      const head = cells(rows[0]);
      const body = rows.slice(1).map(cells);
      out.push('<table><thead><tr>' + head.map(h => `<th>${inline(h)}</th>`).join('') + '</tr></thead><tbody>' +
        body.map(r => '<tr>' + r.map(c => `<td>${inline(c)}</td>`).join('') + '</tr>').join('') +
        '</tbody></table>');
    }
    table = [];
  }

  while (i < lines.length) {
    const line = lines[i];

    // fenced code
    const fence = line.match(/^```(\w*)/);
    if (fence) {
      closeBlocks();
      const buf = [];
      i++;
      while (i < lines.length && !/^```/.test(lines[i])) buf.push(lines[i++]);
      i++;
      out.push(`<pre><code>${highlight(buf.join('\n'))}</code></pre>`);
      continue;
    }

    if (!line.trim()) { closeBlocks(); i++; continue; }

    if (/^\|/.test(line)) { flushList('ul', ul); flushList('ol', ol); table.push(line); i++; continue; }
    flushTable();

    const h = line.match(/^(#{1,4})\s+(.*)$/);
    if (h) { closeBlocks(); out.push(`<h${h[1].length}>${inline(h[2])}</h${h[1].length}>`); i++; continue; }

    if (/^>\s?/.test(line)) {
      closeBlocks();
      const buf = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) buf.push(lines[i++].replace(/^>\s?/, ''));
      out.push(`<blockquote>${buf.map(b => `<p>${inline(b)}</p>`).join('')}</blockquote>`);
      continue;
    }

    const li = line.match(/^\s*[-*]\s+(.*)$/);
    if (li) { flushList('ol', ol); ul.push(inline(li[1])); i++; continue; }

    const oli = line.match(/^\s*\d+\.\s+(.*)$/);
    if (oli) { flushList('ul', ul); ol.push(inline(oli[1])); i++; continue; }

    closeBlocks();
    const buf = [];
    while (i < lines.length && lines[i].trim() && !/^(#{1,4}\s|```|>|\||\s*[-*]\s|\s*\d+\.\s)/.test(lines[i])) {
      buf.push(lines[i++]);
    }
    if (buf.length) out.push(`<p>${inline(buf.join(' '))}</p>`);
  }

  closeBlocks();
  return out.join('\n');
}

// ---------- rendering ----------

function renderSidebar() {
  el.nav.innerHTML = '';
  let currentChapter = null;

  state.lessons.forEach((lesson, idx) => {
    if (lesson.chapter !== currentChapter) {
      currentChapter = lesson.chapter;
      const h = document.createElement('div');
      h.className = 'nav-chapter';
      h.textContent = currentChapter;
      el.nav.appendChild(h);
    }
    const btn = document.createElement('button');
    btn.className = 'nav-item' + (idx === state.index ? ' active' : '') + (state.done.has(lesson.id) ? ' done' : '');
    btn.innerHTML = `<span class="dot">&#10003;</span><span>${escapeHtml(lesson.title)}</span>`;
    btn.addEventListener('click', () => go(idx));
    el.nav.appendChild(btn);
  });
}

function renderProgress() {
  const total = state.lessons.length;
  const done = state.done.size;
  const pct = total ? Math.round((done / total) * 100) : 0;
  el.progressText.textContent = `${done} / ${total} lessons`;
  el.progressPct.textContent = `${pct}%`;
  el.progressFill.style.width = `${pct}%`;
}

function renderLesson() {
  const lesson = state.lessons[state.index];
  if (!lesson) return;

  el.crumb.textContent = `${lesson.chapter} › ${lesson.title}`;
  el.body.innerHTML = renderMarkdown(lesson.body);
  el.body.scrollIntoView({ block: 'start' });

  const ex = lesson.exercise;
  if (ex) {
    el.exercise.hidden = false;
    el.prompt.textContent = ex.prompt;
    el.code.value = ex.starter ?? '';
    el.output.hidden = true;
    el.output.textContent = '';
    el.output.className = 'output';
    resetHints(ex);
    renderFiles(ex.files);
  } else {
    el.exercise.hidden = true;
  }

  el.prevBtn.disabled = state.index === 0;
  el.nextBtn.disabled = state.index === state.lessons.length - 1;
  renderSidebar();
  renderProgress();
}

// Show the files that already exist on disk for this exercise (file lessons).
function renderFiles(files) {
  el.files.innerHTML = '';
  const names = Object.keys(files ?? {});
  if (!names.length) { el.files.hidden = true; return; }
  el.files.hidden = false;

  const label = document.createElement('div');
  label.className = 'files-label';
  label.textContent = names.length === 1 ? 'File in this folder:' : 'Files in this folder:';
  el.files.appendChild(label);

  for (const name of names) {
    const block = document.createElement('div');
    block.className = 'file-item';
    block.innerHTML = `<div class="file-name">${escapeHtml(name)}</div>` +
      `<pre class="file-body">${escapeHtml(files[name])}</pre>`;
    el.files.appendChild(block);
  }
}

function go(index) {
  if (index < 0 || index >= state.lessons.length) return;
  state.index = index;
  renderLesson();
}

// ---------- hints and solutions ----------

let hintsShown = 0;

function resetHints(exercise) {
  hintsShown = 0;
  el.hints.innerHTML = '';
  el.hints.hidden = true;
  const total = (exercise.hints ?? []).length;
  el.hintBtn.hidden = total === 0;
  el.hintBtn.textContent = total > 1 ? `Hint (${total})` : 'Hint';
  el.hintBtn.disabled = total === 0;
  el.solutionBtn.hidden = !exercise.solution;
}

function showNextHint() {
  const lesson = state.lessons[state.index];
  const hints = lesson?.exercise?.hints ?? [];
  if (hintsShown >= hints.length) return;

  if (hintsShown === 0) {
    el.hints.hidden = false;
    el.hints.innerHTML = '<div class="hints-label">Hints</div>';
  }

  const item = document.createElement('div');
  item.className = 'hint-item';
  item.innerHTML = `<span class="hint-num">${hintsShown + 1}</span>` +
    `<span>${escapeHtml(hints[hintsShown])}</span>`;
  el.hints.appendChild(item);
  hintsShown++;

  const left = hints.length - hintsShown;
  el.hintBtn.textContent = left > 0 ? `Hint (${left} left)` : 'No more hints';
  el.hintBtn.disabled = left === 0;
}

function openSolution() {
  const lesson = state.lessons[state.index];
  const solution = lesson?.exercise?.solution;
  if (!solution) return;
  el.solutionCode.textContent = solution;
  el.solutionModal.hidden = false;
  el.solutionClose.focus();
}

function closeSolution() {
  el.solutionModal.hidden = true;
}

async function copySolution() {
  try {
    await navigator.clipboard.writeText(el.solutionCode.textContent);
    el.solutionCopy.textContent = 'Copied';
  } catch {
    el.solutionCopy.textContent = 'Copy failed';
  }
  setTimeout(() => { el.solutionCopy.textContent = 'Copy'; }, 1500);
}

// ---------- code checking ----------

function showOutput(html, kind) {
  el.output.hidden = false;
  el.output.className = 'output ' + kind;
  el.output.innerHTML = html;
}

async function post(path, body) {
  const res = await fetch(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  return res.json();
}

function renderRunResult(result) {
  const bits = [];
  if (result.stdout) bits.push(escapeHtml(result.stdout));
  if (!result.ok && result.stderr) bits.push(`<span class="out-err">${escapeHtml(result.stderr)}</span>`);
  return bits.join('') || '<span class="out-note">(no output)</span>';
}

async function runCode() {
  const lesson = state.lessons[state.index];
  if (!lesson?.exercise) return;
  el.runBtn.disabled = true;
  try {
    const result = await post('/api/run', {
      code: el.code.value,
      files: lesson.exercise.files ?? {},
    });
    showOutput(renderRunResult(result), result.ok ? 'pass' : 'fail');
  } catch {
    showOutput('<span class="out-err">Could not reach the server. Is server.py running?</span>', 'fail');
  } finally {
    el.runBtn.disabled = false;
  }
}

async function submitCode() {
  const lesson = state.lessons[state.index];
  if (!lesson?.exercise) return;
  el.submitBtn.disabled = true;
  try {
    const result = await post('/api/check', {
      code: el.code.value,
      expected: lesson.exercise.expected,
      files: lesson.exercise.files ?? {},
    });

    if (result.passed) {
      state.done.add(lesson.id);
      saveProgress();
      showOutput(
        '<span class="out-ok">✓ Passed!</span> <span class="out-note">Output matches.</span>\n\n' +
        escapeHtml(result.stdout), 'pass');
      renderSidebar();
      renderProgress();
    } else if (!result.ok) {
      showOutput('<span class="out-bad">✗ Your code errored.</span>\n\n' + renderRunResult(result), 'fail');
    } else {
      showOutput(
        '<span class="out-bad">✗ Not quite.</span> <span class="out-note">Your output does not match the expected output.</span>\n\n' +
        `<span class="out-note">expected:</span>\n${escapeHtml(lesson.exercise.expected)}\n` +
        `<span class="out-note">got:</span>\n${escapeHtml(result.stdout)}`, 'fail');
    }
  } catch {
    showOutput('<span class="out-err">Could not reach the server. Is server.py running?</span>', 'fail');
  } finally {
    el.submitBtn.disabled = false;
  }
}

// ---------- boot ----------

async function boot() {
  loadProgress();
  try {
    const res = await fetch('/api/lessons');
    const data = await res.json();
    state.lessons = data.lessons ?? [];
  } catch {
    el.body.innerHTML = '<p class="muted">Could not load lessons. Start the server with <code>python3 server.py</code>, then open <code>http://127.0.0.1:8000</code>.</p>';
    return;
  }

  if (!state.lessons.length) {
    el.body.innerHTML = '<p class="muted">No lessons found in content/lessons.json.</p>';
    return;
  }

  const fromHash = state.lessons.findIndex(l => `#${l.id}` === location.hash);
  state.index = fromHash >= 0 ? fromHash : 0;

  el.prevBtn.addEventListener('click', () => go(state.index - 1));
  el.nextBtn.addEventListener('click', () => go(state.index + 1));
  el.runBtn.addEventListener('click', runCode);
  el.submitBtn.addEventListener('click', submitCode);
  el.hintBtn.addEventListener('click', showNextHint);
  el.solutionBtn.addEventListener('click', openSolution);
  el.solutionClose.addEventListener('click', closeSolution);
  el.solutionDismiss.addEventListener('click', closeSolution);
  el.solutionCopy.addEventListener('click', copySolution);
  el.solutionUse.addEventListener('click', () => {
    el.code.value = el.solutionCode.textContent;
    closeSolution();
    el.code.focus();
  });
  el.solutionModal.addEventListener('click', e => {
    if (e.target === el.solutionModal) closeSolution();
  });
  el.resetBtn.addEventListener('click', () => {
    const lesson = state.lessons[state.index];
    if (lesson?.exercise) el.code.value = lesson.exercise.starter ?? '';
  });
  el.menuBtn.addEventListener('click', () => el.sidebar.classList.toggle('collapsed'));

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && !el.solutionModal.hidden) { closeSolution(); return; }
    if (e.ctrlKey && e.key === ',') { e.preventDefault(); go(state.index - 1); }
    if (e.ctrlKey && e.key === '.') { e.preventDefault(); go(state.index + 1); }
    if (e.ctrlKey && e.key === 'Enter' && !el.exercise.hidden) { e.preventDefault(); submitCode(); }
    if (e.ctrlKey && e.key === 'h' && !el.exercise.hidden) { e.preventDefault(); showNextHint(); }
  });

  // Tabbing inside the code box should indent, not leave the field.
  el.code.addEventListener('keydown', e => {
    if (e.key !== 'Tab') return;
    e.preventDefault();
    const { selectionStart: s, selectionEnd: t, value } = el.code;
    el.code.value = value.slice(0, s) + '    ' + value.slice(t);
    el.code.selectionStart = el.code.selectionEnd = s + 4;
  });

  renderLesson();
}

boot();
