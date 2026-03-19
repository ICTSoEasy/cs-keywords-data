# Contributing to CS Keywords

Thank you for helping make CS vocabulary more accessible! Contributions of all sizes are welcome — fixing a typo, improving a definition, adding a new keyword, or translating into a new language.

---

## Before you start

A few principles that keep the site useful for its audience (students aged 8–18, including many EAL learners):

- **Plain language.** Write definitions as if explaining to a smart 12-year-old. Avoid defining a word using harder words.
- **Short and clear.** One or two sentences is ideal. Aim for under 30 words per definition.
- **No jargon in the definition itself** unless the jargon is also defined elsewhere in the list.
- **Consistent tone.** Friendly and informative, not textbook-dry.

---

## How the repo works

Each keyword lives in its own file inside the `keywords/` folder (e.g. `keywords/algorithm.json`). There are also two shared files: `topics.json` (the list of topics) and `ui.json` (translated UI labels and the language list).

When a pull request is merged into `main`, a GitHub Actions bot automatically combines everything into `dist/bundle.json`, which the website then fetches. **You never need to edit `dist/bundle.json` yourself.**

---

## Ways to contribute

### 1. Fix a typo or improve a definition

If you just want to fix a small mistake, you don't need to clone anything.

1. Browse to the relevant file in `keywords/` on GitHub
2. Click the **pencil icon** (✏️) in the top-right of the file view
3. Make your change
4. Scroll down and click **"Propose changes"**
5. Click **"Create pull request"**

That's it — GitHub handles the fork automatically.

---

### 2. Add a new keyword

Each keyword is a separate JSON file in the `keywords/` folder. The filename should match the keyword's `id` (e.g. `keywords/bubble_sort.json`).

**Example file — `keywords/bubble_sort.json`:**

```json
{
  "id": "bubble_sort",
  "topics": ["algorithms"],
  "translations": {
    "en": {
      "term": "Bubble Sort",
      "definition": "A simple sorting method that repeatedly steps through a list, compares neighbouring items, and swaps them if they are in the wrong order."
    },
    "pl": {
      "term": "Sortowanie bąbelkowe",
      "definition": "Prosta metoda sortowania, która wielokrotnie przechodzi przez listę, porównuje sąsiednie elementy i zamienia je miejscami, jeśli są w złej kolejności."
    }
  }
}
```

**Field guide:**

| Field | Description |
|---|---|
| `id` | Unique identifier. Lowercase letters, numbers, and underscores only. Must match the filename (without `.json`). |
| `topics` | Array of topic IDs this keyword belongs to. Must match IDs in `topics.json`. A keyword can belong to more than one topic. |
| `translations` | One entry per language. You must include at least `en`. |
| `term` | The keyword as displayed on the site. |
| `definition` | Plain language, 1–2 sentences, suitable for ages 8–18. |

**Don't speak all the languages?** No problem — add the languages you know and note in your PR that others still need translating. Someone else can fill them in later.

**To submit:** fork the repo, create the new file, and open a pull request.

---

### 3. Add a translation for an existing keyword

Find the keyword's file in `keywords/` and add a new language key inside `translations`:

```json
"translations": {
  "en": { "term": "Algorithm", "definition": "..." },
  "pl": { "term": "Algorytm", "definition": "..." },
  "fr": { "term": "Algorithme", "definition": "..." }
}
```

The language code must already exist in `ui.json`. If you're adding a brand-new language, see below.

---

### 4. Add a new topic

Adding a topic means editing one file: `topics.json`.

Add a new entry to the array:

```json
{
  "id": "new_topic",
  "icon": "🔧",
  "labels": {
    "en": "New Topic",
    "pl": "Nowy temat",
    "cy": "Pwnc Newydd",
    "ar": "موضوع جديد",
    "ro": "Subiect nou"
  }
}
```

Add a `labels` entry for every language already listed in `ui.json`. Then add keywords with `"topics": ["new_topic"]` as normal.

---

### 5. Add a new language

Adding a language requires changes to two files.

**Step 1 — `ui.json`:** add the language to the `languages` array and add a full set of UI strings to `strings`:

```json
"languages": [
  ...,
  { "code": "fr", "label": "Français" }
],
"strings": {
  ...,
  "fr": {
    "site_title": "Mots-clés Info",
    "site_subtitle": "Vocabulaire informatique pour tous",
    "search_placeholder": "Rechercher des mots-clés…",
    "all_topics": "Tous les sujets",
    "no_results": "Aucun mot-clé trouvé. Essayez une autre recherche ou un autre sujet.",
    "no_translation": "Traduction pas encore disponible",
    "second_language": "Deuxième langue",
    "footer_text": "Données contribuées par la communauté.",
    "footer_contribute": "Suggérer des modifications sur GitHub"
  }
}
```

**Step 2 — `topics.json`:** add a `labels` entry for the new language in every topic.

**Step 3 (optional but welcome):** add `translations` for the new language to as many keyword files as you can.

---

## Topic IDs

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

---

## Pull request checklist

Before submitting, please check:

- [ ] Any new or edited `.json` files are valid JSON (paste into [jsonlint.com](https://jsonlint.com) if unsure)
- [ ] Every new keyword has at least an `en` translation
- [ ] The `id` matches the filename (without `.json`), uses only lowercase letters, numbers, and underscores, and is unique
- [ ] `topics` values match IDs in the topic list above
- [ ] Definitions are plain English, suitable for ages 8–18
- [ ] You have **not** edited `dist/bundle.json` — the bot does that automatically

---

## Questions?

Open an issue and we'll help you out.
