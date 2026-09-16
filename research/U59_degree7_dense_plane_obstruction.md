# U59: no dense linear planes on the two degree-7 Delsarte quotients

**Status:** exact characteristic-zero obstruction for every dense linear P2 on the two U25 degree-7 quotients. Boundary-supported planes remain and are already excluded from the target by U29. No target-bearing cycle is constructed; this does not solve the Hodge conjecture.

Date: 2026-09-16. Base checkpoint: U58.

## 1. Quotient equations

Use the U28 equations

A2:

    f2 = x0^4*x4^2*x5 + x0*x1^5*x5 + x0*x1^2*x2^3*x4
       + x0*x2*x3^4*x4 + x2^3*x3*x4*x5^2 + x3^2*x4^2*x5^3.

A3:

    f3 = x0^4*x2*x5^2 + x0*x1^5*x4 + x0*x1^2*x2^2*x4*x5
       + x0*x2*x3^4*x5 + x2^2*x3*x4^3*x5 + x2*x3^2*x4^2*x5^2.

U25 proves that the unique rational primitive Hodge orbit on either quotient is the alpha orbit. Thus a plane not confined to the coordinate boundary would be a high-value candidate surface.

## 2. Scalar-coordinate planes are impossible

Restrict first to planes where each xi is a nonzero scalar multiple of one of three plane coordinates u,v,w. Exact enumeration of all 3^6 assignments finds zero assignments for A2 and zero for A3 satisfying even the necessary exponent-collision condition for f|P=0. Thus no scalar-coordinate dense plane exists.

## 3. Finite-field Fano census

Direct enumeration of rank-3 row-reduced 3x6 matrices over F2 and F3 finds many rational planes but no dense ones. Over F3, A2 has 233 rational planes and A3 has 312, every one contained in a coordinate hyperplane. The same qualitative result holds over F2. These finite-field calculations motivated but are not used as the characteristic-zero proof.

## 4. Valuation reduction

Let a characteristic-zero plane P be parametrized by six nonzero linear forms L0,...,L5 on P2. At a generic point of a divisor Li=0, the valuation of each of the six Delsarte monomials is the corresponding xi exponent, after grouping proportional Li. For an identity f|P=0, the minimum valuation at each divisor must occur at least twice.

Applying this condition to all proportionality partitions of {0,...,5} reduces the 203 set partitions to 36 candidates for A2 and 16 for A3. In particular the generic six-direction case is impossible.

## 5. Three-direction types

For each surviving partition with exactly three proportionality classes, normalize the three directions to u,v,w, substitute scalar multiples into f2 or f3, equate all degree-7 coefficients to zero, and saturate by the nonzero scalars.

Exact Groebner elimination gives the unit ideal in every case:

- A2: all 18 admissible three-direction partitions;
- A3: all 10 admissible three-direction partitions.

## 6. Four-direction types

For every surviving four-direction partition, normalize three directions to u,v,w and write the fourth as a general linear form. Saturating by the minors/scalars that keep four distinct nonzero directions, exact Groebner elimination gives {1} in every chart:

- 180 A2 charts;
- 72 A3 charts.

Thus neither quotient has a dense four-direction plane.

## 7. Five-direction cases: complete closure

The valuation screen leaves no five-direction A3 pattern and only three five-direction A2 patterns.

To remove the general-position caveat in the previous version, redo the A2 computation **without saturating any 3x3 direction minors**. For each possible proportional pair {i,j}, normalize

    xi = u,   xj = k u,   k != 0,

choose two remaining coordinates as v,w, and write the final two coordinates as completely general linear forms

    z1 u+z2 v+z3 w,
    z4 u+z5 v+z6 w.

Equate every coefficient of f2|P to zero and saturate only by k, using an auxiliary equation t*k-1. This deliberately retains all special-collinearity configurations among the five projective directions.

For eight proportional-pair charts the saturated coefficient ideal is immediately the unit ideal. For each of the seven non-unit charts, the exact Groebner basis is

    {z6,z5,z4,z3,z2,z1,-1+k t}.

Hence both supposedly independent remaining coordinate forms are forced identically to zero. Such a plane is contained in coordinate hyperplanes and is not dense. Therefore **no five-direction dense plane exists on A2**, including every special-collinearity subcase omitted by the earlier general-position saturation.

Combining with the valuation classification closes the final linear-plane cases.

## 8. Theorem-level consequence within this route

Every characteristic-zero linear P2 contained in either degree-7 quotient Y_A2 or Y_A3 is supported on the coordinate boundary. U29 proves that coordinate-boundary cycles have zero projection to the target alpha eigenspace after pullback to the Fermat cover.

Therefore **no linear plane on either quotient can furnish the missing alpha Hodge class**.

This closes the linear-plane version of the degree-7 quotient construction route. It does not exclude nonlinear algebraic surfaces on the quotient. Any successful quotient-side cycle must have nonlinear geometry (degree >1 in its projective span) or arise through resolution/intersection-cohomology phenomena not represented by a linear P2.

## 9. Verification scope

All characteristic-zero eliminations use exact polynomial arithmetic and Groebner bases; no floating point is used. The finite-field census is independent corroboration only. The valuation reduction and its completeness over proportionality partitions are mathematical arguments, while the finite lists of coefficient ideals are computer-assisted exact checks.

No formal proof assistant or independent expert review is claimed.