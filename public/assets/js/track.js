/* GGG Technologies — GA4 conversion helpers.
   Sends click events for phone, email and primary CTAs so they can be
   marked as key events in GA4 (Admin → Events → Mark as key event). */
(function () {
  function send(name, params) {
    if (typeof window.gtag === 'function') window.gtag('event', name, params);
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var page = window.location.pathname;
    if (href.indexOf('tel:') === 0) {
      send('phone_click', { link_url: href, page_path: page });
    } else if (href.indexOf('mailto:') === 0) {
      send('email_click', { link_url: href, page_path: page });
    } else if (/^\/(get-a-quote|book-a-visit|contact)\/?(\?|#|$)/.test(href)) {
      send('cta_click', { cta_target: href, cta_text: (a.textContent || '').trim().slice(0, 60), page_path: page });
    }
  }, { passive: true });
})();
