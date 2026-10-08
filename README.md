# Website Fränze Lüttich

Die komplette Website für **fraenzeluettich.com**: englische Startseite unter `/`, deutsche Version unter `/de/`.
Statisches HTML ohne Baukasten, ohne Abo und ohne Datenbank. Hosting später kostenlos über Cloudflare Pages.

## Was liegt wo

| Ordner / Datei | Inhalt |
|---|---|
| `src/content.json` | **Alle Texte**, jeweils Englisch (`en`) und Deutsch (`de`), dazu Bildbeschreibungen (`img.…`) und Google-Titel/-Beschreibung (`meta.…`) |
| `src/template.html` | Aufbau und Design der Seite |
| `src/site.json` | Domain, E-Mail, Telefon, Social-Links |
| `build.py` | Baut aus `src/` die fertigen Seiten |
| `index.html`, `de/index.html` | Die fertigen Seiten (werden von `build.py` erzeugt, nicht von Hand ändern) |
| `img/` | Fotos (WebP, sprechende Dateinamen), `img/set/` = Set-Fotos |
| `video/` | Hero-Showreel (stumm, 1080p und 720p, je zwei Teile) und Showreel mit Ton |
| `fonts/` | Schrift Archivo, selbst gehostet (Open Font License) |
| `functions/_middleware.js` | Leitet Besuch aus DE/AT/CH beim ersten Aufruf auf Deutsch (nur auf Cloudflare aktiv) |
| `docs/` | SEO-Leitfaden, offene Punkte, Anleitung für den Umzug |

## Am einfachsten: mit Claude bearbeiten

Ordner in Claude (Claude Code oder Claude Desktop mit Ordnerzugriff) öffnen und sagen, was sich ändern soll, z. B.
„Füge beim Ensemble zwei Pferde hinzu, Foto liegt in Downloads/pferd.jpg“.
Claude kennt über `CLAUDE.md` alle Regeln dieses Projekts.

## Von Hand ändern

1. Text in `src/content.json` ändern (immer beide Sprachen).
2. Im Terminal im Projektordner: `python3 build.py`
3. Änderungen hochladen (GitHub Desktop: Commit, dann Push). Cloudflare veröffentlicht automatisch.

Vorschau-Version für GitHub Pages (für Google gesperrt): `python3 build.py --preview`

## Weiter lesen

- `docs/OFFEN.md` – was vor dem Livegang noch fehlt
- `docs/UMZUG.md` – GitHub, Cloudflare Pages, Domain umziehen
- `docs/SEO.md` – was für Google wichtig ist und was nach dem Start zu tun ist
