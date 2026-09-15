# U39: an exact Kummer subfield of the degree-70 target's necessary field

Status: **proved by the argument below, with exact arithmetic corroboration and adversarial self-review**; not formally verified or independently expert-reviewed. This is a necessary field-of-definition theorem for one Hodge block, not a proof or counterexample to the rational Hodge conjecture.

Date: 2026-09-15. Remote base: `Joe-Simo/hodge-conjecture@467188a3d6c10a08ab2476fc65c12d14c78771de`. This continues the preserved, previously unpushed U37–U38 evidence. U36 and the earlier construction records are not altered by this argument.

## 1. Exact target and results

Fix an algebraic closure of Q inside C. Put

    K = Q(zeta_70) = Q(zeta_35),
    X = {z0^70+z1^70+z2^70+z3^70+z4^70+z5^70=0} in P^5_K,
    alpha = (1,20,24,42,61,62).

Let W_alpha denote the primitive rational orbit block with complex lines V(u alpha), for the 24 units u modulo 70. As checked in U38, it has rational dimension 24 and Hodge type (2,2). Coefficients of algebraic cycles in this note are rational.

Define the rational numbers

    D = -2^32 * 5^15 / 7^7,
    R = 2 * 5^30 * 7^14,

and the explicitly specified field

    M = K(R^(1/35)).

All choices of the indicated root give the same subfield because K contains the required roots of unity.

**Theorem.**

1. For every finite field F_q with q = 1 modulo 70, every multiplicative character chi of exact order 70, and the normalized degree-four Fermat Jacobi sum j_q(alpha) defined below,

       (j_q(alpha)/q^2)^2 = chi(D).

   The denominator of D is invertible in these fields.

2. There is a cyclic extension E/K of degree exactly 70 that trivializes the target block's normalized Galois representation. Every nonzero vector in that block has the same G_K stabilizer, namely G_E. Its unique degree-35 subfield is exactly M.

3. If L/K is a finite extension and an L-defined codimension-two algebraic cycle on X has nonzero W_alpha projection, then

       E is contained in L; in particular M is contained in L.

   This strengthens U38's degree-divisibility restriction to a field-containment restriction. It does not assert that a cycle exists over E.

4. M/Q is a nonabelian Galois extension of degree 840. Consequently **every cycle defined over a finite abelian extension of Q, and in particular over any cyclotomic number field, has zero W_alpha projection.** For a field F not containing K, the assertion is applied to FK.

The same vanishing applies to the codimension-two Chern-character component of any coherent sheaf defined over such an abelian field. In particular a graded matrix factorization over cyclotomic coefficients, when it gives a coherent sheaf on X, cannot furnish the target coefficient, whatever its rank. This is a coefficient-field obstruction, not a claim about all complex or all ungraded matrix factorizations.

## 2. Source conventions and the uniform finite-field identity

Let psi be a nontrivial additive character of F_q. For 1 <= a <= 69 write

    G(a) = sum_{t in F_q*} chi(t)^a psi(t).

Use the U38 normalization

    j_q(alpha) = (q-1)^(-1) *
       sum_{v_i in F_q*, sum v_i=0} product_i chi(v_i)^(alpha_i).

Additive-character orthogonality gives

    j_q(alpha) = product_i G(alpha_i)/q,
    j_q(alpha)/q^2 = product_i G(alpha_i)/q^3.              (2.1)

Indeed the additive Fourier term at zero vanishes because every chi^(alpha_i) is nontrivial. Every nonzero Fourier parameter gives the same product of Gauss sums, since sum alpha_i = 210 = 0 mod 70. This supplies the factor (q-1)/q before dividing by q-1.

The classical reflection and Davenport–Hasse multiplication identities, in this convention, are

    G(a)G(70-a)/q = chi(-1)^a,                            (2.2)

and, for n in {2,5,7}, 1 <= a < 70/n,

    product_{j=0}^{n-1} G(a+j*70/n)
    ------------------------------------------------ = chi(n)^(-na).
    G(na) product_{j=1}^{n-1} G(j*70/n)                   (2.3)

All arguments in (2.2)–(2.3) used here are nonzero modulo 70, so every Gauss sum divided by is nonzero. The characteristic is different from 2,5,7 because 70 divides q-1.

Reference [1], Proposition 2.2(iii) and Theorem 3.10, supplies these identities. **Sign translation:** Otsubo defines g(phi) = -G(phi), with g(epsilon)=1. Substituting this into his multiplication identity gives exactly (2.3), including the inverse exponent -na; no unspecified sign is dropped.

### 2.1 A finite integer certificate, not an extrapolation

Let e_a denote the formal exponent of G(a), and let e_q denote the exponent of q. Define relation vectors

    Refl(a) = e_a + e_(70-a) - e_q,
    DH(n,a) = sum_{j=0}^{n-1} e_(a+j*70/n)
               - e_(na) - sum_{j=1}^{n-1} e_(j*70/n).

Take the following integer powers of reflection identities:

    (a, power) =
    (8,2), (9,1), (10,1), (11,1), (12,1), (13,-2),
    (18,-1), (20,4), (21,-1), (22,-2), (24,2), (26,2),
    (28,1), (29,-2), (30,-1), (32,-1), (34,1).

Take the following integer powers of multiplication identities:

    (n, a, power) =
    (2,1,-1), (2,3,1), (2,5,2), (2,6,1), (2,7,1),
    (2,8,-2), (2,9,-1), (2,10,1), (2,11,-2), (2,13,2),
    (2,14,1), (2,15,-3), (2,16,-1), (2,17,1),
    (5,1,2), (5,2,-1), (5,3,-1), (7,1,1).

Adding these 35 exponent vectors gives exactly

    2(e_1+e_20+e_24+e_42+e_61+e_62) - 6e_q.             (2.4)

The accumulated exponents on the right of (2.2)–(2.3), in the order chi(-1), chi(2), chi(5), chi(7), are

    (71, 32, 15, -7).                                   (2.5)

Equations (2.4)–(2.5) are integer vector identities: the supplied checker verifies all 70 coordinates, and Wolfram separately verifies the same certificate. Combining them with (2.1) proves

    (j_q(alpha)/q^2)^2
       = chi(-1)^71 chi(2)^32 chi(5)^15 chi(7)^(-7)
       = chi(-2^32*5^15/7^7).                           (2.6)

This proves the identity for **every** q and chi satisfying the stated hypotheses. The eight prime-field examples below are implementation checks, not the reason the theorem is uniform. Negative certificate powers are legitimate because nontrivial Gauss sums never vanish.

## 3. From Frobenius values to a global character

Choose a prime ell different from 2,5,7,491 and a coefficient field containing K. The diagonal group mu_70^6/mu_70 is defined over K. Its character projectors therefore commute with G_K, and each primitive V(a) is one-dimensional after extension of coefficients.

We use the usual geometric Frobenius convention in which the Frobenius eigenvalue on V(a) is j_q(a); the twist (2) divides it by q^2. Equivalently, let rho_a be the character on the **dual** of this twisted line and evaluate it on arithmetic Frobenius. Then its value is j_q(a)/q^2. Passing to the dual changes no kernel or fixed-field conclusion.

The character indexing can be fixed equivariantly, rather than inferred from the unordered eigenvalue list: insert a diagonal automorphism h into the Frobenius point-count formula. Character expansion for the corresponding diagonal equation gives the term a(h) j_q(a). Orthogonality over the diagonal group identifies the coefficient on V(a). Thus one global choice of a (or its negative for inverse-pullback indexing) works at all primes; no prime-by-prime relabeling is allowed. Shioda–Katsura [2, (3.1)–(3.4)] records the normalization; it is also pinned by U38's independent cubic F_7 point count. An exact equivariant source is [5, Theorem 1.2 and Remark 6.6]: take d=70, n=5, c=-1 and the five characters with exponents (20,24,42,61,62). Their product has exponent 69, so all its nontriviality hypotheses hold, and the twisted Jacobi sum there is exactly the sum on 1+v1+...+v5=0 used here. The source's covariant-motive convention can dualize the line, but does not change its kernel.

For a prime pfrak of K not over 2,5,7,ell, its residue field has q=1 mod70. Define the canonical power-residue character by requiring that its value reduce to t^((q-1)/70). Since X is smooth proper at these primes, its representation is unramified there. Formula (2.6) applies to all these residue fields, not just the degree-one primes in the numerical table.

Let theta^70=D and define the Kummer character

    kappa_D(sigma) = sigma(theta)/theta.

At arithmetic Frobenius its value is the canonical chi(D). Consequently (2.6) and Chebotarev density imply

    rho_alpha^2 = kappa_D.                              (3.1)

With the opposite Frobenius/index convention both characters may be inverted; the fixed fields below are unchanged. Here the convention has been fixed so that (3.1) holds as written.

For clarity, no finite-image assumption about rho_alpha is needed to use density: the quotient rho_alpha^2/kappa_D is a continuous one-dimensional ell-adic character. Its value is 1 on the dense set of unramified Frobenius conjugacy classes. Continuity, or reduction modulo successive powers of the coefficient prime, makes it 1 everywhere. Chebotarev is used in its standard number-field form [3, Theorem 8.31].

## 4. An explicit square in K and the exact image order

An explicit square root of -35 in K is tau=T(zeta_70), where

    T(x) = 4x^22 + 2x^21 + 2x^20 - 4x^16 - 4x^15 - 2x^14
           + 4x^11 + 2x^10 + 4x^9 + 4x^8 - 2x^5 - 4x^4 + 1.

Direct polynomial division gives

    T(x)^2+35 = 0 modulo Phi_70(x).

One way to obtain T is to reduce sum_{a=0}^{34} JacobiSymbol(a,35) x^(2a), but the proof only needs the displayed, exactly checked polynomial square. Put

    C = (2^16*5^7/7^4) tau.

Then C^2=D. Every theta with theta^70=D has theta^35=C or -C in K. Hence kappa_D takes values in mu_35. By (3.1),

    rho_alpha^70 = 1.

U38 independently verifies j_491(alpha)/491^2=zeta_70^57, a primitive 70th root. Therefore rho_alpha has image exactly mu_70. Its kernel fixes a cyclic extension E/K of degree 70.

For each unit u modulo70, replacing chi by chi^u in the finite-field sums Galois-conjugates j_q(alpha). Since rho_alpha now has values in mu_70, this implies at every good Frobenius and then by density that

    rho_(u alpha) = rho_alpha^u.

All u are invertible mod70, so all 24 line characters have the same kernel. For every sigma outside that kernel, none of its 24 eigenvalues on W_alpha(2) is 1. Therefore **every nonzero vector** in the block has stabilizer exactly G_E, not merely some possibly larger subgroup.

This also makes E independent of ell and of the dual/index choices: it is the same kernel of a finite character specified by the compatible Frobenius data. It is the minimal field trivializing this cohomological representation; it is not asserted to be a sufficient field for algebraic cycles.

## 5. Identification of the degree-35 subfield

By (3.1), the subfield fixed by ker(rho_alpha^2) is

    K(D^(1/70)).

It is the unique degree-35 subfield of E because rho_alpha has order70.

Since D=C^2 and35 is odd, this field is also K(D^(1/35)). For an explicit verification, if delta^35=D, then theta=delta^18/C satisfies theta^2=delta and theta^70=D; conversely delta=theta^2. Thus the two fields are identical, independently of compatible root choices.

Next, the following rational identity holds exactly:

    D^23 = (2*5^30*7^14) * (-2^21*5^9/7^5)^35.           (5.1)

Because gcd(23,35)=1, changing a Kummer radicand by its 23rd power and a 35th power does not change the field. Therefore

    K(D^(1/70)) = K(D^(1/35)) = K(R^(1/35)) = M.         (5.2)

This is an explicit subfield determination, not a conjectural recognition of finitely many Frobenius values. The elementary Kummer correspondence used here is described in [4, Propositions 5.27–5.28 and Theorem 5.30].

### 5.1 Degree, ramification, and noncommuting automorphisms

K=Q(zeta_35) is unramified at2; for example its cyclotomic discriminant is exactly 5^18*7^20. At every prime above2, v(R)=1. Thus x^35-R is Eisenstein there and is irreducible over K, with total ramification index35. It follows independently that

    [M:K]=35,  [M:Q]=35*24=840.

For the cited local facts see [3, Theorem 6.4 and Proposition 7.55]; the actual discriminant and valuation inputs are checked exactly.

M is the splitting field over Q of x^35-R: it contains a root b and all 35th roots of unity, and conversely the splitting field contains their ratios and hence K. Choose b to be its positive real root. Let tau_0 in Gal(M/K) send b to zeta_35 b, and let c be complex conjugation on M. Then c(b)=b and c(zeta_35)=zeta_35^(-1), so

    c tau_0 c^(-1) = tau_0^(-1) != tau_0.

The inequality follows because tau_0 has order35. Hence M/Q is Galois but nonabelian. No assertion about the full abstract group of E/Q is needed.

## 6. Algebraic cycles and the abelian-coefficient obstruction

Suppose Z is a rational codimension-two cycle defined over a finite L/K and has nonzero W_alpha projection. Its class in H^4_et(X_barK,Q_ell(2)) is fixed by G_L. The rational orbit projector commutes with G_K; Betti/etale comparison respects it. Hence the projected class remains nonzero and is fixed by G_L. Section 4 says that its stabilizer is exactly G_E. Therefore

    G_L is contained in G_E,  hence E is contained in L.

This invokes only the existence and functoriality of cycle classes, not the converse assertion of either the Tate or Hodge conjecture.

Now let F/Q be a finite abelian extension, without assuming K is contained in F. The compositum FK/Q is still abelian. If an F-defined cycle contributed nontrivially, the preceding result applied over FK would force M subset FK. Every subextension of an abelian Galois extension is abelian and Galois over Q, contradicting Section 5. Thus its contribution is zero.

In particular, adjoining more roots of unity can never remove this obstruction. A coherent sheaf over F has codimension-two Chern character in CH^2(X_F)_Q, so the same argument applies to it. For a graded matrix factorization over F that gives such a sheaf, this proves the claimed coefficient-field obstruction without depending on the particular explicit Chern-character formula in the earlier route.

**Scope:** components of a scheme defined over F need not themselves be F-defined. The argument applies to an individually F-defined cycle, not separately to every geometric component of an F-defined union. Components may become defined over nonabelian fields. It is also not a prohibition on arbitrary complex coefficients.

## 7. Executed follow-up: the most direct degree-70 radical field is wrong

The square identity naturally suggests L0=K(C^(1/70)). This extension is cyclic of degree70, but it is **not** E.

First, its degree is indeed70. The Kummer class of C has order divisible35 because v_2(C)=16. At a prime above7, the ramification index in K/Q is6, so v_7(tau)=3 and v_7(C)=-24+3=-21. This forces its Kummer order to be divisible10. These two conditions force order70, while the order already divides70.

Let kappa_C be its Kummer character. Since C^2=D, (rho_alpha/kappa_C)^2=1. We computed the residual quadratic character rather than assuming it trivial. At primes chosen by zeta_70 reducing to g^((p-1)/70), exact results are:

| p | g | exponent of rho_alpha | exponent of chi(D) | exponent of chi(C) | exponent of rho_alpha/chi(C) |
|---:|---:|---:|---:|---:|---:|
| 71 | 7 | 40 | 10 | 40 | 0 |
| 211 | 2 | 12 | 24 | 12 | 0 |
| 281 | 3 | 32 | 64 | 32 | 0 |
| 421 | 2 | 50 | 30 | 15 | 35 |
| 491 | 2 | 57 | 44 | 57 | 0 |
| 631 | 3 | 64 | 58 | 29 | 35 |
| 701 | 2 | 34 | 68 | 34 | 0 |
| 911 | 17 | 0 | 0 | 35 | 35 |

All exponents are modulo70. The first five rows were reproduced in Wolfram; the last three are new holdout checks in exact Python/SymPy arithmetic. Every row satisfies the proved squared identity.

To distinguish **fields**, merely finding a nontrivial quotient character is not enough. Two faithful cyclic-order70 characters with the same kernel differ by a fixed unit power u modulo70. At211 equality of kernels would require 12u=12 mod70, so u=1 mod35; the only unit possibility modulo70 is u=1. At421 this would require 15=50 mod70, which fails. Hence the kernels, and therefore L0 and E, are different.

This avoids replacing the unresolved quadratic factor by an attractive but false radical guess. Writing eta=rho_alpha/kappa_C, the exact result is eta^2=1 and eta is nontrivial. Its global Kummer squareclass has not been identified in this note. In particular even this specific extension of degree70 does not suffice for any nonzero target cycle, because it does not contain E.

## 8. Audit and research consequence

The dependency chain is:

    Gauss reflection + Davenport–Hasse + integer certificate
        -> uniform squared Jacobi identity
        -> Kummer character identity by Chebotarev
        -> image rho_alpha = mu_70 using U38 at491
        -> common kernel of all target conjugates
        -> E subset every relevant cycle field
        -> explicit nonabelian M subset E
        -> zero target projection over every finite abelian field of Q.

The audit explicitly distinguishes the following:

- The algebraic certificate is an identity of 70 integer coordinates; it is not a finite-prime fit.
- Prime-field tests do not verify all finite fields. The classical identities provide that quantifier.
- Frobenius dual/index conventions invert characters but do not alter the field claims; local comparisons use one fixed convention.
- A Galois-invariant cohomology class is not assumed to be algebraic.
- Neither a compatible field degree nor trivialized representation is asserted sufficient to construct a cycle.
- A sheaf's coefficient field is distinguished from an arbitrary field containing some individual numerical period.
- The full Hodge conjecture and the target block's algebraicity over C remain unresolved.

**Outcome:** the limited theorem stated here is proved using classical inputs and the displayed certificate; the review is by the same assistant, not a fresh expert. The independent Wolfram run corroborates arithmetic only.

**Next discriminating task:** determine the nontrivial quadratic character eta (or an equivalent explicit degree70 Kummer radicand for E), then seek a genuinely nonambient cycle over a field containing E. Do not resume arbitrary-rank constructions whose coefficients remain in cyclotomic fields: Section 6 excludes them uniformly. The previously eliminated U35 family also remains excluded independently by U36.

## 9. Sources and reproducibility

[1] Noriyuki Otsubo, *Hypergeometric functions over finite fields*, arXiv:2108.06754v5, 1 August 2023. Definition 2.1, Proposition 2.2(iii), Theorem 3.10; the source also gives a proof of the multiplication identity in Appendix A. https://arxiv.org/pdf/2108.06754v5

[2] Tetsuji Shioda and Toshiyuki Katsura, *On Fermat varieties*, Tohoku Mathematical Journal 31 (1979), 97–115, DOI 10.2748/tmj/1178229881, Section 3, formulas (3.1)–(3.4), printed page107. https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf

[3] J. S. Milne, *Algebraic Number Theory*, version3.08, 19 July 2020: Theorem6.4, Proposition7.55 and Theorem8.31. https://www.jmilne.org/math/CourseNotes/ANT.pdf

[4] J. S. Milne, *Fields and Galois Theory*, author-hosted version inspected 15 September2026, Propositions5.27–5.28 and Theorem5.30, printed pages74–76. https://www.jmilne.org/math/CourseNotes/FT.pdf

[5] Noriyuki Otsubo and Takao Yamazaki, *Motivic Gauss and Jacobi sums*, arXiv:2402.06072v3 (2 March 2025), Theorem1.2, Remark6.6 and Section7.2; published in Annales de la Faculte des sciences de Toulouse, serie6, 35 (2026), 95–135, DOI10.5802/afst.1842. The pinned preprint formulas are the ones checked here. https://arxiv.org/pdf/2402.06072v3

The source formulas and their translation were read directly; discovery snippets and old unsupported project claims are not substitute assumptions. No global novelty claim is made for the individual classical identities or for the specialized corollary derived here.

Run:

    python research/computations/U39/verify_u39.py

The checker imports the preserved U38 exact arithmetic implementation without invoking its output writer. It verifies the formal certificate, square-root and radical identities, all24 conjugates at491, the independent additive convolution at491, the sign benchmark, eight prime fields, and rejection of every unit-power identification of E with L0. See the source record, self-review, input hashes, independent Wolfram input/output, native validation log and run certificate alongside the code.
