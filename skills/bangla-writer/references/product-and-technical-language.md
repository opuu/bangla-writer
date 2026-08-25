# Product and technical language

Use this reference for software, UI, customer support, business, ecommerce, and mixed-language professional text.

## Choose terminology from the audience

For each important term, choose among:

1. an established Bengali word: `নথি`, `সংযোগ`, `অনুমতি`
2. a naturalized Bengali-script loanword: `ফাইল`, `লগইন`, `পাসওয়ার্ড`
3. the official or established Latin-script term: `API`, `staging environment`, `retryCount`

Prefer the form the intended reader will recognize fastest. Do not transliterate every English term, and do not replace familiar product language with obscure purist coinages. Follow a supplied glossary or existing interface over this guide.

## Common naturalized terms

Depending on locale, product, and house style, Bengali-script forms commonly include:

- product and UI: `অ্যাপ`, `ফাইল`, `ফোল্ডার`, `লিঙ্ক`, `সেটিংস`, `নোটিফিকেশন`, `আপডেট`, `অ্যাকাউন্ট`, `মেসেজ`
- actions: `লগইন`, `লগআউট`, `ডাউনলোড`, `আপলোড`, `সেভ`, `ডিলিট`, `ব্যাকআপ`, `রিসেট`
- systems: `সার্ভার`, `ব্রাউজার`, `ডেটাবেস`, `ওটিপি`, `স্ক্রিনশট`
- business and commerce: `মিটিং`, `প্রজেক্ট`, `ক্লায়েন্ট`, `পেমেন্ট`, `অর্ডার`, `ডেলিভারি`, `রিফান্ড`, `ইনভয়েস`, `ডিসকাউন্ট`

These are options, not mandatory replacements. `বৈঠক`, `বার্তা`, `নথি`, `ছাড়`, `ফেরত`, and other Bengali terms may be more natural in public-sector, editorial, literary, or fully localized contexts.

Avoid obscure literal substitutes such as `গুপ্তশব্দ` for password or `অধোগমন` for download unless discussing the words themselves.

Spell these loanwords without `ষ` or `ণ` — `পোস্ট`, `রেজিস্ট্রেশন`, `কর্নার`, not `পোষ্ট`, `রেজিষ্ট্রেশন`, `কর্ণার`. See [orthography-and-typography.md](orthography-and-typography.md).

## Light and compound verbs

Borrowed nouns and verbs combine naturally with Bengali verbs, and a vector verb often carries the aspect an interface needs:

- `লগইন করা`
- `কল করা` / `কল দেওয়া`
- `চেক করে নেওয়া`
- `সেভ করে রাখা`
- `আপডেট দেওয়া`
- `ডিলিট করে ফেলা`

Choose the vector from what the action actually does. `ডিলিট করুন` is neutral; `ডিলিট করে ফেলুন` tells the user the deletion is final, which is wrong on a control that only moves an item to trash. See the compound-verb section in [grammar-and-syntax.md](grammar-and-syntax.md).

Do not stack borrowed words when a short Bengali predicate is clearer. `ফাইলটি খুলুন` may be smoother than `ফাইলটি ওপেন করুন`; both can be appropriate in different interfaces.

## UI localization

Translate the action in context rather than an isolated English label:

- `Continue` → `চালিয়ে যান`, `পরবর্তী`, or `এগিয়ে যান`, depending on what the control does
- `Cancel` → usually `বাতিল`, though conversational product copy may use `ক্যান্সেল`
- `Try again` → `আবার চেষ্টা করুন` or, for an established conversational voice, `আবার ট্রাই করুন`

Keep labels short, parallel, and consistent across a flow. Do not add politeness markers to every button. Match the product's chosen `আপনি` or `তুমি` in explanatory text. Bengali usually runs longer than English, so check that the label still fits its control rather than padding it.

## Placeholders, variables, and plurals

Localized strings are code as well as prose.

- Never translate, reorder, respace, or "correct" a placeholder token: `{count}`, `%s`, `%1$d`, `{{name}}`, `<b>`, `\n`. Reordering positional tokens such as `%s` changes which value lands where.
- Attach classifiers and case markers to a placeholder the way you would to the value it holds: `{count}টি ফাইল মুছে ফেলা হয়েছে।`, `{name}-কে পাঠানো হয়েছে।` Write `{name}-এর ফাইল`, never `{name} এর ফাইল`.
- Confirm what the variable actually renders before attaching a suffix. `-টি` after a numeral is fine; after a word or a formatted string it may not be.
- CLDR defines `one` and `other` plural categories for Bengali, but the two forms are usually the same text because Bengali does not mark plural agreement on the counted noun. Supply a distinct `one` string only when the copy genuinely differs at 1, and do not invent an English-style singular/plural split.
- A string that only reads well with the variable in the middle should be rewritten, not bent. If the framework forces a leading placeholder, choose wording that survives it.

## Error and support messages

State what happened, what the user can do, and any irreversible consequence. Avoid blaming the user or exposing implementation detail without a reason.

Over-translated:

> সংযোগে ত্রুটি সংঘটিত হয়েছে। অনুগ্রহপূর্বক পুনরায় প্রচেষ্টা করুন।

Natural formal:

> সংযোগে সমস্যা হয়েছে। আবার চেষ্টা করুন।

Natural conversational product voice:

> নেটওয়ার্কে সমস্যা হয়েছে। আবার ট্রাই করুন।

The best version depends on the existing interface vocabulary.

## Technical precision

- Preserve identifiers, commands, paths, URLs, API names, configuration keys, and code exactly.
- If both audiences need the term, introduce it once as `বাংলা শব্দ (English term)` or the reverse, then use one stable form.
- Do not substitute different synonyms for the same concept merely to avoid repetition, and keep one term for one concept across the whole document.
- Keep modality exact: `may`, `can`, `must`, and `should` should not collapse into the same strength. `করতে হবে` (must), `করা উচিত` (should), `করতে পারেন` (may/can) are distinct, and the difference is consequential in legal, medical, and safety text.
- Retain standard abbreviations such as `OTP`, `API`, `URL`, or `HTTP` when they help recognition; define them only when the audience needs it.
- Money and quantities follow the Bengali units: `১২ লাখ টাকা`, not `১.২ মিলিয়ন টাকা`.

## Mixed-script suffixes

Attach Bengali case markers to Bengali-script loanwords directly: `অ্যাপে`, `ফাইলটি`, `সার্ভারের`. With Latin-script terms, a hyphen is usually clearer: `API-তে`, `server-এর`, `ChatGPT-কে`. This is the general affix rule from [grammar-and-syntax.md](grammar-and-syntax.md) applied to product text; an established product style overrides it.

## Transliteration consistency

When using Bengali-script loans, choose a recognized modern spelling and keep it stable. Short `ি` is common in many non-tatsama foreign words such as `পলিসি`, `ডিগ্রি`, and `সিকিউরিটি`, but brand spellings and regional house styles take precedence. Do not alter quoted text or proper names to enforce this tendency.
