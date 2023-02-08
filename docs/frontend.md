# Frontend

The dashboard lives in `web/` and is built with Vite, React and TypeScript.

```
$ cd web
$ npm install
$ npm run dev
```

Vite proxies `/api` to `http://localhost:8000`, so start the API first.

## Structure

| Path | Purpose |
| --- | --- |
| `src/api` | Typed fetch wrapper and shared types |
| `src/hooks` | Data loading and timer state |
| `src/components` | Presentation only, no fetching |
| `src/pages` | One component per route |
| `src/lib` | Formatting helpers, unit tested with vitest |

Components never call `fetch` directly. That keeps the API boundary in one
place when the endpoints change.
