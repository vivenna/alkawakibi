/* Alkawakibi e. V. – Verhalten der Website.
 *
 * Alles hier ist Zugabe: ohne JavaScript bleiben alle Inhalte lesbar, die
 * Navigation bedienbar und das Formular über das E-Mail-Programm absendbar.
 */
(function () {
  'use strict';

  var KONF = window.ALKAWAKIBI_KONFIGURATION || {};
  var ruhig = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function alle(auswahl, wurzel) {
    return Array.prototype.slice.call((wurzel || document).querySelectorAll(auswahl));
  }

  /* ------------------------------------------------------------ Navigation */

  function navigationEinrichten() {
    var kopf = document.getElementById('kopfbereich');
    var schalter = document.querySelector('.menue-schalter');
    var menue = document.getElementById('hauptmenue');
    if (!schalter || !menue) { return; }

    var fokussierbar = 'a[href], button:not([disabled]), input, select, textarea';

    function offen() { return schalter.getAttribute('aria-expanded') === 'true'; }

    function setzen(zustand) {
      schalter.setAttribute('aria-expanded', zustand ? 'true' : 'false');
      document.body.classList.toggle('menue-offen', zustand);
      menue.classList.toggle('ist-offen', zustand);
      if (zustand) {
        var erstes = menue.querySelector(fokussierbar);
        if (erstes) { erstes.focus(); }
      }
    }

    schalter.addEventListener('click', function () {
      var neu = !offen();
      setzen(neu);
      if (!neu) { schalter.focus(); }
    });

    document.addEventListener('keydown', function (ereignis) {
      if (ereignis.key !== 'Escape') { return; }
      if (offen()) { setzen(false); schalter.focus(); }
    });

    /* Fokus im geöffneten Menü halten */
    document.addEventListener('keydown', function (ereignis) {
      if (ereignis.key !== 'Tab' || !offen()) { return; }
      var elemente = alle(fokussierbar, menue).concat([schalter]);
      if (!elemente.length) { return; }
      var erstes = elemente[0];
      var letztes = elemente[elemente.length - 1];
      if (ereignis.shiftKey && document.activeElement === erstes) {
        ereignis.preventDefault(); letztes.focus();
      } else if (!ereignis.shiftKey && document.activeElement === letztes) {
        ereignis.preventDefault(); erstes.focus();
      }
    });

    /* Untermenüs: auf kleinen Bildschirmen aufklappbar */
    alle('.untermenue-schalter').forEach(function (knopf) {
      knopf.addEventListener('click', function () {
        var auf = knopf.getAttribute('aria-expanded') === 'true';
        alle('.untermenue-schalter').forEach(function (anderer) {
          if (anderer !== knopf) {
            anderer.setAttribute('aria-expanded', 'false');
            anderer.parentNode.classList.remove('untermenue-offen');
          }
        });
        knopf.setAttribute('aria-expanded', auf ? 'false' : 'true');
        knopf.parentNode.classList.toggle('untermenue-offen', !auf);
      });
    });

    document.addEventListener('click', function (ereignis) {
      if (ereignis.target.closest && ereignis.target.closest('.hat-untermenue')) { return; }
      alle('.untermenue-schalter').forEach(function (knopf) {
        knopf.setAttribute('aria-expanded', 'false');
        knopf.parentNode.classList.remove('untermenue-offen');
      });
    });

    /* Zustand des Kopfbereichs beim Blättern */
    if (kopf) {
      var pruefen = function () {
        kopf.classList.toggle('ist-gescrollt', window.scrollY > 40);
      };
      pruefen();
      window.addEventListener('scroll', pruefen, { passive: true });
    }
  }

  /* ------------------------------------------------------- IBAN kopieren */

  function ibanEinrichten() {
    alle('.iban-kopieren').forEach(function (knopf) {
      if (!navigator.clipboard) { return; }
      knopf.hidden = false;
      var beschriftung = knopf.textContent;
      knopf.addEventListener('click', function () {
        navigator.clipboard.writeText(knopf.getAttribute('data-iban')).then(function () {
          knopf.textContent = 'Kopiert';
          knopf.classList.add('ist-kopiert');
          window.setTimeout(function () {
            knopf.textContent = beschriftung;
            knopf.classList.remove('ist-kopiert');
          }, 2200);
        }).catch(function () {
          knopf.textContent = 'Kopieren nicht möglich';
        });
      });
    });
  }

  /* ------------------------------------------------------------- Formular */

  var FEHLERTEXTE = {
    name: 'Bitte geben Sie Ihren Namen an.',
    email: 'Bitte geben Sie eine gültige E-Mail-Adresse an.',
    betreff: 'Bitte wählen Sie einen Betreff.',
    nachricht: 'Bitte schreiben Sie uns mindestens ein paar Worte.',
    einwilligung: 'Ohne Ihre Einwilligung können wir die Anfrage nicht bearbeiten.'
  };

  function formularEinrichten() {
    var formular = document.getElementById('kontaktformular-formular');
    if (!formular) { return; }
    var meldung = document.getElementById('formular-meldung');

    function fehlerZeigen(kennung, text) {
      var feld = formular.elements[kennung];
      var stelle = document.getElementById('fehler-' + kennung);
      if (stelle) { stelle.textContent = text || ''; }
      if (feld) {
        feld.setAttribute('aria-invalid', text ? 'true' : 'false');
        feld.closest('.formfeld').classList.toggle('hat-fehler', Boolean(text));
      }
    }

    function pruefen() {
      var fehlend = [];
      var werte = {
        name: formular.elements.name.value.trim(),
        email: formular.elements.email.value.trim(),
        betreff: formular.elements.betreff.value,
        nachricht: formular.elements.nachricht.value.trim(),
        einwilligung: formular.elements.einwilligung.checked
      };
      ['name', 'email', 'betreff', 'nachricht', 'einwilligung'].forEach(function (k) {
        fehlerZeigen(k, '');
      });
      if (werte.name.length < 2) { fehlend.push('name'); }
      if (!/^[^@\s]+@[^@\s.]+\.[^@\s]{2,}$/.test(werte.email)) { fehlend.push('email'); }
      if (!werte.betreff) { fehlend.push('betreff'); }
      if (werte.nachricht.length < 10) { fehlend.push('nachricht'); }
      if (!werte.einwilligung) { fehlend.push('einwilligung'); }
      fehlend.forEach(function (k) { fehlerZeigen(k, FEHLERTEXTE[k]); });
      return { fehlend: fehlend, werte: werte };
    }

    function ersatzVerweis(werte) {
      var text = 'Name: ' + werte.name + '\nE-Mail: ' + werte.email +
                 '\nTelefon: ' + (formular.elements.telefon.value || '-') +
                 '\n\n' + werte.nachricht;
      return 'mailto:' + (KONF.ersatzEmail || 'info@alkawakibi.org') +
             '?subject=' + encodeURIComponent(werte.betreff) +
             '&body=' + encodeURIComponent(text);
    }

    function melden(text, art, werte) {
      if (!meldung) { return; }
      meldung.textContent = text;
      meldung.className = 'formular-meldung meldung-' + art;
      meldung.setAttribute('role', art === 'fehler' ? 'alert' : 'status');
      if (art === 'fehler' && werte) {
        var verweis = document.createElement('a');
        verweis.href = ersatzVerweis(werte);
        verweis.textContent = 'Nachricht per E-Mail-Programm senden';
        meldung.appendChild(document.createTextNode(' '));
        meldung.appendChild(verweis);
      }
    }

    formular.addEventListener('submit', function (ereignis) {
      ereignis.preventDefault();
      var ergebnis = pruefen();
      if (ergebnis.fehlend.length) {
        var erstes = formular.elements[ergebnis.fehlend[0]];
        if (erstes) { erstes.focus(); }
        melden('Bitte prüfen Sie die hervorgehobenen Felder.', 'fehler', null);
        return;
      }
      if (formular.elements.website.value) { return; }   /* Honigtopf */

      var knopf = formular.querySelector('button[type="submit"]');
      var daten = {
        name: ergebnis.werte.name,
        email: ergebnis.werte.email,
        telefon: formular.elements.telefon.value.trim(),
        betreff: ergebnis.werte.betreff,
        nachricht: ergebnis.werte.nachricht,
        einwilligung: true,
        website: '',
        quelle: location.pathname.split('/').pop() || 'index.html',
        userAgent: navigator.userAgent
      };

      if (!KONF.formularEndpunkt) {
        melden('Der Versand ist noch nicht eingerichtet.', 'fehler', ergebnis.werte);
        return;
      }

      knopf.disabled = true;
      var alteBeschriftung = knopf.textContent;
      knopf.textContent = 'Wird gesendet …';
      melden('Ihre Nachricht wird gesendet …', 'warten', null);

      fetch(KONF.formularEndpunkt, {
        method: 'POST',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify(daten)
      }).then(function (antwort) {
        return antwort.json().catch(function () { return { ok: antwort.ok }; });
      }).then(function (ergebnisDaten) {
        if (ergebnisDaten && ergebnisDaten.ok) {
          formular.reset();
          melden('Vielen Dank. Ihre Nachricht ist bei uns eingegangen – wir melden uns zeitnah.', 'erfolg', null);
        } else {
          melden('Das Senden hat leider nicht geklappt. Bitte schreiben Sie uns direkt an info@alkawakibi.org.', 'fehler', ergebnis.werte);
        }
      }).catch(function () {
        melden('Das Senden hat leider nicht geklappt. Bitte schreiben Sie uns direkt an info@alkawakibi.org.', 'fehler', ergebnis.werte);
      }).then(function () {
        knopf.disabled = false;
        knopf.textContent = alteBeschriftung;
      });
    });
  }

  /* ------------------------------------------------------------- Lightbox */

  function galerieEinrichten() {
    var bilder = alle('.galerie-bild');
    if (!bilder.length) { return; }

    var overlay = document.createElement('div');
    overlay.className = 'lichtkasten';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Bildansicht');
    overlay.hidden = true;
    overlay.innerHTML =
      '<button class="lichtkasten-schliessen" type="button">Schließen</button>' +
      '<button class="lichtkasten-zurueck" type="button" aria-label="Vorheriges Bild">&#8249;</button>' +
      '<img class="lichtkasten-bild" src="" alt="">' +
      '<button class="lichtkasten-weiter" type="button" aria-label="Nächstes Bild">&#8250;</button>' +
      '<p class="lichtkasten-zaehler" aria-live="polite"></p>';
    document.body.appendChild(overlay);

    var bild = overlay.querySelector('.lichtkasten-bild');
    var zaehler = overlay.querySelector('.lichtkasten-zaehler');
    var schliessen = overlay.querySelector('.lichtkasten-schliessen');
    var aktuell = 0;
    var vorher = null;

    function zeigen(nummer) {
      aktuell = (nummer + bilder.length) % bilder.length;
      var verweis = bilder[aktuell];
      bild.src = verweis.getAttribute('data-gross') || verweis.href;
      bild.alt = verweis.querySelector('img').alt;
      zaehler.textContent = 'Bild ' + (aktuell + 1) + ' von ' + bilder.length;
    }

    function oeffnen(nummer) {
      vorher = document.activeElement;
      overlay.hidden = false;
      document.body.classList.add('lichtkasten-offen');
      zeigen(nummer);
      schliessen.focus();
    }

    function zu() {
      overlay.hidden = true;
      document.body.classList.remove('lichtkasten-offen');
      if (vorher) { vorher.focus(); }
    }

    bilder.forEach(function (verweis, nummer) {
      verweis.addEventListener('click', function (ereignis) {
        ereignis.preventDefault();
        oeffnen(nummer);
      });
    });

    schliessen.addEventListener('click', zu);
    overlay.querySelector('.lichtkasten-zurueck').addEventListener('click', function () { zeigen(aktuell - 1); });
    overlay.querySelector('.lichtkasten-weiter').addEventListener('click', function () { zeigen(aktuell + 1); });
    overlay.addEventListener('click', function (ereignis) {
      if (ereignis.target === overlay) { zu(); }
    });
    document.addEventListener('keydown', function (ereignis) {
      if (overlay.hidden) { return; }
      if (ereignis.key === 'Escape') { zu(); }
      if (ereignis.key === 'ArrowLeft') { zeigen(aktuell - 1); }
      if (ereignis.key === 'ArrowRight') { zeigen(aktuell + 1); }
      if (ereignis.key === 'Tab') {
        var knoepfe = alle('button', overlay);
        var erstes = knoepfe[0];
        var letztes = knoepfe[knoepfe.length - 1];
        if (ereignis.shiftKey && document.activeElement === erstes) {
          ereignis.preventDefault(); letztes.focus();
        } else if (!ereignis.shiftKey && document.activeElement === letztes) {
          ereignis.preventDefault(); erstes.focus();
        }
      }
    });
  }


  /* ------------------------------------------------------------ Aufmacher */

  function wechslerEinrichten() {
    var wechsler = document.querySelector('.aufmacher');
    if (!wechsler) { return; }
    var tafeln = alle('.aufmacher-tafel', wechsler);
    if (tafeln.length < 2) { return; }

    wechsler.classList.add('ist-bereit');
    var punkte = document.createElement('div');
    punkte.className = 'aufmacher-punkte';
    var aktuell = 0;
    var uhr = null;

    function zeigen(nummer) {
      aktuell = (nummer + tafeln.length) % tafeln.length;
      tafeln.forEach(function (tafel, i) {
        tafel.classList.toggle('ist-sichtbar', i === aktuell);
        tafel.setAttribute('aria-hidden', i === aktuell ? 'false' : 'true');
      });
      alle('button', punkte).forEach(function (knopf, i) {
        knopf.setAttribute('aria-current', i === aktuell ? 'true' : 'false');
      });
    }

    tafeln.forEach(function (tafel, i) {
      var knopf = document.createElement('button');
      knopf.type = 'button';
      knopf.innerHTML = '<span class="nur-vorlesen">Tafel ' + (i + 1) + '</span>';
      knopf.addEventListener('click', function () { zeigen(i); anhalten(); });
      punkte.appendChild(knopf);
    });

    var zurueck = document.createElement('button');
    zurueck.type = 'button';
    zurueck.className = 'aufmacher-pfeil aufmacher-zurueck';
    zurueck.setAttribute('aria-label', 'Vorherige Tafel');
    zurueck.innerHTML = '&#8249;';
    var weiter = document.createElement('button');
    weiter.type = 'button';
    weiter.className = 'aufmacher-pfeil aufmacher-weiter';
    weiter.setAttribute('aria-label', 'Nächste Tafel');
    weiter.innerHTML = '&#8250;';
    zurueck.addEventListener('click', function () { zeigen(aktuell - 1); anhalten(); });
    weiter.addEventListener('click', function () { zeigen(aktuell + 1); anhalten(); });

    wechsler.appendChild(zurueck);
    wechsler.appendChild(weiter);
    wechsler.appendChild(punkte);
    wechsler.setAttribute('aria-live', 'polite');

    function laufen() {
      if (ruhig || uhr) { return; }
      uhr = window.setInterval(function () { zeigen(aktuell + 1); }, 6000);
    }
    function anhalten() {
      if (uhr) { window.clearInterval(uhr); uhr = null; }
    }

    wechsler.addEventListener('mouseenter', anhalten);
    wechsler.addEventListener('mouseleave', laufen);
    wechsler.addEventListener('focusin', anhalten);
    wechsler.addEventListener('focusout', laufen);

    zeigen(0);
    laufen();
  }


  /* ------------------------------------------------------------- Start */

  function start() {
    navigationEinrichten();
    ibanEinrichten();
    formularEinrichten();
    galerieEinrichten();
    wechslerEinrichten();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
}());
