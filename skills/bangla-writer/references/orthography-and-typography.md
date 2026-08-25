# Orthography and typography

Use the user's or publisher's stated style first. Otherwise apply one coherent convention and avoid silently modernizing quoted, historical, or branded text.

## Foreign and loanword spelling (ণ-ত্ব ও ষ-ত্ব বর্জন)

Non-tatsama words — English, Persian, Arabic, Portuguese, and other borrowings — do not take `ষ` or `ণ`. Both the Bangla Academy (Dhaka) and Paschimbanga Bangla Akademi standards agree on this, and misapplying the Sanskrit retroflex rules to loanwords is one of the most common spelling failures in generated Bengali.

| Correct | Not |
| --- | --- |
| `পোস্ট` | `পোষ্ট` |
| `স্টেশন` | `ষ্টেশন` |
| `রেজিস্ট্রেশন` | `রেজিষ্ট্রেশন` |
| `স্টাফ`, `মাস্টার`, `স্টাইল` | `ষ্টাফ`, `মাষ্টার`, `ষ্টাইল` |
| `কর্নার`, `গভর্নর`, `ইন্টারনেট` | `কর্ণার`, `গভর্ণর`, `ইন্টারণেট` |

`ষ` and `ণ` remain correct in tatsama vocabulary, where the rules do apply: `কষ্ট`, `বিশিষ্ট`, `কারণ`, `ব্যাকরণ`. Do not "fix" those.

Two exceptions: a proper name, brand, or trademark spells itself however it spells itself, and quoted or historical text is reproduced as written.

## সাধু and চলিত must not mix

Standard modern prose is চলিত. Do not leave `তাহার`, `উহারা`, `যাহা`, `ইহা`, `করিয়াছে`, `হইতে`, or `হইয়াছিল` inside otherwise modern sentences — the mixture is গুরুচণ্ডালী দোষ and reads as an error, not as formality. Formality comes from vocabulary and sentence structure, not archaic inflection. When a source is deliberately সাধু, convert all of it or none of it.

## Spelling

- Keep the selected regional standard consistent.
- Distinguish the yes/no particle `কি` from interrogative or exclamatory `কী` when the distinction applies: `আপনি কি যাবেন?` and `আপনি কী চান?`
- Bangladeshi standard usage prefers ই-কার in many naturalized and derived words where West Bengal usage often keeps ঈ-কার: `জরুরি`/`জরুরী`, `দাবি`/`দাবী`, `শ্রেণি`/`শ্রেণী`, `তরকারি`/`তরকারী`. Pick the one that matches the chosen locale and apply it throughout — mixing the two in one document is a stronger regional tell than any single vocabulary choice.
- **Drop terminal bisarga (শব্দান্তে বিসর্গ বর্জন):** Standard modern Bengali in both Bangladesh and West Bengal omits trailing `ঃ` from adverbs, conjunctions, and derived words: `মূলত`, `প্রধানত`, `সাধারণত`, `বিশেষত`, `ফলত`, `ক্রমশ`, `প্রায়শ` (not `*মূলত:`, `*প্রধানত:`, `*ফলত:`, `*ক্রমশ:`). Medial bisarga in tatsama compounds remains: `দুঃখ`, `নিঃশব্দ`, `পুনঃপুন`.
- Do not "correct" a proper name, title, trademark, or intentional character voice without evidence.
- Avoid mixing alternative spellings of the same word in one document unless reproducing source material.

When a spelling is consequential and uncertain, consult the user's specified dictionary, organizational guide, or jurisdictional authority. Do not invent a universal rule from memory beyond the settled ones above.

## Punctuation

- `।` is the usual sentence terminator for Bengali prose. A product, technical document, or house style may consistently use `.` instead; follow that style.
- Do not leave a space before `।`, and do not substitute `|` (the pipe character) for it.
- Use `?` and `!` sparingly and according to the tone.
- Use commas to clarify grouping, not to reproduce every pause or comma in an English source.
- Use one quotation style consistently, commonly `“…”` with `‘…’` for a quote inside a quote.
- Avoid decorative em dashes, ellipses, bolding, or parentheses that were not needed by the content.

## Numerals, dates, and units

Choose Bengali or Latin digits from context:

- Bengali digits often suit general Bengali prose, cultural material, and publications that use them consistently.
- Latin digits often suit code, data, scientific units, international product interfaces, account details, and mixed-language technical text.

Whichever you choose, use it for every numeral in the document.

### Large numbers

Bengali counts in `হাজার`, `লাখ`, `কোটি`, not in millions and billions. Converting the unit is part of localization, and the arithmetic must be exact.

- 1.2 million → `১২ লাখ`, not `১.২ মিলিয়ন`
- 25 million → `আড়াই কোটি` or `২ কোটি ৫০ লাখ`
- 3 billion → `৩০০ কোটি`

Bangladesh writes `লাখ`; West Bengal also uses `লক্ষ`. Both regions group digits South Asian style: `২,৪৭,৮০০`, not `247,800`. Keep the value identical to the source, and if the source figure is approximate, keep it approximate.

### Dates and units

Preserve exact values. Keep dates unambiguous for the audience — `৫ জানুয়ারি ২০২৫` is safe in both regions, while numeric forms such as 05/01/2025 are not. Do not convert calendars or units unless asked; if a Bangla-calendar date appears, reproduce it rather than converting it. Put a normal space between a value and a unit when the applicable style calls for it.

## Foreign terms and transliteration

- Preserve code, commands, paths, URLs, handles, model names, and identifiers exactly.
- Use an established Bengali spelling for widely naturalized names when appropriate; otherwise retain the official Latin form or introduce a Bengali rendering once.
- Do not transliterate an English technical term merely to make it look Bengali if that makes it harder to recognize.
- In mixed text, keep spacing around Latin terms readable and consistent with the surrounding format.

## Unicode care

- Return actual Unicode Bengali text, not romanized Bengali, unless transliteration is requested.
- Use standard precomposed (NFC) characters: prefer `য়` (`U+09DF`) over decomposed `য` (`U+09AF`) + Nukta (`U+09BC`), and `ৎ` (`U+09CE`, Khanda Ta) over decomposed `ত` (`U+09A4`) + Virama (`U+09CD`).
- Do not manipulate joiners (ZWJ/ZWNJ), conjuncts, or normalization merely for visual neatness.
- Avoid unnecessary trailing hasanta (`্`) on closed syllables where standard Bengali spelling does not require it (`চেক`, `ট্যাক্স`, not `চেক্`, `ট্যাক্স্`).
- Copy sensitive strings such as names, quotations, and identifiers faithfully.
