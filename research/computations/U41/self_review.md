# U40–U41 adversarial self-review

Reviewer: the same assistant, not an independent expert or formal proof checker.
Primary verdict: **proved as written for the restricted statements, using the explicitly identified external inputs**.
No conclusion of the full Hodge conjecture or target-block algebraicity follows.

| Obligation | Result | Evidence / exact limit |
|---|---|---|
| U39 versions refer to the same squared character | Passed | U40 (3); remote/local C and D kept distinct |
| Necessary degree-35 fields agree | Passed | U40 (4), gcd(22,35)=1 |
| Missing quadratic factor, not a finite fit | Passed with external theorem | Deligne/Kubert–Lichtenbaum 1.6 plus the displayed formal gamma identity |
| Remote comparison quadratic is not confused with E's quadratic subfield | Passed | s=-tau/7; quotient uses Delta/s; E intersect L0=M |
| Real coefficient and minimal degree | Passed | Conjugation, exact degree-12 resultant, ramification degree lower bounds |
| Diagonal normalization classification | Passed | Uniform descent character and injective Kummer map; no cycle-class surjectivity assumed |
| Proper block coverage | Passed | Odd-block trace or binary degree; finite set-partition check is corroboration |
| Parity vs internal grading | Passed | D odd with degree 35; binary closed paths degree 68 |
| Cones vs retracts | Passed after explicit restriction | Theorem A excludes arbitrary retracts of cones; the 4x4 positive example demonstrates why |
| Univariate End algebra and nilpotent ideal | Passed | Direct kernels/images give (8); a weight bound proves ideal nilpotence |
| Idempotent conjugacy | Passed | u=e e0+(1-e)(1-e0); u=1 modulo a nilpotent ideal; inverse exists in endomorphism cohomology |
| Homotopy vs strict polynomial invertibility | Passed | Only invertibility in cohomology is needed for the retract isomorphism; no polynomial invertibility claim |
| Global interpretation of local character | External theorem checked | Favero–Kelly 3.6 is a primary preprint; Polishchuk–Vaintrob 3.2.3 is published; neither has been formally verified here |
| Scope under coefficient twisting | Passed | Nonzero diagonal rescaling does not change the monomial Jacobian ideal or character support |
| Code coverage | Passed in recorded domains | 7 new arithmetic tests, 8 new MF tests, 22 inherited tests; no 69^6 brute-force claim |
| Fresh expert or formal audit | Not performed | Wolfram is separate arithmetic corroboration only |
| Native lint / type checking | Blocked | ruff and mypy absent; attempted local installation failed at network DNS; syntax compilation passes |

Decisive counterexample to an overbroad claim: the 4x4 quadratic tensor has total trace 0 and complementary projector traces +2i and -2i.

Open mathematical obligation: construct a nonambient cycle, a genuinely coupled graded factorization, or a target-bearing retract of a nontrivial cone. Neither passing arithmetic normalization nor a zero total trace decides that obligation.
