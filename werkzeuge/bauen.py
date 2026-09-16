#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt die drei Website-Entwürfe.

Aufruf aus dem Projektordner:
    python3 werkzeuge/bauen.py            alle drei Entwürfe
    python3 werkzeuge/bauen.py 1          nur Entwurf 1
"""
import os
import shutil
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
WURZEL = os.path.dirname(HIER)
sys.path.insert(0, HIER)

import basis
import inhalte as I
import skripte
from entwurf1 import PetrolGold
from entwurf2 import Institut
from entwurf3 import Manifest

DOMAIN = 'https://alkawakibi.org/'


def seiteninhalt(d, datei, paragrafen):
    if datei == 'index.html':
        return basis.startseite(d)
    if datei == 'wer-wir-sind.html':
        return basis.wer_wir_sind(d)
    if datei == 'namensgeber.html':
        return basis.namensgeber(d)
    if datei == 'aktivitaeten.html':
        return basis.aktivitaeten(d)
    if datei == 'projekt-epithetik.html':
        return basis.projekt_epithetik(d)
    if datei == 'projekt-forum.html':
        return basis.projekt_forum(d)
    if datei == 'spenden.html':
        return basis.spenden(d)
    if datei == 'mitglied-werden.html':
        return basis.mitglied_werden(d)
    if datei == 'kontakt.html':
        return basis.kontakt(d)
    if datei == 'satzung.html':
        return basis.satzung(d, paragrafen)
    if datei == 'impressum.html':
        return basis.rechtstext(d, datei, I.IMPRESSUM)
    if datei == 'datenschutz.html':
        return basis.rechtstext(d, datei, I.DATENSCHUTZ, I.DATENSCHUTZ_HINWEIS)
    if datei == '404.html':
        return basis.fehlerseite(d)
    raise ValueError('unbekannte Seite: ' + datei)


def assets_kopieren(ziel):
    quelle = os.path.join(WURZEL, 'assets')
    zielordner = os.path.join(ziel, 'assets')
    for unterordner in ('bilder', 'schriften', 'dokumente'):
        von = os.path.join(quelle, unterordner)
        nach = os.path.join(zielordner, unterordner)
        if not os.path.isdir(von):
            continue
        if os.path.isdir(nach):
            shutil.rmtree(nach)
        shutil.copytree(von, nach)
    schriften_json = os.path.join(zielordner, 'schriften', 'schriften.json')
    if os.path.exists(schriften_json):
        os.remove(schriften_json)


def nebendateien(d, ziel):
    seiten = I.REIHENFOLGE
    eintraege = '\n'.join(
        '  <url><loc>%s%s</loc><changefreq>monthly</changefreq>'
        '<priority>%s</priority></url>'
        % (DOMAIN, '' if s == 'index.html' else s, '1.0' if s == 'index.html' else '0.7')
        for s in seiten)
    basis.schreiben(os.path.join(ziel, 'sitemap.xml'),
                    '<?xml version="1.0" encoding="UTF-8"?>\n'
                    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                    + eintraege + '\n</urlset>')

    basis.schreiben(os.path.join(ziel, 'robots.txt'),
                    'User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n' % DOMAIN)

    with open(os.path.join(ziel, '.nojekyll'), 'w') as f:
        f.write('')

    basis.schreiben(os.path.join(ziel, 'assets', 'js', 'konfiguration.js'),
                    skripte.KONFIGURATION)
    basis.schreiben(os.path.join(ziel, 'assets', 'js', 'haupt.js'),
                    skripte.haupt_js(d.js_zusatz(), d.js_start()))
    basis.schreiben(os.path.join(ziel, 'assets', 'css', 'stil.css'), d.css())
    basis.schreiben(os.path.join(ziel, 'README.md'), d.liesmich())


def bauen(d):
    ziel = os.path.join(WURZEL, 'frontend', d.kennung)
    d.ordner = ziel
    os.makedirs(ziel, exist_ok=True)

    # alte Erzeugnisse entfernen, Ordner sonst unangetastet lassen
    for name in os.listdir(ziel):
        if name.endswith(('.html', '.xml', '.txt', '.md')) or name == '.nojekyll':
            os.remove(os.path.join(ziel, name))

    assets_kopieren(ziel)
    paragrafen = basis.satzung_lesen(os.path.join(WURZEL, 'inhalte', 'satzung.md'))

    for datei in I.REIHENFOLGE + ['404.html']:
        inhalt = seiteninhalt(d, datei, paragrafen)
        basis.schreiben(os.path.join(ziel, datei), d.rahmen(datei, inhalt))

    nebendateien(d, ziel)
    anzahl = len([x for x in os.listdir(ziel) if x.endswith('.html')])
    print('%-26s %2d Seiten  ->  frontend/%s/' % (d.name, anzahl, d.kennung))


if __name__ == '__main__':
    entwuerfe = {'1': PetrolGold, '2': Institut, '3': Manifest}
    gewaehlt = sys.argv[1:] or ['1', '2', '3']
    for nummer in gewaehlt:
        bauen(entwuerfe[nummer]())
