# -*- coding: utf-8 -*-
"""Entwurf 4 – „Türkis & Gelb“.

Die Handschrift ist die von Entwurf 1: linksbündiger Aufmacher mit Schleier
über dem Foto, Serifen-Überschriften in Cormorant Garamond, ruhige
Abschnittsfolge, feine Linien, kantige Schaltflächen. Neu ist die Farbwelt –
das vom Vorstand gewünschte Türkis mit einem kräftigen Gelb, in den Werten
von malerroundaboutiffouzar.de.

Von dort stammen die Farben, nicht die Gestaltung: kein zentrierter Aufmacher,
keine Leuchtringe, kein Scroll-Symbol. Auf Wunsch des Vorstands treten Türkis
und Gelb jetzt deutlicher hervor, der Grünstich der ersten Fassung ist
zurückgenommen – die dunklen Töne sind bewusst ins Blaue statt ins Grüne
gezogen und kräftiger gesättigt.

Gegenüber Entwurf 1 kommen hinzu: ein schmaler Merkmalstreifen unter dem
Aufmacher, der Wechsel aus türkisen und hellen Abschnitten (lange Texte wie
die Satzung stehen dadurch auf Hell), die Farbübergänge aus Entwurf 5 und
zurückhaltende Bewegung beim Scrollen.

Das Logo bleibt unverändert schwarz-grün und steht auf einer weißen Plakette.
"""
import inhalte as I
import skripte
from basis import e
from css_basis import GRUNDLAGE
from entwurf_basis import Entwurf


class TuerkisGelb(Entwurf):
    kennung = 'entwurf-4-tuerkis-gelb'
    name = 'Türkis & Gelb'
    schriften = ['cormorant-garamond', 'inter', 'noto-naskh-arabic']
    logo = 'assets/bilder/logo.png'
    logo_fuss = 'assets/bilder/logo.png'
    farbe_browser = '#0e3a41'

    # ------------------------------------------------------------- Startseite

    def startseite(self):
        """Reihenfolge wie in Entwurf 1, davor der Merkmalstreifen.

        Die Texte kommen unverändert aus inhalte.py – nur der Streifen und
        die Bebilderung unterscheiden sich von den anderen Entwürfen.
        """
        t = [self.hero(), self.merkmale()]

        t.append(self.abschnitt(
            self.zitat(I.LEITGEDANKE, I.LEITGEDANKE_QUELLE), ton='zitat'))

        wer = (self.kicker('Der Verein') + self.h2('Wer wir sind')
               + ''.join(self.absatz(p) for p in I.WER_WIR_SIND)
               + self.schaltflaechen([('Mehr über uns', 'wer-wir-sind.html', 1)]))
        t.append(self.abschnitt(self.zweispalter(
            wer,
            self.bild(I.BILD + 'gespraechsrunde-800.jpg',
                      'Gesprächsrunde bei einer Veranstaltung des Vereins',
                      None, 800, 600)), ton='hell'))

        felder = (self.kicker('Arbeitsfelder') + self.h2('Woran wir arbeiten')
                  + self.karten([{'titel': tt, 'text': tx}
                                 for tt, tx in I.ARBEITSFELDER]))
        t.append(self.abschnitt(felder))

        a = I.AUSZEICHNUNG
        aus = (self.kicker(a['kicker']) + self.h2(a['titel']) + self.absatz(a['text'])
               + self.schaltflaechen([(a['linktext'], a['ziel'], 1)]))
        t.append(self.abschnitt(self.zweispalter(
            aus, self.bild(a['bild_klein'], a['alt'], a['bildunterschrift'], 800, 600),
            bild_zuerst=True), ton='hell'))

        # Ersatzbild, damit keine Teaser-Karte bildlos neben bebilderten steht
        ersatz = {'projekt-epithetik.html': (
            I.BILD + 'begegnung-gespraech-800.jpg',
            'Gespräch am Rande einer Veranstaltung des Vereins')}
        teaser = []
        for p in I.PROJEKTE:
            bild, alt = p.get('bild'), p.get('alt')
            if not bild and p['ziel'] in ersatz:
                bild, alt = ersatz[p['ziel']]
            teaser.append({'titel': p['titel'], 'text': p['text'], 'ziel': p['ziel'],
                           'linktext': p['linktext'], 'bild': bild, 'alt': alt})
        teaser.append({'titel': 'Bildung & Begegnung',
                       'text': 'Seminare, Podiumsdiskussionen und '
                               'Nachbarschaftsfeste in Berlin.',
                       'ziel': 'aktivitaeten.html', 'linktext': 'Alle Aktivitäten',
                       'bild': I.BILD + 'podiumsdiskussion-800.jpg',
                       'alt': 'Podiumsdiskussion des Vereins'})
        t.append(self.abschnitt(
            self.kicker('Unsere Aktivitäten') + self.h2('Woran wir gerade arbeiten')
            + self.karten(teaser)))

        s = I.SPENDENAUFRUF
        t.append(self.abschnitt(self.aufruf(s['titel'], s['text'], [
            ('Jetzt spenden', 'spenden.html', 1),
            ('Mitglied werden', 'mitglied-werden.html', 2)]), ton='aufruf'))
        return '\n'.join(t)

    # ------------------------------------------------------------- Struktur

    def hero(self):
        """Linksbündig wie in Entwurf 1, Schleier von links ins Bild."""
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

    def merkmale(self):
        """Schmale Zeile mit vier Angaben zum Verein."""
        punkte = '\n'.join(
            '          <li class="merkmal">\n'
            '            <span class="merkmal-titel">%s</span>\n'
            '            <span class="merkmal-text">%s</span>\n'
            '          </li>' % (e(titel), e(text))
            for titel, text in I.MERKMALE)
        return ('    <section class="merkmale">\n'
                '      <div class="huelle">\n'
                '        <ul class="merkmal-liste">\n%s\n        </ul>\n'
                '      </div>\n    </section>' % punkte)

    def seitenkopf(self, datei):
        s = I.SEITEN[datei]
        teile = ''
        if s.get('kicker'):
            teile += '          <p class="kicker">%s</p>\n' % e(s['kicker'])
        teile += '          <h1>%s</h1>\n' % e(s['h1'])
        teile += '          <span class="gelblinie" aria-hidden="true"></span>\n'
        if s.get('einleitung'):
            teile += '          <p class="einleitung">%s</p>\n' % e(s['einleitung'])
        return ('    <section class="seitenkopf">\n      <div class="huelle">\n'
                '%s      </div>\n    </section>' % teile)

    # ------------------------------------------------------------- Zusätze

    def js_zusatz(self):
        return skripte.EINBLENDEN + r"""
  /* ------------------------------------------------- Aufmacher-Parallaxe */

  function aufmacherEinrichten() {
    var bild = document.querySelector('.hero-bild');
    if (!bild || ruhig) { return; }
    var laeuft = false;

    function zeichnen() {
      laeuft = false;
      var y = window.scrollY || window.pageYOffset;
      if (y > 900) { return; }
      bild.style.transform = 'translate3d(0, ' + (y * 0.1).toFixed(1) + 'px, 0) scale(1.06)';
    }

    window.addEventListener('scroll', function () {
      if (laeuft) { return; }
      laeuft = true;
      window.requestAnimationFrame(zeichnen);
    }, { passive: true });

    zeichnen();
  }
"""

    def js_start(self):
        return ('    einblendenEinrichten();\n'
                '    aufmacherEinrichten();')

    # ------------------------------------------------------------- Gestaltung

    def css(self):
        return GRUNDLAGE + """
/* ==========================================================================
   Entwurf 4 – Türkis & Gelb
   Aufbau und Handschrift von Entwurf 1, Farbwelt aus Türkis und Gelb.
   Türkise und helle Abschnitte wechseln sich ab; die Bausteine holen ihre
   Farben aus Variablen, die der jeweilige Abschnitt setzt.
   ========================================================================== */

:root {
  /* Farben – bewusst ins Blaue statt ins Grüne gezogen, kräftiger gesättigt */
  --tuerkis-nacht:    #0a2e33;
  --tuerkis-tief:     #0e3a41;
  --tuerkis-dunkel:   #155864;
  --tuerkis:          #1c7686;
  --tuerkis-mittel:   #4aa0b0;   /* Grundton des Farbvorbilds, angehoben */
  --tuerkis-linie:    #237e8c;
  --nebel-hell:       #e9efed;
  --tinte:            #102e2d;
  --gelb:             #f7cf1d;
  --gelb-hell:        #ffe36a;
  --gelb-tief:        #b8930a;
  --creme:            #f0f5f3;
  --creme-gedaempft:  #a9c4c3;
  --weiss:            #ffffff;
  --fokus:            var(--gelb);

  /* Farbübergänge – dieselbe Machart wie in Entwurf 5 */
  --verlauf-flaeche:  linear-gradient(168deg, var(--tuerkis) 0%, var(--tuerkis-dunkel) 58%, var(--tuerkis-tief) 100%);
  --verlauf-tief:     linear-gradient(168deg, var(--tuerkis-tief) 0%, var(--tuerkis-nacht) 100%);
  --verlauf-hell:     linear-gradient(168deg, #f4f8f6 0%, var(--nebel-hell) 100%);
  --verlauf-linie:    linear-gradient(90deg, var(--gelb) 0%, rgba(247, 207, 29, 0) 100%);
  --verlauf-kante:    linear-gradient(90deg, rgba(247, 207, 29, 0) 0%, var(--gelb) 40%, var(--gelb-hell) 70%, rgba(247, 207, 29, 0) 100%);

  /* Flächenfarben eines Abschnitts – helle Abschnitte setzen sie neu */
  --text:             var(--creme);
  --text-leise:       var(--creme-gedaempft);
  --ueberschrift:     var(--weiss);
  --verweis:          var(--gelb);
  --verweis-hover:    var(--gelb-hell);
  --kicker-farbe:     var(--gelb);
  --flaeche:          var(--tuerkis);       /* eine Stufe heller als der Grund */
  --linie:            var(--tuerkis-linie);

  /* Maße – wie in Entwurf 1 */
  --huelle-breite:    72rem;
  --rand:             clamp(1.25rem, 5vw, 3rem);
  --abstand-abschnitt: clamp(3.5rem, 8vw, 6.5rem);
  --abstand-gross:    clamp(2.5rem, 5vw, 4rem);
  --abstand-mittel:   clamp(1.5rem, 3vw, 2.25rem);
  --abstand-klein:    1rem;
  --kopf-polster:     1rem;
  --logo-hoehe:       3.1rem;
  --rundung:          2px;

  /* Schriften – wie in Entwurf 1 */
  --serif: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
  --sans:  'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --arabisch: 'Noto Naskh Arabic', var(--sans);
}

body {
  background-color: var(--tuerkis-dunkel);
  background-image:
    radial-gradient(54rem 36rem at 84% -6%, rgba(74, 160, 176, .4), transparent 66%),
    radial-gradient(42rem 32rem at 0% 40%, rgba(14, 58, 65, .55), transparent 62%);
  background-attachment: fixed;
  color: var(--text);
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
  color: var(--ueberschrift);
  margin: 0 0 .5em;
}
h1 { font-size: clamp(2.6rem, 6vw, 5rem); }
h2 { font-size: clamp(1.9rem, 3.6vw, 3rem); }
h3 { font-size: clamp(1.25rem, 1.8vw, 1.5rem); line-height: 1.25; }

p { margin: 0 0 1.1em; max-width: 68ch; }
a { color: var(--verweis); text-underline-offset: .2em; }
a:hover { color: var(--verweis-hover); }

.hervor { color: var(--gelb); }

.kicker {
  font-size: .75rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .18em;
  color: var(--kicker-farbe);
  margin: 0 0 1em;
}

.einleitung { font-size: 1.2em; color: var(--text); max-width: 60ch; }
.unterzeile {
  font-family: var(--serif); font-size: 1.35rem; font-style: italic;
  color: var(--text-leise); margin-top: -.6em;
}
.hinweis { font-size: .92rem; color: var(--text-leise); }
.hinweis-stark {
  border-left: 2px solid var(--gelb);
  padding: .8rem 1.1rem; background: var(--flaeche); color: var(--text);
}
.hervorhebung {
  font-family: var(--serif); font-size: 1.5rem; font-style: italic;
  color: var(--gelb-hell); max-width: 44ch; margin-top: 1.5em;
}
.abschnitt-hell .hervorhebung, .abschnitt-text .hervorhebung { color: #0f6a74; }

/* Feine Linie unter den Seitenüberschriften – die Goldlinie aus Entwurf 1,
   hier in Gelb und mit einem Hauch Verlauf */
.gelblinie {
  display: block; width: 4rem; height: 2px;
  background: var(--verlauf-linie); opacity: .9;
  margin: 1.6rem 0;
}

/* --------------------------------------------------------- Sprungmarke */

.sprungmarke {
  background: var(--gelb); color: var(--tuerkis-nacht); font-weight: 600;
}

/* --------------------------------------------------------- Kopfbereich */

.kopfbereich {
  background: transparent;
  border-bottom: 1px solid transparent;
  transition: background .25s ease, border-color .25s ease;
}
.kopfbereich.ist-gescrollt {
  background: var(--tuerkis-nacht);
  border-bottom-color: rgba(247, 207, 29, .28);
}
/* Auf Unterseiten liegt kein Bild hinter dem Kopf */
.seite:not(.seite-index) .kopfbereich { background: var(--tuerkis-nacht); }

/* Das Logo bleibt schwarz-grün und bekommt dafür eine weiße Plakette */
.logo {
  background: var(--weiss);
  padding: .4rem .65rem;
  border-radius: var(--rundung);
}

.hauptnavigation {
  margin-left: auto; display: flex; align-items: center; gap: var(--abstand-klein);
}
.navi-liste { gap: 1.6rem; }
.navi-punkt > a {
  color: var(--creme); font-size: .95rem; padding: .5rem 0;
  border-bottom: 1px solid transparent;
}
.navi-punkt > a:hover { color: var(--gelb-hell); }
.navi-punkt.ist-aktiv > a { color: var(--gelb); border-bottom-color: var(--gelb); }

.untermenue {
  display: none; position: absolute; left: -1rem; top: 100%;
  min-width: 17rem; padding: .5rem 0;
  background: var(--tuerkis-nacht);
  border-top: 2px solid var(--gelb);
  box-shadow: 0 18px 40px rgba(0, 0, 0, .45);
}
.untermenue a { color: var(--creme); padding: .6rem 1.2rem; font-size: .92rem; }
.untermenue a:hover { background: var(--tuerkis-dunkel); color: var(--gelb-hell); }

.navi-spende {
  background: var(--gelb); color: var(--tuerkis-nacht);
  padding: .65rem 1.35rem; text-decoration: none;
  font-size: .8rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .12em;
  border-radius: var(--rundung); transition: background .2s ease;
}
.navi-spende:hover { background: var(--gelb-hell); color: var(--tuerkis-nacht); }

.menue-schalter { color: var(--creme); margin-left: auto; }
.menue-wort { font-size: .78rem; text-transform: uppercase; letter-spacing: .14em; }

@media (max-width: 899px) {
  .menue-schalter { display: flex; }
  .hauptnavigation {
    position: fixed; inset: 0 0 0 auto; width: min(22rem, 88vw);
    background: var(--tuerkis-nacht);
    border-left: 1px solid var(--tuerkis-linie);
    flex-direction: column; align-items: stretch; justify-content: flex-start;
    gap: 0; padding: 5.5rem 1.75rem 2rem;
    transform: translateX(100%); transition: transform .28s ease;
    overflow-y: auto;
  }
  .hauptnavigation.ist-offen { transform: translateX(0); }
  .navi-liste { flex-direction: column; align-items: stretch; gap: 0; }
  .navi-punkt { border-bottom: 1px solid var(--tuerkis-linie); }
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

/* --------------------------------------------------------- Aufmacher */

.hero { position: relative; display: grid; min-height: min(88vh, 760px); overflow: hidden; }
.hero > * { grid-area: 1 / 1; }
.hero-bild {
  width: 100%; height: 100%; object-fit: cover;
  transform: scale(1.06); will-change: transform;
}
/* Schleier wie in Entwurf 1: von links und von unten – das Foto bleibt
   sichtbar. Das Bild trägt für die Parallaxe ein transform und bildet damit
   einen eigenen Stapelkontext; Schleier und Inhalt brauchen einen z-index. */
.hero-schleier {
  position: relative; z-index: 1;
  background:
    linear-gradient(to bottom, rgba(10, 46, 51, .30) 0%, rgba(14, 58, 65, .72) 58%, rgba(21, 88, 100, .96) 100%),
    linear-gradient(to right, var(--tuerkis-nacht) 0%, rgba(14, 58, 65, .55) 55%, rgba(28, 118, 134, .3) 100%);
}
.hero-inhalt {
  position: relative; z-index: 2;
  align-self: end; padding-block: clamp(3rem, 9vw, 6rem);
}
.hero-dachzeile {
  font-size: .78rem; font-weight: 600; text-transform: uppercase;
  letter-spacing: .2em; color: var(--gelb); margin-bottom: 1.2rem;
}
.hero h1 { max-width: 18ch; margin-bottom: .35em; }
.hero-text { font-size: 1.2em; max-width: 52ch; color: var(--creme); }

/* Zurückhaltende Einfahrt beim Laden */
@media (prefers-reduced-motion: no-preference) {
  .hero-dachzeile, .hero h1, .hero-text, .hero .schaltflaechen {
    animation: aufsteigen .75s cubic-bezier(.22, .8, .3, 1) backwards;
  }
  .hero-dachzeile { animation-delay: .05s; }
  .hero h1 { animation-delay: .16s; }
  .hero-text { animation-delay: .28s; }
  .hero .schaltflaechen { animation-delay: .4s; }
}
@keyframes aufsteigen {
  from { opacity: 0; transform: translateY(1.2rem); }
  to   { opacity: 1; transform: none; }
}

/* --------------------------------------------------------- Merkmalstreifen */

.merkmale {
  background: var(--verlauf-tief);
  border-bottom: 1px solid var(--tuerkis-linie);
  padding-block: clamp(1.5rem, 3.5vw, 2.25rem);
}
.merkmal-liste {
  list-style: none; display: grid; gap: var(--abstand-klein) var(--abstand-mittel);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 12rem), 1fr));
}
.merkmal { display: grid; gap: .05rem; }
.merkmal-titel {
  font-family: var(--serif); font-size: 1.45rem; font-weight: 600;
  color: var(--gelb); line-height: 1.15;
}
.merkmal-text {
  font-size: .78rem; color: var(--creme-gedaempft);
  text-transform: uppercase; letter-spacing: .1em;
}

/* --------------------------------------------------------- Abschnitte */

/* Türkise Abschnitte erben die Farbvariablen aus :root.
   Helle Abschnitte setzen sie neu – alle Bausteine folgen automatisch. */
.abschnitt-hell, .abschnitt-text {
  --text:          var(--tinte);
  --text-leise:    #4a6b74;
  --ueberschrift:  var(--tuerkis-nacht);
  --verweis:       #0f6a74;
  --verweis-hover: #0a4f57;
  --kicker-farbe:  #0f6a74;
  --flaeche:       var(--weiss);
  --linie:         #cddbe0;
  background: var(--verlauf-hell);
  color: var(--text);
}
.abschnitt-zitat { background: var(--verlauf-flaeche); text-align: center; }
.abschnitt-aufruf { background: var(--verlauf-tief); }
.abschnitt-text { padding-block: var(--abstand-abschnitt); }

.seitenkopf {
  background: var(--verlauf-tief);
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2rem, 5vw, 3.5rem);
}
.seitenkopf h1 { max-width: 20ch; }

/* Einfahren beim Scrollen – nur ein leichtes Aufsteigen */
.faehrt-ein { opacity: 0; transform: translateY(1.1rem); }
.faehrt-ein.ist-da {
  opacity: 1; transform: none;
  transition: opacity .6s ease, transform .6s cubic-bezier(.22, .8, .3, 1);
}
.karte.faehrt-ein.ist-da, .person.faehrt-ein.ist-da {
  transition-delay: calc(var(--folge, 0) * 80ms);
}
.karte:nth-child(2), .person:nth-child(2) { --folge: 1; }
.karte:nth-child(3), .person:nth-child(3) { --folge: 2; }
.karte:nth-child(4), .person:nth-child(4) { --folge: 3; }
.karte:nth-child(5), .person:nth-child(5) { --folge: 4; }

/* --------------------------------------------------------- Schaltflächen */

.schaltflaeche {
  padding: .85rem 1.7rem; border-radius: var(--rundung);
  font-size: .8rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .12em;
  transition: background .2s ease, color .2s ease, border-color .2s ease;
}
.stufe-1 {
  background: var(--gelb); color: var(--tuerkis-nacht);
  border: 1px solid var(--gelb);
}
.stufe-1:hover {
  background: var(--gelb-hell); border-color: var(--gelb-hell);
  color: var(--tuerkis-nacht);
}
.stufe-2 {
  background: transparent; color: var(--gelb);
  border: 1px solid rgba(247, 207, 29, .55);
}
.stufe-2:hover {
  background: rgba(247, 207, 29, .12); border-color: var(--gelb); color: var(--gelb-hell);
}
/* Auf hellem Grund ist Gelb als Schrift zu schwach – dort steht Türkis */
.abschnitt-hell .stufe-2, .abschnitt-text .stufe-2 {
  color: #0f6a74; border-color: rgba(15, 106, 116, .5);
}
.abschnitt-hell .stufe-2:hover, .abschnitt-text .stufe-2:hover {
  background: rgba(15, 106, 116, .1); border-color: #0f6a74; color: #0a4f57;
}

/* --------------------------------------------------------- Karten */

.karte {
  background: var(--flaeche);
  border: 1px solid var(--linie);
  border-top: 2px solid var(--gelb);
  border-radius: var(--rundung);
  padding: var(--abstand-mittel);
  display: flex; flex-direction: column; gap: .35rem;
  transition: transform .22s ease, border-top-color .22s ease, box-shadow .22s ease;
}
.karte:hover {
  transform: translateY(-4px);
  border-top-color: var(--gelb-hell);
  box-shadow: 0 16px 34px rgba(0, 0, 0, .28);
}
.abschnitt-hell .karte { box-shadow: 0 4px 14px rgba(16, 46, 45, .06); }
.abschnitt-hell .karte:hover { box-shadow: 0 16px 30px rgba(16, 46, 45, .12); }
.karte-bild {
  width: calc(100% + 2 * var(--abstand-mittel));
  margin: calc(-1 * var(--abstand-mittel)) calc(-1 * var(--abstand-mittel)) var(--abstand-klein);
  aspect-ratio: 3 / 2; object-fit: cover;
  filter: saturate(.85) brightness(.92); transition: filter .25s ease;
}
.karte:hover .karte-bild { filter: none; }
.karte-titel { font-size: 1.35rem; margin-bottom: .2em; }
.karte-text { color: var(--text-leise); margin-bottom: .6em; }
.karte-verweis {
  margin-top: auto; font-size: .78rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .12em; text-decoration: none;
}

/* --------------------------------------------------------- Bilder */

.bild img, .reihe-bild img, .galerie img, .person-bild img {
  filter: saturate(.85); transition: filter .3s ease;
  border-radius: var(--rundung);
}
.bild:hover img, .reihe-bild:hover img, .galerie a:hover img { filter: none; }
.bild figcaption, .reihe-bild figcaption {
  font-size: .85rem; color: var(--text-leise); margin-top: .6rem;
}
.spalte-bild .bild img { box-shadow: 0 20px 50px rgba(0, 0, 0, .3); }

/* --------------------------------------------------------- Zitat */

.zitat { position: relative; max-width: 46rem; margin-inline: auto; padding-top: 2rem; }
.zitat::before {
  content: '\\201C'; position: absolute; top: -1.4rem; left: 50%; transform: translateX(-50%);
  font-family: var(--serif); font-size: 6rem; line-height: 1;
  color: var(--gelb); opacity: .5;
}
.zitat blockquote { margin: 0; }
.zitat p {
  font-family: var(--serif); font-style: italic;
  font-size: clamp(1.4rem, 2.6vw, 2.1rem); line-height: 1.4;
  color: var(--weiss); max-width: none;
}
.zitat figcaption {
  font-size: .78rem; text-transform: uppercase; letter-spacing: .16em;
  color: var(--gelb); margin-top: 1.4rem;
}

/* --------------------------------------------------------- Listen */

.nummer {
  font-family: var(--serif); font-size: 2rem; line-height: 1;
  color: var(--gelb);
}
.abschnitt-hell .nummer, .abschnitt-text .nummer { color: var(--gelb-tief); }
.nummer-punkt h3 { margin-bottom: .25em; }
.nummer-punkt p { color: var(--text-leise); margin: 0; }

/* --------------------------------------------------------- Personen */

.person-name { font-size: 1.2rem; margin: .9rem 0 .1em; }
.person-rolle { color: var(--gelb); font-size: .9rem; margin: 0 0 .1em; }
.abschnitt-hell .person-rolle { color: var(--gelb-tief); }
.person-zusatz { color: var(--text-leise); font-size: .85rem; margin: 0; }
.person-initialen {
  background: var(--flaeche); border: 1px solid var(--linie);
  color: var(--gelb); font-family: var(--serif);
}
.abschnitt-hell .person-initialen { color: var(--gelb-tief); }

/* --------------------------------------------------------- Konto */

.konto {
  background: var(--flaeche); border: 1px solid var(--linie);
  border-left: 2px solid var(--gelb);
  padding: var(--abstand-mittel); margin-bottom: var(--abstand-klein);
  color: var(--text);
}
.konto-titel { font-size: 1.15rem; color: var(--ueberschrift); }
.konto-daten dt { color: var(--text-leise); font-weight: 400; font-size: .9rem; }
.konto-daten dd { color: var(--text); }
.iban-kopieren {
  margin-left: .6rem; background: transparent; color: var(--verweis);
  border: 1px solid var(--linie); border-radius: var(--rundung);
  padding: .2rem .6rem; font-size: .75rem;
  transition: background .2s ease, border-color .2s ease;
}
.iban-kopieren:hover { border-color: var(--gelb); }
.iban-kopieren.ist-kopiert {
  background: var(--gelb); color: var(--tuerkis-nacht); border-color: var(--gelb);
}

/* --------------------------------------------------------- Downloads */

.download {
  background: var(--flaeche); border: 1px solid var(--linie);
  padding: .9rem 1.2rem; color: var(--text);
  transition: border-color .2s ease;
}
.download:hover { border-color: var(--gelb); }
.download-art {
  font-size: .7rem; font-weight: 600; letter-spacing: .12em;
  color: var(--tuerkis-nacht); background: var(--gelb);
  padding: .2rem .5rem; border-radius: var(--rundung); flex: 0 0 auto;
}

/* --------------------------------------------------------- Aufruf */

.aufruf {
  position: relative;
  border: 1px solid rgba(247, 207, 29, .4);
  padding: var(--abstand-gross); text-align: center;
}
.aufruf::before {
  content: ''; position: absolute; left: 0; right: 0; top: 0; height: 2px;
  background: var(--verlauf-kante);
}
.aufruf p { margin-inline: auto; }
.aufruf .schaltflaechen { justify-content: center; }

/* --------------------------------------------------------- Satzung */

.inhaltsverzeichnis {
  background: var(--flaeche); border: 1px solid var(--linie);
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
.paragraf li { color: var(--text); }
.paragraf li::marker { color: var(--gelb-tief); }

/* --------------------------------------------------------- Formular */

.formular-block { max-width: 52rem; }
.formfeld input, .formfeld select, .formfeld textarea {
  background: var(--weiss); color: var(--tinte);
  border: 1px solid var(--linie); border-radius: var(--rundung);
  transition: border-color .2s ease, box-shadow .2s ease;
}
.formfeld input:focus, .formfeld select:focus, .formfeld textarea:focus {
  border-color: var(--gelb); outline: none;
  box-shadow: 0 0 0 3px rgba(247, 207, 29, .3);
}
.formfeld label { font-size: .9rem; }
.pflicht { color: #a8710a; }
.feldfehler { color: #a32d16; }
.hat-fehler input, .hat-fehler select, .hat-fehler textarea { border-color: #c2452a; }
.formular-meldung {
  padding: .9rem 1.1rem; border-left: 2px solid var(--gelb);
  background: var(--nebel-hell);
}
.meldung-erfolg { border-left-color: #2e7d59; }
.meldung-fehler { border-left-color: #c2452a; }
.formfeld-haken label { font-size: .92rem; color: var(--text-leise); }

/* --------------------------------------------------------- Anschrift */

.anschrift { font-size: 1.05rem; line-height: 1.9; }

/* --------------------------------------------------------- Lichtkasten */

.lichtkasten { background: rgba(10, 46, 51, .96); }
.lichtkasten button { color: var(--creme); }
.lichtkasten button:hover { color: var(--gelb); }
.lichtkasten-zurueck, .lichtkasten-weiter { font-size: 2.4rem; padding: .3rem .8rem; }
.lichtkasten-schliessen {
  font-size: .78rem; text-transform: uppercase; letter-spacing: .14em;
  border: 1px solid rgba(247, 207, 29, .5); padding: .5rem 1rem;
}
.lichtkasten-zaehler { color: var(--creme-gedaempft); font-size: .85rem; }

/* --------------------------------------------------------- Fußbereich */

.fussbereich {
  background: var(--verlauf-tief);
  border-top: 1px solid rgba(247, 207, 29, .3);
  color: var(--creme);
}
.fuss-marke img {
  background: var(--weiss); padding: .45rem .65rem;
  border-radius: var(--rundung); width: min(205px, 62%);
}
.fuss-titel {
  font-family: var(--sans); font-size: .75rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: .16em; color: var(--gelb);
  margin-bottom: 1rem;
}
.fussbereich p, .fussbereich address, .fussbereich a {
  color: var(--creme-gedaempft); font-size: .92rem;
}
.fussbereich a:hover { color: var(--gelb-hell); }
.fussbereich .fuss-claim {
  font-family: var(--serif); font-size: 1.25rem; font-style: italic;
  color: var(--gelb); margin: .8rem 0 .5rem;
}
.fuss-zeile { border-top: 1px solid var(--tuerkis-linie); font-size: .85rem; }
.fuss-zeile p { margin: 0; font-size: .85rem; }
"""
