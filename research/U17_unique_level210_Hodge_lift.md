# U17: unique coordinatewise level-210 rational Hodge lift

Status: verified finite arithmetic discovery only. This does not prove algebraicity and does not solve the Hodge conjecture.

Date: 2026-09-14.

## Search

Following U16, test elementary coordinatewise lifts from level 70 to small multiples 70k. For each k, each coordinate has k lifts

    beta_i = alpha_i + 70 j_i,  j_i in {0,...,k-1},

and beta is required to satisfy the rational middle-Hodge condition at level 70k for every unit u:

    sum_i <u beta_i>_(70k) = 3*(70k).

Exact Wolfram enumeration for k=2,...,6 gives:

    k=2, level 140: 64 lifts,     0 rational Hodge lifts
    k=3, level 210: 729 lifts,    1 rational Hodge lift
    k=4, level 280: 4096 lifts,   0 rational Hodge lifts
    k=5, level 350: 15625 lifts,  0 rational Hodge lifts
    k=6, level 420: 46656 lifts,  0 rational Hodge lifts

The unique level-210 lift is

    beta=(141,90,24,42,201,132).

Its coordinate sum is 630=3*210, and exact testing over every unit modulo 210 confirms that every Galois conjugate retains least-positive-residue sum 630. Thus beta is a genuine rational (2,2) Fermat-fourfold Hodge character at level 210.

## Decomposability test

All 10 partitions into two triples were checked. No triple has sum 0 modulo 210. Hence beta does not close by the elementary two-zero-sum-triples criterion.

The closest symmetric partition is

    {141,42,132} / {90,24,201},

with sums 315/315, again half-integral relative to 210 rather than 210 or 420.

## Why this matters

Unlike the failed level-140 experiment, level 210 produces an actual rational Hodge block lying above alpha under reduction modulo 70. This is a new structural lead.

However, algebraicity of beta is not established. Also, even if beta is algebraic, descent of its cycle class along the coordinatewise cube map

    X_210^4 -> X_70^4,

must be checked carefully. At the character level beta reduces to alpha modulo 70, but a pushforward/pullback calculation with the diagonal deck group is required to prove that a nonzero beta-cycle projects to the alpha eigenspace rather than vanishing.

## Next obligations

1. Test beta against all known algebraicity criteria available at level 210: pair, triple, Aoki/standard-cycle criteria where definitions are available, and lower-level factorization through divisors of 210.
2. Derive the exact character behavior of the finite cube map X_210 -> X_70 and prove whether algebraicity of V(beta) would imply algebraicity of V(alpha).
3. Do not infer the Hodge conjecture for alpha from the existence of beta alone.
