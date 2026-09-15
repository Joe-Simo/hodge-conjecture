# U45 source/application and adversarial self-review

Date:2026-09-15. Base:bfdb70edaae96b5ec0aaef8782ab3baffd448826.
Primary verdict: **proved as written within the stated formal seed calculus**, with a finite certificate supplying the bounded profile identity. Review performed by the same assistant. No formal kernel, fresh mathematical reviewer, or independent expert verified the argument.

## Source status

- Markman2502.03415v2, Theorem1.5.1: read the exact polarized Weil-sixfold, imaginary-quadratic, discriminant-minus-one statement and the introduction's construction; Corollary1.6.1 and its reduction to fourfolds were read. The entire sheaf/deformation proof was not independently re-proved. Used as motivation only; no candidate is certified algebraic here by a guessed discriminant.
- Markman2509.23403v2: read Abstract, Theorem1.2, and distinctions between proved dimension4/split6 cases and higher-dimensional semiregularity questions. The dimension<=5 statement is source-reported. Header/manuscript dates differ as recorded in U45. No attempt to resolve the version anomaly by assumption.
- Gao--Ullmo, DOI10.1017/S1474748025101291, publisher HTML online2025-09-19: Section2.1 defines induced/primitive CM pairs and the simple-factor criterion. Theorem3.1 and its proof establish Hodge-balance of coefficient-Galois translates, including nonsimple CM abelian varieties. The proof uses disjoint coordinate basis terms, so cancellation cannot hide a non-Hodge orbit component. Its applicability is only to our explicitly embedded CM-profile palette, not any abelian variety one might name.
- Otsubo--Yamazaki2402.06072v3: re-read Proposition4.11(ii) and Theorem7.2 in full HTML, including nontriviality and roots-of-unity conditions. No finite-characteristic-only assertion was promoted to a characteristic-zero correspondence. U45's core negative theorem is formal and does not require an additional motivic identity.
- Kahnmath/0606424 Conjecture2: revisited as a candidate route, not used as a theorem. Neither an invertible-motive conjecture nor additive torsion-motive theorem extracts the unknown normalized motive from its square.
- CMI official Hodge page was revisited; no new complete solution used in this attempt.

Primary URLs are in U45. All sources were read online in HTML; no licensed PDF or private manuscript was cached/uploaded. The mathematical proof and checkers, not source copies, are delivered. No global novelty search or claim is made. Consensus quota had been exhausted earlier; primary web sources were used instead.

## Dependency graph

U44 definitions and proved dual functional -> J_aug killed by psi.
Direct 1,152-triple certificate -> psi is a sum of five profile differences on the small palette.
Constant Hodge profile -> each of the five differences cancels in every integer word.
These two results + target psi1 + exact lifted square certificate -> exact order2 in the enlarged formal quotient.

CM-field/profile dictionary and Pohlmann -> a restricted geometric interpretation of the granted seed list, not a converse algebraicity claim.

## Obligations checked

- **Passed:** m420, nonzero residues, repetitions, sorted enumeration, both possible ordinary sums, all96 units, and all447 orbits.
- **Passed:** exact orbit-stabilizer count; g is half the profile orbit, not half the raw tuple's character orbit or its conductor's Euler phi by default.
- **Passed:** (3.1) for every1,152 small triple, not only one representative or a few determinant cases.
- **Passed:** an integer word with constant profile c has total multiplicity2c. This validates the normalization -3c ell even with negative multiplicities.
- **Passed:** both Hodge-profile convention choices lead to the same mod2 difference identity and balance test.
- **Passed:** all419 reflections and8,317 multiplication rows, all lifted target unit conjugates, and each coordinate of the square certificate.
- **Passed:** zero result cannot be ascribed to a empty population; small population has1,152 triples and a genus1 benchmark. Dropping unit11 fails on(7,35,378).
- **Passed:** all g<=8 is a finite definition; no assertion of a theorem at arbitrary Fermat levels was appended. The enlargement combines the new result with the previous one *at420*.
- **Passed:** explicit12-dimensional profile fails the formula; a four-factor Hodge word has odd psi and equals the target modulo three reflections. It is not asserted independently algebraic.
- **Passed:** the CM subfield is fixed by the entire profile stabilizer; primitivity follows from its maximality. It is not inferred that arbitrary CM factors have conductor dividing420.
- **Passed with scope restriction:** Markman inputs motivate the list; granting more Hodge words makes the negative test stronger without using an unproved eightfold Hodge conjecture.
- **Out of scope:** arbitrary sums/morphisms/retracts in the actual Chow category, arbitrary geometric correspondences, and non-Fermat profiles. The formal group can have relations killed by geometry which are not in J_new.
- **Not achieved:** a nonzero realized L^2 -> N, target-bearing surface on X, or full Hodge solution.

## Execution correction

The first standalone checker rejected the expected ordered boundary dimensions(12,2,3,12); direct calculation yields(12,3,2,12). The two middle entries in the exploratory handoff were transposed. The checker expectation and manuscript were corrected, not the computation. The original failed log is retained, and Wolfram separately confirms the corrected order.

## Next actionable obligation

Do not increase the tensor length inside the small-palette word calculus: its obstruction is proved for every length. Investigate whether an independently algebraic relation involving one of the explicit dimension12 CM types, or a surface-supported correspondence outside the word calculus, produces the required unsquared map. Re-labelling the boundary word as algebraic would assume the missing result; its odd parity is not a counterexample to Hodge.
