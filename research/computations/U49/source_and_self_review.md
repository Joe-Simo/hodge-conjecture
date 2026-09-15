# U49 source/application audit and adversarial self-review

Date: 2026-09-15. Base: cd4ba6bd38ce1b86d41ced84322b6b1b021282d9.
Review is by the same assistant. Different computer algebra systems do not constitute independent expert review.

## Dependency record

- Formal coefficients and reflection certificate: new direct derivations in U49 Sections 3--6; exact integer checker corroborates selected degrees only.
- Full automorphism group of F_m, m>=4: Hayashi, Arabian J. Math.10(2021), Definition2.1/Theorem2.2, DOI10.1007/s40065-021-00321-5. Publisher HTML read directly. It attributes the standard theorem to Harui and Tzermias. The free abelian subgroup classification is independently derived in U49 Section2.
- Curve character projectors, invertible Jacobi motives and reflection/cocycle interpretation: Otsubo--Yamazaki, arXiv:2402.06072v3, Section4.2, especially Propositions4.7,4.8,4.11; HTML statements and proofs rechecked. The complete balanced-word dictionary is the preserved U42 Section3. Its standard-library checker was restored without replacing an existing file and all8 tests rerun.
- Target remains nonzero in the formal method: preserved U44 all-level parity theorem; U49 adds only words already in the reflection subgroup, so no extension of that theorem's hypotheses is needed.
- New source family: Patel--Zhang, arXiv:2506.13729v2 (23 May2026), Theorems1.1--1.2. The tested object is the full top determinant of each nontrivial character eigenspace for an etale abelian cover. No ramified case or subdeterminant is granted by this reference.

Primary locators:
https://link.springer.com/article/10.1007/s40065-021-00321-5
https://arxiv.org/html/2402.06072v3
https://arxiv.org/html/2506.13729v2
https://arxiv.org/pdf/2506.13729v2

## Source discrepancies, kept separate from U49's proof

Two displayed auxiliary statements of the Patel--Zhang preprint should not be imported verbatim. They occur in both the HTML and the visually inspected PDF pages4 and11.

1. With the printed definition Delta_d(x)=d[x], AJ_d Delta_d(x)=d[x-P]. Thus the induced map on the integral H_1 lattice is multiplication by d, not an isomorphism for d>1 and positive genus. Using the embedding x -> x+(d-1)P instead gives the usual Abel--Jacobi map and the intended identity on H_1. This is an explicit correction of a map, not a silent redefinition of the source.
2. The printed subgroup G0={(g,-g,0,...)} is contained in the kernel of the sum G^r -> G, and cannot map isomorphically to that quotient. The coordinate subgroup {(g,0,...)} does map isomorphically. More robustly, a tensor character (chi_1,...,chi_r) trivial on the full sum kernel has all chi_i equal. A nontrivial quotient character therefore forces all r factors into the matching H^1 character space, since H^0 and H^2 carry trivial characters; the geometric symmetric projector includes the odd-degree signs and yields the usual exterior power.

These elementary checks do not refute the main algebraicity theorem. The general theorem's full proof is not certified here. Crucially the U49 redundancy theorem remains valid even if every listed determinant is merely granted as an additional algebraic input: its word is already an integral reflection combination. For this Fermat subclass the existing U42 correspondence dictionary independently justifies the balanced-word conclusion. We do not extrapolate it to all generalized Prym varieties.

An attempted publisher fetch of the 2016 alternative proof of the Fermat automorphism theorem timed out; the exact full-group statement was instead read in Hayashi's primary research article. No unavailable text is cited as inspected. The first/last of four PDF screenshot requests returned cache errors; the two relevant pages4 and11 were successfully inspected. No paper PDF is redistributed in the evidence archive.

## Adversarial checks

Passed: excluded the elliptic cubic; required faithful action; excluded even-order groups via a fixed-line involution; checked every power in the diagonal freeness condition; classified the C3 permutation image and its diagonal centralizer; used projective, not matrix, commutation for C3 x C3; excluded both fixed triple lines only in nontrivial characters; distinguished full determinant from a subdeterminant; recovered the Lefschetz coefficient and the integral self-dual coefficient; separated cohomological degree from codimension; kept scalar coefficient fields separate from fields of definition; did not infer original algebraicity from another tensor identity.

Positive controls: free degree5 cyclic quotient, non-diagonal degree6 quotients, exact cyclic projectors with diagonal coefficient1/3, and the full rank4830 degree210 determinant.
Negative controls: a distinct-eigenvalue generator with a nonfree power; a ramified diagonal action with unbalanced eigenspace; retaining the two sigma-fixed triples gives the wrong rank; asymmetric or odd-rank words fail reflection recovery; the original alpha fails the same recovery and has parity1 at all tested scaled levels.

Limits: the universal result uses the displayed proofs and the stated classical inputs, not a finite sweep; the code does not verify Chow correspondence theorems. Only determinant seeds with classical Fermat upstairs are exhausted. Arbitrary Prym cycles, new transport correspondences, other upstairs curves, ramified covers and selected subdeterminants remain outside scope. No global novelty claim is made.

## Execution deviations

The first Wolfram coefficient call had malformed syntax and returned $Failed. Its corrected self-contained replacement passed. A later projector/ramification call used a destructuring Table iterator unsupported by Wolfram; the ramification part remained unevaluated. The corrected self-contained call, saved as independent_wolfram_projectors.wl, passed completely. Neither failed call is evidence of a mathematical result. Only successful output is serialized in independent_wolfram.json.

All10 new tests and8 inherited U42 tests pass. Syntax compilation passes. Ruff and mypy are absent; their actual failed native invocations and return codes are recorded. No formal-verification, lint or static-type-check success is claimed.
