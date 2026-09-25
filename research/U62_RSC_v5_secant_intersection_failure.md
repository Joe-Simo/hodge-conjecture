# U62: The v5 relative-secant proof uses an ambient intersection of the wrong codimension

**Date:** 2026-09-24

**Status:** primary-source audit of a non-peer-reviewed claimed proof. The RSC argument in v5 does not prove the full Hodge conjecture. This does not refute the conjecture.

Primary source: [Bhattacharjee–Bhattacharya, *Relative Secant Cycles and Hodge Classes*, v5](https://www.preprints.org/manuscript/202602.0462/v5). Its landing page marks the version posted 5 August 2026 as not peer-reviewed.

## 1. The secant variety contains the embedded abelian variety

Section 2.8 defines

```text
Sec^n(Y) = closure of the union of the (n−1)-planes spanned by n points of Y.
```

For every point y in Y, choose an n-tuple containing y. Its span contains y, so

```text
Y ⊂ Sec^n(Y),     Sec^n(Y) ∩ Y = Y set-theoretically.
```

This holds for every n >= 2; taking a closure does not remove the original points. In the paper’s setting, dim(A^vee)=2n, so the intersection has codimension zero in A^vee, not codimension n. The expected-dimension formula in §2.8 and §4.1 cannot override the actual containment; the intersection is not proper.

## 2. The structure-sheaf class is not the claimed Weil class

In §4.1, Definition 3 sets F=O_Sigma on the ambient projective space and restricts it to A^vee. Because A^vee is contained in Sigma,

```text
F|Avee=O_Avee,
ch(O_Avee)=1,
ch_n(O_Avee)=0 for n>0.
```

The paper instead treats this restriction as supported on a codimension-n locus and claims ch_n(O_Avee)=[Z_Sigma]≠0. Its nonvanishing proof in Lemma 4 also assumes dim(Avee∩Sigma)=n. Both statements conflict with the set-theoretic containment.

The same invalid class is load-bearing in §4.5: the union of ambient secant varieties is placed in the relative Chow group of the dual abelian scheme as a codimension-$n$ cycle, then Fourier–Mukai transformed into the “universal Weil cycle.” Definition 5 restates the same intersection. Neither is a valid codimension-$n$ cycle under the stated definitions.

## 3. The appendix acknowledges the issue only for n=2

Appendix E.3 states explicitly that

```text
Sec^2(A^vee) ∩ A^vee = A^vee,
```

because every point lies on a limiting secant line. It replaces that construction for $n=2$ with a different object: a degeneracy locus formed from a strict-secant sheaf and a determinant section. This is not the scheme-theoretic intersection from Definition 5, and the appendix gives no corresponding general-$n$ construction. The same containment defect applies to every n >= 3.

## 4. Consequence for the full-proof claim

The manuscript’s stated dependency chain is:

```text
RSC Theorem 4
  → Theorem 5: Hodge conjecture for all abelian varieties
  → Theorem 8: abelian-dominated varieties
  → Theorem 12: primitive coniveau-zero classes via Kuga–Satake
  → Theorem 13: full Hodge conjecture.
```

Theorem 5 reduces arbitrary abelian varieties to Weil classes of unbounded parameter $n$, and Case E uses RSC for Kuga–Satake abelian varieties whose dimension grows exponentially. Since the stated universal Weil cycle is not established for n >= 3, these later conclusions do not follow. The v5 preprint therefore does not prove the general Hodge conjecture.

The appendix’s separate $n=2$ construction points to the known abelian-fourfold case; it does not validate the all-dimensional RSC theorem. The classical divisor case $n=1$ also remains independently valid. No counterexample to the rational Hodge conjecture is produced.

## Jev triage

The Hodge Jev screen assigned this claim viability score 2.99/3 for a fatal flaw. The raw record is `results/evidence/RSC_Hodge_v5_secant_intersection_1790267309.json` and is `HYPOTHESIS_ONLY`; the verdict above rests on the direct source definitions and dimension argument, not on Jev.
