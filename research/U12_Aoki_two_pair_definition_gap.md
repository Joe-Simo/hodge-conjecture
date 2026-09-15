# U12: primary-definition audit for the Aoki/two-pair route

Status: route-definition checkpoint only. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## Starting point

U11 correctly observed that the genuine recent two-pair closure is not a partition into zero-sum triples. The accessible abstract of Rifat Jumagulov's 2026 preprint states the criterion as follows: after adjoining two vanishing pairs, the character decomposes into an Aoki standard sextuple and a grade-2 Hodge quadruple.

The abstract alone does not provide the coordinate-level definitions of:

- an Aoki standard sextuple;
- a grade-2 Hodge quadruple;
- the precise equivalence operations allowed before decomposition;
- the exact compatibility hypotheses needed for the geometric algebraicity conclusion.

Those definitions are mathematically essential. Guessing them from terminology would make any exhaustive computation unreliable.

## Literature cross-check

Genival da Silva's 2021 paper proves the Hodge conjecture for Fermat fourfolds of degree m <= 100 coprime to 6, and for X_21^n and X_27^n. Degree 70 is not coprime to 6, so that theorem does not settle X_70^4.

The 2026 Jumagulov theorem covers odd degrees <=199. Degree 70 is even, so its final theorem also does not settle X_70^4 directly. Its two-pair construction may still inspire a valid even-degree construction, but such an extension must be proved rather than assumed.

Therefore the degree-70 orbit remains a legitimate stress test within the current project.

## Consequence

No U12 computation is promoted as a theorem test until the full primary definitions are available. The next exact route should either:

1. obtain the full theorem text and implement its definitions verbatim, then separately prove that the construction extends to even m=70; or
2. bypass that dependency and search directly for an algebraic certificate using the Favero-Kelly matrix-factorization/Chern-character formula already recorded in U05-U07.

Given the parity mismatch, route (2) is currently cleaner: it works directly on the degree-70 hypersurface and does not require extending an odd-degree theorem.

## Research decision

Return the active frontier to the exact matrix-factorization certificate target of U07. Restrict first to structured higher-rank factorizations built from tensor products/extensions of elementary factorizations and use character support to reject ansatz families before symbolic expansion. Any successful factorization must have nonzero primitive Chern-character projection onto the target Jacobian monomial

    x1^19 x2^23 x3^41 x4^60 x5^61.

This is a construction problem, not evidence that the target is non-algebraic.
