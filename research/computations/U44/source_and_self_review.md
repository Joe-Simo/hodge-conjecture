# U44 source and self-review record

Base revision: f7d6581d58f28b4faffee0366b0907b1a3a20223. Local U42 and U43 proof files were read in full; both standalone checkers were rerun. Earlier unrelated claims are not certified by this run.

## External sources actually inspected

- Otsubo-Yamazaki, arXiv:2402.06072v3, https://arxiv.org/html/2402.06072v3 : Section4.2 and Theorem7.2, including the characteristic-zero statement and its proof using covers. The claim here is a no-go result for the explicitly defined formal calculus; no assertion that this calculus captures every Chow correspondence is made.
- G. da Silva Jr., Experimental Results2(2021), e22, DOI10.1017/exp.2021.14, full publisher HTML: Section2, Lefschetz(1,1), Fermat character criterion and correspondence decomposition. This supplies the terminology and familiar divisor interpretation; the negative certificate also holds if those seeds are simply granted.
- Jumagulov, arXiv:2608.18134v1, full HTML: odd-degree theorem statement, examples at105, AppendicesA,B,D. The even-degree appendix explicitly separates computed remaining cases from its proved odd result. Its main theorem, closure implementation, and ancillary records are not assumed in U44; all105 sextuples are granted as seeds instead. Served header/version date discrepancies were not resolved by assumption.
- Kahn, arXiv:math/0606424, full HTML: Conjecture2 remains a conjectural general classification, not a way to infer N=L^2 from N^2=L^4.
- Current CMI Hodge page was rechecked: https://www.claymath.org/millennium/hodge-conjecture/ . It lists the problem unsolved; no submission or award assertion follows.
- Limited search for universal ordinary distribution sign-cohomology located Kubert1979, DOI10.24033/bsmf.1892, and Anderson math/9710225. Only bibliographic/abstract discovery was used; their theorems are not proof dependencies. No global novelty claim is made.

No PDF was fetched for this run; no new copyrighted full source copy was added to Git. Existing project/conversation prompt and proof texts supplied the research contract. Consensus's previously observed quota block was not treated as a mathematical obstruction or silently bypassed with an invented result.

## Dependency closure and primary verdict

**Verdict: proved as written for the specified formal calculus**, with a proved all-level cyclic-group argument and a finite exhaustive certificate at420. The actual target motive's triviality and the full Hodge conjecture remain unresolved.

1. Formal R/D definitions -> cyclic subgroup parity lemma: passed by a separate derivation using C_m=C_d direct sum C_(m/d); oddness and unitary-divisor hypotheses both tested against failing examples.
2. Level embeddings -> order preservation: passed by m k / gcd(m k,k a)=m/gcd(m,a).
3. Target nonzero, doubled target zero: passed by prime-primary parity and explicit re-addition of U42's square certificate. This is exact order2 in a formal quotient, not in the unknown actual Picard kernel.
4. Augmented420 generators -> psi=0: all8317 multiplication generators,23307 sorted Hodge quadruples, all curve Hodge pair profiles, and27690 degree105 sextuples checked. Entry repetition, arbitrary coordinate permutations and all unit embeddings are covered.
5. Finite-to-unbounded word length: passed; linearity of one F2 functional kills every integer combination of the enumerated generators. No depth cutoff is used in the conclusion.
6. All-level result with extra geometric seeds: NOT CLAIMED. Only the R/D result is all-level. The enlarged result is only at420 with exactly the listed seed populations.
7. Arbitrary cycle exclusion or completeness of motivic operations: NOT CLAIMED. There is no proved injection of the formal quotient into the actual Chow Picard group; sums/retracts and new geometric relations can escape the calculus.
8. Independent review: arithmetic only. Wolfram's direct quadruple loops differ from Python profile matching. The mathematical proof was reviewed by the same assistant, not a fresh expert or formal kernel.

## Executed attempts and rejected inferences

The raw F2 discovery span first used small divisor seeds, then all surface seeds, then all divisors n and all admissible a. It left a nonzero target. A long nullspace mask was extracted but is not used as the final certificate: the simpler order-in-{7,21} test replaced it and is rechecked directly. Known28 and105 example words were also tested and had zero certificate value. The full105 census was then performed to avoid relying on a few examples.

The old primary7 functional is explicitly invalid on the known algebraic surface tuple(1,4,18,19) at21. The final420 functional passes that input. This negative control guards against misreporting a formal obstruction as a nonalgebraicity theorem.

One combined Wolfram sextuple/curve call returned HTTP502 with no mathematical output. Its completion is not asserted. A smaller curve-only call succeeded. The full105 census is a single-engine finite result with all accepted tuples checked over all units and small independently generated census benchmarks; the report preserves this limit.

Validation: nine new and18 inherited tests pass; syntax compilation passes. `python -m ruff check ...` and `python -m mypy ...` both fail because those packages are not installed. No successful native lint/static-type checking is claimed. Original input hashes are unchanged.

Next discriminating route: an independently algebraic input with nonzero certificate value and an exact transport, or a correspondence with appropriate support producing a realized map L^2 -> N. Repeating deeper cancellation solely within the tested subgroup cannot help.
