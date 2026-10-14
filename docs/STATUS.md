# MANIFEX-CCI-001 — Milestone Status

**Status: IN PROGRESS — NOT QUALIFIED**

## Scope
Build an auditable creative-capability inventory. First investigation target: full-song generation and audio production. Catalog domains: beat-making, vocals, mixing, mastering, video, graphics, animation, and 3D.

## Evidence rules
- DOCUMENTATION records what a source says; it is not proof of runtime behavior.
- DIRECT_OBSERVATION records observed behavior and environment.
- REPRODUCIBLE_TEST records repeatable tests and retained results.
- INDEPENDENT_REVIEW records a reviewer independent of implementation.
- INFERENCE is interpretation, never silently upgraded to observation or verification.
- Missing, unknown, or untested information remains NOT_MEASURED.
- Code licenses, model-weight licenses, dataset terms, output rights, and hosted-service terms are separate records.
- Benchmarks should record hardware, software versions, workload, duration, quality metrics, outcome, and artifact provenance.

## Acceptance gates
1. Package and CLI work in a clean Python 3.11+ environment.
2. Automated tests pass.
3. Invalid domains, evidence categories, and license areas are rejected.
4. Reports include provenance, dependencies, evidence, licenses, benchmarks, and unknowns.
5. Source/version and licensing findings cite exact source URLs and retrieval dates.
6. No capability is called implemented, reproducible, or independently verified without evidence.
7. A reviewer can reproduce results from repository instructions.

## Known limitations
- Local SQLite only; no external services contacted.
- No third-party tool has yet been tested or independently verified.
- No automated test execution or CI result has yet been recorded.
- Source version is mandatory; NOT_MEASURED is permitted when unknown.

## Next investigation packet
For each candidate, record provider/product, exact documentation URL, retrieval timestamp, product/model version, access method, input/output constraints, commercial terms, model/data terms, test conditions, test input, output artifact hash, repeatability, and open questions. Keep claims separate from observations.
