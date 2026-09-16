# U55: p-adic formal lifting of the degree-70 target and the exact algebraization gap

**Status:** a restricted positive formal-lifting result, conditional only on the previously preserved Shioda–Katsura supersingular identification of the special-fiber target block; the final algebraization step is not known and no characteristic-zero target cycle is constructed. This does not solve the Hodge conjecture.

Date: 2026-09-16.

## 1. Smooth unramified model

Let p=139 and let k be a perfect algebraic extension of F_p large enough to contain the fields of definition of the required special-fiber cycles. Put W=W(k). Since p does not divide 70, the degree-70 Fermat surface

    F/W : x0^70+x1^70+x2^70+x3^70=0 in P^3_W

is smooth and projective, and so is

    Y = F x_W F,

of relative dimension 4.

The congruence

    139 == -1 mod 70

is exactly the Shioda–Katsura supersingularity condition. Their Theorem II states that for an even-dimensional Fermat variety, if p^nu == -1 mod m for some nu, its l-adic cohomology is spanned by algebraic cycles. For the Fermat surface, Theorem 2.6 gives the Tate-cycle statement, and their supersingular definition identifies the full middle H^2 as algebraic after a sufficiently large finite field extension.

The U46 product correspondence identifies our original degree-70 fourfold target block with the beta tensor gamma block in H^2(F) tensor H^2(F), where

    beta=(1,42,62,35),
    gamma=(20,24,61,35).

Thus on the special fiber Y_1 there is a rational codimension-two cycle z_1 whose crystalline class is the specialization lambda_1 of the characteristic-zero target class lambda.

This use of crystalline cohomology is justified because the special-fiber H^2 is spanned by divisor classes; their crystalline first Chern classes span H^2_cris rationally, and products span the relevant H^2 x H^2 Kunneth summand of H^4_cris(Y_1/W).

## 2. Isolating pure Adams weight 2

Choose xi_1 in K_0(Y_1)_Q with codimension-two Chern character equal to z_1; for example start from structure sheaves of a rational cycle representative and use Q-linearity.

Let psi^2 be the second Adams operation. On the degree-2r Chern-character piece it acts by 2^r. Because dim(Y_1)=4, the polynomial

    e_2(T)=((T-1)(T-2)(T-8)(T-16))/((4-1)(4-2)(4-8)(4-16))
          =(T^4-27T^3+202T^2-432T+256)/288

is the projector onto Adams weight 2 among weights 0,1,2,3,4.

Replace xi_1 by

    xi_1^(2)=e_2(psi^2) xi_1.

Then exactly

    ch_r(xi_1^(2))=0 for r != 2,
    ch_2(xi_1^(2))=lambda_1.

This removes the higher-Chern-component problem that would occur for a naive product such as (L-1) box-times (M-1).

## 3. Bloch–Esnault–Kerz applies

Bloch–Esnault–Kerz, *p-adic deformation of algebraic cycle classes*, arXiv:1203.2776v2, Theorem 1.3, applies to a smooth projective X/W of relative dimension d provided p>d+6. Here

    d=4,
    p=139>10.

Their theorem says that the crystalline-Hodge filtration condition on the Chern character of a class in K_0(X_1)_Q is equivalent to the existence of a rational compatible pro-class

    hat xi in (lim_n K_0(X_n))_Q

lifting it through every p^n-thickening.

For xi_1^(2), the only nonzero Chern component is lambda_1 in degree 4. Under crystalline-de Rham comparison it is the specialization of our characteristic-zero (2,2) Hodge class lambda, hence lies in F^2. Therefore Theorem 1.3 gives

    hat xi in (lim_n K_0(Y_n))_Q

with special fiber xi_1^(2).

So the target block has a **formal p-adic K-theory lift to all infinitesimal orders**.

## 4. Why this still does not solve the target

The same Bloch–Esnault–Kerz paper explicitly separates formal deformation from algebraization. In its introduction it states that, unlike Picard groups, there is no general approach to the algebraization problem for higher K_0/cycle classes. Their Theorem 1.3 produces an inverse-limit K_0 class, not an element of K_0(Y)_Q.

The required final arrow is therefore

    K_0(Y)_Q  --->  (lim_n K_0(Y_n))_Q.

Surjectivity is not a formal consequence of Grothendieck existence. Formal GAGA algebraizes a **compatible object** (for example a compatible coherent sheaf or perfect complex), whereas an arbitrary element of the inverse limit of Grothendieck groups need not be represented by a compatible system of objects.

Bloch–Esnault–Kerz's characteristic-zero companion, arXiv:1310.1773, makes this distinction explicit. It notes that the analogous K_0 algebraization map is not surjective in general and gives a counterexample even for a trivial deformation of an abelian surface. Thus claiming algebraization here without an additional geometric argument would be invalid.

Consequently the current chain is

    supersingular algebraic special-fiber target
      -> pure Adams-weight-2 K_0 class
      -> Hodge-filtration condition
      -> formal K_0 lift to every p^n-thickening
      -/-> algebraic K_0 class on the W-scheme (open step).

## 5. Research consequence

This sharply improves the characteristic-139 route: **formal deformation is no longer the obstruction. Algebraization is.**

A successful continuation can now take either of two forms:

1. construct a compatible perfect-complex representative of hat xi; formal GAGA would then algebraize that object and its ch_2 would solve the degree-70 target block; or
2. construct an actual lci cycle/sheaf on the special fiber representing xi_1^(2) for which a semiregularity theorem kills all object-level deformation obstructions, upgrading the K_0 pro-class to a compatible formal object.

The second route is especially concrete because the special-fiber class may be represented inside the H^2(F) tensor H^2(F) summand by products of divisor classes. One must not assume that the two divisor factors lift individually; the whole point is to deform the coupled codimension-two object.

## 6. Sources checked

- T. Shioda and T. Katsura, *On Fermat varieties*, Tohoku Math. J. 31 (1979), 97–115, Theorem II and Theorem 2.6. Primary PDF: https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf
- S. Bloch, H. Esnault, M. Kerz, *p-adic deformation of algebraic cycle classes*, arXiv:1203.2776v2, especially Theorem 1.3 and Introduction discussion of algebraization: https://arxiv.org/abs/1203.2776
- S. Bloch, H. Esnault, M. Kerz, *Deformation of algebraic cycle classes in characteristic zero*, arXiv:1310.1773, Introduction, especially the discussion around map K_0(X)->lim K_0(X_n) and the algebraization counterexample: https://arxiv.org/abs/1310.1773

The arithmetic identity for the Adams projector was independently checked in Wolfram:

    e_2(T)=(T^4-27T^3+202T^2-432T+256)/288.

No claim of formal verification or independent expert review is made.
