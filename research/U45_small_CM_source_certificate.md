# U45: a five-unit certificate for all small-profile CM source words

**Status:** the restricted formal obstruction below is proved by an exact finite certificate and an unbounded linear argument; its finite inputs were independently recomputed in Python and Wolfram. Adversarially self-reviewed, not formally verified or independently expert-reviewed. No target-bearing surface and no resolution of the rational Hodge conjecture are claimed.

Date: 2026-09-15. Pinned remote base: `Joe-Simo/hodge-conjecture@bfdb70edaae96b5ec0aaef8782ab3baffd448826` (U44). The existing local evidence was inspected and retained; only missing computation files were restored from the supplied U44 archive. This note does not globally revalidate historical claims.

## 1. New route and exact target

The target remains the rational 24-dimensional primitive (2,2) block W on

    X = {z0^70+z1^70+z2^70+z3^70+z4^70+z5^70=0} in P^5_C,
    alpha = (1,20,24,42,61,62).

U43 reduced this block to copies of a rational rank-one motive N whose square is L^4. Its outstanding obligation is a nonzero realized algebraic map L^2 -> N. U44 excluded reflection/multiplication identities supplemented by certain divisor and degree105 inputs, not arbitrary further algebraic geometry.

The different input tested here is Hodge tensors from small simple CM factors of Fermat Jacobians. This is motivated by Markman's algebraicity results for abelian fourfolds and split Weil sixfolds, and the reported consequence for abelian varieties of dimension at most five [1,2]. Rather than require a separate cycle construction or discriminant test for every candidate, the negative test **grants every Hodge tensor word** built from the specified small profiles, including arbitrary products and signed cancellations. It therefore tests a strictly defined relaxation of the proposed source method.

No Hodge conjecture for abelian eightfolds is assumed. The word calculus is not claimed to contain every algebraic correspondence that can involve an abelian variety.

## 2. Profiles and the size cutoff

Fix m=420 and U=(Z/420)^*, with |U|=96. A curve triple beta=(a,b,c) has nonzero entries modulo420 and a+b+c=0 modulo420. Coordinate permutations are immaterial, so list triples in increasing order, permitting repetitions. Write <a> for the positive residue modulo420.

Define its Hodge profile

    p_beta(u) = (<ua>+<ub>+<uc>)/420 - 1,     u in U.

It has values in {0,1}, and p_beta(-u)=1-p_beta(u). A choice between this grading and its complement exchanges (1,0) and (0,1) and does not change any Hodge-balance condition below. Translation by v in U sends p(u) to p(vu). Put

    g(beta) = (number of distinct U-translates of p_beta)/2.

This is an integer: negation complements the profile and cannot stabilize it. Let B_small be the set of all curve triples with g(beta)<=8.

### The CM dictionary, and its limitation

A curve character of conductor d|420 is a line over Q(zeta_d) in a rational weight-one CM Hodge structure. Pull its type back to K_420=Q(zeta_420). If H is the stabilizer of its profile, the type is constant on cosets of H and descends to F=K_420^H. The field F is CM because complex conjugation is not in H. Its type is primitive: a descent to a smaller CM field would give a strictly larger stabilizer. Thus [F:Q]=|U/H|=2g(beta).

Equivalently, the corresponding primitive/simple CM abelian factor has complex dimension g(beta). The elementary reason an induced type gives repeated factors is that an F-basis of Q(zeta_d) identifies its weight-one Hodge structure with copies of F with the descended type; all embeddings above one embedding of F have the same grading. Standard CM-pair classification and the primitive/simple criterion are stated in [3, Section 2.1]. This dictionary describes *these Fermat-derived profiles*, not all CM types in all fields.

In particular, all products, powers, and determinant-type Hodge words from this list of simple factors of dimension at most eight are included. A low-dimensional abelian variety not represented by these profiles, or a different correspondence outside the formal calculus, is not excluded by the theorem.

## 3. The finite certificate

Use U44's functional on its free abelian group F_420:

    psi(ell)=0,
    psi(e_a)=1 iff the additive order 420/gcd(420,a) is 7 or21.

For a curve triple write epsilon(beta)=psi(e_a+e_b+e_c). The new certificate is

    epsilon(beta) = sum_(v in {11,23,37,59,71})
                       (p_beta(v)-p_beta(1))  modulo2,        (3.1)

for **every beta in B_small**. All five listed numbers are units modulo420.

This is a finite identity, with the following complete census:

| g | Profile orbits | Distinct profiles | Sorted curve triples |
|---|---:|---:|---:|
| 1 | 5 | 10 | 88 |
| 2 | 2 | 8 | 100 |
| 3 | 3 | 18 | 96 |
| 4 | 5 | 40 | 200 |
| 6 | 16 | 192 | 444 |
| 8 | 4 | 64 | 224 |
| **Total <=8** | **35** | **332** | **1,152** |

There are no g=5 or7 profiles. For the full population there are 29,400 sorted curve triples, 27,404 profiles, and447 profile orbits. The complete orbit count by g is

    {1:5, 2:2, 3:3, 4:5, 6:16, 8:4, 12:60, 24:170, 48:182}.

Equation (3.1) fails for zero of the1,152 applicable triples. Both Python and Wolfram independently reconstruct the full population, orbit sizes, applicable triples, and certificate.

### Coverage and reproducibility

Any sorted nonzero zero-sum triple has ordinary sum420 or840. The standalone Python checker iterates these two sums and every1<=a<=b<420, sets c=sum-a-b, and retains exactly b<=c<420. This is a bijective enumeration, not a sample or a degree-bound guess. It tests all96 units, groups profiles, and computes each complete unit orbit. A direct orbit-stabilizer calculation separately checks each of the35 small profile orbits.

Wolfram instead derives c as the residue of -a-b and computes the same finite data. The checker does not import the exploratory Gaussian-elimination code. The certificate itself is only the five displayed units; a solver's verdict is not required to check it.

The sorted small-triple/profile/g table has SHA-256

    6d30d5187e836dc6f5b2fe34f132c983085eb6188bf612fcbf71491acf987474

in the explicitly documented serialization in `verification.json`. This hash identifies a reproducible table, not a proof on its own. See `verify_u45.py` for the complete finite certificate.

## 4. Unbounded consequence: any tensor length and signed cancellation

Let (n_beta) be **any finitely supported family of integers**, with beta in B_small, and assume its total profile is constant:

    sum_beta n_beta p_beta(u) = c for every u in U.           (4.1)

This includes ordinary Hodge tensors, duals, and differences of tensors with identical profiles. Comparing u and -u gives sum_beta n_beta=2c. In particular c is an integer and the following normalized formal word is integral:

    w(n) = sum_beta n_beta (e_a+e_b+e_c) - 3c ell.           (4.2)

**Theorem.** Every such w(n) satisfies psi(w(n))=0.

**Proof.** Multiply (3.1) by each integer n_beta and sum. Interchange the two finite sums. For each of the five v, the corresponding difference is

    sum_beta n_beta p_beta(v) - sum_beta n_beta p_beta(1)
       = c-c=0.

The ell term has psi-value zero. Therefore psi(w(n))=0. QED.

There is no bound here on the number of tensor factors, their multiplicities, negative exponents, or cancellation depth. The finite cutoff is on the **profiles of individual factors**, not on the resulting product's dimension or its tensor length.

For 2r actual H^1 factors, (4.1) has c=r and expresses Hodge type(r,r) in every coefficient embedding. The Fermat curve word is e_a+e_b+e_c-ell; subtracting the extra r Lefschetz factors gives exactly (4.2). This agrees with the characteristic-zero Fermat correspondence normalization [4]. The usual CM Hodge-word criterion, including products and powers, is [3, Theorem3.1 and its proof]. Nothing in this identification asserts that an arbitrary Hodge word is already algebraic.

### Exact enlargement of U44

Let B_<=8 be the subgroup of F_420 consisting of the words (4.2), and define

    J_new = J_420^aug + B_<=8,

where J_420^aug is exactly U44's reflection/multiplication/divisor/curve-pair/degree105-seed subgroup. By U44 and the theorem, psi kills J_new. But

    psi(t_420(6alpha))=1.

U44's lifted square certificate has 2t_420(6alpha) in J_420, and was rechecked here coefficient-by-coefficient. Consequently

    t_420(6alpha) has exact order two in F_420/J_new.         (4.3)

This remains a statement about the formal presentation, not a nontriviality theorem for the actual normalized Chow motive N L^(-2). Rational cycle coefficients are not division of integer tensor exponents by two.

## 5. Exact boundary: twelve-dimensional profiles can escape

The cutoff is real, not an untested extrapolation. The triple

    beta=(2,140,278) modulo420

has g=12, epsilon(beta)=0, but the right side of (3.1) is1. This refutes extension of that particular five-unit identity to all g<=12 profiles.

More decisively, take the four level70 curve triples

    beta1=(24,61,55), beta2=(20,15,35),
    beta3=(35,42,63), beta4=(7,62,1),

and lift them by multiplication by6. Their profile dimensions, in this order, are

    (12,3,2,12).

Their four Hodge profiles sum to2 at every one of the96 units; their total psi-value is1. If w is the normalized concatenation word at420, then the exact integer identity is

    w - t_420(6alpha) = R_420(90)+R_420(210)+R_420(42).     (5.1)

Indeed the extra entries are the three complementary pairs (90,330), (210,210), (42,378). The ell coefficients also agree. All intermediate pair sums for the underlying Fermat factorization are nonzero. Thus the familiar curve factorization reaches an odd word as soon as these twelve-dimensional types are admitted; it supplies no independent proof that the word is algebraic.

There are no g=9,10,11 profiles in the complete level420 census. Therefore, within this exact palette, g=12 is the first size permitting an odd Hodge word. This is **not** a universal minimum dimension for an arbitrary source variety or an arbitrary correspondence.

## 6. Audit and research consequence

The earliest executed test was a narrow determinant-word search; the final result replaces its tensor-length bound with the finite certificate (3.1). The exploratory elimination is preserved separately, but the theorem's checker neither imports it nor relies on failure of a search to find an identity. A first checker run caught an incorrectly ordered expected tuple of boundary dimensions (the middle3 and2 had been interchanged); it was corrected and independently rechecked. The original failed log is retained.

The source-driven route therefore fails **within J_new**, even after granting more Hodge words than the currently verified Markman cases. There is no discriminant-based pruning or conjectural algebraicity premise in this negative result. It does not rule out a new motive relation, arbitrary geometric morphisms or retracts, non-Fermat CM types, or new seeds at levels not treated by U45.

The remaining original obligation is unchanged: construct a nonzero realized map L^2 -> N or a target-bearing surface on X. A useful next attempt must supply either an independently algebraic odd word using a larger/new profile type with a justified transport, or a genuinely different surface-supported correspondence. Equation (5.1) isolates four explicit curve factors but is not itself such an independent seed. Do not continue increasing tensor length among the small factors: Section4 already handles every length.

Seven new tests pass; inherited U42-U44 tests and native validation results are recorded separately in the execution manifest. Arithmetic agreement is not an independent expert review or a formal proof of geometric source theorems.

## 7. Sources and commands

[1] E. Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415v2, Theorem1.5.1 and Corollary1.6.1. The theorem covers polarized Weil sixfolds with imaginary quadratic multiplication and discriminant -1; the corollary covers abelian fourfolds. https://arxiv.org/html/2502.03415v2

[2] E. Markman, *Secant sheaves and Weil classes on abelian varieties*, served arXiv:2509.23403v2, Abstract, Theorem1.2, Sections11-12. The abstract reports the consequence for dimension<=5. The served HTML header says11 February2026 while its manuscript date says24 August2026; these are recorded separately, not silently reconciled. https://arxiv.org/html/2509.23403v2

[3] Z. Gao and E. Ullmo, *Hodge cycles and quadratic relations between holomorphic periods on CM abelian varieties*, Journal of the Institute of Mathematics of Jussieu, DOI10.1017/S1474748025101291, publisher HTML, online19 September2025, Section2.1 and Theorem3.1 (Pohlmann), including the displayed proof. Used for CM terminology and the Hodge-word interpretation, not as an algebraicity theorem for our words. https://doi.org/10.1017/S1474748025101291

[4] N. Otsubo and T. Yamazaki, *Motivic Gauss and Jacobi sums*, arXiv:2402.06072v3, Proposition4.11(ii), Theorem7.2, and U42's pinned balanced-word dictionary. The source permits characteristic-zero fields and the relevant character coefficient field. https://arxiv.org/html/2402.06072v3

All sources checked15 September2026. This is a specialized new certificate in this project; no claim of global mathematical novelty is made. Markman's results motivate the attempt but are not assumptions needed to prove (3.1)-(4.3), which grant the entire stated seed population.

Run from the project root:

    python research/computations/U45/verify_u45.py --output research/computations/U45/verification.json

The execution record pins dependencies, checksums, actual outcomes, the independent Wolfram calculation, and validation limitations.
