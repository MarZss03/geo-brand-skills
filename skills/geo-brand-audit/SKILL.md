---
name: geo-brand-audit
description: Audit how a brand appears in generative and AI answer engines using reproducible query tests, citation evidence, technical discoverability checks, and explicit uncertainty. Use when a user asks for a GEO audit, AI visibility audit, answer-engine visibility comparison, brand citation analysis, or a baseline before optimization. Do not use for generic SEO copywriting or unsupported ranking promises.
---

# GEO Brand Audit

Build an evidence-backed baseline of a brand's observed visibility in AI-generated answers. Treat each answer as a time-stamped observation, not a permanent ranking.

## Workflow

1. Confirm the brand/domain, market and language, relevant answer engines or models, competitors, and audit date. State any assumptions instead of blocking on minor omissions.
2. Build a query set across four intents: category discovery, problem/solution, comparison, and branded verification. Include at least five queries per important market when practical.
3. Capture each run using the fields in [evidence-schema.md](references/evidence-schema.md). Preserve the exact query, engine/model, date, locale, observed answer, brand mentions, cited URLs, and collection method.
4. Validate the evidence file:

   ```bash
   python3 scripts/validate_evidence.py path/to/evidence.csv
   ```

5. Score only what the evidence supports. Report:
   - mention rate: runs mentioning the brand / valid runs;
   - citation rate: runs citing a brand-controlled URL / valid runs;
   - competitor share: observed mentions by competitor;
   - source concentration: which third-party sources recur;
   - answer fit: whether the brand is associated with the intended category and claims.
6. Inspect publicly available technical signals when relevant: crawl/index controls, canonicalization, structured data, entity consistency, authorship, update dates, and pages that substantiate important claims.
7. Separate output into **observed**, **inferred**, and **recommended to test**. Never present an inference as measured fact.

## Evidence rules

- Use live observations or user-provided exports. Do not invent model answers, citations, traffic, or ranking positions.
- Record engine/model names exactly as exposed at collection time. Note when model/version is unknown.
- Repeated runs are separate samples. Do not silently select the best answer.
- A brand mention is not automatically a recommendation; label the answer context.
- A link in a browsing interface is a citation only when the answer visibly attributes or links to it.
- Avoid a single composite “GEO score” unless the user supplies a formula. Prefer transparent component metrics.
- Do not promise that a change will cause inclusion, ranking, or citation in an answer engine.

Read [methodology.md](references/methodology.md) when designing a new query set or comparing engines. Use [report-template.md](references/report-template.md) for the final deliverable.

## Required output

Return:

1. scope and collection limitations;
2. query-set summary;
3. visibility and citation matrix;
4. key observed strengths and gaps, each linked to evidence rows;
5. technical discoverability findings;
6. a prioritized handoff for `$geo-brand-optimizer`;
7. a retest recommendation using the same query set and conditions.
