# U26: rationality screen for the two degree-7 Delsarte quotients

Status: two published sufficient rationality criteria fail for these candidates. This does not prove nonrationality and does not solve the Hodge conjecture.

Date: 2026-09-14.

## Why rationality would matter

If a smooth projective resolution of one quotient were rational, the rational Hodge conjecture in codimension two would follow by birational invariance together with the known conjecture in lower dimensions for blow-up centers. Since U25 shows the quotient's unique primitive rational Hodge orbit is alpha, rationality would close the target block.

## Esser criterion 1: determinant equals weighted degree

For an invertible Delsarte polynomial in a well-formed weighted projective space, Esser's Theorem 3.2 gives rationality when the weighted degree equals the determinant of the exponent matrix (in the theorem's normalized setup).

Our quotients are ordinary degree-7 hypersurfaces in P^5, with exponent determinants

    |det A2|=980,
    |det A3|=490.

Therefore the determinant=degree sufficient criterion does not apply.

## Esser criterion 2: projection/quadric-bundle condition

Esser's Theorem 3.3 gives another sufficient condition: after choosing a nonempty block of variables, every monomial must have total degree 1 or 2 in that block, and at least one monomial must have block-degree 1 (plus weight well-formedness conditions, automatic here in ordinary projective space).

Exact exhaustive testing over every nonempty proper subset of the six variables finds no qualifying subset for either A2 or A3.

Thus this rationality criterion also does not apply.

## Consequence

Neither of these modern sufficient criteria proves the degree-7 quotients rational. This is only a negative screen; it is not evidence of irrationality.

The quotient route therefore remains open, but it has not yet reduced the target to a known rational/uniruled fourfold class.

## Source

Louis Esser, `Rational weighted projective hypersurfaces`, Section 3: Theorem 3.2 (invertible Delsarte determinant criterion) and Theorem 3.3 (projection/degree-1-or-2 block criterion), checked 2026-09-14.

## Next route

Audit the singular locus of A2 and A3. If the quotient's primitive degree-four cohomology is entirely contributed by resolution strata of dimension at most two, it would be algebraic; if a nontrivial intersection-cohomology primitive piece survives, the quotient has merely repackaged the original problem.
