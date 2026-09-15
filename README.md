# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

**Status: no complete proof or counterexample has been verified.**

## Current checkpoint: U49 (2026-09-15)

[U49: etale Prym determinant redundancy](research/U49_etale_Prym_determinant_redundancy.md) tests a new algebraic-source route: full determinant classes from finite abelian etale covers with a classical Fermat curve upstairs. It classifies the free actions, including non-diagonal C3 and C3 x C3 actions, and proves at every degree that every such normalized determinant word is an integral sum of reflection relations alone. Thus these inputs do not enlarge the existing reflection/multiplication method; this is not an obstruction to arbitrary Prym cycles or new geometric transport.

The natural cyclic actions on U47's four fixed source curves are also checked directly: each fixes the unique point over infinity in its cyclic presentation, so none of their nontrivial subgroups gives an etale quotient. Ramified/generalized-Prym extensions of the source theorem are not assumed.

No target-bearing algebraic surface has been constructed. U49 does not change U48's geometric obstruction or turn the known tensor-square classes into a class on the original fourfold.

[Exact checker](research/computations/U49/verify_u49.py), [finite output](research/computations/U49/verification.json), [independent Wolfram input](research/computations/U49/independent_wolfram.wl), [projector/ramification input](research/computations/U49/independent_wolfram_projectors.wl), [Wolfram output](research/computations/U49/independent_wolfram.json), [source audit and self-review](research/computations/U49/source_and_self_review.md), and [run manifest](research/computations/U49/run_manifest.json).

Ten new tests and eight inherited U42 tests pass. Exact Python checks cover 16296 parameter/character cases over41 degrees; Wolfram separately verifies1228 diagonal cases, non-diagonal formulas at seven degrees, cyclic projectors and the four ramification lists. Preliminary Wolfram syntax/iterator errors were corrected and not counted as evidence. Syntax compilation passes; ruff and mypy are absent, so lint and static type checking remain unperformed. The mathematical proof is self-reviewed, not formally or independently expert-verified. The primary-source audit explicitly distinguishes two problematic auxiliary formulas in the Prym preprint from the limited theorem and the independent reflection argument used here.

**Next obligation:** obtain an independently algebraic input outside the tested relation subgroup with a justified transport, or construct a genuinely coupled surface correspondence on the U46 mixed product. Do not repeat deeper combinations of the full Fermat-cover determinant seeds excluded uniformly by U49.

## Preserved research

- [U48](research/U48_crossed_correspondence_and_product_domination.md): crossed degree35 correspondence and product-domination obstruction in the fixed four-curve cover.
- [U47](research/U47_fibration_support_obstruction.md) and [U46](research/U46_explicit_Horikawa_product_reduction.md): fixed-curve covers and the explicit Horikawa mixed-product reduction.
- [U45](research/U45_small_CM_source_certificate.md) and [U44](research/U44_level_stable_parity_and_seed_obstruction.md): small-CM-profile and formal all-level obstructions.
- [U43](research/U43_full_tensor_block_and_rank_one_reduction.md) and [U42](research/U42_tensor_square_algebraicity.md): algebraic product blocks, not a vector on the original fourfold.
- Earlier arithmetic, toric and factorization records remain preserved with their original scopes.

All earlier mathematical files remain unchanged. The complete previous remote README is preserved at cd4ba6bd38ce1b86d41ced84322b6b1b021282d9. Historical claims are not globally revalidated by U49.
