# -*- coding: utf-8 -*-
"""Entwurf 2 – „Institut“.

Hell, redaktionell gegliedert, in den Logofarben Schwarz und Dunkelgrün.
Dienstleiste, feste Navigationsleiste, Aufmacher mit Wechsler, Karten mit
„Weiterlesen“ und Seitenleisten – das Ordnungsprinzip von e-cfr.org auf
Vereinsgröße gebracht.
"""
import inhalte as I
import skripte
from basis import e
from css_basis import GRUNDLAGE
from entwurf_basis import Entwurf

TAFELN = [
    {'kicker': 'Für Demokratie und Menschenrechte',
     'titel': 'Demokratie wächst dort, wo Menschen einander zuhören.',
     'text': I.HERO['text'],
     'ziel': 'wer-wir-sind.html', 'linktext': 'Über den Verein',
     'bild': I.BILD + 'veranstaltung-publikum-800.jpg',
     'breite': 800, 'hoehe': 534,
     'alt': I.HERO['alt']},
    {'kicker': 'Projekt',
     'titel': 'Epithetik-Projekt',
     'text': I.PROJEKTE[0]['text'],
     'ziel': 'projekt-epithetik.html', 'linktext': 'Zum Projekt',
     'bild': I.BILD + 'begegnung-gespraech-800.jpg',
     'breite': 800, 'hoehe': 534,
     'alt': 'Gespräch am Rande einer Veranstaltung des Vereins'},
    {'kicker': 'Ausgezeichnet',
     'titel': '1. Preis beim Berliner Gesundheitspreis 2017',
     'text': I.AUSZEICHNUNG['text'],
     'ziel': 'projekt-forum.html', 'linktext': 'Zum Forum',
     'bild': I.AUSZEICHNUNG['bild'],
     'breite': I.AUSZEICHNUNG['breite'], 'hoehe': I.AUSZEICHNUNG['hoehe'],
     'alt': I.AUSZEICHNUNG['alt']},
]


class Institut(Entwurf):
    kennung = 'entwurf-2-institut'
    name = 'Institut'
    schriften = ['source-serif-4', 'source-sans-3', 'noto-naskh-arabic']
    logo = 'assets/bilder/logo.png'
    logo_fuss = 'assets/bilder/logo-weiss.png'
    farbe_browser = '#0d4a0d'

    # ------------------------------------------------------------- Struktur

    def kopf(self, aktiv):
        v = I.VEREIN
        return f"""  <div class="dienstleiste">
    <div class="dienst-huelle">
      <p class="dienst-ort">{e(v['strasse'])} · {e(v['ort'])}</p>
      <p class="dienst-rechts">
        <a href="mailto:{v['email']}">{v['email']}</a>
        <a href="mitglied-werden.html">Mitglied werden</a>
      </p>
    </div>
  </div>
  <header class="kopfbereich" id="kopfbereich">
    <div class="kopf-huelle">
      <a class="logo" href="index.html">
        <img src="{self.logo}" alt="{e(v['kurz'])} – {e(v['claim'])}" width="220" height="79">
      </a>
      <a class="navi-spende" href="spenden.html">Spenden</a>
      <button class="menue-schalter" type="button" aria-expanded="false" aria-controls="hauptmenue">
        <span class="menue-striche" aria-hidden="true"></span>
        <span class="menue-wort">Menü</span>
      </button>
    </div>
    <nav class="hauptnavigation" id="hauptmenue" aria-label="Hauptmenü">
      <div class="navi-huelle">
        <ul class="navi-liste">
{self.navigation(aktiv)}
        </ul>
      </div>
    </nav>
  </header>"""

    def brotkrumen(self, datei):
        s = I.SEITEN[datei]
        eltern = None
        for eintrag in I.NAVIGATION:
            for unter in eintrag['unter']:
                if unter['ziel'].split('#')[0] == datei:
                    eltern = eintrag
        teile = ['<li><a href="index.html">Startseite</a></li>']
        if eltern:
            teile.append('<li><a href="%s">%s</a></li>' % (eltern['ziel'], e(eltern['titel'])))
        teile.append('<li aria-current="page">%s</li>' % e(s['h1']))
        return ('    <nav class="brotkrumen" aria-label="Sie sind hier">\n'
                '      <div class="huelle"><ol>%s</ol></div>\n    </nav>\n'
                % ''.join(teile))

    def seitenkopf(self, datei):
        s = I.SEITEN[datei]
        teile = ''
        if s.get('kicker'):
            teile += '          <p class="kicker">%s</p>\n' % e(s['kicker'])
        teile += '          <h1>%s</h1>\n' % e(s['h1'])
        if s.get('einleitung'):
            teile += '          <p class="einleitung">%s</p>\n' % e(s['einleitung'])
        krumen = self.brotkrumen(datei) if datei != '404.html' else ''
        return (krumen + '    <section class="seitenkopf">\n      <div class="huelle">\n'
                '%s      </div>\n    </section>' % teile)

    def hero(self):
        tafeln = []
        for nummer, t in enumerate(TAFELN):
            zuerst = ' fetchpriority="high"' if nummer == 0 else ' loading="lazy"'
            # Eine Seite hat genau eine Hauptüberschrift. Die weiteren Tafeln
            # des Wechslers sind ihr untergeordnet.
            rang = 'h1' if nummer == 0 else 'h2'
            tafeln.append(f"""        <article class="aufmacher-tafel">
          <div class="tafel-text">
            <p class="kicker">{e(t['kicker'])}</p>
            <{rang} class="tafel-titel">{e(t['titel'])}</{rang}>
            <p>{e(t['text'])}</p>
            <p class="schaltflaechen">
              <a class="schaltflaeche stufe-1" href="{t['ziel']}">{e(t['linktext'])}</a>
            </p>
          </div>
          <div class="tafel-bild">
            <img src="{t['bild']}" alt="{e(t['alt'])}" width="{t['breite']}" height="{t['hoehe']}"{zuerst}>
          </div>
        </article>""")
        return ('    <section class="aufmacher" aria-label="Aktuelles im Überblick">\n'
                '      <div class="aufmacher-huelle">\n%s\n      </div>\n    </section>'
                % '\n'.join(tafeln))

    def randspalte(self, seite):
        v = I.VEREIN
        return f"""          <aside class="seitenleiste">
            <div class="leisten-kasten leisten-spenden">
              <h2>Spenden</h2>
              <p>Ihre Spende trägt unsere Bildungs-, Begegnungs- und Hilfsprojekte.</p>
              <p class="leisten-iban">{I.KONTO_VEREIN['iban']}</p>
              <p><a class="schaltflaeche stufe-1" href="spenden.html">Zum Spendenkonto</a></p>
            </div>
            <div class="leisten-kasten">
              <h2>Kontakt</h2>
              <address>
                {e(v['name'])}<br>{e(v['strasse'])}<br>{e(v['ort'])}<br>
                <a href="mailto:{v['email']}">{v['email']}</a>
              </address>
            </div>
          </aside>
"""

    def inhaltsverzeichnis(self, paragrafen):
        teile = '\n'.join('              <li><a href="#%s">%s</a></li>' % (p['id'], e(p['titel']))
                          for p in paragrafen)
        return f"""          <aside class="seitenleiste">
            <nav class="leisten-kasten inhaltsverzeichnis" aria-label="Inhaltsverzeichnis der Satzung">
              <h2>Auf dieser Seite</h2>
              <ol>
{teile}
              </ol>
            </nav>
            <div class="leisten-kasten leisten-spenden">
              <h2>Mitglied werden</h2>
              <p>Die Satzung regelt, wie man Mitglied wird – den Antrag finden Sie hier.</p>
              <p><a class="schaltflaeche stufe-1" href="mitglied-werden.html">Zum Antrag</a></p>
            </div>
          </aside>
"""

    def js_zusatz(self):
        return skripte.WECHSLER

    def js_start(self):
        return '    wechslerEinrichten();'

    # ------------------------------------------------------------- Gestaltung

    def css(self):
        return GRUNDLAGE + """
/* ==========================================================================
   Entwurf 2 – Institut
   Hell, redaktionell, in den Logofarben. Dienstleiste, Wechsler, Seitenleisten.
   ========================================================================== */

:root {
  --gruen-tief:   #093309;
  --gruen:        #0d4a0d;
  --gruen-hell:   #2e6b2e;
  --gruen-blass:  #eaf0e7;
  --schwarz:      #111111;
  --grau:         #4e4e4e;
  --grau-linie:   #dcd8cd;
  --papier:       #f6f5f1;
  --weiss:        #ffffff;
  --fokus:        var(--gruen);

  --huelle-breite:    74rem;
  --rand:             clamp(1.25rem, 4vw, 2.5rem);
  --abstand-abschnitt: clamp(3rem, 6vw, 5rem);
  --abstand-gross:    clamp(2rem, 4vw, 3.25rem);
  --abstand-mittel:   clamp(1.25rem, 2.5vw, 2rem);
  --abstand-klein:    1rem;
  --kopf-polster:     .9rem;
  --logo-hoehe:       3.75rem;

  --serif: 'Source Serif 4', Georgia, 'Times New Roman', serif;
  --sans:  'Source Sans 3', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --arabisch: 'Noto Naskh Arabic', var(--sans);
}

body {
  background: var(--papier);
  color: var(--schwarz);
  font-family: var(--sans);
  font-size: clamp(1rem, .96rem + .22vw, 1.09rem);
  line-height: 1.7;
}
[lang="ar"] { font-family: var(--arabisch); }

/* --------------------------------------------------------- Typografie */

h1, h2, h3 {
  font-family: var(--serif); font-weight: 600; line-height: 1.2;
  color: var(--schwarz); margin: 0 0 .5em;
}
h1 { font-size: clamp(2.1rem, 3.6vw, 3.1rem); }
h2 { font-size: clamp(1.5rem, 2.4vw, 2.1rem); }
h3 { font-size: 1.22rem; }

p { margin: 0 0 1em; max-width: 70ch; }
a { color: var(--gruen); text-underline-offset: .18em; }
a:hover { color: var(--gruen-hell); }

.kicker {
  display: flex; align-items: center; gap: .6rem;
  font-size: .75rem; font-weight: 700; text-transform: uppercase;
  letter-spacing: .12em; color: var(--gruen); margin: 0 0 .9em;
}
.kicker::before {
  content: ''; width: 1.5rem; height: 3px; background: var(--gruen); flex: 0 0 auto;
}

.einleitung { font-size: 1.15em; color: var(--grau); max-width: 62ch; }
.unterzeile { font-family: var(--serif); font-size: 1.2rem; color: var(--gruen); margin-top: -.6em; }
.hinweis { font-size: .9rem; color: var(--grau); }
.hinweis-stark {
  background: var(--gruen-blass); border-left: 4px solid var(--gruen);
  padding: .9rem 1.2rem; color: var(--schwarz);
}
.hervorhebung {
  font-family: var(--serif); font-size: 1.3rem; color: var(--gruen);
  border-left: 4px solid var(--gruen); padding-left: 1.1rem; max-width: 48ch;
}

/* --------------------------------------------------------- Sprungmarke */

.sprungmarke { background: var(--gruen); color: var(--weiss); font-weight: 600; }

/* --------------------------------------------------------- Dienstleiste */

.dienstleiste { background: var(--gruen-tief); color: #e6ece4; font-size: .82rem; }
.dienst-huelle {
  max-width: var(--huelle-breite); margin-inline: auto;
  padding: .45rem var(--rand);
  display: flex; flex-wrap: wrap; gap: .3rem 1.5rem; justify-content: space-between;
}
.dienst-huelle p { margin: 0; max-width: none; }
.dienst-rechts { display: flex; gap: 1.25rem; }
.dienstleiste a { color: #e6ece4; text-decoration: none; }
.dienstleiste a:hover { color: var(--weiss); text-decoration: underline; }
@media (max-width: 640px) { .dienst-ort { display: none; } }

/* --------------------------------------------------------- Kopfbereich */

.kopfbereich { position: static; background: var(--weiss); }
.kopf-huelle { gap: var(--abstand-klein); }
.navi-spende {
  margin-left: auto; background: var(--gruen); color: var(--weiss);
  padding: .6rem 1.3rem; text-decoration: none; font-weight: 600; font-size: .9rem;
  border-radius: 3px;
}
.navi-spende:hover { background: var(--gruen-tief); color: var(--weiss); }

.hauptnavigation {
  position: sticky; top: 0; z-index: 100;
  background: var(--weiss);
  border-top: 1px solid var(--grau-linie);
  border-bottom: 1px solid var(--grau-linie);
}
.navi-huelle { max-width: var(--huelle-breite); margin-inline: auto; padding-inline: var(--rand); }
.navi-liste { gap: 0; }
.navi-punkt { border-right: 1px solid var(--grau-linie); }
.navi-punkt:first-child { border-left: 1px solid var(--grau-linie); }
.navi-punkt > a {
  color: var(--schwarz); padding: .95rem 1.15rem; font-size: .95rem; font-weight: 600;
  border-bottom: 3px solid transparent;
}
.navi-punkt > a:hover { color: var(--gruen); background: var(--gruen-blass); }
.navi-punkt.ist-aktiv > a { color: var(--gruen); border-bottom-color: var(--gruen); }

.untermenue {
  display: none; position: absolute; left: 0; top: 100%; min-width: 19rem;
  background: var(--weiss); border: 1px solid var(--grau-linie);
  border-top: 3px solid var(--gruen);
  box-shadow: 0 14px 30px rgba(0, 0, 0, .12); padding: .35rem 0; z-index: 10;
}
.untermenue a { color: var(--schwarz); padding: .6rem 1.15rem; font-size: .92rem; }
.untermenue a:hover { background: var(--gruen-blass); color: var(--gruen); }

.menue-schalter { color: var(--schwarz); display: none; }
.menue-wort { font-size: .85rem; font-weight: 600; }

@media (max-width: 899px) {
  .menue-schalter { display: flex; }
  .navi-spende { margin-left: auto; }
  /* Auf Telefonen ist die Navigationsleiste eingeklappt. Bliebe der Kopf
     dann unbeweglich, scrollte der Menüknopf mit dem Seitenanfang aus dem
     Bild und wäre von weiter unten nicht mehr erreichbar. */
  .kopfbereich { position: sticky; top: 0; z-index: 100; }
  .hauptnavigation { display: none; }
  .hauptnavigation.ist-offen {
    display: block;
    max-height: calc(100vh - 6rem); overflow-y: auto;
  }
  .navi-liste { flex-direction: column; align-items: stretch; }
  .navi-punkt, .navi-punkt:first-child {
    border: 0; border-bottom: 1px solid var(--grau-linie);
  }
  .navi-punkt > a { border-bottom: 0; padding: .9rem 0; }
  .hat-untermenue { display: grid; grid-template-columns: 1fr auto; align-items: center; }
  .untermenue-schalter { display: block; color: var(--schwarz); }
  .untermenue {
    display: none; position: static; grid-column: 1 / -1; border: 0;
    border-left: 3px solid var(--gruen-blass); box-shadow: none;
    margin: 0 0 .6rem .4rem; min-width: 0;
  }
  .untermenue-offen .untermenue { display: block; }
}

/* --------------------------------------------------------- Aufmacher */

.aufmacher { position: relative; background: var(--weiss); border-bottom: 1px solid var(--grau-linie); }
.aufmacher-huelle { max-width: var(--huelle-breite); margin-inline: auto; position: relative; }
.aufmacher-tafel { display: grid; }
@media (min-width: 900px) {
  .aufmacher-tafel { grid-template-columns: 45% 55%; align-items: stretch; }
}
.tafel-text { padding: clamp(1.75rem, 4vw, 3.25rem) var(--rand); align-self: center; }
.tafel-titel { font-size: clamp(1.7rem, 2.9vw, 2.5rem); }
.tafel-text p { color: var(--grau); }
.tafel-bild img { width: 100%; height: 100%; min-height: 15rem; object-fit: cover; }

/* Ohne JavaScript stehen alle drei Tafeln schlicht untereinander.
   Erst wenn das Skript den Wechsler aufgebaut hat, wird eine davon gezeigt. */
.aufmacher.ist-bereit .aufmacher-tafel { display: none; }
.aufmacher.ist-bereit .aufmacher-tafel.ist-sichtbar { display: block; }
@media (min-width: 900px) {
  .aufmacher.ist-bereit .aufmacher-tafel.ist-sichtbar { display: grid; }
}

.aufmacher-pfeil {
  position: absolute; top: 50%; transform: translateY(-50%); z-index: 5;
  background: rgba(255, 255, 255, .92); border: 1px solid var(--grau-linie);
  color: var(--gruen); font-size: 1.8rem; line-height: 1;
  width: 2.75rem; height: 2.75rem; border-radius: 50%;
}
.aufmacher-pfeil:hover { background: var(--gruen); color: var(--weiss); }
.aufmacher-zurueck { left: .6rem; }
.aufmacher-weiter { right: .6rem; }

.aufmacher-punkte {
  position: absolute; bottom: .9rem; left: 50%; transform: translateX(-50%);
  display: flex; gap: .5rem; z-index: 5;
}
.aufmacher-punkte button {
  width: .7rem; height: .7rem; border-radius: 50%; padding: 0;
  border: 1px solid var(--gruen); background: rgba(255, 255, 255, .85);
}
.aufmacher-punkte button[aria-current="true"] { background: var(--gruen); }

/* --------------------------------------------------------- Abschnitte */

.abschnitt-hell { background: var(--weiss); }
.abschnitt-zitat { background: var(--gruen-blass); }
.abschnitt-aufruf { background: var(--gruen); color: var(--weiss); }
.abschnitt-text { background: var(--weiss); }

.brotkrumen { background: var(--papier); border-bottom: 1px solid var(--grau-linie); }
.brotkrumen ol {
  list-style: none; display: flex; flex-wrap: wrap; gap: .5rem;
  padding-block: .65rem; font-size: .85rem; color: var(--grau);
}
.brotkrumen li + li::before { content: '›'; margin-right: .5rem; color: var(--grau); }
.brotkrumen a { text-decoration: none; }

.seitenkopf { background: var(--papier); padding-block: clamp(2rem, 5vw, 3.5rem) clamp(1.5rem, 3vw, 2.25rem); }

/* --------------------------------------------------------- Schaltflächen */

.schaltflaeche { padding: .7rem 1.4rem; border-radius: 3px; font-weight: 600; font-size: .95rem; }
.stufe-1 { background: var(--gruen); color: var(--weiss); border: 1px solid var(--gruen); }
.stufe-1:hover { background: var(--gruen-tief); border-color: var(--gruen-tief); color: var(--weiss); }
.stufe-2 { background: var(--weiss); color: var(--gruen); border: 1px solid var(--grau-linie); }
.stufe-2:hover { border-color: var(--gruen); background: var(--gruen-blass); }
.abschnitt-aufruf .stufe-2 { background: transparent; color: var(--weiss); border-color: rgba(255, 255, 255, .6); }
.abschnitt-aufruf .stufe-2:hover { background: rgba(255, 255, 255, .14); color: var(--weiss); }
.abschnitt-aufruf .stufe-1 { background: var(--weiss); color: var(--gruen); border-color: var(--weiss); }
.abschnitt-aufruf .stufe-1:hover { background: var(--gruen-blass); color: var(--gruen-tief); }

/* --------------------------------------------------------- Karten */

.karte {
  background: var(--weiss); border: 1px solid var(--grau-linie);
  display: flex; flex-direction: column; overflow: hidden;
  transition: border-color .18s ease, box-shadow .18s ease;
}
.karte:hover { border-color: var(--gruen); box-shadow: 0 10px 24px rgba(0, 0, 0, .08); }
.karte-bild { width: 100%; aspect-ratio: 3 / 2; object-fit: cover; }
.karte-titel { font-size: 1.3rem; padding: var(--abstand-klein) var(--abstand-klein) 0; margin-bottom: .3em; }
.karte-text { color: var(--grau); padding-inline: var(--abstand-klein); margin-bottom: 1em; }
.karte-verweis {
  margin-top: auto; padding: 0 var(--abstand-klein) var(--abstand-klein);
  font-weight: 600; font-size: .92rem; text-decoration: none;
}

/* --------------------------------------------------------- Bilder */

.bild img, .reihe-bild img { border: 1px solid var(--grau-linie); }
.bild figcaption, .reihe-bild figcaption {
  font-size: .85rem; color: var(--grau); margin-top: .5rem;
  border-left: 3px solid var(--gruen-blass); padding-left: .7rem;
}

/* --------------------------------------------------------- Zitat */

.zitat { max-width: 52rem; border-left: 4px solid var(--gruen); padding-left: clamp(1rem, 3vw, 2rem); }
.zitat blockquote { margin: 0; }
.zitat p { font-family: var(--serif); font-size: clamp(1.2rem, 2vw, 1.6rem); line-height: 1.5; max-width: none; }
.zitat figcaption { color: var(--grau); font-size: .9rem; }

/* --------------------------------------------------------- Listen */

.nummer {
  font-family: var(--serif); font-size: 1.7rem; font-weight: 600;
  color: var(--gruen); line-height: 1.1; min-width: 2.2rem;
}
.nummer-punkt { padding-bottom: var(--abstand-klein); border-bottom: 1px solid var(--grau-linie); }
.nummer-punkt h3 { margin-bottom: .2em; }
.nummer-punkt p { color: var(--grau); margin: 0; }

/* --------------------------------------------------------- Personen */

.person { background: var(--weiss); border: 1px solid var(--grau-linie); padding-bottom: var(--abstand-klein); }
.person-name { font-size: 1.15rem; margin: .9rem var(--abstand-klein) .1em; }
.person-rolle { color: var(--gruen); font-size: .9rem; font-weight: 600; margin: 0 var(--abstand-klein) .1em; }
.person-zusatz { color: var(--grau); font-size: .85rem; margin: 0 var(--abstand-klein); }
.person-initialen { background: var(--gruen-blass); color: var(--gruen); font-family: var(--serif); }

/* --------------------------------------------------------- Konto */

.konto {
  background: var(--gruen-blass); border: 1px solid #cfe0cb;
  padding: var(--abstand-mittel); margin-bottom: var(--abstand-klein);
}
.konto-titel { font-size: 1.1rem; color: var(--gruen); }
.konto-daten dt { color: var(--grau); font-weight: 600; font-size: .9rem; }
.konto-daten dd { color: var(--schwarz); }
.iban-kopieren {
  margin-left: .6rem; background: var(--weiss); color: var(--gruen);
  border: 1px solid var(--gruen); border-radius: 3px; padding: .2rem .6rem; font-size: .78rem;
}
.iban-kopieren:hover { background: var(--gruen); color: var(--weiss); }
.iban-kopieren.ist-kopiert { background: var(--gruen); color: var(--weiss); }

/* --------------------------------------------------------- Downloads */

.download { background: var(--weiss); border: 1px solid var(--grau-linie); padding: .85rem 1.1rem; color: var(--schwarz); }
.download:hover { border-color: var(--gruen); background: var(--gruen-blass); }
.download-art {
  font-size: .72rem; font-weight: 700; letter-spacing: .08em;
  background: var(--gruen); color: var(--weiss); padding: .2rem .55rem; border-radius: 3px; flex: 0 0 auto;
}

/* --------------------------------------------------------- Aufruf */

.aufruf { text-align: center; }
.abschnitt-aufruf h2, .abschnitt-aufruf p { color: var(--weiss); }
.aufruf p { margin-inline: auto; }
.aufruf .schaltflaechen { justify-content: center; }

/* --------------------------------------------------------- Textbereich */

.textbereich { display: grid; gap: var(--abstand-gross); }
@media (min-width: 1100px) {
  .textbereich { grid-template-columns: minmax(0, 1fr) 19rem; }
  .seitenleiste { order: 2; position: sticky; top: 5rem; align-self: start; }
  .textspalte { order: 1; }
}
.seitenleiste { display: grid; gap: var(--abstand-klein); align-content: start; }
.leisten-kasten { background: var(--papier); border: 1px solid var(--grau-linie); padding: var(--abstand-klein); }
.leisten-kasten h2 { font-size: 1.05rem; margin-bottom: .5em; }
.leisten-kasten p, .leisten-kasten address { font-size: .92rem; color: var(--grau); }
.leisten-spenden { background: var(--gruen-blass); border-color: #cfe0cb; }
.leisten-kasten .leisten-iban {
  font-variant-numeric: tabular-nums; font-size: .88rem; color: var(--schwarz);
  letter-spacing: .02em;
}
.inhaltsverzeichnis ol { list-style: none; display: grid; gap: .35rem; font-size: .9rem; }
.inhaltsverzeichnis a { text-decoration: none; }
.inhaltsverzeichnis a:hover { text-decoration: underline; }

.textspalte { max-width: 70ch; }
.paragraf { margin-bottom: var(--abstand-gross); }
.paragraf h2 { font-size: clamp(1.35rem, 2vw, 1.75rem); padding-top: .3em; border-bottom: 1px solid var(--grau-linie); padding-bottom: .3em; }
.satzung-punkte { list-style: decimal; padding-left: 1.5rem; display: grid; gap: .6rem; }
.satzung-unterpunkte { list-style: disc; padding-left: 1.5rem; display: grid; gap: .45rem; margin: .5rem 0; }

/* --------------------------------------------------------- Formular */

.formular-block { max-width: 52rem; }
.formfeld input, .formfeld select, .formfeld textarea {
  background: var(--weiss); color: var(--schwarz);
  border: 1px solid var(--grau-linie); border-radius: 3px;
}
.formfeld input:focus, .formfeld select:focus, .formfeld textarea:focus {
  border-color: var(--gruen); outline: none; box-shadow: 0 0 0 3px rgba(13, 74, 13, .15);
}
.formfeld label { font-size: .93rem; }
.pflicht { color: var(--gruen); }
.feldfehler { color: #a3231a; }
.hat-fehler input, .hat-fehler select, .hat-fehler textarea { border-color: #a3231a; }
.formular-meldung { padding: .85rem 1.1rem; border-left: 4px solid var(--gruen); background: var(--gruen-blass); }
.meldung-fehler { border-left-color: #a3231a; background: #fbeceb; }
.formfeld-haken label { font-size: .92rem; color: var(--grau); }

/* --------------------------------------------------------- Anschrift */

.anschrift { font-size: 1.05rem; line-height: 1.85; }

/* --------------------------------------------------------- Lichtkasten */

.lichtkasten { background: rgba(9, 51, 9, .96); }
.lichtkasten button { color: var(--weiss); }
.lichtkasten-zurueck, .lichtkasten-weiter { font-size: 2.4rem; padding: .3rem .8rem; }
.lichtkasten-schliessen {
  font-size: .9rem; font-weight: 600; border: 1px solid rgba(255, 255, 255, .5);
  padding: .5rem 1rem; border-radius: 3px;
}
.lichtkasten-zaehler { color: #cfe0cb; font-size: .88rem; }

/* --------------------------------------------------------- Fußbereich */

.fussbereich { background: var(--gruen-tief); color: #d8e2d5; }
.fuss-titel {
  font-family: var(--sans); font-size: .78rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: .12em; color: var(--weiss); margin-bottom: .9rem;
}
.fussbereich p, .fussbereich address, .fussbereich a { color: #d8e2d5; font-size: .92rem; }
.fussbereich a:hover { color: var(--weiss); text-decoration: underline; }
.fussbereich .fuss-claim { font-family: var(--serif); font-size: 1.2rem; color: var(--weiss); margin: .8rem 0 .5rem; }
.fuss-zeile { border-top: 1px solid rgba(255, 255, 255, .18); }
.fuss-zeile p { font-size: .85rem; }
"""
