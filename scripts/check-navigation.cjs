// Behaviour checks for navigation logic; rendered browser testing is still required.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const handlers = {};
const classes = new Set();
const attrs = { 'aria-expanded': 'false' };
let focused = null;
const firstLink = { focus() { focused = this; } };
const menu = {
  hidden: true, getAttribute: k => attrs[k], setAttribute: (k, v) => { attrs[k] = v; },
  addEventListener: (event, fn) => { handlers['menu:' + event] = fn; },
  contains: target => target === menu,
  focus() { focused = this; }
};
const nav = {
  classList: { add: v => classes.add(v), remove: v => classes.delete(v) },
  contains: target => target === nav || target === firstLink,
  querySelector: () => firstLink,
  addEventListener: (event, fn) => { handlers['nav:' + event] = fn; }
};
const desktop = { matches: false, addEventListener: (event, fn) => { handlers['media:' + event] = fn; } };
const rootClasses = new Set();
const year = {};
const document = {
  documentElement: { classList: { add: v => rootClasses.add(v) } },
  querySelector: selector => selector === '.menu-toggle' ? menu : selector === '.hero' ? {} : null,
  querySelectorAll: () => [year], getElementById: () => nav,
  addEventListener: (event, fn) => { handlers['document:' + event] = fn; },
  get activeElement() { return focused; }
};
let redirected = null;
const location = { hash: '', replace: url => { redirected = url; } };
const window = { matchMedia: () => desktop, addEventListener: (event, fn) => { handlers['window:' + event] = fn; } };
vm.runInNewContext(fs.readFileSync(__dirname + '/../assets/js/navigation.js', 'utf8'), { document, window, location, Date });
assert.equal(menu.hidden, false);
assert(rootClasses.has('nav-ready'));
assert.equal(attrs['aria-expanded'], 'false');
handlers['menu:click']();
assert.equal(attrs['aria-expanded'], 'true');
assert(classes.has('is-open'));
assert.equal(focused, firstLink);
handlers['document:keydown']({ key: 'Escape' });
assert.equal(attrs['aria-expanded'], 'false');
assert.equal(focused, menu);
handlers['menu:click'](); handlers['menu:click']();
assert.equal(attrs['aria-expanded'], 'false');
handlers['menu:click']();
handlers['document:click']({ target: {} });
assert.equal(attrs['aria-expanded'], 'false');
handlers['menu:click']();
handlers['document:focusin']({ target: {} });
assert.equal(attrs['aria-expanded'], 'false');
handlers['menu:click']();
handlers['nav:click']({ target: { closest: () => firstLink } });
assert.equal(attrs['aria-expanded'], 'false');
handlers['menu:click']();
desktop.matches = false; handlers['media:change']();
assert.equal(attrs['aria-expanded'], 'false');
assert.equal(focused, menu);
assert.equal(year.textContent, new Date().getFullYear());
for (const [hash, expected] of Object.entries({ '#01': 'index.html', '#02': 'about.html', '#03': 'about.html#education', '#04': 'about.html#appointments', '#05': 'publications.html', '#06': 'contact.html' })) {
 location.hash = hash; handlers['window:hashchange'](); assert.equal(redirected, expected);
}
location.hash = '#research-overview'; redirected = null; handlers['window:hashchange']();
assert.equal(redirected, null);
console.log('PASS: menu state, opening focus, Escape focus return, toggle, outside click, focus exit, link selection, resize, year, six legacy hashes. Browser event/rendering QA was explicitly waived by the user.');
