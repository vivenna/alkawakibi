# Website Alkawakibi e. V.

Neue Website des **Alkawakibi Verein e. V.** – deutsch-syrischer Verein für
Demokratie und Menschenrechte, Berlin.

Reines HTML, CSS und JavaScript, kein Framework, keine Abhängigkeiten.

## Vier Entwürfe zur Auswahl

Der Vorstand hat zwei Vorbild-Websites genannt, deren Anforderungen sich nicht
widerspruchsfrei vereinen lassen (Logo in Schwarz/Dunkelgrün, gewünschtes
Farbschema in Türkis/Gelb). Statt eines Kompromisses liegen vier vollständig
ausgearbeitete Entwürfe vor – **inhaltlich identisch, gestalterisch
grundverschieden**. Jeder ist eine komplette, eigenständige Website aus
zwölf Seiten plus Fehlerseite.

| Ordner | Entwurf | Idee |
|---|---|---|
| `frontend/entwurf-1-petrol-gold` | **Petrol & Gold** | Durchgehend dunkel, Petrol mit Goldakzent, Serifen-Überschriften. Direkte Umsetzung des Farbvorbilds. |
| `frontend/entwurf-2-institut` | **Institut** | Hell und redaktionell in den Logofarben Schwarz/Dunkelgrün, klare Themenbereiche, Seitenleisten. Strukturvorbild e-cfr.org. |
| `frontend/entwurf-3-manifest` | **Manifest** | Modernistisch-geometrisch, Sand und Tiefschwarz mit grünen Diagonalflächen, große Typografie. |
| `frontend/entwurf-4-smaragd` | **Smaragd** | Anlage wie Entwurf 1, aber ganz in den Logofarben: Grünverläufe von tief bis mint, weichere Formen. |

## Aufbau

```
assets/       Bilder, Schriften, Dokumente – in allen Entwürfen identisch
inhalte/      Redaktionsplan und Satzung als Textgrundlage
backend/      Kontaktformular: Google Apps Script + Supabase
werkzeuge/    Quelle der Entwürfe (siehe unten)
frontend/     die vier fertigen Websites
```

### Warum ein Generator?

Die Entwürfe tragen dieselben Texte. Stünden sie vierfach in 52 HTML-Dateien,
müsste jede Korrektur – eine Telefonnummer, ein Satzungsparagraf, ein
Navigationspunkt – bis zu 52-mal nachgezogen werden. Deshalb liegen Inhalt und
Gestaltung getrennt in `werkzeuge/`, und die HTML-Dateien werden daraus erzeugt:

```
werkzeuge/inhalte.py         alle Texte, Adressen, Kontodaten – einmal
werkzeuge/basis.py           welche Seite welche Inhalte zeigt
werkzeuge/entwurf_basis.py   gemeinsame Bausteine aller Entwürfe
werkzeuge/css_basis.py       gemeinsames CSS-Fundament
werkzeuge/skripte.py         gemeinsames JavaScript
werkzeuge/entwurf1.py        Gestaltung Petrol & Gold
werkzeuge/entwurf2.py        Gestaltung Institut
werkzeuge/entwurf3.py        Gestaltung Manifest
werkzeuge/entwurf4.py        Gestaltung Smaragd
werkzeuge/bauen.py           erzeugt frontend/
```

**Wichtig:** `frontend/` wird erzeugt. Änderungen dort gehen beim nächsten Bauen
verloren – geändert wird in `werkzeuge/`.

## Bauen

```
python3 werkzeuge/bauen.py        alle vier Entwürfe
python3 werkzeuge/bauen.py 2      nur Entwurf 2
```

Kein Python-Paket nötig, nur die Standardbibliothek.

## Ansehen

```
python3 -m http.server -d frontend/entwurf-1-petrol-gold 8000
```

Dann http://localhost:8000 öffnen.

## Veröffentlichen

Ist ein Entwurf ausgewählt, wird sein Ordner über GitHub Pages veröffentlicht
(*Einstellungen → Pages*). Solange die Auswahl offen ist, liegen alle vier
nebeneinander im Repository.

**Kontaktformular:** siehe `backend/README.md`. Ohne eingetragenen Endpunkt
funktioniert die Seite weiter, das Formular bietet dann den Versand über das
E-Mail-Programm an.

## Vor dem Livegang

Die offenen Punkte stehen am Ende von `inhalte/redaktionsplan.md` –
unter anderem Telefonnummer fürs Impressum, Gründungsjahr, Fotos zweier
Vorstandsmitglieder und die Prüfung der Datenschutzerklärung.
