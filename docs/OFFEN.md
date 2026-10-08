# Offen vor dem Livegang

## Fränze muss bestätigen oder liefern
- [ ] **Telefon/WhatsApp**: bewusst nicht veröffentlicht. Falls gewünscht, in `src/site.json` bei `phone` eintragen, dann erscheint es automatisch im Kontaktbereich.
- [ ] **E-Mail**: derzeit animal_trainer@outlook.de. Später besser eine Domain-Adresse (z. B. hello@fraenzeluettich.com), dann nur in `src/site.json` ändern.
- [ ] **Versicherungssumme**: `[amount]` / `[Summe]` im Abschnitt „Shooting in Germany“.
- [ ] **Ensemble**: Stimmen Anzahl und Arten (2 Raben, 2 Füchse, 2 Weimaraner, 1 Dackel, Hühner)? Weitere Tiere ergänzen.
- [ ] **Tierkategorien im Mosaik**: Welche Tiere sind wirklich über das Netzwerk buchbar?
- [ ] **Credits** (Auswahl-Wolke): alle 25 Namen gegenlesen, v. a. Berlin Nobody, Schlafende Hunde, Habibi Baba Boom, Babylon Berlin (aus Crew United).
- [ ] **VFX/KI**: Gab es schon Jobs mit VFX-Anteil? Dann als Beispiel nennen.
- [ ] **American Humane**: Aussage „Familiar with No Animals Were Harmed monitoring“ nur, wenn zutreffend.
- [ ] **Impressum** (`src/impressum.html`, orange markierte Stellen; `build.py` warnt, solange etwas offen ist):
  - ladungsfähige Anschrift (Pflicht, kein Postfach). Bewusst keine Wohnadresse: Geschäftsadresse, Coworking oder Büroservice mit Postannahme nutzen.
  - Behörde, die die Erlaubnis nach § 11 TierSchG erteilt hat, mit Anschrift
  - Hinweis zum Formular-Dienst, sobald das Formular angeschlossen ist
  - Bewusst weggelassen: Telefon (Kontaktformular reicht als zweiter Kontaktweg), USt-IdNr., private Angaben
- [ ] Altes Impressum war unvollständig (keine Anschrift, kein Telefon), verwies noch auf die abgeschaltete EU-Streitschlichtungsplattform und auf Google Analytics. Ist im neuen behoben.
- [ ] **Kontaktformular**: ist noch nicht verbunden. Vorschlag: Cloudflare Pages Function mit E-Mail-Versand oder Formspree.
- [ ] **Bildrechte**: Fotograf*innen der Set-Fotos und Shootings klären, ggf. Credit ergänzen. Showreel-Ausschnitte stammen aus Produktionen, Nutzung als Referenz mit den Produktionen abstimmen. Neu: Set-Foto Taube auf Schwert (`white-dove-sword-painted-sky-900.webp`): Zustimmung der abgebildeten Person und Fotograf*in fehlt noch.
- [ ] **Instagram/Crew United/IMDb**: Links in `src/site.json` prüfen, IMDb-Profil ergänzen, falls vorhanden.
