# Vendored third-party scripts

Populated in Phase 4. Will contain:

- `marked.min.js` — markdown parser, loaded with Subresource Integrity (SRI) hash
- `dompurify.min.js` — HTML sanitizer, loaded with SRI hash

Both are vendored locally rather than loaded from a CDN so we:

1. Avoid third-party CDN dependencies at runtime (privacy + reliability)
2. Can pin and verify exact versions
3. Can apply a strict Content Security Policy that disallows external scripts

Update procedure (post-launch): download new version, compute SRI hash with `openssl dgst -sha384 -binary file.js | openssl base64 -A`, update the `integrity=` attribute in `library.html`, commit.
