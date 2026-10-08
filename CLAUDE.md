# CLAUDE.md – Website Fränze Lüttich

Statische, zweisprachige Website (EN unter `/`, DE unter `/de/`) für die Tiertrainerin und Tieragentur Fränze Lüttich.
Die Person, die hier mit dir arbeitet, ist keine Entwicklerin. Erkläre, was eine Änderung bewirkt, nicht wie der Code aussieht.
Antworten an Fränze: kurz, in Stichpunkten, nur das Wichtigste. Keine langen Erklärungen.

## Arbeitsweise

- Texte nur in `src/content.json` ändern, immer `en` **und** `de`. Neue Texte bekommen einen neuen Schlüssel und im Template `{{schluessel}}`.
- Aufbau/Design in `src/template.html`. Pfade zu Dateien immer mit `{{root}}` beginnen (`{{root}}img/…`), sonst bricht die deutsche Seite.
- Nach jeder Änderung bauen. Solange die Seite nur auf GitHub Pages läuft (kilianamrehn.github.io/fraenze oder unter Fränzes GitHub-Namen): `python3 build.py --preview` (für Google gesperrt). Sobald die echte Domain auf Cloudflare läuft: `python3 build.py`.
- Danach die Änderungen committen und auf `main` pushen. GitHub Pages bzw. Cloudflare veröffentlichen automatisch nach 1 bis 2 Minuten. Fränze bekommt am Ende immer kurz gesagt, was sich geändert hat und den Link zum Anschauen.
- `index.html`, `de/index.html`, `404.html`, `sitemap.xml`, `robots.txt`, `site.webmanifest` sind generiert. Nie direkt bearbeiten.
- Vor dem Abschluss beide Seiten im Browser prüfen (Handy- und Desktop-Breite).

## Sprache und Ton

- Englisch ist die Hauptsprache (internationale Produktionen), Deutsch gleichwertig.
- Deutsch: Ansprache mit „ihr“ (Filmteams). Gendern: wo möglich neutral formulieren, sonst Gendersternchen (Tierhalter*innen, Trainer*innen). Fränze selbst: „Tiertrainerin“.
- Keine Gedankenstriche (—) in Texten. Kurz, klar, konkret.
- Keine erfundenen Credits, Tiere oder Zahlen. Nur, was Fränze bestätigt hat.

## Bilder

- Format WebP, sprechender Dateiname auf Englisch mit Bindestrichen (`weimaraner-cinema-camera-900.webp`), Breite im Namen.
- Große Bilder in zwei Breiten (700 und 1400, Set-Fotos 900) mit `srcset`/`sizes`, immer `width`/`height`, `loading="lazy"` und `decoding="async"`.
- Jedes inhaltliche Bild bekommt einen Alt-Text in beiden Sprachen in `src/content.json` (Schlüssel `img.…`): sachlich beschreiben, was zu sehen ist, Tierart nennen, kein Keyword-Stapeln. Rein dekorative Duplikate: `alt=""`.
- Python mit Pillow zum Umwandeln: `Image.open(...).save('x.webp', 'WEBP', quality=80, method=6)`.

## SEO-Regeln (Details in docs/SEO.md)

- Eine `h1` pro Seite. Titel ca. 50–60 Zeichen, Beschreibung ca. 140–160 Zeichen (`meta.title`, `meta.description`).
- hreflang en/de/x-default, Canonical und Sitemap erzeugt `build.py` automatisch aus `src/site.json`.
- Strukturierte Daten (JSON-LD) entstehen in `build.py` (`jsonld()`); nur sichtbare, wahre Angaben eintragen, keine Bewertungssterne.
- Das Hero-Poster ist das LCP-Element: nie lazy laden, `fetchpriority="high"` behalten.

## Sprachweiche

- Cloudflare: `functions/_middleware.js` leitet Erstbesuch aus DE/AT/CH/LI von `/` auf `/de/` (nicht für Bots, nicht wenn Cookie `fl-lang` gesetzt).
- Fallback im Browser (z. B. GitHub Pages): Skript im `<head>` der englischen Seite nach Zeitzone.
- Manuelle Sprachwahl über die EN/DE-Links wird gespeichert und hat immer Vorrang.
