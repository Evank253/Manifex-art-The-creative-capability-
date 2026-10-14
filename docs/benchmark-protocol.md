# Benchmark Protocol

Every benchmark definition must state:

- Benchmark ID and version.
- Capability and implementation version under test.
- Purpose, task scope, and known exclusions.
- Input fixture/dataset identity, provenance, license, and hash.
- Baseline(s), where meaningful.
- Metrics, units, scoring method, and aggregation method.
- Hardware, operating system, runtime, dependencies, model/provider versions, and network conditions.
- Number of trials, seeds/randomness controls, warm-up, timeouts, and failure handling.
- Raw outputs, logs, timing data, and error artifacts.
- Known confounders and reproducibility instructions.

## Music-specific initial metrics
Use task-appropriate metrics rather than collapsing all quality into one score:
- Prompt/brief adherence (documented rubric and, where possible, blinded evaluation).
- Song structure completeness and duration.
- Audio integrity: clipping, silence, sample rate, channel count, and export validity.
- Vocal intelligibility and artifact review where vocals are included.
- Stem availability/separation quality where relevant.
- Latency, success rate, timeout rate, and repeatability.
- Rights/terms status and any external service cost.

Subjective ratings must include the rubric, evaluator count, and disagreement information. Do not compare scores across incompatible datasets or protocols without an explicit qualification.
