# U46 source/application audit and adversarial self-review

Date: 2026-09-15. Base: `8fff2a01be0453fc613c0776239085816c155fdd`.
Review type: same-assistant mathematical self-review. The second computation is a stateless Wolfram arithmetic implementation, not an independent expert or a formal proof of the geometry.

## Scope and dependency chain

The target remains the rational Hodge conjecture for all smooth projective complex varieties. This work concerns only the degree-70 block alpha=(1,20,24,42,61,62), and does not construct an original target-bearing cycle.

U45's boundary character word -> beta and gamma -> exact quotient function fields -> degree-ten canonical models -> ADE resolutions and complete Hodge data -> algebraic self-product classes and exact mixed-product transport.

The original abstract surface profiles appeared already in U42 Section7. The present new content is the explicit small canonical models, their singularities/Picard ranks, the complete product calculation, and the precise remaining correspondence. No global novelty claim is made.

## Primary sources actually used

1. Shioda--Katsura, *On Fermat varieties*, Tohoku Math. J.31(1979),97-115, DOI10.2748/tmj/1178229881. The classical nonzero-character decomposition and grade rule are inherited from the pinned U42 record. Current-run J-STAGE requests, including the `/_pdf/-char/en` alternative, failed; a DOI redirect also failed. No new direct PDF verification is claimed. The product map needed here is derived in full in U46 Section7, with an accessible modern source independently checked in item2. This is an access limit, not evidence against the formula.
2. Otsubo--Yamazaki, *Motivic Gauss and Jacobi sums*, arXiv:2402.06072v3, version header2March2025. The served HTML body has a later regenerated date,24August2026; that is not treated as a new arXiv version. Sections3 and4.2, especially Propositions4.9--4.11, the equivariance formula(4.6), and Corollary4.13 were read directly at https://arxiv.org/html/2402.06072v3 . The convention is homological Chow motives, opposite to common cohomological notation; U46 instead writes actual equal-dimension pullback/pushforward maps on rational H^4. Source characteristic-zero applicability and exceptional terms are checked, not inferred from the finite-field introduction. No Tate/Beilinson conjecture in the final section is used.
3. Franciosi--Pardini--Rollenske, *Gorenstein stable surfaces with K_X^2=1 and p_g>0*, arXiv:1511.03238, Theorem3.3(i), directly read at https://arxiv.org/html/1511.03238 . It identifies the degree-ten canonical format in weights(1,1,2,5). Our particular models satisfy the needed normality/ADE/adjunction hypotheses by direct calculations. No converse from weights alone is used. Corollary3.5 is about moduli rationality and has been removed from the draft citation because it is not needed.
4. Gallardo--Pearlstein--Schaffler--Zhang, *Unimodal singularities and boundary divisors in the KSBA moduli of a class of Horikawa surfaces*, arXiv:2209.08877v2, Section2.1; Math.Nachr.297(2024),595-628, DOI10.1002/mana.202300019. Read at https://arxiv.org/html/2209.08877v2 . Terminology and canonical-model context only; no Hodge-conjecture assertion imported.
5. Huybrechts, *Lectures on K3 surfaces*, author-hosted draft, Chapter1, formula(2.7), printedp13/PDFindex12. Rendered page inspected using the web PDF screenshot tool. It supplies b2(K3)=22 and the Hodge diamond; this excludes the proposed rank24 simple Hodge summands as factors of actual K3 H^2. https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf . Author-hosted draft is not redistributed.
6. Buskin, *Every rational Hodge isometry between two K3 surfaces is algebraic*, arXiv:1510.02852v3, version header21December2016, Theorem1.1, directly read at https://arxiv.org/html/1510.02852v3 . This applies to actual projective K3 surfaces and isometries. It does not apply here. Publication: J.reine angew.Math.755(2019),127-150, DOI10.1515/crelle-2017-0027.

The finite-dimensional Hodge facts also use the standard Lefschetz(1,1) theorem, semisimplicity of polarizable rational Hodge structures, surface blowup formula, adjunction, and Noether formula. These standard inputs are distinct from any claimed solution of a Hodge conjecture. No complete external article/PDF is included in the evidence package.

## Obligation matrix and adversarial checks

| Obligation | Verdict | Decisive check or limit |
|---|---|---|
| Actual admissible surfaces | Passed | Irreducible normal degree10 models; ADE minimal resolutions are smooth projective. |
| Correct quotient group and orientation | Passed | Explicit rational invariant functions and reconstruction of roots prove degrees980*5 and700*7; character generators checked modulo70. |
| Projective singularity coverage | Passed | T=1 and X=1 plus the remaining T=X=0 locus; neither ambient orbifold point lies on either model. |
| Surface invariants | Passed | Canonical degree1, two canonical sections, H1 injection from Fermat cover, Noether formula. |
| Complete transcendental list | Passed | All69 multiples examined; only conductors70,10 or70,14; residual group invariance eliminates rational(1,1) in each orbit. |
| Picard completeness | Passed | Independent divisor Gram determinants5 and7 attain b2 minus the transcendental lower bound. No integral NS basis claimed. |
| Simplicity and K3 exclusion | Passed | Unique h20 plus no rational(1,1), semisimplicity, then rank24>22; excludes sums of K3 H^2, not tensor products or all K3-derived constructions. |
| Hodge isomorphism vs isometry | Passed after explicit distinction | Embedding conjugation matches full profiles. No isometry or algebraicity inferred. |
| All rational product Hodge classes | Passed | Exhaust all nonzero character pairs and all24 units, not just type at one embedding; include NS and extremal Kunneth terms. |
| Self-product algebraicity | Passed | Graphs of cyclic powers span the complete transcendental Hodge endomorphism algebra; remaining classes are points/divisor products. |
| Mixed-product equivalence | Passed | Explicit degree70 map, blowup exceptional terms excluded by nontrivial last-coordinate characters, quotient maps inverted on the image by degree. Codimension stays2. |
| Arbitrary known product projector gives original cycle | Rejected | No mixed correspondence is supplied by self-product endomorphisms. |
| New mixed cycle | Not addressed successfully | Still requires a nonzero realized R5-to-R7 correspondence. |
| Complete rational Hodge conjecture | Not achieved | Neither the original W nor the universal domain is settled. |

## Discovery corrections preserved in this audit

An initial double-octic presentation for the second quotient had a (2,3,7)-type singularity at infinity, so its naive smooth-double-cover invariants were not used. The final degree-ten model has an A1 point, verified in both implementations. This discarded presentation is not an additional geometric candidate.

The change from U45's CM dimension language to surface H^2 ranks is explicit:12 denotes a curve CM-profile dimension, while24 here is the rational rank of the resulting surface Hodge summand. No numerical equality is treated as a comparison theorem.

The quintic discriminant recorded for S7 is not used alone to prove non-isotriviality, non-isogeny, or a missing correspondence. The direct isotrivial normalization of the first pencil is just constructive data.

## Arithmetic evidence and limitations

Ten new tests pass with exact Python/SymPy arithmetic. Eight U42, ten U43 and seven U45 tests were rerun from preserved code:25 inherited tests pass. The inherited tests are context checks, not dependencies establishing the new geometric assertions. Syntax compilation passes. Native `python -m ruff check ...` and `python -m mypy ...` return exit1 because their modules are not installed. No lint/static-type-check success is claimed.

Wolfram15.0.1 independently recomputed full character populations, product pairs, both invariant substitutions, residual kernels, all singularity chart ideals, Gram determinants and the quintic discriminant. Output JSON normalizes temporary symbol names and notation only. This corroborates finite arithmetic, not the external geometric theorems. Existing local input hashes remain unchanged; missing inherited checkers were restored without overwriting existing files.

## Executable next question

Work on the specific mixed product of the two displayed resolutions, using the genus-two pencils or another genuinely coupled correspondence. Success requires one algebraic codimension-two cycle with nonzero projection to the identified24-dimensional mixed block. An arbitrary complete intersection or a graph on just one surface cannot meet that criterion. No extra charge, public publication, or researcher contact was authorized or performed.
