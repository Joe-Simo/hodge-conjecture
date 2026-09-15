# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

**Status: no complete proof or counterexample has been verified.**

## Current checkpoint: U47 (2026-09-15)

[U47: pencil-supported correspondences vanish; explicit fixed-curve covers](research/U47_fibration_support_obstruction.md) continues the concrete Horikawa surface pair in the remote U46. It proves that the generic Jacobians of their canonical genus-two pencils have no homomorphisms after any finite base change: one becomes a fixed simple Jacobian, while the other retains a nonzero nodal monodromy operator. The Picard/Jacobian comparison and a spreading argument then rule out every surface correspondence supported over a curve in the product of the two pencil bases.

An executed alternative gives explicit degree-10 and degree-14 rational covers D5 x C5 -> S5 and D7 x C7 -> S7, with genera (31,2) and (32,3). The second uses a different, isotrivial genus-three pencil. Its simple constant Jacobian is not isogenous to that of C5, so the analogous base-curve-supported construction also vanishes. The new cover maps transport the missing mixed block to a specified subspace of H^1(D5) tensor H^1(C5) tensor H^1(D7) tensor H^1(C7), with inverse on the image supplied by normalized pushforward.

**No target-bearing cycle has been constructed.** A contributing surface must dominate the two-dimensional base product for each tested pencil pair, not merely match fibres along a base curve. These are support obstructions and explicit reductions, not nonalgebraicity or a solution of the Hodge conjecture.

[Exact checker](research/computations/U47/verify_u47.py), [finite results](research/computations/U47/verification.json), [separate Wolfram input](research/computations/U47/independent_wolfram.wl), [Wolfram output](research/computations/U47/independent_wolfram.json), and [validation record](research/computations/U47/validation_status.json). The proof includes the source applications and adversarial self-review.

Nine new tests and eight inherited tests for the **distinct supplied local CM19 U46** pass. The latter are not a rerun of this repository's Horikawa U46 checker. Syntax compilation passes; native ruff and mypy invocations fail because their modules are absent. Arithmetic agreement does not verify the geometric proof; that proof is self-reviewed, not formally or independently expert-verified.

**Next obligation:** construct an actual nonambient codimension-two cycle in the four-fixed-curve source image, or a mixed surface correspondence dominating both base parameters. Do not revisit merely fibrewise Picard correspondences. The local CM19 U46 record and its evidence archive remain preserved separately; neither historical U46 route was overwritten or silently merged.

## Preserved research

- [U46: explicit Horikawa surfaces](research/U46_explicit_Horikawa_product_reduction.md): the exact mixed-product transfer and the two self-product results used here.
- [U45](research/U45_small_CM_source_certificate.md): the small-CM-profile formal obstruction and dimension-twelve boundary.
- [U44](research/U44_level_stable_parity_and_seed_obstruction.md): the all-level reflection/multiplication and augmented-seed obstruction.
- [U43](research/U43_full_tensor_block_and_rank_one_reduction.md) and [U42](research/U42_tensor_square_algebraicity.md): algebraic product blocks, not a vector on the original fourfold.
- [U40](research/U40_twist_reconciliation_and_normalization.md) and [U41](research/U41_tensor_and_retract_obstructions.md): arithmetic normalization and restricted factorization obstructions.
- [U39](research/U39_exact_Kummer_subfield_and_abelian_obstruction.md), [U38](research/U38_degree70_field_of_definition_obstruction.md), [U37](research/U37_toric_component_obstruction.md), and [U36](research/U36_U35_uniform_vanishing.md): preserved field and toric obstructions.

All earlier mathematical files remain unchanged. The full preceding README is preserved at parent commit `50cbb2c7839121abc193f57ced6e880ed4e4a23b`; historical claims are not globally revalidated by U47.
