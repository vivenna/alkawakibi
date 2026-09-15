# Redaktionsplan – Website Alkawakibi e. V.

Verbindliche Textgrundlage für **alle drei Design-Varianten**. Der Inhalt ist in
allen Varianten identisch; unterschiedlich sind ausschließlich Gestaltung,
Seitenaufbau und Bildeinsatz.

Quellen: Konzeptdokument des Vorstands, WordPress-Export der alten Website
(24.01.2021), Satzung vom 29.05.2015.

> **Regel:** Nichts erfinden. Zahlen, Namen, Daten und Bankverbindungen stehen
> unten wörtlich. Was nicht hier steht, kommt nicht auf die Seite.
> Offene Punkte sind mit `[KLÄREN]` markiert und dürfen **nicht** als Text
> erscheinen.

---

## 0. Grunddaten

| Feld | Wert |
|---|---|
| Vollständiger Name | Alkawakibi Verein e. V. |
| Kurzform | Alkawakibi e. V. |
| Claim (aus dem Logo) | Für Demokratie und Menschenrechte |
| Arabisch | الكواكبي |
| Sitz | Triftstr. 8, 13353 Berlin |
| E-Mail | info@alkawakibi.org |
| Registergericht | Amtsgericht Charlottenburg |
| Registernummer | VR 31792 B |
| Steuernummer | 27/660/63668 |
| Gemeinnützigkeit | anerkannt für kulturelle Zwecke, Bildung und Entwicklungshilfe |
| Telefon | `[KLÄREN]` – die alte Nummer gehört dem früheren Vorsitzenden und wird **nicht** übernommen |
| Gründungsjahr | `[KLÄREN]` – Satzung datiert 29.05.2015, Fotos belegen Aktivitäten ab 2014. Auf der Seite deshalb nur „seit über zehn Jahren", keine Jahreszahl |

### Bankverbindungen (geprüft, IBAN-Prüfziffern korrekt)

**Verein allgemein**
Alkawakibi Verein e. V.
IBAN: DE25 3006 0601 0008 5002 06
BIC: DAAEDEDDXXX
Deutsche Apotheker- und Ärztebank, Berlin

**Epithetik-Projekt (zweckgebunden)**
Alkawakibi Verein e. V. – Epithetik Projekt
IBAN: DE69 3006 0601 0108 5002 06
BIC: DAAEDEDDXXX
Deutsche Apotheker- und Ärztebank, Berlin

---

## 1. Seitenstruktur und Navigation

Vorgabe des Vorstands sind vier Hauptpunkte plus Kontaktformular. Das
Kontaktformular liegt als eigener Abschnitt auf der Kontaktseite und ist
zusätzlich direkt aus dem Menü erreichbar.

```
Wer sind wir            → wer-wir-sind.html
  Namensgeber           → namensgeber.html
  Satzung               → satzung.html
  Mitglied werden       → mitglied-werden.html
Unsere Aktivitäten      → aktivitaeten.html
  Epithetik-Projekt     → projekt-epithetik.html
  Forum für Ärzte …     → projekt-forum.html
Spenden                 → spenden.html
Kontakt                 → kontakt.html
  Kontaktformular       → kontakt.html#kontaktformular
```

Fußzeile zusätzlich: Impressum (`impressum.html`), Datenschutz (`datenschutz.html`).

**Dateinamen sind in allen drei Varianten identisch.** Startseite: `index.html`.

---

## 2. Startseite (`index.html`)

### Titel / Meta
- `<title>`: Alkawakibi e. V. – Für Demokratie und Menschenrechte
- Meta-Description: Alkawakibi e. V. ist ein deutsch-syrischer Verein in Berlin. Wir stärken Menschenrechte, demokratische Werte und den Aufbau einer lebendigen Zivilgesellschaft.

### Hero
- Dachzeile: `Deutsch-syrischer Verein in Berlin`
- Überschrift: `Demokratie wächst dort, wo Menschen einander zuhören.`
- Fließtext: `Alkawakibi e. V. stärkt Menschenrechte und demokratische Werte – durch Bildung, Begegnung und humanitäre Hilfe. In Berlin, in Deutschland und über Grenzen hinweg.`
- Erste Schaltfläche: `Unsere Aktivitäten` → `aktivitaeten.html`
- Zweite Schaltfläche: `Jetzt spenden` → `spenden.html`
- Hintergrundbild: `assets/bilder/aktivitaeten/veranstaltung-publikum-1600.jpg`

### Leitgedanke (wörtliches Zitat – Pflichttext, unverändert)
> Eine der zentralen Aufgaben des Verbands ist der Aufbau einer Zivilgesellschaft, die auf der Förderung von Menschenrechten und demokratischen Werten beruht, indem das Bewusstsein hierfür sowie demokratische Praktiken gestärkt werden.

Quellenangabe darunter: `Leitgedanke des Alkawakibi Verein e. V.`

### Kurzvorstellung „Wer wir sind"
Überschrift: `Wer wir sind`

Absatz 1: `Alkawakibi Verein e. V. (kurz Alkawakibi e. V.) ist ein deutsch-syrischer Verein mit Sitz in Berlin. Wir engagieren uns für die Stärkung von demokratischen Werten und fördern den Aufbau von zivilen Gesellschaftsstrukturen auf nationaler wie internationaler Ebene. Mit unseren Bildungs- und Beratungsangeboten richten wir uns insbesondere an Menschen arabischer Herkunft. Ihnen Möglichkeiten zur gewaltfreien Teilhabe am pluralistischen Leben aufzuzeigen, ist unser Anliegen.`

Absatz 2: `In unserem Tun orientieren wir uns an den allgemein gültigen Menschenrechten und setzen uns für Umwelt- und Verbraucherschutz ein.`

Verweis: `Mehr über uns` → `wer-wir-sind.html`

### Drei Arbeitsfelder (Kacheln)
1. **Demokratie & Menschenrechte** – `Wir fördern eine Kultur des Respekts vor den Menschenrechten und die Teilhabe am politischen Leben – pluralistisch, gewaltfrei und unabhängig von Herkunft, Geschlecht, Religion oder politischer Meinung.`
2. **Bildung & Begegnung** – `Seminare, Vorträge, Podiumsdiskussionen und Workshops schaffen Räume, in denen Menschen unterschiedlicher Herkunft miteinander statt übereinander sprechen.`
3. **Humanitäre Hilfe** – `Mit dem Epithetik-Projekt geben wir Kriegsverletzten ihr Gesicht zurück und bauen vor Ort medizinisches Wissen auf, das bleibt.`

### Auszeichnung
- Dachzeile: `Ausgezeichnet`
- Überschrift: `1. Preis beim Berliner Gesundheitspreis 2017`
- Text: `Das Deutsch-Syrische Forum für Ärzte, Zahnärzte und Apotheker wurde 2017 mit dem 1. Preis des Berliner Gesundheitspreises ausgezeichnet – für seinen Beitrag zur beruflichen Integration geflüchteter Medizinerinnen und Mediziner.`
- Bild: `assets/bilder/aktivitaeten/gesundheitspreis-2017-1600.jpg`
- Bildunterschrift: `Preisverleihung des Berliner Gesundheitspreises 2017.`
- Verweis: `Zum Forum` → `projekt-forum.html`

### Aktivitäten-Teaser (zwei bis drei Karten)
- **Epithetik-Projekt** – `Epithetische Versorgung von Kriegsverletzten in Idlib und Reyhanli – und Coaching für syrische Kolleginnen und Kollegen.` → `projekt-epithetik.html`, Bild `kinder-workshop-800.jpg` **nicht** verwenden; Bild: `assets/bilder/aktivitaeten/forum-aerzte-einladung-800.jpg` nur beim Forum.
  Für das Epithetik-Projekt kein Foto verwenden (es liegt keines vor) – stattdessen typografische Karte oder Symbol.
- **Forum für Ärzte, Zahnärzte und Apotheker** – `Eine Plattform für Medizinerinnen und Mediziner arabischer Herkunft: Approbation, Fachsprache, Mentoring.` → `projekt-forum.html`, Bild `assets/bilder/aktivitaeten/forum-aerzte-einladung-800.jpg`
- **Bildung & Begegnung** – `Seminare, Podiumsdiskussionen und Nachbarschaftsfeste in Berlin.` → `aktivitaeten.html`, Bild `assets/bilder/aktivitaeten/seminar-runde-800.jpg`

### Spendenaufruf (Abschluss)
- Überschrift: `Ihre Spende wirkt`
- Text: `Alkawakibi e. V. ist als gemeinnützig anerkannt und arbeitet ehrenamtlich. Jeder Beitrag fließt direkt in unsere Bildungs-, Begegnungs- und Hilfsprojekte.`
- Schaltfläche: `Jetzt spenden` → `spenden.html`
- Zweiter Verweis: `Mitglied werden` → `mitglied-werden.html`

---

## 3. Wer sind wir (`wer-wir-sind.html`)

- `<title>`: Wer sind wir – Alkawakibi e. V.
- Meta-Description: Leitgedanke, Ziele und Vorstand des deutsch-syrischen Vereins Alkawakibi e. V. in Berlin.
- Seitenüberschrift: `Wer sind wir`
- Einleitung: `Ein deutsch-syrischer Verein in Berlin, der sich seit über zehn Jahren für Menschenrechte, demokratische Bildung und eine starke Zivilgesellschaft einsetzt.`

### Abschnitt „Unser Leitgedanke"
Wörtliches Zitat wie auf der Startseite (siehe 2.), prominent gesetzt.

### Abschnitt „Wer wir sind"
Die beiden Absätze aus Abschnitt 2 („Alkawakibi Verein e. V. (kurz …)" und „In unserem Tun …").

### Abschnitt „Unsere Ziele" (aus § 2 der Satzung, sinnwahrend gekürzt)
1. `Demokratie stärken` – `Wir unterstützen die Entwicklung der Demokratie auf internationaler Ebene und in Deutschland, insbesondere unter Menschen arabischer Herkunft, den Aufbau ziviler Gesellschaftsstrukturen und die Teilnahme am politischen Leben auf Grundlage von pluralistischer Demokratie und Gewaltfreiheit.`
2. `Unabhängigkeit und gegenseitige Achtung` – `Wir wollen zu einer unabhängigen und demokratischen Gesellschaft beitragen, die Abhängigkeit und Absolutismus ablehnt, und fördern die gegenseitige Achtung von Menschen verschiedener Geschlechter, Herkunft, Kulturen, Religionen und politischer Meinungen.`
3. `Menschenrechte verteidigen` – `Wir fördern eine Kultur des Respekts für die Menschenrechte mit friedlichen und rechtmäßigen Mitteln – und das Verständnis für die Ursachen und Folgen von Ausbeutung und totalitären Regimen, um deren Wiederkehr zu verhindern.`
4. `Frauen beteiligen` – `Wir fördern die aktive Rolle der Frau und ihre wirksame Beteiligung am Aufbau der Zivilgesellschaft mit dem Ziel der Gleichberechtigung.`
5. `Jugend bilden` – `Wir fördern die demokratische Bildung der Jugend und unterstützen ihre Initiativen und innovativen Beiträge.`
6. `Umwelt und Verbraucher schützen` – `Wir fördern das Bewusstsein für den Umwelt- und Verbraucherschutz.`
7. `Humanitär helfen` – `Wir unterstützen humanitäre Hilfsorganisationen.`

### Abschnitt „So arbeiten wir" (aus § 2 Satzung, Umsetzung)
- `Bildungsangebote` – `Tagungen, Seminare, Kongresse, Vorträge und Exkursionen – lokal und international, offen für alle.`
- `Austausch und Podium` – `Wissenschaftliche und künstlerische Aktivitäten, regelmäßige Podiumsdiskussionen und Workshops für Migrantinnen und Migranten.`
- `Studien und Publikationen` – `Soziale und statistische Studien, Broschüren und informative Veröffentlichungen.`
- `Zusammenarbeit` – `Kooperation mit Vereinen und Institutionen, deren Ziele mit unseren vereinbar sind.`
- `Nothilfe` – `Humanitäre Nothilfe in Katastrophengebieten durch die Vorbereitung von Hilfsgruppen.`

Verweis am Ende: `Vollständige Satzung lesen` → `satzung.html`

### Abschnitt „Unser Vorstand"
Einleitung: `Der Vorstand führt den Verein ehrenamtlich. Er besteht satzungsgemäß aus fünf Mitgliedern.`

| Name | Funktion | Bild |
|---|---|---|
| Rami Kanoua | Vorstandsvorsitzender · Dipl.-Sozialpädagoge | `assets/bilder/vorstand/rami-kanoua.jpg` |
| Dr. Abdul-Hakeem Bazara | Stellvertretender Vorsitzender · Beauftragter für Organisation | `assets/bilder/vorstand/abdul-hakeem-bazara.jpg` |
| Mohamad Ali Treifi | Kassenwart · Beauftragter für Finanzen · Zahnarzt | `assets/bilder/vorstand/mohamad-ali-treifi.jpg` |
| Anan Jakisch | Beauftragter für externe Aktivitäten · Ingenieur | kein Foto – Platzhalter mit Initialen `AJ` |
| Sawsan Dakkalbab | Beauftragte für Medien und Öffentlichkeitsarbeit · Ingenieurin | kein Foto – Platzhalter mit Initialen `SD` |

Graustufen-Fassungen der Porträts liegen als `*-sw.jpg` daneben und dürfen
verwendet werden, wenn es zum Design passt.

Hinweis darunter: `Sie erreichen den Vorstand über` → Verweis `Kontakt` → `kontakt.html`

### Abschnitt „Woher der Name kommt" (Teaser)
Text: `Der Verein trägt den Namen von Abd ar-Rahman al-Kawakibi (1855–1902) – einem syrischen Publizisten, der schon vor über hundert Jahren über die Mechanik der Despotie schrieb und für Reformen in der arabischen Welt eintrat.`
Bild: `assets/bilder/namensgeber/al-kawakibi.jpg`
Verweis: `Mehr zum Namensgeber` → `namensgeber.html`

---

## 4. Namensgeber (`namensgeber.html`)

- `<title>`: Abd ar-Rahman al-Kawakibi – Namensgeber des Vereins
- Seitenüberschrift: `Abd ar-Rahman al-Kawakibi`
- Dachzeile: `Unser Namensgeber`
- Bild: `assets/bilder/namensgeber/al-kawakibi.jpg`, Bildunterschrift `Abd ar-Rahman al-Kawakibi (1855–1902)`

### Biografie (wörtlich von der alten Website übernommen)
`Abd ar-Rahmān al-Kawākibī (geb. 1855 in Aleppo; gest. 1902 in Kairo) war ein einflussreicher syrischer islamischer Theologe und Publizist.`

`Bekannt wurde er durch seine Bemühungen für demokratische Reformen innerhalb der arabisch-muslimischen Welt. Kawakibi propagierte eine arabische kulturelle Renaissance (Nahda). Der Intellektuelle war ein Vertreter der Strömung der Reformtradition (Islah) des Afghanen Dschamal ad-Din al-Afghani (1838–1897), des Ägypters Muhammad Abduh (1849–1905) und seines Landsmannes Raschid Rida (1865–1935). Als Herausgeber zweier Zeitungen kritisierte er die Behörden unter dem osmanischen Sultan Abdülhamid II. und befürwortete soziale und religiöse Reformen. Seine Zeitung asch-Schahbāʾ wurde nach der 16. Ausgabe verboten. 1879 brachte er eine weitere Wochenzeitung namens al-Iʿtidāl heraus. Diese wurde im Oktober desselben Jahres ebenfalls verboten. Al-Kawakibi wurde später festgenommen und war einige Monate inhaftiert.`

`Im Exil in Ägypten wurde er in Kairo mit den muslimischen reformistischen Führern al-Afghani, Abduh und Rida bekannt. Er nahm an Aktivitäten zur islamischen Reform teil und war publizistisch aktiv. Als Autor predigte er religiöse Reformen und befürwortete eine Wiederbelebung der arabischen Kultur. Für seine Ziele warb er in arabischen Ländern sowie in Ostafrika und Südasien. Zu al-Kawakibis bekanntesten Werken zählt seine berühmte Abhandlung über das Wesen der Diktatur aus dem Jahr 1899: „Die Eigenarten der Despotie und die Stätten der Versklavung".`

Externe Verweise (in neuem Tab, `rel="noopener"`):
- Dschamal ad-Din al-Afghani → `https://de.wikipedia.org/wiki/Dschamal_ad-Din_al-Afghani`
- Muhammad Abduh → `https://de.wikipedia.org/wiki/Muhammad_Abduh`
- Raschid Rida → `https://de.wikipedia.org/wiki/Raschid_Rida`

### Abschnitt „Was ist Despotie?"
Dachzeile: `Aus unseren Fachinformationen`
Text (Einleitung, gekürzt von der alten Website):
`Abd al-Rahman al-Kawakibi verbrachte den Großteil seines Lebens in Aleppo, wo er unter anderem für mehrere Zeitungen arbeitete und als Bürgermeister tätig war. Das heutige Syrien war damals noch Teil des Osmanischen Reiches. Aufgrund seiner liberalen Ansichten geriet er immer wieder mit den osmanischen Behörden aneinander, weshalb er sich letztlich nach Kairo zurückzog und sich dem Zirkel um Muhammad Abduh und Raschid Rida anschloss. Dort veröffentlichte er – anonym – eines seiner wichtigsten Werke: „Die Eigenschaften der Despotie".`

`Wie die meisten seiner Zeitgenossen beschäftigte auch er sich mit der Frage, warum die islamische Welt im Vergleich zu den europäischen Mächten ins Hintertreffen geraten war. Seine Antwort: nicht der Islam selbst, sondern die Despotie – die Herrschaft, die Wissen, Religion und Wirtschaft ihrem Machterhalt unterordnet – habe die Gesellschaft gelähmt.`

Schlusszeile: `Diese Frage – wie Gesellschaften frei werden und frei bleiben – ist bis heute der Kern unserer Arbeit.`

---

## 5. Unsere Aktivitäten (`aktivitaeten.html`)

- `<title>`: Unsere Aktivitäten – Alkawakibi e. V.
- Seitenüberschrift: `Unsere Aktivitäten`
- Einleitung: `Wir arbeiten dort, wo demokratische Praxis konkret wird: in Seminarräumen, auf Podien, in Nachbarschaften – und dort, wo Menschen nach Krieg und Flucht medizinische Hilfe brauchen.`

### Projekt 1 – Epithetik-Projekt (hervorgehoben)
- Titel: `Epithetik-Projekt`
- Untertitel: `Kriegsverletzten ihr Gesicht zurückgeben`
- Text: `Gemeinsam mit dem Deutsch-Syrischen Verein zur Förderung der Freiheiten und Menschenrechte e. V. versorgen wir Kriegsverletzte in Idlib (Syrien) und Reyhanli (Türkei) epithetisch – und bilden syrische Kolleginnen und Kollegen vor Ort aus.`
- Verweis: `Zum Projekt` → `projekt-epithetik.html`

### Projekt 2 – Forum für Ärzte, Zahnärzte und Apotheker
- Titel: `Forum für Ärzte, Zahnärzte und Apotheker`
- Untertitel: `Berufliche Integration im Gesundheitswesen`
- Text: `Das Deutsch-Syrische Forum bietet Medizinerinnen und Medizinern arabischer Herkunft eine Plattform zum Austausch über Approbation, Fachsprache und Berufserlaubnis – ergänzt um ein Mentorenprojekt. 2017 mit dem 1. Preis des Berliner Gesundheitspreises ausgezeichnet.`
- Bild: `assets/bilder/aktivitaeten/forum-aerzte-einladung-800.jpg`
- Verweis: `Zum Forum` → `projekt-forum.html`

### Arbeitsfeld 3 – Politische Bildung und Podium
- Titel: `Politische Bildung und Podiumsdiskussionen`
- Text: `Vorträge, Seminare und Podiumsdiskussionen zu Demokratie, Menschenrechten und der Zukunft Syriens – unter anderem im Berliner Abgeordnetenhaus, mit Referentinnen und Referenten aus Wissenschaft, Politik und Zivilgesellschaft.`
- Bilder: `podiumsdiskussion-800.jpg`, `vortrag-referent-800.jpg`, `diskussion-wortmeldung-800.jpg`

### Arbeitsfeld 4 – Seminare und Workshops
- Titel: `Seminare und Workshops`
- Text: `In kleinen Runden geht es um das, was Teilhabe im Alltag ausmacht: Rechte kennen, sich einbringen, Konflikte gewaltfrei austragen. Unsere Angebote richten sich besonders an Menschen arabischer Herkunft und an Neuzugewanderte.`
- Bilder: `seminar-runde-800.jpg`, `seminar-teilnehmende-800.jpg`, `gespraechsrunde-800.jpg`

### Arbeitsfeld 5 – Begegnung in der Nachbarschaft
- Titel: `Begegnung in der Nachbarschaft`
- Text: `Nachbarschafts- und Begegnungsfeste, Kulturabende und Angebote für Kinder: Orte, an denen aus Nebeneinander ein Miteinander wird.`
- Bilder: `begegnungsfest-stand-800.jpg`, `begegnungsfest-kinder-800.jpg`, `kinder-workshop-800.jpg`, `kulturabend-musik-800.jpg`, `austausch-treffen-800.jpg`

### Bildergalerie
Alle Bilder aus `assets/bilder/aktivitaeten/` dürfen als Galerie gezeigt werden
(Lightbox optional). Hinweis unter der Galerie:
`Impressionen aus der Vereinsarbeit der vergangenen Jahre.`

### Abschluss
Text: `Sie möchten bei einer Veranstaltung dabei sein oder ein Projekt unterstützen?`
Schaltflächen: `Kontakt aufnehmen` → `kontakt.html`, `Mitglied werden` → `mitglied-werden.html`

---

## 6. Epithetik-Projekt (`projekt-epithetik.html`)

- `<title>`: Epithetik-Projekt – Alkawakibi e. V.
- Dachzeile: `Projekt`
- Überschrift: `Epithetik-Projekt`
- Einleitung: `Geben Sie Menschen ihr Gesicht zurück.`

### Abschnitt „Worum es geht" (wörtlich von der alten Website)
`Aufgrund des lang anhaltenden Krieges in Syrien ist die Zahl der Patienten mit Gesichtsdefekten stark angestiegen. In Kooperation mit dem Deutsch-Syrischen Verein zur Förderung der Freiheiten und Menschenrechte e. V. setzt Alkawakibi e. V. ein einzigartiges Projekt in der türkisch-syrischen Grenzregion um. Das Ziel des internationalen Hilfsprojektes besteht in der epithetischen Versorgung von Kriegsverletzten in Idlib (Syrien) und Reyhanli (Türkei).`

`Unser Arbeitsteam hat sich ehrenamtlich für die epithetische Rekonstruktion von Gesichtsverletzungen zur Verfügung gestellt. Das Team hat das Ziel, die Patienten epithetisch zu versorgen und zugleich ein Coaching für syrische Kollegen anzubieten, sodass sich eine Infrastruktur zur Behandlung und Nachsorge von Epithetikpatienten aufbauen kann.`

### Abschnitt „Was ist Epithetik?" (wörtlich)
`Unter Epithetik versteht man den Ersatz von fehlenden Körperteilen, zum Beispiel nach einem Unfall, einer Tumorerkrankung oder bei angeborenen Fehlbildungen. Man nennt diese künstlichen Körperteile Epithesen. Sie sollen den Defekt möglichst naturgetreu abdecken und so dem Patienten ermöglichen, wieder unter Menschen zu gehen und sich sicher in der Gesellschaft zu bewegen.`

### Abschnitt „Spendenaufruf" (hervorgehoben)
Überschrift: `Geben Sie Menschen ihr Gesicht zurück!`
Text: `Aktuell warten über zehn kriegsversehrte syrische Patientinnen und Patienten im Flüchtlingslager Reyhanli an der türkisch-syrischen Grenze auf Augen-Implantate, darunter viele Kinder. Bitte helfen Sie uns, ihnen ihr Lachen zurückzugeben.`

Spendenkonto (zweckgebunden):
```
Alkawakibi Verein e. V. – Epithetik Projekt
IBAN: DE69 3006 0601 0108 5002 06
BIC:  DAAEDEDDXXX
Deutsche Apotheker- und Ärztebank, Berlin
Verwendungszweck: Epithetik
```
Schaltfläche: `Alle Spendenwege` → `spenden.html`

### Weiterführend
Verweis (neuer Tab): `Projektwebsite epithetik-projekt.de` → `http://www.epithetik-projekt.de/de_DE/`
Hinweis darunter: `Externe Website des Projektpartners.`

---

## 7. Forum für Ärzte, Zahnärzte und Apotheker (`projekt-forum.html`)

- `<title>`: Forum für Ärzte, Zahnärzte und Apotheker – Alkawakibi e. V.
- Dachzeile: `Projekt`
- Überschrift: `Forum für Ärzte, Zahnärzte und Apotheker`
- Einleitung: `Das Deutsch-Syrische Forum – ausgezeichnet mit dem 1. Preis des Berliner Gesundheitspreises 2017.`

### Abschnitt „Worum es geht" (wörtlich)
`Das Deutsch-Syrische Forum bietet Ärzten, Zahnärzten und Apothekern mit arabischer Herkunft eine Plattform zum Austausch. Das Ziel besteht darin, den geflohenen Kolleginnen und Kollegen die berufliche Integration zu erleichtern. Bei regelmäßigen Treffen werden Fragen rund um die Approbation, den (Fach-)Spracherwerb und die Berufserlaubnis erläutert sowie Fortbildungsmöglichkeiten aufgezeigt.`

`Darüber hinaus bietet das Forum ein Mentorenprojekt für Medizinerinnen und Mediziner mit Fluchterfahrung. Durch die Eins-zu-eins-Begleitung können Bedarfe individuell identifiziert und Maßnahmen ergriffen werden. Auf diese Weise trägt das Forum zur Integration von dringend benötigten Fachkräften aus dem Gesundheitssektor bei.`

### Abschnitt „Auszeichnung"
`2017 erhielt das Forum den 1. Preis des Berliner Gesundheitspreises.`
Bild: `assets/bilder/aktivitaeten/gesundheitspreis-2017-1600.jpg`
Bildunterschrift: `Preisverleihung des Berliner Gesundheitspreises 2017.`

### Abschnitt „Das Angebot im Überblick"
- `Regelmäßige Treffen` – `Austausch unter Kolleginnen und Kollegen, offen für Ärztinnen und Ärzte, Zahnärztinnen und Zahnärzte sowie Apothekerinnen und Apotheker.`
- `Wege zur Approbation` – `Informationen zu Anerkennung, Berufserlaubnis und den nötigen Prüfungen.`
- `Fachsprache` – `Hinweise zum medizinischen Spracherwerb und zur Fachsprachprüfung.`
- `Mentoring` – `Eins-zu-eins-Begleitung durch erfahrene Kolleginnen und Kollegen.`

Bild: `assets/bilder/aktivitaeten/forum-aerzte-einladung-800.jpg`, Bildunterschrift `Einladung zu einem Forumstreffen (deutsch/arabisch).`

### Weiterführend
Verweis (neuer Tab): `forum.alkawakibi.org` → `http://forum.alkawakibi.org/`
Hinweis: `Die Seite des Forums wird gesondert gepflegt.` `[KLÄREN]` – ob die Adresse noch erreichbar ist.

---

## 8. Spenden (`spenden.html`)

- `<title>`: Spenden – Alkawakibi e. V.
- Überschrift: `Spenden`
- Einleitung: `Wir arbeiten ehrenamtlich und finanzieren unsere Arbeit aus Mitgliedsbeiträgen und Spenden. Jeder Betrag kommt direkt in den Projekten an.`

### Abschnitt „Wohin Ihre Spende geht"
- `Bildung und Begegnung` – `Räume, Referentinnen und Referenten, Material für Seminare, Workshops und Nachbarschaftsfeste.`
- `Epithetik-Projekt` – `Material und Reisen für die epithetische Versorgung von Kriegsverletzten und das Coaching vor Ort.`
- `Forum für Medizinerinnen und Mediziner` – `Treffen, Informationsmaterial und das Mentorenprojekt.`

### Abschnitt „Spendenkonto"
**Für die allgemeine Vereinsarbeit**
```
Alkawakibi Verein e. V.
IBAN: DE25 3006 0601 0008 5002 06
BIC:  DAAEDEDDXXX
Deutsche Apotheker- und Ärztebank, Berlin
Verwendungszweck: Spende
```

**Zweckgebunden für das Epithetik-Projekt**
```
Alkawakibi Verein e. V. – Epithetik Projekt
IBAN: DE69 3006 0601 0108 5002 06
BIC:  DAAEDEDDXXX
Deutsche Apotheker- und Ärztebank, Berlin
Verwendungszweck: Epithetik
```

Beide IBAN erhalten eine Schaltfläche `IBAN kopieren` (JavaScript, mit
Rückmeldung „Kopiert"). Ohne JavaScript bleibt die IBAN als Text lesbar.

### Abschnitt „Spendenquittung"
`Alkawakibi Verein e. V. ist beim Finanzamt für Körperschaften als gemeinnützig anerkannt – für kulturelle Zwecke, Bildung und Entwicklungshilfe (Steuernummer 27/660/63668). Für Spenden stellen wir auf Wunsch eine Zuwendungsbestätigung aus. Bitte geben Sie dafür Ihre Anschrift im Verwendungszweck an oder schreiben Sie uns an info@alkawakibi.org.`

Hinweis: `Bis 300 Euro genügt gegenüber dem Finanzamt in der Regel der Kontoauszug als Nachweis.`

### Abschnitt „Andere Wege zu helfen"
- `Mitglied werden` – `Werden Sie Teil des Vereins und gestalten Sie mit.` → `mitglied-werden.html`
- `Freund des Vereins werden` – `Die Satzung kennt „Freunde des Vereins": Menschen, die keine Mitglieder sind, aber unsere Ziele teilen und uns mit ihren Fähigkeiten unterstützen.` → `kontakt.html`
- `Weitersagen` – `Erzählen Sie von unserer Arbeit – in Ihrem Verein, Ihrer Praxis, Ihrer Nachbarschaft.`

`[KLÄREN]` – PayPal oder ein Spendentool sind noch nicht beauftragt. Solange
keine Entscheidung vorliegt, zeigt die Seite ausschließlich die Bankverbindung.

---

## 9. Mitglied werden (`mitglied-werden.html`)

- `<title>`: Mitglied werden – Alkawakibi e. V.
- Überschrift: `Mitglied werden`
- Einleitung: `Sie möchten Mitglied werden? Wunderbar. Hier finden Sie den Aufnahmeantrag – auf Deutsch und auf Arabisch.`

### Abschnitt „So wird man Mitglied" (aus § 4 der Satzung)
1. `Antrag ausfüllen` – `Laden Sie den Aufnahmeantrag herunter und füllen Sie ihn aus.`
2. `Antrag einreichen` – `Senden Sie den unterschriebenen Antrag an den Vorstand – per Post an Triftstr. 8, 13353 Berlin, oder per E-Mail an info@alkawakibi.org.`
3. `Bestätigung` – `Der Vorstand entscheidet über die Aufnahme und bestätigt sie schriftlich.`
4. `Assoziierte Mitgliedschaft` – `Die Aufnahme erfolgt zunächst als assoziiertes Mitglied. Nach einem Jahr kann die Ernennung zum ordentlichen Mitglied erfolgen.`

### Abschnitt „Antrag herunterladen"
- `Aufnahmeantrag (Deutsch) – PDF` → `assets/dokumente/mitgliedsantrag-deutsch.pdf`
- `Aufnahmeantrag (Deutsch) – Word` → `assets/dokumente/mitgliedsantrag-deutsch.docx`
- `طلب انتساب (Arabisch) – PDF` → `assets/dokumente/mitgliedsantrag-arabisch.pdf`
- `طلب انتساب (Arabisch) – Word` → `assets/dokumente/mitgliedsantrag-arabisch.docx`

Die arabischen Beschriftungen tragen `lang="ar" dir="rtl"`.

### Abschnitt „Beitrag"
`Die Höhe des Jahresbeitrags legt die Generalversammlung fest; Näheres regelt die Beitragsordnung.` `[KLÄREN]` – konkrete Beitragshöhe, sobald sie vorliegt.

### Abschluss
`Bei Fragen stehen wir Ihnen gern zur Verfügung.` → Verweis `Kontakt` → `kontakt.html`

---

## 10. Kontakt (`kontakt.html`)

- `<title>`: Kontakt – Alkawakibi e. V.
- Überschrift: `Kontakt`
- Einleitung: `Sie haben eine Frage, möchten mitarbeiten oder ein Projekt unterstützen? Schreiben Sie uns.`

### Kontaktangaben
```
Alkawakibi Verein e. V.
Triftstr. 8
13353 Berlin
E-Mail: info@alkawakibi.org
```
E-Mail als `mailto:`-Verweis. Anschrift in `<address>`.
`[KLÄREN]` – Telefonnummer und mögliche Sprechzeiten.

### Abschnitt „Kontaktformular" (Anker `#kontaktformular`)
Überschrift: `Kontaktformular`
Einleitung: `Felder mit * sind Pflichtfelder.`

Felder:
| Feld | Name | Typ | Pflicht |
|---|---|---|---|
| Name | `name` | text | ja |
| E-Mail | `email` | email | ja |
| Telefon (optional) | `telefon` | tel | nein |
| Betreff | `betreff` | select | ja |
| Nachricht | `nachricht` | textarea | ja |
| Einwilligung | `einwilligung` | checkbox | ja |
| (Honigtopf, unsichtbar) | `website` | text | nein |

Auswahl für `betreff`: `Allgemeine Anfrage`, `Mitgliedschaft`, `Spenden`,
`Epithetik-Projekt`, `Forum für Ärzte, Zahnärzte und Apotheker`, `Presse`, `Sonstiges`

Beschriftung der Einwilligung: `Ich bin damit einverstanden, dass meine Angaben zur Bearbeitung meiner Anfrage gespeichert werden. Hinweise dazu in der Datenschutzerklärung.` (Wort „Datenschutzerklärung" verweist auf `datenschutz.html`.)

Absenden-Schaltfläche: `Nachricht senden`
Erfolgsmeldung: `Vielen Dank. Ihre Nachricht ist bei uns eingegangen – wir melden uns zeitnah.`
Fehlermeldung: `Das Senden hat leider nicht geklappt. Bitte schreiben Sie uns direkt an info@alkawakibi.org.`

Technik siehe `backend/README.md`. Endpunkt steht in `assets/js/konfiguration.js`.

### Abschnitt „Anfahrt"
`Der Vereinssitz liegt in Berlin-Wedding. Bitte vereinbaren Sie vor einem Besuch einen Termin.`
Keine Karte einbinden (keine Drittanbieter-Einbettung ohne Einwilligung).

---

## 11. Satzung (`satzung.html`)

- `<title>`: Satzung – Alkawakibi e. V.
- Überschrift: `Satzung`
- Vorbemerkung: `Satzung des Alkawakibi Verein e. V., beschlossen in Berlin am 29. Mai 2015.`
- Volltext der Satzung § 1 bis § 13 – die Datei `inhalte/satzung.md` enthält den vollständigen Wortlaut und ist **unverändert** zu übernehmen.
- Ein Inhaltsverzeichnis mit Sprungmarken zu den Paragrafen ist erwünscht.
- Downloadhinweis entfällt (es liegt keine PDF-Fassung vor).

---

## 12. Impressum (`impressum.html`)

- `<title>`: Impressum – Alkawakibi e. V.

```
Angaben gemäß § 5 DDG

Alkawakibi Verein e. V.
Triftstr. 8
13353 Berlin

Vertreten durch den Vorstand:
Rami Kanoua (Vorsitzender)

Kontakt
E-Mail: info@alkawakibi.org

Registereintrag
Eintragung im Vereinsregister
Registergericht: Amtsgericht Charlottenburg
Registernummer: VR 31792 B

Steuerliche Angaben
Anerkannt beim Finanzamt für Körperschaften als gemeinnützige Körperschaft zur
Förderung kultureller Zwecke, der Bildung und der Entwicklungshilfe.
Steuernummer: 27/660/63668

Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV
Rami Kanoua
Triftstr. 8
13353 Berlin

Bildnachweise
Fotos: Alkawakibi Verein e. V.
Porträt Abd ar-Rahman al-Kawakibi: historische Aufnahme, gemeinfrei.

Haftung für Inhalte
Als Diensteanbieter sind wir für eigene Inhalte auf diesen Seiten nach den
allgemeinen Gesetzen verantwortlich. Wir sind jedoch nicht verpflichtet,
übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach
Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.

Haftung für Links
Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir
keinen Einfluss haben. Für die Inhalte der verlinkten Seiten ist stets der
jeweilige Anbieter oder Betreiber verantwortlich. Zum Zeitpunkt der Verlinkung
waren keine Rechtsverstöße erkennbar.

Urheberrecht
Die durch die Betreiber erstellten Inhalte und Werke auf diesen Seiten
unterliegen dem deutschen Urheberrecht. Beiträge Dritter sind als solche
gekennzeichnet.
```

`[KLÄREN]` – Telefonnummer für das Impressum; presserechtlich Verantwortlicher
bestätigen (hier: der Vorsitzende).

---

## 13. Datenschutz (`datenschutz.html`)

- `<title>`: Datenschutzerklärung – Alkawakibi e. V.
- Hinweis am Anfang: `Entwurf – vor der Veröffentlichung rechtlich prüfen lassen.` (Dieser Hinweis wird vor dem Livegang entfernt.)

Abschnitte:
1. `Verantwortlicher` – Alkawakibi Verein e. V., Triftstr. 8, 13353 Berlin, info@alkawakibi.org
2. `Hosting` – `Diese Website wird über GitHub Pages (GitHub Inc.) bereitgestellt. Beim Aufruf werden technisch notwendige Zugriffsdaten wie IP-Adresse, Datum und Uhrzeit verarbeitet. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO.`
3. `Kontaktformular` – `Die im Formular angegebenen Daten (Name, E-Mail-Adresse, optional Telefonnummer, Betreff und Nachricht) übermitteln wir über einen Dienst von Google (Google Apps Script) an unsere Datenbank bei Supabase, wo sie zur Bearbeitung Ihrer Anfrage gespeichert werden. Rechtsgrundlage ist Art. 6 Abs. 1 lit. a und lit. b DSGVO. Wir löschen die Daten, sobald die Anfrage abschließend bearbeitet ist und keine gesetzlichen Aufbewahrungspflichten entgegenstehen.`
4. `Keine Cookies, keine Analyse` – `Diese Website setzt keine Cookies zu Analyse- oder Werbezwecken und bindet keine Dienste Dritter zur Reichweitenmessung ein. Schriften werden lokal ausgeliefert.`
5. `Ihre Rechte` – `Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch nach Art. 15 bis 21 DSGVO. Eine erteilte Einwilligung können Sie jederzeit widerrufen. Außerdem haben Sie das Recht, sich bei einer Aufsichtsbehörde zu beschweren – für Berlin: Berliner Beauftragte für Datenschutz und Informationsfreiheit.`
6. `Kontakt in Datenschutzfragen` – `info@alkawakibi.org`

---

## 14. Gemeinsame Elemente aller Seiten

### Kopfbereich
- Logo verweist auf `index.html`. Logodatei je nach Hintergrund:
  `assets/bilder/logo.png` (heller Grund) oder `assets/bilder/logo-weiss.png` /
  `logo-weiss-gold.png` (dunkler Grund). Alternativtext: `Alkawakibi e. V. – Für Demokratie und Menschenrechte`
- Hauptnavigation gemäß Abschnitt 1, feststehend beim Scrollen (sticky).
- Aktive Seite ist mit `aria-current="page"` gekennzeichnet.
- Deutlich sichtbare Schaltfläche `Spenden` in der Navigation.
- Mobil: Menü über eine Schaltfläche mit `aria-expanded`, Untermenüs aufklappbar,
  Bedienung per Tastatur möglich, `Esc` schließt.

### Fußbereich
Spalte 1: Logo, Claim `Für Demokratie und Menschenrechte`, Kurzsatz
`Deutsch-syrischer Verein für Menschenrechte, demokratische Bildung und Zivilgesellschaft. Sitz in Berlin.`
Spalte 2: `Verein` – Wer sind wir, Namensgeber, Satzung, Mitglied werden
Spalte 3: `Themen` – Unsere Aktivitäten, Epithetik-Projekt, Forum für Ärzte…, Spenden
Spalte 4: `Kontakt` – Anschrift, E-Mail, Verweis Kontaktformular
Fußzeile unten: `© 2026 Alkawakibi Verein e. V.` · Impressum · Datenschutz
Zusatz: `Gemeinnütziger Verein · VR 31792 B · Amtsgericht Charlottenburg`

### Pflicht in jeder Datei
- `<html lang="de">`
- `<meta charset="utf-8">`, Viewport-Angabe
- `<title>` und `<meta name="description">` wie oben je Seite
- Open-Graph-Angaben: `og:title`, `og:description`, `og:image`
  (`assets/bilder/aktivitaeten/veranstaltung-publikum-1600.jpg`), `og:type`, `og:locale` = `de_DE`
- Favicon-Verweise auf `assets/bilder/favicon-32.png` und `apple-touch-icon.png`
- Sprungmarke `Zum Inhalt springen` als erstes fokussierbares Element
- `<main id="inhalt">`
- Sichtbarer Fokusrahmen, Kontrast mindestens 4,5:1
- Bilder mit `alt`, `width`, `height` und `loading="lazy"` (außer dem Hero-Bild)

### Sprache und Ton
- Deutsch, Sie-Anrede, sachlich und warm, keine Werbesprache.
- Geschlechtergerecht durch Doppelnennung oder neutrale Formulierungen –
  **kein** Gendersternchen.
- Arabische Wörter mit `lang="ar" dir="rtl"` auszeichnen.

---

## 15. Offene Punkte (nicht auf der Website anzeigen)

1. Telefonnummer für Impressum und Kontaktseite.
2. Gründungsjahr des Vereins.
3. Porträtfotos von Anan Jakisch und Sawsan Dakkalbab.
4. Höhe des Mitgliedsbeitrags.
5. Ist `forum.alkawakibi.org` noch erreichbar?
6. Soll ein Zahlungsdienstleister (PayPal o. Ä.) ergänzt werden?
7. Bestätigung des presserechtlich Verantwortlichen.
8. Aktuelle Projekte 2026 – gibt es laufende Aktivitäten, die ergänzt werden sollen?
