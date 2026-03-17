# CS Keywords Data

The keyword data behind **[keywords.ictsoeasy.co.uk](https://keywords.ictsoeasy.co.uk)** — a free, searchable reference of Computer Science vocabulary for students aged 8–18, available in multiple languages.

## What this repo is

This repository holds a single file — `keywords.json` — containing all the keyword definitions shown on the website. Anyone can suggest new keywords, fix definitions, or add translations by submitting a pull request. When a PR is merged into `main`, the website updates automatically.

## How to contribute

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for full details.

The short version:
1. Fork this repo
2. Edit `keywords.json`
3. Open a pull request
4. Once merged, your changes go live on the site

## Current topics

| Topic | ID |
|---|---|
| ⚙️ Algorithms | `algorithms` |
| 💻 Programming | `programming` |
| 🌐 Networking | `networking` |
| 🗄️ Data & Databases | `data` |
| 🔒 Security | `security` |

## Current languages

| Language | Code |
|---|---|
| English | `en` |
| Polski | `pl` |

Want to add a new language? See [Adding a new language](CONTRIBUTING.md#adding-a-new-language).

## Data format

All data lives in `keywords.json`. The top-level structure is:

```json
{
  "meta": { ... },
  "ui": { ... },
  "topics": [ ... ],
  "keywords": [ ... ]
}
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for field-by-field documentation.

## License

Content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and share with attribution.
