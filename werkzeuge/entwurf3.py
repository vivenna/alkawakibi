# -*- coding: utf-8 -*-
"""Entwurf 3 – „Manifest“.

Modernistisch und plakativ: warmer Sandton, Tiefschwarz, große grüne Flächen
mit schrägen Kanten. Die geometrische Fahne aus dem Logo wird zum
Gestaltungsprinzip der ganzen Seite.
"""
import inhalte as I
import skripte
from basis import e
from css_basis import GRUNDLAGE
from entwurf_basis import Entwurf

BUEHNENBILDER = [
    (I.BILD + 'veranstaltung-publikum-800.jpg', 'Volles Publikum bei einer Veranstaltung des Vereins'),
    (I.BILD + 'seminar-runde-800.jpg', 'Seminar des Vereins im Stuhlkreis'),
    (I.BILD + 'begegnungsfest-kinder-800.jpg', 'Kinder basteln am Stand des Vereins'),
    (I.BILD + 'podiumsdiskussion-800.jpg', 'Podiumsdiskussion mit mehreren Rednern'),
]


class Manifest(Entwurf):
    kennung = 'entwurf-3-manifest'
    name = 'Manifest'
    schriften = ['space-grotesk', 'ibm-plex-sans', 'noto-naskh-arabic']
    logo = 'assets/bilder/marke.png'
    logo_fuss = 'assets/bilder/marke-weiss.png'
    farbe_browser = '#f4f1ea'

    # ------------------------------------------------------------- Struktur

    def kopf(self, aktiv):
        v = I.VEREIN
        return f"""  <header class="kopfbereich" id="kopfbereich">
    <div class="kopf-huelle">
      <a class="logo" href="index.html">
        <img src="{self.logo}" alt="" width="251" height="251" aria-hidden="true">
        <span class="logo-wort">ALKAWAKIBI</span>
        <span class="nur-vorlesen">{e(v['kurz'])} – {e(v['claim'])}, zur Startseite</span>
      </a>
      <button class="menue-schalter" type="button" aria-expanded="false" aria-controls="hauptmenue">
        <span class="menue-striche" aria-hidden="true"></span>
        <span class="menue-wort">Menü</span>
      </button>
      <nav class="hauptnavigation" id="hauptmenue" aria-label="Hauptmenü">
        <ul class="navi-liste">
{self.navigation(aktiv)}
        </ul>
        <a class="navi-spende" href="spenden.html">Spenden</a>
        <p class="menue-fuss">
          {e(v['strasse'])} · {e(v['ort'])}<br>
          <a href="mailto:{v['email']}">{v['email']}</a>
        </p>
      </nav>
    </div>
  </header>"""

    def hero(self):
        h = I.HERO
        titel = e(h['titel']).replace(
            e(h['hervor']), '<span class="hervor">%s</span>' % e(h['hervor']))
        bilder = '\n'.join(
            '          <li><img src="%s" alt="%s" width="800" height="800"%s></li>'
            % (quelle, e(alt), ' fetchpriority="high"' if i == 0 else ' loading="lazy"')
            for i, (quelle, alt) in enumerate(BUEHNENBILDER))
        return f"""    <section class="buehne">
      <div class="huelle buehne-raster">
        <div class="buehne-text">
          <p class="buehne-dachzeile"><span class="ziffer" aria-hidden="true">01</span>{e(h['dachzeile'])}</p>
          <h1>{titel}</h1>
          <p class="buehne-vorspann">{e(h['text'])}</p>
          <p class="schaltflaechen">
            <a class="schaltflaeche stufe-1" href="aktivitaeten.html">Unsere Aktivitäten</a>
            <a class="schaltflaeche stufe-2" href="spenden.html">Jetzt spenden</a>
          </p>
        </div>
        <div class="buehne-flagge">
          <img src="assets/bilder/marke-weiss.png" alt="" width="251" height="251" aria-hidden="true">
          <span class="buehne-arabisch" lang="ar" dir="rtl">{I.VEREIN['arabisch']}</span>
        </div>
      </div>
      <ul class="buehne-bilder">
{bilder}
      </ul>
    </section>"""

    def seitenkopf(self, datei):
        s = I.SEITEN[datei]
        nummer = (I.REIHENFOLGE.index(datei) + 1) if datei in I.REIHENFOLGE else 0
        teile = ''
        teile += ('          <p class="kicker"><span class="ziffer" aria-hidden="true">%02d</span>%s</p>\n'
                  % (nummer, e(s.get('kicker', 'Seite'))))
        teile += '          <h1>%s</h1>\n' % e(s['h1'])
        if s.get('einleitung'):
            teile += '          <p class="einleitung">%s</p>\n' % e(s['einleitung'])
        return ('    <section class="seitenkopf">\n      <div class="huelle">\n'
                '%s      </div>\n    </section>' % teile)

    def kicker(self, text):
        return ('        <p class="kicker"><span class="ziffer" aria-hidden="true">›</span>%s</p>\n'
                % e(text))

    def zitat(self, text, quelle):
        return (f'        <figure class="zitat">\n'
                f'          <span class="zitat-winkel" aria-hidden="true"></span>\n'
                f'          <blockquote><p>{e(text)}</p></blockquote>\n'
                f'          <figcaption>{e(quelle)}</figcaption>\n'
                f'        </figure>\n')

    def js_zusatz(self):
        return skripte.EINBLENDEN

    def js_start(self):
        return '    einblendenEinrichten();'

    # ------------------------------------------------------------- Gestaltung

    def css(self):
        return GRUNDLAGE + """
/* ==========================================================================
   Entwurf 3 – Manifest
   Sand und Tiefschwarz, grüne Diagonalflächen, plakative Typografie.
   Keine Rundungen, keine Schatten, harte Kanten.
   ========================================================================== */

:root {
  --sand:        #f4f1ea;
  --sand-dunkel: #e7e2d6;
  --tinte:       #0a0a0a;
  --tinte-weich: #3a3a38;
  --gruen:       #0d4a0d;
  --gruen-tief:  #072707;
  --zinnober:    #e2551e;
  --weiss:       #ffffff;
  --fokus:       var(--zinnober);

  --huelle-breite:    78rem;
  --rand:             clamp(1.25rem, 5vw, 3.5rem);
  --abstand-abschnitt: clamp(3.5rem, 8vw, 7rem);
  --abstand-gross:    clamp(2.5rem, 5vw, 4rem);
  --abstand-mittel:   clamp(1.5rem, 3vw, 2.25rem);
  --abstand-klein:    1rem;
  --kopf-polster:     .75rem;
  --logo-hoehe:       2.5rem;

  --display: 'Space Grotesk', system-ui, -apple-system, sans-serif;
  --text:    'IBM Plex Sans', system-ui, -apple-system, sans-serif;
  --arabisch: 'Noto Naskh Arabic', var(--text);
}

body {
  background: var(--sand);
  color: var(--tinte);
  font-family: var(--text);
  font-size: clamp(1rem, .95rem + .28vw, 1.1rem);
  line-height: 1.65;
}
[lang="ar"] { font-family: var(--arabisch); }

/* --------------------------------------------------------- Typografie */

h1, h2, h3 {
  font-family: var(--display); font-weight: 700;
  line-height: .98; letter-spacing: -.03em;
  color: var(--tinte); margin: 0 0 .45em;
}
h1 { font-size: clamp(2.6rem, 8vw, 6rem); }
h2 { font-size: clamp(1.9rem, 4.4vw, 3.4rem); }
h3 { font-size: 1.3rem; line-height: 1.15; }

p { margin: 0 0 1em; max-width: 66ch; }
a { color: var(--gruen); text-underline-offset: .2em; text-decoration-thickness: 2px; }
a:hover { color: var(--zinnober); }

.hervor { color: var(--zinnober); }

.kicker {
  display: flex; align-items: baseline; gap: .7rem;
  font-family: var(--display); font-weight: 500;
  font-size: .78rem; text-transform: uppercase; letter-spacing: .2em;
  color: var(--tinte-weich); margin: 0 0 1.1em;
}
.ziffer {
  font-family: var(--display); font-weight: 700; color: var(--zinnober);
  letter-spacing: 0; font-size: 1.05rem;
}

.einleitung { font-size: 1.2em; max-width: 54ch; color: var(--tinte-weich); }
.unterzeile {
  font-family: var(--display); font-weight: 500; font-size: 1.25rem;
  color: var(--zinnober); margin-top: -.5em; letter-spacing: -.01em;
}
.hinweis { font-size: .9rem; color: var(--tinte-weich); }
.hinweis-stark {
  border: 2px solid var(--tinte); border-left-width: 8px; border-left-color: var(--zinnober);
  padding: .9rem 1.2rem; background: var(--weiss);
}
.hervorhebung {
  font-family: var(--display); font-weight: 500;
  font-size: clamp(1.3rem, 2.4vw, 1.8rem); line-height: 1.25;
  max-width: 34ch; margin-top: 1.4em; color: var(--tinte);
  border-top: 2px solid var(--tinte); padding-top: 1rem;
}

/* --------------------------------------------------------- Sprungmarke */

.sprungmarke { background: var(--zinnober); color: var(--weiss); font-weight: 600; }

/* --------------------------------------------------------- Kopfbereich */

.kopfbereich { background: var(--sand); border-bottom: 2px solid var(--tinte); }
.logo { align-items: center; gap: .6rem; text-decoration: none; }
.logo img { height: var(--logo-hoehe); width: auto; }
.logo-wort {
  font-family: var(--display); font-weight: 700; font-size: 1.15rem;
  letter-spacing: .05em; color: var(--tinte);
}

.hauptnavigation { margin-left: auto; display: flex; align-items: center; gap: 1.25rem; }
.navi-liste { gap: 1.4rem; }
.navi-punkt > a {
  font-family: var(--display); font-weight: 500;
  font-size: .78rem; text-transform: uppercase; letter-spacing: .14em;
  color: var(--tinte); text-decoration: none;
  padding: .4rem 0; border-bottom: 2px solid transparent;
}
.navi-punkt > a:hover { color: var(--zinnober); }
.navi-punkt.ist-aktiv > a { border-bottom-color: var(--zinnober); }

.untermenue {
  display: none; position: absolute; left: -1rem; top: 100%;
  min-width: 18rem; background: var(--tinte); border: 2px solid var(--tinte); z-index: 10;
}
.untermenue a { color: var(--sand); padding: .7rem 1.1rem; font-size: .9rem; }
.untermenue a:hover { background: var(--zinnober); color: var(--weiss); }

.navi-spende {
  background: var(--zinnober); color: var(--weiss); text-decoration: none;
  font-family: var(--display); font-weight: 700;
  font-size: .78rem; text-transform: uppercase; letter-spacing: .12em;
  padding: .6rem 1.2rem; border: 2px solid var(--zinnober);
}
.navi-spende:hover { background: var(--tinte); border-color: var(--tinte); color: var(--weiss); }

.menue-schalter { color: var(--tinte); margin-left: auto; }
.menue-wort { font-family: var(--display); font-weight: 700; font-size: .78rem; text-transform: uppercase; letter-spacing: .14em; }
.menue-fuss { display: none; }

@media (max-width: 899px) {
  .menue-schalter { display: flex; position: relative; z-index: 2; }
  .hauptnavigation {
    position: fixed; inset: 0; background: var(--gruen);
    flex-direction: column; align-items: flex-start; justify-content: center;
    gap: 0; padding: 5rem var(--rand) 3rem;
    transform: translateY(-100%); transition: transform .3s ease;
    overflow-y: auto; z-index: 1;
  }
  .hauptnavigation.ist-offen { transform: translateY(0); }
  body.menue-offen { overflow: hidden; }
  body.menue-offen .menue-schalter { color: var(--weiss); }
  .navi-liste { flex-direction: column; align-items: stretch; gap: 0; width: 100%; counter-reset: navi; }
  .navi-punkt { border-bottom: 1px solid rgba(255, 255, 255, .25); width: 100%; }
  .navi-punkt > a {
    color: var(--weiss); font-size: clamp(1.5rem, 6vw, 2.2rem);
    letter-spacing: -.02em; text-transform: none; font-weight: 700;
    padding: .7rem 0; border-bottom: 0;
  }
  .navi-punkt.ist-aktiv > a { color: #f6c1a8; }
  .hat-untermenue { display: grid; grid-template-columns: 1fr auto; align-items: center; }
  .untermenue-schalter { display: block; color: var(--weiss); }
  .untermenue {
    display: none; position: static; grid-column: 1 / -1; border: 0;
    background: transparent; padding-bottom: .7rem; min-width: 0;
  }
  .untermenue-offen .untermenue { display: block; }
  .untermenue a { color: rgba(255, 255, 255, .85); padding: .4rem 0 .4rem 1rem; font-size: 1rem; }
  .untermenue a:hover { background: transparent; color: var(--weiss); }
  .navi-spende { margin-top: 1.75rem; }
  .menue-fuss { display: block; margin-top: 2rem; color: rgba(255, 255, 255, .8); font-size: .9rem; }
  .menue-fuss a { color: var(--weiss); }
}

/* --------------------------------------------------------- Bühne */

.buehne { padding-top: clamp(2.5rem, 6vw, 5rem); overflow: hidden; }
.buehne-raster { display: grid; gap: var(--abstand-gross); align-items: center; }
@media (min-width: 900px) { .buehne-raster { grid-template-columns: 7fr 5fr; } }

.buehne-dachzeile {
  display: flex; align-items: baseline; gap: .7rem;
  font-family: var(--display); font-weight: 500; font-size: .8rem;
  text-transform: uppercase; letter-spacing: .2em; color: var(--tinte-weich);
  margin-bottom: 1.2rem;
}
.buehne h1 { max-width: 14ch; margin-bottom: .3em; }
.buehne-vorspann { font-size: 1.2em; max-width: 44ch; color: var(--tinte-weich); }

.buehne-flagge {
  position: relative; background: var(--gruen);
  aspect-ratio: 4 / 5; display: grid; place-items: center; gap: 1rem;
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 calc(100% - 5vw));
  padding: 2rem;
}
.buehne-flagge img { width: min(52%, 11rem); }
.buehne-arabisch {
  position: absolute; bottom: 14%; font-size: clamp(1.6rem, 3.5vw, 2.4rem);
  color: rgba(255, 255, 255, .92);
}

.buehne-bilder {
  list-style: none; display: grid; gap: 2px; margin-top: clamp(2.5rem, 6vw, 4.5rem);
  grid-template-columns: repeat(4, 1fr);
  width: calc(100% + var(--rand)); margin-right: calc(-1 * var(--rand));
  padding-left: var(--rand);
}
@media (max-width: 700px) { .buehne-bilder { grid-template-columns: repeat(2, 1fr); } }
.buehne-bilder img {
  width: 100%; aspect-ratio: 1; object-fit: cover;
  filter: grayscale(.25) contrast(1.05); transition: filter .25s ease;
}
.buehne-bilder li:hover img { filter: none; }

/* --------------------------------------------------------- Abschnitte */

.abschnitt-hell { background: var(--sand-dunkel); }
.abschnitt-text { background: var(--weiss); }

.abschnitt-zitat {
  background: var(--gruen); color: var(--weiss);
  clip-path: polygon(0 4vw, 100% 0, 100% 100%, 0 calc(100% - 4vw));
  padding-block: calc(var(--abstand-abschnitt) + 4vw);
  margin-block: -1px;
}
.abschnitt-zitat h2, .abschnitt-zitat p { color: var(--weiss); }

.abschnitt-aufruf { background: var(--tinte); color: var(--sand); }
.abschnitt-aufruf h2 { color: var(--weiss); }
.abschnitt-aufruf p { color: rgba(244, 241, 234, .82); }

.seitenkopf {
  padding-block: clamp(2.5rem, 7vw, 5rem) clamp(1.5rem, 4vw, 2.5rem);
  border-bottom: 2px solid var(--tinte);
}
.seitenkopf h1 { max-width: 16ch; }

/* --------------------------------------------------------- Schaltflächen */

.schaltflaeche {
  font-family: var(--display); font-weight: 700;
  font-size: .82rem; text-transform: uppercase; letter-spacing: .12em;
  padding: .85rem 1.6rem; border: 2px solid var(--tinte); border-radius: 0;
  transition: background .18s ease, color .18s ease, border-color .18s ease;
}
.stufe-1 { background: var(--zinnober); color: var(--weiss); border-color: var(--zinnober); }
.stufe-1:hover { background: var(--tinte); border-color: var(--tinte); color: var(--weiss); }
.stufe-2 { background: transparent; color: var(--tinte); }
.stufe-2:hover { background: var(--tinte); color: var(--sand); }
.abschnitt-aufruf .stufe-2, .abschnitt-zitat .stufe-2 { color: var(--sand); border-color: var(--sand); }
.abschnitt-aufruf .stufe-2:hover, .abschnitt-zitat .stufe-2:hover { background: var(--sand); color: var(--tinte); }

/* --------------------------------------------------------- Karten */

.karte {
  background: var(--weiss); border: 2px solid var(--tinte);
  padding: var(--abstand-mittel); position: relative;
  display: flex; flex-direction: column; gap: .3rem;
  transition: transform .18s ease;
}
.karte::after {
  content: ''; position: absolute; inset: 0; border: 2px solid var(--zinnober);
  opacity: 0; transform: translate(0, 0); transition: opacity .18s ease, transform .18s ease;
  pointer-events: none;
}
.karte:hover { transform: translate(-4px, -4px); }
.karte:hover::after { opacity: 1; transform: translate(6px, 6px); }
.abschnitt-hell .karte { background: var(--sand); }
.karte-bild {
  width: calc(100% + 2 * var(--abstand-mittel));
  margin: calc(-1 * var(--abstand-mittel)) calc(-1 * var(--abstand-mittel)) var(--abstand-klein);
  aspect-ratio: 3 / 2; object-fit: cover;
  border-bottom: 2px solid var(--tinte);
}
.karte-titel { font-size: 1.4rem; margin-bottom: .25em; }
.karte-text { color: var(--tinte-weich); margin-bottom: .8em; }
.karte-verweis {
  margin-top: auto; font-family: var(--display); font-weight: 700;
  font-size: .78rem; text-transform: uppercase; letter-spacing: .12em;
  text-decoration: none; color: var(--zinnober);
}

/* --------------------------------------------------------- Bilder */

.bild img, .reihe-bild img, .galerie img {
  border: 2px solid var(--tinte); transition: filter .2s ease, border-color .2s ease;
}
.galerie a:hover img, .reihe-bild:hover img { border-color: var(--zinnober); filter: brightness(1.05); }
.bild figcaption, .reihe-bild figcaption {
  font-family: var(--display); font-weight: 500; font-size: .8rem;
  text-transform: uppercase; letter-spacing: .08em;
  color: var(--tinte-weich); margin-top: .6rem;
}
.spalte-bild .bild img { aspect-ratio: 4 / 5; object-fit: cover; width: 100%; }

/* --------------------------------------------------------- Zitat */

.zitat { position: relative; max-width: 50rem; padding-left: clamp(0rem, 4vw, 4rem); }
.zitat-winkel {
  position: absolute; left: 0; top: .4rem; width: 2rem; height: 2rem;
  border-left: 4px solid var(--weiss); border-top: 4px solid var(--weiss);
}
@media (max-width: 700px) { .zitat-winkel { display: none; } }
.zitat blockquote { margin: 0; }
.zitat p {
  font-family: var(--display); font-weight: 500;
  font-size: clamp(1.3rem, 3vw, 2.2rem); line-height: 1.25;
  letter-spacing: -.02em; max-width: none;
}
.zitat figcaption {
  font-family: var(--display); font-size: .78rem; text-transform: uppercase;
  letter-spacing: .18em; color: rgba(255, 255, 255, .75); margin-top: 1.4rem;
}

/* --------------------------------------------------------- Listen */

.nummernliste { counter-reset: punkt; }
.nummer-punkt {
  border-top: 2px solid var(--tinte); padding-top: var(--abstand-klein);
  grid-template-columns: minmax(3.5rem, auto) 1fr; gap: var(--abstand-mittel);
}
.nummer { font-family: var(--display); font-size: clamp(2rem, 4vw, 3rem); font-weight: 700; color: var(--zinnober); line-height: .9; }
.nummer-punkt h3 { margin-bottom: .25em; }
.nummer-punkt p { color: var(--tinte-weich); margin: 0; }

/* --------------------------------------------------------- Personen */

.person-bild img { border: 2px solid var(--tinte); filter: grayscale(1) contrast(1.05); transition: filter .25s ease; }
.person:hover .person-bild img { filter: none; }
.person-initialen {
  background: var(--gruen); color: var(--weiss);
  font-family: var(--display); border: 2px solid var(--tinte);
}
.person-name { font-family: var(--display); font-size: 1.15rem; margin: .8rem 0 .1em; }
.person-rolle { color: var(--zinnober); font-size: .88rem; font-weight: 600; margin: 0 0 .1em; }
.person-zusatz { color: var(--tinte-weich); font-size: .85rem; margin: 0; }

/* --------------------------------------------------------- Konto */

.konto {
  background: var(--weiss); border: 2px solid var(--tinte);
  padding: var(--abstand-mittel); margin-bottom: var(--abstand-klein);
}
.abschnitt-aufruf .konto { background: var(--sand); }
.konto-titel { font-family: var(--display); font-size: 1.1rem; }
.konto-daten dt { font-size: .82rem; text-transform: uppercase; letter-spacing: .08em; color: var(--tinte-weich); font-weight: 600; }
.abschnitt-aufruf .konto-daten dd, .abschnitt-aufruf .konto-titel { color: var(--tinte); }
.iban-kopieren {
  margin-left: .6rem; background: var(--tinte); color: var(--weiss);
  border: 2px solid var(--tinte); padding: .2rem .6rem;
  font-family: var(--display); font-size: .72rem; text-transform: uppercase; letter-spacing: .08em;
}
.iban-kopieren:hover, .iban-kopieren.ist-kopiert { background: var(--zinnober); border-color: var(--zinnober); }

/* --------------------------------------------------------- Downloads */

.download { background: var(--weiss); border: 2px solid var(--tinte); padding: .85rem 1.1rem; color: var(--tinte); }
.download:hover { background: var(--tinte); color: var(--sand); }
.download:hover .download-art { background: var(--zinnober); }
.download-art {
  font-family: var(--display); font-size: .72rem; font-weight: 700; letter-spacing: .1em;
  background: var(--gruen); color: var(--weiss); padding: .25rem .6rem; flex: 0 0 auto;
}

/* --------------------------------------------------------- Aufruf */

.aufruf { max-width: 44rem; }
.aufruf h2 { font-size: clamp(2.2rem, 5vw, 3.6rem); }

/* --------------------------------------------------------- Textbereich */

.textspalte { max-width: 68ch; }
.inhaltsverzeichnis { border: 2px solid var(--tinte); padding: var(--abstand-mittel); margin-bottom: var(--abstand-gross); }
.inhaltsverzeichnis h2 { font-size: 1.2rem; }
.inhaltsverzeichnis ol { list-style: none; columns: 2; column-gap: 2rem; }
@media (max-width: 640px) { .inhaltsverzeichnis ol { columns: 1; } }
.inhaltsverzeichnis li { margin-bottom: .35rem; break-inside: avoid; }
.inhaltsverzeichnis a { font-size: .92rem; text-decoration: none; }
.inhaltsverzeichnis a:hover { text-decoration: underline; }

.paragraf { margin-bottom: var(--abstand-gross); }
.paragraf h2 { font-size: clamp(1.4rem, 2.6vw, 2rem); border-top: 2px solid var(--tinte); padding-top: .5em; }
.satzung-punkte { list-style: decimal; padding-left: 1.6rem; display: grid; gap: .65rem; }
.satzung-unterpunkte { list-style: square; padding-left: 1.6rem; display: grid; gap: .5rem; margin: .5rem 0; }

/* --------------------------------------------------------- Formular */

.formular-block { max-width: 52rem; }
.formfeld input, .formfeld select, .formfeld textarea {
  background: var(--weiss); color: var(--tinte); border: 2px solid var(--tinte); border-radius: 0;
}
.formfeld input:focus, .formfeld select:focus, .formfeld textarea:focus {
  border-color: var(--zinnober); outline: none;
}
.formfeld label {
  font-family: var(--display); font-weight: 500; font-size: .8rem;
  text-transform: uppercase; letter-spacing: .1em;
}
.formfeld-haken label { text-transform: none; letter-spacing: 0; font-family: var(--text); font-size: .92rem; color: var(--tinte-weich); }
.pflicht { color: var(--zinnober); }
.feldfehler { color: #b3200a; font-size: .85rem; }
.hat-fehler input, .hat-fehler select, .hat-fehler textarea { border-color: #b3200a; }
.formular-meldung { border: 2px solid var(--tinte); border-left-width: 8px; padding: .9rem 1.1rem; background: var(--weiss); }
.meldung-erfolg { border-left-color: var(--gruen); }
.meldung-fehler { border-left-color: #b3200a; }

/* --------------------------------------------------------- Anschrift */

.anschrift { font-size: 1.05rem; line-height: 1.85; }

/* --------------------------------------------------------- Einblenden */

.faehrt-ein { opacity: 0; transform: translateY(16px); transition: opacity .5s ease, transform .5s ease; }
.faehrt-ein.ist-da { opacity: 1; transform: none; }

/* --------------------------------------------------------- Lichtkasten */

.lichtkasten { background: rgba(10, 10, 10, .97); }
.lichtkasten button { color: var(--sand); font-family: var(--display); }
.lichtkasten-zurueck, .lichtkasten-weiter { font-size: 2.4rem; padding: .3rem .8rem; }
.lichtkasten-schliessen {
  font-size: .78rem; text-transform: uppercase; letter-spacing: .12em; font-weight: 700;
  border: 2px solid var(--sand); padding: .5rem 1rem;
}
.lichtkasten-schliessen:hover { background: var(--zinnober); border-color: var(--zinnober); color: var(--weiss); }
.lichtkasten-bild { border: 2px solid var(--sand); }
.lichtkasten-zaehler { color: rgba(244, 241, 234, .7); font-size: .82rem; }

/* --------------------------------------------------------- Fußbereich */

.fussbereich {
  background: var(--gruen); color: rgba(255, 255, 255, .85);
  clip-path: polygon(0 3vw, 100% 0, 100% 100%, 0 100%);
  padding-top: 3vw; margin-top: -1px;
}
.fuss-titel {
  font-family: var(--display); font-size: .78rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: .14em; color: var(--weiss); margin-bottom: .9rem;
}
.fussbereich p, .fussbereich address, .fussbereich a { color: rgba(255, 255, 255, .85); font-size: .92rem; }
.fussbereich a { text-decoration: none; }
.fussbereich a:hover { color: var(--weiss); text-decoration: underline; }
.fuss-marke img { width: min(120px, 40%); }
.fussbereich .fuss-claim {
  font-family: var(--display); font-weight: 700; font-size: 1.2rem;
  color: var(--weiss); letter-spacing: -.01em; margin: .9rem 0 .5rem;
}
.fuss-zeile { border-top: 1px solid rgba(255, 255, 255, .25); }
.fuss-zeile p { font-size: .85rem; }
"""
