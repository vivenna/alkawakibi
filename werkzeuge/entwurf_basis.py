# -*- coding: utf-8 -*-
"""Basisklasse eines Entwurfs: HTML-Rahmen, Kopf, Fuß und alle Bausteine.

Die drei Entwürfe erben hiervon und überschreiben, was sie anders machen.
"""
import os

import inhalte as I
from basis import e, formular_felder_html


class Entwurf:
    # --- von den Entwürfen zu setzen ---
    kennung = 'basis'
    name = 'Basis'
    ordner = '.'
    schriften = []                      # Dateinamen in assets/schriften/
    logo = 'assets/bilder/logo.png'
    logo_fuss = 'assets/bilder/logo.png'
    og_bild = I.HERO['bild']
    farbe_browser = '#0d4a0d'           # theme-color

    # ---------------------------------------------------------- HTML-Rahmen

    def rahmen(self, datei, inhalt):
        s = I.SEITEN[datei]
        schriften = '\n'.join(
            '  <link rel="stylesheet" href="assets/schriften/%s.css">' % n
            for n in self.schriften)
        noindex = '\n  <meta name="robots" content="noindex">' if datei == '404.html' else ''
        return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(s['titel'])}</title>
  <meta name="description" content="{e(s['beschreibung'])}">{noindex}
  <meta name="theme-color" content="{self.farbe_browser}">
  <meta property="og:title" content="{e(s['titel'])}">
  <meta property="og:description" content="{e(s['beschreibung'])}">
  <meta property="og:image" content="{self.og_bild}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="de_DE">
  <link rel="icon" href="assets/bilder/favicon-32.png" sizes="32x32">
  <link rel="apple-touch-icon" href="assets/bilder/apple-touch-icon.png">
{schriften}
  <link rel="stylesheet" href="assets/css/stil.css">
</head>
<body class="seite seite-{datei.replace('.html', '')}">
  <a class="sprungmarke" href="#inhalt">Zum Inhalt springen</a>
{self.kopf(datei)}
  <main id="inhalt">
{inhalt}
  </main>
{self.fuss()}
  <script src="assets/js/konfiguration.js" defer></script>
  <script src="assets/js/haupt.js" defer></script>
</body>
</html>"""

    # ---------------------------------------------------------- Kopf und Fuß

    def navigation(self, aktiv):
        punkte = []
        for eintrag in I.NAVIGATION:
            ist_aktiv = (eintrag['ziel'] == aktiv
                         or any(u['ziel'].split('#')[0] == aktiv for u in eintrag['unter']))
            marke = ' aria-current="page"' if eintrag['ziel'] == aktiv else ''
            klasse = ' class="ist-aktiv"' if ist_aktiv else ''
            if eintrag['unter']:
                unter = '\n'.join(
                    '            <li><a href="%s">%s</a></li>' % (u['ziel'], e(u['titel']))
                    for u in eintrag['unter'])
                kennung = 'untermenue-' + eintrag['ziel'].replace('.html', '')
                punkte.append(f"""        <li class="navi-punkt hat-untermenue{klasse and ' ist-aktiv'}">
          <a href="{eintrag['ziel']}"{marke}>{e(eintrag['titel'])}</a>
          <button class="untermenue-schalter" type="button" aria-expanded="false" aria-controls="{kennung}">
            <span class="nur-vorlesen">Untermenü {e(eintrag['titel'])} öffnen</span>
            <span class="pfeil" aria-hidden="true"></span>
          </button>
          <ul class="untermenue" id="{kennung}">
{unter}
          </ul>
        </li>""")
            else:
                punkte.append(
                    '        <li class="navi-punkt%s"><a href="%s"%s>%s</a></li>'
                    % (klasse and ' ist-aktiv', eintrag['ziel'], marke, e(eintrag['titel'])))
        return '\n'.join(punkte)

    def kopf(self, aktiv):
        return f"""  <header class="kopfbereich" id="kopfbereich">
    <div class="kopf-huelle">
      <a class="logo" href="index.html">
        <img src="{self.logo}" alt="{e(I.VEREIN['kurz'])} – {e(I.VEREIN['claim'])}" width="220" height="79">
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
      </nav>
    </div>
  </header>"""

    def fuss(self):
        spalten = []
        for titel, punkte in I.FUSS_SPALTEN:
            eintraege = '\n'.join(
                '          <li><a href="%s">%s</a></li>' % (ziel, e(text))
                for text, ziel in punkte)
            spalten.append(f"""      <div class="fuss-spalte">
        <h2 class="fuss-titel">{e(titel)}</h2>
        <ul>
{eintraege}
        </ul>
      </div>""")
        v = I.VEREIN
        return f"""  <footer class="fussbereich">
    <div class="fuss-huelle">
      <div class="fuss-spalte fuss-marke">
        <img src="{self.logo_fuss}" alt="{e(v['kurz'])}" width="200" height="72" loading="lazy">
        <p class="fuss-claim">{e(v['claim'])}</p>
        <p>Deutsch-syrischer Verein für Menschenrechte, demokratische Bildung und
           Zivilgesellschaft. Sitz in Berlin.</p>
      </div>
{chr(10).join(spalten)}
      <div class="fuss-spalte">
        <h2 class="fuss-titel">Kontakt</h2>
        <address>
          {e(v['name'])}<br>
          {e(v['strasse'])}<br>
          {e(v['ort'])}<br>
          <a href="mailto:{v['email']}">{v['email']}</a>
        </address>
        <p><a href="kontakt.html#kontaktformular">Zum Kontaktformular</a></p>
      </div>
    </div>
    <div class="fuss-zeile">
      <p>© {v['jahr']} {e(v['name'])} · Gemeinnütziger Verein · {v['registernummer']} · {e(v['registergericht'])}</p>
      <p><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a></p>
    </div>
  </footer>"""

    # ---------------------------------------------------------- Bausteine

    def abschnitt(self, inhalt, ton=None):
        klasse = 'abschnitt' + (' abschnitt-' + ton if ton else '')
        return f'    <section class="{klasse}">\n      <div class="huelle">\n{inhalt}\n      </div>\n    </section>'

    def kicker(self, text):
        return '        <p class="kicker">%s</p>\n' % e(text)

    def h2(self, text):
        return '        <h2>%s</h2>\n' % e(text)

    def unterzeile(self, text):
        return '        <p class="unterzeile">%s</p>\n' % e(text)

    def absatz(self, text, roh=False):
        return '        <p>%s</p>\n' % (text if roh or '<a ' in text else e(text))

    def hinweis(self, text, stark=False):
        klasse = 'hinweis hinweis-stark' if stark else 'hinweis'
        return '        <p class="%s">%s</p>\n' % (klasse, e(text))

    def hervorhebung(self, text):
        return '        <p class="hervorhebung">%s</p>\n' % e(text)

    def schaltflaechen(self, liste):
        if not liste:
            return ''
        teile = []
        for text, ziel, stufe in liste:
            teile.append('          <a class="schaltflaeche stufe-%d" href="%s">%s</a>'
                         % (stufe, ziel, e(text)))
        return '        <p class="schaltflaechen">\n%s\n        </p>\n' % '\n'.join(teile)

    def zweispalter(self, links, rechts, bild_zuerst=False):
        klasse = 'zweispalter' + (' bild-zuerst' if bild_zuerst else '')
        return (f'        <div class="{klasse}">\n'
                f'          <div class="spalte-text">\n{links}          </div>\n'
                f'          <div class="spalte-bild">\n{rechts}          </div>\n'
                f'        </div>\n')

    def bild(self, quelle, alt, unterschrift, breite, hoehe, lazy=True):
        laden = ' loading="lazy"' if lazy else ''
        img = ('<img src="%s" alt="%s" width="%d" height="%d"%s>'
               % (quelle, e(alt), breite, hoehe, laden))
        if unterschrift:
            return ('            <figure class="bild">\n              %s\n'
                    '              <figcaption>%s</figcaption>\n            </figure>\n'
                    % (img, e(unterschrift)))
        return '            <figure class="bild">\n              %s\n            </figure>\n' % img

    def bildreihe(self, bilder):
        teile = []
        for quelle, alt in bilder:
            teile.append('          <figure class="reihe-bild"><img src="%s" alt="%s" '
                         'width="800" height="600" loading="lazy"></figure>'
                         % (quelle, e(alt)))
        return '        <div class="bildreihe">\n%s\n        </div>\n' % '\n'.join(teile)

    def karten(self, liste):
        teile = []
        for k in liste:
            innen = ''
            if k.get('bild'):
                innen += ('          <img class="karte-bild" src="%s" alt="%s" '
                          'width="800" height="533" loading="lazy">\n'
                          % (k['bild'], e(k.get('alt', ''))))
            innen += '          <h3 class="karte-titel">%s</h3>\n' % e(k['titel'])
            innen += '          <p class="karte-text">%s</p>\n' % e(k['text'])
            if k.get('ziel'):
                innen += ('          <a class="karte-verweis" href="%s">%s<span aria-hidden="true"> →</span></a>\n'
                          % (k['ziel'], e(k.get('linktext', 'Weiterlesen'))))
            teile.append('        <article class="karte">\n%s        </article>' % innen)
        return '        <div class="karten">\n%s\n        </div>\n' % '\n'.join(teile)

    def nummernliste(self, liste):
        teile = []
        for nummer, (titel, text) in enumerate(liste, 1):
            teile.append('          <li class="nummer-punkt">\n'
                         '            <span class="nummer" aria-hidden="true">%02d</span>\n'
                         '            <div><h3>%s</h3><p>%s</p></div>\n'
                         '          </li>' % (nummer, e(titel), e(text)))
        return '        <ol class="nummernliste">\n%s\n        </ol>\n' % '\n'.join(teile)

    def personen(self, liste):
        teile = []
        for p in liste:
            if p['bild']:
                bild = ('<img src="%s" alt="Porträt von %s" width="800" height="1000" loading="lazy">'
                        % (p['bild'], e(p['name'])))
            else:
                bild = ('<span class="person-initialen" aria-hidden="true">%s</span>'
                        % e(p['initialen']))
            teile.append('          <li class="person">\n'
                         '            <div class="person-bild">%s</div>\n'
                         '            <h3 class="person-name">%s</h3>\n'
                         '            <p class="person-rolle">%s</p>\n'
                         '            <p class="person-zusatz">%s</p>\n'
                         '          </li>'
                         % (bild, e(p['name']), e(p['rolle']), e(p['zusatz'])))
        return '        <ul class="personen">\n%s\n        </ul>\n' % '\n'.join(teile)

    def konto(self, k):
        return f"""        <div class="konto">
          <h3 class="konto-titel">{e(k['titel'])}</h3>
          <dl class="konto-daten">
            <dt>Empfänger</dt><dd>{e(k['inhaber'])}</dd>
            <dt>IBAN</dt><dd><span class="iban">{k['iban']}</span>
              <button class="iban-kopieren" type="button" data-iban="{k['iban'].replace(' ', '')}" hidden>IBAN kopieren</button></dd>
            <dt>BIC</dt><dd>{k['bic']}</dd>
            <dt>Bank</dt><dd>{e(k['bank'])}</dd>
            <dt>Verwendungszweck</dt><dd>{e(k['zweck'])}</dd>
          </dl>
        </div>
"""

    def downloads(self, liste):
        teile = []
        for titel, art, ziel, sprache in liste:
            attr = ' lang="ar" dir="rtl"' if sprache == 'ar' else ''
            teile.append('          <li><a class="download" href="%s" download>'
                         '<span class="download-art">%s</span>'
                         '<span class="download-titel"%s>%s</span></a></li>'
                         % (ziel, art, attr, e(titel)))
        return '        <ul class="downloads">\n%s\n        </ul>\n' % '\n'.join(teile)

    def galerie(self, bilder):
        teile = []
        for basis_pfad, alt in bilder:
            klein = basis_pfad + '-800.jpg'
            gross = basis_pfad + '-1600.jpg'
            gross_da = os.path.exists(os.path.join(self.ordner, gross))
            ziel = gross if gross_da else klein
            teile.append('          <li><a class="galerie-bild" href="%s" '
                         'data-gross="%s"><img src="%s" alt="%s" width="800" '
                         'height="600" loading="lazy"></a></li>'
                         % (ziel, ziel, klein, e(alt)))
        return '        <ul class="galerie">\n%s\n        </ul>\n' % '\n'.join(teile)

    def zitat(self, text, quelle):
        return (f'        <figure class="zitat">\n'
                f'          <blockquote><p>{e(text)}</p></blockquote>\n'
                f'          <figcaption>{e(quelle)}</figcaption>\n'
                f'        </figure>\n')

    def aufruf(self, titel, text, schaltflaechen):
        return (f'        <div class="aufruf">\n'
                f'          <h2>{e(titel)}</h2>\n'
                f'          <p>{e(text)}</p>\n'
                f'{self.schaltflaechen(schaltflaechen)}'
                f'        </div>\n')

    def anschrift(self):
        v = I.VEREIN
        return (f'        <address class="anschrift">\n'
                f'          <strong>{e(v["name"])}</strong><br>\n'
                f'          {e(v["strasse"])}<br>\n'
                f'          {e(v["ort"])}<br>\n'
                f'          <a href="mailto:{v["email"]}">{v["email"]}</a>\n'
                f'        </address>\n')

    # ---------------------------------------------------------- Formular

    def feld(self, kennung, beschriftung, art, pflicht, autofill):
        stern = ' <span class="pflicht" aria-hidden="true">*</span>' if pflicht else ''
        erf = ' required' if pflicht else ''
        return f"""          <div class="formfeld">
            <label for="{kennung}">{e(beschriftung)}{stern}</label>
            <input type="{art}" id="{kennung}" name="{kennung}" autocomplete="{autofill}"
                   aria-describedby="fehler-{kennung}"{erf}>
            <span class="feldfehler" id="fehler-{kennung}"></span>
          </div>"""

    def auswahl(self, kennung, beschriftung, werte, pflicht):
        stern = ' <span class="pflicht" aria-hidden="true">*</span>' if pflicht else ''
        optionen = '\n'.join('              <option value="%s">%s</option>' % (e(w), e(w))
                             for w in werte)
        return f"""          <div class="formfeld">
            <label for="{kennung}">{e(beschriftung)}{stern}</label>
            <select id="{kennung}" name="{kennung}" aria-describedby="fehler-{kennung}" required>
{optionen}
            </select>
            <span class="feldfehler" id="fehler-{kennung}"></span>
          </div>"""

    def textfeld(self, kennung, beschriftung, pflicht):
        stern = ' <span class="pflicht" aria-hidden="true">*</span>' if pflicht else ''
        return f"""          <div class="formfeld formfeld-breit">
            <label for="{kennung}">{e(beschriftung)}{stern}</label>
            <textarea id="{kennung}" name="{kennung}" rows="7"
                      aria-describedby="fehler-{kennung}" required></textarea>
            <span class="feldfehler" id="fehler-{kennung}"></span>
          </div>"""

    def haken(self, kennung, beschriftung, pflicht):
        return f"""          <div class="formfeld formfeld-breit formfeld-haken">
            <input type="checkbox" id="{kennung}" name="{kennung}"
                   aria-describedby="fehler-{kennung}" required>
            <label for="{kennung}">{beschriftung} <span class="pflicht" aria-hidden="true">*</span></label>
            <span class="feldfehler" id="fehler-{kennung}"></span>
          </div>"""

    def formular(self):
        return f"""        <div class="formular-block" id="kontaktformular">
          <h2>Kontaktformular</h2>
          <p>Felder mit <span aria-hidden="true">*</span><span class="nur-vorlesen">Stern</span> sind Pflichtfelder.</p>
          <form class="kontaktformular" id="kontaktformular-formular" method="post"
                action="mailto:{I.VEREIN['email']}" enctype="text/plain">
            <div class="formfelder">
{formular_felder_html(self)}
            </div>
            <div class="honigtopf" aria-hidden="true">
              <label for="website">Bitte nicht ausfüllen</label>
              <input type="text" id="website" name="website" tabindex="-1" autocomplete="off">
            </div>
            <p class="formular-senden">
              <button class="schaltflaeche stufe-1" type="submit">Nachricht senden</button>
            </p>
            <p class="formular-meldung" id="formular-meldung" role="status"></p>
          </form>
        </div>
"""

    # ---------------------------------------------------------- Satzung

    def inhaltsverzeichnis(self, paragrafen):
        teile = '\n'.join('          <li><a href="#%s">%s</a></li>' % (p['id'], e(p['titel']))
                          for p in paragrafen)
        return ('        <nav class="inhaltsverzeichnis" aria-label="Inhaltsverzeichnis der Satzung">\n'
                '          <h2>Auf dieser Seite</h2>\n          <ol>\n%s\n          </ol>\n'
                '        </nav>\n' % teile)

    def satzungstext(self, paragrafen):
        teile = []
        for p in paragrafen:
            innen = '          <h2 id="%s">%s</h2>\n' % (p['id'], e(p['titel']))
            offen = None
            for art, text in p['knoten']:
                if art == 'punkt':
                    if offen != 'ol':
                        if offen:
                            innen += '          </%s>\n' % offen
                        innen += '          <ol class="satzung-punkte">\n'
                        offen = 'ol'
                    innen += '            <li>%s</li>\n' % e(text)
                elif art == 'unterpunkt':
                    if offen != 'ul':
                        if offen:
                            innen += '          </%s>\n' % offen
                        innen += '          <ul class="satzung-unterpunkte">\n'
                        offen = 'ul'
                    innen += '            <li>%s</li>\n' % e(text)
                else:
                    if offen:
                        innen += '          </%s>\n' % offen
                        offen = None
                    if art == 'zwischentitel':
                        innen += '          <h3>%s</h3>\n' % e(text)
                    else:
                        innen += '          <p>%s</p>\n' % e(text)
            if offen:
                innen += '          </%s>\n' % offen
            teile.append('        <section class="paragraf">\n%s        </section>' % innen)
        return '\n'.join(teile)

    # ---------------------------------------------------------- Seitenköpfe

    def seitenkopf(self, datei):
        s = I.SEITEN[datei]
        teile = ''
        if s.get('kicker'):
            teile += '        <p class="kicker">%s</p>\n' % e(s['kicker'])
        teile += '        <h1>%s</h1>\n' % e(s['h1'])
        if s.get('einleitung'):
            teile += '        <p class="einleitung">%s</p>\n' % e(s['einleitung'])
        return ('    <section class="seitenkopf">\n      <div class="huelle">\n'
                '%s      </div>\n    </section>' % teile)

    def hero(self):
        h = I.HERO
        titel = e(h['titel']).replace(
            e(h['hervor']), '<span class="hervor">%s</span>' % e(h['hervor']))
        return f"""    <section class="hero">
      <img class="hero-bild" src="{h['bild']}" alt="{e(h['alt'])}" width="{h['breite']}" height="{h['hoehe']}" fetchpriority="high">
      <div class="hero-inhalt huelle">
        <p class="hero-dachzeile">{e(h['dachzeile'])}</p>
        <h1>{titel}</h1>
        <p class="hero-text">{e(h['text'])}</p>
        <p class="schaltflaechen">
          <a class="schaltflaeche stufe-1" href="aktivitaeten.html">Unsere Aktivitäten</a>
          <a class="schaltflaeche stufe-2" href="spenden.html">Jetzt spenden</a>
        </p>
      </div>
    </section>"""

    def textbereich(self, seitenleiste, haupt):
        """Langer Textbereich, bei manchen Entwürfen mit Seitenleiste."""
        return ('        <div class="textbereich">\n'
                '%s'
                '          <div class="textspalte">\n%s          </div>\n'
                '        </div>\n' % (seitenleiste, haupt))

    def randspalte(self, seite):
        """Kästen neben Rechtstexten. Standard: nichts."""
        return ''

    # ---------------------------------------------------------- Zusätze

    def js_zusatz(self):
        return ''

    def js_start(self):
        return ''

    def css(self):
        raise NotImplementedError

    def liesmich(self):
        seiten = '\n'.join('- `%s`' % s for s in I.REIHENFOLGE)
        return f"""# Entwurf: {self.name}

Vollständiger Entwurf für die Website des {I.VEREIN['name']} –
zwölf Seiten plus Fehlerseite, reines HTML, CSS und JavaScript.

Diese Dateien werden erzeugt – von Hand geändert wird in `werkzeuge/`,
siehe unten.

## Veröffentlichen über GitHub Pages

Repository-Einstellungen → *Pages* → *Build and deployment* →
*Source: GitHub Actions*, dann in `.github/workflows/` den Ordner
`frontend/{self.kennung}` als Veröffentlichungsquelle eintragen.

Zum Ansehen genügt lokal:

```
python3 -m http.server -d frontend/{self.kennung} 8000
```

## Seiten

{seiten}

Dazu `404.html`, `robots.txt`, `sitemap.xml` und `.nojekyll`.

## Kontaktformular

Der Endpunkt wird in `assets/js/konfiguration.js` eingetragen. Einrichtung des
Backends (Google Apps Script schreibt nach Supabase): siehe `backend/README.md`
im Projektordner. Ohne Endpunkt bleibt die Seite benutzbar – das Formular bietet
dann den Versand über das E-Mail-Programm an.

## Ändern

Die Seiten werden aus `werkzeuge/` erzeugt, damit alle drei Entwürfe dieselben
Texte tragen:

```
python3 werkzeuge/bauen.py
```

Texte stehen in `werkzeuge/inhalte.py` (Quelle: `inhalte/redaktionsplan.md`),
die Gestaltung dieses Entwurfs in `werkzeuge/{self.kennung.split('-')[0]}{self.kennung.split('-')[1]}.py`.
Wer lieber direkt im HTML arbeitet, kann das tun – dann sollte der Bauläufer
allerdings nicht mehr über die Dateien laufen.
"""
