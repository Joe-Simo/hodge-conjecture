# U23: three balanced degree-7 exponent-matrix candidates survive the coarse Delsarte filter

Status: exact bounded integer-linear-algebra result. These matrices are candidates only; no valid Shioda correspondence or algebraic cycle has been proved.

Date: 2026-09-14.

## Fixed convention and stronger filter

Continue U22 with rows interpreted as exponent vectors of six monomials in an ordinary homogeneous degree-7 polynomial. Require each row r to satisfy:

1. sum(r_i)=7 (ordinary homogeneity);
2. alpha dot r == 0 mod 70, for alpha=(1,20,24,42,61,62), as the current coarse necessary character filter.

There are exactly 14 admissible rows. Among the C(14,6)=3003 six-row subsets, exactly 1331 give an invertible 6x6 matrix.

As an additional balancing filter, require column sums also equal 7. This is not yet asserted to be a theorem-level Shioda condition; it is a strong symmetry/homogeneity constraint useful for reducing the search and is satisfied by only three matrices.

## Three survivors

A1 =

    [0 1 1 0 4 1
     0 2 0 0 0 5
     0 3 1 3 0 0
     2 0 4 1 0 0
     2 1 0 3 0 1
     3 0 1 0 3 0]

with det(A1)=-1470 and lcm of inverse denominators 210.

A2 =

    [0 1 1 0 4 1
     0 2 0 0 0 5
     0 3 1 3 0 0
     2 0 4 1 0 0
     2 1 1 1 2 0
     3 0 0 2 1 1]

with det(A2)=980 and inverse-denominator lcm 70.

A3 =

    [0 1 1 0 4 1
     0 2 0 0 0 5
     1 2 1 2 1 0
     2 0 4 1 0 0
     2 1 0 3 0 1
     2 1 1 1 2 0]

with det(A3)=-490 and inverse-denominator lcm 70.

All three have every row sum and every column sum equal to 7 and full rank 6.

## Structural observations

None of the matrices is diagonal or a simple pair-block matrix; their monomials genuinely mix coordinates. This is exactly the type of structure that survived the earlier pair/triple obstructions.

The inverse denominator levels 70 or 210 are compatible with the arithmetic scales already appearing in the target problem, but this is only suggestive.

## Critical unresolved point

The alpha-dot-row congruence used to generate these matrices is still only a coarse necessary filter. Before calling any A_i a Delsarte/Shioda source, derive the exact character transformation from the standard Shioda construction. In particular determine, with a fixed convention, the Fermat covering degree m and maps encoded by B=m A^{-1}, then calculate which source/cover character maps to alpha.

Only if that exact equation holds should we test quasismoothness/singularity and whether the relevant source Hodge class is algebraic.

This file therefore records three finite candidates, not a proof of algebraicity.
