# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

**Status: no complete proof or counterexample has been verified.**

## Current checkpoint: U48 (2026-09-15)

[U48: crossed correspondence and product-domination obstruction](research/U48_crossed_correspondence_and_product_domination.md) constructs an explicit irreducible surface Gamma on S5 x S7 with degree35 projections onto both surfaces. It dominates both base products tested in U47, with degrees70 and50. Nevertheless its missing-block projection is zero. This demonstrates that dominating both bases is not sufficient, rather than merely restating U47's fibrewise obstruction.

The exact transported target in Y4=D5 x C5 x D7 x C7 has character tuple(37,49,33,25) in the specified cyclic generators. None of its six character pairs can contribute a rational divisor class. This excludes all divisor-product classes and, by a proved factorization lemma for maps from products of curves, **every surface in Y4 dominated by a product of two smooth projective curves**, with arbitrary source genera and degrees. This last theorem is scoped to the fixed four-curve cover; it is not automatically an obstruction to product-dominated surfaces downstairs.

The explicit maps D5 -> C7 and D7 -> C5 also provide trace projectors that annihilate the target; the target lies in both complementary Prym parts. **No target-bearing algebraic cycle has been constructed.** These are construction obstructions, not nonalgebraicity or a solution of the Hodge conjecture.

[Proof and self-review](research/U48_crossed_correspondence_and_product_domination.md), [exact checker](research/computations/U48/verify_u48.py), [finite results](research/computations/U48/verification.json), [separate Wolfram input](research/computations/U48/independent_wolfram.wl), [Wolfram output](research/computations/U48/independent_wolfram.json), and [run manifest](research/computations/U48/run_manifest.json).

Eight new tests and nine inherited U47 tests pass. Syntax compilation passes; native ruff and mypy invocations fail because their modules are absent, and their logs are preserved. Separate Wolfram calculations corroborate arithmetic, not the geometric proof. The proof is self-reviewed, not formally verified or independently expert-reviewed.

**Next obligation:** construct an intrinsically non-product-dominated surface in this four-curve cover with nonzero target projection, or an equivalent non-factorizing mixed correspondence on S5 x S7. Generic complete intersections, pairwise divisor constructions, and the crossed quotient maps just tested do not suffice. Do not transport the product-domination obstruction backwards through finite covers without a proof.

## Preserved research

- [U47](research/U47_fibration_support_obstruction.md): fibrewise-support obstructions and explicit fixed-curve covers of the two surfaces.
- [U46: Horikawa surface pair](research/U46_explicit_Horikawa_product_reduction.md): mixed-product transfer to the original degree70 block; distinct from the separately preserved local CM19 U46.
- [U45](research/U45_small_CM_source_certificate.md) and [U44](research/U44_level_stable_parity_and_seed_obstruction.md): small-CM-profile and formal relation-method obstructions.
- [U43](research/U43_full_tensor_block_and_rank_one_reduction.md) and [U42](research/U42_tensor_square_algebraicity.md): algebraic product blocks, not a vector on the original fourfold.
- [U40](research/U40_twist_reconciliation_and_normalization.md) and [U41](research/U41_tensor_and_retract_obstructions.md): arithmetic normalization and restricted factorization obstructions.
- [U39](research/U39_exact_Kummer_subfield_and_abelian_obstruction.md), [U38](research/U38_degree70_field_of_definition_obstruction.md), [U37](research/U37_toric_component_obstruction.md), and [U36](research/U36_U35_uniform_vanishing.md): preserved field and toric obstructions.

All earlier mathematical files remain unchanged. The complete preceding README is preserved in parent commit `2b2032a2c846436b0105ec426147a640db8f721b`; historical claims are not globally revalidated by U48.
