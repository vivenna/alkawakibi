/**
 * Kontaktformular der Website des Alkawakibi Verein e. V.
 *
 * Nimmt die Formulardaten entgegen, prüft sie, schreibt sie in die
 * Supabase-Tabelle "kontaktanfragen" und schickt dem Verein eine
 * Benachrichtigung per E-Mail.
 *
 * Einrichtung siehe ../README.md
 */

/** Konfiguration wird in den Skripteigenschaften hinterlegt, nicht im Code. */
function konfiguration_() {
  var e = PropertiesService.getScriptProperties();
  return {
    supabaseUrl:   e.getProperty('SUPABASE_URL'),          // https://xxxx.supabase.co
    supabaseKey:   e.getProperty('SUPABASE_SERVICE_KEY'),  // service_role-Schlüssel
    tabelle:       e.getProperty('SUPABASE_TABELLE') || 'kontaktanfragen',
    benachrichtigung: e.getProperty('BENACHRICHTIGUNG_AN') || '',
    erlaubteHerkunft: (e.getProperty('ERLAUBTE_HERKUNFT') || '').split(',')
                        .map(function (s) { return s.trim(); })
                        .filter(String)
  };
}

var BETREFFE = [
  'Allgemeine Anfrage', 'Mitgliedschaft', 'Spenden', 'Epithetik-Projekt',
  'Forum für Ärzte, Zahnärzte und Apotheker', 'Presse', 'Sonstiges'
];

function doGet() {
  return antwort_({ ok: true, dienst: 'Kontaktformular Alkawakibi e. V.' });
}

function doPost(e) {
  try {
    var daten = lesen_(e);
    var fehler = pruefen_(daten);
    if (fehler.length) {
      return antwort_({ ok: false, fehler: fehler }, 400);
    }

    // Honigtopf: ausgefüllt heißt Bot. Wir melden Erfolg und verwerfen still.
    if (daten.website) {
      return antwort_({ ok: true, hinweis: 'verworfen' });
    }

    var zeile = {
      name:         kuerzen_(daten.name, 120),
      email:        kuerzen_(daten.email, 160),
      telefon:      daten.telefon ? kuerzen_(daten.telefon, 60) : null,
      betreff:      BETREFFE.indexOf(daten.betreff) >= 0 ? daten.betreff : 'Sonstiges',
      nachricht:    kuerzen_(daten.nachricht, 5000),
      einwilligung: daten.einwilligung === true || daten.einwilligung === 'true',
      quelle:       kuerzen_(daten.quelle || '', 120) || null,
      user_agent:   kuerzen_(daten.userAgent || '', 300) || null
    };

    speichern_(zeile);
    benachrichtigen_(zeile);
    return antwort_({ ok: true });

  } catch (fehler) {
    console.error(fehler);
    return antwort_({ ok: false, fehler: ['Serverfehler'] }, 500);
  }
}

/** Liest JSON-Text oder klassische Formularfelder. */
function lesen_(e) {
  if (e && e.postData && e.postData.contents) {
    try {
      return JSON.parse(e.postData.contents);
    } catch (ignoriert) { /* fällt auf Parameter zurück */ }
  }
  return (e && e.parameter) || {};
}

function pruefen_(d) {
  var fehler = [];
  if (!d.name || String(d.name).trim().length < 2)          fehler.push('name');
  if (!d.email || !/^[^@\s]+@[^@\s.]+\.[^@\s]{2,}$/.test(String(d.email).trim()))
                                                             fehler.push('email');
  if (!d.nachricht || String(d.nachricht).trim().length < 10) fehler.push('nachricht');
  if (!(d.einwilligung === true || d.einwilligung === 'true')) fehler.push('einwilligung');
  return fehler;
}

function kuerzen_(wert, laenge) {
  return String(wert === null || wert === undefined ? '' : wert).trim().slice(0, laenge);
}

function speichern_(zeile) {
  var k = konfiguration_();
  if (!k.supabaseUrl || !k.supabaseKey) {
    throw new Error('SUPABASE_URL oder SUPABASE_SERVICE_KEY fehlt in den Skripteigenschaften.');
  }
  var antwort = UrlFetchApp.fetch(
    k.supabaseUrl.replace(/\/+$/, '') + '/rest/v1/' + k.tabelle,
    {
      method: 'post',
      contentType: 'application/json',
      headers: {
        apikey: k.supabaseKey,
        Authorization: 'Bearer ' + k.supabaseKey,
        Prefer: 'return=minimal'
      },
      payload: JSON.stringify(zeile),
      muteHttpExceptions: true
    }
  );
  var code = antwort.getResponseCode();
  if (code < 200 || code >= 300) {
    throw new Error('Supabase antwortete mit ' + code + ': ' + antwort.getContentText());
  }
}

function benachrichtigen_(zeile) {
  var k = konfiguration_();
  if (!k.benachrichtigung) return;
  var text =
    'Neue Nachricht über das Kontaktformular der Website\n\n' +
    'Name:      ' + zeile.name + '\n' +
    'E-Mail:    ' + zeile.email + '\n' +
    'Telefon:   ' + (zeile.telefon || '–') + '\n' +
    'Betreff:   ' + zeile.betreff + '\n' +
    'Seite:     ' + (zeile.quelle || '–') + '\n\n' +
    zeile.nachricht + '\n';
  MailApp.sendEmail({
    to: k.benachrichtigung,
    subject: '[Website] ' + zeile.betreff + ' – ' + zeile.name,
    body: text,
    replyTo: zeile.email
  });
}

function antwort_(nutzlast, code) {
  // Apps-Script-Webanwendungen können keine eigenen Statuscodes setzen;
  // der Erfolg steht deshalb im Feld "ok".
  if (code) { nutzlast.status = code; }
  return ContentService
    .createTextOutput(JSON.stringify(nutzlast))
    .setMimeType(ContentService.MimeType.JSON);
}

/** Einmal von Hand ausführen: prüft Konfiguration und Schreibzugriff. */
function selbsttest() {
  speichern_({
    name: 'Selbsttest', email: 'test@example.org', telefon: null,
    betreff: 'Sonstiges', nachricht: 'Testeintrag aus dem Apps Script.',
    einwilligung: true, quelle: 'selbsttest', user_agent: 'Apps Script'
  });
  console.log('Schreibzugriff auf Supabase funktioniert.');
}
