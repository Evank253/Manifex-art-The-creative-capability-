# Evidence Policy

## Evidence classes
- **Claim:** a statement awaiting corroboration.
- **Artifact:** a file, output, model card, source reference, configuration, or report.
- **Runtime log:** a trace from an identified run and environment.
- **Reproduction:** a repeat execution with recorded inputs and versions.
- **Independent review:** a review performed outside the implementation path.
- **Benchmark:** a measurement tied to a declared protocol and raw results.
- **License review:** terms and rights assessment tied to a specific version/source.

## Required metadata
Every material evidence item should include a stable ID, type, source, timestamp when known, artifact URI/path, content hash where feasible, status, and notes describing limitations.

## Status discipline
- `UNVERIFIED`: evidence exists but has not been independently checked.
- `VERIFIED`: the specified check passed; this is scoped to the exact artifact and check.
- `DISPUTED`: conflicting evidence or a reproducible concern exists.
- `NOT_MEASURED`: the measurement has not been run.
- `UNRESOLVED`: attempted investigation did not settle the question.

Do not infer a pass from a missing result. Preserve historical values as historical claims unless the raw supporting evidence is available and reviewed.
