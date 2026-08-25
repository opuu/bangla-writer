# Naturalness patterns

Use these patterns to diagnose translationese and generic machine prose in any kind of text — a letter, a news report, an essay, a notice, a caption. None is automatically wrong; revise only when the phrase weakens this particular text.

Every rewrite below stays inside the source's content. Cutting padding is not a licence to add specifics, causes, or numbers that the source never supplied — an invented detail is a worse failure than the padding it replaced.

## Translate the intent, not the surface

Literal structure often carries the words but loses the Bengali thought pattern.

- `At the end of the day` may become `শেষ পর্যন্ত`, `শেষমেশ`, or disappear entirely; it is not always `দিনের শেষে`.
- `We are excited to announce` may be `জানাতে পেরে আমরা আনন্দিত`, a direct announcement, or a warmer conversational line depending on the speaker.
- An English passive may be clearer as an active or subjectless Bengali sentence.
- Several short English sentences may form one fluent Bengali sentence; one overloaded English sentence may need to be split.

Before:

> দিনের শেষে, এটি মনে রাখা গুরুত্বপূর্ণ যে ছোট পরিবর্তনগুলো একটি বড় প্রভাব তৈরি করতে পারে।

After:

> শেষ পর্যন্ত ছোট পরিবর্তনও বড় প্রভাব ফেলতে পারে।

The revision removes framing that contributes no meaning and uses a more direct predicate. `প্রভাব` stays because the source said impact.

## Convert English passives to impersonal or modal frames

Bengali obligation and agentless report do not need a `দ্বারা` phrase. Copying one produces the single most recognizable calque in translated Bengali.

- "Applicants are required to submit two photographs."
  - Calque: `আবেদনকারীদের দ্বারা দুই কপি ছবি জমা দেওয়া আবশ্যক।`
  - Natural: `দুই কপি ছবি জমা দিতে হবে।` or `আবেদনকারীকে দুই কপি ছবি জমা দিতে হবে।`
- "It was decided to postpone the meeting."
  - Calque: `এটি সিদ্ধান্ত নেওয়া হয়েছিল যে সভা পিছিয়ে দেওয়া হবে।`
  - Natural: `সভা পেছানোর সিদ্ধান্ত নেওয়া হয়েছে।`
- "The letter was written by my grandfather."
  - Calque: `চিঠিটি আমার দাদুর দ্বারা লিখিত হয়েছিল।`
  - Natural: `চিঠিটা আমার দাদু লিখেছিলেন।`
- "Your request has been received."
  - Natural: `আপনার অনুরোধ পেয়েছি।` or agentless `আপনার অনুরোধ গৃহীত হয়েছে।`

Choose the frame from what the source commits to. If the source deliberately hides the agent, do not name one; if it names the agent, do not delete them. Keep `দ্বারা` or `কর্তৃক` where a legal, scientific, or official genre expects it, and keep impersonal academic frames such as `দেখা যায়` or `বলা যেতে পারে`, which are native Bengali, not calques.

## Prefer verbs to padded noun phrases

LLM prose often adds `করা`, `প্রদান করা`, `নিশ্চিত করা`, or an abstract noun where a plain verb is clearer.

Before:

> কমিটি বিষয়টির একটি পর্যালোচনা সম্পাদন করবে এবং সুপারিশের বাস্তবায়ন করবে।

After:

> কমিটি বিষয়টি পর্যালোচনা করে সুপারিশ কার্যকর করবে।

The nouns become verbs and the two clauses join non-finitely; `পর্যালোচনা` is kept because review is what the source says, not something looser like `দেখা`.

Keep the more formal noun phrase when it is an official process or technical term.

## Remove empty framing

Question phrases such as these when they recur without doing real work:

- `উল্লেখ্য যে`
- `এ কথা বলার অপেক্ষা রাখে না`
- `বর্তমান প্রেক্ষাপটে`
- `সামগ্রিকভাবে বলা যায়`
- `একটি গুরুত্বপূর্ণ ভূমিকা পালন করে`
- `নতুন দিগন্ত উন্মোচন করে`
- `সময়ের সাথে সাথে`

Do not replace them mechanically. State the underlying fact, or keep the phrase when emphasis, contrast, or scope genuinely requires it.

Before:

> বর্তমান ডিজিটাল যুগে সামাজিক যোগাযোগমাধ্যম আমাদের দৈনন্দিন জীবনে একটি গুরুত্বপূর্ণ ভূমিকা পালন করে।

After:

> সামাজিক যোগাযোগমাধ্যম এখন দৈনন্দিন জীবনেরই অংশ।

The source claims only that social media matters in daily life, so the revision claims only that. Writing something like `ছবি ভাগ করা থেকে খবর জানা পর্যন্ত সবই এখন সামাজিক মাধ্যমে হয়` would read well and still be a failure: it invents activities and a scope the source never mentioned. When the source is vague, the honest rewrite is short, not detailed. This is the commonest fault in rewritten essays and opinion pieces, where a hollow opening tempts you to fill it.

## Control connectors

`তবে`, `এছাড়া`, `অন্যদিকে`, `ফলে`, and `সুতরাং` are useful when the logical relation is real. Repeating one at the start of each paragraph makes the structure audible. Let sequence and syntax carry obvious relationships.

## Avoid unnecessary subjects and references

Repeated `এটি`, `সেটি`, `তিনি`, or a full noun can sound translated when the referent is already clear. Omit it only when no ambiguity results.

Before:

> বইটি ছোট। এটি সহজ ভাষায় লেখা। এটি নতুন পাঠকের জন্যও উপযুক্ত।

After:

> বইটি ছোট, সহজ ভাষায় লেখা এবং নতুন পাঠকের জন্যও উপযুক্ত।

## Let compound verbs carry aspect

Flat bare verbs are a quieter symptom of translated prose than a bad word choice, and easier to miss.

Before:

> রান্না করুন, তারপর টেবিলে খাবার দিন এবং সবাইকে ডাকুন।

After:

> রান্না করে রাখুন, তারপর টেবিলে খাবার দিয়ে সবাইকে ডেকে নিন।

Add the vector only when its meaning is true: `করে রাখুন` implies doing it in advance, `ডেকে নিন` implies gathering them to you. See the compound-verb section in [grammar-and-syntax.md](grammar-and-syntax.md).

## Keep repetition when it helps

Do not rotate through synonyms merely to avoid repeating a precise word. In technical, legal, and instructional text, stable terminology is usually more natural and safer.

Conversely, repeated sentence openings or identical three-part lists may signal a template. Change the structure, not just the vocabulary.

## Calibrate claims and emotion

Do not turn ordinary facts into `যুগান্তকারী`, `অভূতপূর্ব`, `বৈপ্লবিক`, `অনন্য`, or `অপরিহার্য` claims without support. Match the source's confidence. Marketing can be energetic without inventing proof.

Deflating a claim is also an edit. `সম্ভবত`, `হতে পারে`, `কিছু ক্ষেত্রে`, and `প্রায়` must survive the rewrite when the source hedges, and must not appear when it does not.

## Use code-switching deliberately

Loanwords are normal in ordinary Bengali, not only in technical writing: `স্কুল`, `ট্রেন`, `ডাক্তার`, `চেয়ার`, `কলম`, `বাজার` come from four different languages and nobody hears them as foreign. Retain the terms the audience actually uses. Translate when a Bengali expression is established and equally clear. Avoid unstable mixtures such as translating a term differently on every occurrence.

Natural in a workplace note:

> মিটিংয়ের আগে রিপোর্টটা একবার দেখে নিন।

Natural in a developer's note:

> ডিপ্লয় করার আগে staging environment-এ পরিবর্তনগুলো পরীক্ষা করুন।

Natural in a school textbook, where the same idea gets defined once and then localized:

> পরিবেশ (environment) বলতে এখানে বোঝানো হচ্ছে…

Choose based on audience, not purity. Reaching for `দূরালাপনী` instead of `ফোন` is as much a failure as leaving an English word the reader will not know.

## Watch for সাধু-চলিত mixing

A model that has absorbed older Bengali text will sometimes drop a single archaic form into modern prose: `তাহার`, `উহারা`, `করিয়াছে`, `হইতে`, `যাহা`, `ইহা`. One such form in an otherwise চলিত sentence is গুরুচণ্ডালী দোষ, and native readers notice it immediately.

Wrong:

> তাহার সিদ্ধান্ত জানার পর আমরা কাজ শুরু করেছি।

Right:

> তাঁর সিদ্ধান্ত জানার পর আমরা কাজ শুরু করেছি।

The same applies in reverse: when a source is deliberately সাধু, convert all of it or none of it. Half-converted prose is worse than either. Verse, scripture, and some official formulas are legitimately সাধু; leave them alone.

## Preserve voice during rewriting

Human writing can contain fragments, asymmetry, humor, hesitation, and repetition. Do not polish away a distinctive voice merely because it is irregular. Fix what obstructs the requested effect; preserve what creates it.

## Do not manufacture naturalness

Natural Bengali is not automatically casual Bengali. Do not add slang, echo words such as `কাজটাজ`, conversational fillers, contractions, English loans, or emphatic particles merely to make formal or neutral text sound human. Likewise, do not remove every passive, nominalization, `যদি … তাহলে`, or repeated term. Prefer the form that serves the genre, relationship, and intended emphasis.

If a source sentence is already idiomatic and correct, leave it alone. A smaller edit is better than a conspicuous rewrite that changes the writer's voice.
