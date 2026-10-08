# SEO-Leitfaden (Stand Oktober 2026)

## Was schon eingebaut ist
- **Zwei echte Sprachseiten** (`/` Englisch, `/de/` Deutsch) statt Umschalten per Skript. Google sieht beide Versionen.
- **hreflang** en, de, x-default auf beiden Seiten und in der Sitemap, Canonical je Sprache auf sich selbst.
- **Sprachweiche** für DE/AT/CH nur beim ersten Besuch, nie für Suchmaschinen, manuelle Wahl hat Vorrang. Google rät generell von automatischen Weiterleitungen ab. Weil Googlebot ausgenommen ist und beide Seiten verlinkt sind, bleibt das Risiko gering.
- **Titel und Beschreibung** je Sprache mit den wichtigsten Suchbegriffen (animal trainer, film animals, Germany / Filmtiere, Tiertrainerin, Deutschland).
- **Strukturierte Daten** (JSON-LD): WebSite, WebPage, ProfessionalService (Tieragentur), Person (Fränze). Keine FAQ-Daten: Google zeigt seit Mai 2026 keine FAQ-Ergebnisse mehr.
- **Bilder**: WebP, sprechende Dateinamen, Alt-Texte in beiden Sprachen, Breite/Höhe gesetzt, Lazy Loading unterhalb des sichtbaren Bereichs, mehrere Größen für Handy/Desktop.
- **Ladezeit** (Core Web Vitals: LCP unter 2,5 s, INP unter 200 ms, CLS unter 0,1): Hero-Poster wird zuerst geladen, Video erst danach, Handys bekommen 720p, Schrift selbst gehostet (auch DSGVO), Caching über `_headers`.
- **Open Graph** (Vorschaubild 1200×630 für WhatsApp, LinkedIn, Mail), Favicon in allen Größen, `robots.txt`, `sitemap.xml`, 404-Seite.

## Nach dem Livegang (in dieser Reihenfolge)
1. **Google Search Console**: Domain-Property per DNS-Eintrag in Cloudflare bestätigen, `https://www.fraenzeluettich.com/sitemap.xml` einreichen.
2. **Bing Webmaster Tools**: aus der Search Console importieren (Bing speist auch ChatGPT-Suche).
3. **Crew United**: Website-Link eintragen, Credits aktuell halten. Wichtigster Branchen-Link.
4. **IMDb**: Credits nachtragen lassen, Website verlinken.
5. **Film Commissions / Location Guides**: Hamburg Film Commission (MOIN), Medienboard Berlin-Brandenburg, FFF Bayern, Film- und Medienstiftung NRW, The Location Guide, Screen Global Production. Dort als Dienstleisterin listen lassen.
6. **Google Business Profile** als Gebiets-Unternehmen ohne Adresse (Hamburg, ganz Deutschland). Name, Mail, Telefon exakt wie auf der Website.
7. **Instagram-Bio** auf die neue Domain verlinken.

## Später (lohnt sich, wenn Zeit ist)
1. Eigene Seite **„Animal reference for VFX & AI“** (kaum Konkurrenz, eigenes Suchthema).
2. Eigene Seite **„Filming with animals in Germany“** für internationale Produktionen (Genehmigungen, Ablauf, Transport).
3. **Showreel-Seite** mit dem Video als Hauptinhalt und VideoObject-Daten. Nur so erscheint das Video in der Google-Videosuche.
4. **Credits-Seite** mit allen Produktionen und Links zu IMDb.
5. Einzelne Tierseiten nur, wenn es echten eigenen Inhalt gibt (keine dünnen Seiten).
6. Zitate von Produktionen (echte Namen, mit Erlaubnis) als Vertrauenssignal.

## Was nichts bringt
- `meta keywords`, FAQ-Schema, eigene Bewertungssterne, „KI-optimierte“ Plugins.
- `llms.txt`: wird laut Logdaten von KI-Suchen praktisch nicht abgerufen. Für KI-Antworten gilt dasselbe wie für Google: klare, sachliche Texte und konsistente Einträge (Crew United, IMDb, Instagram).

## Quellen
- Google: Mehrsprachige Websites https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites
- Google: Sprachabhängige Seiten und Redirects https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages
- Google: KI-Funktionen in der Suche https://developers.google.com/search/docs/appearance/ai-features
- Ende der FAQ-Ergebnisse 2026 https://ppc.land/google-kills-faq-rich-results-what-seos-saw-coming-since-2019/
- llms.txt-Nutzung https://ppc.land/llms-txt-adoption-rises-8-8x-but-97-of-files-get-zero-ai-requests/
