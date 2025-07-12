
// Algorithm Ecosystem Platform Service Worker
const CACHE_NAME = 'algorithm-ecosystem-v1';
const urlsToCache = [
    '/',
    '/shared/styles.css',
    '/shared/components.css',
    '/shared/animations.css',
    '/shared/accessibility.css',
    '/shared/utilities.css',
    '/shared/scripts.js'
];

self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
            .then(function(response) {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            })
    );
});
