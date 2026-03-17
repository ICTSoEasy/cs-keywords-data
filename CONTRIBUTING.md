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

## Ways to contribute

### 1. Fix a typo or improve a definition

1. Fork this repository
2. Edit `keywords.json` directly on GitHub (click the pencil icon) or clone it locally
3. Make your change
4. Open a pull request with a brief description of what you changed and why

### 2. Add a new keyword

Find the `keywords` array in `keywords.json` and add a new entry using this structure:

```json
{
  "id": "your-keyword-id",
  "topic": "algorithms",
  "translations": {
    "en": {
      "term": "Your Keyword",
      "definition": "A clear, plain-English definition suitable for ages 8–18."
    },
    "pl": {
      "term": "Twoje słowo kluczowe",
      "definition": "Jasna definicja odpowiednia dla uczniów w wieku 8–18 lat."
    }
  }
}
```

**Field guide:**

| Field | Description |
|---|---|
| `id` | Unique identifier. Use lowercase and hyphens, e.g. `binary-search`. No spaces. |
| `topic` | Must match an existing topic `id` (see the topics list below). |
| `translations` | An object with one key per language code. You must include at least `en`. |
| `term` | The keyword as it should be displayed. |
| `definition` | The definition. Plain language, 1–2 sentences. |

**If you don't speak all the languages**, that's fine — add the languages you know and note in your PR that others need translating. Someone else can fill them in.

### 3. Add a translation for an existing keyword

Find the keyword in `keywords.json` and add a new language key inside its `translations` object:

```json
"translations": {
  "en": { "term": "Algorithm", "definition": "..." },
  "pl": { "term": "Algorytm", "definition": "..." },
  "fr": { "term": "Algorithme", "definition": "..." }
}
```

### 4. Add a new topic

Adding a topic requires changes in two places.

**Step 1** — add it to the `topics` array:

```json
{
  "id": "hardware",
  "icon": "🖥️",
  "labels": {
    "en": "Hardware",
    "pl": "Sprzęt"
  }
}
```

**Step 2** — add UI labels for the new topic in every language that exists in `meta.languages`.

Then add keywords with `"topic": "hardware"` as normal.

### 5. Add a new language

Adding a language requires three changes:

**Step 1** — add it to `meta.languages`:
```json
{ "code": "fr", "label": "Français" }
```

**Step 2** — add UI strings to the `ui` object:
```json
"fr": {
  "site_title": "Mots-clés Info",
  "site_subtitle": "Vocabulaire informatique pour tous",
  "search_placeholder": "Rechercher des mots-clés…",
  "all_topics": "Tous les sujets",
  "no_results": "Aucun mot-clé trouvé. Essayez une autre recherche.",
  "footer_text": "Données contributives.",
  "footer_contribute": "Suggérer des modifications sur GitHub"
}
```

**Step 3** — add the new language's `labels` to every topic, and `translations` to as many keywords as you can.

---

## Topic IDs

| Icon | Label | ID |
|---|---|---|
| ⚙️ | Algorithms | `algorithms` |
| 💻 | Programming | `programming` |
| 🌐 | Networking | `networking` |
| 🗄️ | Data & Databases | `data` |
| 🔒 | Security | `security` |

---

## Pull request checklist

Before submitting, please check:

- [ ] `keywords.json` is valid JSON (paste it into [jsonlint.com](https://jsonlint.com) if unsure)
- [ ] Every new keyword has at least an `en` translation
- [ ] `id` values are unique and use only lowercase letters, numbers, and hyphens
- [ ] Definitions are plain English, suitable for ages 8–18
- [ ] No duplicate keywords (search the file for your term first)

---

## Questions?

Open an issue and we'll help you out.
