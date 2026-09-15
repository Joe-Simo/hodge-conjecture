# U11: exact one/two cancelling-pair zero-triple exhaustion

Status: verified finite combinatorial obstruction only. This does not solve the Hodge conjecture and does not establish non-algebraicity of the degree-70 orbit.

Date: 2026-09-14.

## Target

For the degree-70 Fermat fourfold character

    alpha=(1,20,24,42,61,62) mod 70,

test a stronger decomposability ansatz than U06: adjoin one or two cancelling pairs `(t,-t)` modulo 70 and ask whether the resulting 8- or 10-entry multiset can be partitioned completely into zero-sum triples.

This is motivated by Aoki/Shioda-style constructions in which auxiliary cancelling pairs can permit a higher-dimensional character to decompose into algebraic lower-dimensional pieces. The test below is deliberately narrower than the full Aoki calculus: failure rules out only this exact zero-triple ansatz.

## Exact exhaustive computation

Using Wolfram Language with exact integer arithmetic modulo 70:

1. For every `t=1,...,69`, form

       alpha union {t,70-t}.

   Enumerate all 3-subsets with sum 0 mod 70 and run exact-cover backtracking to test whether all eight entries can be partitioned into triples. Since 8 is not divisible by 3, no complete triple partition is possible; the implementation nevertheless rejects all cases directly.

2. For every unordered pair `1<=s<=t<=69`, form

       alpha union {s,70-s,t,70-t}.

   Enumerate all zero-sum triples and run exact-cover backtracking on all ten indexed entries. Again 10 is not divisible by 3, and exact enumeration returns no witness for all 2415 choices `(s,t)`.

Wolfram output:

    onePairWitnesses -> {}
    twoPairWitnessCount -> 0

## Interpretation and correction of scope

The raw negative result is exact, but the dimension count exposes an important methodological point: merely adjoining one or two cancelling pairs cannot by itself lead to a *complete partition solely into triples*, because the resulting lengths are 8 and 10. Therefore this ansatz is structurally impossible independently of the residue values.

Actual Aoki/two-pair closure criteria can mix blocks of different sizes (for example a standard sextuple plus a Hodge quadruple) rather than requiring every entry to belong to a triple. Consequently this computation must NOT be cited as ruling out Aoki's construction or the recent two-pair criterion in full.

## Next obligation

Implement the genuine mixed-block criterion from its primary theorem: after adjoining two cancelling pairs, test decomposition into the exact standard sextuple plus grade-2 Hodge quadruple required by the source, with all hypotheses translated explicitly. Do not substitute the simpler triple-partition test for that theorem.
