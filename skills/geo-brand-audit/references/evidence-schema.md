# Evidence schema

Use CSV or JSONL. Required fields:

| Field | Meaning |
| --- | --- |
| `evidence_id` | Stable unique ID such as `E001` |
| `observed_at` | ISO 8601 date or timestamp |
| `engine` | Product or answer engine name |
| `model` | Exposed model/version, or `unknown` |
| `locale` | Language-region code such as `en-CA` |
| `query` | Exact prompt or query |
| `intent` | `category`, `problem`, `comparison`, or `branded` |
| `brand_mentioned` | `true` or `false` |
| `brand_cited` | `true` or `false` |
| `answer_excerpt` | Short evidence-bearing excerpt or faithful summary |
| `cited_urls` | Pipe-separated URLs in CSV; JSON array or string in JSONL |
| `collection_method` | Manual, browser export, API, or user-provided |

Optional fields: `run_id`, `competitors_mentioned`, `answer_context`, `notes`, and `screenshot_path`.

Do not store secrets, session cookies, private prompts, or personal data that is unnecessary for the audit.
