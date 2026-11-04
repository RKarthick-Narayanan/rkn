'use strict';
const menu = document.querySelector('.menu-toggle');
const nav = document.getElementById('primary-nav');
const desktop = window.matchMedia('(min-width: 1120px)');

// Navigation stays visible when JavaScript is unavailable.
if (menu && nav) {
  document.documentElement.classList.add('nav-ready');
  menu.hidden = false;
  const isOpen = () => menu.getAttribute('aria-expanded') === 'true';
  const close = (returnFocus = false) => {
    nav.classList.remove('is-open');
    menu.setAttribute('aria-expanded', 'false');
    if (returnFocus) menu.focus();
  };
  menu.addEventListener('click', () => {
    if (isOpen()) close();
    else {
      nav.classList.add('is-open');
      menu.setAttribute('aria-expanded', 'true');
      nav.querySelector('a').focus();
    }
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && isOpen()) close(true);
  });
  document.addEventListener('click', event => {
    if (isOpen() && !nav.contains(event.target) && !menu.contains(event.target)) close();
  });
  nav.addEventListener('click', event => {
    if (event.target.closest('a')) close();
  });
  document.addEventListener('focusin', event => {
    if (isOpen() && !nav.contains(event.target) && !menu.contains(event.target)) close();
  });
  desktop.addEventListener('change', () => {
    // Avoid retaining keyboard focus in links hidden after a desktop-to-mobile resize.
    const focusInNav = nav.contains(document.activeElement);
    close(!desktop.matches && focusInNav);
  });
}

document.querySelectorAll('[data-year]').forEach(element => {
  element.textContent = new Date().getFullYear();
});

// Existing external bookmarks to the former one-page site remain useful.
if (document.querySelector('.hero')) {
  const legacy = {
    '#01': 'index.html', '#02': 'about.html', '#03': 'about.html#education',
    '#04': 'about.html#appointments', '#05': 'publications.html', '#06': 'contact.html'
  };
  const followLegacy = () => {
    if (legacy[location.hash]) location.replace(legacy[location.hash]);
  };
  followLegacy();
  window.addEventListener('hashchange', followLegacy);
}
