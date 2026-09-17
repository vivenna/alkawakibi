# Entwurf: Institut

Vollständiger Entwurf für die Website des Alkawakibi Verein e. V. –
zwölf Seiten plus Fehlerseite, reines HTML, CSS und JavaScript.

Diese Dateien werden erzeugt – von Hand geändert wird in `werkzeuge/`,
siehe unten.

## Veröffentlichen über GitHub Pages

Repository-Einstellungen → *Pages* → *Build and deployment* →
*Source: GitHub Actions*, dann in `.github/workflows/` den Ordner
`frontend/entwurf-2-institut` als Veröffentlichungsquelle eintragen.

Zum Ansehen genügt lokal:

```
python3 -m http.server -d frontend/entwurf-2-institut 8000
```

## Seiten

- `index.html`
- `wer-wir-sind.html`
- `namensgeber.html`
- `aktivitaeten.html`
- `projekt-epithetik.html`
- `projekt-forum.html`
- `spenden.html`
- `mitglied-werden.html`
- `kontakt.html`
- `satzung.html`
- `impressum.html`
- `datenschutz.html`

Dazu `404.html`, `robots.txt`, `sitemap.xml` und `.nojekyll`.

## Kontaktformular

Der Endpunkt wird in `assets/js/konfiguration.js` eingetragen. Einrichtung des
Backends (Google Apps Script schreibt nach Supabase): siehe `backend/README.md`
im Projektordner. Ohne Endpunkt bleibt die Seite benutzbar – das Formular bietet
dann den Versand über das E-Mail-Programm an.

## Ändern

Die Seiten werden aus `werkzeuge/` erzeugt, damit alle Entwürfe dieselben
Texte tragen:

```
python3 werkzeuge/bauen.py
```

Texte stehen in `werkzeuge/inhalte.py` (Quelle: `inhalte/redaktionsplan.md`),
die Gestaltung dieses Entwurfs in `werkzeuge/entwurf2.py`.
Wer lieber direkt im HTML arbeitet, kann das tun – dann sollte der Bauläufer
allerdings nicht mehr über die Dateien laufen.
