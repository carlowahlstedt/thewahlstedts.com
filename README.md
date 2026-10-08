# thewahlstedts.com

Landing page for [thewahlstedts.com](https://thewahlstedts.com), linking to:

- [carlo.thewahlstedts.com](https://carlo.thewahlstedts.com) — Carlo's site ([carlowahlstedt.github.io](https://github.com/carlowahlstedt/carlowahlstedt.github.io))
- [amanda.thewahlstedts.com](https://amanda.thewahlstedts.com) — Amanda's site
- [edub-is-cool.github.io/games](https://edub-is-cool.github.io/games/) — Ephraim's site

Static HTML served by GitHub Pages. `404.html` forwards any old blog URL (e.g. `thewahlstedts.com/2020-01-01-some-post/`) to the same path on `carlo.thewahlstedts.com`.

## Your card: `wahlstedt.json`

Each person's card on the portal comes from a `wahlstedt.json` file at the root of their own site (e.g. `https://carlo.thewahlstedts.com/wahlstedt.json`). Change the file on your site and the portal picks it up — no change to this repo needed.

```json
{
  "name": "Carlo",
  "tagline": "Code, coffee, and the occasional blog post.",
  "color": "#00a5ff",
  "avatar": "img/avatar-icon.jpg",
  "url": "/"
}
```

Every field is optional:

| Field     | What it does                                                          |
|-----------|-----------------------------------------------------------------------|
| `name`    | Heading on the card.                                                  |
| `tagline` | Short line under the name. Plain text.                                |
| `color`   | Accent color for the card's top border (any CSS color).               |
| `avatar`  | Round image above the name. Relative to your site, or a full URL.     |
| `url`     | Where the card links. Relative to your site, or a full URL. Defaults to your site's home page. |

Any host works, no CORS setup needed: a GitHub Action (`.github/workflows/fetch-cards.yml`) fetches every site's `wahlstedt.json` hourly and commits the result to `cards.json`, which the portal reads from its own origin. If your site also allows cross-origin requests (GitHub Pages does), the portal fetches your file live too, so edits show up immediately instead of within the hour. To refresh the cache right away, run the "Fetch cards" workflow from the Actions tab.

If your file is missing or can't be read, your card uses the last cached copy, or the name and color in `sites.json`.

### Adding a new Wahlstedt

Add an entry to `sites.json` with the site's base URL (ending in `/`) and a fallback name and color. Pushing the change runs the fetch workflow.
