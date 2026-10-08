// Cloudflare Pages: Besuch aus Deutschland, Österreich, Schweiz oder Liechtenstein
// landet beim ersten Aufruf der Startseite auf /de/. Alle anderen Länder sehen Englisch.
// Kein Redirect für Suchmaschinen und nie, wenn jemand die Sprache selbst gewählt hat (Cookie fl-lang).
const DE_COUNTRIES = ['DE', 'AT', 'CH', 'LI'];
const BOT = /bot|crawl|spider|slurp|facebookexternalhit|embedly|lighthouse|headless|preview/i;

export async function onRequest(context) {
  const { request, next } = context;
  const url = new URL(request.url);
  if (url.pathname === '/' && request.method === 'GET') {
    const cookie = request.headers.get('Cookie') || '';
    const chosen = /(?:^|;\s*)fl-lang=/.test(cookie);
    const ua = request.headers.get('User-Agent') || '';
    const country = request.cf && request.cf.country;
    if (!chosen && !BOT.test(ua) && DE_COUNTRIES.includes(country)) {
      return new Response(null, { status: 302, headers: { Location: '/de/', 'Cache-Control': 'private, no-store', Vary: 'Cookie' } });
    }
  }
  return next();
}
