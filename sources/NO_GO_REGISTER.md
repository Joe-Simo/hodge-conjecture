# No-Go Register: Hodge Conjecture

Authoritative register of disproved conjectures, refuted frameworks, and structural barriers for the Hodge Conjecture.

---

## 1. Disproved Conjectures & Historical Traps

### 1.1 Integral Hodge Conjecture Refutation (Atiyah & Hirzebruch, 1962; Kollár, 1992)
- **Claim**: Every integral Hodge class in $H^{2k}(X, \mathbb{Z}) \cap H^{k,k}(X)$ is the fundamental class of an algebraic cycle with integer coefficients.
- **Refutation**: Atiyah and Hirzebruch (1962) constructed smooth projective varieties where torsion classes in $H^{2k}(X, \mathbb{Z})$ cannot be algebraic using Steenrod operations. Kollár (1992) proved that the integral Hodge conjecture fails for degree 3 curve classes on complex 3-folds. Totaro (1997) showed failures occur even for cycle classes of dimension 2.
- **Rule**: The rational Hodge conjecture ($\mathbb{Q}$-coefficients) is the only open conjecture. Never conflate integral classes with rational cycles.

### 1.2 Hodge Conjecture on Compact Kähler Manifolds (Claire Voisin, 2004)
- **Claim**: The Hodge conjecture extends to non-projective compact Kähler manifolds.
- **Refutation**: Claire Voisin (2004) constructed compact Kähler manifolds of dimension $\ge 4$ that have no non-trivial subvarieties, yet possess non-zero rational Hodge classes.
- **Rule**: Projectivity (existence of an ample line bundle / polarization) is an indispensable global requirement. Never apply Hodge-theoretic arguments to non-projective Kähler spaces.

---

## 2. Repo-Certified Structural Traps (Fermat & Degree-70 Block)

### 2.1 First-Witt Deformation Obstruction ($W_2$ Obstruction, U58)
- **Status**: Certified in `research/U58_explicit_detecting_conic_and_W2_obstruction.md`.
- **Barrier**: Explicit semiregular curves (Hermitian line/conic images) in the special fiber over $\mathbb{F}_{139}$ fail to lift to $W_2(\mathbb{F}_{139})$. General first-order quadratic perturbations modulo $139^2$ encounter an exact coefficient mismatch ($81 \ne 88$).
- **Rule**: Raw geometric special-fiber cycles cannot be directly deformed to characteristic zero without coherent sheaf / matrix factorization algebraization.

### 2.2 Formal GAGA Non-Algebraization Gap (U55)
- **Status**: Certified in `research/U55_padic_formal_lift_and_algebraization_gap.md`.
- **Barrier**: Bloch–Esnault–Kerz gives a compatible formal pro-class in rational $K$-theory across all Witt thickenings, but the $K_0$ algebraization map is not known to be surjective in general. Formal GAGA applies to coherent sheaves / complexes, not naked cohomology classes.
- **Rule**: A formal pro-class is not an algebraic cycle until represented by a genuine perfect complex.

### 2.3 Torus-Coset Surface Obstruction (U51)
- **Status**: Certified in `research/U51_torus_coset_surface_obstruction.md`.
- **Barrier**: All non-degenerate 4-tuples under coordinate torus actions produce components whose character projections violate the Hodge condition.
- **Rule**: Torus-coset and linear coordinate subvarieties cannot span the primitive Hodge locus for the degree-70 Fermat orbit.

## 3. External Claimed-Proof Audit

### 3.1 Relative Secant Cycles and Hodge Classes v5 (2026)
- **Status**: The general proof claim is not established by the preprint as written; see `research/U62_RSC_v5_secant_intersection_failure.md`.
- **Failure**: Its RSC cycle uses `Sec^n(A^vee) ∩ A^vee` as a codimension-`n` cycle. By the paper's own definition, `Sec^n(A^vee)` contains `A^vee`, so this intersection has codimension zero. The paper's Appendix E.3 acknowledges the defect for `n=2` and supplies a different degeneracy-locus construction only for that case; no general `n≥3` replacement is given.
- **Scope**: This invalidates the stated RSC dependency chain for Theorems 4, 5, 12, and 13. It does not refute the rational Hodge conjecture or the separately known abelian-fourfold cases.
