#!/usr/bin/env python3
"""Baut die Website aus src/ (nur Python-Standardbibliothek).

  python3 build.py            -> Live-Version fuer die echte Domain (indexierbar)
  python3 build.py --preview  -> Vorschau (GitHub Pages), fuer Google gesperrt

Texte aendern: src/content.json (je Eintrag "en" und "de").
Aufbau und Design aendern: src/template.html.
Danach immer neu bauen. Erzeugt: index.html, de/index.html, 404.html,
robots.txt, sitemap.xml, site.webmanifest.
"""
import json, os, re, sys, html, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = json.load(open(os.path.join(ROOT, 'src', 'site.json'), encoding='utf-8'))
PREVIEW = '--preview' in sys.argv
BASE = SITE['preview_url'] if PREVIEW else SITE['live_url']
if not BASE.endswith('/'):
    BASE += '/'
CONTENT = json.load(open(os.path.join(ROOT, 'src', 'content.json'), encoding='utf-8'))
TEMPLATE = open(os.path.join(ROOT, 'src', 'template.html'), encoding='utf-8').read()
TODAY = datetime.date.today().isoformat()

URL = {'en': BASE, 'de': BASE + 'de/'}
GEO_COUNTRIES_TZ = ['Europe/Berlin', 'Europe/Busingen', 'Europe/Vienna', 'Europe/Zurich', 'Europe/Vaduz']


def t(key, lang):
    v = CONTENT[key][lang]
    return v


def text_value(key, lang):
    v = t(key, lang)
    # Werte ohne HTML werden fuer Attribute sicher gemacht
    return v if '<' in v else v.replace('"', '&quot;')


def jsonld(lang):
    biz = {
        '@type': 'ProfessionalService',
        '@id': BASE + '#business',
        'name': 'Fränze Lüttich',
        'alternateName': 'Fränze Lüttich Animal Talent Agency' if lang == 'en' else 'Fränze Lüttich Filmtieragentur',
        'url': URL[lang],
        'description': t('meta.business_desc', lang),
        'image': BASE + 'img/og-image.jpg',
        'logo': BASE + 'icon-512.png',
        'email': SITE['email'],
        'areaServed': [{'@type': 'Country', 'name': 'Germany'}, {'@type': 'Country', 'name': 'Austria'},
                       {'@type': 'Country', 'name': 'Switzerland'}, {'@type': 'Place', 'name': 'Worldwide'}],
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Hamburg', 'addressCountry': 'DE'},
        'knowsLanguage': ['en', 'de', 'fr'],
        'knowsAbout': ['Animal training for film', 'Film animals', 'Animal wrangling', 'Animal reference for VFX',
                       'Tiertraining für Film', 'Filmtiere'],
        'founder': {'@id': BASE + '#fraenze'},
        'sameAs': SITE['same_as'],
    }
    if SITE.get('phone'):
        biz['telephone'] = SITE['phone']
    person = {
        '@type': 'Person',
        '@id': BASE + '#fraenze',
        'name': 'Fränze Lüttich',
        'jobTitle': t('meta.job_title', lang),
        'image': BASE + 'img/fraenze-luettich-portrait-raccoon-1000.webp',
        'worksFor': {'@id': BASE + '#business'},
        'url': URL[lang],
        'sameAs': SITE['same_as'],
    }
    site = {
        '@type': 'WebSite',
        '@id': BASE + '#website',
        'name': 'Fränze Lüttich',
        'url': BASE,
        'inLanguage': ['en', 'de'],
        'publisher': {'@id': BASE + '#business'},
    }
    page = {
        '@type': 'WebPage',
        '@id': URL[lang] + '#webpage',
        'url': URL[lang],
        'name': t('meta.title', lang),
        'description': t('meta.description', lang),
        'inLanguage': lang,
        'isPartOf': {'@id': BASE + '#website'},
        'about': {'@id': BASE + '#business'},
        'primaryImageOfPage': BASE + 'img/og-image.jpg',
        'dateModified': TODAY,
    }
    data = {'@context': 'https://schema.org', '@graph': [site, page, biz, person]}
    return json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')


def geo_js(lang):
    if lang != 'en':
        return ''
    # Nur fuer Besuch auf der englischen Startseite: Zeitzone DE/AT/CH/LI -> deutsche Seite.
    # Kein Redirect fuer Bots und nie, wenn jemand die Sprache selbst gewaehlt hat.
    tz = json.dumps(GEO_COUNTRIES_TZ)
    return ("(function(){try{var s=localStorage.getItem('fl-lang')||(document.cookie.match(/(?:^|; )fl-lang=(\\w+)/)||[])[1];"
            "if(s||/bot|crawl|spider|slurp|lighthouse|headless|preview/i.test(navigator.userAgent))return;"
            "var z=Intl.DateTimeFormat().resolvedOptions().timeZone;"
            "if(" + tz + ".indexOf(z)>-1)location.replace('de/'+location.hash);}catch(e){}})();")


def render(lang, root, page_url):
    other = 'de' if lang == 'en' else 'en'
    vals = {
        'lang': lang,
        'root': root,
        'base': BASE,
        'url': page_url,
        'url_en': URL['en'],
        'url_de': URL['de'],
        'home': root or './',
        'href_en': (root or './') if lang == 'de' else './',
        'href_de': 'de/' if lang == 'en' else './',
        'cur_en': ' aria-current="page"' if lang == 'en' else '',
        'cur_de': ' aria-current="page"' if lang == 'de' else '',
        'og_locale': 'en_GB' if lang == 'en' else 'de_DE',
        'og_locale_alt': 'de_DE' if lang == 'en' else 'en_GB',
        'robots_meta': '<meta name="robots" content="noindex, nofollow">\n' if PREVIEW else '',
        'geo_js': geo_js(lang),
        'jsonld': jsonld(lang),
        'email': SITE['email'],
        'phone_block': ('          <div class="line-item"><div class="k">' + t('contact.phone_and_whatsapp', lang) + '</div><div class="v"><a href="tel:' + SITE['phone'].replace(' ', '') + '">' + SITE['phone'] + '</a></div></div>\n') if SITE.get('phone') else '',
        'og_image': BASE + ('img/og-image-de.jpg' if lang == 'de' else 'img/og-image.jpg'),
    }
    if lang == 'de':
        vals['href_en'] = '../'

    def sub(m):
        k = m.group(1)
        if k in vals:
            return vals[k]
        if k in CONTENT:
            return text_value(k, lang)
        raise KeyError('Unbekannter Platzhalter: {{%s}}' % k)
    out = re.sub(r'\{\{([a-zA-Z0-9_.]+)\}\}', sub, TEMPLATE)
    return out


def page_404():
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 | Fränze Lüttich</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>body{{margin:0;min-height:100vh;display:grid;place-items:center;background:#0f1615;color:#ece6dc;font:17px/1.5 Helvetica,Arial,sans-serif;text-align:center;padding:24px}}a{{color:#d9683a}}h1{{font-size:56px;margin:0 0 8px}}</style>
</head><body><main><h1>404</h1>
<p>{t('404.title','en')}. <a href="{BASE}">{t('404.text','en')}</a></p>
<p lang="de">{t('404.title','de')}. <a href="{URL['de']}">{t('404.text','de')}</a></p></main></body></html>
'''


def sitemap():
    alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{u}"/>' for h, u in
                   [('en', URL['en']), ('de', URL['de']), ('x-default', URL['en'])])
    urls = ''.join(f'<url><loc>{URL[l]}</loc><lastmod>{TODAY}</lastmod>{alts}</url>' for l in ('en', 'de'))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
            + urls + '</urlset>\n')


def robots():
    if PREVIEW:
        return 'User-agent: *\nDisallow: /\n'
    return f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n'


def manifest():
    return json.dumps({'name': 'Fränze Lüttich', 'short_name': 'Fränze Lüttich', 'start_url': './',
                       'display': 'browser', 'background_color': '#0f1615', 'theme_color': '#0f1615',
                       'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
                                 {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'}]},
                      ensure_ascii=False, indent=1)


def impressum():
    tpl = open(os.path.join(ROOT, 'src', 'impressum.html'), encoding='utf-8').read()
    d = datetime.date.today()
    monate = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
    vals = {'root': '../', 'base': BASE, 'email': SITE['email'], 'year': str(d.year),
            'today_de': f'{monate[d.month - 1]} {d.year}'}
    out = re.sub(r'\{\{([a-z_]+)\}\}', lambda m: vals[m.group(1)], tpl)
    if 'class="todo"' in out:
        print('Achtung: Im Impressum sind noch Platzhalter offen (orange markiert). Vor dem Livegang ausfüllen!')
    return out


def write(rel, text):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(text)


if __name__ == '__main__':
    missing = [k for k, v in CONTENT.items() if not v.get('en') or not v.get('de')]
    if missing:
        print('Achtung, Text fehlt in einer Sprache:', ', '.join(missing))
    write('index.html', render('en', '', URL['en']))
    write('de/index.html', render('de', '../', URL['de']))
    write('404.html', page_404())
    write('sitemap.xml', sitemap())
    write('robots.txt', robots())
    write('site.webmanifest', manifest())
    write('impressum/index.html', impressum())
    print('Fertig:', 'VORSCHAU (noindex)' if PREVIEW else 'LIVE', BASE)
