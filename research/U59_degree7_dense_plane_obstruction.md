# U59: dense linear-plane obstruction on the two degree-7 Delsarte quotients

**Status:** exact computational/valuation obstruction for broad linear-plane strata, with complete characteristic-zero elimination for all 3-direction and 4-direction proportionality types and a strong exact screen for the remaining 5-direction A2 types. No target-bearing cycle is constructed; this does not solve the Hodge conjecture.

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

First restrict to planes where each xi is a nonzero scalar multiple of one of three plane coordinates u,v,w. There are 3^6 assignments before removing redundancies. For f|P to vanish identically, every degree-7 exponent vector occurring after restriction must occur at least twice so coefficients can cancel.

Exact enumeration finds zero assignments for A2 and zero for A3 satisfying even this necessary exponent-collision condition. Thus no scalar-coordinate dense plane exists.

## 3. Full finite-field Fano census

A direct enumeration of rank-3 row-reduced 3x6 matrices over F2 and F3 gives:

- over F3: A2 has 233 rational planes, A3 has 312;
- every such plane is contained in at least one coordinate hyperplane;
- hence there are zero dense-torus planes over F3 for both quotients.

The same qualitative result holds over F2: all rational planes found are boundary-supported. This finite-field evidence is not by itself a characteristic-zero proof.

## 4. Valuation reduction by proportional linear forms

Let a characteristic-zero plane P be parametrized by six nonzero linear forms L0,...,L5 on P2. If no two Li are proportional, choose a generic point on the line Li=0 avoiding all other Lj=0. In f|P, the six monomial terms have valuations equal to their xi-exponents. For the sum to vanish identically, the minimum valuation at every such divisor must occur at least twice. Applying this simultaneously to all six coordinate divisors eliminates the generic six-direction case.

Repeating after allowing proportional classes reduces the possible incidence partitions drastically. Among all 203 set partitions of six labels, only 36 patterns survive the valuation-minimum necessary condition for A2 and 16 for A3.

## 5. Complete exact elimination of 3-direction types

For every surviving partition with exactly three proportionality classes, choose the three distinct projective directions as u,v,w. Each Li is then a nonzero scalar multiple of its class representative. Substitute into f2 or f3, equate all degree-7 coefficients to zero, and saturate by the product of all scalar parameters to exclude coordinate-boundary degenerations.

Exact Groebner elimination gives the unit ideal in every case:

- A2: all 18 admissible three-direction partitions eliminated;
- A3: all 10 admissible three-direction partitions eliminated.

Therefore neither quotient contains a dense plane with only three distinct coordinate-line directions.

## 6. Complete exact elimination of 4-direction types

For every surviving four-direction partition, work chart-by-chart on Gr(3,4): normalize three directions to u,v,w and write the fourth as a general linear form a u+b v+c w. Saturate by the parameters/minors required for four distinct nonzero directions.

The coefficient ideal plus saturation has Groebner basis {1} in every chart checked exhaustively:

- 180 A2 charts;
- 72 A3 charts.

Thus no dense plane with four coordinate-line directions exists on either quotient.

## 7. Five-direction A2 residue

The valuation screen leaves only three five-direction proportionality patterns, all on A2; A3 has none. A representative exact chart with x0 proportional to x5 is normalized as

    x0=u, x5=k u, x1=v, x2=w,
    x3=a u+b v+c w,
    x4=d u+e v+f w.

After equating all 27 coefficients of f2|P to zero and saturating by k and the minors forcing the five directions to remain distinct/in general position, the Groebner basis is {1}.

A broader exact general-position screen over all 15 choices of proportional pair likewise gives the unit ideal in every case. This is strong evidence against all five-direction dense planes. Because the saturation used all 3x3 minors and therefore excludes special collinear configurations of direction points in the dual P2, it is recorded as a screen rather than promoted to a complete theorem for the last three special five-direction strata.

## 8. Consequence

The degree-7 quotient route does not yield an obvious linear P2 away from the singular coordinate boundary. We have now rigorously eliminated all dense planes with three or four proportionality directions and all scalar-coordinate planes; finite-field censuses and saturated general-position elimination also find none in the remaining five-direction regime.

This substantially narrows the quotient-side construction route. The remaining linear-plane obligation is small and explicit: analyze the special-collinearity subcases of the three surviving A2 five-direction patterns without saturating their 3x3 minors. If those also vanish, every dense linear P2 on both degree-7 quotients is excluded.

A successful quotient-side cycle would then need degree >1 or nonlinear geometry.

No formal proof assistant or independent expert review is claimed.