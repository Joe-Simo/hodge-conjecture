# U34: saturated toric ansatz carrying the target character — dimension correction

Status: corrected. The proposed fixed-parameter construction defines a curve, not a surface, so it cannot directly represent a codimension-2 Hodge class on the Fermat fourfold. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## Relation lattice

Start with

    r0=(1,20,24,-28,-9,-8),
    r1=(1,0,-1,0,0,0),
    r2=(0,1,-1,0,0,0).

The 3x6 relation matrix has rank 3 and saturation index 1. Also

    alpha-r0=(0,0,0,70,70,70),

so alpha == r0 mod 70. Thus the stabilizer calculation remains correct: the torus defined by these three fixed Laurent relations has stabilizer compatible with alpha.

## Correct dimension count

The earlier version incorrectly treated the constants in

    z0=a z2,
    z1=b z2

as coordinates of a single cycle. For a fixed algebraic subvariety, a,b and lambda are parameters/constants, not additional coordinates.

In P5:

- the two independent relations r1,r2 cut dimension 5 to 3;
- the independent r0 Laurent relation cuts dimension 3 to 2;
- intersecting with the Fermat hypersurface cuts the generic dimension to 1.

Therefore the fixed relation lattice defines a curve in X_70, not a surface. A curve contributes to H^6 / codimension 3, not the desired codimension-2 H^4 class.

The chart equations previously written as two equations in five variables described the total family with a,b varying, not one member of the family. That family dimension cannot be counted as the dimension of an individual algebraic cycle.

## Consequence

U34 is not a candidate solution for V(alpha). The character/stabilizer idea remains useful, but a surface inside the fourfold should generically impose only two independent conditions on X_70 (equivalently two independent Laurent relations in the ambient projective torus), not three.

This creates a structural tension: with only two homogeneous relation vectors, the stabilizer criterion requires alpha to lie in their mod-70 span together with the projective diagonal. U32 showed the particular two minimal support-3 relations fail, but it did not rule out all rank-2 relation lattices.

## Correct next problem

Search rank-2 homogeneous relation lattices L=<r,s> satisfying

    alpha in span_mod70(r,s,1).

Any such lattice has the correct generic dimension for a surface after intersection with X_70. Minimize coefficient size/support, require saturation, then explicitly analyze the resulting surface and its alpha-period.

This rank-2 search replaces the erroneous rank-3 surface search.
