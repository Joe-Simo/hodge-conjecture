# U38: a primitive order-70 Frobenius eigenvalue restricts cycle fields and component orbits

Status: proved below using classical Frobenius/étale-cohomology results, two exact local algorithms, a separate Wolfram computation, and self-review. Not formally verified or independently expert-reviewed. This is a necessary condition for algebraic-cycle certificates, not a resolution of the rational Hodge conjecture.

Date: 2026-09-15. Base: Joe-Simo/hodge-conjecture@467188a3d6c10a08ab2476fc65c12d14c78771de.

## 1. Exact theorem

Put K=Q(zeta_70), X={z0^70+...+z5^70=0} subset P^5_K, and alpha=(1,20,24,42,61,62). Let W_alpha be the rational primitive cohomology block whose complex character lines are V(u alpha), u in (Z/70Z)^*. It has dimension 24 and Hodge type (2,2); the full 24-element character and residue-sum check is reproduced in the accompanying code.

**Theorem.** Suppose L/K is a finite extension and Z is a codimension-two algebraic cycle on X defined over L, with rational coefficients. If the Betti class of Z has a nonzero projection onto W_alpha, then for every prime pfrak of K above 491 and every prime w of L above pfrak,

    70 divides f(w/pfrak).

In particular,

    70 divides [L:K].

The theorem allows ramification of L/K at 491. The degree condition is necessary, not sufficient. For a field not containing K, apply the assertion to its compositum with K; no unqualified statement about its absolute degree is made.

**Component corollary.** Let Y subset X be any closed subscheme defined over K with finitely many geometric surface components. If one of those components has a nonzero W_alpha projection, then there are at least 70 geometric surface components in its orbit under a local Frobenius lift at 491. Consequently a K-defined candidate with fewer than 70 geometric surface components cannot furnish the target, even if its components are not individually K-defined.

For a K-defined toric intersection as in U37, these must be at least 70 **non-binomial** components. The earlier weaker 'two non-binomial components' condition is therefore not enough for such K-defined constructions.

## 2. Normalization and the exact finite assertion

For a prime p=1 mod 70, let g be the least primitive root of F_p^*, and define chi(g)=zeta_70. Extend every nontrivial character by zero at zero. Set

    j_p(alpha) = 1/(p-1) * sum_{v_i in F_p^*, sum v_i=0}
                                  product_i chi(v_i)^(alpha_i).

The normalization is **positive** in dimension four. Scaling all six coordinates by v0^(-1) changes the equation to 1+v1+...+v5=0, with no character multiplier since sum alpha_i=0 mod 70. Thus this formula is precisely Shioda-Katsura (3.4), whose sign is (-1)^r with r=4; their (3.1)-(3.2) identify it as a primitive Frobenius eigenvalue. Depending on whether characters are indexed by pullback or inverse pullback, alpha may be replaced by -alpha; that replacement belongs to the same rational block and does not change any order below.

Exact computations in Z[zeta_70], with no floating-point approximation, give:

| p | least primitive root g | j_p(alpha)/p^2 | exact order |
|---|---:|---|---:|
| 71 | 7 | zeta_70^40 | 7 |
| 211 | 2 | zeta_70^12 | 35 |
| 281 | 3 | zeta_70^32 | 35 |
| 421 | 2 | zeta_70^50 | 7 |
| 491 | 2 | zeta_70^57 = -zeta_70^22 | 70 |

Only the last row is needed for the degree-70 theorem. The other rows independently test the arithmetic implementation and illustrate that the bound from p=71 alone would have been weaker.

In particular, the decisive exact identity is

    j_491(alpha) = -241081 zeta_70^22.

Since gcd(57,70)=1, every conjugate zeta_70^(57u), gcd(u,70)=1, has order 70. Equivalently the characteristic polynomial of normalized Frobenius on W_alpha(2) is Phi_70(T). The source's eigenline description, not merely a nonequivariant total point count, is being used here.

One can choose the prime of K by reducing zeta_70 to 2^7=128 mod 491. All other primes above 491 change the multiplicative character by a unit power, and hence preserve exact order 70. Inverting the Frobenius convention also preserves the order. No unspecified global minus sign is discarded; it is fixed by the dimension-four formula and the independent benchmark below.

## 3. Two different exact algorithms

### 3.1 Four binary Jacobi sums with arbitrary-size integers

Define

    J(a,b) = sum_{t in F_p, t!=0,1} chi(t)^a chi(1-t)^b.

The nonzero successive prefix characters of alpha are 1,21,45,17,8 mod 70. Repeatedly group the first five variables by their sum. Since none of these prefixes is zero, this gives

    j_p(alpha) = chi(-1)^62 J(1,20)J(21,24)J(45,42)J(17,61).

For the primes in the table, chi(-1)^62=1. To check the identity rather than quote a shortcut, the first-five-variable character sum at total t is chi(t)^8 times the product of the four J's when t!=0. At t=0 it vanishes by nontriviality of chi^8. The sixth coordinate must be -t; multiplying its character and summing the p-1 nonzero t's yields the stated formula.

The checker counts each binary sum in Z[C_70], multiplies using arbitrary-size Python integers, then reduces modulo Phi_70. Wolfram independently computes the same binary factors using exact polynomial arithmetic. All four 24-entry reduced coefficient vectors at p=491 are preserved and compared, not just the final root order.

### 3.2 Direct six-variable additive convolution

A second algorithm uses a table indexed by (additive sum in F_p, character exponent in Z/70Z). For each of the six variables, it convolves with all p-1 nonzero values. The additive-sum-zero row divided by p-1 gives j_p directly; it does not use the binary-product identity.

NumPy int64 is used solely for counting. Every entry and intermediate nonnegative sum is bounded by the total population (p-1)^6. At the largest tested p=491 this is 490^6=13,841,287,201,000,000, strictly below 2^63-1. The code checks this bound before allocation and checks the full population after every convolution. Thus the fixed-width implementation is exact in its stated range, not a numerical approximation. Final cyclotomic reduction is exact SymPy integer arithmetic.

Both algorithms agree on the entire cyclotomic power-basis vector at all five primes.

### 3.3 Sign and convention benchmark

For the cubic Fermat fourfold over F_7, the checker separately enumerates all projective points using a unique first-nonzero-coordinate normalization. It obtains 3690 points. It also sums the direct Jacobi values over all 22 primitive characters, obtaining 889. The ambient contribution is 1+7+49+343+2401=2801, and

    3690 = 2801 + 889.

This pins the even-dimensional plus sign independently of the target's root-of-unity result. Additional checks reverse the order of coordinates, invert the multiplicative character, reject invalid inputs, and check that no proper divisor of 70 makes the p=491 root equal to 1.

## 4. Geometric proof of the theorem

Choose a prime ell different from 491, and extend ell-adic coefficients to contain the 70th roots of unity. Because all diagonal Fermat automorphisms are defined over K, their character projectors commute with G_K. The rational orbit projector e_O is the sum of the 24 conjugate line projectors and is defined over Q in the group algebra.

X has smooth proper reduction at every prime above 491: 491 does not divide 70, and the partial derivatives 70 z_i^69 cannot vanish simultaneously at a projective point. Smooth proper base change identifies the local ell-adic representation with that of the reduction and makes inertia act trivially. The Frobenius eigenvalues on the character lines are the Jacobi sums in Section 2. After the Tate twist (2), the eigenvalues on the full orbit block are exactly primitive 70th roots of unity, or their inverses under the opposite Frobenius convention.

A cycle Z defined over L has a G_L-invariant class in H^4_et(X_barK,Q_ell(2)). This uses only naturality of the cycle class map. It is the easy direction underlying the Tate conjecture, not the conjectural assertion that every invariant class is algebraic. Betti/étale comparison carries the rational orbit projector and the nonzero cycle component to the same nonzero component in ell-adic cohomology.

Fix w above pfrak above 491 and put f=f(w/pfrak). A local Frobenius element for L_w acts, on this unramified representation, as the f-th power of a Frobenius for K_pfrak. Since it fixes the nonzero projected class, some primitive 70th-root eigenvalue raised to f must equal 1. Thus 70 divides f. This argument does not require that L_w/K_pfrak be unramified: inertia on the cohomology is already trivial.

Finally the local degree decomposition gives

    [L:K] = sum_{w|pfrak} e(w/pfrak) f(w/pfrak).

Every summand is divisible by 70, proving the field-degree assertion. QED.

## 5. Proof of the component corollary

Choose a local Frobenius lift sigma in G_K at a prime above 491. It permutes the finite set of geometric surface components of a K-defined subscheme Y. Let C have nonzero W_alpha projection, and let n be the length of its sigma-orbit. Then sigma^n fixes C as a cycle, hence fixes its projected cohomology class. But all eigenvalues of sigma on W_alpha(2) have exact order 70. Therefore 70 divides n.

This proof deliberately does not infer individual invariance from invariance of the union, and does not assume that a field of definition of C is unramified. In the toric setting, a binomial component is a classical paired plane by U37 and has zero projection. Its Galois conjugates have that same property; hence the useful orbit consists of at least 70 non-binomial components.

## 6. What is and is not established

Established: an exact necessary field-of-definition and component-count restriction for this specific rational Hodge block. It rules out every individually K-defined cycle and every finite L/K with degree not divisible by 70 as a certificate with nonzero target projection.

Not established:

- existence of a cycle over any extension of degree 70 or greater;
- the minimal field of definition, its ramification, or a sufficient field;
- a contradiction for cycles over C (extensions of degree divisible by 70 are allowed);
- a proof of the Hodge or Tate conjecture, even for this single block;
- a novelty claim about this specialization or the general Frobenius method.

The earlier U36 family is already ruled out geometrically for all complex parameters. The present arithmetic result is a different restriction on other candidates, and must not be advertised as merely reproving U36.

## 7. Audit, evidence, and the next discriminating construction

Self-review dependencies:

1. Target orbit: exact 24-character finite check, repeated here.
2. Jacobi/Frobenius identification: Shioda-Katsura, (3.1)-(3.4), p.107, with sign checked by direct cubic point counting.
3. Arithmetic at 491: two different local algorithms plus Wolfram; four binary factor vectors and full final vector compared.
4. Cycle invariance, comparison and good reduction: standard theorems in the inspected sources below; no cycle conjecture is invoked.
5. Local/global degree implication and component orbits: explicit arguments in Sections 4-5.

Commands:

    python research/computations/U37/verify_u37.py
    python research/computations/U38/verify_u38.py
    python -m py_compile research/computations/U37/verify_u37.py research/computations/U38/verify_u38.py

Twelve focused local tests pass (four in U37 and eight in U38), and syntax compilation passes. The two local checkers, Wolfram input and returned coefficient records, actual outputs and test logs accompany this note. A checksum manifest covers deliverables. GitHub publication is pending: discovery returned 48 read-only actions, no write action, and no GitHub CLI is installed. No remote commit is claimed; the evidence package includes a patch against the pinned base. Lint/static-type tools were absent; an attempted project-local Ruff/Mypy installation failed because the package index was unreachable. Syntax compilation and focused tests run, but no lint/static-type-check success is claimed. The installation error is preserved separately from mathematical results.

Next construction gate: for a K-defined toric intersection, first look for at least 70 non-binomial geometric components and the correct local Frobenius orbit, before calculating their periods. A construction written directly over a larger field must meet the residue-degree condition, not merely an arbitrarily large coefficient degree. Passing either gate is not itself evidence of a nonzero period. No current candidate is marked solved or running in the background.

## 8. Sources actually inspected

[S1] Tetsuji Shioda and Toshiyuki Katsura, *On Fermat varieties*, Tohoku Mathematical Journal 31 (1979), 97-115, DOI 10.2748/tmj/1178229881. Section 3, equations (3.1)-(3.4), printed p.107 (PDF page 11), inspected as a rendered page, and following text identifying the Frobenius eigenvalues. https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf .

[S2] J. S. Milne, *Lectures on Etale Cohomology*, v2.21, March 22, 2013. Section 21 for comparison; Section 23, the natural cycle map and Remark 23.7, printed pp.138-143, for the necessary Galois-invariance direction. https://www.jmilne.org/math/CourseNotes/LEC.pdf . The converse discussed there is conjectural and is not used.

[S3] Kiran S. Kedlaya, authored course notes, Chapter 9, *Etale cohomology as a black box*, Proposition 9.2.2: smooth-projective good reduction gives a Galois-equivariant identification with the special-fiber cohomology and unramifiedness. https://kskedlaya.org/weil-cohom/chapter-9.html . Underlying proper/smooth base-change statements also checked in the Stacks Project, tags 095T and 0EYQ.

[S4] Rifat Jumagulov, arXiv:2608.18134v1 (2026), Sections concerning the m=33 arithmetic certificate. https://arxiv.org/html/2608.18134v1 . Discovery aid for this style of field-of-definition test and an external cubic benchmark; none of its new geometric or computer-assisted algebraicity assertions is assumed here. All arithmetic in this note is recomputed for alpha at degree 70.

Sources checked 2026-09-15. A separate direct download of [S1] failed in the local environment; its full web PDF and rendered normalization page were read successfully. No local PDF cache or unperformed independent expert review is claimed.
