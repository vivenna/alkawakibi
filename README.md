# Website Alkawakibi e. V.

Neue Website des **Alkawakibi Verein e. V.** – deutsch-syrischer Verein für
Demokratie und Menschenrechte, Berlin.

Reines HTML, CSS und JavaScript ohne Bauprozess, geeignet für GitHub Pages.

## Drei Entwürfe zur Auswahl

Der Vorstand hat zwei Vorbild-Websites genannt, deren Anforderungen sich nicht
widerspruchsfrei vereinen lassen (Logo in Schwarz/Dunkelgrün, gewünschtes
Farbschema in Türkis/Gelb). Statt eines Kompromisses liegen drei vollständig
ausgearbeitete Entwürfe vor – inhaltlich identisch, gestalterisch grundverschieden.

| Branch | Entwurf | Idee |
|---|---|---|
| `entwurf-1-petrol-gold` | **Petrol & Gold** | Durchgehend dunkel, Petrol mit Goldakzent, Serifen-Überschriften. Direkte Umsetzung des Farbvorbilds. |
| `entwurf-2-institut` | **Institut** | Hell und redaktionell in den Logofarben Schwarz/Dunkelgrün, klare Themenbereiche, Seitenleisten. Strukturvorbild e-cfr.org. |
| `entwurf-3-manifest` | **Manifest** | Modernistisch-geometrisch, Sand und Tiefschwarz mit grünen Diagonalflächen, große Typografie. |

Auf `main` liegt eine Vergleichsseite, die alle drei nebeneinander zeigt.

## Aufbau

```
assets/        Bilder, Schriften, Dokumente – in allen Entwürfen identisch
inhalte/       Redaktionsplan und Satzung als Textgrundlage
backend/       Kontaktformular: Google Apps Script + Supabase
varianten/     nur auf main: Kopien der drei Entwürfe für die Vergleichsseite
```

## Veröffentlichen

**Einen Entwurf live stellen:** in den Repository-Einstellungen unter
*Pages → Build and deployment → Source: Deploy from a branch* den gewünschten
Branch und den Ordner `/ (root)` wählen.

**Alle drei zum Vergleich zeigen:** `main` veröffentlichen. Die Startseite ist
dann die Vergleichsseite, die Entwürfe liegen unter `varianten/entwurf-1/` usw.

**Kontaktformular:** siehe `backend/README.md`. Ohne eingetragenen Endpunkt
funktioniert die Seite weiter, das Formular bietet dann den Versand über das
E-Mail-Programm an.

## Vor dem Livegang

Die offenen Punkte stehen am Ende von `inhalte/redaktionsplan.md` –
unter anderem Telefonnummer fürs Impressum, Gründungsjahr, Fotos zweier
Vorstandsmitglieder und die Prüfung der Datenschutzerklärung.
