# U25: exact degree-7 quotient reduction isolates precisely the target Hodge orbit

Status: verified finite character-lattice reduction for two Delsarte quotients. This does not prove algebraicity and does not solve the Hodge conjecture.

Date: 2026-09-14.

## Exact quotient interpretation

For a Delsarte exponent matrix A with Fermat cover degree m and B=m A^{-1}, the standard quotient description gives

    X_m / Gamma  birational to  Y_A,

with

    Gamma = Ker(B mod m) = Im(A mod m)

on the diagonal deck group (modulo the usual projective diagonal relation).

A Fermat character a descends to the quotient precisely when it is trivial on Gamma. With column-vector convention for the deck group, this is

    A^T a == 0 mod m.

This is the correct quotient-side character criterion.

## Two degree-7 matrices

Take the transposes of the two U23 matrices whose minimal Fermat covering degree is m=70. Call them A2 and A3. Exact arithmetic gives

    det(A2)=980,   Smith diagonal=(1,1,1,1,14,70),
    det(A3)=-490,  Smith diagonal=(1,1,1,1,7,70).

Both satisfy

    A_i^T alpha == 0 mod 70

for

    alpha=(1,20,24,42,61,62).

Thus the target alpha-eigenspace really does descend through each degree-7 Delsarte quotient.

## Full invariant-character census

To determine whether the quotient contains additional primitive rational Hodge blocks, compute

    Ker(A_i^T mod 70) = Im(B_i^T mod 70)

exactly by finite subgroup generation.

For A2:

    invariant character subgroup size = 980,
    projective primitive characters (all six coordinates nonzero, sum 0) = 104,
    rational (2,2) Hodge characters = 24,
    unit/Galois Hodge orbits = 1,
    orbit size = 24.

For A3:

    invariant character subgroup size = 490,
    projective primitive characters = 48,
    rational (2,2) Hodge characters = 24,
    unit/Galois Hodge orbits = 1,
    orbit size = 24.

In both cases the unique rational primitive Hodge orbit is exactly the unit orbit of alpha.

## Consequence

For either quotient, the entire primitive rational (2,2) Hodge problem reduces to the original degree-70 target block. There are no other primitive rational Hodge orbits in the quotient that need to be controlled simultaneously.

Therefore, after resolving singularities carefully, proving the rational Hodge conjecture for either quotient fourfold would prove algebraicity of V(alpha) by pullback.

Conversely, this quotient does not yet simplify algebraicity by itself: it repackages the target into a fourfold whose primitive rational Hodge space is exactly the target orbit.

## Source dependence

The quotient description Gamma=Ker(B_m)=Im(A_m) and Fermat-to-Delsarte monomial map come from the standard Shioda Delsarte construction. The invariant-character condition follows directly by character duality.

## Next question

Determine whether either quotient fourfold belongs to a class for which the Hodge conjecture is already known (for example rational/uniruled fourfolds), or whether its singularities force the primitive invariant Hodge classes to arise from algebraic exceptional strata. Do not infer either conclusion from the character census alone.
