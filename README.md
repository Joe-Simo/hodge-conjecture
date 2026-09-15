# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

**Status: no complete proof or counterexample has been verified.**

## Current checkpoint: U45 (2026-09-15)

[U45: small-profile CM source certificate](research/U45_small_CM_source_certificate.md) tests a new algebraic-source route motivated by low-dimensional abelian-variety results. At level420 it proves a five-unit parity identity for all1,152 curve triples whose primitive CM-profile dimension is at most8. This implies that every Hodge-balanced tensor word from those profiles, with arbitrary length and signed cancellation, has zero value under U44's functional.

Even granting all those Hodge words as new relations, the target remains of exact order two in the resulting **formal** quotient. This is not nonalgebraicity and is not a restriction on arbitrary geometric correspondences. The limitation is sharp in the tested palette: an explicit four-curve Hodge word with profile dimensions(12,3,2,12) has odd parity and is the original target modulo three reflection relations, but its algebraicity has not been proved.

[Proof](research/U45_small_CM_source_certificate.md), [standalone exact checker](research/computations/U45/verify_u45.py), [finite output](research/computations/U45/verification.json), [independent Wolfram input](research/computations/U45/independent_wolfram.wl), [Wolfram output](research/computations/U45/independent_wolfram.json), [source and self-review](research/computations/U45/source_and_self_review.md), and [run summary](research/computations/U45/run_summary.json).

Seven new tests and27 inherited U42-U44 tests pass. Syntax compilation passes. Native ruff and mypy invocations fail because the modules are unavailable; no lint or static-type-check success is claimed. The proof is self-reviewed, not formally verified or independently expert-reviewed. The full local evidence archive additionally preserves actual logs, discovery code, and the corrected failed expectation.

**Next obligation:** find an independently algebraic odd input involving a larger/new CM type with a justified transport, or construct a surface-supported correspondence giving a nonzero realized L^2 -> N. Merely increasing tensor length among the small profiles is excluded uniformly. No target-bearing surface on the original X has been constructed.

## Preserved research

- [U44](research/U44_level_stable_parity_and_seed_obstruction.md): all-level reflection/multiplication obstruction and the level420 augmented-seed theorem.
- [U43](research/U43_full_tensor_block_and_rank_one_reduction.md): the576-dimensional algebraic product block and rank-one motive reduction; this is not a vector on X.
- [U42](research/U42_tensor_square_algebraicity.md): diagonal tensor-square construction and its scope.
- [U40](research/U40_twist_reconciliation_and_normalization.md) and [U41](research/U41_tensor_and_retract_obstructions.md): arithmetic normalization, proper tensor products, and raw-retract limitations.
- [U39](research/U39_exact_Kummer_subfield_and_abelian_obstruction.md), [U38](research/U38_degree70_field_of_definition_obstruction.md), [U37](research/U37_toric_component_obstruction.md), and [U36](research/U36_U35_uniform_vanishing.md): preserved field, toric-component, and uniform family obstructions.

The complete previous README is preserved in parent commit `bfdb70edaae96b5ec0aaef8782ab3baffd448826`. Earlier mathematical notes were not modified or globally revalidated by U45.
