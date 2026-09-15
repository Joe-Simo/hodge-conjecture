# U21: small-degree Delsarte column search for the degree-70 character

Status: exact bounded integer-linear-algebra search. This does not establish a valid Delsarte map or solve the Hodge conjecture.

Date: 2026-09-14.

## Goal

Generalize the U08 cubic obstruction. Let

    alpha=(1,20,24,42,61,62).

As a first necessary arithmetic filter for a degree-d Delsarte exponent matrix, enumerate nonnegative integer column vectors c in Z_{>=0}^6 with

    sum_i c_i=d

and require

    alpha dot c == 0 mod 70.

A six-column exponent matrix capable of mixing the target character must at minimum have six linearly independent admissible columns. This is only a necessary filter: passing it does not establish the correct Shioda character relation, invertibility in the required sense, quasismoothness, or algebraicity of the source Hodge class.

## Exact enumeration

Wolfram exact enumeration gives:

- d=3: 0 admissible columns;
- d=4: 1 admissible column;
- d=5: 4 admissible columns;
- d=6: 8 admissible columns, but no six are linearly independent;
- d=7: 14 admissible columns and 1331 linearly independent six-column subsets;
- d=8: 20 admissible columns and 23315 linearly independent six-column subsets.

Thus degrees 3,4,5 are impossible already by column count, and degree 6 fails the rank-6 requirement despite having eight admissible columns.

The first degree at which this coarse arithmetic obstruction disappears is d=7.

One exact rank-6 degree-7 column set is

    c1=(0,0,3,2,0,2)
    c2=(0,0,4,0,2,1)
    c3=(0,1,0,2,2,2)
    c4=(0,2,0,0,0,5)
    c5=(0,3,1,3,0,0)
    c6=(1,0,0,1,3,2)

with determinant 490 for the matrix having these as columns.

## Interpretation

This is genuine narrowing relative to U08: the same coarse character-column mechanism rules out all ordinary source degrees d<=6, not just cubic degree 3. Degree 7 is the first place where a mixed-coordinate exponent matrix is arithmetically possible.

However, the displayed degree-7 matrix is NOT yet a Delsarte certificate. Before using it, the following must be checked:

1. correct orientation of the exponent matrix and the exact Shioda character equation (the present alpha-dot-column condition is only a necessary filter);
2. row sums/weighted homogeneity appropriate to the source hypersurface;
3. determinant/inverse denominators and resulting Fermat covering level;
4. nonnegative monomial structure and quasismoothness/singularity behavior;
5. whether the relevant source (2,2) class is known algebraic;
6. whether pullback/pushforward lands nontrivially on V(alpha).

## Next bounded attempt

Take the degree-7 candidate pool and solve the full exponent-matrix equations rather than merely column congruences. If no valid ordinary degree-7 Delsarte source exists, repeat at degree 8. Do not promote the 1331 rank-6 subsets to geometric candidates until the full Shioda equations are imposed.
