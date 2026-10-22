// Browser test: loads index.html + app.js in a real DOM (happy-dom) against a
// running server, then clicks the actual buttons.
//
//   python3 server.py &            # in one terminal
//   bun tests/dom.test.mjs         # in another
//
// Needs bun and happy-dom:
//   bun install
//
// Static analysis cannot catch a button wired to the wrong function or state
// that never resets. This does.

import { Window } from 'happy-dom';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const BASE = process.env.BASE_URL ?? 'http://127.0.0.1:8000';

const failures = [];
const check = (name, cond, detail = '') => {
  if (!cond) failures.push(`${name}${detail ? ': ' + detail : ''}`);
};

// Fail fast with a useful message if the server is not up.
try {
  const probe = await fetch(`${BASE}/api/lessons`);
  if (!probe.ok) throw new Error(`status ${probe.status}`);
} catch (err) {
  console.error(`Cannot reach ${BASE} (${err.message}).\nStart it first:  python3 server.py`);
  process.exit(2);
}

const window = new Window({ url: BASE + '/' });
const { document } = window;
document.write(readFileSync(join(ROOT, 'index.html'), 'utf8'));

window.fetch = (path, opts) => fetch(new URL(path, BASE).href, opts);
try {
  Object.defineProperty(window.navigator, 'clipboard', {
    value: { writeText: async () => {} }, configurable: true,
  });
} catch { /* clipboard is optional */ }
window.HTMLElement.prototype.scrollIntoView = function () {};

window.eval(readFileSync(join(ROOT, 'app.js'), 'utf8'));

const tick = (ms = 150) => new Promise(r => setTimeout(r, ms));
await tick(700);

const $ = sel => document.querySelector(sel);
const text = sel => ($(sel)?.textContent ?? '').trim();
const count = sel => document.querySelectorAll(sel).length;
const navItems = () => [...document.querySelectorAll('.nav-item')];

// ---- boot ----
check('boot: sidebar populated', count('.nav-item') > 0, `got ${count('.nav-item')}`);
check('boot: progress rendered', /\/ \d+ lessons/.test(text('#progress-text')), text('#progress-text'));
check('boot: lesson rendered', text('.lesson-body h1').length > 0);
check('boot: exercise visible', !$('#exercise').hidden);
check('boot: no raw markdown fences', !$('.lesson-body').innerHTML.includes('```'));

// ---- hints ----
check('hint: button visible', !$('#hint-btn').hidden);
check('hint: panel hidden initially', $('#hints').hidden);
check('hint: label shows count', /^Hint \(\d+\)$/.test(text('#hint-btn')), text('#hint-btn'));

$('#hint-btn').click();
await tick();
check('hint: panel shown after click', !$('#hints').hidden);
check('hint: one item revealed', count('.hint-item') === 1, `got ${count('.hint-item')}`);
check('hint: label decrements', /left|No more/.test(text('#hint-btn')), text('#hint-btn'));

const total = navItems().length;
$('#hint-btn').click();
await tick();
check('hint: two items revealed', count('.hint-item') === 2, `got ${count('.hint-item')}`);
check('hint: exhausts to disabled', $('#hint-btn').disabled, text('#hint-btn'));

// ---- solution modal ----
check('solution: modal hidden initially', $('#solution-modal').hidden);
$('#solution-btn').click();
await tick();
check('solution: modal opens', !$('#solution-modal').hidden);
check('solution: code populated', text('#solution-code').length > 0);

$('#solution-dismiss').click();
await tick();
check('solution: dismiss closes', $('#solution-modal').hidden);

$('#solution-btn').click();
await tick();
$('#solution-use').click();
await tick();
check('solution: use closes modal', $('#solution-modal').hidden);
check('solution: code landed in editor', $('#code').value.length > 0);

// ---- submitting the published solution must pass ----
$('#submit-btn').click();
await tick(900);
check('submit: output visible', !$('#output').hidden);
check('submit: published solution passes', text('#output').includes('Passed'), text('#output'));
check('submit: progress increments', text('#progress-text').startsWith('1 /'), text('#progress-text'));
check('submit: nav marks done', count('.nav-item.done') >= 1);

// ---- a wrong answer is rejected ----
navItems()[1].click();
await tick(350);
$('#code').value = 'print("nope")';
$('#submit-btn').click();
await tick(900);
check('wrong: rejected', text('#output').includes('Not quite'), text('#output'));
check('wrong: shows expected output', text('#output').includes('expected'));

// ---- runtime errors surface ----
$('#code').value = 'print(1/0)';
$('#run-btn').click();
await tick(900);
check('run: error surfaced', text('#output').includes('ZeroDivisionError'), text('#output'));

// ---- file lesson shows its files ----
const fileNav = navItems().find(b => /Reading Files/.test(b.textContent));
if (fileNav) {
  fileNav.click();
  await tick(350);
  check('file: panel shown', !$('#exercise-files').hidden);
  check('file: filename listed', text('#exercise-files').includes('notes.txt'));
  check('file: contents listed', text('#exercise-files').includes('hello'));
} else {
  check('file: lesson present', false, 'Reading Files lesson not found');
}

// ---- navigating resets per-lesson state ----
navItems()[2].click();
await tick(350);
check('nav: hints reset', $('#hints').hidden, 'hints still visible');
check('nav: hint button reset', /^Hint \(\d+\)$/.test(text('#hint-btn')), text('#hint-btn'));
check('nav: output cleared', $('#output').hidden);
check('nav: crumb updated', text('#crumb').includes('›'));

// ---- keyboard shortcuts ----
const before = text('#crumb');
document.dispatchEvent(new window.KeyboardEvent('keydown', { key: '.', ctrlKey: true, bubbles: true }));
await tick(350);
check('keys: ctrl+. advances', text('#crumb') !== before);

document.dispatchEvent(new window.KeyboardEvent('keydown', { key: ',', ctrlKey: true, bubbles: true }));
await tick(350);
check('keys: ctrl+, goes back', text('#crumb') === before, text('#crumb'));

$('#solution-btn').click();
await tick(250);
document.dispatchEvent(new window.KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
await tick(250);
check('keys: escape closes modal', $('#solution-modal').hidden);

if (failures.length) {
  console.log(`\n${failures.length} FAILURE(S):`);
  for (const f of failures) console.log('  x ' + f);
  process.exit(1);
}
console.log('PASS: DOM tests (boot, hints, solution modal, submit, errors, files, nav, keys)');
