# U59: no plane meeting the dense torus on either degree-7 Delsarte quotient

**Status:** proved for linear projective planes by a valuation reduction plus exact saturated Gröbner elimination. This does not rule out nonlinear surfaces, prove rationality/nonrationality, or solve the Hodge conjecture.

Date: 2026-09-16. Base checkpoint: U55–U58.

## 1. Objects

Use the two degree-7 quotient equations from U25/U28:

    A2:
    f2 = x0^4*x4^2*x5
       + x0*x1^5*x5
       + x0*x1^2*x2^3*x4
       + x0*x2*x3^4*x4
       + x2^3*x3*x4*x5^2
       + x3^2*x4^2*x5^3.

    A3:
    f3 = x0^4*x2*x5^2
       + x0*x1^5*x4
       + x0*x1^2*x2^2*x4*x5
       + x0*x2*x3^4*x5
       + x2^2*x3*x4^3*x5
       + x2*x3^2*x4^2*x5^2.

U25 proves that the unique primitive rational Hodge orbit on either quotient is the degree-70 target orbit. Hence a plane meeting the dense coordinate torus would be a particularly useful candidate algebraic surface.

## 2. Valuation lemma

Let P^2 -> P^5 be a linear plane not contained in any coordinate hyperplane. Write the six restricted coordinate functions as nonzero linear forms l_0,...,l_5 on P^2.

Partition {0,...,5} by proportionality of these forms. For a block B and one Delsarte monomial M_j=prod_i x_i^(e_{j,i}), the vanishing order of M_j|P along the line represented by B is

    v_B(M_j)=sum_(i in B) e_(j,i).

If f|P=sum_j M_j|P is identically zero, the minimum of the six integers v_B(M_j) must be attained at least twice for every block B: a unique lowest-order term cannot cancel in the DVR at the generic point of that line.

The six restricted forms span H^0(P^2,O(1)), so their proportionality partition has at least three blocks.

Enumerating all 203 set partitions of six indices gives the following complete necessary lists:

- A2: 36 partitions survive the valuation test: 18 with 3 blocks, 15 with 4 blocks, 3 with 5 blocks, none with 6 blocks;
- A3: 16 survive: 10 with 3 blocks, 6 with 4 blocks, none with 5 or 6 blocks.

Thus every hypothetical dense-torus plane is covered by finitely many proportionality types.

## 3. Exact elimination for three directions

For a 3-block partition the three line directions must be independent. After a projective change of coordinates on P^2 take them to u,v,w. In each block normalize one ambient coordinate coefficient to 1; the remaining 3 coefficients are nonzero relative scalars.

Substitute into f2 or f3, collect the 36 possible degree-7 monomial coefficients in u,v,w, and saturate by the product of the relative scalars. Exact Gröbner bases over Q give the unit ideal in every case:

    A2: 18/18 systems unit,
    A3: 10/10 systems unit.

Hence no dense-torus plane has exactly three proportionality directions.

## 4. Exact elimination for four directions

For each surviving 4-block partition, choose any 3 independent block directions as u,v,w. The fourth direction is represented on one of its three standard affine charts by

    u + a v + b w,
    a u + v + b w,
    a u + b v + w,

with a separate nonzero scale for the representative ambient coordinate and nonzero relative scales for additional coordinates in that block.

Saturating all nonzero coordinate scales and computing exact Gröbner bases gives the unit ideal in every chart:

    A2: 15 * C(4,3) * 3 = 180/180 charts unit,
    A3:  6 * C(4,3) * 3 =  72/72 charts unit.

This covers every possible choice of independent block triple.

## 5. Exact elimination for the three A2 five-direction patterns

Only A2 has 5-block survivors, namely the proportional pairs

    {x1,x4},  {x4,x5},  {x0,x4},

with the other four coordinate forms pairwise nonproportional.

Choose any 3 independent block directions as u,v,w. The two remaining block directions are distinct from each basis direction. Therefore each has support on at least two of {u,v,w}. Two subsets of a 3-element set, each of size at least 2, intersect; hence the two nonbasis forms have at least one common nonzero basis coefficient. After permuting u,v,w, both may be placed simultaneously on the same affine chart with that coefficient normalized to 1.

There are therefore only

    3 partitions * C(5,3) * 3 = 90

charts to check, not 270 independent chart pairs. Exact saturated Gröbner bases over Q are the unit ideal in all 90.

## 6. Theorem

Combining Sections 2–5:

> Neither Y_A2 nor Y_A3 contains a projective plane P^2 that meets the dense coordinate torus (G_m)^5.

Coordinate-boundary planes certainly exist; U28 lists the singular coordinate planes, and U29 explains why boundary-supported cycles cannot hit the alpha eigenspace upstairs.

Thus **linear planes cannot supply the missing primitive Hodge class on either degree-7 quotient.** Any successful quotient-side cycle must be nonlinear.

## 7. Independent finite-field corroboration

As a separate bounded check, enumerate every F_p-rational plane in P^5 by unique 3x6 RREF matrices and test polynomial restriction exactly.

Results:

    p=2: A2 has 84 planes, 0 dense-torus; A3 has 109, 0 dense-torus.
    p=3: A2 has 233 planes, 0 dense-torus; A3 has 312, 0 dense-torus.

These finite-field counts are corroboration only; the characteristic-zero theorem is the valuation reduction plus Q-Gröbner elimination above.

## 8. Reproducibility and next route

Checker: `research/computations/U59/verify_u59.py`.

Execution used Python 3.13.5 and SymPy 1.14.0 with exact rational Gröbner arithmetic. The complete checker rerun takes about 26 seconds in the recorded runtime.

The rationality shortcut from a linear target-bearing surface is now closed. The next quotient-side constructions should begin with genuinely nonlinear surfaces (e.g. low-degree surfaces in P^3 sections or residual components of singular-center projections), not more plane searches.
