# U33: constructive homogeneous lifts of the target character

Status: exact lattice observation that simplifies the U32 search criterion. This does not construct a cycle and does not solve the Hodge conjecture.

Date: 2026-09-14.

## U32 criterion

A relation-defined torus cycle can have nonzero alpha projection only if its relation lattice L satisfies

    alpha in L + <1> mod 70,

where 1=(1,1,1,1,1,1), and every integral relation vector used for a homogeneous Laurent equation has coordinate sum zero.

## Diagonal shift restriction

Since sum(alpha)=210, if

    alpha == r + c*1 mod 70

with sum(r)=0 over the integers, summing coordinates modulo 70 gives

    210 - 6c == 0 mod 70.

The only c modulo 70 satisfying this are

    c=0 or c=35.

Thus only two projective diagonal shifts need ever be considered.

## Explicit homogeneous lifts

For c=0, an exact sum-zero integral lift of alpha is

    r0=(1,20,24,-28,-9,-8).

It satisfies

    sum(r0)=0,
    r0 == alpha mod 70.

For c=35, an exact sum-zero lift of alpha-35*1 is

    r35=(-34,-15,-11,7,26,27),

with

    sum(r35)=0,
    r35 == alpha-35*1 mod 70.

These were selected by exact finite minimization of the infinity norm among nearby coordinate lifts.

## Consequence

The stabilizer condition itself is not hard to satisfy: a relation lattice containing r0 (or r35) automatically passes the alpha-triviality test. The real obstruction is geometric complexity. The minimal direct lift r0 already involves all six coordinates and exponents up to 28 in absolute value.

Its Laurent equation can be written on the dense torus as

    z0 z1^20 z2^24 = lambda z3^28 z4^9 z5^8.

This equation is homogeneous because both sides have total exponent 45.

A codimension-3 torus surface could be obtained by adjoining two independent homogeneous relations r1,r2. Since r0 itself carries the target character, the full stabilizer of any lattice containing r0 is automatically contained in ker(alpha) projectively.

## New constructive route

Rather than enumerate arbitrary triples of small relations, fix r0 and search for two very small homogeneous relations r1,r2 such that:

1. rank_Z{r0,r1,r2}=3;
2. the three Laurent equations, together with the Fermat hypersurface, define a nonempty two-dimensional subvariety after projective closure;
3. the closure is not supported on the coordinate boundary;
4. at least one irreducible component is not merely a classical paired cycle;
5. its alpha-period / Favero-Kelly coefficient is nonzero.

The simplest choices for r1,r2 should be used to parameterize the torus defined by the lattice, reducing the Fermat equation to a lower-dimensional Laurent polynomial. This converts the next problem into finding a tractable toric surface whose defining lattice already has the correct target character by construction.
