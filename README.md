# GEO Brand Skills

Two open-source Codex skills for measuring and improving how brands appear in generative and AI answer engines.

- [`geo-brand-audit`](skills/geo-brand-audit): creates a reproducible, evidence-backed visibility and citation baseline.
- [`geo-brand-optimizer`](skills/geo-brand-optimizer): turns audit findings into a prioritized, measurable backlog and retest plan.

The project deliberately avoids universal “GEO scores” and ranking guarantees. Model answers vary; every claim should remain tied to dated evidence.

## Install

Clone this repository, then copy either or both skill directories into your Codex skills folder:

```bash
git clone https://github.com/MarZss03/geo-brand-skills.git
mkdir -p ~/.codex/skills
cp -R geo-brand-skills/skills/geo-brand-audit ~/.codex/skills/
cp -R geo-brand-skills/skills/geo-brand-optimizer ~/.codex/skills/
```

Restart Codex if the new skills do not appear immediately. Invoke them as `$geo-brand-audit` and `$geo-brand-optimizer`.

## Try it

```text
Use $geo-brand-audit to design and run a reproducible audit of Example Brand's visibility in AI answer engines for English-speaking Canadian buyers.
```

```text
Use $geo-brand-optimizer to turn this audit dataset into an evidence-linked backlog and comparable retest plan.
```

Each skill contains references, sample inputs, and a dependency-free Python utility. Validate the included examples with:

```bash
python3 skills/geo-brand-audit/scripts/validate_evidence.py skills/geo-brand-audit/examples/sample-evidence.csv
python3 skills/geo-brand-optimizer/scripts/build_backlog.py skills/geo-brand-optimizer/examples/sample-findings.json
```

## Principles

- Observations before recommendations.
- Exact queries, dates, models, locales, and source URLs stay in the evidence trail.
- Transparent component metrics instead of opaque scoring.
- Useful, verifiable brand information instead of model manipulation.
- Comparable retests instead of outcome promises.

## Contributing

Bug reports, methodology critiques, examples, and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT © Martin / MarZss03. See [LICENSE](LICENSE).
