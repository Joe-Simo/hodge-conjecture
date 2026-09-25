# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

**Status: no complete proof or counterexample has been verified.**

## External claimed proof audit

[U62](research/U62_RSC_v5_secant_intersection_failure.md) audits the August 2026 v5 preprint *Relative Secant Cycles and Hodge Classes*. Its load-bearing RSC cycle is defined using `Sec^n(A^vee) ∩ A^vee`, but the secant variety already contains `A^vee`; the intersection is codimension zero. Appendix E.3 acknowledges this for `n=2` and gives a different degeneracy-locus construction only for that case. Thus the v5 manuscript does not establish its claimed general Hodge theorem. This is a flaw in that proof, not a counterexample to the Hodge conjecture.

## Literature correction: the degree-70 Fermat fourfold is already covered

[U59: Kang's theorem closes the degree-70 Fermat fourfold target](research/U59_kang_closes_degree70_fermat_fourfold.md) records a primary-source check of Kang (2016), Corollary 3.2. It proves the rational Hodge conjecture for every Fermat fourfold `X_m^4`, with no degree restriction. The project's `X_70^4` and its `W_alpha` class are therefore algebraic. This is a solved special case, not a proof of the Clay conjecture for arbitrary smooth projective varieties.

## Preserved construction checkpoint: U55–U58 (2026-09-16)

[U55: p-adic formal K-theory lift and algebraization gap](research/U55_padic_formal_lift_and_algebraization_gap.md) starts from the characteristic-139 supersingular witness and isolates the target in Adams weight 2. Bloch–Esnault–Kerz gives a compatible formal pro-class in rational K-theory through every Witt thickening. The formal-to-algebraic `K_0` map remains a genuine obstacle for this particular lifting construction, but it is not an existence gap for the Hodge class on `X_70^4`: U59 supplies an independent characteristic-zero theorem.

[U56: Hermitian line span and semiregular low-degree witnesses](research/U56_Hermitian_line_span_and_semiregular_conics.md) uses the degree-140 Hermitian cover in characteristic 139. The generalized-quadrangle incidence spectrum proves that its line classes have intersection-matrix rank exactly b2, hence span the full Neron–Severi space. Their square-map images span NS of the degree-70 Fermat surface and are lines or smooth conics. Every such curve is rigid and divisor-semiregular, so there exist low-degree special-fiber curves detecting the beta and gamma directions.

[U57: product semiregularity on the special fiber](research/U57_product_semiregularity_special_fiber.md) proves that for detecting line/conic curves C_beta and C_gamma, the surface C_beta x C_gamma in F x F is codimension-two semiregular. Its Bloch semiregularity map splits as the two injective divisor semiregularity maps tensored with the other curve's nonzero divisor class, landing in distinct Kunneth summands. The verified all-obstruction deformation theorems are characteristic-zero results, so this does not imply a Witt-vector lift.

[U58: explicit detecting conic and first-Witt obstruction](research/U58_explicit_detecting_conic_and_W2_obstruction.md) makes the tension concrete. The Hermitian line

    [s:t] -> [25(s+t):25(-s+t):s:t]

maps to the smooth conic

    y0+y1+y2+y3=0,
    (y0-y1)^2=4 y2 y3

on the degree-70 Fermat surface over F_139. An exact diagonal-incidence Fourier calculation proves that this single conic has nonzero beta and gamma projections. Nevertheless the most general first-order deformation of its quadratic parametrization cannot satisfy the Fermat equation modulo 139^2: the s^136 t^4 and s^134 t^6 correction rows are identical while the divided Fermat defect has coefficients 81 and 88. Thus the conic, and its raw product with itself, fail already over W2.

The exact U58 checker is [research/computations/U58/verify_u58.py](research/computations/U58/verify_u58.py). It reproduces the 19,739 intersecting diagonal translates, nonzero Fourier certificates 134 and 175 modulo 281, and the W2 coefficient obstruction. Python syntax compilation passes locally; ruff and mypy are unavailable, so lint/static-type success is not claimed.

**Status after U59:** U55–U58 still describe a formal lift and a failed embedded lift for specific special-fiber representatives. Kang's theorem means neither construction is needed to establish algebraicity of the degree-70 target class. An explicit cycle matched to U55's special-fiber `K_0` class remains a separate construction question; it is not the remaining step in the Hodge conjecture for this fourfold.

To pursue the full Clay problem, work must now target a broader class of smooth projective varieties or establish a universal reduction to cases already solved. More degree-70 cycles, matrix factorizations, or finite-characteristic witnesses alone cannot close the general conjecture. The other live route is a genuinely non-Koszul/nonseparable matrix factorization with nonzero Favero–Kelly coefficient on x1^19 x2^23 x3^41 x4^60 x5^61. Classical reflection/Davenport–Hasse, torus-coset, fibrewise, product-dominated, and etale-Prym determinant constructions remain excluded by the preserved checkpoints.

## Preserved research

- U51–U54: torus-coset obstruction, exact Horikawa/order-two identification, characteristic-139 supersingular witness, and rigidity of visible order-70 symmetry loci.
- [U49](research/U49_etale_Prym_determinant_redundancy.md): etale abelian Fermat-cover determinant seeds reduce to reflection words.
- [U48](research/U48_crossed_correspondence_and_product_domination.md): crossed degree35 correspondence and product-domination obstruction in the fixed four-curve cover.
- [U47](research/U47_fibration_support_obstruction.md) and [U46](research/U46_explicit_Horikawa_product_reduction.md): fixed-curve covers and the explicit Horikawa mixed-product reduction.
- U42–U45: algebraic tensor-square/product blocks, rational rank-one reduction, and the formal all-level/small-CM obstructions.
- Earlier arithmetic, Delsarte, toric and factorization records remain preserved with their original scopes.

Historical claims outside the cited dependency chain are not globally revalidated by this checkpoint.
