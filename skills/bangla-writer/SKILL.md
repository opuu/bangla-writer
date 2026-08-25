---
name: bangla-writer
description: Write, translate, localize, rewrite, or review natural Bengali (Bangla) prose for a given audience, region, and register. Use for everyday messages, letters, literary and creative prose, journalism, essays and academic writing, official and legal notices, education, health and public information, business, marketing, support, and product or technical text, in Bangladeshi, West Bengal, or cross-region varieties. Do not use for transliteration-only requests or linguistic analysis that produces no Bengali prose.
license: MIT
metadata:
  author: bangla-writer contributors
  version: "1.1"
  language: bn
---

# Natural Bengali Writing

Produce Bengali that reads as if it was conceived in Bengali, not mapped word by word from another language. Preserve the writer's meaning, facts, stance, and formatting while improving idiom, flow, and audience fit.

This applies to any kind of text — a message to a friend, a short story, a news report, an exam answer, a government notice, a product screen. The grammar rules below hold everywhere; the register, vocabulary, and rhythm change with the genre.

## Decide the target

Infer these from the request and source text:

- task: compose, translate/localize, rewrite, review only, or review and revise
- genre and medium: what kind of text this is and where it will appear
- audience and relationship to the reader
- region: Bangladesh, West Bengal (Indian Bengali), or cross-region
- register: intimate, conversational, professional, formal, literary, journalistic, academic, official, or promotional

Ask a concise question only when an unresolved choice would materially change the result. Otherwise use broadly understood standard colloquial Bengali. If the context clearly points to Bangladesh or West Bengal, keep that variety coherent — but real writers mix forms current in both regions, so keep the choices consistent without purging every overlapping form.

When guidance conflicts, follow this order: an explicit user instruction, then a supplied glossary or the existing publication, interface, or house style, then the established voice of the source text, then this skill.

## Always apply

These rules decide most of the distance between native and translated Bengali. Apply them in every genre, even when no reference file is loaded.

1. **Negation follows the predicate.** `নেই` for absence or possession, `নয়/নন` for identity, `না` for verbs and imperatives, and the suffix `-নি` for the past and perfect: `আমি বুঝিনি`, never `আমি বুঝেছিলাম না`. `আসে না` (habitual) and `আসেনি` (past) are not interchangeable.
2. **Keep address and agreement coherent.** `আপনি`, `তুমি`, or `তুই` fixes the possessive and the verb form for the whole text. Never pair `তিনি` with `বলল`.
3. **Never mix সাধু and চলিত** (গুরুচণ্ডালী দোষ). Do not drop `তাহার`, `উহারা`, `করিয়াছে`, or `হইতে` into otherwise modern prose, and do not leave one archaic inflection behind when converting a সাধু source.
4. **Use compound verbs where Bengali would.** `খেয়ে নাও`, `বলে দিয়ো`, `লিখে ফেলেছি`, `ভুলে গেছি` carry aspect and stance that the bare verb loses.
5. **Do not calque English passives.** Prefer an impersonal or modal frame: `আবেদন করতে হবে`, not `আবেদনকারীদের দ্বারা আবেদন করা আবশ্যক`.
6. **Mark plurals by animacy.** `-রা/-দের` for people and animals, `-গুলো/-গুলি` for things. `চিঠিরা` is not Bengali; `ছাত্রগুলো` is wrong in formal text.
7. **Foreign loanwords take no `ষ` or `ণ`.** `পোস্ট`, `স্টেশন`, `রেজিস্ট্রেশন`, `কর্নার` — not `পোষ্ট`, `ষ্টেশন`, `রেজিষ্ট্রেশন`, `কর্ণার`.
8. **Cut empty framing, but add nothing.** Remove `বর্তমান প্রেক্ষাপটে`, `উল্লেখ্য যে`, or `একটি গুরুত্বপূর্ণ ভূমিকা পালন করে` without replacing the removed words with facts the source never stated.

## Write and revise

1. Preserve claims, quantities, names, quotations, links, markup, and technical meaning. Do not add facts or stronger certainty.
2. Express the idea with natural Bengali syntax. Restructure clauses rather than imitating the source's word order.
3. Keep pronouns, honorific level, and verb agreement consistent. Omit an already clear subject when Bengali naturally would.
4. Prefer concrete, familiar wording at the requested register. Keep loanwords or English terms when the audience would normally use them; do not pursue linguistic purity.
5. Vary sentence length according to the content. Remove mechanical transitions, repeated conclusions, inflated significance, and template-like lists when they add no meaning.
6. Read the result once for meaning and once for voice. It should sound plausible when spoken or signed by the intended writer.

## Reference files

Read only what the task needs.

| Read this                                                                                    | When                                                                                                                                                             |
| -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [references/genres.md](references/genres.md)                                                 | The text belongs to a recognizable genre — letter, story, report, essay, notice, lesson, speech, caption, or anything else with its own conventions              |
| [references/grammar-and-syntax.md](references/grammar-and-syntax.md)                         | Negation, tense and aspect, compound verbs, experiencer subjects, reflexives, honorific agreement, classifiers, plural marking, conditionals, or clause chaining |
| [references/naturalness-patterns.md](references/naturalness-patterns.md)                     | Translating, or repairing stiff, formulaic, or machine-written prose. Treat its patterns as diagnostic clues, not banned words                                   |
| [references/region-and-register.md](references/region-and-register.md)                       | Regional vocabulary, forms of address, or a shift in formality                                                                                                   |
| [references/orthography-and-typography.md](references/orthography-and-typography.md)         | Spelling, punctuation, numerals, large numbers, quotations, or mixed-script text                                                                                 |
| [references/product-and-technical-language.md](references/product-and-technical-language.md) | Software, UI, support, business, or ecommerce text, before deciding whether to translate, transliterate, or keep an English term                                 |
| [references/examples.md](references/examples.md)                                             | A difficult rewrite, or a genre you want to see demonstrated. Adapt the decisions; never copy an example as a template                                           |

## Output

- For composition, translation, localization, or rewriting, return only the finished text unless the user asks for commentary.
- For **review and revise**, give the revised text first, followed by brief notes on consequential choices.
- For **review only** — the user asks for a diagnosis, critique, or judgment — give the assessment and quote short fragments to illustrate. Do not substitute a full rewrite for the answer; offer one only if the user invites it.
- Preserve requested structure and length. Do not add headings, summaries, emoji, or multiple alternatives unless useful or requested.
- If the source is genuinely ambiguous, preserve the ambiguity rather than silently inventing a meaning.

## Final check

Before returning the text, verify:

- no meaning or factual detail was introduced, removed, or intensified unintentionally, including when cutting empty framing
- genre, region, and register are coherent, with no সাধু form left inside চলিত prose
- forms of address agree with verbs throughout
- past and perfect negation uses `-নি`, and each negator matches its predicate
- plural suffixes match animacy; classifiers and case markers fit the actual construction rather than a blanket rule
- passives were reframed rather than calqued
- sentences do not sound translated merely to retain the source structure
- spelling, punctuation, numerals, large-number units, and retained foreign terms follow one consistent convention
