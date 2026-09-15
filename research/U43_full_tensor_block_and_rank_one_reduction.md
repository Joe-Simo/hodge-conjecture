# U43: the full 576-dimensional tensor block and a rational rank-one reduction

**Status:** restricted positive results proved below using the pinned U42 argument, directly rechecked characteristic-zero Chow-motive inputs, and an exact integer certificate; adversarially self-reviewed, not formally verified or independently expert-reviewed. Neither a target-bearing surface on the original fourfold nor a complete Hodge solution has been constructed.

Date: 2026-09-15. Pinned remote base: `Joe-Simo/hodge-conjecture@517a6403f0802198b1bcf4c84458cbe22e199827`. The supplied Hodge prompt was inspected through its current-conversation source. Work is confined to the existing Hodge workspace and dedicated private repository. The historical notes outside the dependencies below are not globally revalidated.

## 1. Exact objects and theorem

Work over C, with rational equivalence for Chow groups. Put

    X = {z0^70+z1^70+z2^70+z3^70+z4^70+z5^70=0} in P^5,
    alpha = (1,20,24,42,61,62),
    K = Q(zeta_70),  U = (Z/70)^*.

X is smooth (its six partial derivatives cannot vanish at a projective point), projective, and of complex dimension four. Let M_a be its primitive character Chow motive with coefficient field K, and let V(a) be its one-dimensional Betti realization at a fixed embedding K into C. Let L be the Lefschetz motive, of degree two and type (1,1).

The diagonal automorphism group is G=mu_70^6/mu_70. Write e_a for its character idempotents, interpreted as graph correspondences. The projector

    P = sum_(u in U) e_(u alpha)

has rational coefficients by coefficient-Galois invariance. Let Wcal=(X,P) in Chow(C,Q), with rational Betti realization W. Its scalar extension is the direct sum of the 24 motives M_(u alpha). Each target character has positive-residue sum 210 at every unit, so W has dimension 24 and type (2,2).

**Theorem.**

1. For every u,v in U there are Chow-motive isomorphisms over C with coefficients K,

       M_(u alpha) ~= M_(v alpha),
       M_(u alpha) tensor M_(v alpha) ~= L^4.

2. The full rational subspace

       W tensor_Q W  subset H^8(X x X,Q)

   is spanned by algebraic codimension-four cycle classes. Its dimension is **576**, not merely U42's simultaneous-square dimension 24. This is not a claim about all of H^8(X x X).

3. Betti realization induces an isomorphism of Q-algebras

       End_Chow(C,Q)(Wcal)  -> End_Q(W) ~= Mat_24(Q).

   In particular there is a rational-coefficient Chow motive N with

       Wcal ~= N^(direct sum 24),   N tensor N ~= L^4,
       dim_Q H_B(N)=1,              H_B(N) of type (2,2).

   Thus T=N tensor L^(-2) satisfies T tensor T ~= 1 and has realization Q(0).

The theorem does **not** show T ~= 1 or that W consists of algebraic classes on X. It replaces that remaining question by the existence of a morphism L^2 -> N with nonzero Betti realization. The algebraic projector defining N is not itself a codimension-two cycle representing its image.

## 2. The established geometric bridge, and what is rechecked

U42 Sections 2-4 construct an abelian group containing injectively the Picard group of actual invertible Chow motives. In its notation e_a is a formal symbol, unrelated to the Chow projector with the same traditional letter above; hereafter all e_a in Sections 2-4 are **formal symbols**. The free group has basis e_1,...,e_69,ell. Set

    R(a) = e_a + e_(70-a) - ell,
    D(n,a) = sum_(j=0)^(n-1) e_(a+70j/n)
             - e_(na) - sum_(j=1)^(n-1) e_(70j/n),
    t_u = sum_(i=0)^5 e_(<u alpha_i>_70) - 3ell.

Residues in D are reduced modulo70 and must be nonzero. The bridge maps ell to [L], every used R and D to zero, and t_u to [M_(u alpha)]-2[L]. It therefore turns an **integral** combination of these relations into an isomorphism of invertible Chow motives, not merely an equality of Gauss sums.

The exact external inputs are [OY], Proposition4.8 (reflection), Proposition4.11(ii) (Jacobi factorization) and its invertibility assertion, and Theorem7.2 together with Proposition4.7 (multiplication after adjoining roots of n). Their scope includes characteristic zero. We inspected the statements and their proofs directly in the pinned source, and rechecked U42's cocycle construction, including its zero-argument cases.

A short independent check on that construction is useful: if J(a,b) is the actual binary Jacobi motive class, with J(a,0)=0 and J(a,-a)=ell, its symmetric cocycle identity makes P_Pic x Z/70 an abelian group via

    (p,a)+(q,b)=(p+q+J(a,b),a+b).

P_Pic embeds as the first factor at zero. The identity e_a+e_b-e_(a+b)=J(a,b) is exact there. Expanding each e_(a+j*70/n) shows D(n,a) equals the difference between the repeated-argument Jacobi motive and the binary product in [OY, Theorem7.2]. All partial multiples in every new application and every unit transport are nonzero, so repeated Jacobi factorization is legitimate.

The elementary coordinate scalings and multiplication isomorphisms can all be made over U42's field F=Q(zeta_140,2^(1/70),5^(1/70),7^(1/70)), and then base-changed to C. The field of definition F is not the correspondence coefficient field K. No finite-character arithmetic result from U38-U40 is an assumption here.

## 3. New 31-term integral certificate

The new identity is

    t_3 - t_1 = sum_(a,c in R_new) c R(a)
                + sum_(n,a,c in D_new) c D(n,a).          (3.1)

The complete nonzero coefficient lists are:

    R_new (a,c):
    (8,-2), (10,1), (11,-1), (12,-1), (13,1),
    (14,2), (20,-2), (21,1), (22,1), (24,-1),
    (26,-1), (29,1), (30,1), (34,-1), (35,1).

    D_new (n,a,c):
    (2,1,1), (2,5,-1), (2,7,-1), (2,8,2),
    (2,10,-1), (2,11,2), (2,13,-1), (2,14,-1),
    (2,15,2), (2,16,1), (2,17,-1),
    (5,1,-1), (5,2,1), (5,3,1), (7,1,-1), (7,2,1).

Their reflection coefficients sum to zero. Direct integer addition in all70 coordinates proves (3.1); both the standalone Python checker and a separate Wolfram evaluation return zero residual. Here 3alpha modulo70 is (3,60,2,56,43,46). No rational division of a relation, numerical fit, or tensor square-root cancellation is used.

For provenance, a SymPy Smith-decomposition calculation discovered this certificate in a 70-by-91 integer matrix of safe generators. That discovery is not part of the proof: the checker only adds the displayed integer vectors. In particular no claim of completeness of those91 geometric relations is needed.

Evaluation of (3.1) through Section2 gives the actual isomorphism

    M_(3 alpha) ~= M_alpha.                              (3.2)

## 4. Why this connects all 24 lines

The powers of3 modulo70 are

    1,3,9,27,11,33,29,17,51,13,39,47,

followed by1. Their12 negatives are disjoint and, together, are exactly U. Thus U is generated by3 and-1.

Applying an automorphism of the **coefficient field** K to a Chow correspondence changes every projector label a to ua. It does not assert any unproved automorphism of the variety. Consequently (3.2) yields

    M_(3u alpha) ~= M_(u alpha)

for every unit u. The needed isomorphisms along all powers of3 follow by composition.

U42 proves M_alpha^2 ~= L^4. Also [OY, Proposition4.11, (4.8)] gives M_alpha tensor M_(-alpha) ~= L^4. Cancelling M_alpha, which is tensor-invertible, gives M_(-alpha) ~= M_alpha. This is cancellation of a known invertible object, **not** cancellation of exponent2. Coefficient transport then gives the negative coset as well. This proves Theorem1's first isomorphism, and its second follows from U42.

There is an explicit all-pairs certificate, without a further search. Denote the right side of (3.1) by d and U42's displayed certificate for2t_1 by s. Set

    q_1=0,
    q_(3^(k+1))=q_(3^k)+tau_(3^k)(d),  0<=k<11,
    q_(-u)=q_u+tau_u(sum_i R(alpha_i)-s),

where u ranges over the12 powers and tau_u(e_a)=e_(ua), tau_u(ell)=ell. Then q_u=t_u-t_1. For every ordered pair (u,v),

    s+q_u+q_v=t_u+t_v.                                  (4.1)

Every term remains a valid reflection/multiplication relation; unit transport preserves nonzero partial multiples. The checker verifies all24 differences and all576 equations (4.1). The generation argument, rather than an unexplained bounded sweep, proves that this population is complete.

## 5. Rational algebraicity of the full product block

For every u,v, the isomorphism L^4 -> M_(u alpha) tensor M_(v alpha) is represented by a K-linear algebraic cycle of codimension four on X x X. Its inverse makes its Betti class nonzero. The target line for each ordered pair is independent of the other575 lines.

The rational projector is now P x P, rather than U42's sum of matched projectors. It cuts out exactly W tensor_Q W, with dimension24^2. These K-linear witnesses span its scalar extension. Expand their coefficients in a Q-basis of K and apply P x P to the resulting rational cycles; equivalently use faithful scalar extension of vector spaces. Their rational cycle classes span W tensor_Q W. This proves Theorem2.

This descent concerns **coefficients of cycles**. It does not claim that the equations of those cycles have rational coefficients or contradict U39's field-of-definition restriction.

## 6. Rational rank-one Chow summand, without a nilpotence assumption

We supply the extra argument rather than infer a rational motive decomposition just from a Betti decomposition.

Since all24 character motives are isomorphic to the invertible motive M_alpha,

    Wcal_K ~= M_alpha^(direct sum 24).

Tensoring with its inverse identifies End(M_alpha) with End(1)=K. Every nonzero endomorphism is a scalar multiple of the identity and has nonzero realization. Conjugating by the established isomorphisms gives

    End(Wcal_K) ~= Mat_24(K),

and its Betti realization is the full matrix algebra on H_B(Wcal)_K, **faithfully**. There are no undetected homologically zero endomorphisms in this particular block.

For a rational projector P, extending coefficients commutes with its corner of the Chow correspondence group:

    End(Wcal) tensor_Q K ~= End(Wcal_K).

Thus the rational Betti algebra map is injective and both sides have dimension576 overQ. It is an isomorphism. This argument uses actual coefficient extension of Chow groups, not a conjecture about fullness or conservativity of Betti realization on all motives.

Choose matrix units relative to any Q-basis of W, and lift them through this algebra isomorphism. Their multiplication equations hold in the Chow algebra itself. The24 diagonal matrix units are orthogonal rational Chow idempotents summing to P; their images are isomorphic motives N_i. With N=N_1 this gives Wcal ~= N^(direct sum 24). This is an existence construction of correspondences, not an expanded polynomial description.

After extending coefficients, N_K ~= M_alpha, since a rank-one idempotent in Mat_24(K) is conjugate to the first coordinate projector. Hence (N tensor N)_K ~= L^4_K. This last isomorphism also descends to rational coefficients, as follows. Each of

    Hom(L^4,N tensor N),   Hom(N tensor N,L^4)

becomes one-dimensional overK, so each is one-dimensional overQ. Choose nonzero rational morphisms f,g. After scalar extension they are nonzero multiples of inverse isomorphisms, so gf=c id with c a nonzero rational scalar and fg=c id as well. Faithful coefficient extension gives these equalities overQ. Thus c^(-1)g is an inverse to f, proving N tensor N ~= L^4. This proves Theorem3. No Kimura nilpotence or conjectural lifting of a cohomological inverse has been used.

## 7. Executed extraction attempts and the exact remaining gap

**Diagonal restriction does not recover a degree-four class.** Pullback by the diagonal X -> X x X preserves cohomological degree8 and lands in the top cohomology of X, not in H^4(X). Moreover a cup product V(u alpha) cup V(v alpha) can be nonzero only if u+v=0 modulo70, because top cohomology has trivial diagonal-group character and alpha's first entry is1. There are exactly24 such ordered pairs and none with u=v. Thus U42's matched squares pull back to zero; the larger block can yield top-degree pairings, not the missing surfaces.

**Contraction with ambient cycles is zero.** For a primitive degree-four class w, its pairing with h^2 is zero. Hence intersecting the product correspondence with a pulled-back ambient surface class and pushing to the other factor cannot generate the target. An algebraic degree-four seed that contracts nontrivially against W must itself have nonzero W projection, which is the missing restricted Hodge statement already.

**A rational rank-one square is not an algebraic vector.** Put T=N tensor L^(-2). We have T^2 ~=1 and H_B(T)=Q(0), but have not constructed a morphism 1 -> T with nonzero realization. In Rep_Q(Z/2), the sign representation has these same two properties after forgetting its action and nevertheless has no invariant vector. This refutes the purely tensor-categorical inference, not the Hodge conjecture or the assertion T~=1 in Chow(C,Q).

The same formal parity obstruction from U42 persists: epsilon(e_a)=1 precisely for a=14,28,42,56; epsilon(ell)=0. It vanishes on all admissible reflection/multiplication relations, while epsilon(t_u)=1 for all units u. Our new differences have parityzero. Thus extending the orbit of known identities cannot alone cancel the remaining odd generator. This only describes that presentation, not all possible geometric correspondences.

A potential shortcut would be to assert that every rational invertible Chow motive overC is a Lefschetz power. In the primary source [K], this is a special case of **Conjecture2**, not an unconditional theorem; Proposition2 derives that conjecture from Hodge/Tate-type inputs. We do not use it. The literature check here is scoped: it identifies a precisely circular proposed source implication, not a claim that no specialized later theorem can exist.

Equivalently, the remaining task is to construct a nonzero realized morphism L^2 -> N. Such a morphism would be an isomorphism: use N^2~=L^4 to dualize it, compose, and note that End(N)=Q and the nonzero one-dimensional realization makes the scalar nonzero. Conversely an isomorphism N~=L^2 supplies the missing classes. In terms of cycles, one nonzero target projection plus the established full endomorphism algebra produces all of W, but that initial cycle has not been found.

**A useful next geometric obligation:** turn the rational rank-one projector into a correspondence supported on a surface on the source side, or construct directly a surface Z with P cl(Z)!=0. A projector or product class alone does not provide that support. An alternative is additional characteristic-zero geometry annihilating the formal parity obstruction, not another enlargement of the same identity lattice.

## 8. Evidence, limitations, and sources

The standalone checker uses exact Python integers, not the Smith solver that discovered (3.1), and requires no third-party package. It checks ten focused assertions, including intentional bad-input/perturbed-certificate failures, all24 transported certificates, all576 mixed certificates, and the geometric source-admissibility conditions. Eight inherited U42 tests are rerun separately; neither suite is a proof assistant for Chow theory. See `research/computations/U43/` for inputs, outputs, source/notation review, and validation record.

[OY] N. Otsubo and T. Yamazaki, *Motivic Gauss and Jacobi sums*, pinned arXiv:2402.06072v3, Section4.2 and Theorem7.2. Primary full text: https://arxiv.org/html/2402.06072v3 . We rechecked Props4.7,4.8,4.11 and the characteristic-zero multiplication proof. The served HTML displays differing dates in its version header and body; the URL, observed labels and mathematical locators are recorded without silently reconciling metadata.

[K] B. Kahn, *Motivic zeta functions of motives*, arXiv:math/0606424, Section4, Conjecture2 and Proposition2. Primary full text: https://arxiv.org/html/math/0606424 . Used to audit a proposed shortcut, not as a positive input.

[U42] `research/U42_tensor_square_algebraicity.md` at the base revision stated above, especially Sections2-5. Its square certificate and all new exponent identities are rechecked. The new result is a specialized deduction from these correspondences and the displayed certificate; no global novelty or independent-acceptance claim is made.
