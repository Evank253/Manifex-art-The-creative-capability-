# MANIFEX Creative Capability Inventory (MANIFEX-CCI-001)

> **Master hub and evidence-driven reconstruction program for the MANIFEX creative powerhouse.**

MANIFEX-CCI-001 is the inventory, research, evidence, and qualification layer for building a unified, free-to-use creative production platform. The intended platform brings together music generation, vocals, audio production, mixing/mastering, video, graphics, animation/3D, and editing through modular capabilities rather than one monolithic model.

This repository is the **working implementation**. Existing investigation repositories and frozen originals remain separate and must not be edited or overwritten by this project.

## Mission

Build a capability-driven creative system that can:

- Discover and inventory relevant repositories, files, services, models, tools, and documented capabilities.
- Track mechanisms, interfaces, dependencies, constraints, licensing, model/data provenance, and operational requirements.
- Reconstruct capabilities independently from lawful, observable behavior and available documentation—not copy protected source code, weights, private data, or restricted assets.
- Benchmark components with reproducible tasks, declared environments, baseline comparisons, and stored raw results.
- Route a request only to registered, eligible capabilities; avoid activating an entire toolbox for a single task.
- Compose capabilities into end-to-end workflows, beginning with **full-song generation and audio production**.
- Export auditable reports so missing files, unverified claims, failed tests, and unresolved integration gaps can be found from this hub.

## Non-negotiable evidence rules

1. **A claim is not proof.** Keep claims, artifacts, execution logs, reproduced results, independent reviews, and cross-environment results distinct.
2. **Unknown stays unknown.** Use `NOT_MEASURED`, `NOT_TESTED`, `UNRESOLVED`, or `NOT_APPLICABLE` explicitly; never silently convert missing evidence into a pass.
3. **No fabricated scores.** Every benchmark score must identify the test, dataset or fixture, version, environment, timestamp, method, raw artifact, and calculation.
4. **Provenance first.** Track repository URL and ref, path, content hash where available, acquisition date, license/terms, dependencies, and evidence links.
5. **Frozen sources stay frozen.** This repo indexes and references source projects; it does not rewrite their historical records or canonical files.
6. **Human authority stays external.** Software may enforce delegated permissions and record human decisions; it cannot become, replace, or self-authorize human authority.
7. **Capability is not qualification.** A discovered feature is not considered verified, production-ready, or safe merely because it exists.
8. **Free-to-use is a product goal, not a licensing shortcut.** The platform must disclose service limits, attribution requirements, model licenses, and any cost-bearing external dependency.

## Initial scope

### Phase 1 — Inventory and evidence foundation
- Repository and artifact manifest.
- Capability record schema and registry.
- Evidence ledger and immutable artifact references.
- License and dependency tracking.
- Test/benchmark record format.
- Searchable reports for missing, stale, conflicting, or unverified information.

### Phase 2 — Music production capability map
Inventory and evaluate:
- Text/prompt-to-music and full-song generation.
- Lyrics, arrangement, structure, and genre control.
- Vocal synthesis, voice conversion, and vocal separation (with consent and rights safeguards).
- Stem separation, source isolation, transcription, and MIDI extraction.
- Audio editing, effects, synthesis, sampling, and sound design.
- Mixing, loudness analysis, mastering, and export.
- Timing, latency, quality, reproducibility, hardware, and runtime costs.

### Phase 3 — Creative workflow orchestration
- Register capabilities through stable, versioned interfaces.
- Plan multi-step workflows from user intent.
- Invoke only the tools required for a task.
- Preserve input/output provenance across each stage.
- Support retries, cancellation, partial output, and clear failure reporting.

### Phase 4 — Cross-media expansion
Add video generation/editing, graphics and cover art, animation/3D, and broader creative tools only after each capability has an inventory record, rights review, measurable evaluation plan, and integration contract.

## Registry model

Each capability should record, at minimum:

| Field | Purpose |
|---|---|
| Capability ID / name | Stable identity and human-readable label |
| Category / task | What the component does |
| Source repository / URL / ref | Where it was discovered |
| Paths / artifacts / hashes | How to locate and identify relevant material |
| Mechanism summary | Observed or documented mechanism, separated from inference |
| Interface / inputs / outputs | Integration contract and data formats |
| Dependencies / runtime | Libraries, models, services, hardware, and version constraints |
| License / terms / restrictions | Use, distribution, attribution, and commercial limitations |
| Test suite / benchmark | Reproducible evaluation definition |
| Results / raw evidence | Scores, logs, fixtures, environment, and artifact references |
| Status | Discovery, implementation, test, qualification, and integration states |
| Gaps / risks / next action | What remains unknown or must be done next |
| Provenance / timestamps | Source and record history |

## Evidence and status vocabulary

Use separate fields rather than one blended trust score.

- **Discovery:** `UNREVIEWED`, `INVENTORIED`, `DUPLICATE_CANDIDATE`
- **Implementation:** `NOT_STARTED`, `PROTOTYPE`, `IMPLEMENTED`
- **Testing:** `NOT_TESTED`, `PASS`, `FAIL`, `PARTIAL`
- **Measurement:** `NOT_MEASURED`, `MEASURED`, `UNRESOLVED`
- **Rights:** `UNKNOWN`, `REVIEW_REQUIRED`, `CLEARED`, `RESTRICTED`
- **Integration:** `NOT_INTEGRATED`, `INTEGRATION_REQUIRED`, `INTEGRATED`

A status applies only to the exact artifact/version and test conditions recorded.

## Repository layout (target)

```text
MANIFEX-CCI-001/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── evidence-policy.md
│   └── benchmark-protocol.md
├── schemas/
│   ├── capability-record.schema.json
│   └── benchmark-record.schema.json
├── registry/
│   ├── repositories.json
│   └── capabilities.json
├── evidence/
│   ├── manifests/
│   └── reports/
├── src/
│   └── manifex_cci/
├── tests/
└── pyproject.toml
```

This is a target structure, not a claim that every component has already been implemented.

## Operating workflow

`Discover → Acquire/Reference → Inventory → Classify → Rights Review → Extract Observable Behavior → Reconstruct → Test → Benchmark → Verify → Register → Integrate → Monitor`

Every transition should leave a traceable record. A component can remain useful while still being marked unverified or not measured.

## First milestone and acceptance criteria

**Milestone CCI-001-A: Music capability inventory foundation**

- [ ] Repository and artifact records can be stored in a machine-readable format.
- [ ] Capability records validate against a versioned schema.
- [ ] Every record supports source/ref/path and provenance metadata.
- [ ] Evidence and benchmark records can be linked without embedding unsupported scores.
- [ ] Search/report output identifies missing required fields and unresolved statuses.
- [ ] Automated tests cover valid records, malformed records, missing provenance, and unknown measurements.
- [ ] No frozen source repository is modified by inventory operations.
- [ ] Full-song generation/audio production is the first evaluated capability family.

## How to contribute a capability

1. Create a unique capability ID.
2. Link the exact repository, version/ref, file paths, and relevant artifacts.
3. Record what is directly observed separately from hypotheses or inferred mechanisms.
4. Document license, terms, attribution, data handling, and service requirements.
5. Define a repeatable evaluation with inputs, expected outputs, metrics, and failure conditions.
6. Attach raw results and environment details; do not enter a score without its supporting evidence.
7. Record limitations, unresolved questions, and the next action.
8. Re-run affected tests whenever the implementation, model, dependency, or environment changes.

## Project boundary

MANIFEX-CCI-001 is the **master inventory and evidence program**, not itself a music model and not proof that any external capability has been reproduced. Integration claims will be made only after implementation and tests support them.

- Working branch: `work/manifex-cci-001`
- Initial anchor branch: `Python-3`
- Frozen investigation sources: reference-only unless a separate, explicitly authorized workflow says otherwise.
