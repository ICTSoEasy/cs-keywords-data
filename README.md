# CS Keywords Data

The keyword data behind **[keywords.ictsoeasy.co.uk](https://keywords.ictsoeasy.co.uk)** — a free, searchable reference of Computer Science vocabulary for students aged 8–18, available in multiple languages.

## What this repo is

This repository holds all the keyword definitions shown on the website. Anyone can suggest new keywords, fix definitions, or add translations by submitting a pull request. When a PR is merged into `main`, the website updates automatically.

## How to contribute

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for full details.

The short version:
1. Fork this repo
2. Make your change (add or edit a file in `keywords/`, or edit `topics.json` / `ui.json`)
3. Open a pull request
4. Once merged, a bot rebuilds the site data automatically — your changes go live shortly after

> **No need to touch `dist/bundle.json`** — that file is generated automatically. Never edit it by hand.

## Repository structure

```
keywords/          ← one JSON file per keyword (e.g. algorithm.json)
topics.json        ← list of all topics with icons and translated labels
ui.json            ← UI strings (page titles, button labels) and language list
dist/bundle.json   ← auto-generated — do not edit directly
scripts/bundle.py  ← the script that builds dist/bundle.json (runs via GitHub Actions)
```

## Current languages

| Language | Code |
|---|---|
| English | `en` |
| Polski | `pl` |
| Cymraeg | `cy` |
| العربية | `ar` |
| Română | `ro` |

Want to add a new language? See [Adding a new language](CONTRIBUTING.md#5-add-a-new-language).

## Current topics

| Icon | Topic | ID |
|---|---|---|
| ⚙️ | Algorithms | `algorithms` |
| 💻 | Programming | `programming` |
| 🧠 | Computational Thinking | `computational_thinking` |
| 🔢 | Data Representation | `data_representation` |
| 🖥️ | Hardware & Computer Systems | `hardware` |
| 📦 | Software | `software` |
| 🌐 | Networking | `networking` |
| 🗄️ | Data & Databases | `data` |
| 🔒 | Security & Cybersecurity | `security` |
| ⊻ | Boolean Logic | `logic` |
| 🛠️ | Software Development | `software_development` |
| 🌳 | Data Structures | `data_structures` |
| 📐 | Theory of Computation | `theory` |
| ⚖️ | Ethical & Legal Issues | `ethics` |
| 🤖 | Artificial Intelligence | `ai` |
| 🦾 | Robotics & Physical Computing | `robotics` |

## License

Content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use and share with attribution.
