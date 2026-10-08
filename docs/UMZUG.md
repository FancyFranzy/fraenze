# Umzug: GitHub, Cloudflare Pages, Domain

## 1. GitHub
Repository mit diesem Ordner (aktuell `kilianamrehn/fraenze`, kann an Fränzes Account übertragen werden: Settings > Transfer).

## 2. Cloudflare Pages
1. Kostenloses Konto auf cloudflare.com anlegen.
2. Workers & Pages > Create > Pages > Connect to Git > Repository wählen.
3. Build-Einstellungen: Framework „None“, Build command `python3 build.py`, Output directory `/` (leer lassen bzw. Root).
4. Deploy. Die Seite läuft dann unter `…pages.dev`.
5. Der Ordner `functions/` wird automatisch erkannt (Sprachweiche DE/AT/CH).

## 3. Domain fraenzeluettich.com
1. In Cloudflare: Add a domain > fraenzeluettich.com, Free-Plan. Cloudflare zeigt zwei Nameserver.
2. Beim bisherigen Domain-Anbieter (Squarespace Domains) die Nameserver auf die von Cloudflare umstellen.
3. Im Pages-Projekt: Custom domains > `www.fraenzeluettich.com` und `fraenzeluettich.com` hinzufügen.
4. Bevorzugt ist `https://www.fraenzeluettich.com/` (so steht es in `src/site.json`). Die Variante ohne www per Redirect Rule (301) auf www leiten.
5. E-Mail: Falls über die Domain Mails laufen (MX-Einträge), diese vor dem Umstellen in Cloudflare übernehmen.
6. Squarespace-Abo erst kündigen, wenn die neue Seite live ist.

## 4. Alte Adressen
Die alte Seite hatte `/portfolio`, `/behind-the-scenes`, `/about`. In Cloudflare eine Datei `_redirects` anlegen:
```
/portfolio          /#work         301
/behind-the-scenes  /#bts          301
/about              /#about        301
```
