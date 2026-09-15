# U31: minimal multi-monomial character relations beyond paired cycles

Status: exact finite character-lattice search. This does not construct an algebraic cycle and does not solve the Hodge conjecture.

Date: 2026-09-14.

## Motivation

U30 eliminated surfaces on the degree-7 quotients defined by pairing the six Delsarte monomials, because their pullbacks are unions of the classical paired linear cycles on X_70. A genuinely new quotient-side cycle must therefore use relations involving at least three defining monomials.

## Exact search

Let

    alpha=(1,20,24,42,61,62) mod 70.

Search primitive integer relation vectors r=(r0,...,r5) with:

    sum r_i = 0,
    alpha dot r == 0 mod 70,

and small coefficients. The first condition makes a Laurent monomial relation homogeneous on the torus; the second makes its character compatible with the target/deck arithmetic. This is only a character-lattice filter, not a geometric existence theorem.

For coefficients in [-3,3], 128 primitive relations occur with support at least three. Their support distribution is:

    support 3: 2
    support 4: 32
    support 5: 36
    support 6: 58.

Expanding the support-3 search to coefficients [-5,5] yields, up to sign, exactly two primitive minimal relations:

    rA=(0,-1,3,0,-2,0),
    rB=(0,-4,1,3,0,0).

They satisfy

    -20 + 3*24 - 2*61 = -70,

and

    -4*20 + 24 + 3*42 = 70,

respectively.

Thus the smallest genuinely non-paired target-compatible monomial relations involve the coordinate triples {1,2,4} and {1,2,3} (zero-based indexing in the vectors above).

## Geometric interpretation to test

On a Delsarte quotient with defining monomials M_i, these suggest torus equations of the form

    M_2^3 = lambda M_1 M_4^2

and

    M_2 M_3^3 = mu M_1^4,

with nonzero constants lambda,mu (indices matching rA,rB after moving negative powers to the other side).

Unlike pair equations M_i+M_j=0, their pullbacks through the Fermat cover are not immediately unions of paired linear P^2 cycles. They therefore form the first low-complexity quotient-side ansatz not already killed by U30.

## Caveat

A target-compatible lattice relation does not imply that intersecting two such equations gives a surface whose cohomology has nonzero alpha projection. The next step must:

1. choose two independent minimal relations;
2. pull them back explicitly to X_70 using AB=70 I;
3. analyze dimension/components on the dense torus;
4. compute the stabilizer character of an irreducible component;
5. reject the construction if alpha is nontrivial on that stabilizer.

This is now the cheapest concrete non-paired cycle search.
