# U44: a level-stable parity obstruction and an enlarged geometric-seed audit

**Status:** the uniform group-theoretic statements are proved below; the explicitly bounded seed statement has a complete finite certificate and two separate arithmetic implementations for its main census. Adversarially self-reviewed, not formally verified or independently expert-reviewed. No new cycle on the original fourfold and no resolution of the rational Hodge conjecture are claimed.

Date: 2026-09-15. Base: `Joe-Simo/hodge-conjecture@f7d6581d58f28b4faffee0366b0907b1a3a20223` (U43). Files and writes remain in the existing Hodge workspace and private repository. Previous proofs are retained, not globally revalidated.

## 1. Target and the route actually tested

Let X be the degree-70 Fermat fourfold, alpha=(1,20,24,42,61,62), and W its rational 24-dimensional primitive (2,2) orbit block. U43 constructs a rational rank-one Chow summand N, with Wcal isomorphic to 24 copies of N and N tensor N isomorphic to L^4. The missing step is still a nonzero realized algebraic morphism L^2 -> N, not another correspondence on X x X.

This attempt tests a specific way to obtain that morphism: enlarge the **formal identity calculus** of U42-U43 to higher Fermat levels, and add relations coming from algebraic divisors. A failure in this calculus is not a proof that the actual Chow motive is nontrivial. The map from formal symbols to actual motivic isomorphism classes need not be injective.

## 2. Exact formal presentation

For m>=2 let F_m be the free abelian group with basis e_a for 1<=a<m and one extra symbol ell. The symbol ell records a Lefschetz factor; these are integer tensor exponents, not coefficients of algebraic cycles. Define

    R_m(a) = e_a + e_(m-a) - ell,                    1<=a<m,

    D_m(n,a) = sum_(j=0)^(n-1) e_(a+jm/n)
                 - e_(na) - sum_(j=1)^(n-1) e_(jm/n),

where n>1 divides m and na is nonzero modulo m. Every subscript is reduced modulo m. Admissibility ensures every displayed subscript is nonzero. Let J_m be the integer span of **all** such R and D, including composite n and all admissible a, not merely a reduced generator list.

For an even-length tuple beta of nonzero residues, set

    t_m(beta) = sum_i e_(beta_i) - (#beta/2) ell.

The normalized target is t_70(alpha). Its actual motivic interpretation in U42 is [M_alpha]-2[L]. The formulas above extend the same formal presentation. Our negative result remains valid even if some additional D relations are treated as a relaxation rather than supplied with an explicit geometric derivation.

For m|M, the map e_a -> e_((M/m)a), ell -> ell sends J_m into J_M, directly from the displayed formulas. It is the correct scaling of the character under a coordinate power map, not arbitrary reduction modulo the old level.

## 3. Uniform parity lemma

**Lemma.** Let d divide m, assume d is odd and gcd(d,m/d)=1, and let C_d be the subgroup of order d in C_m=Z/m. Define an F_2-valued homomorphism by

    epsilon_(m,d)(ell)=0,
    epsilon_(m,d)(e_a)=1 if a is a nonzero element of C_d, and 0 otherwise.

Equivalently, epsilon(e_a)=1 precisely when the additive order m/gcd(m,a) divides d. Then epsilon annihilates J_m.

**Proof.** Negation preserves C_d, so every reflection has value zero. Fix D_m(n,a). Its numerator indices form the coset a+C_n, where C_n is the kernel of multiplication by n in C_m. The denominator subgroup indices are C_n minus zero.

Use the direct decomposition C_m=C_d direct sum C_(m/d). Write a=a_d+a_q. The coset a+C_n meets C_d if and only if n a_q=0, equivalently na belongs to C_d: if n a_q=0, adding -a_q, which lies in C_n, gives a_d. A nonempty intersection has size |C_d intersection C_n|=gcd(d,n), an odd number. Since na is nonzero, the coset cannot contain zero. Thus the numerator's parity equals epsilon(e_(na)).

The denominator contributes gcd(d,n)-1, which is even. These two observations prove epsilon(D_m(n,a))=0. This covers every admissible a and every divisor n, not just prime n. QED.

Both hypotheses matter. For m=6,d=2, the even subgroup gives value one on D_6(2,1). For m=9,d=3, the non-direct-factor subgroup gives value one on D_9(3,1). These are intentional failing controls in the checker.

### 3.1 Consequence at every multiple of 70

For any odd prime p|m choose d=p^(v_p(m)). The lemma then gives

    epsilon_(m,p)(e_a)=1 iff the additive order of a is a nontrivial p-power.

The coordinate power-map lift a -> k a from level m to km preserves the additive order exactly. Therefore these prime-primary parities are compatible with every level increase, including increases divisible by p itself.

The six orders of alpha at70, and of k alpha at70k, are

    (70,7,35,5,70,35).

Consequently the normalized target has parity one for p=5 and for p=7, at **every** level70k and for every unit conjugate. It is nonzero modulo J_(70k).

The exact square certificate of U42 lifts to every level. For completeness its nonzero coefficients at70 are:

    R(a), coefficient:
    (1,1),(4,1),(9,1),(16,1),(22,-1),(24,2),(26,1),(28,-1),(30,1).

    D(n,a), coefficient:
    (2,1,1),(2,9,-1),(2,26,1),(2,34,-1),
    (5,4,-1),(5,6,1),(5,12,-1),(7,2,1),(7,6,-1).

Their sum is 2 t_70(alpha); the standalone checker re-adds the vectors exactly. Scaling replaces every a by ka and preserves n. It follows that the target has **exact order two** in F_(70k)/J_(70k) for every k>=1, and stays nonzero in the direct limit over all these levels.

Thus no number of applications of these reflection/multiplication identities, even after arbitrary pure level enlargement, can establish the unsquared target identity. This is a theorem about a presentation. It does not prove that N tensor L^(-2) is a nontrivial Chow motive. Rational coefficients on cycles do not license division by two in this integer group of tensor exponents.

## 4. Why additional algebraic inputs had to be tested

The preceding parity does not vanish on all known algebraic motives. At level21 the surface tuple

    beta=(1,4,18,19)

has least-positive-residue sum42 at every unit, hence gives a divisor Hodge block. Its orders are (21,21,7,21), so epsilon_(21,7)(t_21(beta))=1. Divisor algebraicity therefore supplies a genuinely new relation, beyond J_21.

This is an explicit warning against interpreting Section3 as nonalgebraicity. It also motivates the next experiment rather than merely increasing the previous search bound.

## 5. A stronger, completely specified test at level420

The common level420 simultaneously admits the degree70 target, degree20 and21 exceptional divisor inputs, and the full degree105 fourfold character population. It also includes the degree28 curve-join example and every lower-level divisor input whose level divides420.

Enlarge J_420 by the following sets of additional formal relations:

A. t_420(beta) for **every** nonzero four-tuple beta satisfying

       sum_i <u beta_i>_420 = 840 for every unit u modulo420.

These are all primitive rational divisor-character blocks on the Fermat surface.

B. t_420(beta concatenated gamma) for all nonzero zero-sum character triples beta,gamma for which the product of their curve H^1 lines is of type(1,1) at every unit. Divisors on the smooth projective product of the two Fermat curves give these algebraic inputs; the extra Tate factor in the Fermat join explains the six-entry normalization.

C. t_420(4 delta) for **every** nonzero six-tuple delta at level105 with residue sum315 at every unit. For purposes of this negative test, grant all these relations. No unverified theorem about their algebraicity is needed: enlarging the relation subgroup can only make the test stronger.

Call the resulting integer subgroup J_420^aug. Permutations, repetitions of entries, both signs, and every unit conjugate are included in these definitions.

**Finite certificate theorem.** The class t_420(6 alpha) is nonzero, and has exact order two, in F_420/J_420^aug.

The dual certificate is particularly small:

    psi(ell)=0,
    psi(e_a)=1 iff 420/gcd(420,a) is 7 or21.              (5.1)

It is epsilon_(420,21)+epsilon_(420,3). Both21 and3 are odd direct-factor subgroup orders at420, so Section3 proves that it kills all R and D. The target has value one. The remaining seed checks are the following exact finite assertions:

| Exhaustive population | Count | Certificate failures |
| --- | ---: | ---: |
| R_420(a), including duplicate signs | 419 | 0 |
| All admissible D_420(n,a) | 8,317 | 0 |
| Sorted surface Hodge quadruples, allowing repeats | 23,307 | 0 |
| Sorted nonzero Fermat-curve character triples | 29,400 | See profile test below |
| Ordered pairs of these triples giving Hodge type(1,1) | 39,604 | 0 |
| Sorted degree105 fourfold Hodge sextuples | 27,690 | 0 |

The curve triples form27,404 distinct half-unit Hodge-profile groups. Within each group, the value of psi on the triple is constant. Negation preserves psi and reverses the Hodge profile; therefore every Hodge pair has total value zero. This tests all39,604 ordered pairs (19,802 unordered pairs), not just one convenient pair per group.

Because psi kills every generator, it kills **every integer combination**, without a bound on the number of summands or on the depth of cancellation. It cannot kill the target. The lifted U42 square certificate proves exact order two also in this enlarged quotient.

### 5.1 Coverage proof for the finite census

A tuple is always sorted, and coordinate repetition is allowed. Split a four-tuple uniquely into its first and last two entries; split a six-tuple into its first and last three. Enumerate all sorted half-tuples and record their vectors of residue sums over one representative of each pair of units u,-u. Match complementary profiles: totals2m for a quadruple, 3m for a sextuple. Retain exactly pairs whose middle entries are in increasing order. Every sorted admissible tuple has exactly this middle split; none is omitted or counted twice.

Testing half the unit group is sufficient because all residues are nonzero and <(-u)a>_m=m-<ua>_m. The checker additionally retests every accepted tuple against **all** units. Permutation invariance of the Hodge test and of psi extends the result from sorted tuples to all indexed tuples.

For curves enumerate a<=b, set c=(-a-b) mod420, and retain c>=b. This is exactly every sorted nonzero zero-sum triple. Its Hodge profile consists of grades1 or2. A pair is Hodge exactly when the two profiles add to3 coordinatewise. The two opposite profile groups have equal cardinality by negation, giving sum of squared group sizes =39,604 ordered pairs.

The code uses only exact integer residues, not floating linear algebra, reconstructed periods, or an oracle claiming irreducibility. The short order-based functional in (5.1), not a Smith solver or an opaque nullspace vector, is the decisive certificate.

### 5.2 Independent and negative controls

The separate Wolfram implementation enumerates quadruples by three nested loops with the fourth entry forced by total840, rather than the Python meet-in-the-middle algorithm. It independently returns23,307 accepted quadruples and zero odd values, and checks all8,317 D relations. A second successful Wolfram call separately confirms the29,400 curve triples,27,404 profiles,39,604 ordered pairs and constant profile parity.

A combined Wolfram sextuple/curve call returned HTTP502 without a mathematical result. It is not evidence. The complete degree105 sextuple census is checked in exact Python and rechecked against all units, but its full population was **not** independently reproduced in Wolfram in this run. Small direct brute-force censuses independently test the Python enumeration logic.

The level21 divisor above violates the old primary7 parity but satisfies the new psi test after lifting to420. Thus the augmented test does not silently reuse an invariant already falsified by its own new inputs.

## 6. Source and interpretation audit

[OY] Otsubo-Yamazaki, *Motivic Gauss and Jacobi sums*, arXiv:2402.06072v3, Section4.2 and Theorem7.2: https://arxiv.org/html/2402.06072v3 . The characteristic-zero multiplication statement was read directly, including its root-of-unity and nontriviality hypotheses. The relation-to-Chow dictionary is the pinned U42-U43 construction; our new uniform proof is a direct cyclic-group argument, not an extrapolation of finite-field sums.

[DS] G. da Silva Jr., *Notes on the Hodge conjecture for Fermat varieties*, Experimental Results2(2021), e22, DOI10.1017/exp.2021.14, Section2, Theorems2.1-2.2: https://doi.org/10.1017/exp.2021.14 . The full publisher HTML records the Fermat character/Hodge criterion and the correspondence decomposition. Divisor algebraicity uses the classical Lefschetz(1,1) theorem on smooth projective surfaces and on products of curves; it is not an assumption of the general Hodge conjecture.

[J] R. Jumagulov, *The Hodge conjecture for Fermat fourfolds of odd degree at most199*, served arXiv:2608.18134v1, AppendixD: https://arxiv.org/html/2608.18134v1 . This preprint reports a remaining degree70 family beyond its closure methods. It motivated comparison with degree105; it is **not a theorem input** to our finite negative result, which grants all degree105 sextuple seeds. The served version/header dating is not silently reconciled. Its entire ancillary computation was not reverified here.

[K] B. Kahn, *Motivic zeta functions of motives*, arXiv:math/0606424, Conjecture2, was revisited as in U43: a general classification of rational invertible Chow motives is not used as an unconditional root-extraction theorem. The rank-one reduction was read in full, including its coefficient descent and its warning about product classes versus original cycles.

A focused search also located Kubert's1979 and Anderson's1997/1999 work on sign-cohomology of the universal ordinary distribution. Those were discovery records, not additional proof inputs. No global novelty claim is made for parity methods or for this specialized application.

## 7. Self-review, consequence, and next executable obligation

The primary verdict for Sections3-5 is **proved as written within the explicitly defined formal calculus**, with the finite portion supported by complete executable checks. The mathematical review is by the same assistant. Arithmetic engine agreement is not independent expert verification.

The crucial distinctions are: integer tensor exponents versus rational cycle coefficients; all-level R/D-only obstruction versus one-level augmented obstruction; a formal quotient versus the actual Picard group of Chow motives; and granted seeds versus a proof of their algebraicity. None is interchangeable with another.

The new result removes two concrete proposed escapes from the U43 bottleneck: arbitrary higher-level reflection/multiplication identities, and the precisely enlarged divisor/curve/degree105 seed calculus at420. It does not eliminate a relation with genuinely new geometry, a different higher-level seed family, or morphisms/idempotents not encoded by this additive identity calculus. It is not a completeness theorem for the tensor category generated by these objects under arbitrary sums, morphisms and retracts.

**Next obligation:** construct a geometrically new correspondence with a nonzero realized map L^2 -> N, or find an additional *independently algebraic* seed whose normalized word has psi-value one and an exact integral transport certificate at a justified common level. Do not merely rerun deeper cancellation searches inside J_420^aug: its exclusion is unbounded in expression length. The U43 surface-support approach remains separate and unexecuted here.

Run the standalone verification from the project root:

    python research/computations/U44/verify_u44.py --output research/computations/U44/verification.json

Nine new tests and the eight U42 plus ten U43 inherited tests pass. Python syntax compilation passes. Native ruff/mypy invocations fail because those modules are not installed; no lint or static-type-check success is claimed. Full input/output hashes, source checks, successful and failed Wolfram scope, and run commands are preserved alongside the checker. The original variety's target cycle remains unconstructed.
