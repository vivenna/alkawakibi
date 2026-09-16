# -*- coding: utf-8 -*-
"""Entwurf 1 – „Petrol & Gold“.

Durchgehend dunkler Auftritt in tiefem Petrol mit sparsamem Goldakzent und
Serifen-Überschriften. Umsetzung des vom Vorstand genannten Farbvorbilds.
"""
import inhalte as I
from basis import e
from css_basis import GRUNDLAGE
from entwurf_basis import Entwurf


class PetrolGold(Entwurf):
    kennung = 'entwurf-1-petrol-gold'
    name = 'Petrol & Gold'
    schriften = ['cormorant-garamond', 'inter', 'noto-naskh-arabic']
    logo = 'assets/bilder/logo-weiss-gold.png'
    logo_fuss = 'assets/bilder/logo-weiss.png'
    farbe_browser = '#071f1e'

    # ------------------------------------------------------------- Struktur

    def hero(self):
        h = I.HERO
        titel = e(h['titel']).replace(
            e(h['hervor']), '<span class="hervor">%s</span>' % e(h['hervor']))
        return f"""    <section class="hero">
      <img class="hero-bild" src="{h['bild']}" alt="{e(h['alt'])}" width="{h['breite']}" height="{h['hoehe']}" fetchpriority="high">
      <div class="hero-schleier" aria-hidden="true"></div>
      <div class="hero-inhalt">
        <div class="huelle">
          <p class="hero-dachzeile">{e(h['dachzeile'])}</p>
          <h1>{titel}</h1>
          <p class="hero-text">{e(h['text'])}</p>
          <p class="schaltflaechen">
            <a class="schaltflaeche stufe-1" href="aktivitaeten.html">Unsere Aktivitäten</a>
            <a class="schaltflaeche stufe-2" href="spenden.html">Jetzt spenden</a>
          </p>
        </div>
      </div>
    </section>"""

    def seitenkopf(self, datei):
        s = I.SEITEN[datei]
        teile = ''
        if s.get('kicker'):
            teile += '          <p class="kicker">%s</p>\n' % e(s['kicker'])
        teile += '          <h1>%s</h1>\n' % e(s['h1'])
        teile += '          <span class="goldlinie" aria-hidden="true"></span>\n'
        if s.get('einleitung'):
            teile += '          <p class="einleitung">%s</p>\n' % e(s['einleitung'])
        return ('    <section class="seitenkopf">\n      <div class="huelle">\n'
                '%s      </div>\n    </section>' % teile)

    # ------------------------------------------------------------- Gestaltung

    def css(self):
        return GRUNDLAGE + """
/* ==========================================================================
   Entwurf 1 – Petrol & Gold
   Durchgehend dunkel. Kein heller Abschnitt, keine helle Karte.
   ========================================================================== */

:root {
  /* Farben */
  --petrol-tief:      #071f1e;
  --petrol:           #0b2e2c;
  --petrol-hell:      #103b38;
  --petrol-linie:     #1c4f4a;
  --gold:             #c9a227;
  --gold-hell:        #e3c766;
  --creme:            #f3efe4;
  --creme-gedaempft:  #afc2bf;
  --weiss:            #ffffff;
  --fokus:            var(--gold-hell);

  /* Maße */
  --huelle-breite:    72rem;
  --rand:             clamp(1.25rem, 5vw, 3rem);
  --abstand-abschnitt: clamp(3.5rem, 8vw, 6.5rem);
  --abstand-gross:    clamp(2.5rem, 5vw, 4rem);
  --abstand-mittel:   clamp(1.5rem, 3vw, 2.25rem);
  --abstand-klein:    1rem;
  --kopf-polster:     1rem;
  --logo-hoehe:       3.25rem;

  /* Schriften */
  --serif: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
  --sans:  'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --arabisch: 'Noto Naskh Arabic', var(--sans);
}

body {
  background: var(--petrol);
  color: var(--creme);
  font-family: var(--sans);
  font-size: clamp(1rem, .95rem + .3vw, 1.125rem);
  line-height: 1.75;
}

[lang="ar"] { font-family: var(--arabisch); }

/* --------------------------------------------------------- Typografie */

h1, h2, h3 {
  font-family: var(--serif);
  font-weight: 600;
  line-height: 1.08;
  letter-spacing: -.01em;
  color: var(--weiss);
  margin: 0 0 .5em;
}
h1 { font-size: clamp(2.6rem, 6vw, 5rem); }
h2 { font-size: clamp(1.9rem, 3.6vw, 3rem); }
h3 { font-size: clamp(1.25rem, 1.8vw, 1.5rem); line-height: 1.25; }

p { margin: 0 0 1.1em; max-width: 68ch; }
a { color: var(--gold-hell); text-underline-offset: .2em; }
a:hover { color: var(--gold); }

.hervor { color: var(--gold-hell); }

.kicker {
  font-family: var(--sans);
  font-size: .75rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .18em;
  color: var(--gold);
  margin: 0 0 1em;
}

.einleitung { font-size: 1.2em; color: var(--creme); max-width: 60ch; }
.unterzeile {
  font-family: var(--serif); font-size: 1.35rem; font-style: italic;
  color: var(--creme-gedaempft); margin-top: -.6em;
}
.hinweis { font-size: .92rem; color: var(--creme-gedaempft); }
.hinweis-stark {
  border-left: 2px solid var(--gold);
  padding: .8rem 1.1rem; background: var(--petrol-hell); color: var(--creme);
}
.hervorhebung {
  font-family: var(--serif); font-size: 1.5rem; font-style: italic;
  color: var(--gold-hell); max-width: 44ch; margin-top: 1.5em;
}

.goldlinie {
  display: block; width: 4rem; height: 1px;
  background: var(--gold); opacity: .55; margin: 1.6rem 0;
}

/* --------------------------------------------------------- Sprungmarke */

.sprungmarke {
  background: var(--gold); color: var(--petrol-tief); font-weight: 600;
}

/* --------------------------------------------------------- Kopfbereich */

.kopfbereich {
  background: transparent;
  border-bottom: 1px solid transparent;
  transition: background .25s ease, border-color .25s ease, padding .25s ease;
}
.kopfbereich.ist-gescrollt {
  background: var(--petrol-tief);
  border-bottom-color: rgba(201, 162, 39, .3);
}
/* Auf Unterseiten liegt kein Bild hinter dem Kopf */
.seite:not(.seite-index) .kopfbereich { background: var(--petrol-tief); }

.hauptnavigation {
  margin-left: auto; display: flex; align-items: center; gap: var(--abstand-klein);
}
.navi-liste { gap: 1.6rem; }
.navi-punkt > a {
  color: var(--creme); font-size: .95rem; padding: .5rem 0;
  border-bottom: 1px solid transparent;
}
.navi-punkt > a:hover { color: var(--gold-hell); }
.navi-punkt.ist-aktiv > a { color: var(--gold-hell); border-bottom-color: var(--gold); }

.untermenue {
  display: none; position: absolute; left: -1rem; top: 100%;
  min-width: 17rem; padding: .5rem 0;
  background: var(--petrol-tief);
  border-top: 2px solid var(--gold);
  box-shadow: 0 18px 40px rgba(0, 0, 0, .45);
}
.untermenue a { color: var(--creme); padding: .6rem 1.2rem; font-size: .92rem; }
.untermenue a:hover { background: var(--petrol-hell); color: var(--gold-hell); }

.navi-spende {
  background: var(--gold); color: var(--petrol-tief);
  padding: .65rem 1.35rem; text-decoration: none;
  font-size: .8rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .12em;
  border-radius: 2px; transition: background .2s ease;
}
.navi-spende:hover { background: var(--gold-hell); color: var(--petrol-tief); }

.menue-schalter { color: var(--creme); margin-left: auto; }
.menue-wort { font-size: .78rem; text-transform: uppercase; letter-spacing: .14em; }

@media (max-width: 899px) {
  .menue-schalter { display: flex; }
  .hauptnavigation {
    position: fixed; inset: 0 0 0 auto; width: min(22rem, 88vw);
    background: var(--petrol-tief);
    border-left: 1px solid var(--petrol-linie);
    flex-direction: column; align-items: stretch; justify-content: flex-start;
    gap: 0; padding: 5.5rem 1.75rem 2rem;
    transform: translateX(100%); transition: transform .28s ease;
    overflow-y: auto;
  }
  .hauptnavigation.ist-offen { transform: translateX(0); }
  .navi-liste { flex-direction: column; align-items: stretch; gap: 0; }
  .navi-punkt { border-bottom: 1px solid var(--petrol-linie); }
  .navi-punkt > a { padding: .9rem 0; font-size: 1.05rem; }
  .hat-untermenue { display: grid; grid-template-columns: 1fr auto; align-items: center; }
  .untermenue-schalter { display: block; color: var(--creme); }
  .untermenue {
    display: none; position: static; grid-column: 1 / -1;
    box-shadow: none; border-top: 0; padding: 0 0 .6rem 1rem; min-width: 0;
    background: transparent;
  }
  .untermenue-offen .untermenue { display: block; }
  .navi-spende { margin-top: 1.5rem; text-align: center; }
  body.menue-offen { overflow: hidden; }
}

/* --------------------------------------------------------- Hero */

.hero { position: relative; display: grid; min-height: min(88vh, 760px); }
.hero > * { grid-area: 1 / 1; }
.hero-bild { width: 100%; height: 100%; object-fit: cover; filter: saturate(.8); }
.hero-schleier {
  background:
    linear-gradient(to bottom, rgba(7, 31, 30, .35) 0%, rgba(7, 31, 30, .75) 55%, rgba(7, 31, 30, .97) 100%),
    linear-gradient(to right, var(--petrol-tief) 0%, rgba(7, 31, 30, .25) 65%, rgba(7, 31, 30, 0) 100%);
}
.hero-inhalt { align-self: end; padding-block: clamp(3rem, 9vw, 6rem); position: relative; }
.hero-dachzeile {
  font-size: .78rem; font-weight: 600; text-transform: uppercase;
  letter-spacing: .2em; color: var(--gold); margin-bottom: 1.2rem;
}
.hero h1 { max-width: 18ch; margin-bottom: .35em; }
.hero-text { font-size: 1.2em; max-width: 52ch; color: var(--creme); }

/* --------------------------------------------------------- Abschnitte */

.abschnitt-hell { background: var(--petrol-hell); }
.abschnitt-zitat { background: var(--petrol-hell); text-align: center; }
.abschnitt-aufruf { background: var(--petrol-tief); }
.abschnitt-text { background: var(--petrol); }

.seitenkopf {
  background: var(--petrol-tief);
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2rem, 5vw, 3.5rem);
}
.seitenkopf h1 { max-width: 20ch; }

/* --------------------------------------------------------- Schaltflächen */

.schaltflaeche {
  padding: .85rem 1.7rem; border-radius: 2px;
  font-size: .8rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .12em;
  transition: background .2s ease, color .2s ease, border-color .2s ease;
}
.stufe-1 { background: var(--gold); color: var(--petrol-tief); border: 1px solid var(--gold); }
.stufe-1:hover { background: var(--gold-hell); border-color: var(--gold-hell); color: var(--petrol-tief); }
.stufe-2 { background: transparent; color: var(--gold-hell); border: 1px solid rgba(201, 162, 39, .6); }
.stufe-2:hover { background: rgba(201, 162, 39, .12); border-color: var(--gold); color: var(--gold-hell); }

/* --------------------------------------------------------- Karten */

.karte {
  background: var(--petrol-hell);
  border: 1px solid var(--petrol-linie);
  border-top: 2px solid var(--gold);
  border-radius: 2px;
  padding: var(--abstand-mittel);
  display: flex; flex-direction: column; gap: .35rem;
  transition: transform .22s ease, border-top-color .22s ease, box-shadow .22s ease;
}
.karte:hover {
  transform: translateY(-4px);
  border-top-color: var(--gold-hell);
  box-shadow: 0 16px 34px rgba(0, 0, 0, .35);
}
.abschnitt-hell .karte { background: var(--petrol); }
.karte-bild {
  width: calc(100% + 2 * var(--abstand-mittel));
  margin: calc(-1 * var(--abstand-mittel)) calc(-1 * var(--abstand-mittel)) var(--abstand-klein);
  aspect-ratio: 3 / 2; object-fit: cover;
  filter: saturate(.85) brightness(.9); transition: filter .25s ease;
}
.karte:hover .karte-bild { filter: none; }
.karte-titel { font-size: 1.35rem; margin-bottom: .2em; }
.karte-text { color: var(--creme-gedaempft); margin-bottom: .6em; }
.karte-verweis {
  margin-top: auto; font-size: .78rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .12em; text-decoration: none;
}

/* --------------------------------------------------------- Bilder */

.bild img, .reihe-bild img, .galerie img, .person-bild img {
  filter: saturate(.85); transition: filter .3s ease;
  border-radius: 2px;
}
.bild:hover img, .reihe-bild:hover img, .galerie a:hover img { filter: none; }
.bild figcaption, .reihe-bild figcaption {
  font-size: .85rem; color: var(--creme-gedaempft); margin-top: .6rem;
}
.spalte-bild .bild img { box-shadow: 0 20px 50px rgba(0, 0, 0, .4); }

/* --------------------------------------------------------- Zitat */

.zitat { position: relative; max-width: 46rem; margin-inline: auto; padding-top: 2rem; }
.zitat::before {
  content: '“'; position: absolute; top: -1.4rem; left: 50%; transform: translateX(-50%);
  font-family: var(--serif); font-size: 6rem; line-height: 1;
  color: var(--gold); opacity: .35;
}
.zitat blockquote { margin: 0; }
.zitat p {
  font-family: var(--serif); font-style: italic;
  font-size: clamp(1.4rem, 2.6vw, 2.1rem); line-height: 1.4;
  color: var(--weiss); max-width: none;
}
.zitat figcaption {
  font-size: .78rem; text-transform: uppercase; letter-spacing: .16em;
  color: var(--gold); margin-top: 1.4rem;
}

/* --------------------------------------------------------- Listen */

.nummer { font-family: var(--serif); font-size: 2rem; color: var(--gold); line-height: 1; }
.nummer-punkt h3 { margin-bottom: .25em; }
.nummer-punkt p { color: var(--creme-gedaempft); margin: 0; }

/* --------------------------------------------------------- Personen */

.person-name { font-size: 1.2rem; margin: .9rem 0 .1em; }
.person-rolle { color: var(--gold-hell); font-size: .9rem; margin: 0 0 .1em; }
.person-zusatz { color: var(--creme-gedaempft); font-size: .85rem; margin: 0; }
.person-initialen {
  background: var(--petrol-hell); border: 1px solid var(--petrol-linie);
  color: var(--gold); font-family: var(--serif);
}

/* --------------------------------------------------------- Konto */

.konto {
  background: var(--petrol-hell); border: 1px solid var(--petrol-linie);
  border-left: 2px solid var(--gold);
  padding: var(--abstand-mittel); margin-bottom: var(--abstand-klein);
}
.abschnitt-hell .konto, .abschnitt-aufruf .konto { background: var(--petrol); }
.konto-titel { font-size: 1.15rem; color: var(--gold-hell); }
.konto-daten dt { color: var(--creme-gedaempft); font-weight: 400; font-size: .9rem; }
.iban-kopieren {
  margin-left: .6rem; background: transparent; color: var(--gold-hell);
  border: 1px solid rgba(201, 162, 39, .5); border-radius: 2px;
  padding: .2rem .6rem; font-size: .75rem;
}
.iban-kopieren:hover { background: rgba(201, 162, 39, .14); }
.iban-kopieren.ist-kopiert { background: var(--gold); color: var(--petrol-tief); }

/* --------------------------------------------------------- Downloads */

.download {
  background: var(--petrol-hell); border: 1px solid var(--petrol-linie);
  padding: .9rem 1.2rem; color: var(--creme); transition: border-color .2s ease;
}
.download:hover { border-color: var(--gold); }
.download-art {
  font-size: .7rem; font-weight: 600; letter-spacing: .12em;
  color: var(--petrol-tief); background: var(--gold);
  padding: .2rem .5rem; border-radius: 2px; flex: 0 0 auto;
}

/* --------------------------------------------------------- Aufruf */

.aufruf {
  border: 1px solid rgba(201, 162, 39, .45);
  padding: var(--abstand-gross); text-align: center;
}
.aufruf p { margin-inline: auto; }
.aufruf .schaltflaechen { justify-content: center; }

/* --------------------------------------------------------- Satzung */

.inhaltsverzeichnis {
  background: var(--petrol-hell); border: 1px solid var(--petrol-linie);
  padding: var(--abstand-mittel); margin-bottom: var(--abstand-gross);
}
.inhaltsverzeichnis h2 { font-size: 1.3rem; }
.inhaltsverzeichnis ol { list-style: none; columns: 2; column-gap: 2rem; }
@media (max-width: 640px) { .inhaltsverzeichnis ol { columns: 1; } }
.inhaltsverzeichnis li { margin-bottom: .4rem; break-inside: avoid; }
.inhaltsverzeichnis a { font-size: .95rem; }

.paragraf { margin-bottom: var(--abstand-gross); max-width: 68ch; }
.paragraf h2 { font-size: clamp(1.5rem, 2.4vw, 2rem); padding-top: .4em; }
.satzung-punkte { list-style: decimal; padding-left: 1.6rem; display: grid; gap: .7rem; }
.satzung-unterpunkte { list-style: disc; padding-left: 1.6rem; display: grid; gap: .5rem; margin: .6rem 0; }
.paragraf li { color: var(--creme); }

/* --------------------------------------------------------- Formular */

.formular-block { max-width: 52rem; }
.formfeld input, .formfeld select, .formfeld textarea {
  background: var(--petrol-tief); color: var(--creme);
  border: 1px solid var(--petrol-linie); border-radius: 2px;
}
.formfeld input:focus, .formfeld select:focus, .formfeld textarea:focus {
  border-color: var(--gold); outline: none;
  box-shadow: 0 0 0 3px rgba(201, 162, 39, .25);
}
.formfeld label { font-size: .9rem; }
.pflicht { color: var(--gold); }
.feldfehler { color: #ffb4a2; }
.hat-fehler input, .hat-fehler select, .hat-fehler textarea { border-color: #ff8f78; }
.formular-meldung { padding: .9rem 1.1rem; border-left: 2px solid var(--gold); background: var(--petrol-tief); }
.meldung-erfolg { border-left-color: #7fbf7f; }
.meldung-fehler { border-left-color: #ff8f78; }
.formfeld-haken label { font-size: .92rem; color: var(--creme-gedaempft); }

/* --------------------------------------------------------- Anschrift */

.anschrift { font-size: 1.05rem; line-height: 1.9; }

/* --------------------------------------------------------- Lichtkasten */

.lichtkasten { background: rgba(7, 31, 30, .96); }
.lichtkasten button { color: var(--creme); }
.lichtkasten button:hover { color: var(--gold-hell); }
.lichtkasten-zurueck, .lichtkasten-weiter { font-size: 2.4rem; padding: .3rem .8rem; }
.lichtkasten-schliessen {
  font-size: .78rem; text-transform: uppercase; letter-spacing: .14em;
  border: 1px solid rgba(201, 162, 39, .5); padding: .5rem 1rem;
}
.lichtkasten-zaehler { color: var(--creme-gedaempft); font-size: .85rem; }

/* --------------------------------------------------------- Fußbereich */

.fussbereich { background: var(--petrol-tief); border-top: 1px solid rgba(201, 162, 39, .3); }
.fuss-titel {
  font-family: var(--sans); font-size: .75rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .16em; color: var(--gold);
  margin-bottom: 1rem;
}
.fussbereich p, .fussbereich address, .fussbereich a { color: var(--creme-gedaempft); font-size: .92rem; }
.fussbereich a:hover { color: var(--gold-hell); }
.fussbereich .fuss-claim {
  font-family: var(--serif); font-size: 1.25rem; font-style: italic;
  color: var(--gold-hell); margin: .8rem 0 .5rem;
}
.fuss-zeile { border-top: 1px solid var(--petrol-linie); font-size: .85rem; }
.fuss-zeile p { margin: 0; font-size: .85rem; }
"""
