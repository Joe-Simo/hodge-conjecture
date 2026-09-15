# U24: the three balanced degree-7 candidates fail the exact Fermat-cover descent test

Status: verified source-formula audit plus exact modular linear algebra for the three U23 candidates. This closes only that bounded candidate family and does not solve the Hodge conjecture.

Date: 2026-09-14.

## Primary-formula verification

The standard Shioda/Delsarte construction uses a nonnegative invertible exponent matrix A with constant row sum. Let A*=(det A)A^{-1}; divide its entries by their gcd, equivalently choose the minimal positive integer m for which

    B = m A^{-1}

is integral. Then the Fermat hypersurface of degree m dominates the Delsarte hypersurface via the monomial map

    x_i = product_j z_j^{b_ij}.

This formula is explicitly recorded in the Delsarte-surface literature and extends as the usual monomial Fermat-cover construction for Delsarte hypersurfaces.

Under this map, a character c=(c_i) on the Delsarte coordinate torus pulls back to the Fermat diagonal character

    c B   (mod m)

(with row-vector convention). Therefore a Fermat eigenspace V(alpha) descends through this quotient only if the modular linear system

    c B == alpha (mod m)

has a solution.

## Apply to the three U23 matrices

For A1, the minimal denominator-clearing level is m=210. Exact computation gives B=210 A1^{-1} integral. The modular system

    c B == alpha (mod 210)

has no integer solution. (Strictly, alpha itself is level 70; any comparison at level 210 requires a specified level-210 representative. Thus A1 is not on a direct level-70 cover and is not a direct candidate for alpha without an additional comparison map.)

For A2, m=70 and

    B = 70 A2^{-1}

is integral. Exact integer solving of

    c B - alpha = 70 z

for c,z in Z^6 returns no solution.

For A3, m=70 and the analogous system also has no solution.

Thus the two balanced candidates whose natural Fermat cover is exactly X_70 do not carry alpha in the pullback character lattice of the Delsarte quotient. The third candidate naturally lives over X_210 and likewise does not directly realize alpha.

## Consequence

The three U23 matrices are eliminated as direct Delsarte quotients detecting V(alpha). The arithmetic coincidence of inverse denominators 70/210 was not enough; the exact character-lattice test kills the route.

This also retrospectively clarifies the role of U21's alpha-dot-row filter: it was only a coarse heuristic/necessary-style screening device, not the true descent criterion. Future Delsarte searches should skip that filter as the load-bearing condition and instead construct A from geometric constraints, compute its minimal Fermat cover B=mA^{-1}, and test alpha membership in the row span of B modulo m directly.

## Next route

There are two sensible continuations:

1. redo the bounded degree-7/8 Delsarte search using the exact B-lattice criterion from the start, rather than alpha-dot-row congruences; or
2. return to the direct Favero-Kelly higher-rank matrix-factorization construction, which avoids quotient-character descent entirely.

Because U21's initial filter may have excluded valid matrices, degree <=6 is not globally ruled out by U21 unless the coarse congruence is independently proved necessary. That earlier scope claim must therefore be weakened: U21 rules out only matrices inside its filter, not all Delsarte sources of degree <=6.

## Source checked

A Delsarte source describing the standard construction states: for exponent matrix A, choose m so that B=m A^{-1} is integral (equivalently via the cofactor gcd), and map the Fermat cover to the Delsarte variety by monomials with exponent matrix B. This exact formula, rather than the earlier alpha-dot-row screening, is used here.
