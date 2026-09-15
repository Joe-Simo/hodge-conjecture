# U43 source record and adversarial self-review

Date checked: 2026-09-15. Reviewer: the same assistant that derived U43. No fresh expert, formal kernel, or separate AI reviewer was used. Wolfram is a separately executed arithmetic check, not independent mathematical review.

## Source questions and scope

1. Do the multiplication and reflection identities used in U42/U43 exist as characteristic-zero **Chow** isomorphisms?
2. Does a known invertible-motive classification let one cancel the remaining tensor square without a Hodge-type hypothesis?

The authorized local U42 proof, checker, and source record were inspected first. No project-local copy of the original papers was present. Source statements were read directly as HTML; no PDF, OCR, or newly cached paper was used.

**[OY]** Noriyuki Otsubo and Takao Yamazaki, *Motivic Gauss and Jacobi sums*, https://arxiv.org/html/2402.06072v3 . Locators: Section4.2; Props4.7,4.8,4.11 including (4.8); Section7.2, Theorem7.2 and proof. The served header says v3 / 02 Mar2025, but its body says Date: August24,2026. These differing observed labels are retained; no explanation for the metadata mismatch is assumed. The mathematical statements at these locators were inspected as served.

Dictionary: source d=70, base field kappa=C, coefficient field Lambda=K=Q(zeta70). Its hypersurface dimension is n-1; n=5 gives our fourfold after an algebraic sign scaling. Its twist Lambda(1) is our Lefschetz L. The nontriviality condition is a_i !=0 and sum(a_i)!=0. Theorem7.2's diagonal coefficient n is removed only after adjoining a70th root of n (automatic overC); n=2,5,7 suffices here. Its proof constructs nonzero algebraic correspondences; no use is made of a Frobenius-to-characteristic-zero lifting principle. Each partial multiple used by U43, including every unit transport, was checked.

**[K]** Bruno Kahn, *Motivic zeta functions of motives*, arXiv:math/0606424, https://arxiv.org/html/math/0606424 . Locators: Section4, Conjecture2 and Proposition2. The asserted description of all rational invertible motives in terms of Lefschetz and quadratic Artin motives is a conjecture in this source, and its derivation uses Hodge/Tate-type hypotheses. It is not an input to the positive U43 theorem. Nilpotence lifts an existing homological isomorphism there; it does not create the missing morphism.

A bounded search used terminology 'Chow motives Picard torsion algebraically closed', 'invertible motives square abelian', and 'Artin motives tensor torsion Kahn'. It did not verify a specialized theorem trivializing this T. Papers on motives whose identity is killed by an integer concern additive torsion, not invertible objects whose tensor power is the unit, and were not substituted. No global novelty or negative literature-completeness claim is made.

**Software:** SymPy1.14.0 official DomainMatrix and normal-forms documentation was checked: https://docs.sympy.org/latest/modules/polys/domainmatrix.html . The optional discovery script first imported the Matrix-interface Smith function while supplying a DomainMatrix; it failed before an output claim. The import was corrected to sympy.polys.matrices.normalforms, and exact decomposition, unimodularity, integral solution and agreement with the preserved discovery JSON all passed. The standalone proof checker needs no SymPy.

## Dependency graph

OY characteristic-zero Jacobi correspondences
 -> U42 Picard-group cocycle and square certificate
 -> U43 integer difference t_3-t_1
 -> coefficient transport under <3,-1>
 -> all24 motives isomorphic, all576 mixed tensors Lefschetz
 -> rational product-cycle span
 -> faithful endomorphism algebra Mat24(Q)
 -> exact rational rank-one Chow summand N and N^2=L^4.

No U35 toric construction, arithmetic splitting-field inference, Hodge conjecture, Tate conjecture, or global conservativity assertion enters this chain.

## Obligations

- **Passed:** original X smooth/projective, dim4; product dim8; target degrees/codimensions4/2 and8/4 distinct.
- **Passed:** integral certificate all70 coordinates, including ell and duplicate e35 reflection.
- **Passed:** all used multiplication characters and intermediate partial multiples nonzero.
- **Passed:** unit3 has order12, negative coset supplies the other12; no unjustified unit/permutation equivalence.
- **Passed:** coefficient-field automorphisms act on correspondences, not invented automorphisms of X.
- **Passed:** U42 cocycle zero/partial-zero cases and actual motive invertibility rechecked; eight inherited tests rerun.
- **Passed:** full576 block distinguished from24 matched squares and from all Hodge classes of the product.
- **Passed:** rational descent is of coefficients, not of fields of definition.
- **Passed:** End(Wcal)_K is a matrix algebra and realization is injective because its simple factors are invertible; no phantom-endomorphism assumption is hidden.
- **Passed:** rational matrix idempotents lifted through the proved algebra isomorphism; equalities hold in Chow, not only in Betti.
- **Passed:** N^2 descends by nonzero one-dimensional rational Hom spaces and a nonzero rational composite; a general descent theorem for arbitrary isomorphisms is not assumed.
- **Failed proposed shortcut:** square-trivial T does not formally imply a nonzero realized map1->T; the representation-theoretic control refutes that inference only.
- **Failed proposed extraction:** diagonal yields degree8, ambient contraction is zero; a nonambient seed would already solve the remaining problem.
- **Not addressed:** explicit equations/composed matrices for the new correspondences, an algebraic surface with nonzero W projection, or the full Hodge conjecture.
- **Unavailable:** ruff and mypy modules; syntax compilation and all executed tests passed, but these are not replacements for lint/static type checking.

**Verdict:** U43's restricted theorem is proved as written from the identified inputs, on this self-review. The assertion that the original target is algebraic remains incomplete with the exact missing morphism L^2->N (nonzero realization). No global solution status is warranted.
