# U41: proper tensor factorizations, the direct-summand loophole, and a uniform retract obstruction

**Status:** the restricted statements below are proved by explicit algebra, with exact computational corroboration and adversarial self-review. Their application to projective Chern characters uses the precisely cited formula. Not formally verified or independently expert-reviewed. No target cycle and no complete Hodge solution have been obtained.

Date: 2026-09-15. Research base: remote `2b4835c05d27f039235fbab8898d7dcee12c9159` and the reconciled arithmetic in U40. Earlier U13–U15 are historical motivation only, not assumptions in the proof.

## 1. Target, objects, and coefficient scope

Work over C, or over any characteristic-zero coefficient field followed by extension to C. Let

    f = sum_(i=0)^5 c_i z_i^70,  c_i != 0,
    X_f = {f=0} in P^5,
    Jac(f) = C[z0,...,z5]/(z0^69,...,z5^69).

This includes the arithmetic-normalized twist of U40. A graded matrix factorization is a finite graded free supermodule with odd differential D satisfying D^2=f id and the usual compatible internal grading. Because 70 is even, the internal shifts may be arranged so that D has degree 35. Write Gamma for the parity operator. The relevant polynomial is

    T(D) = str(partial_5 D ... partial_0 D) in Jac(f),
    str(M) = tr(Gamma M).                             (1)

Its homogeneous degree is 6*(35-1)=204. Under the Griffiths residue identification, it represents the primitive Chern character of the associated sheaf, up to a fixed nonzero scalar and convention-dependent sign [1, Theorem 3.6]. All arguments below concern zero/nonzero, so neither changes the conclusion. The local formula and its endomorphism-inserted version are independently classical [2, Theorem 3.2.3]. We never replace the full six-variable primitive component by a narrower equivariant sector.

The target monomial has exponents

    b = alpha-1 = (0,19,23,41,60,61),
    alpha = (1,20,24,42,61,62).

All its unit conjugates have degree 204. No two alpha coordinates sum to zero modulo 70. Diagonal rescaling changes nonzero coefficients but not this character-support statement. A complex eigenline is distinguished from its whole rational 24-dimensional orbit block throughout.

## 2. Every proper disjoint-block external tensor product fails for this target

Partition the six variables into at least two nonempty disjoint blocks I_1,...,I_t. On each block take any finite-rank **graded** ordinary matrix factorization D_j of f_j=sum_(i in I_j)c_i z_i^70. Form their external super tensor product, with differential

    D = sum_j Gamma_1 tensor ... tensor Gamma_(j-1)
              tensor D_j tensor id tensor ... tensor id.          (2)

**Theorem A.** The coefficient of the target monomial, and of each of its 24 unit conjugates, is zero in T(D). The same holds after finite direct sums, shifts, and mapping cones of such objects. This assertion does **not** automatically include direct summands of cones.

**Proof.** Set n_j=|I_j|, and order the variables block by block; the Chern-character expression is invariant up to the corresponding global sign [2, Corollary 3.2.4]. Let P_j be the product of the n_j derivatives of D_j. Multiplying the Kronecker factors in (2) shows that, up to a sign, (1) is a product of terms

    tr(Gamma_j^(1+sum_(l>j)n_l) P_j).                 (3)

Every derivative of D_j is odd. If any n_j is odd, P_j is off diagonal in the parity decomposition. Multiplication by a power of Gamma_j leaves it off diagonal, so its trace in (3) is zero. The *entire* T(D) then vanishes. This rules out 3+3 at every rank and for every coefficient choice, not merely ordinary Fermat-curve triples. Assigning an order-two character to each ternary block does not repair this ordinary primitive trace.

If every block size is even, a proper partition of six necessarily has a binary block: the only size patterns are 2+4 and 2+2+2. For a graded binary factor the product of its two derivatives, on any diagonal matrix entry, has polynomial degree 70-2=68. One can verify this without equal basis shifts: along a closed two-step matrix path the basis-degree shifts cancel, leaving the sum of the two differential degrees minus two. Therefore every monomial contributed by that block obeys

    b_i+b_j=68,  equivalently a_i+a_j=70.             (4)

Our alpha has no such pair, nor does any unit multiple. Other tensor factors use disjoint variables and cannot alter this pair degree. The monomial Jacobian ideal kills terms; it never replaces an exponent by a smaller exponent. This proves the target vanishing.

Direct sums add traces and parity shifts negate them. For a mapping cone the differential and all its derivatives are block upper triangular. Their diagonal contributions give T(cone)=T(target)-T(source), regardless of variable coupling in the off-diagonal cone map. Iteration proves the asserted closure. QED.

The finite combinatorial check lists 203 set partitions of six elements: 202 proper, 172 with an odd block, and 30 all-even. The structural dichotomy above, not reliance on a black-box census, proves coverage. No genericity, bounded rank, coefficient-height bound, or field-degree bound enters Theorem A.

## 3. Why direct summands require their own proof

An idempotent e is an even closed endomorphism with e^2=e (or its homotopy-category counterpart). A summand selected by e has Chern character

    T(D,e) = str(partial_5 D ... partial_0 D e)        (5)

in the idempotent-completed category [2, Section 1.2 and Theorem 3.2.3]. In particular T(D)=0 does not imply T(D,e)=0. This is not a speculative warning: there is a small exact counterexample.

Let

    G = diag(1,-1),  X = [[0,1],[1,0]],  J = [[0,1],[-1,0]],
    D = x X tensor id + y G tensor X,
    T1 = J tensor id,  T2 = G tensor J,
    e = (id + i T1 T2)/2,  Gamma = G tensor G.

Then D^2=(x^2+y^2)id, e is even, e^2=e, and eD=De. Direct multiplication, in the ordering P=(partial_y D)(partial_x D), gives

    str(P)=0,  str(Pe)=2i,  str(P(1-e))=-2i.           (6)

This is a controlled two-variable example, not an algebraic cycle for the degree-70 target. It disproves a blanket extension of Theorem A to a thick closure. In particular a claim that a collection of objects *split-generates* a category does not imply their individual Chern characters span every summand's Chern character by additivity alone.

## 4. A constructive follow-up: all raw univariate tensor retracts also fail

We next test a concrete way to exploit the loophole. For arbitrary exponents 1<=a_i<=69, take the six rank-one univariate factorizations

    D_i = [[0,z_i^a_i],[c_i z_i^(70-a_i),0]],

and their raw external tensor product F. We allow **any direct summand of F in the homotopy idempotent completion**, not just its obvious constant projectors.

**Theorem B.** Every such summand has zero target coefficient. More precisely, if any a_i is not 35, all its ordinary Chern-character components in Jac(f) vanish. If all a_i=35, its ordinary Chern character is a scalar multiple of

    (z0 z1 z2 z3 z4 z5)^34,                            (7)

whose character is (35,35,35,35,35,35), not the target. Theorem B does not concern retracts of an arbitrary cone built from these tensors.

### 4.1 Exact endomorphism algebra of one factor

Swapping parity if necessary reduces to k_i=min(a_i,70-a_i)<=35; parity shifts change only signs of Chern characters. For one variable z and nonzero c write

    D=[[0,z^k],[c z^(70-k),0]],
    theta=[[0,1],[-c z^(70-2k),0]].

A direct computation with the differential d(h)=Dh-(-1)^|h|hD gives

    H End(D) = (C[z]/(z^k)) plus (C[z]/(z^k)) theta,
    |theta|=1,  theta^2=-c z^(70-2k).                 (8)

For completeness, a closed even endomorphism diag(u,v) has u=v, and the even boundaries generate the ideal (z^k). A closed odd matrix [[0,u],[v,0]] has v=-c z^(70-2k)u; its boundaries are precisely the multiples z^k theta. This proves (8), including its product, without a matrix-factorization classification theorem.

Disjoint variables and the Kunneth identity over the field C identify H End(F) with the super tensor product of the six algebras (8). It has a basis of products of z_i powers below k_i and each theta_i at most once, with distinct theta_i anticommuting. Completion at the origin leaves this finite-dimensional endomorphism cohomology and the finite-dimensional Jacobian quotient unchanged.

### 4.2 Removing the nilpotent part does not lose any idempotent class

Call i balanced when k_i=35. In H End(F), let N be the ideal generated by all z_i and all theta_i for unbalanced i. The quotient is the Clifford algebra generated by balanced theta_i, with theta_i^2=-c_i. That quotient has an explicit algebra section: its generators are represented by the same balanced, constant, odd closed matrices. This also gives a section on the even parts.

The ideal N is nilpotent. Assign weight 2 to each z_i, weight 1 to each unbalanced theta_i, and weight 0 to balanced theta_i. Reductions by (8) never decrease weight, and a nonzero basis element has weight at most

    M=2 sum_i(k_i-1)+number of unbalanced indices.

Thus N^(M+1)=0. This is an explicit proof of nilpotence, not an assumption that all individual nilpotents generate a nilpotent ideal.

Let e be any idempotent in the even endomorphism cohomology. Project it to the quotient and lift it by the section to a constant balanced-Clifford idempotent e0. Then e-e0 is in N, and

    u=e e0+(1-e)(1-e0)

satisfies eu=ue0 and u=1 modulo N. The finite geometric series in 1-u is its inverse. Hence e and e0 select isomorphic objects in the homotopy idempotent completion and have the same Chern character. This also treats a polynomial strict idempotent, by passing to its cohomology class. Categorical trace depends only on that class [2].

### 4.3 Computing the surviving inserted traces

The constant representative e0 is a linear combination of even products of the odd closed matrices belonging to balanced variables only. If some variable is unbalanced, its single derivative in (5) remains an odd local matrix; all insertions on that variable are only identity or parity operators. The trace factors as in Section 2 and is zero. This proves the first alternative of Theorem B.

If every variable is balanced, each derivative is

    partial_i D = 35 z_i^34 K_i

for a constant matrix K_i. Therefore even (5) with an arbitrary **polynomial** idempotent has the common monomial factor (7). Reduction modulo the monomial Jacobian ideal cannot lower exponents. In degree 204, the only possible surviving monomial is exactly (7). The endomorphism-algebra argument gives the same conclusion for homotopy retracts, not just strict polynomial ones.

The target has total degree 204 but is not (34,34,34,34,34,34); at least one exponent of every conjugate is below 34. Its coefficient is consequently zero. This completes the proof. QED.

A positive control verifies that the balanced calculation is not falsely proving every inserted trace zero. For c_i=1, take three commuting even involutions i*T0*T1, i*T2*T3, i*T4*T5 from the balanced Clifford operators, and multiply their +1 projectors. The resulting 64-by-64 projector has a nonzero inserted trace. Its support is (7), exactly as the theorem permits.

## 5. Research impact and exact remaining opening

These results hold after arbitrary nonzero diagonal twisting, so U40's arithmetic normalization does not revive ordinary 3+3 tensors, binary-block tensors, or any raw rank-one univariate tensor retract. The proofs cover all finite factor ranks in Theorem A and all 69^6 univariate exponent choices in Theorem B without enumerating that enormous product.

They do **not** exclude a six-variable factorization with genuine coupling, a nontrivial direct summand of a cone, a different algebraic correspondence, or a surface outside these construction families. In particular (6) is a positive demonstration of a mechanism that defeats naive additivity-based exclusion. A next admissible construction must provide either a new globally graded factorization or an explicit even closed idempotent on a nontrivial cone, and must compute its inserted trace, not just that of its parent. The required geometric coefficient remains the same target monomial. No invariant-to-algebraic inference has been added.

The rational Hodge conjecture, and the algebraicity of this individual block, are not settled here. No novelty beyond the scope of the cited input and this project derivation is claimed.

## 6. Checks, dependencies, and self-review

`computations/U41/verify_u41.py` uses exact SymPy arithmetic. Its focused tests cover complete set-partition counts, all 24 target conjugates, a symbolic odd-block trace identity, a nonzero binary control, (6) and a deliberately invalid projector, (8) at all 69 exponent choices, the conjugacy identity, the balanced 64-by-64 nonzero control, and an unbalanced-variable vanishing control. These are corroborations; Sections 2 and 4 provide the quantified mathematical bridges.

A separate Wolfram kernel reproduced (6), the idempotent and commutation identities, all 69 versions of (8), and the partition counts using integer partitions rather than the Python set-partition iterator. It did not independently verify the entire categorical interpretation or the proof about all idempotents. The review remains self-review.

The adversarial pass checked: the original projective/rational target; the field of coefficients versus the complex calculation; ordinary versus equivariant sectors; parity versus internal grading; arbitrary rank versus bounded tests; monomial Jacobian reduction; cone additivity versus retracts; nilpotence of an ideal versus of its generators; cohomological conjugacy versus polynomial invertibility; and the explicit positive controls. The precise limitation about retracts of cones is essential and intentionally retained.

### Primary source record

[1] David Favero and Tyler L. Kelly, *The Chern Character of a coherent sheaf on a smooth projective hypersurface*, arXiv:2609.12759v1, 11 September 2026, Theorem 3.6 and its proof in Section 3.2; Propositions 4.2–4.4 for Fermat characters. https://arxiv.org/html/2609.12759v1 . This is a checked primary **preprint**, not asserted peer-reviewed publication. Its projective formula is the external interpretation used in (1). The matrix vanishing arguments themselves are elementary identities. Reversal of derivative ordering affects a sign, not the zero statement.

[2] Alexander Polishchuk and Arkady Vaintrob, *Chern characters and Hirzebruch–Riemann–Roch formula for matrix factorizations*, Duke Mathematical Journal 161 (2012), 1863–1926, DOI 10.1215/00127094-1645540. Pinned author version arXiv:1002.2116v3 (22 May 2012), Section 1.2, Theorem 3.2.3 and Corollary 3.2.4, manuscript pp.33–34. https://arxiv.org/pdf/1002.2116v3 . These establish the local character and endomorphism-inserted trace. The theorem hypotheses include characteristic zero, an isolated hypersurface singularity, and finite-rank matrix factorizations; f satisfies them.

Sources checked 2026-09-15. The text and formulas of [2] were available in the primary PDF; web screenshot attempts returned errors, so no successful rendered-page inspection of [2] is claimed. The source-dependent projective step and the self-reviewed deduction are explicitly distinguished from formal proof verification.
