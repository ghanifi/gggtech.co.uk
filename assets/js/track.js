/* GGG Technologies — GA4 conversion helpers.
   Sends click/submit events for phone, WhatsApp, email, CTAs and lead-form
   submissions so they can be marked as key events in GA4
   (Admin → Events → Mark as key event).
   Standard key-event names: generate_lead, click_to_call, click_whatsapp. */
(function () {
  function send(name, params) {
    if (typeof window.gtag === 'function') window.gtag('event', name, params);
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var low = href.toLowerCase();
    var page = window.location.pathname;
    if (href.indexOf('tel:') === 0) {
      send('phone_click', { link_url: href, page_path: page });      // legacy
      send('click_to_call', { link_url: href, page_path: page });    // key event
    } else if (low.indexOf('wa.me') !== -1 || low.indexOf('api.whatsapp.com') !== -1 || low.indexOf('whatsapp.com/send') !== -1) {
      send('click_whatsapp', { link_url: href, page_path: page });   // key event
    } else if (href.indexOf('mailto:') === 0) {
      send('email_click', { link_url: href, page_path: page });
    } else if (/^\/(get-a-quote|book-a-visit|contact)\/?(\.html)?(\?|#|$)/.test(href)) {
      send('cta_click', { cta_target: href, cta_text: (a.textContent || '').trim().slice(0, 60), page_path: page });
    }
  }, { passive: true });
  // Lead-form submissions → generate_lead (key event)
  document.addEventListener('submit', function (e) {
    var form = e.target;
    if (!form || form.tagName !== 'FORM') return;
    var page = window.location.pathname;
    var isLeadPage = /^\/(get-a-quote|book-a-visit|contact|demo-request)(\/|\.html|$)/.test(page);
    if (isLeadPage || (form.closest && form.closest('[data-lead-form]'))) {
      send('generate_lead', {
        form_id: form.id || form.getAttribute('name') || 'form',
        page_path: page
      });
    }
  }, true);
})();
