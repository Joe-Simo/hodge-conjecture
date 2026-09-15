# U27: no smooth/quasismooth atomic Delsarte quotient of degree <=5 carries the target orbit

Status: exact finite classification within the quasismooth invertible Delsarte class. This does not rule out singular low-degree quotients or solve the Hodge conjecture.

Date: 2026-09-14.

## Motivation

A smooth/quasismooth degree <=5 fourfold quotient carrying alpha would be extremely useful because the rational Hodge conjecture is known for smooth fourfold hypersurfaces through degree 5. We therefore search the entire quasismooth invertible Delsarte class in ordinary P^5.

## Exhaustive reduction to atomic types

A quasismooth invertible Delsarte polynomial over C is a disjoint sum of Fermat, loop, and chain atoms. On six variables there are only 29 unlabeled atomic decompositions.

For ordinary degree d, the corresponding atomic exponent blocks are:

- Fermat F1: [d];
- chain CL: diagonal d-1 with a single 1 to the next variable, ending in [d];
- loop LL: diagonal d-1 with a single cyclic 1 to the next variable.

For each atomic type with total length six, form its exact integer exponent matrix A, compute the minimal Fermat covering level

    m = lcm(denominators of A^{-1}),

and retain only cases with m | 70, since only those admit the standard coordinatewise Fermat cover from X_70 without enlarging the level. Then test the exact quotient-character invariance condition

    A^T a == 0 mod 70

for every permutation a of alpha=(1,20,24,42,61,62), accounting for coordinate relabeling.

## Exact classification

The atomic-type covering levels are:

### Degree 2

All nonsingular atomic types have minimal covering level m=2, hence m|70. However no labeling can satisfy the invariance equations. Structurally, each column equation is built from one of

    a_i,
    2 a_i,
    a_i+a_j,
    2a_i+a_j

modulo 70, according to whether the corresponding vertex is internal/terminal in a chain or loop. For the six entries of alpha, none of these required zero congruences can be satisfied consistently; in particular alpha contains no complementary pair and no relation 2a_i+a_j == 0 mod70.

### Degree 3

Across all 29 atomic types, the possible minimal covering levels include

    3,6,9,12,15,18,24,30,33,36,48,63,96,

and none divides 70. Hence no degree-3 quasismooth atomic quotient is covered by X_70 in this standard Delsarte construction.

### Degree 4

Possible minimal covering levels include

    4,8,12,24,28,36,56,72,80,84,108,216,240,244,252,324,728,972,

and again none divides 70.

### Degree 5

Among all 29 atomic types, the only type with minimal covering level dividing 70 is the pure Fermat type F1^6, with m=5 and A=5 I_6. Its invariance condition is

    5 alpha == 0 mod70,

which fails coordinatewise.

## Consequence

There is no smooth/quasismooth invertible Delsarte fourfold of ordinary degree 2,3,4, or 5 arising from a standard Fermat quotient of X_70 whose primitive cohomology contains the target alpha eigenspace.

Thus the most attractive quotient shortcut—descend alpha to a smooth low-degree fourfold for which the Hodge conjecture is already known—is closed within the full atomic/quasismooth invertible Delsarte class.

This does NOT rule out:

- singular low-degree Delsarte quotients whose resolutions might still be tractable;
- weighted-projective quotients;
- non-invertible equations;
- correspondences that are not standard Shioda Delsarte quotients.

## Sources and computation

- Louis Esser, `Rational weighted projective hypersurfaces`, Section 3.1, which states that a quasismooth Delsarte hypersurface over C decomposes into Fermat, loop and chain atoms.
- Exact atomic-type enumeration and rational matrix arithmetic performed 2026-09-14; 29 unlabeled atomic decompositions on six variables were checked.

## Research decision

The smooth degree<=5 quotient path is exhausted in this class. Return priority to either:

1. the two singular degree-7 quotients from U25, whose primitive rational Hodge sector is exactly the alpha orbit; or
2. the direct nonseparable matrix-factorization certificate from U07.
