# U37: reducibility alone is not enough — component-wise toric obstructions

Status: proved below, with exact finite corroboration and self-review; not formally verified or independently expert-reviewed. A restricted construction obstruction, not a solution of the Hodge conjecture.

Date: 2026-09-15. Base: Joe-Simo/hodge-conjecture@467188a3d6c10a08ab2476fc65c12d14c78771de. U36 and its original evidence are preserved unchanged.

## 1. Target and contract

Let X={sum z_i^70=0} in P^5 over C, h=c_1(O_X(1)), and alpha=(1,20,24,42,61,62). Write e_alpha for the alpha character projector of the diagonal Fermat group G=(mu_70)^6/mu_70. All coefficient statements are in cohomology over a splitting field; their rational counterpart is the full unit-orbit projector e_O.

Let T be the reduced projective closure of a translate of a connected three-dimensional subtorus of the ambient projective torus. Assume T is not contained in X. On its dense torus, restrict the Fermat equation and factor the resulting Laurent polynomial. An irreducible factor is called binomial here if, up to an invertible Laurent monomial, it has exactly two monomial terms.

**Theorem.** If this restriction has at most one non-binomial irreducible factor, then every surface component of T intersect X has zero alpha projection. Consequently a useful component of a toric intersection requires at least two non-binomial components. This condition is necessary, not sufficient.

## 2. Proof, including the boundary and multiplicities

The Chow class of T in P^5 is deg(T) H^2. The refined Cartier-divisor pullback along i:X -> P^5 gives the fundamental intersection cycle

    i^![T] = deg(T) h^2 in CH^2(X).

This is a statement on X, not an inference from equality of degrees or from an injective pushforward. It applies to an integral T with proper intersection and allows component multiplicities. Its alpha projection is zero because h^2 is G-invariant. This is the same standard intersection-theory input used and checked in U36, Section 5.

Every surface component supported on the coordinate boundary is contained in z_j=0 for some j. The automorphism scaling only z_j by a 70th root fixes that component pointwise. Since alpha_j is nonzero, its alpha projection is zero. No irreducibility assumption about the whole boundary is necessary.

An irreducible binomial Laurent factor on the three-dimensional torus defines a translate of a connected two-dimensional subtorus: irreducibility over C forces its exponent difference to be primitive. Its image in the ambient torus is again a two-dimensional torus coset contained in X.

Here is the relevant classification, independently repeated from U36. Express its six coordinates as c_i times torus characters, with c_i nonzero. Their exponent vectors have affine span two. Group the six Fermat terms according to equal exponents. Independence of distinct torus characters forces each group to contain at least two terms. Affine span two requires at least three groups, so exactly three groups occur, with two terms each. Thus three coordinate pairs are proportional with ratios xi satisfying xi^70=-1. The projective closure, having dimension two, is the corresponding classical paired plane P^2.

For a paired plane, simultaneous scaling of the two coordinates of each pair preserves the plane. A nonzero alpha projection would require alpha_i+alpha_j=0 mod 70 for each pair. Our alpha has no complementary pair at all; all 15 pair sums have been checked. Hence every binomial component has zero alpha projection.

If a single non-binomial component C remains, write the fundamental cycle as n[C] plus the binomial and boundary components, with n positive. Project the total-cycle identity onto alpha. Every term except n e_alpha[C] vanishes, so e_alpha[C]=0 in characteristic zero. If there is no non-binomial component, the result is immediate. The same reasoning applies to every unit conjugate of alpha. QED.

## 3. A stabilizer must stabilize the individual component

The failure of a proposed class to be invariant under a symmetry rules out that class only if the symmetry fixes the individual cycle. A group preserving a reducible intersection can permute its components. Thus the earlier U32 argument about a full intersection stabilizer must not, by itself, be extended to unknown irreducible components.

Let H be a finite diagonal subgroup preserving T, let C be a surface component, and let H_C be its actual stabilizer. If e_alpha[C] is nonzero, then

    H_C is contained in ker(chi_alpha restricted to H).

If q is the order of chi_alpha restricted to H, the number of components in the H-orbit of C is [H:H_C], a multiple of q. In particular, at least q such components must occur. If C is non-binomial, its entire diagonal orbit remains non-binomial.

Proof: h in H_C fixes [C], while acting on its nonzero alpha projection by chi_alpha(h); therefore chi_alpha(h)=1. The index assertion follows from H_C subset ker chi_alpha subset H. This proves the assertion without assuming that H fixes every component.

### Correct projective character convention

An element a of the character group of G is a vector modulo 70 satisfying sum a_i=0 mod 70. Such vectors are **not** identified by adding arbitrary multiples of (1,1,1,1,1,1). If T has homogeneous relation lattice L and H is the kernel of those relations in G, then the annihilator of H is the image of L modulo 70. This follows by dualizing the homomorphism G -> Hom(L,mu_70). No additional all-ones character is inserted.

The specific useful congruences in U35 use no all-ones shift, so this correction does not change them or U36. It does prevent reuse of the overbroad shifted-span criterion in U32-U34. A stabilizer test remains necessary, not sufficient.

## 4. Executed reducible examples

### 4.1 Triangular prism / Segre threefold

Use T=P^2 x P^1 in P^5 with coordinates

    (s0 t0, s1 t0, s2 t0, s0 t1, s1 t1, s2 t1).

The restricted Fermat equation factors exactly as

    (s0^70+s1^70+s2^70)(t0^70+t1^70).

Its components are 70 paired planes and one irreducible C_70 x P^1. The latter is a genuine non-binomial surface, but the theorem shows that its alpha projection vanishes. Its degree is 140, the planes contribute degree 70, and the total degree is 210=70 deg(T), with deg(T)=3. These degree checks corroborate but do not replace the refined intersection argument.

### 4.2 Two non-binomial components can still be insufficient

Consider the join of two conics, parametrized by

    (s^2, c s t, t^2, u^2, c u v, v^2), with c^70=2.

The two homogeneous torus relations have exponent rows

    (1,-2,1,0,0,0), (0,0,0,1,-2,1).

The Fermat pullback is

    (s^70+t^70)^2 + (u^70+v^70)^2
      = (s^70+t^70+i(u^70+v^70))
        (s^70+t^70-i(u^70+v^70)).

Both factors define smooth irreducible diagonal surfaces in P^3. The parametrization has generic degree two, with deck involution changing the signs of s,t together. Since 70 is even, it preserves each factor, so their images are two distinct irreducible components, not a single component split only by the parametrization.

For the standard labelling the order q of the target character on the diagonal stabilizer is 70. More generally, test all 90 unordered partitions of the coordinates into two triples with a distinguished middle coordinate in each triple. The orders are 70 for 78 choices and 35 for 12 choices; none is 1 or 2. Hence an H-orbit carrying a nonzero target projection cannot fit into these two components. This entire conic-join construction fails for alpha, even though it passes the weaker 'at least two non-binomial factors' test.

The exact check uses q=min{n>0: n alpha lies in the two-row span modulo 70}. In each triple the two endpoint coordinates must agree and the middle must be minus twice either endpoint. The formula is q=70/gcd(70, the four resulting defects). A second direct modular-span enumeration checks the standard labelling.

## 5. Evidence and handoff

    python research/computations/U37/verify_u37.py

Four focused tests check all complementary pairs, the two uniform factorization identities, and all 90 conic-join character orders. General statements in Sections 2-3 are proved above, not inferred from that finite census.

A subsequent candidate should be screened for non-binomial factor count and **component-permutation** orbits before computing periods. U38 adds a separate Galois-orbit obstruction for candidates defined over Q(zeta_70). No arbitrary surface, arbitrary matrix factorization, or complex Hodge class has been excluded.

## Sources

- U36, Sections 5-6, preserved at base commit 467188a3d6c10a08ab2476fc65c12d14c78771de. The torus-coset proof is repeated above; no stronger result is imported.
- Stacks Project, projective-space Chow formula, tag 02TV: https://stacks.math.columbia.edu/tag/02TV .
- Stacks Project, refined Cartier intersection, tags 02T7 and 02TK: https://stacks.math.columbia.edu/tag/02T7 and https://stacks.math.columbia.edu/tag/02TK .

No novelty claim; this is a proved restriction on the project's current construction strategy. Historical U01-U34 are not globally revalidated.
