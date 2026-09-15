# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

**Status: no complete proof or counterexample has been verified.**

## Current checkpoint: U46 (2026-09-15)

[U46: explicit Horikawa surfaces and the remaining mixed-product correspondence](research/U46_explicit_Horikawa_product_reduction.md) continues U45's dimension-12 boundary by replacing its abstract surface Hodge profiles with explicit canonical models in P(1,1,2,5):

    S5_bar: Z^2+Y^5+X^9 T+X^2 T^8=0,
    S7_bar: Z^2+Y^5+X^7 Y T+T^10=0.

Their minimal resolutions have K^2=1, p_g=2, q=0, b2=33 and Picard numbers5 and3. The quotient maps from the Fermat surface, all projective singularity charts, and the full transcendental character decomposition are explicit. The rank24 (1,22,1) profiles themselves were already noted in U42; that rediscovery is not counted as new.

All codimension-two rational Hodge classes on each self-product are algebraic: the two spaces have dimensions55 and41. On the mixed product there are41 Hodge dimensions, of which17 are supplied by points and divisors. The remaining24-dimensional block is equivalent, by algebraic correspondences preserving degree, to the original degree70 block W. **The mixed correspondence has not been constructed, and W remains unresolved.**

The surfaces are not birational. Their simple rank24 Hodge pieces cannot factor through H^2 of an actual K3 surface, so a theorem for K3 Hodge isometries cannot be applied just from similar Hodge numbers. An abstract Hodge isomorphism is not promoted to an algebraic correspondence.

[Standalone exact checker](research/computations/U46/verify_u46.py), [finite output](research/computations/U46/verification.json), [separate Wolfram input](research/computations/U46/independent_wolfram.wl), [Wolfram output](research/computations/U46/independent_wolfram.json), [source/application audit and self-review](research/computations/U46/source_and_self_review.md), and [run manifest](research/computations/U46/run_manifest.json).

Ten new tests and25 inherited U42/U43/U45 tests pass. Syntax compilation passes; ruff and mypy are unavailable and their failed invocations are preserved. Mathematical proofs are self-reviewed, not formally or independently expert-verified. The exact arithmetic does not itself prove the geometric comparison or the missing cycle's existence. The original J-STAGE PDF could not be re-fetched this run; the pinned source is distinguished from the freshly read modern primary source and the displayed direct map.

**Next obligation:** construct one algebraic codimension-two cycle on S5 x S7 with nonzero R5 tensor R7 projection, for example a genuinely coupled correspondence between the explicit genus-two pencils. Ordinary divisor intersections lie in the known17-dimensional part and do not suffice. The surfaces being defined over Q does not ensure a contributing cycle has rational or cyclotomic coefficients.

## Preserved research

- [U45](research/U45_small_CM_source_certificate.md): the small-CM-profile formal obstruction and the dimension12 boundary used here.
- [U44](research/U44_level_stable_parity_and_seed_obstruction.md): all-level reflection/multiplication obstruction and the level420 augmented-seed theorem.
- [U43](research/U43_full_tensor_block_and_rank_one_reduction.md): the576-dimensional algebraic product block and rank-one motive reduction, not a vector on X.
- [U42](research/U42_tensor_square_algebraicity.md): diagonal tensor-square construction and earlier surface profiles.
- [U40](research/U40_twist_reconciliation_and_normalization.md) and [U41](research/U41_tensor_and_retract_obstructions.md): arithmetic normalization and restricted factorization obstructions.
- [U39](research/U39_exact_Kummer_subfield_and_abelian_obstruction.md), [U38](research/U38_degree70_field_of_definition_obstruction.md), [U37](research/U37_toric_component_obstruction.md), and [U36](research/U36_U35_uniform_vanishing.md): preserved field and toric obstructions.

All earlier mathematical files remain unchanged. The prior README is preserved in parent commit `8fff2a01be0453fc613c0776239085816c155fdd`; historical claims are not globally revalidated by this checkpoint.
