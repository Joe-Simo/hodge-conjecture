# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

**Status: no complete proof or counterexample has been verified.**

## Current checkpoint: U51–U54 (2026-09-16)

[U51: torus-coset surface obstruction](research/U51_torus_coset_surface_obstruction.md) proves that every two-dimensional torus translate contained in the degree-70 Fermat fourfold must be of three-pair type, and an exhaustive check of all 15 pairings shows that none can have nonzero projection to the target character alpha=(1,20,24,42,61,62). This closes the entire torus-coset/binomial complete-intersection family, not arbitrary non-toric surfaces.

[U52: Horikawa mixed class equals the same order-two obstruction](research/U52_Horikawa_mixed_class_same_order2_obstruction.md) corrects the duality sign in the U46 mixed-product comparison. The missing map is M_{-beta}->M_gamma. Its normalized formal word Delta differs from the original fourfold target word by exactly -R(1)-R(8)-R(28). In the full level-70 reflection/Davenport-Hasse relation lattice, both are the same nonzero generator of the unique Z/2 torsion subgroup. Thus U42's parity obstruction, U43's rank-one motive, U46's mixed Horikawa correspondence, and the squared Jacobi-sum arithmetic are the same unresolved order-two class.

[U53: supersingular characteristic-139 witness](research/U53_supersingular_special_fiber_witness.md) gives a positive special-fiber result. Since 139=-1 mod70, Shioda-Katsura supersingularity makes the degree-70 Fermat surface and fourfold fully algebraic in even cohomology over the algebraic closure of F_139. The U46 quotient surfaces consequently have Picard rank 33 in the special fiber, so the missing mixed block is represented there by products of divisors. Those divisor directions do not lift individually to characteristic zero, where R5 and R7 are transcendental; the remaining problem is a genuinely coupled lift.

[U54: rigidity of the visible order-70 symmetry loci](research/U54_order70_symmetry_fixed_rigidity.md) classifies all weighted-degree-10 monomials with the required semi-invariant character for the two Horikawa models. Each symmetry-preserving linear system consists only of the four monomials already present, and diagonal coordinate rescaling removes their coefficients. Hence both models are isolated in their specified order-70 symmetry loci. Any variational-Hodge route must break that visible symmetry.

The newest external checks also confirm that Favero-Kelly's September 2026 Chern-character formula gives an effective matrix-factorization target, while the September 2026 semiregularity preprint independently singles out the same degree-70 orbit as the remaining Fermat-fourfold case after its tested constructions. Neither source supplies the missing cycle.

**Next obligation:** construct one odd algebraic relation beyond the classical reflection/multiplication lattice. The strongest surviving routes are (1) a coupled characteristic-zero lift of the p=139 supersingular divisor-product witness, likely via semiregularity/perfect-complex deformation; (2) a genuinely non-toric complete intersection or nonseparable matrix factorization with nonzero Favero-Kelly target coefficient; or (3) a symmetry-breaking mixed correspondence on S5 x S7. Do not restart torus-coset, fibrewise, product-dominated, etale-Prym-determinant, or pure reflection/Davenport-Hasse searches already excluded by U47-U54.

## Preserved research

- [U49](research/U49_etale_Prym_determinant_redundancy.md): etale abelian Fermat-cover determinant seeds reduce to reflection words.
- [U48](research/U48_crossed_correspondence_and_product_domination.md): crossed degree35 correspondence and product-domination obstruction in the fixed four-curve cover.
- [U47](research/U47_fibration_support_obstruction.md) and [U46](research/U46_explicit_Horikawa_product_reduction.md): fixed-curve covers and the explicit Horikawa mixed-product reduction.
- [U45](research/U45_small_CM_source_certificate.md) and [U44](research/U44_level_stable_parity_and_seed_obstruction.md): small-CM-profile and formal all-level obstructions.
- [U43](research/U43_full_tensor_block_and_rank_one_reduction.md) and [U42](research/U42_tensor_square_algebraicity.md): algebraic product blocks, not a vector on the original fourfold.
- Earlier arithmetic, toric and factorization records remain preserved with their original scopes.

Historical claims outside the cited dependency chain are not globally revalidated by this checkpoint.
