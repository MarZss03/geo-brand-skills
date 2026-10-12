# Action schema

The backlog builder accepts a JSON array. Each object requires:

- `id`: stable action ID;
- `title`: concise action name;
- `evidence_ids`: array of audit evidence IDs;
- `problem`: observed gap;
- `hypothesis`: why the action may improve a measured signal;
- `action`: concrete implementation;
- `owner`: responsible role;
- `effort`, `expected_impact`, `confidence`, `evidence_strength`: integers from 1 to 5;
- `expected_signal`: observable result;
- `measurement`: how to measure it;
- `retest_window`: when or under what condition to retest.

Optional: `target`, `dependencies`, `risks`, `acceptance_criteria`, and `category`.
