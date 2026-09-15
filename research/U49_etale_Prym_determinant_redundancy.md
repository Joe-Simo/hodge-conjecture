# U49: every etale abelian Fermat-cover determinant is already a reflection word

**Status:** the restricted, all-degree result below is proved by explicit group and character arguments, with exact finite corroboration and adversarial self-review. It is not formally verified or independently expert-reviewed. No algebraic cycle representing the original degree-70 target, and no solution of the rational Hodge conjecture, is claimed.

Date: 2026-09-15. Remote base: `Joe-Simo/hodge-conjecture@cd4ba6bd38ce1b86d41ced84322b6b1b021282d9` (U48). All writes are confined to `/mnt/data/hodge-conjecture`. Existing evidence is preserved. The supplied Hodge prompt, SHA-256 `0639b0689036cee1ed7a990147fba250ee3188d5bc3143dc2625e50d4d85bbb3`, was read in full. Historical results outside the dependencies explicitly used here are not globally revalidated.

## 1. New route and exact result

U48 excludes product-dominated surfaces in the fixed four-curve source. Rather than try another such surface, this attempt tests the determinant classes on generalized Prym varieties associated with unramified finite abelian covers. Patel--Zhang [PZ, Theorems 1.1 and 1.2] identifies this algebraic input family, extending Schoen's cyclic-cover construction. These are not assumed to be products of divisor classes.

We test the entire subclass whose upstairs curve is a classical Fermat curve, including non-diagonal group actions, at arbitrary degree. The result is stronger than a bounded search and narrower than a statement about all Prym varieties.

Work over C. Set

    F_m = {x^m+y^m+z^m=0} in P^2,  m >= 4.

Let H be a nontrivial finite abelian group acting faithfully and freely on F_m; the quotient B=F_m/H is a smooth curve and F_m -> B is etale. For a nontrivial character chi of H put

    V_chi = H^1(F_m,C)_chi,
    r = dim V_chi = 2g(B)-2,
    D_chi = exterior^r V_chi.

D_chi is a one-dimensional Hodge space of type (r/2,r/2). Its coefficient-Galois orbit is one of the determinant spaces relevant to the Prym construction. A determinant is taken of the **whole chi-eigenspace**, not an arbitrary smaller subspace of it.

Use U42's free formal group

    A_m = direct sum_(1<=j<m) Z e_j  (+) Z ell,
    R_m(j) = e_j + e_(m-j) - ell.

A nonzero Fermat curve character triple (a,b,c), with a+b+c=0 mod m, is represented by e_a+e_b+e_c-ell. The symbol ell represents the Lefschetz motive. Individual e_j are not assigned to hypothetical characteristic-zero Gauss motives; U42 Section 3 supplies the interpretation of balanced expressions in actual Jacobi motives.

**Theorem.** After algebraic coordinate-conjugation and, for the non-diagonal cases, algebraic cyclic-orbit projectors, every normalized determinant D_chi tensor L^(-r/2) has a formal word

    d_chi = sum_j c_j e_j - (3r/2) ell

which is an **integral sum of reflection relations alone**. The complete explicit coefficients are given in Sections 4--6. This covers every m>=4, every free finite abelian H, and every nontrivial chi, without a bound on r or group order.

Consequently adjoining all these determinant words as algebraic inputs at arbitrary Fermat levels does not enlarge the reflection/multiplication relation subgroup used in U42--U45. In particular it cannot remove U44's formal obstruction to

    alpha=(1,20,24,42,61,62),  t_alpha=sum e_(alpha_i)-3ell.

This is a restriction on this source-and-transport method, not on arbitrary algebraic correspondences from Prym varieties to the target. No assertion of nonalgebraicity is made.

## 2. Classification of the free abelian actions

The classical automorphism theorem says that, for m>=4 in characteristic zero,

    Aut(F_m) = (mu_m^3/mu_m) semidirect S_3.             (2.1)

The generators and split exact sequence are stated explicitly in the primary research article [H, Theorem 2.2], attributing the theorem to Harui and Tzermias. Thus all automorphisms relevant here are projective monomial transformations. The subgroup classification needed below is proved directly, rather than assumed from a subgroup table.

### 2.1 The group has odd order

A nonidentity projective involution in PGL_3(C) has a repeated eigenvalue, and hence fixes a line pointwise. That line meets the positive-degree plane curve F_m over C. It therefore cannot belong to a free action. Cauchy's theorem excludes even |H|. The abelian image of H in S_3 is consequently either trivial or C_3.

### 2.2 Trivial permutation image

Normalize diagonal elements as diag(a,b,1). Freeness makes each of the homomorphisms a, b and a/b injective on H: a nontrivial element in any of their kernels has a repeated eigenvalue and fixes a line meeting F_m. Thus H is cyclic, of order h dividing m. After choosing a generator using the injective first coordinate,

    H = <diag(zeta_h,zeta_h^s,1)>,
    gcd(s,h)=gcd(s-1,h)=1.                             (2.2)

These conditions imply h odd and are sufficient: every nonidentity power has three distinct eigenvalues, so its only projective fixed points are the three coordinate points, none of which belongs to F_m. These parameters are not claimed to be a nonredundant list of quotient isomorphism classes.

### 2.3 Nontrivial permutation image

Choose a lift g=D sigma, where sigma cyclically permutes x,y,z. Its cube is scalar, so g has projective order three. Since H is abelian, H intersect (mu_m^3/mu_m) is contained in the sigma-fixed diagonal group. Solving the three diagonal equations up to scalar gives the identity only when 3 does not divide m, and otherwise the cyclic group generated by

    delta = diag(omega,omega^2,1),  omega^3=1, omega!=1.

The diagonal kernel therefore has order at most three.

Write D=diag(zeta_m^a,zeta_m^b,1). At an eigenpoint of D sigma, the three mth powers, up to common scale, are

    1, omega^(a+b+j m), omega^(2(a+b+j m)),  j=0,1,2.

If 3 does not divide m, two of these eigenpoints lie on F_m. If 3 divides m, none lies on F_m precisely when a+b=0 mod3; otherwise all three do. This is an exact fixed-point test, not a Riemann--Hurwitz-only guess.

In the free case take q=(a+b)/3 and conjugate by the diagonal element with exponent vector (0,q-a,2q-a-b). Direct matrix multiplication conjugates D sigma to zeta_m^q sigma, the same projective transformation as sigma. This conjugation commutes with delta. Hence the only remaining representatives are

    <sigma> ~= C_3,    or    <delta,sigma> ~= C_3 x C_3,

with 3|m. They are free: the nontrivial diagonal elements have distinct eigenvalues, and every other element is a three-cycle with diagonal product one. Although chosen matrix lifts of delta and sigma can commute only up to scalar, they commute in PGL_3 and act as an abelian group on the curve's cohomology.

This exhausts the free abelian actions. The exceptional elliptic Fermat cubic is deliberately excluded; it is outside both (2.1) and the required quotient-genus range.

## 3. Determinants, ranks, and a uniform reflection test

The full H^1 character set of F_m is

    T_m={(a,b,c):1<=a,b,c<m, a+b+c=0 mod m}.

It has (m-1)(m-2) members. The sum m gives holomorphic lines and the sum 2m antiholomorphic lines, up to reversing all conventions. The diagonal graph projectors are algebraic.

For an etale abelian cover, a nontrivial eigenspace has dimension r=2g(B)-2 and holomorphic dimension g(B)-1. For completeness, it is cohomology of a nontrivial rank-one torsion local system on B; H^0 and H^2 vanish, and Euler characteristic gives r. Riemann--Roch applied to the corresponding nontrivial degree-zero line bundle gives the holomorphic dimension. Also

    r = m(m-3)/|H|.                                    (3.1)

In a direct sum of r distinct one-dimensional lines, the ordinary top exterior line is the tensor product of those lines. The same identification on the relevant cohomological image is effected by algebraic projectors and permutation/cup-product correspondences. One must use the usual exterior power of H^1, including the odd-degree signs; there is no claim that a symmetric power of an ordinary vector space is its exterior power.

Here is the elementary certificate we will apply. Suppose c_j are the coordinate multiplicities of r selected triples and satisfy

    c_j=c_(m-j),
    c_(m/2) even when m is even.

Then

    sum_j c_j e_j - (3r/2)ell
      = sum_(1<=j<m/2) c_j R_m(j)
        + [c_(m/2)/2] R_m(m/2),                        (3.2)

where the last term is omitted for odd m. Indeed each e-coordinate agrees; the ell coefficient agrees because sum c_j=3r. The half-coefficient is integral, not an illicit division by two in a quotient group.

Through U42's cocycle construction and [OY, Section 4.2], (3.2) is already justified by the existing characteristic-zero correspondence calculus. This also gives algebraicity for these determinant images by known correspondences, independently of relying on the auxiliary proof lines of [PZ] discussed in the source audit. No new relations are obtained by declaring these same words zero a second time.

## 4. Diagonal cyclic covers: all orders and characters

Use (2.2), q=m/h and chi(g)=zeta_h^k with 1<=k<h. The selected triples satisfy

    a+s b=k mod h.

For each 1<=j<m their total coordinate multiplicity is

    c_j = 3q
      -1_(j=k)-1_(-j=k)
      -1_(s j=k)-1_(-s j=k)
      -1_((s-1)j=k)-1_(-(s-1)j=k),                    (4.1)

where all six equalities in the subscripts are modulo h.

Derivation: fixing a=j leaves q possible b modulo m before excluding b=0 and b=-j, yielding q-1_(k=j)-1_(k=(1-s)j). Fixing b=j gives q-1_(k=sj)-1_(k=(s-1)j). Fixing c=j gives q-1_(k=-sj)-1_(k=-j). These are exact counts even when different exclusions have the same residue modulo h: the two excluded coordinate values are still distinct modulo m.

Formula (4.1) is unchanged under j -> m-j. If m is even, h is odd, so j=m/2 is zero modulo h. None of the six indicators is then one because k!=0. Thus c_(m/2)=3m/h is even. Equation (3.2) proves the theorem for every diagonal case.

The number of selected triples is r=m(m-3)/h. This also follows by counting all pairs modulo h and deleting a=0, b=0, c=0: the three excluded sets are disjoint for k!=0 and each has m/h members. No constant-genus or small-CM-dimension hypothesis was imposed.

## 5. A permutation C_3: the non-diagonal case

Let H=<sigma> and chi(sigma)=omega or omega^2. Cyclic rotation partitions T_m into orbits of size three, except for

    (m/3,m/3,m/3),  (2m/3,2m/3,2m/3).

The two fixed lines have sigma-eigenvalue +1. On holomorphic residues the cyclic coordinate permutation has determinant +1 and fixes the symmetric monomial; the antiholomorphic statement is its conjugate. Hence these lines do not occur for the two characters under consideration.

Each size-three orbit contributes one line to each sigma character. Its chi-eigenline is algebraically isomorphic, on the cohomological image, to any chosen diagonal line in that orbit: if p_chi is the cyclic projector and e_t one diagonal projector, then e_t p_chi e_t=(1/3)e_t; multiplying the inverse map by three gives the inverse on the image. This is a nonzero correspondence, not merely a Hodge-profile match.

Choose one triple from each size-three orbit. Before removing the fixed triples, each coordinate value j occurs 3(m-2) times in T_m. Division by the three rotations after removal gives

    c_j = m-2 -1_(j=m/3)-1_(j=2m/3),
    r = m(m-3)/3.                                     (5.1)

The coefficient is symmetric. For even m, c_(m/2)=m-2 is even. Thus (3.2) applies to both nontrivial permutation characters.

## 6. C_3 x C_3: all eight nontrivial characters

Use H=<delta,sigma>, delta=diag(omega,omega^2,1), and label chi by (k,l) modulo three. A diagonal triple has delta label a+2b mod3, constant on its cyclic orbit because a+b+c=0 mod3. On each size-three orbit all three sigma labels occur once. The two all-equal triples have (k,l)=(0,0), so are absent from every determinant considered here.

For k=1 or2 (any l), choose one triple from each orbit with label k. Counting the selected triples before dividing by three gives

    c_j = m/3 -1_(j=1 mod3)-1_(j=2 mod3).              (6.1)

For k=0 and l=1 or2 it gives

    c_j = m/3 -2*1_(3|j)
                 -1_(j=m/3)-1_(j=2m/3).              (6.2)

One can derive these from the same fixed-coordinate count as (4.1), with h=3,s=2, retaining the k=0 case before removing the two fixed triples. The orbit projector is the nonzero algebraic map described in Section 5.

Each eigenspace has r=m(m-3)/9. Both formulas are symmetric. If m is even, m is divisible by six: the middle coefficient is m/3 in (6.1) and m/3-2 in (6.2), both even. All eight characters therefore have the integral reflection certificate (3.2).

For example, at m=210 the group C_3 x C_3 gives g(F_m)=21736, g(B)=2416, and r=4830. For (k,l)=(0,1), c_105=68 and the reflection multiplicities sum to7245. This is an arbitrary-size determinant construction, not an extension of a bounded small-profile test by extrapolation.

## 7. Consequence for the original degree-70 method

All determinant words above belong to the reflection subgroup at their own level. Passing to a common multiple of levels sends e_j to e_(qj), ell to ell, and R_m(j) to R_(qm)(qj). Consequently arbitrary sums, differences, level changes and tensor combinations of these inputs add no relation beyond those already present.

In particular the order-five and order-seven parity functionals of U44 kill all these inputs. Each has value one on the scaled original target: the additive orders of alpha's entries are

    (70,7,35,5,70,35).

Thus this new source family cannot trivialize the unsquared target through the current reflection/multiplication calculus, at any common multiple of70. U44 supplies the already-proved preservation under multiplication relations. The present conclusion does **not** require classifying all cycles on the Prym variety.

It also does not say that any arbitrary correspondence from a determinant's ambient variety to X must vanish; proving a new such correspondence with nonzero target image would be additional geometry outside the tested method. Nor are ramified covers, generalized Fermat curves, arbitrary subdeterminants, or nonabelian groups covered by this theorem.

## 8. Direct application to U47's four source curves is branched

The natural cyclic actions on the actual fixed curves of U47--U48 do not themselves meet the etale hypothesis. Here is a direct check, rather than an inference from the word "Prym".

For D5: w^10=t^2(1+t^7), put x=t^7. Its function field is also

    w^70=x^2(1+x)^7,
    t=w^40/[x(1+x)^4].

The inverse follows by taking the seventh and second powers of the displayed formula. For D7: v^14=s^6(1+s^5), put x=s^5. Then

    v^70=x^6(1+x)^5,
    s=v^14/[x(1+x)].

These give the same cyclic groups of order70 as the natural residual actions, possibly with a different choice of generator. Their branch exponent lists are respectively (2,7,-9) and (6,5,-11). At infinity the exponent is coprime to70, so there is a unique point above infinity with inertia the full cyclic group. Every nontrivial subgroup fixes that point and is ramified on taking its quotient.

Likewise C5: b^2=a^5+1 has the cyclic presentation (ab)^10=x^2(1+x)^5 with x=a^5, and C7: d^2=c^7+1 has (cd)^14=x^2(1+x)^7 with x=c^7. The inverse uses the coprimality of2 with5 or7. Their infinity exponents are -7 and -9, coprime to10 and14. The same conclusion holds for their natural residual groups.

Riemann--Hurwitz gives genera (31,32,2,3) from these four branch lists, agreeing with the independently derived U48 data. This does not classify every automorphism of these four non-Fermat curves; it excludes direct use of their specified cyclic deck actions as unramified covers.

## 9. Source audit, verification, and remaining work

[PZ] D. Patel and Y. Zhang, *Algebraicity of Hodge classes on some Generalized Prym Varieties*, arXiv:2506.13729v2,23 May2026, Theorems1.1--1.2. https://arxiv.org/html/2506.13729v2 . The etale hypothesis and full determinant, not a selected tensor factor, define the tested family. The primary PDF was also opened and printed pages4 and11 visually inspected. Two auxiliary displayed conventions require correction: the map x->d[x] multiplies H_1 by d, not by1; the subgroup (g,-g,0,...) maps to zero under the sum quotient, not isomorphically. The source audit gives the elementary corrected formulas. These discrepancies are not used to refute the main theorem; U49's formal conclusion and its special-case correspondence justification do not depend on those problematic lines.

[H] T. Hayashi, *Orders of automorphisms of smooth plane curves for the automorphism groups to be cyclic*, Arabian J. Math.10(2021),409--422, DOI10.1007/s40065-021-00321-5, Definition2.1 and Theorem2.2. https://link.springer.com/article/10.1007/s40065-021-00321-5 . Used only for the full monomial automorphism group of F_m for m>=4; the free-subgroup classification is proved in Section2. Its original attribution is P. Tzermias, J. Number Theory53(1995),173--178. The earlier alternative-proof publisher endpoint timed out, and is not passed off as a directly read proof.

[OY] N. Otsubo and T. Yamazaki, *Motivic Gauss and Jacobi sums*, arXiv:2402.06072v3,2 March2025, Section4.2, Propositions4.7,4.8,4.11. https://arxiv.org/html/2402.06072v3 . The same characteristic-zero Jacobi-motive inputs were rechecked; the zero/partial-sum conventions and group extension are in U42 Section3. No Gauss sum is lifted from finite characteristic without a correspondence.

All new source checks occurred on15 September2026. No claim of global novelty or expert acceptance is made. The subgroup facts are classical in context; the new research contribution here is the explicit, all-degree source-to-relation audit for this attempted route.

Run `python research/computations/U49/verify_u49.py --output research/computations/U49/verification.json`.

Ten new tests pass, covering 16296 parameter/character cases across41 distinct degrees (16136 diagonal and160 non-diagonal), complete curve populations, all determinant coefficients, integral reflection recovery, Hodge balance, freeness and centralizer inputs, negative controls, scaled-target parity and the four source-curve ramification lists. These counts count the stated parameterization, not quotient isomorphism classes. Eight inherited U42 tests also pass. A separate stateless Wolfram implementation verifies1228 diagonal cases and the non-diagonal formulas at seven degrees including210. Two malformed preliminary Wolfram calls were discarded and corrected; the coefficient census and the projector/ramification check both passed on rerun. Native lint/static type checking remain unperformed because ruff/mypy are absent; syntax compilation is checked separately. These computations corroborate but do not replace the uniform proof.

**Remaining mathematical task:** obtain a genuinely new target-bearing input, for example from an etale cover with a different upstairs curve and a proved transport, a ramified/generalized-Prym theorem in the required form, or a coupled surface correspondence on the U46 mixed product. None is assumed here. No original target cycle has been constructed, and U48's product-domination obstruction has not been weakened or generalized without proof.
