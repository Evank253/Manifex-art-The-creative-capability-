# MANIFEX-CCI-001 Architecture

## Purpose
Keep the inventory/evidence control plane separate from the creative execution plane. The inventory records what exists and what evidence supports it; the runtime later selects registered capabilities through explicit interfaces.

## Logical components

1. **Source catalog** — repository, branch/ref, directory/file, model, service, documentation, and artifact references.
2. **Inventory scanner** — discovers files and metadata without changing source repositories. Initial operation should be read-only.
3. **Capability registry** — validated records with stable IDs, interfaces, dependencies, rights, and lifecycle state.
4. **Rights intelligence** — stores license/terms evidence and flags unknown or restricted items before distribution or use.
5. **Evidence ledger** — connects claims to artifacts, logs, reproductions, reviews, and benchmark runs.
6. **Evaluation harness** — runs declared test fixtures and records environment, metrics, raw output, failures, and reproducibility information.
7. **Report/search layer** — locates capabilities and artifacts and surfaces missing evidence, stale records, duplicates, and unresolved integration work.
8. **Future creative orchestrator** — selects only registered, eligible tools for a task; this is a later milestone, not part of the inventory's current capability.

## Data flow

`Source → Discovery Record → Rights Review → Capability Record → Test Definition → Run Artifacts → Evaluation Record → Verification/Review → Registry Update → Searchable Report`

No stage should overwrite the source material. Derived records should identify their inputs and version.

## Trust boundaries
- External human authority remains outside the software.
- A model output or self-reported flag cannot certify its own correctness.
- Scores do not replace raw artifacts or independent review.
- A capability is not eligible for integration merely because it was discovered.
- Unknown license, unknown benchmark conditions, and missing artifacts remain explicitly unresolved.

## Initial technical direction
Use portable JSON records and a small Python package/CLI first. Avoid committing to one provider or model. Keep adapters behind narrow interfaces so free/local models and optional hosted services can be compared. Any cloud service, model, dataset, or generated asset must carry its own rights and cost notes.
