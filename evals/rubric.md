# Evaluation rubric

## Status

The skill has not been behaviorally validated. This directory contains prompts and a rubric; no run has been completed and no results are recorded. Until `results/` holds at least one full run scored under this rubric, the skill is structurally reviewed, not evidence-backed. Do not describe it as validated before then.

## Protocol

- Run every prompt in [prompts.md](prompts.md) with and without the skill, same model and settings.
- Generate **three samples per prompt per condition**. Score all of them; report medians and the spread, since a skill that raises the floor matters as much as one that raises the ceiling.
- Use **at least two independent reviewers per locale**, each a native speaker familiar with the requested variety. Use reviewers from both Bangladesh and West Bengal for cross-region prompts.
- Blind the condition and randomize pair order. Reviewers must not see which sample came from which condition, or which samples share a prompt.
- Report results **broken down by task type** — the prompt groups in [prompts.md](prompts.md) — and not only as one aggregate median. A skill can help translation and hurt review.
- Record inter-reviewer agreement. If two reviewers of the same locale disagree by more than one point on a dimension, discuss that item before it enters the totals.

## Automated checks (run before human review)

These are mechanical and should gate the run; a failure here does not need a reviewer's time.

- **Protected strings:** every URL, command, path, filename, code span, API name, identifier, and placeholder token (`{count}`, `%s`, `%1$d`, `{{name}}`) from the source appears in the output byte-identical, and no new ones appear.
- **Quotations:** any span quoted in the source is reproduced exactly.
- **Numbers:** every numeral in the source has a counterpart in the output with the same value, allowing for Bengali/Latin digit conversion and লাখ/কোটি unit conversion. Flag any number that appears in the output but not the source.
- **Markup:** heading levels, list markers, bold/italic spans, and link targets match the source structure.
- **Script:** the output is Unicode Bengali, not romanized, unless transliteration was requested.
- **Length and format:** word-count and structural constraints stated in the prompt are met.
- **Digit consistency:** the output does not mix Bengali and Latin digits except where the prompt requires it (code, identifiers).
- **Honorific agreement:** flag `তিনি` co-occurring with non-honorific finite verbs (`বলল`, `করল`, `গেল`) for reviewer attention.
- **সাধু forms:** flag `তাহা*`, `উহা*`, `ইহা`, `যাহা`, `করিয়া*`, `হইয়া*`, `হইতে` in output that is otherwise চলিত. Bookish-but-valid words such as `নিকট` or `প্রদান` are not সাধু; route those to the register dimension instead of failing them.
- **Loanword spelling:** flag `ষ্ট` and `ণ` inside known non-tatsama loanwords (`পোষ্ট`, `ষ্টেশন`, `রেজিষ্ট্রেশন`, `কর্ণার`).
- **Invalid plurals:** flag `-রা`/`-দের` on clearly inanimate nouns and `-গুলো`/`-গুলি` on person nouns in formal output.

## Hard failures

Mark an output as failed if it:

- adds, removes, or materially strengthens a factual claim, including by replacing removed padding with invented specifics
- changes a number, name, quotation, URL, command, identifier, or explicit constraint
- uses inconsistent forms of address or mismatched honorific verbs
- leaves সাধু forms inside চলিত prose, or half-converts a সাধু source
- ignores the requested region, register, format, or length
- resolves an ambiguity the prompt required it to preserve
- returns a full rewrite when the prompt asked for review only
- "corrects" an already natural construction because of an overgeneralized rule

## Scored dimensions

Score each from 1 to 5, using these anchors. Reserve 3 for competent-but-unremarkable output; do not treat it as a default.

**1. Fidelity** — meaning, stance, uncertainty, and details.
5: every claim, hedge, quantity, and emphasis survives; nothing is added. 4: one negligible shade of emphasis shifts. 3: a minor detail is generalized or a hedge weakened, without changing the point. 2: a claim is strengthened, narrowed, or invented. 1: the output says something the source does not.

**2. Idiomaticity** — syntax and collocations conceived in Bengali.
5: no sentence betrays a source language; negation, aspect, compound verbs, and clause structure are all native. 4: fluent, with one avoidable calque. 3: readable but the English shape shows in two or three places. 2: recognizably translated throughout — calqued passives, bare verbs, English word order. 1: comprehensible only by reconstructing the English.

**3. Audience fit** — vocabulary, explanation level, code-switching.
5: terminology and explanation land exactly for the stated reader and medium. 4: one term is slightly off-register. 3: generally appropriate, with noticeable over- or under-translation of technical vocabulary. 2: purist coinages or unexplained jargon that the stated reader would stumble on. 1: aimed at a different audience entirely.

**4. Regional and register consistency** — locale, formality, pronouns, verb forms.
5: fully coherent, with no unmotivated regional or register swing. 4: one overlapping form that a native writer might also use. 3: mostly coherent, one clear inconsistency. 2: repeated swings between varieties or formality levels. 1: incoherent, or the wrong variety for an explicit request.

**5. Flow and voice** — sentence rhythm, paragraph movement, distinctive voice.
5: varied rhythm, connectors earn their place, any distinctive voice is intact. 4: slight uniformity in sentence length or openings. 3: competent but even-paced; the structure is faintly audible. 2: templated — repeated openings, a connector at every paragraph head, a summarizing final sentence nobody asked for. 1: mechanical, or the source's voice has been erased.

**6. Orthography and typography** — spelling, punctuation, numerals, mixed scripts, protected strings.
5: one consistent convention throughout, loanword spelling correct, protected strings exact. 4: one trivial inconsistency. 3: two or three inconsistencies, none consequential. 2: `ষ`/`ণ` in loanwords, mixed digit systems, or inconsistent spelling of the same word. 1: protected strings altered.

**7. Restraint** — edits are consequential and not imposed.
5: every change is justified; already-natural constructions are untouched. 4: one cosmetic edit. 3: some unnecessary polishing, no harm done. 2: rules applied mechanically — classifiers, slang, loanwords, or syntactic transformations added where context does not support them. 1: a conspicuous rewrite that changed the writer's voice without being asked.

## Pairwise judgment

After scoring, ask: “Which version would a capable native writer be more likely to publish or send in this context?” Allow A, B, or tie, and require a one-sentence reason.

## Publication bar

The skill is ready to publish when:

- no hard failure is attributable to a skill instruction
- it improves median idiomaticity and audience-fit scores over the no-skill baseline, in each task group and not only in aggregate
- it does not reduce median fidelity in any task group
- it does not reduce median restraint — a gain in idiomaticity paid for by overcorrection is not a gain
- neither regional reviewer group shows a recurring preference against the skill output

Treat reviewer disagreement as evidence to refine a narrow example or decision rule, not as a reason to add universal prohibitions.

## Recording results

Write one file per run under `results/`, containing: model and settings, date, prompt set version, per-prompt scores for both conditions from every reviewer, automated-check failures, pairwise verdicts with reasons, and the task-group breakdown. Note any prompt where reviewers disagreed by more than one point and how it was resolved.
