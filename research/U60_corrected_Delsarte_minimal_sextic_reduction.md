# U60: corrected Delsarte search — no degree 2–5 source, first exact source is sextic

**Status:** the finite degree-2-through-6 exponent-matrix classification below is exact, and the displayed sextic's character/Hodge census is exact. The result is a new reduction, not an algebraic-cycle construction and not a proof of the Hodge conjecture.

Date: 2026-09-16. Base: U55–U59.

## 1. Correction of the old search contract

Let

    alpha=(1,20,24,42,61,62) mod 70.

For an ordinary homogeneous Delsarte fourfold of degree d in P^5, let A be its 6x6 exponent matrix, with rows the six monomials. Thus A has nonnegative integer entries, is invertible over Q, and

    A * 1 = d * 1.

If m_A is the minimal Fermat covering level, then B=m_A A^{-1} is integral. To compare with the degree-70 target, pass to any common level M divisible by both 70 and m_A. The pullback of alpha to X_M is

    beta=(M/70) alpha.

The exact quotient-character condition is

    A^T beta == 0 mod M,

which is equivalent to

    A^T alpha == 0 mod 70.                              (1.1)

This condition is independent of the chosen common level. Earlier U21 imposed an additional balancing condition on columns; that was useful as a coarse filter but was not the full search. U60 removes that extra condition.

Writing c_j for the columns of A, condition (1.1) says

    alpha dot c_j == 0 mod 70

for each j. Row homogeneity says exactly

    c_1+...+c_6=(d,d,d,d,d,d).

So the exhaustive search is finite: enumerate the nonzero c in {0,...,d}^6 with alpha.c divisible by 70, choose six distinct columns summing to d*1, and require nonzero determinant.

## 2. Exact degree census

A deterministic depth-first exact-cover search gives

| d | admissible nonzero columns | invertible six-column solution |
|---|---:|---|
| 2 | 12 | none |
| 3 | 59 | none |
| 4 | 230 | none |
| 5 | 663 | none |
| 6 | 1716 | yes |

The recorded search visits respectively

    10, 157, 2036, 26344, 11

nodes before proving failure or finding the first witness. All determinant arithmetic is exact over Q.

Therefore **there is no ordinary homogeneous Delsarte source of degree 2, 3, 4 or 5 carrying the degree-70 target through the exact Shioda quotient condition. Degree 6 is the first possible degree.**

## 3. A clean sextic with a unique rational Hodge orbit

A particularly useful degree-6 witness is

    A =
    [3 1 0 2 0 0
     3 0 2 1 0 0
     0 1 2 2 1 0
     1 0 0 0 0 5
     3 1 2 0 0 0
     1 2 0 0 3 0].

Its rows sum to 6 and

    det(A)=420,

    A^T alpha=(350,210,210,70,210,210),

so (1.1) holds. The inverse-denominator lcm is

    m_A=210,

and

    B=210 A^{-1}=
    [ 20   50  -45   0   -5   15
      50 -190   45   0  145  -15
     -55   20   45   0   40  -15
      50   20   45   0  -65  -15
     -40  110  -15   0  -95   75
      -4  -10    9  42    1   -3].

The corresponding sextic is

    Y_6 :
      y0^3 y1 y3^2
    + y0^3 y2^2 y3
    + y1 y2^2 y3^2 y4
    + y0 y5^5
    + y0^3 y1 y2^2
    + y0 y1^2 y4^3 = 0.

Because A*1=6*1, any integral Fermat cover matrix m A^{-1} satisfies

    (m A^{-1})*1=(m/6)*1,

so 6 divides every Fermat covering level m. To compare with degree 70, a common level is therefore divisible by lcm(6,70)=210. The displayed m_A=210 is **minimal possible** for any sextic source in this route.

At level 210 the actual pullback target is

    3 alpha=(3,60,72,126,183,186).

It lies in the invariant character subgroup Im(B^T mod 210).

## 4. Complete invariant Hodge census of Y_6

Exact subgroup generation gives

    |Im(B^T mod 210)| = 420.

Among these, exactly 48 characters are primitive projective characters (all six coordinates nonzero and total sum 0 mod 210). Their least-positive-residue sums are

    420 : 4 characters,
    630 : 40 characters,
    840 : 4 characters.

Thus the complex primitive invariant spectrum has 4 lines of type (3,1), 40 of type (2,2), and 4 of type (1,3); there is no invariant (4,0) or (0,4) line.

A rational Hodge block requires residue sum 630 for every unit conjugate modulo 210. Exactly 24 primitive characters satisfy this condition, and they form **one** unit/Galois orbit of size 24. That orbit contains 3 alpha.

Hence the sextic quotient isolates the original obstruction exactly:

> the unique primitive rational Hodge orbit of Y_6 is the pullback orbit of the degree-70 target.

Proving the rational Hodge conjecture for a resolution of this one sextic quotient would therefore prove algebraicity of the degree-70 block.

## 5. Why the sextic is not an immediate rationality shortcut

The modern Delsarte rationality screens used in U26 do not close this candidate.

1. **determinant=degree criterion.** Any target-carrying A has A^T alpha=0 modulo 5 and modulo 7. If det(A) were prime to 5 or 7, A^T would be invertible modulo that prime and would force alpha=0 there, impossible. Hence det(A) is divisible by 5 or 7. In particular |det A| cannot equal 6.

2. **degree-1/2 block criterion.** For d=6, exhaustively require a nonempty variable block whose six row-degrees all lie in {1,2}, with at least one 1. In column language its selected columns must sum componentwise to a vector in {1,2}^6 containing a 1. Among the 1716 admissible columns, only 12 are coordinatewise <=2, and the only possible selected sum is the single column (1,1,1,1,1,1). No five-column complement summing to (5,...,5) makes an invertible exact matrix. Therefore no degree-6 exact target matrix satisfies this rationality criterion.

This is a route obstruction, not a proof that Y_6 is nonrational.

## 6. Research consequence

The exact low-degree Delsarte frontier is now corrected:

- degrees 2–5: impossible under the true quotient-character condition;
- degree 6: possible, with optimal common cover level 210 and an explicit quotient whose only rational primitive Hodge orbit is the target;
- the previously studied degree-7 quotients are no longer minimal.

The next high-information questions are geometric: determine whether Y_6 is rational/unirational, whether its singular resolution forces the unique Hodge orbit to be algebraic, or construct one nonboundary surface on Y_6 with nonzero target projection. The sextic's sparse quadratic/elliptic presentations are useful for that search but do not themselves prove algebraicity.

## 7. Reproducibility

Exact checker:

    research/computations/U60/verify_u60.py

It uses exact integer/Fraction arithmetic for the degree census, the cover matrix, the complete invariant-character subgroup and all unit conjugates. No floating-point arithmetic is used. A separate Wolfram calculation independently reproduced the sextic cover level, subgroup size 420, primitive count 48, Hodge distribution 4/40/4, and unique 24-element rational target orbit.

The proof is self-reviewed, not formally verified or independently expert-reviewed.
