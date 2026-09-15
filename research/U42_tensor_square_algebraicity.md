# U42: algebraicity of the diagonal tensor-square block

**Status:** a restricted positive result proved below from characteristic-zero Chow-correspondence theorems and an exact integer certificate; adversarially self-reviewed, not formally verified or independently expert-reviewed. The original degree-70 block and the full rational Hodge conjecture remain unresolved. No polynomial equations for a target-bearing surface on the original fourfold are claimed.

Date: 2026-09-15. Base: `Joe-Simo/hodge-conjecture@489b743689ac96345ea56ec49f4a1568623236cc`. The full supplied Hodge research prompt was read. U40's displayed integer certificate is rechecked independently here; its arithmetic splitting-field theorem and U41's obstruction are not assumptions in this proof.

## 1. Result and its exact scope

Put

    X = {z0^70+z1^70+z2^70+z3^70+z4^70+z5^70=0} in P^5_C,
    alpha = (1,20,24,42,61,62),  K = Q(zeta_70).

Write V(a) for a primitive complex Fermat character line and M_a for the corresponding Chow motive with coefficient field K, cut out by the diagonal-character projector. Let L be the Lefschetz motive, whose realization has cohomological degree 2 and Hodge type (1,1); this avoids opposite conventions for Tate-twist notation.

**Theorem.** There is an isomorphism in the category of Chow motives over C with coefficients K,

    M_alpha tensor M_alpha  ~=  L^4.                         (1)

Consequently the rational subspace whose complexification is

    W_square,C = direct sum over u in (Z/70)^*
                 V(u alpha) tensor V(u alpha)
                 inside H^8(X x X,C)                         (2)

is spanned by rational algebraic codimension-four cycle classes. Its rational dimension is 24. The tensor in (1)-(2) is an **external tensor on two copies of X**, not a cup-square on X, and not the automatically algebraic pairing with V(-alpha).

This is a correspondence-based existence proof of cycles for (2): it composes genuine Chow isomorphisms supplied by the primary sources. It is not an expanded list of defining equations or an implemented symbolic composition of all those correspondences. In particular it supplies no nonzero algebraic class in V(alpha) on X itself.

All base changes used below can be made in the explicit number field

    F = Q(zeta_140, 2^(1/70), 5^(1/70), 7^(1/70)).             (3)

The assertion over C does not require (3) to be a minimal field. The coefficient field K of correspondences is distinct from their field of definition F.

## 2. Characteristic-zero geometric inputs

The principal source is Otsubo--Yamazaki [OY], pinned arXiv:2402.06072v3. Although the title concerns finite-field sums, Section 4.2 and Theorem 7.2 hold over arbitrary appropriate perfect fields, including F and C. Only these geometric parts, not a lifting of Frobenius eigenvalues, are used.

In the source, F_m^(n) is the hypersurface

    x1^m+...+xn^m = x0^m in P^n,

of dimension n-1. For residues a1,...,an with each ai and their sum nonzero modulo m, let H(a1,...,an) be its primitive character motive. Source Proposition 4.11 proves its invertibility. Proposition 4.8 gives

    H(a,b) tensor H(-a,-b) ~= L,                             (4)

when a,b,a+b are nonzero. Proposition 4.11(ii) gives the associative factorization into binary Jacobi motives when the partial sums are nonzero. Coordinate permutations supply the corresponding permutations of full projective characters. The requisite minus-sign changes are algebraic coordinate scalings over F, since zeta_140 is available.

For n dividing 70 and na nonzero, Theorem 7.2 and Proposition 4.7 give, after adjoining n^(1/70),

    H(a,...,a) [n entries]
      ~= tensor product over j=1,...,n-1 of H(a,70j/n).      (5)

This is a Chow-motive isomorphism, not merely equality of periods. For every application below, n is 2, 5, or 7, so (3) supplies all required scalings. Each factor in (5) is admissible. The proof of Theorem 7.2 constructs finite covers through the variety t^70=product(s_i), sum(s_i)=n, and a product of curves x^70+y^n=1; the projector calculation has nonzero composite 1/(n-1)!. Thus the theorem supplies nonzero algebraic correspondences in characteristic zero. Its subsequent finite-field Corollary 7.3 is not being used as a characteristic-zero theorem.

## 3. Making formal Gauss symbols legitimate

Individual formal Gauss symbols will NOT be assigned to hypothetical characteristic-zero Gauss motives. Instead, the following elementary group-extension construction interprets only balanced combinations using actual Jacobi motives.

Let P be the abelian group of isomorphism classes of invertible Chow motives over F with coefficients K, written additively. Define J(a,b) in P for a,b in Z/70 by

    J(a,0)=J(0,a)=0,
    J(a,-a)=[L] when a != 0,
    J(a,b)=[H(a,b)] when a,b,a+b != 0.

These conventions include zero residues explicitly; no nonexistent primitive curve character is used when a+b=0.

**Cocycle lemma.** J is symmetric and

    J(a,b)+J(a+b,c) = J(b,c)+J(a,b+c).                      (6)

Proof. Zero inputs are immediate. If a,b,c, their two partial sums, and their total sum are nonzero, both sides are the class of H(a,b,c), by Proposition 4.11(ii). If the total sum is zero while the inputs and partial sums are nonzero, the second term on each side is L, and H(a,b) ~= H(b,c) by cyclic permutation of the three projective coordinates. If a+b=0 but b+c!=0, the left side is L and the two curve factors on the right have full projective character triples which are negatives up to permutation; (4) applies. The case b+c=0 is symmetric. If both partial sums vanish, both sides are L. These cases cover all residues. Symmetry comes from exchanging the affine coordinates. QED.

Give the set P x Z/70 the law

    (p,a)+(q,b) = (p+q+J(a,b), a+b).

Equation (6) makes it an abelian group G. Its identity is (0,0); an inverse of (p,a) is (-p-J(a,-a),-a). The map P -> G, p -> (p,0), is injective by construction. Write e_a=(0,a), with e_0=0, and ell=([L],0).

The following identities now hold in this explicitly constructed group, with no independence assertion about the e_a:

    e_a+e_-a = ell,
    e_a+e_b-e_(a+b) = (J(a,b),0).                          (7)

For a multiplication relation put

    DH(n,a) = sum_(j=0)^(n-1)e_(a+70j/n)
              -e_(na)-sum_(j=1)^(n-1)e_(70j/n).

By (7), its value in G is

    [H(a,...,a)] - sum_(j=1)^(n-1)[H(a,70j/n)] = 0,         (8)

using (5). For the nine instances used here all partial multiples a,2a,...,na are nonzero, so the first term follows by directly iterating Proposition 4.11(ii). Negative coefficients are allowed because every motive involved is tensor-invertible.

This group construction is the bridge absent from a bare gamma/Gauss identity: an equality of formal exponent vectors is evaluated in a group built from **algebraic** correspondences, with an injective copy of their Picard group.

## 4. Evaluate the exact certificate

Let theta=e_1+e_20+e_24+e_42+e_61+e_62 and N_a=e_a+e_(70-a). In the free abelian group on the 69 nonzero symbols, direct integer addition verifies

    2 theta = sum n_a N_a + sum h_(n,a) DH(n,a),             (9)

where the nonzero entries are

    (a,n_a): (1,1),(4,1),(9,1),(16,1),(22,-1),
             (24,2),(26,1),(28,-1),(30,1),

    (n,a,h): (2,1,1),(2,9,-1),(2,26,1),(2,34,-1),
             (5,4,-1),(5,6,1),(5,12,-1),(7,2,1),(7,6,-1).

The sum of the n_a is 6. Equation (9) is an exact identity with 69 coordinates, not a numerical fit. The separate Python and Wolfram checks recompute it.

The partial sums of the first five target entries are

    1,21,45,17,8  modulo 70.

They are all nonzero, while the sum of all six is zero. Thus (7) and Proposition 4.11(ii) give

    theta = [H(1,20,24,42,61)] + ell
          = [M_alpha] + ell                               (10)

inside the embedded P: the omitted projective exponent is -8=62 modulo70. The equality between the all-plus X and the source convention is an algebraic coordinate scaling and a permutation.

Evaluate (9) in G. Every N_a maps to ell and every DH(n,a) maps to zero by (8), so

    2[M_alpha]+2[L] = 6[L] in P.

Cancellation in the group of invertible motives proves (1). This does not cancel the factor 2; it cancels only tensor-invertible Lefschetz factors. The resulting isomorphism is M_alpha^2 ~= L^4, exactly as claimed.

## 5. From coefficient-K motives to rational cycle classes

An isomorphism L^4 -> M_alpha tensor M_alpha is represented by a K-linear algebraic codimension-four cycle on X x X. Its Betti realization is nonzero because an inverse correspondence composes to the identity. No conservativity conjecture or Hodge/Tate surjectivity assumption is used here.

Write e_a for the usual diagonal-character Chow projector in this paragraph only. The projector

    P_square = sum_(u in (Z/70)^*) e_(u alpha) x e_(u alpha)

has rational coefficients: it is fixed under all coefficient-field automorphisms of K. Its 24 summands are orthogonal, and each has a one-dimensional complex realization. Hence its rational image is the 24-dimensional space (2). This is only the simultaneous orbit; it is not the full 24 x 24 tensor product.

Apply each automorphism of the coefficient field to (1). Every line V(u alpha) tensor V(u alpha) then has a nonzero algebraic cycle class with coefficients in K. Since the rational cycle-class image is a Q-linear subspace and extension of scalars to K is faithfully flat, spanning these lines over K proves spanning of the rational image of P_square over Q. Equivalently, expand the finitely many K-linear witness cycles in a Q-basis of K and apply P_square to their rational-coefficient components.

The residue-sum criterion, checked at all 24 units, gives type (2,2) for each original line and hence (4,4) for each line in (2). All varieties are smooth projective over C, the product has complex dimension 8, and codimension-four cycles have exactly the claimed cohomological degree 8.

## 6. Why this still does not solve the unsquared target

Set T=M_alpha tensor L^(-2). The proved statement is T^2 ~= 1. It does not construct a morphism 1 -> T. In a general rigid symmetric tensor category, the sign representation of the group of order two satisfies S^2=1 but Hom(1,S)=0. This is a counterexample to the **formal implication**, not an example of a nonalgebraic Hodge class and not an assertion that T is nontrivial.

There is an exact obstruction within the particular reflection/multiplication presentation used above. In the free group on e_1,...,e_69 and ell define

    epsilon(v) = v_14+v_28+v_42+v_56 modulo2,
    epsilon(ell)=0.

It kills every N_a-ell and every admissible DH(n,a), for all n dividing70 with n>1 and na!=0. Here admissible means no argument in the relation is zero. A direct proof is as follows. The selected residues are precisely the nonzero elements of the order-five subgroup H of Z/70. If 5 does not divide n, the n-term coset in the numerator meets H once exactly when na is in H, and the nonzero denominator subgroup has no H-elements. If 5 divides n, an admissible numerator coset is disjoint from H, na is not in H, and the denominator subgroup contains four H-elements. In either case the parity is zero. Reflection contributes zero or two selected entries.

But epsilon(theta-3ell)=1 because 42 is the only selected target entry. Therefore theta-3ell is NOT an integral combination of these defining relations, while (9) proves that twice it is. Its class has order exactly two in this **formal presentation quotient**. This does not imply order exactly two in the actual motivic Picard group: extra geometric relations can kill it. It identifies precisely what the present certificate does and does not supply.

Thus the next construction must supply additional geometry that trivializes T itself, not just another squared-period identity. Arithmetic normalization in U40 and tensor-square algebraicity here do not by themselves do this. U41 concerns factorizations of f on X; a codimension-four correspondence on X x X is a different object, so (1) does not contradict that obstruction.

## 7. Executed alternative and retained lead

Before the multiplication theorem was verified, the surface-product route was also computed exactly. Among the ten partitions of alpha into two triples, adjoining opposite balancing entries yields three pairs of rank-24 surface Hodge structures with Hodge numbers (1,22,1). For one pair,

    beta=(1,42,61,36) at level70,
    gamma=(25,23,4,18) at level35,

the Hodge profiles of beta and 2gamma agree under the natural unit-group identification. This supplies an abstract Hodge-isomorphism target, not an algebraic correspondence. No theorem turning these particular rank-24 Hodge-profile matches into algebraic correspondences has been verified here. The calculation is retained in verification.json as a secondary lead, not an input to (1); an unverified appeal to a K3-isometry theorem is not used.

## 8. Sources, verification, and next checkpoint

[OY] N. Otsubo and T. Yamazaki, *Motivic Gauss and Jacobi sums*, arXiv:2402.06072v3 (2 March 2025), Section4.2, Propositions4.7,4.8,4.11, and Theorem7.2 with its proof. Primary full text: https://arxiv.org/html/2402.06072v3 . Publication: Annales de la Faculte des sciences de Toulouse 35 (2026), 95-135, DOI10.5802/afst.1842. The pinned preprint's numbering is used.

[SK] T. Shioda and T. Katsura, *On Fermat varieties*, Tohoku Math. J.31 (1979), 97-115, Lemma1.1, Theorem1.7 and Remark1.8. DOI10.2748/tmj/1178229881. Primary PDF: https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf . The explicit rational map and characteristic-zero scope were inspected, including rendered pp.97-98. [OY] gives the exact character-motive statements needed here.

The source formulas, all zero/partial-sum cases of the cocycle, coefficient-field descent, Tate degrees, invertible cancellation, and distinction between a square and its square root were adversarially reviewed by the same assistant. The source theorem is external mathematical input; the code is not a proof assistant and cannot verify it. The result is a specialized corollary of the cited correspondence identities and this certificate; no global novelty or expert-acceptance claim is made.

Run `python research/computations/U42/verify_u42.py`. The checker uses exact integer arithmetic, tests the complete formal certificate and its perturbations, and checks the parity obstruction at every admissible multiplication relation at level70. The proof in Sections2-5 is what converts this finite certificate into algebraic-cycle existence. Reproducibility, source translation, and actual validation outcomes are recorded alongside the checker.

**Next unresolved obligation:** find an algebraic trivialization of M_alpha tensor L^(-2), for example a nonzero correspondence from L^2 into M_alpha, over a field permitted by U40. The present proof constructs the tensor square only. No claimed resolution of the original rational Hodge conjecture is being withheld or implied.
