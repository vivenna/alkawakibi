# -*- coding: utf-8 -*-
"""Entwurf 4 – „Smaragd“.

Dieselbe Anlage wie Entwurf 1 – durchgehend dunkel, Serifen-Überschriften,
ruhige Abschnittsfolge –, aber in den Logofarben: Grün von tief bis hell.
Statt des Goldakzents trägt hier ein Verlauf von Smaragd nach Mint die
Hervorhebungen; Flächen, Linien und Schaltflächen sind weich abgestuft.
"""
import inhalte as I
from basis import e
from css_basis import GRUNDLAGE
from entwurf_basis import Entwurf


class Smaragd(Entwurf):
    kennung = 'entwurf-4-smaragd'
    name = 'Smaragd'
    schriften = ['cormorant-garamond', 'inter', 'noto-naskh-arabic']
    logo = 'assets/bilder/logo-weiss.png'
    logo_fuss = 'assets/bilder/logo-weiss.png'
    farbe_browser = '#04170f'

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
      <div class="hero-saum" aria-hidden="true"></div>
    </section>"""

    def seitenkopf(self, datei):
        s = I.SEITEN[datei]
        teile = ''
        if s.get('kicker'):
            teile += '          <p class="kicker">%s</p>\n' % e(s['kicker'])
        teile += '          <h1>%s</h1>\n' % e(s['h1'])
        teile += '          <span class="zierlinie" aria-hidden="true"></span>\n'
        if s.get('einleitung'):
            teile += '          <p class="einleitung">%s</p>\n' % e(s['einleitung'])
        return ('    <section class="seitenkopf">\n      <div class="huelle">\n'
                '%s      </div>\n    </section>' % teile)

    # ------------------------------------------------------------- Gestaltung

    def css(self):
        return GRUNDLAGE + """
/* ==========================================================================
   Entwurf 4 – Smaragd
   Durchgehend dunkel wie Entwurf 1, aber ganz in Grün: die Abstufungen
   tragen die Gliederung, ein Verlauf von Smaragd nach Mint die Akzente.
   ========================================================================== */

:root {
  /* Farben */
  --gruen-nacht:      #04170f;
  --gruen-tief:       #072a1d;
  --gruen:            #0b3827;
  --gruen-hell:       #114a34;
  --gruen-linie:      #1d6449;
  --smaragd:          #1f9d6b;
  --mint:             #6fe0ab;
  --mint-hell:        #a9f0ce;
  --creme:            #edf6f1;
  --creme-gedaempft:  #a7c7b7;
  --weiss:            #ffffff;
  --fokus:            var(--mint);

  /* Verläufe */
  --verlauf-akzent:   linear-gradient(100deg, var(--mint-hell) 0%, var(--mint) 38%, var(--smaragd) 100%);
  --verlauf-flaeche:  linear-gradient(168deg, var(--gruen-hell) 0%, var(--gruen) 58%, var(--gruen-tief) 100%);
  --verlauf-tief:     linear-gradient(168deg, var(--gruen-tief) 0%, var(--gruen-nacht) 100%);
  --verlauf-linie:    linear-gradient(90deg, var(--mint) 0%, var(--smaragd) 45%, rgba(31, 157, 107, 0) 100%);
  --verlauf-kante:    linear-gradient(90deg, rgba(111, 224, 171, 0) 0%, var(--smaragd) 30%, var(--mint) 70%, rgba(111, 224, 171, 0) 100%);

  /* Maße */
  --huelle-breite:    72rem;
  --rand:             clamp(1.25rem, 5vw, 3rem);
  --abstand-abschnitt: clamp(3.5rem, 8vw, 6.5rem);
  --abstand-gross:    clamp(2.5rem, 5vw, 4rem);
  --abstand-mittel:   clamp(1.5rem, 3vw, 2.25rem);
  --abstand-klein:    1rem;
  --kopf-polster:     1rem;
  --logo-hoehe:       3.25rem;
  --rundung:          6px;

  /* Schriften */
  --serif: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
  --sans:  'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --arabisch: 'Noto Naskh Arabic', var(--sans);
}

body {
  background-color: var(--gruen);
  background-image:
    radial-gradient(60rem 40rem at 82% -8%, rgba(31, 157, 107, .20), transparent 65%),
    radial-gradient(48rem 38rem at 0% 42%, rgba(17, 74, 52, .55), transparent 60%);
  background-attachment: fixed;
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
a { color: var(--mint); text-underline-offset: .2em; }
a:hover { color: var(--mint-hell); }

/* Hervorhebung im Fließtext: Verlauf direkt in der Schrift */
.hervor {
  background: var(--verlauf-akzent);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  /* Rückfall, falls der Browser den Verlauf nicht in die Schrift legt */
  -webkit-text-fill-color: transparent;
}
@supports not (background-clip: text) {
  .hervor { color: var(--mint); -webkit-text-fill-color: currentColor; }
}

.kicker {
  font-family: var(--sans);
  font-size: .75rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .18em;
  color: var(--mint);
  margin: 0 0 1em;
}

.einleitung { font-size: 1.2em; color: var(--creme); max-width: 60ch; }
.unterzeile {
  font-family: var(--serif); font-size: 1.35rem; font-style: italic;
  color: var(--creme-gedaempft); margin-top: -.6em;
}
.hinweis { font-size: .92rem; color: var(--creme-gedaempft); }
.hinweis-stark {
  border-left: 2px solid transparent;
  border-image: var(--verlauf-akzent) 1;
  padding: .8rem 1.1rem;
  background: linear-gradient(90deg, rgba(31, 157, 107, .16), rgba(31, 157, 107, 0) 70%);
  color: var(--creme);
}
.hervorhebung {
  font-family: var(--serif); font-size: 1.5rem; font-style: italic;
  color: var(--mint); max-width: 44ch; margin-top: 1.5em;
}

.zierlinie {
  display: block; width: 5.5rem; height: 2px;
  background: var(--verlauf-linie); border-radius: 2px;
  margin: 1.6rem 0;
}

/* --------------------------------------------------------- Sprungmarke */

.sprungmarke {
  background: var(--verlauf-akzent); color: var(--gruen-nacht); font-weight: 600;
  border-radius: var(--rundung);
}

/* --------------------------------------------------------- Kopfbereich */

.kopfbereich {
  background: transparent;
  border-bottom: 1px solid transparent;
  transition: background .25s ease, border-color .25s ease, box-shadow .25s ease;
}
.kopfbereich.ist-gescrollt {
  background: rgba(4, 23, 15, .92);
  backdrop-filter: blur(10px);
  border-bottom-color: rgba(111, 224, 171, .22);
  box-shadow: 0 12px 30px rgba(0, 0, 0, .35);
}
/* Auf Unterseiten liegt kein Bild hinter dem Kopf */
.seite:not(.seite-index) .kopfbereich { background: var(--gruen-nacht); }

.hauptnavigation {
  margin-left: auto; display: flex; align-items: center; gap: var(--abstand-klein);
}
.navi-liste { gap: 1.6rem; }
.navi-punkt > a {
  position: relative;
  color: var(--creme); font-size: .95rem; padding: .5rem 0;
}
.navi-punkt > a::after {
  content: ''; position: absolute; left: 0; right: 0; bottom: 0; height: 2px;
  background: var(--verlauf-akzent); border-radius: 2px;
  transform: scaleX(0); transform-origin: left;
  transition: transform .22s ease;
}
.navi-punkt > a:hover { color: var(--mint-hell); }
.navi-punkt > a:hover::after { transform: scaleX(1); }
.navi-punkt.ist-aktiv > a { color: var(--mint); }
.navi-punkt.ist-aktiv > a::after { transform: scaleX(1); }

.untermenue {
  display: none; position: absolute; left: -1rem; top: 100%;
  min-width: 17rem; padding: .5rem 0;
  background: var(--gruen-nacht);
  border-top: 2px solid transparent;
  border-image: var(--verlauf-kante) 1;
  border-radius: 0 0 var(--rundung) var(--rundung);
  box-shadow: 0 18px 40px rgba(0, 0, 0, .45);
}
.untermenue a { color: var(--creme); padding: .6rem 1.2rem; font-size: .92rem; }
.untermenue a:hover {
  background: linear-gradient(90deg, rgba(31, 157, 107, .22), rgba(31, 157, 107, 0));
  color: var(--mint-hell);
}

.navi-spende {
  background: var(--verlauf-akzent); color: var(--gruen-nacht);
  padding: .65rem 1.35rem; text-decoration: none;
  font-size: .8rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .12em;
  border-radius: 999px;
  box-shadow: 0 6px 18px rgba(31, 157, 107, .28);
  transition: filter .2s ease, transform .2s ease, box-shadow .2s ease;
}
.navi-spende:hover {
  color: var(--gruen-nacht); filter: brightness(1.08);
  transform: translateY(-1px); box-shadow: 0 10px 24px rgba(31, 157, 107, .38);
}

.menue-schalter { color: var(--creme); margin-left: auto; }
.menue-wort { font-size: .78rem; text-transform: uppercase; letter-spacing: .14em; }

@media (max-width: 899px) {
  .menue-schalter { display: flex; }
  .hauptnavigation {
    position: fixed; inset: 0 0 0 auto; width: min(22rem, 88vw);
    background: var(--verlauf-tief);
    border-left: 1px solid var(--gruen-linie);
    flex-direction: column; align-items: stretch; justify-content: flex-start;
    gap: 0; padding: 5.5rem 1.75rem 2rem;
    transform: translateX(100%); transition: transform .28s ease;
    overflow-y: auto;
  }
  .hauptnavigation.ist-offen { transform: translateX(0); }
  .navi-liste { flex-direction: column; align-items: stretch; gap: 0; }
  .navi-punkt { border-bottom: 1px solid var(--gruen-linie); }
  .navi-punkt > a { padding: .9rem 0; font-size: 1.05rem; }
  .navi-punkt > a::after { display: none; }
  .hat-untermenue { display: grid; grid-template-columns: 1fr auto; align-items: center; }
  .untermenue-schalter { display: block; color: var(--creme); }
  .untermenue {
    display: none; position: static; grid-column: 1 / -1;
    box-shadow: none; border-top: 0; border-image: none;
    padding: 0 0 .6rem 1rem; min-width: 0;
    background: transparent;
  }
  .untermenue-offen .untermenue { display: block; }
  .navi-spende { margin-top: 1.5rem; text-align: center; }
  body.menue-offen { overflow: hidden; }
}

/* --------------------------------------------------------- Hero */

.hero { position: relative; display: grid; min-height: min(88vh, 760px); }
.hero > * { grid-area: 1 / 1; }
.hero-bild { width: 100%; height: 100%; object-fit: cover; filter: saturate(.75); }
.hero-schleier {
  background:
    linear-gradient(to bottom, rgba(4, 23, 15, .38) 0%, rgba(7, 42, 29, .78) 52%, rgba(11, 56, 39, .98) 100%),
    linear-gradient(to right, var(--gruen-nacht) 0%, rgba(7, 42, 29, .68) 45%, rgba(31, 157, 107, .22) 100%);
}
/* Weicher Übergang in den folgenden Abschnitt */
.hero-saum {
  align-self: end; height: 9rem; pointer-events: none;
  background: linear-gradient(to bottom, rgba(11, 56, 39, 0), var(--gruen) 92%);
}
.hero-inhalt { align-self: end; padding-block: clamp(3rem, 9vw, 6rem); position: relative; z-index: 1; }
.hero-dachzeile {
  font-size: .78rem; font-weight: 600; text-transform: uppercase;
  letter-spacing: .2em; color: var(--mint); margin-bottom: 1.2rem;
}
.hero h1 { max-width: 18ch; margin-bottom: .35em; }
.hero-text { font-size: 1.2em; max-width: 52ch; color: var(--creme); }

/* --------------------------------------------------------- Abschnitte */

.abschnitt-hell { background: var(--verlauf-flaeche); }
.abschnitt-zitat {
  background:
    radial-gradient(38rem 22rem at 50% 0%, rgba(31, 157, 107, .22), transparent 70%),
    var(--verlauf-flaeche);
  text-align: center;
}
.abschnitt-aufruf { background: var(--verlauf-tief); }
.abschnitt-text { background: transparent; }

/* Haarfeine Lichtkante zwischen den Abschnitten */
.abschnitt-hell, .abschnitt-zitat, .abschnitt-aufruf { position: relative; }
.abschnitt-hell::before, .abschnitt-zitat::before, .abschnitt-aufruf::before {
  content: ''; position: absolute; left: 0; right: 0; top: 0; height: 1px;
  background: var(--verlauf-kante); opacity: .5;
}

.seitenkopf {
  background:
    radial-gradient(42rem 26rem at 88% -20%, rgba(31, 157, 107, .28), transparent 68%),
    var(--verlauf-tief);
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2rem, 5vw, 3.5rem);
}
.seitenkopf h1 { max-width: 20ch; }

/* --------------------------------------------------------- Schaltflächen */

.schaltflaeche {
  padding: .85rem 1.7rem; border-radius: 999px;
  font-size: .8rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .12em;
  transition: filter .2s ease, transform .2s ease, box-shadow .2s ease,
              background .2s ease, border-color .2s ease, color .2s ease;
}
.stufe-1 {
  background: var(--verlauf-akzent); color: var(--gruen-nacht);
  border: 1px solid transparent;
  box-shadow: 0 8px 22px rgba(31, 157, 107, .30);
}
.stufe-1:hover {
  color: var(--gruen-nacht); filter: brightness(1.08);
  transform: translateY(-2px); box-shadow: 0 12px 28px rgba(31, 157, 107, .42);
}
.stufe-2 {
  background: rgba(111, 224, 171, .06); color: var(--mint);
  border: 1px solid rgba(111, 224, 171, .45);
}
.stufe-2:hover {
  background: rgba(111, 224, 171, .16); border-color: var(--mint);
  color: var(--mint-hell); transform: translateY(-2px);
}

/* --------------------------------------------------------- Karten */

.karte {
  position: relative;
  background: var(--verlauf-flaeche);
  border: 1px solid var(--gruen-linie);
  border-radius: var(--rundung);
  padding: var(--abstand-mittel);
  display: flex; flex-direction: column; gap: .35rem;
  overflow: hidden;
  transition: transform .22s ease, border-color .22s ease, box-shadow .22s ease;
}
/* Verlaufskante oben statt einfarbiger Linie */
.karte::before {
  content: ''; position: absolute; left: 0; right: 0; top: 0; height: 2px;
  background: var(--verlauf-akzent);
  opacity: .75; transition: opacity .22s ease;
}
.karte:hover {
  transform: translateY(-4px);
  border-color: rgba(111, 224, 171, .45);
  box-shadow: 0 18px 38px rgba(0, 0, 0, .38);
}
.karte:hover::before { opacity: 1; }
.abschnitt-hell .karte { background: var(--verlauf-tief); }
.karte-bild {
  width: calc(100% + 2 * var(--abstand-mittel));
  margin: calc(-1 * var(--abstand-mittel)) calc(-1 * var(--abstand-mittel)) var(--abstand-klein);
  aspect-ratio: 3 / 2; object-fit: cover;
  filter: saturate(.8) brightness(.88); transition: filter .25s ease, transform .3s ease;
}
.karte:hover .karte-bild { filter: none; transform: scale(1.03); }
.karte-titel { font-size: 1.35rem; margin-bottom: .2em; }
.karte-text { color: var(--creme-gedaempft); margin-bottom: .6em; }
.karte-verweis {
  margin-top: auto; font-size: .78rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .12em; text-decoration: none;
}

/* --------------------------------------------------------- Bilder */

.bild img, .reihe-bild img, .galerie img, .person-bild img {
  filter: saturate(.82); transition: filter .3s ease;
  border-radius: var(--rundung);
}
.bild:hover img, .reihe-bild:hover img, .galerie a:hover img { filter: none; }
.bild figcaption, .reihe-bild figcaption {
  font-size: .85rem; color: var(--creme-gedaempft); margin-top: .6rem;
}
.spalte-bild .bild img { box-shadow: 0 22px 52px rgba(0, 0, 0, .45); }

/* --------------------------------------------------------- Zitat */

.zitat { position: relative; max-width: 46rem; margin-inline: auto; padding-top: 2rem; }
.zitat::before {
  content: '“'; position: absolute; top: -1.4rem; left: 50%; transform: translateX(-50%);
  font-family: var(--serif); font-size: 6rem; line-height: 1;
  color: var(--mint); opacity: .35;
}
.zitat blockquote { margin: 0; }
.zitat p {
  font-family: var(--serif); font-style: italic;
  font-size: clamp(1.4rem, 2.6vw, 2.1rem); line-height: 1.4;
  color: var(--weiss); max-width: none;
}
.zitat figcaption {
  font-size: .78rem; text-transform: uppercase; letter-spacing: .16em;
  color: var(--mint); margin-top: 1.4rem;
}

/* --------------------------------------------------------- Listen */

.nummer {
  font-family: var(--serif); font-size: 2rem; line-height: 1;
  background: var(--verlauf-akzent);
  -webkit-background-clip: text; background-clip: text;
  color: transparent; -webkit-text-fill-color: transparent;
}
@supports not (background-clip: text) {
  .nummer { color: var(--mint); -webkit-text-fill-color: currentColor; }
}
.nummer-punkt h3 { margin-bottom: .25em; }
.nummer-punkt p { color: var(--creme-gedaempft); margin: 0; }

/* --------------------------------------------------------- Personen */

.person-name { font-size: 1.2rem; margin: .9rem 0 .1em; }
.person-rolle { color: var(--mint); font-size: .9rem; margin: 0 0 .1em; }
.person-zusatz { color: var(--creme-gedaempft); font-size: .85rem; margin: 0; }
.person-initialen {
  background: var(--verlauf-flaeche); border: 1px solid var(--gruen-linie);
  border-radius: var(--rundung);
  color: var(--mint); font-family: var(--serif);
}

/* --------------------------------------------------------- Konto */

.konto {
  position: relative; overflow: hidden;
  background: var(--verlauf-flaeche);
  border: 1px solid var(--gruen-linie);
  border-radius: 0 var(--rundung) var(--rundung) 0;
  padding: var(--abstand-mittel); margin-bottom: var(--abstand-klein);
  color: var(--creme);
}
/* Akzent nur an der linken Kante, als Verlauf von oben nach unten */
.konto::before {
  content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 2px;
  background: linear-gradient(to bottom, var(--mint), var(--smaragd));
}
.abschnitt-hell .konto, .abschnitt-aufruf .konto { background: var(--verlauf-tief); }
.konto-titel { font-size: 1.15rem; color: var(--mint); }
.konto-daten dt { color: var(--creme-gedaempft); font-weight: 400; font-size: .9rem; }
.konto-daten dd { color: var(--creme); }
.iban-kopieren {
  margin-left: .6rem; background: rgba(111, 224, 171, .08); color: var(--mint);
  border: 1px solid rgba(111, 224, 171, .45); border-radius: 999px;
  padding: .2rem .7rem; font-size: .75rem;
  transition: background .2s ease, color .2s ease;
}
.iban-kopieren:hover { background: rgba(111, 224, 171, .2); }
.iban-kopieren.ist-kopiert { background: var(--verlauf-akzent); color: var(--gruen-nacht); border-color: transparent; }

/* --------------------------------------------------------- Downloads */

.download {
  background: var(--verlauf-flaeche); border: 1px solid var(--gruen-linie);
  border-radius: var(--rundung);
  padding: .9rem 1.2rem; color: var(--creme);
  transition: border-color .2s ease, transform .2s ease;
}
.download:hover { border-color: rgba(111, 224, 171, .5); transform: translateX(3px); }
.download-art {
  font-size: .7rem; font-weight: 600; letter-spacing: .12em;
  color: var(--gruen-nacht); background: var(--verlauf-akzent);
  padding: .2rem .55rem; border-radius: 999px; flex: 0 0 auto;
}

/* --------------------------------------------------------- Aufruf */

.aufruf {
  border: 1px solid rgba(111, 224, 171, .28);
  border-radius: var(--rundung);
  background:
    radial-gradient(30rem 18rem at 50% 0%, rgba(31, 157, 107, .18), transparent 70%);
  padding: var(--abstand-gross); text-align: center;
}
.aufruf p { margin-inline: auto; }
.aufruf .schaltflaechen { justify-content: center; }

/* --------------------------------------------------------- Satzung */

.inhaltsverzeichnis {
  background: var(--verlauf-flaeche); border: 1px solid var(--gruen-linie);
  border-radius: var(--rundung);
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
.paragraf li::marker { color: var(--mint); }

/* --------------------------------------------------------- Formular */

.formular-block { max-width: 52rem; }
.formfeld input, .formfeld select, .formfeld textarea {
  background: rgba(4, 23, 15, .75); color: var(--creme);
  border: 1px solid var(--gruen-linie); border-radius: var(--rundung);
  transition: border-color .2s ease, box-shadow .2s ease;
}
.formfeld input:focus, .formfeld select:focus, .formfeld textarea:focus {
  border-color: var(--mint); outline: none;
  box-shadow: 0 0 0 3px rgba(111, 224, 171, .22);
}
.formfeld label { font-size: .9rem; }
.pflicht { color: var(--mint); }
.feldfehler { color: #ffb4a2; }
.hat-fehler input, .hat-fehler select, .hat-fehler textarea { border-color: #ff8f78; }
.formular-meldung {
  padding: .9rem 1.1rem; border-left: 2px solid var(--smaragd);
  border-radius: 0 var(--rundung) var(--rundung) 0;
  background: rgba(4, 23, 15, .8);
}
.meldung-erfolg { border-left-color: var(--mint); }
.meldung-fehler { border-left-color: #ff8f78; }
.formfeld-haken label { font-size: .92rem; color: var(--creme-gedaempft); }

/* --------------------------------------------------------- Anschrift */

.anschrift { font-size: 1.05rem; line-height: 1.9; }

/* --------------------------------------------------------- Lichtkasten */

.lichtkasten { background: rgba(4, 23, 15, .96); }
.lichtkasten button { color: var(--creme); }
.lichtkasten button:hover { color: var(--mint); }
.lichtkasten-zurueck, .lichtkasten-weiter { font-size: 2.4rem; padding: .3rem .8rem; }
.lichtkasten-schliessen {
  font-size: .78rem; text-transform: uppercase; letter-spacing: .14em;
  border: 1px solid rgba(111, 224, 171, .45); border-radius: 999px; padding: .5rem 1.1rem;
}
.lichtkasten-zaehler { color: var(--creme-gedaempft); font-size: .85rem; }

/* --------------------------------------------------------- Fußbereich */

.fussbereich {
  position: relative;
  background: var(--verlauf-tief);
  border-top: 1px solid transparent;
}
.fussbereich::before {
  content: ''; position: absolute; left: 0; right: 0; top: 0; height: 2px;
  background: var(--verlauf-kante);
}
.fuss-titel {
  font-family: var(--sans); font-size: .75rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .16em; color: var(--mint);
  margin-bottom: 1rem;
}
.fussbereich p, .fussbereich address, .fussbereich a { color: var(--creme-gedaempft); font-size: .92rem; }
.fussbereich a:hover { color: var(--mint); }
.fussbereich .fuss-claim {
  font-family: var(--serif); font-size: 1.25rem; font-style: italic;
  color: var(--mint); margin: .8rem 0 .5rem;
}
.fuss-zeile { border-top: 1px solid var(--gruen-linie); font-size: .85rem; }
.fuss-zeile p { margin: 0; font-size: .85rem; }
"""
