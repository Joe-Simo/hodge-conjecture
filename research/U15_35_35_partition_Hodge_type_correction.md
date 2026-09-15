# U15: Hodge-type audit of the 35/35 ternary partition

Status: verified conceptual correction of the U14 lead. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## Candidate from U14

The unique equal-sum partition of

    alpha=(1,20,24,42,61,62)

is

    A=(1,42,62),
    B=(20,24,61),

with ordinary sums

    sum(A)=sum(B)=105 = 3*70/2.

U14 noted that this is congruent to 35 modulo 70 and suggested investigating an order-two ternary sector.

## Hodge-type audit

For Fermat character decompositions, the relevant invariant is not merely the coordinate sum modulo m. The Hodge grade is determined by the least-positive-residue sum divided by m (with the usual dimension-dependent shift). For a genuine Fermat curve character triple `(a,b,c)` satisfying `a+b+c == 0 mod m`, the least-positive sum is either m or 2m, corresponding to the two Hodge types of H^1.

Here each candidate triple has least-positive sum 105, which is neither 70 nor 140 and is not 0 modulo 70. Therefore neither A nor B is an ordinary Fermat-curve character triple. The arithmetic equality 105/105 cannot be interpreted as a product of two H^1 Fermat-curve eigenspaces.

Equivalently, the apparent order-two residue 35 records a nontrivial central character defect. Tensoring the two defects cancels globally because 35+35=70, but each block separately is not an ordinary projective Fermat-curve eigenspace.

## Consequence

The 35/35 observation does not provide a standard 3+3 join construction and should not be treated as evidence that a ternary matrix factorization exists.

A genuinely useful 3+3 factorization would have to be *twisted/equivariant* in such a way that each ternary block carries the order-two central character and the tensor product descends to the projective degree-70 fourfold. Establishing such an object requires an explicit equivariant matrix factorization or a theorem about twisted Landau-Ginzburg sectors; residue arithmetic alone is insufficient.

## Research decision

Do not spend further effort treating A and B as ordinary Fermat-curve blocks. Instead test whether the order-two defect can be removed by a finite cover/stacky lift: pass from level 70 to level 140, where the half-level character may become an honest integral grading after an appropriate lift, and check whether alpha admits a decomposable lift whose algebraicity descends along the power map X_140 -> X_70.

This is analogous in spirit to the level-lift strategy used for exceptional odd-degree classes, but no conclusion is assumed. The next task is an exact finite search over lifts of each coordinate from a_i mod 70 to a_i or a_i+70 mod 140, subject to the level-140 Hodge condition and zero-sum triple decomposition, followed by an audit of whether such a lift can descend to alpha.
