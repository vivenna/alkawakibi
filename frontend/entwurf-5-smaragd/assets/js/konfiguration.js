/* Einstellungen der Website.
 *
 * formularEndpunkt: Adresse der Google-Apps-Script-Webanwendung, die die
 * Nachrichten des Kontaktformulars entgegennimmt und nach Supabase schreibt.
 * Einrichtung: siehe backend/README.md im Projektordner.
 *
 * Solange der Eintrag leer ist, bietet das Formular den Versand über das
 * E-Mail-Programm an. Die Seite funktioniert also auch ohne Backend.
 */
window.ALKAWAKIBI_KONFIGURATION = {
  formularEndpunkt: '',
  ersatzEmail: 'info@alkawakibi.org'
};

/* Beim örtlichen Ausprobieren wird der mitgelieferte Testserver benutzt
 * (backend/lokal/testserver.py). Auf der echten Domain greift das nie. */
if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') {
  window.ALKAWAKIBI_KONFIGURATION.formularEndpunkt = 'http://localhost:8090/formular';
}
