# Kontaktformular – Einrichtung

Die Website liegt auf GitHub Pages und hat damit keinen eigenen Server. Das
Kontaktformular schickt seine Daten deshalb an eine **Google-Apps-Script-Webanwendung**,
die sie in eine **Supabase-Datenbank** schreibt und dem Verein eine
Benachrichtigung per E-Mail sendet.

```
Formular (Browser)  ──POST JSON──▶  Apps Script  ──REST──▶  Supabase
                                         └──────────────▶  E-Mail an den Verein
```

Der Supabase-Schlüssel liegt ausschließlich im Apps Script, nie im Browser.

---

## 1. Supabase vorbereiten

1. Projekt auf [supabase.com](https://supabase.com) anlegen.
2. Im **SQL-Editor** die Datei `supabase/schema.sql` ausführen.
   Sie legt die Tabelle `kontaktanfragen` an, schaltet Row Level Security ein
   und entzieht `anon` sämtliche Rechte – die Anfragen sind damit über die
   öffentliche API nicht lesbar.
3. Unter **Project Settings → API** notieren:
   - `Project URL` (z. B. `https://abcdefgh.supabase.co`)
   - `service_role`-Schlüssel (geheim halten, niemals ins Repository)

## 2. Apps Script einrichten

1. [script.google.com](https://script.google.com) öffnen → **Neues Projekt**.
2. Den Inhalt von `apps-script/Code.gs` in die Datei `Code.gs` einfügen.
3. Über **Projekteinstellungen → „appsscript.json"-Manifestdatei anzeigen** die
   Datei `appsscript.json` durch die Fassung aus diesem Ordner ersetzen.
4. Unter **Projekteinstellungen → Skripteigenschaften** anlegen:

   | Eigenschaft | Wert |
   |---|---|
   | `SUPABASE_URL` | Project URL aus Schritt 1 |
   | `SUPABASE_SERVICE_KEY` | service_role-Schlüssel |
   | `SUPABASE_TABELLE` | `kontaktanfragen` (optional) |
   | `BENACHRICHTIGUNG_AN` | `info@alkawakibi.org` |

5. Funktion `selbsttest` einmal ausführen und die Berechtigungen bestätigen.
   Danach steht in Supabase ein Testeintrag – anschließend löschen.
6. **Bereitstellen → Neue Bereitstellung → Web-App**
   - Ausführen als: *Ich*
   - Zugriff: *Jeder*
   - Die angezeigte URL (`https://script.google.com/macros/s/…/exec`) kopieren.

> Nach jeder Änderung am Code muss **eine neue Bereitstellung** erstellt oder
> die bestehende aktualisiert werden, sonst bleibt die alte Fassung aktiv.

## 3. Website verbinden

In `assets/js/konfiguration.js` die URL eintragen:

```js
window.ALKAWAKIBI_KONFIGURATION = {
  formularEndpunkt: 'https://script.google.com/macros/s/.../exec',
  ersatzEmail: 'info@alkawakibi.org'
};
```

Solange `formularEndpunkt` leer bleibt, zeigt das Formular einen Hinweis und
bietet den Versand per E-Mail-Programm an. Die Seite funktioniert also auch
ohne eingerichtetes Backend.

## 4. Datenformat

Die Website sendet `POST` mit `Content-Type: text/plain;charset=utf-8`
(vermeidet den CORS-Preflight, den Apps Script nicht beantwortet) und diesem
JSON-Körper:

```json
{
  "name": "Beispielname",
  "email": "name@example.org",
  "telefon": "",
  "betreff": "Mitgliedschaft",
  "nachricht": "…",
  "einwilligung": true,
  "website": "",
  "quelle": "kontakt.html",
  "userAgent": "…"
}
```

Antwort bei Erfolg: `{"ok":true}`.
Antwort bei fehlerhaften Feldern: `{"ok":false,"fehler":["email"]}`.

`website` ist der Honigtopf: Bots füllen ihn aus, echte Besucherinnen und
Besucher sehen ihn nicht. Ist er gefüllt, wird die Nachricht stillschweigend
verworfen.

## 5. Nachrichten ansehen

In Supabase unter **Table Editor → kontaktanfragen**. Das Feld `status` kann
auf `in_bearbeitung`, `erledigt` oder `spam` gesetzt werden.

## 6. Vor dem Livegang prüfen

- [ ] Testnachricht über das echte Formular gesendet und in Supabase angekommen
- [ ] Benachrichtigungs-E-Mail kommt an (auch den Spam-Ordner prüfen)
- [ ] `service_role`-Schlüssel steht nirgends im Repository
- [ ] Datenschutzerklärung nennt Google Apps Script und Supabase
- [ ] Löschfrist für alte Anfragen festgelegt
