# -*- coding: utf-8 -*-
"""Gemeinsames Gerüst für alle drei Entwürfe.

Die Seiteninhalte werden hier einmal zusammengesetzt und dabei ausschließlich
über die Bausteine des jeweiligen Entwurfs ausgegeben. Dadurch sind die Texte
in allen Entwürfen identisch, das Aussehen aber völlig verschieden.
"""
import html
import os
import re

import inhalte as I


def e(text):
    """Text für HTML absichern."""
    return html.escape(str(text), quote=False)


def schreiben(pfad, text):
    os.makedirs(os.path.dirname(pfad) or '.', exist_ok=True)
    with open(pfad, 'w', encoding='utf-8') as f:
        f.write(text.rstrip() + '\n')


# ------------------------------------------------------------------ Satzung

def satzung_lesen(quelle):
    """Liest inhalte/satzung.md und gibt [(id, titel, [knoten])] zurück.

    Ein Knoten ist ('punkt', text) oder ('unterpunkt', text) oder
    ('zwischentitel', text) oder ('absatz', text).
    """
    zeilen = open(quelle, encoding='utf-8').read().split('\n')
    paragrafen, aktuell = [], None
    for zeile in zeilen:
        roh = zeile.rstrip()
        if not roh.strip():
            continue
        if roh.startswith('## '):
            titel = roh[3:].strip()
            nummer = re.match(r'§\s*(\d+)', titel)
            kennung = 'paragraf-' + (nummer.group(1) if nummer else str(len(paragrafen) + 1))
            aktuell = {'id': kennung, 'titel': titel, 'knoten': []}
            paragrafen.append(aktuell)
        elif roh.startswith('### '):
            if aktuell:
                aktuell['knoten'].append(('zwischentitel', roh[4:].strip()))
        elif aktuell is not None:
            eingerueckt = len(roh) - len(roh.lstrip())
            text = roh.strip()
            nummeriert = re.match(r'^\d+\.\s+(.*)$', text)
            aufzaehlung = re.match(r'^-\s+(.*)$', text)
            if nummeriert:
                art = 'unterpunkt' if eingerueckt >= 4 else 'punkt'
                aktuell['knoten'].append((art, nummeriert.group(1)))
            elif aufzaehlung:
                aktuell['knoten'].append(('unterpunkt', aufzaehlung.group(1)))
            else:
                aktuell['knoten'].append(('absatz', text))
    # Kopfzeilen der Datei (Titel, Vorbemerkung) verwerfen
    return [p for p in paragrafen if p['titel'].startswith('§')]


# ------------------------------------------------------------------ Formular

FORMULARFELDER = [
    ('name', 'Name', 'text', True, 'name'),
    ('email', 'E-Mail', 'email', True, 'email'),
    ('telefon', 'Telefon (optional)', 'tel', False, 'tel'),
]


def formular_felder_html(d):
    """Baut die Formularfelder – Darstellung übernimmt der Entwurf."""
    teile = []
    for kennung, beschriftung, art, pflicht, autofill in FORMULARFELDER:
        teile.append(d.feld(kennung, beschriftung, art, pflicht, autofill))
    teile.append(d.auswahl('betreff', 'Betreff', I.FORMULAR_BETREFFE, True))
    teile.append(d.textfeld('nachricht', 'Nachricht', True))
    einwilligung = I.FORMULAR_EINWILLIGUNG.format(
        datenschutz='<a href="datenschutz.html">Datenschutzerklärung</a>')
    teile.append(d.haken('einwilligung', einwilligung, True))
    return '\n'.join(teile)


# ------------------------------------------------------------------ Seiten

def startseite(d):
    t = []
    t.append(d.hero())
    t.append(d.abschnitt(d.zitat(I.LEITGEDANKE, I.LEITGEDANKE_QUELLE), ton='zitat'))

    wer = (d.kicker('Der Verein') + d.h2('Wer wir sind')
           + ''.join(d.absatz(p) for p in I.WER_WIR_SIND)
           + d.schaltflaechen([('Mehr über uns', 'wer-wir-sind.html', 1)]))
    t.append(d.abschnitt(d.zweispalter(
        wer,
        d.bild(I.BILD + 'seminar-runde-800.jpg',
               'Teilnehmende sitzen im Stuhlkreis bei einem Seminar des Vereins',
               None, 800, 600)), ton='hell'))

    felder = (d.kicker('Arbeitsfelder') + d.h2('Woran wir arbeiten')
              + d.karten([{'titel': tt, 'text': tx} for tt, tx in I.ARBEITSFELDER]))
    t.append(d.abschnitt(felder))

    a = I.AUSZEICHNUNG
    aus = (d.kicker(a['kicker']) + d.h2(a['titel']) + d.absatz(a['text'])
           + d.schaltflaechen([(a['linktext'], a['ziel'], 1)]))
    t.append(d.abschnitt(d.zweispalter(
        aus, d.bild(a['bild_klein'], a['alt'], a['bildunterschrift'], 800, 600),
        bild_zuerst=True), ton='hell'))

    teaser = []
    for p in I.PROJEKTE:
        teaser.append({'titel': p['titel'], 'text': p['text'], 'ziel': p['ziel'],
                       'linktext': p['linktext'], 'bild': p.get('bild'),
                       'alt': p.get('alt')})
    teaser.append({'titel': 'Bildung & Begegnung',
                   'text': 'Seminare, Podiumsdiskussionen und Nachbarschaftsfeste '
                           'in Berlin.',
                   'ziel': 'aktivitaeten.html', 'linktext': 'Alle Aktivitäten',
                   'bild': I.BILD + 'seminar-runde-800.jpg',
                   'alt': 'Seminar des Vereins im Stuhlkreis'})
    t.append(d.abschnitt(d.kicker('Unsere Aktivitäten') + d.h2('Woran wir gerade arbeiten')
                         + d.karten(teaser)))

    s = I.SPENDENAUFRUF
    t.append(d.abschnitt(d.aufruf(s['titel'], s['text'], [
        ('Jetzt spenden', 'spenden.html', 1),
        ('Mitglied werden', 'mitglied-werden.html', 2)]), ton='aufruf'))
    return '\n'.join(t)


def wer_wir_sind(d):
    t = [d.seitenkopf('wer-wir-sind.html')]
    t.append(d.abschnitt(d.kicker('Unser Leitgedanke')
                         + d.zitat(I.LEITGEDANKE, I.LEITGEDANKE_QUELLE), ton='zitat'))
    t.append(d.abschnitt(d.h2('Wer wir sind')
                         + ''.join(d.absatz(p) for p in I.WER_WIR_SIND), ton='hell'))
    t.append(d.abschnitt(d.h2('Unsere Ziele')
                         + d.nummernliste(I.ZIELE)))
    t.append(d.abschnitt(d.h2('So arbeiten wir') + d.nummernliste(I.ARBEITSWEISE)
                         + d.schaltflaechen([('Vollständige Satzung lesen', 'satzung.html', 2)]),
                         ton='hell'))
    t.append(d.abschnitt(
        d.h2('Unser Vorstand')
        + d.absatz('Der Vorstand führt den Verein ehrenamtlich. Er besteht '
                   'satzungsgemäß aus fünf Mitgliedern.')
        + d.personen(I.VORSTAND)
        + d.absatz('Sie erreichen den Vorstand über unser '
                   '<a href="kontakt.html">Kontaktformular</a>.')))
    namensgeber = (d.kicker('Woher der Name kommt') + d.h2('Abd ar-Rahman al-Kawakibi')
                   + d.absatz('Der Verein trägt den Namen von Abd ar-Rahman '
                              'al-Kawakibi (1855–1902) – einem syrischen '
                              'Publizisten, der schon vor über hundert Jahren über '
                              'die Mechanik der Despotie schrieb und für Reformen '
                              'in der arabischen Welt eintrat.')
                   + d.schaltflaechen([('Mehr zum Namensgeber', 'namensgeber.html', 1)]))
    t.append(d.abschnitt(d.zweispalter(
        namensgeber,
        d.bild('assets/bilder/namensgeber/al-kawakibi.jpg',
               'Historisches Porträt von Abd ar-Rahman al-Kawakibi',
               'Abd ar-Rahman al-Kawakibi (1855–1902)', 566, 850)), ton='hell'))
    return '\n'.join(t)


def namensgeber(d):
    t = [d.seitenkopf('namensgeber.html')]
    bio = []
    for absatz in I.NAMENSGEBER_BIO:
        text = absatz
        for schluessel, (beschriftung, adresse) in I.NAMENSGEBER_LINKS.items():
            text = text.replace(
                '{%s}' % schluessel,
                '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
                % (adresse, beschriftung))
        bio.append(d.absatz(text, roh=True))
    t.append(d.abschnitt(d.zweispalter(
        ''.join(bio),
        d.bild('assets/bilder/namensgeber/al-kawakibi.jpg',
               'Historisches Porträt von Abd ar-Rahman al-Kawakibi',
               'Abd ar-Rahman al-Kawakibi (1855–1902)', 566, 850),
        bild_zuerst=True)))
    t.append(d.abschnitt(
        d.kicker('Aus unseren Fachinformationen') + d.h2('Was ist Despotie?')
        + ''.join(d.absatz(p) for p in I.DESPOTIE)
        + d.hervorhebung(I.DESPOTIE_SCHLUSS), ton='hell'))
    return '\n'.join(t)


def aktivitaeten(d):
    t = [d.seitenkopf('aktivitaeten.html')]
    for p in I.PROJEKTE:
        block = (d.kicker('Projekt') + d.h2(p['titel'])
                 + d.unterzeile(p['untertitel']) + d.absatz(p['text'])
                 + d.schaltflaechen([(p['linktext'], p['ziel'], 1)]))
        if p.get('bild'):
            t.append(d.abschnitt(d.zweispalter(
                block, d.bild(p['bild'], p['alt'], None, 800, 1134)), ton='hell'))
        else:
            t.append(d.abschnitt(block))
    for feld in I.ARBEITSFELDER_SEITE:
        t.append(d.abschnitt(
            d.h2(feld['titel']) + d.absatz(feld['text'])
            + d.bildreihe(feld['bilder'])))
    t.append(d.abschnitt(
        d.h2('Impressionen') + d.galerie(I.GALERIE)
        + d.hinweis(I.GALERIE_HINWEIS), ton='hell'))
    t.append(d.abschnitt(d.aufruf(
        'Dabei sein',
        'Sie möchten bei einer Veranstaltung dabei sein oder ein Projekt '
        'unterstützen?',
        [('Kontakt aufnehmen', 'kontakt.html', 1),
         ('Mitglied werden', 'mitglied-werden.html', 2)]), ton='aufruf'))
    return '\n'.join(t)


def projekt_epithetik(d):
    p = I.EPITHETIK
    t = [d.seitenkopf('projekt-epithetik.html')]
    t.append(d.abschnitt(d.h2('Worum es geht')
                         + ''.join(d.absatz(x) for x in p['worum'])))
    t.append(d.abschnitt(d.h2('Was ist Epithetik?')
                         + ''.join(d.absatz(x) for x in p['was_ist']), ton='hell'))
    t.append(d.abschnitt(
        d.kicker('Spendenaufruf') + d.h2(p['aufruf_titel'])
        + d.absatz(p['aufruf_text']) + d.konto(I.KONTO_EPITHETIK)
        + d.schaltflaechen([('Alle Spendenwege', 'spenden.html', 1)]), ton='aufruf'))
    t.append(d.abschnitt(
        d.h2('Weiterführend')
        + d.absatz('<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
                   % (p['extern'][1], e(p['extern'][0])), roh=True)
        + d.hinweis(p['extern_hinweis'])))
    return '\n'.join(t)


def projekt_forum(d):
    p = I.FORUM
    a = I.AUSZEICHNUNG
    t = [d.seitenkopf('projekt-forum.html')]
    t.append(d.abschnitt(d.h2('Worum es geht')
                         + ''.join(d.absatz(x) for x in p['worum'])))
    t.append(d.abschnitt(d.zweispalter(
        d.kicker('Auszeichnung') + d.h2('1. Preis des Berliner Gesundheitspreises')
        + d.absatz('2017 erhielt das Forum den 1. Preis des Berliner '
                   'Gesundheitspreises.'),
        d.bild(a['bild_klein'], a['alt'], a['bildunterschrift'], 800, 600),
        bild_zuerst=True), ton='hell'))
    t.append(d.abschnitt(d.h2('Das Angebot im Überblick')
                         + d.nummernliste(p['angebot'])))
    t.append(d.abschnitt(d.zweispalter(
        d.h2('Weiterführend')
        + d.absatz('<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
                   % (p['extern'][1], e(p['extern'][0])), roh=True)
        + d.hinweis(p['extern_hinweis']),
        d.bild(p['einladung_bild'], p['einladung_alt'],
               p['einladung_unterschrift'], 800, 1134)), ton='hell'))
    return '\n'.join(t)


def spenden(d):
    t = [d.seitenkopf('spenden.html')]
    t.append(d.abschnitt(d.h2('Wohin Ihre Spende geht')
                         + d.karten([{'titel': tt, 'text': tx}
                                     for tt, tx in I.SPENDEN_WOHIN])))
    t.append(d.abschnitt(d.h2('Spendenkonto')
                         + d.konto(I.KONTO_VEREIN) + d.konto(I.KONTO_EPITHETIK),
                         ton='hell'))
    t.append(d.abschnitt(d.h2('Spendenquittung')
                         + ''.join(d.absatz(x) for x in I.SPENDENQUITTUNG)
                         + d.hinweis(I.SPENDENQUITTUNG_HINWEIS)))
    wege = []
    for titel, text, ziel in I.ANDERE_WEGE:
        eintrag = {'titel': titel, 'text': text}
        if ziel:
            eintrag['ziel'] = ziel
            eintrag['linktext'] = 'Mehr erfahren'
        wege.append(eintrag)
    t.append(d.abschnitt(d.h2('Andere Wege zu helfen') + d.karten(wege), ton='hell'))
    return '\n'.join(t)


def mitglied_werden(d):
    t = [d.seitenkopf('mitglied-werden.html')]
    t.append(d.abschnitt(d.h2('So wird man Mitglied')
                         + d.nummernliste(I.MITGLIED_SCHRITTE)))
    t.append(d.abschnitt(d.h2('Antrag herunterladen')
                         + d.downloads(I.MITGLIED_DOWNLOADS), ton='hell'))
    t.append(d.abschnitt(d.h2('Beitrag') + d.absatz(I.MITGLIED_BEITRAG)
                         + d.absatz('Bei Fragen stehen wir Ihnen gern zur '
                                    'Verfügung – über unser '
                                    '<a href="kontakt.html">Kontaktformular</a>.')))
    return '\n'.join(t)


def kontakt(d):
    t = [d.seitenkopf('kontakt.html')]
    t.append(d.abschnitt(d.zweispalter(
        d.h2('Kontaktangaben') + d.anschrift(),
        d.h2('Anfahrt') + d.absatz(I.ANFAHRT))))
    t.append(d.abschnitt(d.formular(), ton='hell'))
    return '\n'.join(t)


def satzung(d, paragrafen):
    t = [d.seitenkopf('satzung.html')]
    t.append(d.abschnitt(d.textbereich(d.inhaltsverzeichnis(paragrafen),
                                       d.satzungstext(paragrafen)), ton='text'))
    return '\n'.join(t)


def rechtstext(d, seite, abschnitte, vorhinweis=None):
    t = [d.seitenkopf(seite)]
    inhalt = ''
    if vorhinweis:
        inhalt += d.hinweis(vorhinweis, stark=True)
    for titel, zeilen in abschnitte:
        inhalt += d.h2(titel)
        for zeile in zeilen:
            inhalt += d.absatz(zeile)
    t.append(d.abschnitt(d.textbereich(d.randspalte(seite), inhalt), ton='text'))
    return '\n'.join(t)


def fehlerseite(d):
    t = [d.seitenkopf('404.html')]
    t.append(d.abschnitt(d.schaltflaechen([
        ('Zur Startseite', 'index.html', 1),
        ('Unsere Aktivitäten', 'aktivitaeten.html', 2),
        ('Kontakt', 'kontakt.html', 2)])))
    return '\n'.join(t)
