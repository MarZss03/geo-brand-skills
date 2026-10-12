---
name: geo-brand-optimizer
description: Turn a GEO or AI-visibility audit into an evidence-linked optimization backlog covering content, entity clarity, technical discoverability, and authority signals, with measurable retest criteria. Use when a user wants to improve brand inclusion or citations in AI answers after an audit or evidence collection. Do not use to guarantee rankings, fabricate authority, or replace measurement with generic SEO advice.
---

# GEO Brand Optimizer

Convert observed gaps into concrete, testable work while preserving the audit's uncertainty and evidence trail.

## Inputs

Prefer a validated evidence file and audit report from `$geo-brand-audit`. If neither exists, build a lightweight baseline first; do not optimize from assumptions alone.

## Workflow

1. Normalize each finding into the fields in [action-schema.md](references/action-schema.md): evidence IDs, problem, hypothesis, action, owner, effort, expected signal, measurement, and retest window.
2. Classify work into:
   - **Answer fit**: clear category, audience, use cases, differentiators, limitations, and comparisons;
   - **Evidence depth**: original data, methodology, examples, author credentials, dates, and claim support;
   - **Entity clarity**: consistent brand/product/person naming and relationships;
   - **Technical access**: crawlability, indexability, canonical URLs, renderability, metadata, and structured data;
   - **External authority**: accurate independent references and community validation, never manufactured endorsements.
3. Prioritize with a transparent score:

   `priority = evidence_strength × expected_impact × confidence ÷ effort`

   Use 1–5 integers for each factor, keep the raw factors visible, and treat the score as a sorting aid rather than truth.
4. Generate a Markdown backlog when the findings are in JSON:

   ```bash
   python3 scripts/build_backlog.py findings.json --output geo-backlog.md
   ```

5. Draft or change content only when authorized. Tie every material claim to a source and avoid keyword stuffing, doorway pages, hidden text, fake reviews, or fabricated citations.
6. Define the retest before implementation. Follow [retest-protocol.md](references/retest-protocol.md) so baseline and follow-up remain comparable.

## Decision rules

- Fix access and factual clarity before producing more pages.
- Prefer one strong, citable source page over many near-duplicate pages.
- Optimize for useful, verifiable answers to real questions—not for model manipulation.
- Preserve brand voice and disclose tradeoffs or eligibility limits that change the answer.
- Label expected effects as hypotheses until a comparable retest observes them.
- Treat model behavior as variable; do not guarantee inclusion, position, citation, or traffic.

## Required output

Return:

1. prioritized backlog with evidence links and raw scoring factors;
2. quick wins, structural work, and experiments separated;
3. exact page or system targets;
4. acceptance criteria for every action;
5. comparable retest plan and decision thresholds;
6. risks, dependencies, and claims that still need verification.
