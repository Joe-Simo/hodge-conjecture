# U40: reconciliation of U39 and exact classification of diagonal normalizations

**Status:** restricted arithmetic results proved below using explicitly identified classical inputs and exact identities; self-reviewed, not formally verified or independently expert-reviewed. No algebraic cycle with a nonzero target component has been constructed.

Date: 2026-09-15. Pinned remote input: `Joe-Simo/hodge-conjecture@2b4835c05d27f039235fbab8898d7dcee12c9159`, especially `research/U39_exact_Kummer_subfield_and_abelian_obstruction.md` (blob `a3652ad8f9546e5957235eae98cfc49c113b3b2b`). A distinct local U39, `U39_explicit_splitting_field_and_twist.md`, was preserved in the previous conversation artifact. These are different arguments with different uses of the letters C and D, not interchangeable file revisions. This note reconciles them without rewriting either historical argument.

The full project remains the rational Hodge conjecture for all smooth projective complex varieties. The statements below concern only the primitive block of the degree-70 Fermat fourfold indexed by

    alpha = (1,20,24,42,61,62),  K = Q(zeta),  zeta = exp(2 pi i/70).

The block W has 24 rational dimensions and consists of the lines indexed by u*alpha for units u modulo 70. The least-positive-residue sum of each is 210. Let rho be the normalized Jacobi character, with arithmetic Frobenius value j_p(alpha)/(Np)^2 on the dual of the Tate-twisted cohomological line. Simultaneously dualizing the conventions changes no fixed-field conclusion.

## 1. Explicit arithmetic input and its verification

To avoid the collision of notation, write

    C0 = 2^8 * 7^7 / 5^5,
    Delta = product (1-zeta^a),  a in {1,4,9,16,22,26,28,30},
    D0 = C0^2 * Delta^35.

The local U39's claim is

    rho = kappa_D0,
    E = K(C0^(1/35), sqrt(Delta)),  [E:K]=70,            (1)

where kappa_d(sigma)=sigma(d^(1/70))/d^(1/70). This identifies a cohomological splitting field, not a sufficient field for cycles.

Here is the load-bearing verification, rather than a reliance on that file's status label. In the free abelian group with basis e_a, 1<=a<=69, set

    N_a = e_a+e_(70-a),
    H_(n,a) = sum_(j=0)^(n-1) e_(a+70j/n)
              -e_(na)-sum_(j=1)^(n-1)e_(70j/n).

Then the exact integer-vector certificate is

    2 sum_(a in alpha)e_a = sum n_a N_a + sum h_(n,a) H_(n,a),

with nonzero coefficients

    (a,n_a) = (1,1),(4,1),(9,1),(16,1),(22,-1),
              (24,2),(26,1),(28,-1),(30,1),

    (n,a,h) = (2,1,1),(2,9,-1),(2,26,1),(2,34,-1),
              (5,4,-1),(5,6,1),(5,12,-1),(7,2,1),(7,6,-1).

All 69 coordinates are checked by `computations/U40/verify_u40.py`. The two scalar sums are sum n_a=6 and sum a*n_a=84. Gamma reflection and multiplication, applied to this identity, give for

    P = product_(a in alpha) Gamma(a/70)/(2 pi i)^3

that

    P^2 = C0^(2/35) U,
    U = zeta^42 product_a(1-zeta^a)^(-n_a)
      = q0^2 Delta,
    q0 = zeta^21 / product_(a in {1,4,9,16,24,26,30})(1-zeta^a).    (2)

The multiplication exponents for 2,5,7 are respectively 16/35,-2/7,2/5. No gamma argument is an integer or outside (0,1). In particular there are no unrecorded shift factors. Reflection phases give zeta^42 and the six minus signs cancel. Thus P equals, up to a sign in K, q0*C0^(1/35)*sqrt(Delta).

**External theorem and notation check.** Kubert–Lichtenbaum [1], Theorem 1.6, identifies the normalized gamma product's Artin character for a Deligne-type formal sum. Here their base field k is K, their level is 70, and their theta is sum[a] over alpha. For each unit u, the sum of negative fractional parts is 3, so n(theta)=3. Their modified Gauss sums are the negatives of the usual Gauss sums; there are six factors, so their normalized Jacobi character is precisely rho, with no remaining sign. Theorem 1.6 and (2) prove (1) uniformly, not just at the finite primes checked in U39. Its statement, its canonical residue-character definition, and the gamma normalization were reread in the primary source, including rendered printed pp.56 and 58. This is an external theorem application, not an independent reproof of Deligne's theorem and not a Hodge-conjecture assumption.

For the degree assertion, at a prime of K above 2, v(C0)=8 and K is unramified. The equation t^35=C0 forces 35|[K(t):K], hence the degree is exactly 35. At primes above 5 and 7, v(Delta)=1, since only the order-5 and order-7 factors in its product are nonunits. Thus Delta is not a square. The quadratic and degree-35 extensions intersect trivially. Finally, for eta=t*sqrt(Delta),

    eta^70=D0,  t=eta^36/(C0 Delta^18).

This proves K(eta)=E and cyclic degree 70 using roots of unity already in K.

## 2. Reconciliation with the pinned remote U39

The remote argument instead defines

    D_R = -2^32 * 5^15 / 7^7,
    R_R = 2 * 5^30 * 7^14,
    C_R = (2^16 * 5^7 / 7^4) tau,

where tau=T(zeta), tau^2=-35, and

    T(x)=4x^22+2x^21+2x^20-4x^16-4x^15-2x^14
         +4x^11+2x^10+4x^9+4x^8-2x^5-4x^4+1.

It proves rho^2=kappa_(D_R) and the necessary degree-35 subfield K(R_R^(1/35)), but leaves the quadratic character rho/kappa_(C_R) unresolved.

The following exact identities reconcile the squared characters and degree-35 fields:

    D_R/C0^4 = -(5/7)^35 = (tau/7)^70,                 (3)
    R_R = C0^22 * (5^4/(2^5*7^4))^35.                 (4)

Since gcd(22,35)=1, (4) implies K(R_R^(1/35))=K(C0^(1/35)). Equation (3) implies kappa_(D_R)=kappa_(C0^4). Thus there is no conflict between the two squared-character formulas.

For the **exact remaining quadratic character in the remote convention**, put s=-tau/7. Then

    C_R = C0^2 s^35,
    rho/kappa_(C_R) = kappa_(Delta/s)^35.              (5)

Consequently its quadratic field is explicitly

    K(sqrt(-7 Delta/tau)).                            (6)

It would be incorrect to identify the remote quotient character with the quadratic character of Delta alone: that is the quadratic factor relative to kappa_(C0^2), not relative to kappa_(C_R). The factor s in (5) accounts for this distinction. The valuation at 5 of Delta/s is 1-2=-1, so the character (5) is genuinely nontrivial. Exact comparison with the pinned Jacobi data gives the quotient exponents 0,0,0,35,0,35,0,35 at 71,211,281,421,491,631,701,911. These comparisons corroborate (5); equations (1) and (5), not these eight examples, establish its universal validity.

The comparison field in (6) is not the same object as the unique quadratic subfield of E, which is K(sqrt(Delta)). In fact the discarded candidate L0=K(C_R^(1/70)) has the exact description

    M=K(C0^(1/35)),  L0=M(sqrt(s)),  E=M(sqrt(Delta)),
    E intersect L0=M,  [E L0:K]=140.

To check this without fitting Frobenius values, s has valuation -3 at 7, Delta has valuation 1 at 5, and Delta/s has valuation -1 at 5. All three are nonsquares in K, so the two quadratic extensions are independent. They remain independent after the odd-degree extension M/K. The same recovery formula as in Section 1 shows that a 70th root of C_R generates M(sqrt(s)). This proves the stated intersection and compositum degrees and explains exactly why the tempting remote candidate was the wrong field.

## 3. A real, degree-12 coefficient presentation

There is a simpler exact presentation for the arithmetic-normalizing hypersurface. Set

    delta = zeta^2 Delta.

The eight exponents in Delta sum to 136. Hence conjugation sends Delta to zeta^4 Delta and fixes delta. In the chosen complex embedding,

    delta = 2^8 product_(a in {1,4,9,16,22,26,28,30}) sin(pi*a/70) > 0.

In particular delta lies in the maximal real cyclotomic subfield K^+, and

    D0 = C0^2 delta^35.                               (7)

An exact polynomial for delta is

    p(t)=t^12-35t^11-210t^10+7805t^9+58170t^8+29925t^7
         -281575t^6-118825t^5+307475t^4+98000t^3
         -79625t^2-12250t+6125.                       (8)

The resultant of Phi_70(x) and t-x^2 Delta(x) is exactly p(t)^2. Delta(x) here means its residue polynomial modulo Phi_70. Both SymPy and Wolfram verify that identity. The embedding is specified by the product defining delta, not by selecting an unspecified root of (8).

There is also a structural minimal-degree check. Let F=Q(delta). At 5 and 7, respectively, K/Q has ramification indices 4 and 6, and v_K(delta)=1. Since e(K/F) divides the valuation of every F-element, these relative indices are 1. Thus [F:Q] is divisible by both 4 and 6 and hence by 12. But F is contained in K^+, of degree 12. Therefore F=K^+ and (8) is the minimal polynomial. The same reasoning applies to D0, whose valuations at 5 and 7 are -5 and 119, coprime to 4 and 6 respectively: Q(D0)=K^+.

Thus the hypersurface with first coefficient D0 is defined over an explicitly presented real number field of degree 12. The target block is asserted Galois-invariant after base change to K, not necessarily already over K^+.

## 4. Classification of all diagonal normalizations over K

Let d_0,...,d_5 be arbitrary nonzero elements of K, and put

    X_d : sum_i d_i y_i^70=0,
    P_d = product_i d_i^(alpha_i).

**Proposition.** The normalized target block on X_d is G_K-invariant if and only if

    P_d = D0 b^70 for some b in K*.                    (9)

**Proof.** At every good prime away from the coefficients and 70, changing variables in the diagonal Jacobi sum multiplies the alpha eigenvalue by chi(P_d)^(-1). Equivalently, descent of the diagonal isomorphism over a field containing all 70th roots of d_i gives

    rho_d = rho * kappa_(P_d)^(-1).

The same equation for u*alpha is its u-th power. Equation (1) and the injectivity of the Kummer correspondence K*/K*70 into mu_70-valued characters prove (9). One can equivalently compare at all good Frobenius elements and use density; finite-prime agreement alone is insufficient. This proof addresses a representation, not the surjectivity of a cycle-class map. QED.

For d_0=D0 and other coefficients 1, (9) holds, recovering the explicit twist. **No choice with all six d_i rational can satisfy (9).** Indeed v_K(P_d) at 5 is divisible by 4 and is therefore even. The right side has valuation -5+70v_K(b), which is odd. This excludes rational-coefficient diagonal normalizations, not rational varieties in general and not cycles over arbitrary number fields.

For a cycle already defined over a finite L/K on this normalized twist, its rational trace to K preserves its target component after division by [L:K]: all conjugate target components are equal because the block is G_K-invariant. This is a useful descent operation on an existing witness; it does not supply the initial witness. Nothing here infers algebraicity from Galois invariance.

## 5. Reproducibility, review, and next construction question

The new standalone exact checker does not import either competing U39 checker. It verifies the formal certificate, (3)–(5), the cyclotomic square, (8), the quadratic comparison data, and the valuation arithmetic. The inherited local U39 and U37–U38 tests are run separately without overwriting their evidence. Independent Wolfram input and output are preserved alongside the new code. Their agreement is arithmetic corroboration, not independent expert review.

A first implementation expanded a degree-770 expression before reduction and exceeded its time bound. The interrupted log is retained. Binary powering in the degree-24 cyclotomic quotient fixes the implementation without changing the assertion. No interrupted run is counted as a success.

The next issue is geometric: construct a target-bearing cycle or graded matrix factorization on the normalized twist. U41 executes a substantive restriction of that search and explicitly audits the danger of inferring vanishing for direct summands from vanishing for their parent object. The full conjecture and even algebraicity of this single block remain open in this project.

### Primary references and scope of use

[1] D. S. Kubert and S. Lichtenbaum, *Jacobi-sum Hecke characters and Gauss-sum identities*, Compositio Mathematica 48 (1983), 55–87, Definitions 1.1–1.4, Theorem 1.6, and the multiplication identities in Section 2. https://www.numdam.org/item/CM_1983__48_1_55_0.pdf . Used for the normalized gamma/Artin-character implication, not a cycle construction.

[2] J. S. Milne, *Fields and Galois Theory*, version 5.10, September 2022, Section 5, Kummer theory, Theorem 5.30. https://www.jmilne.org/math/CourseNotes/FT.pdf . Used for equality of Kummer characters and equality modulo powers. The valuation facts use the cyclotomic ramification inputs already pinned in both U39 arguments.

[3] The pinned remote U39 and the independently preserved local U39 above contain the complete comparison and good-reduction references. Only their precise common normalized character, not their status labels or all earlier project claims, is reused. The extra quadratic factor is determined here using [1] and the displayed certificate.

Source checks: 2026-09-15. This is a new project derivation from known inputs; no global novelty claim or claim of expert acceptance is made.
