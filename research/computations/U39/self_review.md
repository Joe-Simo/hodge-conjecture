# U39 adversarial self-review

Primary verdict: **proved as written**, subject to the stated classical external theorems. Reviewer: the same assistant; no fresh-agent, expert, or formal review is claimed. Independent Wolfram output is arithmetic corroboration only.

Target: the normalized Galois character for alpha=(1,20,24,42,61,62) has cyclic image70, a canonical kernel field E, and a specific nonabelian degree35-over-K subfield M. Nonzero target cycle fields contain E. In particular cyclotomic coefficient fields cannot supply such a cycle.

| Obligation | Verdict | Decisive check |
|---|---|---|
| The target is the rational Hodge block, not an arbitrary complex (2,2) vector | Passed | 24 unit conjugates, residue sums210, U38/12th U39 test |
| The uniform identity is not a fit to prime values | Passed | 70-entry integer relation certificate combined with identities valid for all q=1 mod70 |
| DH and reflection signs/nontriviality | Passed | Otsubo Definition2.1, Proposition2.2(iii), Theorem3.10; g=-G; no zero index |
| Jacobi-to-Gauss factor q^3 is correct | Passed | Additive-character orthogonality, plus direct U38 convolution and cubic F7 benchmark |
| Indexed Frobenius values, not unordered point-count eigenvalues | Passed | Character projectors and exact Otsubo–Yamazaki Theorem1.2 with c=-1,n=5 |
| Frobenius orientation | Passed | Dual twisted line evaluated on arithmetic Frobenius; inversion does not change kernels |
| Chebotarev use before knowing finite image | Passed | Continuous character trivial on dense Frobenii; alternatively reduce modulo coefficient-prime powers |
| D is square in K | Passed | Explicit T(x)^2+35=0 modPhi70 and C^2=D |
| Exact image, not only order dividing70 | Passed | U38 independently corroborated eigenvalue zeta70^57 at491 |
| Every nonzero block vector has the same kernel | Passed | All line characters are rho^u with u a unit; no eigenvalue1 outside ker(rho) |
| K(D^(1/70))=K(D^(1/35)) | Passed | delta^35=D; theta=delta^18/C; theta^2=delta |
| Radical R and degree35 | Passed | D^23=R*(-2^21*5^9/7^5)^35; Eisenstein at2, unramified inK |
| Nonabelian overQ, not merely cyclic overK | Passed | Splitting field of x^35-R; complex conjugation inverts order35 rotation |
| Field containment for arbitrary finite L/K, even nonnormal | Passed | G_L fixes nonzero projected class; contained in G_E |
| Finite abelian field not containingK | Passed | Use compositum FK, still abelian/Q |
| Candidate L0 rejected by kernels, not just unequal characters | Passed | All24 unit powers excluded; explicit211/421 contradiction |
| Individual components distinguished from their union | Passed | Corollary applies only to individually field-defined cycles |
| Uniform primitive vanishing or cycle existence overE | Not asserted | No Tate/Hodge converse used |
| Coherent-sheaf/graded-factorization scope | Passed | Chern characters yield rational cycle classes over the same coefficient field |

Remaining mathematical gap to the actual project goal: no algebraic cycle with nonzero target projection has been constructed, even over E or a larger field. The quadratic character eta is nontrivial, but its Kummer radicand remains unidentified. Matching Galois representations would not alone construct a Chow correspondence; a characteristic-zero motivic lift must be proved separately.

Native tooling limits: Ruff and mypy were invoked and are absent from the environment. Python compilation and all12 focused U39 tests pass. Those tests do not constitute a formal verification of the geometric proof.
