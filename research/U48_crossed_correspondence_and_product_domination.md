# U48: an explicit crossed correspondence and a product-domination obstruction

**Status:** the restricted statements below are proved by the displayed geometric and Hodge-theoretic arguments, with exact arithmetic corroboration and adversarial self-review. No formal or independent expert verification. No cycle representing the original degree-70 target, and no resolution of the rational Hodge conjecture, has been obtained.

Date: 2026-09-15. Base: `Joe-Simo/hodge-conjecture@2b2032a2c846436b0105ec426147a640db8f721b` (U47). Work is confined to `/mnt/data/hodge-conjecture` and this private repository. The full supplied Hodge prompt was read; its SHA-256 is `0639b0689036cee1ed7a990147fba250ee3188d5bc3143dc2625e50d4d85bbb3`. Existing files and archives are preserved. U47's local proof has the exact remote blob `aa8ac3d9f6cc7d2494a61681a243d9637b6ee724`.

## 1. Target and what was actually attempted

Keep U46-U47's smooth projective resolutions S5 and S7 of

    S5_bar: Z^2+Y^5+X^9 T+X^2 T^8=0,
    S7_bar: Z^2+Y^5+X^7 Y T+T^10=0,

in P(1,1,2,5). Their mixed rank-24 Hodge block is equivalent, by the pinned algebraic correspondences, to the original character block W on the Fermat fourfold of degree70. This is only one subproblem of the universal rational Hodge conjecture.

Let all curves below denote their smooth projective normalizations:

    D5: w^10=t^2(1+t^7),       C5: b^2=a^5+1,
    D7: v^14=s^6(1+s^5),       C7: d^2=c^7+1.

Write Y4=D5 x C5 x D7 x C7. The genera are (31,2,32,3). U47 gives rational covers phi5:D5 x C5 -> S5 and phi7:D7 x C7 -> S7 of degrees10 and14, respectively. Their product transports the missing block to a rational subspace Wtilde of H^1(D5) tensor H^1(C5) tensor H^1(D7) tensor H^1(C7), with inverse on the image supplied by normalized pushforward.

The attempt here is **not** a fibre-matching correspondence over a base curve: the crossed surface below dominates both of U47's two-dimensional base products.

**Results.**

1. There is an explicit irreducible surface Gamma on S5 x S7 whose projections to each Si have degree35. It dominates the base products for f5 x g7 and f5 x f7 with degrees70 and50, respectively. It has zero missing-block projection.
2. Every divisor-product class on Y4 has zero Wtilde projection.
3. More strongly, if an irreducible surface Z in Y4 is dominated by a product of two smooth projective curves, then [Z] has zero Wtilde projection. This includes arbitrary source genera, degrees, and complex fields of definition, not merely the explicit crossed construction.

Statement3 is about surfaces **in this fixed four-curve cover**, not all product-dominated surfaces on S5 x S7 or on the original Fermat fourfold. Pulling back a product-dominated surface through a finite cover need not produce a product-dominated surface; we do not use that false inference. Failure of the tested constructions is not nonalgebraicity of W.

## 2. Crossed maps that genuinely couple the bases

The new curve maps are particularly simple:

    h:D5 -> C7,    (t,w) |-> (t,w^5/t),    degree5,
    k:D7 -> C5,    (s,v) |-> (s,v^7/s^3),  degree7.       (2.1)

Their equations follow directly from those of D5,D7. For h, w satisfies w^5=t*d over C7; the faithful order5 action on w gives the full degree. For k the corresponding equation is v^7=s^3*b and the faithful order7 action gives the full degree. Rational maps between smooth projective curves extend over the missing affine points.

Form the crossed graph surface

    j:D5 x D7 -> Y4,
       (p,q) |-> (p,k(q),q,h(p)).                       (2.2)

It is a closed embedding, since the first and third coordinates recover p and q. Compose with phi5 x phi7. In the affine charts T=1 this gives

    S5: (X5,Y5,Z5)=(t, w^2*s, i*w^5*v^7/s^3),
    S7: (X7,Y7,Z7)=(v^2*t/s, s, i*w^5*v^7/(s^3*t)).   (2.3)

Both surface equations vanish identically after substituting the two source curve equations. Let Gamma be the reduced irreducible closure of the image in S5 x S7, resolving rational maps as necessary.

### 2.1 Exact degree and irreducibility

Over C(t,s), the source function field is a Galois extension of degree10*14=140. Its deck group acts by (w,v)->(eta10^a*w,eta14^b*v). The image field contains t=X5 and s=Y7. To fix Y5 and X7 requires eta10^(2a)=eta14^(2b)=1. To fix Z5,Z7 additionally requires (-1)^(a+b)=1. The complete stabilizer is

    (a,b)=(0,0),(5,7).                                 (2.4)

The fundamental theorem of Galois theory therefore gives degree2 from D5 x D7 to Gamma, with Gamma birational to the quotient by the simultaneous involution (w,v)->(-w,-v). In particular Gamma is irreducible and is a surface, not a parameter family counted as one cycle.

The maps to S5 and S7 factor through covers of degrees7*10 and5*14. Dividing by2 proves

    deg(Gamma -> S5)=deg(Gamma -> S7)=35.               (2.5)

The image over the isotrivial bases is (t,s), so deg(Gamma -> P1 x P1)=70. For the canonical second pencil use X7=t*H, where H=v^2/s on D7. At the two points of D7 over s=0, H has a pole of order1; at the single point over infinity it has a pole of order8. These orders follow from the Kummer valuations (ord(s),ord(v))=(7,3), respectively (-14,-11). Thus H has degree10, and (t,X7) has degree10*10/2=50 on Gamma. It too dominates the base product.

Useful elimination identities are

    Z5=t*Z7,
    Y5^5=t^2(1+t^7)s^5,
    X7^7*s=t^7(1+s^5),
    Z7^2=-(1+t^7)(1+s^5).                              (2.6)

These are identities on the stated irreducible image. No claim of a complete unsaturated projective ideal is needed.

Resolutions introduce exceptional curves, not a second dominant surface component; generic degrees and the following cohomological calculation are unaffected. Gamma is a nonzero algebraic cycle: either projection has positive degree35. Its failure is a zero **target projection**, not a zero total cycle class.

## 3. Exact character coordinates for the missing block

Fix zeta=exp(2*pi*i/70), with pullback as the action on cohomology. Use the automorphisms

    delta5(t,w)=(zeta^40*t,zeta*w),
    epsilon5(a,b)=(zeta^14*a,zeta^35*b),
    delta7(s,v)=(zeta^14*s,zeta*v),
    epsilon7(c,d)=(zeta^10*c,zeta^35*d).                (3.1)

They have orders70,10,70,14. All preserve the stated equations. Denote an eigenline of the appropriate action by L_i(k).

The cyclic70 presentations for the large curves are

    D5: w^70=x^2(1+x)^7, x=t^7,
    D7: v^70=x^6(1+x)^5, x=s^5.                       (3.2)

There is no extra isogeny assumption in (3.2): the inverse rational expressions are t=w^40/(x(1+x)^4) and s=v^14/(x(1+x)). Thus the branch exponent triples are (2,7,61) and (6,5,59).

For the action y->zeta*y on a cyclic cover with branch tuple a, the k-eigenspace of holomorphic differentials has dimension

    d(k)=-1+sum_j fractional_part(-k*a_j/70).           (3.3)

The primitive characters here have all three residues nonzero, so d(k) is either0 or1. It equals1 exactly when the positive residues of k*a sum to70. Formula(3.3), including its sign, is the eigendifferential basis in Moonen [1, Section2, final lemma; Section3, definition of d_n]. The branch point at infinity may be moved to a finite point; the author explicitly explains this convention. No theorem about generic endomorphism rings is used.

One can also derive (3.3) by writing a k-eigendifferential as y^(k-70) times a rational differential on P1, imposing the integer valuation inequalities at its three branch points, and counting the allowed polynomial degrees. This gives the same floor/fractional-part formula.

For k a unit modulo70 the holomorphic sets are

    D5: {1,3,11,13,23,31,37,41,43,51,53,61},
    D7: {1,3,17,19,29,31,37,43,47,57,59,61}.           (3.4)

For C5 and C7 the bases da/b,a*da/b and dc/d,c*dc/d,c^2*dc/d give the holomorphic character sets

    C5: {49,63},             C7: {45,55,65}.           (3.5)

The remaining H^1 characters in each conjugate orbit are antiholomorphic.

### 3.1 The comparison with R5 and R7, not just a guessed Hodge tuple

The affine canonical forms dX wedge dY/Z on S5,S7 pull back, up to nonzero constants and wedge order, to

    (dt/w^3) tensor (da/b),
    (s^2*ds/v^5) tensor (dc/d).                        (3.6)

Their character pairs under(3.1) are respectively (37,49) and (37,45). The other canonical forms pull back to (t*dt/w^3) tensor (da/b) and (s*ds/v^3) tensor (c*dc/d); their lower-order D-characters are7 and25. These are separated from the full-order70 pieces being studied.

The forms in(3.6) are regular. For example dt/w^3 has orders1 over t=0,6 over a root of1+t^7, and16 at infinity. The analogous orders of s^2*ds/v^5 are5,8,12. These nonnegative valuations provide a separate check that the character normalization is geometric.

Taking the simultaneous unit orbit of either pair in(3.6) gives24 lines with Hodge counts(1,22,1), the pinned R5 or R7. At the identity unit both pairs are holomorphic two-forms. The mixed Hodge block pairs the first with the complex conjugate of the second. Consequently, after this harmless reindexing of the orbit,

    Wtilde_C = direct sum_(u in (Z/70)^*)
      L_D5(37u) tensor L_C5(49u)
      tensor L_D7(33u) tensor L_C7(25u).               (3.7)

Here 33=-37 and25=-45 modulo70. There are24 distinct summands and each is of type(2,2). This is the image of the **original** block through U46-U47, not a newly substituted example. Its rational projector is the simultaneous coefficient-Galois sum of the four character projectors.

## 4. No pair in the target can come from a divisor

For a pair of factors i,j in Y4, let p_i(u) be1 when its target character in(3.7) is holomorphic and0 otherwise. A necessary condition for a rational divisor class on that pair to contribute to the selected character line is

    p_i(u)+p_j(u)=1 for every unit u modulo70.          (4.1)

Reason: a divisor class is rational and type(1,1). Algebraic automorphisms preserve the Hodge decomposition, so all character projectors preserve it. Coefficient conjugation permutes the projectors and fixes a rational cohomology class. If one conjugate eigenspace is type(2,0) or(0,2), its projected divisor class is zero; conjugating back makes the original projection zero. This concerns rational cycle coefficients, not the field over which its defining equations happen to lie.

Every one of the six pairs fails(4.1):

| Pair | First witnessing unit | Two holomorphic indicators | Number of failing units |
|---|---:|---|---:|
| D5,C5 | 1 | (1,1) | 2 |
| D5,D7 | 3 | (1,1) | 12 |
| D5,C7 | 13 | (1,1) | 10 |
| C5,D7 | 13 | (0,0) | 10 |
| C5,C7 | 3 | (0,0) | 12 |
| D7,C7 | 1 | (0,0) | 2 |

This is a complete24-unit calculation with a small explicit witness for each pair. It remains true for every conjugate target summand, since multiplication by a unit permutes the witnesses. The positive control C5 x C5 with character pair(49,21) does satisfy(4.1); diagonal divisor classes are not erroneously excluded.

The Kunneth decomposition of a divisor on Y4 has terms in H^2 of one factor and in H^1 of two factors. To reach H^1 of all four factors in a product of two divisors, one must select two disjoint pair terms. The table kills each such term. Hence the entire divisor-product subspace has zero Wtilde projection.

For the particular crossed graph there is an even shorter independent check. In(2.1), h is equivariant for delta5 on D5 and epsilon7^11 on C7; k is equivariant for delta7 and epsilon5. The target exponents on those graph pairs have sums

    37+11*25=32 mod70,        33+49=12 mod70.           (4.2)

Both are nonzero, including after multiplication by any unit. The graph cycles are invariant under these automorphisms, so their selected projections vanish. The crossed surface(2.2) is the product of the two graph cycles on the disjoint factor pairs. It has zero Wtilde projection, and the projection formula with the U47 transport proves that Gamma has zero missing-block projection on S5 x S7.

Thus dominance of both base products is necessary by U47, but is demonstrably **not sufficient**. This is a concrete example, not just a proposed warning.

## 5. Uniform extension to all product-dominated surfaces in Y4

We prove the geometric lemma needed here rather than guessing that an arbitrary morphism is separated.

**Factorization lemma.** A nonconstant morphism A x B -> C from two smooth projective connected complex curves to a curve of genus at least2 factors through A or B. The same is true for a rational map.

For the morphism case, pullback injects H^0(C,Omega^1), a space of dimension at least2, into H^0(A,Omega^1) direct sum H^0(B,Omega^1). Wedges of any two pulled-back forms vanish, because they came from a curve. If U is a subspace of V direct sum W of dimension at least2 satisfying v tensor w'=v' tensor w for every two elements, then U is contained in V or in W: when both projections are nonzero the tensor equality forces each projection to have rank one and to determine the other, giving dimension at most1. This contradiction proves the linear assertion. The canonical linear system of a positive-genus smooth curve has no base points, so if all pulled-back one-forms are from A, the differential in the B direction is zero everywhere and the map is independent of B. The other case is symmetric.

For a rational map, resolve indeterminacy by point blowups. Every exceptional rational curve maps constantly to C, by Riemann-Hurwitz; maps contract each connected exceptional tree. The morphism descends through the blowdowns to A x B. Equivalently, the closed graph over the normal source has singleton fibres and is a proper birational quasi-finite map, hence is an isomorphism. This supplies the claimed extension and factorization. Constants are treated separately.

Now suppose A x B dominates an irreducible surface Z in Y4. All four coordinate curves of Y4 have genus at least2. Apply the lemma to the four coordinate maps. If a coordinate map is constant, its H^1 pullback is zero and the target component vanishes. Otherwise each coordinate map uses exactly one source factor, giving a partition of the four coordinates.

If the partition is3+1 or1+3, three H^1 classes must be pulled back to a single curve; their product is zero for degree reasons. A4+0 partition cannot have a surface image. Only2+2 can contribute. In that case the image is the product, on disjoint coordinate pairs, of the two image curves from A and B. Each such image curve is a divisor on its curve-pair surface, so Section4 applies. In every case the Wtilde projection is zero.

Since the map to Z is generically finite, its pushforward is deg(f)[Z]; division by this positive degree is allowed over Q. The argument covers arbitrary source curves and degrees. It is not a finite search over candidate equations. By linearity every rational cycle generated by these surfaces also has zero target component.

## 6. Executed follow-up and next geometric requirement

The crossed maps expose useful algebraic projectors. For h of degree5 and k of degree7,

    e_h=(1/5) h^* h_*,       e_k=(1/7) k^* k_*

on curve H^1 project to the pullbacks from C7 and C5. The complementary projectors are the Prym parts, meaning the parts killed by trace to those lower-genus curves. No conjecture is needed for these graph projectors.

The order5 kernel of h is generated by delta5^14 and the order7 kernel of k by delta7^10. On the target characters these generators have exponents28 and50, respectively, both nonzero for every unit conjugate. Therefore

    (e_h tensor id tensor id tensor id) Wtilde = 0,
    (id tensor id tensor e_k tensor id) Wtilde = 0,

and Wtilde lies in the two complementary Prym parts simultaneously. Any construction factoring either large-curve contribution through the explicit maps(2.1) is excluded before constructing a surface.

A surviving construction in this fixed cover must therefore have a genuine four-factor component, must not be generated by divisor products, and cannot be represented using only surfaces dominated by products of curves. It must also use the complementary trace-zero parts, not the crossed lower-genus quotients. These are necessary conditions, **not evidence that no such cycle exists**.

The next concrete task is to construct an intrinsically non-product-dominated surface in Y4 with nonzero projection under the rational projector(3.7), or an equivalent non-factorizing correspondence on S5 x S7. A generic complete intersection still has divisor-product class and is insufficient. No such witness is asserted here.

## 7. Sources, verification, and adversarial self-review

[1] Ben Moonen, *Special subvarieties arising from families of cyclic covers of the projective line*, Documenta Mathematica15(2010),793-819, DOI10.4171/DM/314, arXiv:1006.3400. The directly inspected arXiv HTML has corrupted subsection numbers; exact locators are Section2's final eigendifferential-basis lemma and Section3's definition of d_n, with the sign convention y->zeta*y. The genus formula and the discussion of a branch point at infinity are also explicit. https://arxiv.org/html/1006.3400

[2] Project U47, pinned commit2b2032a2c846436b0105ec426147a640db8f721b, Sections1,7: fixed curves, covering degrees, and transcendental push-pull comparison. Its exact local blob was checked and its nine tests were rerun. The source-to-original-target comparison also depends on the specified U46 Horikawa reduction; this run does not revalidate all earlier project claims.

The factorization lemma and cycle-class consequences are proved in Sections4-5. The literature lookup did not establish a novelty claim. No claim is made that the general factorization observation is new. The current Clay page was checked and still presents the rational Hodge conjecture as unsolved; this note's status is independently determined by the absent target-cycle witness.

**Self-review:**

- Pair Hodge profiles are checked across all coefficient embeddings, not only the holomorphic forms at the distinguished embedding.
- Curve actions, cyclic presentations, and pulled-back canonical forms fix the character labels. The tuple(37,49,33,25) is not treated as a six-coordinate Fermat character.
- The crossed construction is an actual irreducible surface with fixed equations; its constants are not counted as variables.
- Base dominance and degrees are established, not inferred from a dimension count. The degree2 simultaneous-sign quotient is retained.
- Zero primitive projection is distinguished from zero total cycle class and from rational triviality.
- The product-domination theorem applies to the four-curve cover. It is not transported backwards through arbitrary finite covers without a product-domination proof.
- No abelian-field obstruction, conjectural Hodge isometry algebraicity, or tensor-square extraction is used to prove the new vanishing.
- The arithmetic checker verifies finite inputs, not the Hodge-theoretic and morphism-factorization arguments. Review is by the same assistant; separate Wolfram arithmetic is not expert review.

Run `python research/computations/U48/verify_u48.py --output research/computations/U48/verification.json`. Eight focused new tests and nine rerun U47 tests pass. Separate Wolfram evaluation reproduces the main polynomial, character and deck calculations. Syntax compilation passes. Native ruff and mypy checks were attempted but remain unavailable in the runtime; their failure logs are preserved and no lint/type-check success is claimed.
