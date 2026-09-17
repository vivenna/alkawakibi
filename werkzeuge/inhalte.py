# -*- coding: utf-8 -*-
"""Sämtliche Inhalte der Website als Datenstruktur.

Alle Entwürfe greifen auf dieses Modul zu. Dadurch sind ihre Texte
garantiert identisch und unterscheiden sich nur in der Gestaltung.

Wortlaut stammt aus inhalte/redaktionsplan.md. Nichts hier frei erfinden.
"""

# ---------------------------------------------------------------- Grunddaten

VEREIN = {
    'name':        'Alkawakibi Verein e. V.',
    'kurz':        'Alkawakibi e. V.',
    'claim':       'Für Demokratie und Menschenrechte',
    'arabisch':    'الكواكبي',
    'strasse':     'Triftstr. 8',
    'ort':         '13353 Berlin',
    'email':       'info@alkawakibi.org',
    'registergericht': 'Amtsgericht Charlottenburg',
    'registernummer':  'VR 31792 B',
    'steuernummer':    '27/660/63668',
    'vorsitzender':    'Rami Kanoua',
    'jahr':        '2026',
}

KONTO_VEREIN = {
    'titel': 'Für die allgemeine Vereinsarbeit',
    'inhaber': 'Alkawakibi Verein e. V.',
    'iban': 'DE25 3006 0601 0008 5002 06',
    'bic': 'DAAEDEDDXXX',
    'bank': 'Deutsche Apotheker- und Ärztebank, Berlin',
    'zweck': 'Spende',
}

KONTO_EPITHETIK = {
    'titel': 'Zweckgebunden für das Epithetik-Projekt',
    'inhaber': 'Alkawakibi Verein e. V. – Epithetik Projekt',
    'iban': 'DE69 3006 0601 0108 5002 06',
    'bic': 'DAAEDEDDXXX',
    'bank': 'Deutsche Apotheker- und Ärztebank, Berlin',
    'zweck': 'Epithetik',
}

LEITGEDANKE = (
    'Eine der zentralen Aufgaben des Verbands ist der Aufbau einer '
    'Zivilgesellschaft, die auf der Förderung von Menschenrechten und '
    'demokratischen Werten beruht, indem das Bewusstsein hierfür sowie '
    'demokratische Praktiken gestärkt werden.'
)
LEITGEDANKE_QUELLE = 'Leitgedanke des Alkawakibi Verein e. V.'

WER_WIR_SIND = [
    'Alkawakibi Verein e. V. (kurz Alkawakibi e. V.) ist ein deutsch-syrischer '
    'Verein mit Sitz in Berlin. Wir engagieren uns für die Stärkung von '
    'demokratischen Werten und fördern den Aufbau von zivilen '
    'Gesellschaftsstrukturen auf nationaler wie internationaler Ebene. Mit '
    'unseren Bildungs- und Beratungsangeboten richten wir uns insbesondere an '
    'Menschen arabischer Herkunft. Ihnen Möglichkeiten zur gewaltfreien Teilhabe '
    'am pluralistischen Leben aufzuzeigen, ist unser Anliegen.',
    'In unserem Tun orientieren wir uns an den allgemein gültigen Menschenrechten '
    'und setzen uns für Umwelt- und Verbraucherschutz ein.',
]

# ---------------------------------------------------------------- Navigation

NAVIGATION = [
    {'titel': 'Wer sind wir', 'ziel': 'wer-wir-sind.html', 'unter': [
        {'titel': 'Namensgeber',     'ziel': 'namensgeber.html'},
        {'titel': 'Satzung',         'ziel': 'satzung.html'},
        {'titel': 'Mitglied werden', 'ziel': 'mitglied-werden.html'},
    ]},
    {'titel': 'Unsere Aktivitäten', 'ziel': 'aktivitaeten.html', 'unter': [
        {'titel': 'Epithetik-Projekt', 'ziel': 'projekt-epithetik.html'},
        {'titel': 'Forum für Ärzte, Zahnärzte und Apotheker', 'ziel': 'projekt-forum.html'},
    ]},
    {'titel': 'Spenden', 'ziel': 'spenden.html', 'unter': []},
    {'titel': 'Kontakt', 'ziel': 'kontakt.html', 'unter': [
        {'titel': 'Kontaktformular', 'ziel': 'kontakt.html#kontaktformular'},
    ]},
]

FUSS_SPALTEN = [
    ('Verein', [
        ('Wer sind wir', 'wer-wir-sind.html'),
        ('Namensgeber', 'namensgeber.html'),
        ('Satzung', 'satzung.html'),
        ('Mitglied werden', 'mitglied-werden.html'),
    ]),
    ('Themen', [
        ('Unsere Aktivitäten', 'aktivitaeten.html'),
        ('Epithetik-Projekt', 'projekt-epithetik.html'),
        ('Forum für Ärzte, Zahnärzte und Apotheker', 'projekt-forum.html'),
        ('Spenden', 'spenden.html'),
    ]),
]

# ---------------------------------------------------------------- Ziele

ZIELE = [
    ('Demokratie stärken',
     'Wir unterstützen die Entwicklung der Demokratie auf internationaler Ebene '
     'und in Deutschland, insbesondere unter Menschen arabischer Herkunft, den '
     'Aufbau ziviler Gesellschaftsstrukturen und die Teilnahme am politischen '
     'Leben auf Grundlage von pluralistischer Demokratie und Gewaltfreiheit.'),
    ('Unabhängigkeit und gegenseitige Achtung',
     'Wir wollen zu einer unabhängigen und demokratischen Gesellschaft beitragen, '
     'die Abhängigkeit und Absolutismus ablehnt, und fördern die gegenseitige '
     'Achtung von Menschen verschiedener Geschlechter, Herkunft, Kulturen, '
     'Religionen und politischer Meinungen.'),
    ('Menschenrechte verteidigen',
     'Wir fördern eine Kultur des Respekts für die Menschenrechte mit friedlichen '
     'und rechtmäßigen Mitteln – und das Verständnis für die Ursachen und Folgen '
     'von Ausbeutung und totalitären Regimen, um deren Wiederkehr zu verhindern.'),
    ('Frauen beteiligen',
     'Wir fördern die aktive Rolle der Frau und ihre wirksame Beteiligung am '
     'Aufbau der Zivilgesellschaft mit dem Ziel der Gleichberechtigung.'),
    ('Jugend bilden',
     'Wir fördern die demokratische Bildung der Jugend und unterstützen ihre '
     'Initiativen und innovativen Beiträge.'),
    ('Umwelt und Verbraucher schützen',
     'Wir fördern das Bewusstsein für den Umwelt- und Verbraucherschutz.'),
    ('Humanitär helfen',
     'Wir unterstützen humanitäre Hilfsorganisationen.'),
]

ARBEITSWEISE = [
    ('Bildungsangebote',
     'Tagungen, Seminare, Kongresse, Vorträge und Exkursionen – lokal und '
     'international, offen für alle.'),
    ('Austausch und Podium',
     'Wissenschaftliche und künstlerische Aktivitäten, regelmäßige '
     'Podiumsdiskussionen und Workshops für Migrantinnen und Migranten.'),
    ('Studien und Publikationen',
     'Soziale und statistische Studien, Broschüren und informative '
     'Veröffentlichungen.'),
    ('Zusammenarbeit',
     'Kooperation mit Vereinen und Institutionen, deren Ziele mit unseren '
     'vereinbar sind.'),
    ('Nothilfe',
     'Humanitäre Nothilfe in Katastrophengebieten durch die Vorbereitung von '
     'Hilfsgruppen.'),
]

ARBEITSFELDER = [
    ('Demokratie & Menschenrechte',
     'Wir fördern eine Kultur des Respekts vor den Menschenrechten und die '
     'Teilhabe am politischen Leben – pluralistisch, gewaltfrei und unabhängig '
     'von Herkunft, Geschlecht, Religion oder politischer Meinung.'),
    ('Bildung & Begegnung',
     'Seminare, Vorträge, Podiumsdiskussionen und Workshops schaffen Räume, in '
     'denen Menschen unterschiedlicher Herkunft miteinander statt übereinander '
     'sprechen.'),
    ('Humanitäre Hilfe',
     'Mit dem Epithetik-Projekt geben wir Kriegsverletzten ihr Gesicht zurück '
     'und bauen vor Ort medizinisches Wissen auf, das bleibt.'),
]

# ---------------------------------------------------------------- Vorstand

VORSTAND = [
    {'name': 'Rami Kanoua', 'rolle': 'Vorstandsvorsitzender',
     'zusatz': 'Dipl.-Sozialpädagoge', 'initialen': 'RK',
     'bild': 'assets/bilder/vorstand/rami-kanoua.jpg'},
    {'name': 'Dr. Abdul-Hakeem Bazara', 'rolle': 'Stellvertretender Vorsitzender',
     'zusatz': 'Beauftragter für Organisation', 'initialen': 'AB',
     'bild': 'assets/bilder/vorstand/abdul-hakeem-bazara.jpg'},
    {'name': 'Mohamad Ali Treifi', 'rolle': 'Kassenwart',
     'zusatz': 'Beauftragter für Finanzen · Zahnarzt', 'initialen': 'MT',
     'bild': 'assets/bilder/vorstand/mohamad-ali-treifi.jpg'},
    {'name': 'Anan Jakisch', 'rolle': 'Beauftragter für externe Aktivitäten',
     'zusatz': 'Ingenieur', 'initialen': 'AJ', 'bild': None},
    {'name': 'Sawsan Dakkalbab', 'rolle': 'Beauftragte für Medien und Öffentlichkeitsarbeit',
     'zusatz': 'Ingenieurin', 'initialen': 'SD', 'bild': None},
]

# ---------------------------------------------------------------- Namensgeber

NAMENSGEBER_BIO = [
    'Abd ar-Rahmān al-Kawākibī (geb. 1855 in Aleppo; gest. 1902 in Kairo) war '
    'ein einflussreicher syrischer islamischer Theologe und Publizist.',
    'Bekannt wurde er durch seine Bemühungen für demokratische Reformen '
    'innerhalb der arabisch-muslimischen Welt. Kawakibi propagierte eine '
    'arabische kulturelle Renaissance (Nahda). Der Intellektuelle war ein '
    'Vertreter der Strömung der Reformtradition (Islah) des Afghanen '
    '{afghani}, des Ägypters {abduh} und seines Landsmannes {rida}. Als '
    'Herausgeber zweier Zeitungen kritisierte er die Behörden unter dem '
    'osmanischen Sultan Abdülhamid II. und befürwortete soziale und religiöse '
    'Reformen. Seine Zeitung asch-Schahbāʾ wurde nach der 16. Ausgabe verboten. '
    '1879 brachte er eine weitere Wochenzeitung namens al-Iʿtidāl heraus. Diese '
    'wurde im Oktober desselben Jahres ebenfalls verboten. Al-Kawakibi wurde '
    'später festgenommen und war einige Monate inhaftiert.',
    'Im Exil in Ägypten wurde er in Kairo mit den muslimischen reformistischen '
    'Führern al-Afghani, Abduh und Rida bekannt. Er nahm an Aktivitäten zur '
    'islamischen Reform teil und war publizistisch aktiv. Als Autor predigte er '
    'religiöse Reformen und befürwortete eine Wiederbelebung der arabischen '
    'Kultur. Für seine Ziele warb er in arabischen Ländern sowie in Ostafrika '
    'und Südasien. Zu al-Kawakibis bekanntesten Werken zählt seine berühmte '
    'Abhandlung über das Wesen der Diktatur aus dem Jahr 1899: „Die Eigenarten '
    'der Despotie und die Stätten der Versklavung“.',
]

NAMENSGEBER_LINKS = {
    'afghani': ('Dschamal ad-Din al-Afghani',
                'https://de.wikipedia.org/wiki/Dschamal_ad-Din_al-Afghani'),
    'abduh':   ('Muhammad Abduh',
                'https://de.wikipedia.org/wiki/Muhammad_Abduh'),
    'rida':    ('Raschid Rida',
                'https://de.wikipedia.org/wiki/Raschid_Rida'),
}

DESPOTIE = [
    'Abd al-Rahman al-Kawakibi verbrachte den Großteil seines Lebens in Aleppo, '
    'wo er unter anderem für mehrere Zeitungen arbeitete und als Bürgermeister '
    'tätig war. Das heutige Syrien war damals noch Teil des Osmanischen Reiches. '
    'Aufgrund seiner liberalen Ansichten geriet er immer wieder mit den '
    'osmanischen Behörden aneinander, weshalb er sich letztlich nach Kairo '
    'zurückzog und sich dem Zirkel um Muhammad Abduh und Raschid Rida anschloss. '
    'Dort veröffentlichte er – anonym – eines seiner wichtigsten Werke: „Die '
    'Eigenschaften der Despotie“.',
    'Wie die meisten seiner Zeitgenossen beschäftigte auch er sich mit der Frage, '
    'warum die islamische Welt im Vergleich zu den europäischen Mächten ins '
    'Hintertreffen geraten war. Seine Antwort: nicht der Islam selbst, sondern '
    'die Despotie – die Herrschaft, die Wissen, Religion und Wirtschaft ihrem '
    'Machterhalt unterordnet – habe die Gesellschaft gelähmt.',
]
DESPOTIE_SCHLUSS = ('Diese Frage – wie Gesellschaften frei werden und frei '
                    'bleiben – ist bis heute der Kern unserer Arbeit.')

# ---------------------------------------------------------------- Aktivitäten

BILD = 'assets/bilder/aktivitaeten/'

AKTIVITAETEN_EINLEITUNG = (
    'Wir arbeiten dort, wo demokratische Praxis konkret wird: in Seminarräumen, '
    'auf Podien, in Nachbarschaften – und dort, wo Menschen nach Krieg und '
    'Flucht medizinische Hilfe brauchen.'
)

PROJEKTE = [
    {'titel': 'Epithetik-Projekt',
     'untertitel': 'Kriegsverletzten ihr Gesicht zurückgeben',
     'text': 'Gemeinsam mit dem Deutsch-Syrischen Verein zur Förderung der '
             'Freiheiten und Menschenrechte e. V. versorgen wir Kriegsverletzte '
             'in Idlib (Syrien) und Reyhanli (Türkei) epithetisch – und bilden '
             'syrische Kolleginnen und Kollegen vor Ort aus.',
     'ziel': 'projekt-epithetik.html', 'linktext': 'Zum Projekt', 'bild': None},
    {'titel': 'Forum für Ärzte, Zahnärzte und Apotheker',
     'untertitel': 'Berufliche Integration im Gesundheitswesen',
     'text': 'Das Deutsch-Syrische Forum bietet Medizinerinnen und Medizinern '
             'arabischer Herkunft eine Plattform zum Austausch über Approbation, '
             'Fachsprache und Berufserlaubnis – ergänzt um ein Mentorenprojekt. '
             '2017 mit dem 1. Preis des Berliner Gesundheitspreises ausgezeichnet.',
     'ziel': 'projekt-forum.html', 'linktext': 'Zum Forum',
     'bild': BILD + 'forum-aerzte-einladung-800.jpg',
     'alt': 'Einladung zu einem Treffen des Deutsch-Syrischen Forums, deutsch und arabisch'},
]

ARBEITSFELDER_SEITE = [
    {'titel': 'Politische Bildung und Podiumsdiskussionen',
     'text': 'Vorträge, Seminare und Podiumsdiskussionen zu Demokratie, '
             'Menschenrechten und der Zukunft Syriens – unter anderem im Berliner '
             'Abgeordnetenhaus, mit Referentinnen und Referenten aus Wissenschaft, '
             'Politik und Zivilgesellschaft.',
     'bilder': [(BILD + 'podiumsdiskussion-800.jpg', 'Podiumsdiskussion mit mehreren Rednern vor Publikum'),
                (BILD + 'vortrag-referent-800.jpg', 'Referent spricht ins Mikrofon bei einer Vereinsveranstaltung'),
                (BILD + 'diskussion-wortmeldung-800.jpg', 'Wortmeldung aus dem Publikum während einer Diskussion')]},
    {'titel': 'Seminare und Workshops',
     'text': 'In kleinen Runden geht es um das, was Teilhabe im Alltag ausmacht: '
             'Rechte kennen, sich einbringen, Konflikte gewaltfrei austragen. '
             'Unsere Angebote richten sich besonders an Menschen arabischer '
             'Herkunft und an Neuzugewanderte.',
     'bilder': [(BILD + 'seminar-runde-800.jpg', 'Teilnehmende sitzen im Stuhlkreis bei einem Seminar'),
                (BILD + 'seminar-teilnehmende-800.jpg', 'Seminarteilnehmende an einer langen Tischreihe'),
                (BILD + 'gespraechsrunde-800.jpg', 'Kleine Gesprächsrunde an einem Tisch')]},
    {'titel': 'Begegnung in der Nachbarschaft',
     'text': 'Nachbarschafts- und Begegnungsfeste, Kulturabende und Angebote für '
             'Kinder: Orte, an denen aus Nebeneinander ein Miteinander wird.',
     'bilder': [(BILD + 'begegnungsfest-stand-800.jpg', 'Informationsstand des Vereins bei einem Begegnungsfest'),
                (BILD + 'begegnungsfest-kinder-800.jpg', 'Kinder basteln am Stand des Vereins'),
                (BILD + 'kinder-workshop-800.jpg', 'Kind modelliert bei einem Workshop mit Knete'),
                (BILD + 'kulturabend-musik-800.jpg', 'Musiker spielt Oud bei einem Kulturabend'),
                (BILD + 'austausch-treffen-800.jpg', 'Menschen im Gespräch bei einem Treffen des Vereins')]},
]

GALERIE = [
    (BILD + 'veranstaltung-publikum', 'Volles Publikum bei einer Veranstaltung des Vereins'),
    (BILD + 'vortrag-referent', 'Referent spricht ins Mikrofon'),
    (BILD + 'podiumsdiskussion', 'Podiumsdiskussion mit Flaggen im Hintergrund'),
    (BILD + 'diskussion-wortmeldung', 'Wortmeldung aus dem Publikum'),
    (BILD + 'seminar-runde', 'Seminar im Stuhlkreis'),
    (BILD + 'seminar-teilnehmende', 'Teilnehmende eines Seminars'),
    (BILD + 'gespraechsrunde', 'Gesprächsrunde an einem Tisch'),
    (BILD + 'begegnungsfest-stand', 'Stand des Vereins bei einem Begegnungsfest'),
    (BILD + 'begegnungsfest-kinder', 'Kinder am Stand des Vereins'),
    (BILD + 'kinder-workshop', 'Kind bei einem Bastelworkshop'),
    (BILD + 'kulturabend-musik', 'Musiker mit Oud bei einem Kulturabend'),
    (BILD + 'austausch-treffen', 'Menschen im Gespräch bei einem Treffen'),
    (BILD + 'begegnung-gespraech', 'Gespräch am Rande einer Veranstaltung'),
    (BILD + 'gesundheitspreis-2017', 'Preisverleihung des Berliner Gesundheitspreises 2017'),
]
GALERIE_HINWEIS = 'Impressionen aus der Vereinsarbeit der vergangenen Jahre.'

AUSZEICHNUNG = {
    'kicker': 'Ausgezeichnet',
    'titel': '1. Preis beim Berliner Gesundheitspreis 2017',
    'text': 'Das Deutsch-Syrische Forum für Ärzte, Zahnärzte und Apotheker wurde '
            '2017 mit dem 1. Preis des Berliner Gesundheitspreises ausgezeichnet – '
            'für seinen Beitrag zur beruflichen Integration geflüchteter '
            'Medizinerinnen und Mediziner.',
    'bild': BILD + 'gesundheitspreis-2017-1600.jpg',
    'bild_klein': BILD + 'gesundheitspreis-2017-800.jpg',
    'breite': 1600, 'hoehe': 1200,
    'alt': 'Gruppenfoto der Preisträgerinnen und Preisträger des Berliner Gesundheitspreises 2017',
    'bildunterschrift': 'Preisverleihung des Berliner Gesundheitspreises 2017.',
    'ziel': 'projekt-forum.html', 'linktext': 'Zum Forum',
}

# ---------------------------------------------------------------- Projektseiten

EPITHETIK = {
    'kicker': 'Projekt',
    'titel': 'Epithetik-Projekt',
    'einleitung': 'Geben Sie Menschen ihr Gesicht zurück.',
    'worum': [
        'Aufgrund des lang anhaltenden Krieges in Syrien ist die Zahl der '
        'Patienten mit Gesichtsdefekten stark angestiegen. In Kooperation mit dem '
        'Deutsch-Syrischen Verein zur Förderung der Freiheiten und Menschenrechte '
        'e. V. setzt Alkawakibi e. V. ein einzigartiges Projekt in der '
        'türkisch-syrischen Grenzregion um. Das Ziel des internationalen '
        'Hilfsprojektes besteht in der epithetischen Versorgung von '
        'Kriegsverletzten in Idlib (Syrien) und Reyhanli (Türkei).',
        'Unser Arbeitsteam hat sich ehrenamtlich für die epithetische '
        'Rekonstruktion von Gesichtsverletzungen zur Verfügung gestellt. Das Team '
        'hat das Ziel, die Patienten epithetisch zu versorgen und zugleich ein '
        'Coaching für syrische Kollegen anzubieten, sodass sich eine '
        'Infrastruktur zur Behandlung und Nachsorge von Epithetikpatienten '
        'aufbauen kann.',
    ],
    'was_ist': [
        'Unter Epithetik versteht man den Ersatz von fehlenden Körperteilen, zum '
        'Beispiel nach einem Unfall, einer Tumorerkrankung oder bei angeborenen '
        'Fehlbildungen. Man nennt diese künstlichen Körperteile Epithesen. Sie '
        'sollen den Defekt möglichst naturgetreu abdecken und so dem Patienten '
        'ermöglichen, wieder unter Menschen zu gehen und sich sicher in der '
        'Gesellschaft zu bewegen.',
    ],
    'aufruf_titel': 'Geben Sie Menschen ihr Gesicht zurück!',
    'aufruf_text': 'Aktuell warten über zehn kriegsversehrte syrische Patientinnen '
                   'und Patienten im Flüchtlingslager Reyhanli an der '
                   'türkisch-syrischen Grenze auf Augen-Implantate, darunter viele '
                   'Kinder. Bitte helfen Sie uns, ihnen ihr Lachen zurückzugeben.',
    'extern': ('Projektwebsite epithetik-projekt.de', 'http://www.epithetik-projekt.de/de_DE/'),
    'extern_hinweis': 'Externe Website des Projektpartners.',
}

FORUM = {
    'kicker': 'Projekt',
    'titel': 'Forum für Ärzte, Zahnärzte und Apotheker',
    'einleitung': 'Das Deutsch-Syrische Forum – ausgezeichnet mit dem 1. Preis '
                  'des Berliner Gesundheitspreises 2017.',
    'worum': [
        'Das Deutsch-Syrische Forum bietet Ärzten, Zahnärzten und Apothekern mit '
        'arabischer Herkunft eine Plattform zum Austausch. Das Ziel besteht darin, '
        'den geflohenen Kolleginnen und Kollegen die berufliche Integration zu '
        'erleichtern. Bei regelmäßigen Treffen werden Fragen rund um die '
        'Approbation, den (Fach-)Spracherwerb und die Berufserlaubnis erläutert '
        'sowie Fortbildungsmöglichkeiten aufgezeigt.',
        'Darüber hinaus bietet das Forum ein Mentorenprojekt für Medizinerinnen '
        'und Mediziner mit Fluchterfahrung. Durch die Eins-zu-eins-Begleitung '
        'können Bedarfe individuell identifiziert und Maßnahmen ergriffen werden. '
        'Auf diese Weise trägt das Forum zur Integration von dringend benötigten '
        'Fachkräften aus dem Gesundheitssektor bei.',
    ],
    'angebot': [
        ('Regelmäßige Treffen',
         'Austausch unter Kolleginnen und Kollegen, offen für Ärztinnen und Ärzte, '
         'Zahnärztinnen und Zahnärzte sowie Apothekerinnen und Apotheker.'),
        ('Wege zur Approbation',
         'Informationen zu Anerkennung, Berufserlaubnis und den nötigen Prüfungen.'),
        ('Fachsprache',
         'Hinweise zum medizinischen Spracherwerb und zur Fachsprachprüfung.'),
        ('Mentoring',
         'Eins-zu-eins-Begleitung durch erfahrene Kolleginnen und Kollegen.'),
    ],
    'einladung_bild': BILD + 'forum-aerzte-einladung-800.jpg',
    'einladung_alt': 'Einladung zu einem Forumstreffen, deutsch und arabisch',
    'einladung_unterschrift': 'Einladung zu einem Forumstreffen (deutsch/arabisch).',
    'extern': ('forum.alkawakibi.org', 'http://forum.alkawakibi.org/'),
    'extern_hinweis': 'Die Seite des Forums wird gesondert gepflegt.',
}

# ---------------------------------------------------------------- Spenden

SPENDEN_EINLEITUNG = (
    'Wir arbeiten ehrenamtlich und finanzieren unsere Arbeit aus '
    'Mitgliedsbeiträgen und Spenden. Jeder Betrag kommt direkt in den '
    'Projekten an.'
)

SPENDEN_WOHIN = [
    ('Bildung und Begegnung',
     'Räume, Referentinnen und Referenten, Material für Seminare, Workshops und '
     'Nachbarschaftsfeste.'),
    ('Epithetik-Projekt',
     'Material und Reisen für die epithetische Versorgung von Kriegsverletzten '
     'und das Coaching vor Ort.'),
    ('Forum für Medizinerinnen und Mediziner',
     'Treffen, Informationsmaterial und das Mentorenprojekt.'),
]

SPENDENQUITTUNG = [
    'Alkawakibi Verein e. V. ist beim Finanzamt für Körperschaften als '
    'gemeinnützig anerkannt – für kulturelle Zwecke, Bildung und '
    'Entwicklungshilfe (Steuernummer 27/660/63668). Für Spenden stellen wir auf '
    'Wunsch eine Zuwendungsbestätigung aus. Bitte geben Sie dafür Ihre Anschrift '
    'im Verwendungszweck an oder schreiben Sie uns an info@alkawakibi.org.',
]
SPENDENQUITTUNG_HINWEIS = ('Bis 300 Euro genügt gegenüber dem Finanzamt in der '
                           'Regel der Kontoauszug als Nachweis.')

ANDERE_WEGE = [
    ('Mitglied werden',
     'Werden Sie Teil des Vereins und gestalten Sie mit.', 'mitglied-werden.html'),
    ('Freund des Vereins werden',
     'Die Satzung kennt „Freunde des Vereins“: Menschen, die keine Mitglieder '
     'sind, aber unsere Ziele teilen und uns mit ihren Fähigkeiten unterstützen.',
     'kontakt.html'),
    ('Weitersagen',
     'Erzählen Sie von unserer Arbeit – in Ihrem Verein, Ihrer Praxis, Ihrer '
     'Nachbarschaft.', None),
]

SPENDENAUFRUF = {
    'titel': 'Ihre Spende wirkt',
    'text': 'Alkawakibi e. V. ist als gemeinnützig anerkannt und arbeitet '
            'ehrenamtlich. Jeder Beitrag fließt direkt in unsere Bildungs-, '
            'Begegnungs- und Hilfsprojekte.',
}

# ---------------------------------------------------------------- Mitgliedschaft

MITGLIED_EINLEITUNG = ('Sie möchten Mitglied werden? Wunderbar. Hier finden Sie '
                       'den Aufnahmeantrag – auf Deutsch und auf Arabisch.')

MITGLIED_SCHRITTE = [
    ('Antrag ausfüllen',
     'Laden Sie den Aufnahmeantrag herunter und füllen Sie ihn aus.'),
    ('Antrag einreichen',
     'Senden Sie den unterschriebenen Antrag an den Vorstand – per Post an '
     'Triftstr. 8, 13353 Berlin, oder per E-Mail an info@alkawakibi.org.'),
    ('Bestätigung',
     'Der Vorstand entscheidet über die Aufnahme und bestätigt sie schriftlich.'),
    ('Assoziierte Mitgliedschaft',
     'Die Aufnahme erfolgt zunächst als assoziiertes Mitglied. Nach einem Jahr '
     'kann die Ernennung zum ordentlichen Mitglied erfolgen.'),
]

MITGLIED_DOWNLOADS = [
    ('Aufnahmeantrag (Deutsch)', 'PDF', 'assets/dokumente/mitgliedsantrag-deutsch.pdf', None),
    ('Aufnahmeantrag (Deutsch)', 'Word', 'assets/dokumente/mitgliedsantrag-deutsch.docx', None),
    ('طلب انتساب', 'PDF', 'assets/dokumente/mitgliedsantrag-arabisch.pdf', 'ar'),
    ('طلب انتساب', 'Word', 'assets/dokumente/mitgliedsantrag-arabisch.docx', 'ar'),
]

MITGLIED_BEITRAG = ('Die Höhe des Jahresbeitrags legt die Generalversammlung '
                    'fest; Näheres regelt die Beitragsordnung.')

# ---------------------------------------------------------------- Kontakt

KONTAKT_EINLEITUNG = ('Sie haben eine Frage, möchten mitarbeiten oder ein Projekt '
                      'unterstützen? Schreiben Sie uns.')

FORMULAR_BETREFFE = ['Allgemeine Anfrage', 'Mitgliedschaft', 'Spenden',
                     'Epithetik-Projekt',
                     'Forum für Ärzte, Zahnärzte und Apotheker',
                     'Presse', 'Sonstiges']

FORMULAR_EINWILLIGUNG = ('Ich bin damit einverstanden, dass meine Angaben zur '
                         'Bearbeitung meiner Anfrage gespeichert werden. Hinweise '
                         'dazu in der {datenschutz}.')

FORMULAR_MELDUNGEN = {
    'erfolg': 'Vielen Dank. Ihre Nachricht ist bei uns eingegangen – wir melden '
              'uns zeitnah.',
    'fehler': 'Das Senden hat leider nicht geklappt. Bitte schreiben Sie uns '
              'direkt an info@alkawakibi.org.',
}

ANFAHRT = ('Der Vereinssitz liegt in Berlin-Wedding. Bitte vereinbaren Sie vor '
           'einem Besuch einen Termin.')

# ---------------------------------------------------------------- Rechtliches

IMPRESSUM = [
    ('Angaben gemäß § 5 DDG', [
        'Alkawakibi Verein e. V.', 'Triftstr. 8', '13353 Berlin']),
    ('Vertreten durch den Vorstand', ['Rami Kanoua (Vorsitzender)']),
    ('Kontakt', ['E-Mail: info@alkawakibi.org']),
    ('Registereintrag', [
        'Eintragung im Vereinsregister',
        'Registergericht: Amtsgericht Charlottenburg',
        'Registernummer: VR 31792 B']),
    ('Steuerliche Angaben', [
        'Anerkannt beim Finanzamt für Körperschaften als gemeinnützige '
        'Körperschaft zur Förderung kultureller Zwecke, der Bildung und der '
        'Entwicklungshilfe.',
        'Steuernummer: 27/660/63668']),
    ('Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV', [
        'Rami Kanoua', 'Triftstr. 8', '13353 Berlin']),
    ('Bildnachweise', [
        'Fotos: Alkawakibi Verein e. V.',
        'Porträt Abd ar-Rahman al-Kawakibi: historische Aufnahme, gemeinfrei.']),
    ('Haftung für Inhalte', [
        'Als Diensteanbieter sind wir für eigene Inhalte auf diesen Seiten nach '
        'den allgemeinen Gesetzen verantwortlich. Wir sind jedoch nicht '
        'verpflichtet, übermittelte oder gespeicherte fremde Informationen zu '
        'überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige '
        'Tätigkeit hinweisen.']),
    ('Haftung für Links', [
        'Unser Angebot enthält Links zu externen Websites Dritter, auf deren '
        'Inhalte wir keinen Einfluss haben. Für die Inhalte der verlinkten Seiten '
        'ist stets der jeweilige Anbieter oder Betreiber verantwortlich. Zum '
        'Zeitpunkt der Verlinkung waren keine Rechtsverstöße erkennbar.']),
    ('Urheberrecht', [
        'Die durch die Betreiber erstellten Inhalte und Werke auf diesen Seiten '
        'unterliegen dem deutschen Urheberrecht. Beiträge Dritter sind als solche '
        'gekennzeichnet.']),
]

DATENSCHUTZ_HINWEIS = ('Entwurf – vor der Veröffentlichung rechtlich prüfen '
                       'lassen. Dieser Hinweis wird vor dem Livegang entfernt.')

DATENSCHUTZ = [
    ('Verantwortlicher', [
        'Alkawakibi Verein e. V., Triftstr. 8, 13353 Berlin, info@alkawakibi.org']),
    ('Hosting', [
        'Diese Website wird über GitHub Pages (GitHub Inc.) bereitgestellt. Beim '
        'Aufruf werden technisch notwendige Zugriffsdaten wie IP-Adresse, Datum '
        'und Uhrzeit verarbeitet. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO.']),
    ('Kontaktformular', [
        'Die im Formular angegebenen Daten (Name, E-Mail-Adresse, optional '
        'Telefonnummer, Betreff und Nachricht) übermitteln wir über einen Dienst '
        'von Google (Google Apps Script) an unsere Datenbank bei Supabase, wo sie '
        'zur Bearbeitung Ihrer Anfrage gespeichert werden. Rechtsgrundlage ist '
        'Art. 6 Abs. 1 lit. a und lit. b DSGVO. Wir löschen die Daten, sobald die '
        'Anfrage abschließend bearbeitet ist und keine gesetzlichen '
        'Aufbewahrungspflichten entgegenstehen.']),
    ('Keine Cookies, keine Analyse', [
        'Diese Website setzt keine Cookies zu Analyse- oder Werbezwecken und '
        'bindet keine Dienste Dritter zur Reichweitenmessung ein. Schriften '
        'werden lokal ausgeliefert.']),
    ('Ihre Rechte', [
        'Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, '
        'Datenübertragbarkeit und Widerspruch nach Art. 15 bis 21 DSGVO. Eine '
        'erteilte Einwilligung können Sie jederzeit widerrufen. Außerdem haben '
        'Sie das Recht, sich bei einer Aufsichtsbehörde zu beschweren – für '
        'Berlin: Berliner Beauftragte für Datenschutz und Informationsfreiheit.']),
    ('Kontakt in Datenschutzfragen', ['info@alkawakibi.org']),
]

# ---------------------------------------------------------------- Seitenköpfe

HERO = {
    'dachzeile': 'Deutsch-syrischer Verein in Berlin',
    'titel': 'Demokratie wächst dort, wo Menschen einander zuhören.',
    'hervor': 'zuhören',
    'text': 'Alkawakibi e. V. stärkt Menschenrechte und demokratische Werte – '
            'durch Bildung, Begegnung und humanitäre Hilfe. In Berlin, in '
            'Deutschland und über Grenzen hinweg.',
    'bild': BILD + 'veranstaltung-publikum-800.jpg',
    'breite': 800, 'hoehe': 534,
    'alt': 'Volles Publikum bei einer Veranstaltung des Alkawakibi Verein e. V.',
}

SEITEN = {
    'index.html': {
        'titel': 'Alkawakibi e. V. – Für Demokratie und Menschenrechte',
        'beschreibung': 'Alkawakibi e. V. ist ein deutsch-syrischer Verein in '
                        'Berlin. Wir stärken Menschenrechte, demokratische Werte '
                        'und den Aufbau einer lebendigen Zivilgesellschaft.',
        'h1': 'Demokratie wächst dort, wo Menschen einander zuhören.'},
    'wer-wir-sind.html': {
        'titel': 'Wer sind wir – Alkawakibi e. V.',
        'beschreibung': 'Leitgedanke, Ziele und Vorstand des deutsch-syrischen '
                        'Vereins Alkawakibi e. V. in Berlin.',
        'h1': 'Wer sind wir', 'kicker': 'Über den Verein',
        'einleitung': 'Ein deutsch-syrischer Verein in Berlin, der sich seit über '
                      'zehn Jahren für Menschenrechte, demokratische Bildung und '
                      'eine starke Zivilgesellschaft einsetzt.'},
    'namensgeber.html': {
        'titel': 'Abd ar-Rahman al-Kawakibi – Namensgeber des Vereins | Alkawakibi e. V.',
        'beschreibung': 'Abd ar-Rahman al-Kawakibi (1855–1902), syrischer '
                        'Publizist und Reformer – der Namensgeber des Vereins.',
        'h1': 'Abd ar-Rahman al-Kawakibi', 'kicker': 'Unser Namensgeber',
        'einleitung': ''},
    'aktivitaeten.html': {
        'titel': 'Unsere Aktivitäten – Alkawakibi e. V.',
        'beschreibung': 'Projekte und Arbeitsfelder des Alkawakibi Verein e. V.: '
                        'Epithetik-Projekt, Forum für Ärzte, politische Bildung '
                        'und Begegnung in der Nachbarschaft.',
        'h1': 'Unsere Aktivitäten', 'kicker': 'Was wir tun',
        'einleitung': AKTIVITAETEN_EINLEITUNG},
    'projekt-epithetik.html': {
        'titel': 'Epithetik-Projekt – Alkawakibi e. V.',
        'beschreibung': 'Epithetische Versorgung von Kriegsverletzten in Idlib '
                        'und Reyhanli – ein Hilfsprojekt des Alkawakibi Verein e. V.',
        'h1': 'Epithetik-Projekt', 'kicker': 'Projekt',
        'einleitung': EPITHETIK['einleitung']},
    'projekt-forum.html': {
        'titel': 'Forum für Ärzte, Zahnärzte und Apotheker – Alkawakibi e. V.',
        'beschreibung': 'Das Deutsch-Syrische Forum erleichtert geflüchteten '
                        'Medizinerinnen und Medizinern die berufliche Integration. '
                        '1. Preis des Berliner Gesundheitspreises 2017.',
        'h1': 'Forum für Ärzte, Zahnärzte und Apotheker', 'kicker': 'Projekt',
        'einleitung': FORUM['einleitung']},
    'spenden.html': {
        'titel': 'Spenden – Alkawakibi e. V.',
        'beschreibung': 'Unterstützen Sie die Arbeit des Alkawakibi Verein e. V. '
                        'Bankverbindung, Spendenquittung und weitere Wege zu helfen.',
        'h1': 'Spenden', 'kicker': 'Unterstützen',
        'einleitung': SPENDEN_EINLEITUNG},
    'mitglied-werden.html': {
        'titel': 'Mitglied werden – Alkawakibi e. V.',
        'beschreibung': 'Aufnahmeantrag für die Mitgliedschaft im Alkawakibi '
                        'Verein e. V. – auf Deutsch und auf Arabisch.',
        'h1': 'Mitglied werden', 'kicker': 'Mitmachen',
        'einleitung': MITGLIED_EINLEITUNG},
    'kontakt.html': {
        'titel': 'Kontakt – Alkawakibi e. V.',
        'beschreibung': 'Kontaktangaben und Kontaktformular des Alkawakibi '
                        'Verein e. V. in Berlin.',
        'h1': 'Kontakt', 'kicker': 'Schreiben Sie uns',
        'einleitung': KONTAKT_EINLEITUNG},
    'satzung.html': {
        'titel': 'Satzung – Alkawakibi e. V.',
        'beschreibung': 'Vollständige Satzung des Alkawakibi Verein e. V., '
                        'beschlossen in Berlin am 29. Mai 2015.',
        'h1': 'Satzung', 'kicker': 'Grundlage',
        'einleitung': 'Satzung des Alkawakibi Verein e. V., beschlossen in Berlin '
                      'am 29. Mai 2015.'},
    'impressum.html': {
        'titel': 'Impressum – Alkawakibi e. V.',
        'beschreibung': 'Impressum und Anbieterkennzeichnung des Alkawakibi '
                        'Verein e. V.',
        'h1': 'Impressum', 'kicker': 'Pflichtangaben', 'einleitung': ''},
    'datenschutz.html': {
        'titel': 'Datenschutzerklärung – Alkawakibi e. V.',
        'beschreibung': 'Informationen zur Verarbeitung personenbezogener Daten '
                        'auf der Website des Alkawakibi Verein e. V.',
        'h1': 'Datenschutzerklärung', 'kicker': 'Pflichtangaben', 'einleitung': ''},
    '404.html': {
        'titel': 'Seite nicht gefunden – Alkawakibi e. V.',
        'beschreibung': 'Die aufgerufene Seite existiert nicht.',
        'h1': 'Seite nicht gefunden', 'kicker': 'Fehler 404',
        'einleitung': 'Die Seite, die Sie suchen, gibt es nicht – vielleicht wurde '
                      'sie verschoben oder die Adresse enthält einen Tippfehler.'},
}

REIHENFOLGE = ['index.html', 'wer-wir-sind.html', 'namensgeber.html',
               'aktivitaeten.html', 'projekt-epithetik.html', 'projekt-forum.html',
               'spenden.html', 'mitglied-werden.html', 'kontakt.html',
               'satzung.html', 'impressum.html', 'datenschutz.html']
