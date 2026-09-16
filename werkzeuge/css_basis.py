# -*- coding: utf-8 -*-
"""Gestaltungsneutrale CSS-Grundlage: Zurücksetzung, Mechanik, Zugänglichkeit.

Alles Sichtbare (Farben, Schriften, Formen, Abstände) legen die Entwürfe
selbst fest. Hier steht nur, was in jedem Entwurf gleich funktionieren muss.
"""

GRUNDLAGE = """/* ==========================================================================
   1. Zurücksetzung und Grundlagen
   ========================================================================== */

*, *::before, *::after { box-sizing: border-box; }

html {
  -webkit-text-size-adjust: 100%;
  scroll-behavior: smooth;
  scroll-padding-top: 6rem;
}

body {
  margin: 0;
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}

img, picture, svg { max-width: 100%; height: auto; display: block; }
ul, ol { margin: 0; padding: 0; }
figure { margin: 0; }
address { font-style: normal; }
button { font: inherit; color: inherit; cursor: pointer; }

/* ==========================================================================
   2. Zugänglichkeit
   ========================================================================== */

.nur-vorlesen {
  position: absolute !important;
  width: 1px; height: 1px;
  padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%);
  white-space: nowrap; border: 0;
}

.sprungmarke {
  position: absolute; left: 1rem; top: -100px; z-index: 200;
  padding: .75rem 1.25rem; text-decoration: none;
  transition: top .18s ease;
}
.sprungmarke:focus { top: 1rem; }

:focus-visible { outline: 3px solid var(--fokus); outline-offset: 3px; }

.honigtopf {
  position: absolute !important;
  left: -9999px; width: 1px; height: 1px; overflow: hidden;
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
    scroll-behavior: auto !important;
  }
  .faehrt-ein { opacity: 1 !important; transform: none !important; }
}

/* ==========================================================================
   3. Layout-Mechanik
   ========================================================================== */

.huelle {
  width: 100%;
  max-width: var(--huelle-breite);
  margin-inline: auto;
  padding-inline: var(--rand);
}

.abschnitt { padding-block: var(--abstand-abschnitt); }

.zweispalter { display: grid; gap: var(--abstand-gross); align-items: center; }
@media (min-width: 900px) {
  .zweispalter { grid-template-columns: 1fr 1fr; gap: var(--abstand-gross); }
  .zweispalter.bild-zuerst .spalte-text { order: 2; }
  .zweispalter.bild-zuerst .spalte-bild { order: 1; }
}

.karten {
  display: grid; gap: var(--abstand-mittel);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
}

.bildreihe {
  display: grid; gap: var(--abstand-klein);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
  margin-top: var(--abstand-mittel);
}

.galerie {
  list-style: none;
  display: grid; gap: var(--abstand-klein);
  grid-template-columns: repeat(auto-fill, minmax(min(100%, 15rem), 1fr));
}
.galerie a { display: block; }
.galerie img { aspect-ratio: 4 / 3; object-fit: cover; width: 100%; }

.personen {
  list-style: none;
  display: grid; gap: var(--abstand-mittel);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 13rem), 1fr));
}
.person-bild { position: relative; }
.person-bild img { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; }
.person-initialen {
  display: grid; place-items: center;
  width: 100%; aspect-ratio: 4 / 5;
  font-size: clamp(2rem, 6vw, 3rem); font-weight: 700; letter-spacing: .05em;
}

.nummernliste { list-style: none; display: grid; gap: var(--abstand-mittel); }
.nummer-punkt { display: grid; grid-template-columns: auto 1fr; gap: var(--abstand-klein); }

.downloads { list-style: none; display: grid; gap: .6rem; }
.download { display: flex; align-items: center; gap: .9rem; text-decoration: none; }

.schaltflaechen { display: flex; flex-wrap: wrap; gap: .75rem; }
.schaltflaeche { display: inline-block; text-decoration: none; text-align: center; }

.konto-daten { display: grid; grid-template-columns: max-content 1fr; gap: .4rem 1.2rem; margin: 0; }
.konto-daten dt { font-weight: 600; }
.konto-daten dd { margin: 0; }
.iban { font-variant-numeric: tabular-nums; letter-spacing: .04em; white-space: nowrap; }

/* ==========================================================================
   4. Kopfbereich und Navigation
   ========================================================================== */

.kopfbereich { position: sticky; top: 0; z-index: 100; }
.kopf-huelle {
  max-width: var(--huelle-breite); margin-inline: auto;
  padding: var(--kopf-polster) var(--rand);
  display: flex; align-items: center; gap: var(--abstand-klein);
}
.logo { display: inline-flex; flex: 0 0 auto; }
.logo img { height: var(--logo-hoehe); width: auto; }

.navi-liste { list-style: none; display: flex; flex-wrap: wrap; align-items: center; }
.navi-punkt { position: relative; }
.navi-punkt > a { display: block; text-decoration: none; }
.untermenue { list-style: none; }
.untermenue a { display: block; text-decoration: none; }

.untermenue-schalter {
  background: none; border: 0; padding: .35rem; display: none;
}
.pfeil {
  display: inline-block; width: .5rem; height: .5rem;
  border-right: 2px solid currentColor; border-bottom: 2px solid currentColor;
  transform: rotate(45deg); transition: transform .18s ease;
}
.untermenue-offen .pfeil { transform: rotate(-135deg); }

.menue-schalter { display: none; border: 0; background: none; align-items: center; gap: .5rem; }
.menue-striche { position: relative; display: block; width: 1.4rem; height: 2px; background: currentColor; }
.menue-striche::before, .menue-striche::after {
  content: ''; position: absolute; left: 0; width: 100%; height: 2px; background: currentColor;
  transition: transform .2s ease, top .2s ease;
}
.menue-striche::before { top: -.45rem; }
.menue-striche::after { top: .45rem; }
[aria-expanded="true"] .menue-striche { background: transparent; }
[aria-expanded="true"] .menue-striche::before { top: 0; transform: rotate(45deg); }
[aria-expanded="true"] .menue-striche::after { top: 0; transform: rotate(-45deg); }

/* Desktop: Untermenüs über Zeiger und Tastatur */
@media (min-width: 900px) {
  .hat-untermenue:hover > .untermenue,
  .hat-untermenue:focus-within > .untermenue { display: block; }
}

/* ==========================================================================
   5. Formular
   ========================================================================== */

.formfelder { display: grid; gap: var(--abstand-klein); }
@media (min-width: 700px) { .formfelder { grid-template-columns: 1fr 1fr; } }
.formfeld { display: grid; gap: .35rem; }
.formfeld-breit { grid-column: 1 / -1; }
.formfeld label { font-weight: 600; }
.formfeld input, .formfeld select, .formfeld textarea {
  font: inherit; width: 100%; padding: .7rem .85rem;
}
.formfeld textarea { resize: vertical; min-height: 9rem; }
.feldfehler { font-size: .85rem; min-height: 1.1em; }
.formfeld-haken { grid-template-columns: auto 1fr; align-items: start; gap: .6rem; }
.formfeld-haken input { width: 1.1rem; height: 1.1rem; margin-top: .3rem; }
.formfeld-haken label { font-weight: 400; }
.formfeld-haken .feldfehler { grid-column: 1 / -1; }
.formular-meldung:empty { display: none; }

/* ==========================================================================
   6. Lichtkasten
   ========================================================================== */

body.lichtkasten-offen { overflow: hidden; }
.lichtkasten {
  position: fixed; inset: 0; z-index: 300;
  display: grid; place-items: center;
  grid-template-areas: 'zurueck bild weiter';
  grid-template-columns: auto 1fr auto;
  gap: 1rem; padding: clamp(1rem, 4vw, 3rem);
}
.lichtkasten[hidden] { display: none; }
.lichtkasten-bild {
  grid-area: bild; max-width: 100%; max-height: 82vh;
  width: auto; object-fit: contain; margin-inline: auto;
}
.lichtkasten-zurueck { grid-area: zurueck; }
.lichtkasten-weiter { grid-area: weiter; }
.lichtkasten-schliessen { position: absolute; top: 1rem; right: 1rem; }
.lichtkasten-zaehler { position: absolute; bottom: 1rem; left: 0; right: 0; text-align: center; }
.lichtkasten button { border: 0; background: none; }

/* ==========================================================================
   7. Fußbereich
   ========================================================================== */

.fuss-huelle {
  max-width: var(--huelle-breite); margin-inline: auto;
  padding: var(--abstand-abschnitt) var(--rand) var(--abstand-mittel);
  display: grid; gap: var(--abstand-mittel);
}
@media (min-width: 700px) { .fuss-huelle { grid-template-columns: 1fr 1fr; } }
@media (min-width: 1000px) { .fuss-huelle { grid-template-columns: 1.4fr 1fr 1fr 1fr; } }
.fuss-spalte ul { list-style: none; display: grid; gap: .45rem; }
.fuss-spalte a { text-decoration: none; }
.fuss-marke img { height: auto; width: min(200px, 60%); }
.fuss-zeile {
  max-width: var(--huelle-breite); margin-inline: auto;
  padding: var(--abstand-klein) var(--rand) var(--abstand-mittel);
  display: flex; flex-wrap: wrap; gap: .5rem 1.5rem; justify-content: space-between;
}
.fuss-zeile p { margin: 0; }
"""
