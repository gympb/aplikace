/* Service worker katalogu gymplikace. Slouží k instalaci jako aplikace a k otevření katalogu bez sítě.
   Nic neodesílá a nic nesleduje. Aplikace ve složkách (např. /caesarova-sifra/) a portfolio se nezachytávají,
   načítají se vždy ze sítě. Při změně souborů v SEZNAM zvyš VERZE. */
const VERZE = 'gymplikace-1';
const SEZNAM = ['./', 'index.html', 'katalog.json', 'manifest.webmanifest', 'favicon.svg',
  'assets/ikona/ikona-192.png', 'assets/ikona/ikona-512.png', 'assets/obrazky/skola.svg', 'assets/obrazky/predmety/zaloha.svg'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERZE).then(c => c.addAll(SEZNAM)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(k => Promise.all(k.filter(n => n !== VERZE).map(n => caches.delete(n)))).then(() => self.clients.claim()));
});

const sit = async (req, pouzitCache) => {
  const c = await caches.open(VERZE);
  try {
    const r = await fetch(req);
    if (r.ok) c.put(req, r.clone());
    return r;
  } catch (err) {
    const z = await c.match(req, { ignoreSearch: true });
    if (z) return z;
    throw err;
  }
};
const cacheNejdriv = async req => {                       /* písma a ilustrace: z cache, na pozadí obnovit */
  const c = await caches.open(VERZE), z = await c.match(req);
  const nove = fetch(req).then(r => { if (r.ok) c.put(req, r.clone()); return r; }).catch(() => z);
  return z || nove;
};

self.addEventListener('fetch', e => {
  const req = e.request, u = new URL(req.url);
  if (req.method !== 'GET' || u.origin !== location.origin) return;
  const cesta = u.pathname.replace(/^\/+/, '');
  const koren = cesta === '' || cesta === 'index.html';
  if (req.mode === 'navigate' && !koren) return;           /* podstránky a aplikace vyřizuje prohlížeč sám */
  if (koren || cesta === 'katalog.json' || cesta === 'manifest.webmanifest') e.respondWith(sit(koren ? new Request('index.html') : req));
  else if (cesta.startsWith('assets/')) e.respondWith(cacheNejdriv(req));
});
