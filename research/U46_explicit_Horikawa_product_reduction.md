# U46: two explicit degree-ten surfaces and the remaining mixed-product correspondence

**Status:** the restricted geometric reduction and the two self-product results below are proved by the displayed arguments, with exact arithmetic corroboration and adversarial self-review; not formally verified or independently expert-reviewed. No cycle representing the original degree-70 target, and no resolution of the full rational Hodge conjecture, is claimed.

Date: 2026-09-15. Pinned remote base: `Joe-Simo/hodge-conjecture@8fff2a01be0453fc613c0776239085816c155fdd` (U45). Work is confined to `/mnt/data/hodge-conjecture` and the dedicated private repository. Existing input hashes and restoration of missing checkers are recorded under `research/computations/U46/`. Historical results are not globally revalidated.

## 1. Exact result and relation to the previous work

Keep the original target

    X = {sum_(i=0)^5 z_i^70 = 0} in P^5_C,
    alpha = (1,20,24,42,61,62),
    K = Q(zeta_70).

Let W be its 24-dimensional rational primitive character-orbit block. Its Hodge type is (2,2). The universal project target is still rational Hodge for all smooth projective complex varieties, not only W.

In weighted projective space with coordinates [T:X:Y:Z] of weights (1,1,2,5), define

    S5_bar: Z^2 + Y^5 + X^9 T + X^2 T^8 = 0,
    S7_bar: Z^2 + Y^5 + X^7 Y T + T^10 = 0.               (1.1)

Let S5 and S7 be their minimal resolutions. These are actual smooth projective surfaces, not just formal character lists.

**Theorem.**

1. Both surfaces are minimal surfaces of general type with K^2=1, p_g=2, q=0 and b2=33. Their canonical models have respectively one A4 and one A1 rational double point. Their Picard numbers are respectively 5 and 3.
2. Their rational transcendental Hodge structures decompose as

       T(S5) = R5 (+) C10,  ranks 24+4,
       T(S7) = R7 (+) C14,  ranks 24+6.

   All four summands are simple. R5 and R7 have Hodge numbers (1,22,1) and are abstractly Hodge-isomorphic; C10 and C14 have Hodge numbers (1,2,1) and (1,4,1).
3. The codimension-two rational Hodge spaces of S5 x S5, S7 x S7 and S5 x S7 have dimensions 55, 41 and 41, respectively. All such classes on each **self-product** are algebraic, using divisors and graphs of finite-order automorphisms.
4. On the **mixed product** S5 x S7, 17 dimensions are supplied by point/fundamental classes and products of divisors. The remaining 24-dimensional space is related to W by invertible, degree-preserving algebraic correspondences on its cohomological image. Therefore

       W is algebraic on X
       iff rational Hodge holds in codimension 2 on S5 x S7.        (1.2)

   Equivalently, a single algebraic cycle on the mixed product with a nonzero R5 tensor R7 component suffices; it has not been constructed.
5. S5 and S7 are not birational. Neither R5 nor R7 admits a nonzero Hodge map to or from H^2 of a K3 surface. Consequently a correspondence factoring through those K3 H^2 spaces cannot supply the missing map.

The raw (1,22,1) surface-profile lead was already present in U42 Section 7; that observation is **not** counted as new. U46 supplies small explicit canonical models, resolves their singularities, computes their Picard/transcendental data, and isolates exactly the mixed-product problem. These are special-case results and reductions, not a proof of algebraicity of W.

## 2. Extracting the surface pair from the U45 boundary

Partition alpha, after permuting coordinates, as

    A=(1,42,62), B=(20,24,61), sum(A)=sum(B)=105.

Adjoining the opposite balancing residues gives Fermat-surface characters

    beta=(1,42,62,35), gamma=(20,24,61,35).                (2.1)

They arise directly from U45's four boundary curve triples: its third and fourth triples combine to beta by cancelling (63,7); its first and second combine to gamma by cancelling (55,15). The curve-to-surface comparison is the usual Fermat factorization, with no Tate shift. Thus this is a geometric continuation of that boundary rather than another search among the excluded small profiles.

For a nonzero balanced four-tuple a modulo 70, use the convention

    g_a(u)=sum_i <u a_i>_70 / 70 - 1.

Grades 0,1,2 correspond to Hodge types (2,0),(1,1),(0,2); reversing the convention everywhere has no effect on any conclusion. Every unit orbit in (2.1) contains 24 distinct characters and has grade counts (1,22,1). More precisely,

    beta:  grade 0 at u=17, grade 2 at u=53;
    gamma: grade 0 at u=53, grade 2 at u=17;
    g_beta(u)+g_gamma(u)=2 at all 24 units.              (2.2)

This is an equality of full CM Hodge profiles, not merely of Hodge numbers. Identifying each rank-24 summand with K as a rational vector space, the map t -> conjugate(t) matches their embedding grades because g_gamma(-u)=g_beta(u). It gives the stated rational Hodge isomorphism; it supplies neither an algebraic correspondence nor an isometry for the chosen intersection pairings. The Fermat eigenspace decomposition and grade rule are the classical ones [1]; [2, Section 4] supplies the algebraic character projectors and factorization correspondences.

## 3. Explicit quotient function fields

Let F={x0^70+x1^70+x2^70+x3^70=0} in P^3. Work on its coordinate torus.

### 3.1 The beta quotient

On x0=1 set a=x1^14, b=x2^2, c=x3^35. The first quotient has equation

    1+a^5+b^35+c^2=0.                                   (3.1)

Its first-stage deck group has order 14*2*35=980. The target character on (a,b,c) has exponents (3 mod5,31 mod35,1 mod2). Its remaining kernel has order 5 and is generated by

    (a,b,c) -> (zeta_5 a,zeta_5^2 b,c).

The invariant rational functions

    X=b^5, Y=a b^2, Z=c b^5                              (3.2)

satisfy Z^2+Y^5+X^9+X^2=0. Conversely, away from X=0, choose b^5=X and reconstruct a=Y/b^2 and c=Z/X. Thus the extension of function fields has degree at most 5; the five faithful automorphisms give equality and prove that these functions generate the fixed field. Homogenization is exactly S5_bar in (1.1).

In the original four-character lattice, X,Y,Z have characters

    (60,0,10,0)=60 beta,
    (52,14,4,0)=52 beta,
    (25,0,10,35)=25 beta.                               (3.3)

Their subgroup is exactly <beta>, of order 70. The total quotient has degree 4900 and kernel ker(beta) in mu_70^4/mu_70, not a guessed transpose of an exponent matrix.

### 3.2 The gamma quotient

On x2=1 set a=x0^10, b=x1^2, c=x3^35. The first quotient is

    1+a^7+b^35+c^2=0,                                   (3.4)

with first-stage degree 10*2*35=700. The residual target character is (2 mod7,12 mod35,1 mod2). Its kernel of order 7 is generated by

    (a,b,c) -> (zeta_7 a,zeta_7 b,c).

Now take

    X=a/b, Y=b^7, Z=c.                                  (3.5)

These give Z^2+Y^5+X^7 Y+1=0. Reconstruct b from b^7=Y and then a=Xb,c=Z. Again the degree equals 7 by the faithful kernel action. The correct small canonical compactification is the degree-ten S7_bar in weights (1,1,2,5), not the naive double-octic compactification.

The three pullback characters are

    (10,68,62,0)=32 gamma,
    (0,14,56,0)=56 gamma,
    (0,0,35,35)=35 gamma.                               (3.6)

They generate <gamma> of order 70, and the full degree from F is 4900.

A generically finite quotient followed by resolution identifies the **transcendental** H^2 with the invariant transcendental H^2 upstairs. To see this without equating two singular cohomology theories, resolve the rational map. The pull-push composition is its degree, and the other composition on the transcendental part is the sum of deck graphs; the additional resolution terms factor through divisor classes and act trivially there. Blowups of smooth surfaces at points add only algebraic H^2. This proves the invariant comparison used below. It is not a claim that full H^2 is unchanged by these birational operations.

## 4. Smoothness, singularities and surface invariants

The degree-ten polynomials are irreducible: considered as quadratic polynomials in Z over C(T,X,Y), their negatives are not squares, since their degree in Y is odd. They are normal because their singular loci are isolated.

The singular locus of P(1,1,2,5) consists of its two isolated points supported only in Y or only in Z. Neither is on either surface. Thus adjunction is applied entirely in the smooth ambient locus. The charts T != 0 and X != 0 cover everything except T=X=0; there Y and Z are both nonzero on the surface and the Z derivative is nonzero.

On S5_bar, the T=1 chart has the sole singular point X=Y=Z=0. Its equation is

    Z^2+Y^5+X^2(1+X^7)=0.

The local analytic change X'=X sqrt(1+X^7) identifies it with Z^2+X'^2+Y^5=0, the A4 singularity. The X=1 chart has no singularity. Its resolution contributes a chain of four (-2)-curves.

On S7_bar, the T=1 chart is smooth. On X=1 the sole singular point is T=Y=Z=0, with equation

    Z^2+Y T+Y^5+T^10=0.

Its quadratic Hessian has determinant -2, so the holomorphic Morse lemma gives an A1 singularity. Its resolution contributes a single (-2)-curve. These statements are independently corroborated by exact Groebner calculations; singularity classification is the displayed analytic argument, not a solver assertion.

Weighted adjunction gives K_bar=O(10-(1+1+2+5))=O(1). Rational double points are canonical, so on the resolutions K is its pullback. It is nef and big, proving minimality and general type. Weighted intersection gives

    K^2=10/(1*1*2*5)=1.

The two degree-one monomials T,X give p_g=2. The finite rational covers from the Fermat surface give q=0 by the injectivity of H^1 pullback and H^1(F,Q)=0. Noether's formula then gives c2=12(1+2)-1=35 and b2=35-2=33. The degree-ten canonical-model description is consistent with the classical (1,2)-surface classification [3,4]; the particular hypotheses and singularities have been checked here rather than inferred merely from the weights.

## 5. Complete transcendental and Picard calculation

The only primitive Fermat characters invariant under ker(beta), respectively ker(gamma), are the nonzero-coordinate multiples k beta, respectively k gamma. Exhausting k=1,...,69 gives:

| Model | Conductor | Number | h20,h11,h02 |
|---|---:|---:|---|
| S5 | 70 | 24 | 1,22,1 |
| S5 | 10 | 4 | 1,2,1 |
| S7 | 70 | 24 | 1,22,1 |
| S7 | 14 | 6 | 1,4,1 |

There are no other nonzero-coordinate invariant characters. Each row is one complete coefficient-Galois orbit and one irreducible rational representation of the residual cyclic group. Its rational (1,1) subspace is invariant under that group, because the group acts by Hodge automorphisms. Such a subspace is therefore either zero or the whole row. The latter is impossible since h20=1. Consequently each row has no nonzero rational (1,1) classes and belongs to the transcendental part.

Each row is also **simple as a rational Hodge structure**: polarizable rational Hodge structures are semisimple; in a decomposition of a row with h20=1, one summand would have no (2,0) or (0,2), hence would be a rational (1,1) substructure, which was just excluded.

Thus T(S5) has rank at least 28 and T(S7) rank at least 30. To check that no transcendental or algebraic part was missed, we give independent divisor lower bounds.

For S5, K and the four exceptional curves have Gram matrix [1] direct sum minus the A4 Cartan matrix, of determinant 5. They are independent, so rho>=5. Since b2=33 and rank T>=28, rho<=5. Therefore rho=5 and rank T=28 exactly.

For S7, let E be the A1 exceptional curve and let C be the strict transform of

    Y=0, Z=i T^5.

This is a rational curve parametrized by [T:X]. Its canonical degree is 1. It meets E once: in the local blowup T-chart its parametrization is Y/T=0, Z/T=i T^4, so it meets the exceptional divisor transversely. It is smooth after that blowup. Adjunction gives C^2=-3. The matrix of K,E,C is

    [1  0  1
     0 -2  1
     1  1 -3],

whose determinant is 7. Thus rho>=3; the rank-30 transcendental lower bound forces rho=3. This proves completeness without assuming a computed list of cycles generates all cycles. No assertion that these displayed divisors are an integral basis of NS is needed.

As an independent normalization check, the residual cyclic actions on affine X,Y,Z are respectively

    (zeta^60 X,zeta^52 Y,zeta^25 Z),
    (zeta^32 X,zeta^56 Y,zeta^35 Z).

The two canonical forms have character exponents (17,7) for S5 and (53,15) for S7. They agree with the two grade-zero entries in the respective complete character census.

## 6. Hodge classes on the three products

All statements here use rational cohomology. Since q=0, only H^0 tensor H^4, H^2 tensor H^2, and H^4 tensor H^0 contribute to H^4 of a product. The first and last give two algebraic directions. Inside H^2 tensor H^2, the products of Neron-Severi classes give rho(S_i)rho(S_j) algebraic directions. Cross terms between NS and T have no rational Hodge class.

It remains to examine the complete transcendental pieces. For each pair of invariant primitive characters (k beta,l gamma), a rational character orbit is Hodge precisely when

    g_beta(uk)+g_gamma(ul)=2 for every unit u modulo70.    (6.1)

This criterion is complete: the rational Hodge subspace is stable under the two algebraic cyclic actions, and hence is a sum of irreducible rational character orbits; an orbit is included exactly when all its complex lines are of type (2,2).

The full finite enumeration yields the following, with no cutoff on cohomology beyond the complete lists in Section5:

- S5 x S7: exactly (k,l)=(u,u) for the 24 units u; no pair involving C10 or C14 survives.
- S5 x S5: exactly (k,l)=(k,-k) for all 28 allowed k.
- S7 x S7: exactly (k,l)=(k,-k) for all 30 allowed k.

The mixed result also follows from (2.2) and the trivial stabilizer of its unique (2,0) embedding; different-rank simple Hodge summands have no nonzero maps between them. The exact checker and a separate Wolfram calculation verify the entire finite comparison.

Hence the dimensions are

    dim Hdg^4(S5 x S5)=2+25+28=55,
    dim Hdg^4(S7 x S7)=2+9+30=41,
    dim Hdg^4(S5 x S7)=2+15+24=41.                      (6.2)

For each self-product, all transcendental Hodge classes are algebraic. Indeed the graphs of powers of the residual cyclic automorphism, restricted to the transcendental H^2, span all its diagonal character endomorphisms. Their rational span has dimension deg(Phi_70 Phi_10)=28 or deg(Phi_70 Phi_14)=30. The restriction can be made by algebraic cohomological projectors: remove H^0,H^4 using a point, and remove NS using the inverse rational intersection matrix of its divisor basis. These are rational algebraic correspondences. No assertion about lifting a conjectural Hodge endomorphism is needed. They span the 28 or30 lines just counted, proving the self-product assertions.

This argument does not provide the off-variety Hodge isomorphism R5 -> R7. Having all algebraic endomorphisms on both sides is not a proof that a Hodge isomorphism between them is algebraic.

## 7. Exact transport of the mixed block to the original fourfold

For two copies of F, choose epsilon with epsilon^70=-1 and use the Shioda-type rational map

    ([x0:x1:x2:x3],[y0:y1:y2:y3])
      |-> [x0 y3:x1 y3:x2 y3:
           epsilon x3 y0:epsilon x3 y1:epsilon x3 y2].    (7.1)

Its coordinate 70th powers sum to zero. On the open set where the sum of the first three target powers is nonzero, normalizing x3=y3=1 leaves exactly 70 choices of common scalar, so it is generically finite of degree70.

Blow up the base C70 x C70 defined by x3=y3=0 to obtain a morphism. The blowup's extra H^4 is H^2(C70 x C70)(-1). Scaling x3 alone, or y3 alone, acts trivially on that exceptional contribution. Because beta3=gamma3=35 are nonzero, that contribution has no beta tensor gamma character, nor any of its unit conjugates. The only compatible Kunneth term is H^2(F) tensor H^2(F).

Pullback of the reordered target (A,B) in (2.1) has source character beta tensor gamma, directly by counting x3 and y3 exponents. The pullback is nonzero because proper push-pull is multiplication by70. Each eigenspace is a line, so it is an isomorphism onto that line. This is the exact product-of-surfaces version of the Fermat comparison; [1, Section1] and [2, Section4] describe the general mechanism. The elementary map, degree, character, and exceptional-term checks here fix its application and show that there is **no Tate shift**.

The quotient maps of Section3 identify the beta and gamma orbit summands with R5 and R7 by algebraic graph correspondences. On the transcendental pieces, divide their pushforward by4900 to invert pullback. Combining these with (7.1) gives inverse algebraic correspondences between W and

    H_mix = direct sum_(u in units70) V(u beta) tensor V(u gamma).

All coefficient-field projectors can be summed over the simultaneous unit orbit; the sums have rational coefficients. These maps act on H^4 and preserve codimension-two cycle classes. The factors epsilon and roots of unity are algebraic *fields of definition* of graphs, not non-rational coefficients in their cycles.

Therefore H_mix is algebraic if and only if W is algebraic. The other17 Hodge directions of the mixed product have already been exhibited. This proves (1.2). If a cycle has any nonzero H_mix component, applying its rational orbit projector and the two cyclic actions spans all24 directions, because this is one irreducible rational character orbit. This supplies the stated single-cycle criterion, but not its witness.

## 8. Two shortcuts rejected and the executable next problem

The ranks 28 and30 of the full transcendental parts are birational invariants of smooth projective surfaces: point blowups add only algebraic classes. Hence S5 and S7 are not birational; a graph of a birational map cannot supply the missing correspondence.

Each R_j is simple and has rank24. A nonzero Hodge map from H^2 of a K3 surface to R_j would be surjective onto that simple summand; a nonzero map in the other direction would be injective. Both are impossible because b2(K3)=22 [5]. The same reasoning rules out a factorization through a finite direct sum of such K3 H^2 spaces. Buskin's theorem [6] concerns actual K3 surfaces and Hodge **isometries**, not arbitrary rank24 K3-type structures. We have proved a Hodge isomorphism here, not a polarization-preserving isometry, and do not silently replace those notions.

On T=1, the canonical pencils are explicit genus-two curves:

    S5: Z^2+Y^5+(X^9+X^2)=0,
    S7: Z^2+Y^5+X^7 Y+1=0.

The first becomes constant after adjoining a tenth root of -(X^9+X^2). The second quintic has discriminant 3125+256 X^35. These identities are recorded as constructive data; the discriminant alone is not used as a proof about generic isogeny or non-isotriviality.

**Next obligation:** find a codimension-two algebraic cycle Gamma on this specific mixed product whose R5 tensor R7 component is nonzero, for example a correspondence between the indicated genus-two fibrations not reducible to ambient divisor intersections. A surface produced merely as an intersection of two divisors on the smooth product has class in the already algebraic17-dimensional part and is insufficient. Arithmetic field restrictions in U39-U40 must also be respected; defining the surfaces over Q does not define all their Hodge cycles over Q.

No blanket Hodge conjecture for Horikawa surfaces, no theorem converting profile equality into algebraicity, and no conclusion from a tensor square to its root is assumed.

## 9. Sources and reproducibility

[1] T. Shioda and T. Katsura, *On Fermat varieties*, Tohoku Math. J.31 (1979),97-115, DOI10.2748/tmj/1178229881, Sections1-3. The classical character decomposition and residue grading are used; the needed product map and exceptional terms are explicitly derived in Section7 here. The source and conventions are also pinned in U42. https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf

[2] N. Otsubo and T. Yamazaki, *Motivic Gauss and Jacobi sums*, arXiv:2402.06072v3, Section4.2, Propositions4.6-4.11 and Corollary4.13. Directly rechecked, including character pullback in(4.6) and the exceptional-term calculation. https://arxiv.org/html/2402.06072v3

[3] M. Franciosi, R. Pardini and S. Rollenske, *Gorenstein stable surfaces with K_X^2=1 and p_g>0*, arXiv:1511.03238, Theorem3.3(i). The canonical degree-ten format is checked against this source; the implication for our particular surfaces uses the adjunction and ADE verification given above, not the converse of an unstated classification. https://arxiv.org/html/1511.03238

[4] P. Gallardo, G. Pearlstein, L. Schaffler and Z. Zhang, *Unimodal singularities and boundary divisors in the KSBA moduli of a class of Horikawa surfaces*, arXiv:2209.08877v2, Section2.1; published Math. Nachr.297(2024),595-628, DOI10.1002/mana.202300019. Used for the (1,2)-surface terminology and canonical-model context, not for an algebraic-correspondence theorem. https://arxiv.org/html/2209.08877v2

[5] D. Huybrechts, *Lectures on K3 surfaces*, author-hosted prepublication draft, Chapter1, formula(2.7), printed p.13 (PDF index12). Its rendered Hodge diamond gives b2=22. Read online only; the draft is not redistributed in this package. https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf

[6] N. Buskin, *Every rational Hodge isometry between two K3 surfaces is algebraic*, arXiv:1510.02852v3, Theorem1.1; published J. reine angew. Math.755(2019),127-150, DOI10.1515/crelle-2017-0027. Used only to delimit an inapplicable shortcut. https://arxiv.org/html/1510.02852v3

All new source inspections were on15 September2026. The current-run J-STAGE PDF requests for [1] failed; its previously pinned record is distinguished from the freshly read [2], and Section7 supplies the needed map directly. The served arXiv HTML can show a regenerated manuscript date distinct from the version header; the source record preserves this distinction. No global novelty claim is made for the models or the classical consequences derived from them.

Run:

    python research/computations/U46/verify_u46.py --output research/computations/U46/verification.json

Ten focused tests cover all character multiples, all unit comparisons, quotient kernels, polynomial substitutions, all projective singularity charts, divisor-matrix determinants and the original product-map identity. A separate Wolfram run recomputes the principal outputs. The proof of the source-to-target implication is Section7, not the passing test count. See `source_and_self_review.md` and `run_manifest.json` for limits and actual validation results.
