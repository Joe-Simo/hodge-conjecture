# U09: maximal elementary coordinate quotient attached to the degree-70 orbit

Status: verified structural reduction for one Hodge eigenspace only. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## Character stabilizer data

For

    alpha=(1,20,24,42,61,62) mod 70,

set g_i=gcd(alpha_i,70). Exact arithmetic gives

    g=(1,10,2,14,1,2).

The alpha-eigenspace is invariant under multiplying x_i by any g_i-th root of unity in coordinate i. Quotienting by these elementary stabilizer factors corresponds to the monomial substitutions

    y_i=x_i^{g_i}.

The Fermat equation

    sum x_i^70=0

therefore maps to the weighted Brieskorn-Pham hypersurface

    Y: y_0^70 + y_1^7 + y_2^35 + y_3^5 + y_4^70 + y_5^35 = 0

in weighted projective space

    P(1,10,2,14,1,2),

where every monomial has weighted degree 70.

The descended character is

    alpha'=(1,2,12,3,61,31),

with respective local exponents

    (70,7,35,5,70,35).

Each alpha'_i is coprime to its corresponding local exponent, so this elementary coordinate quotient removes all coordinatewise stabilizer divisibility available from gcd(alpha_i,70).

The normalized age/Hodge sum is unchanged:

    1/70 + 2/7 + 12/35 + 3/5 + 61/70 + 31/35 = 3.

Thus the middle Hodge type is preserved under the character bookkeeping.

## Relation to the degree-35 Fermat fourfold

Because four entries of alpha are even, a smaller intermediate quotient is

    Y_2: x_0^70+x_4^70+y_1^35+y_2^35+y_3^35+y_5^35=0

in P(1,1,2,2,2,2).

Squaring x_0 and x_4 gives a finite map from Y_2 to the ordinary degree-35 Fermat fourfold. However the target eigenspace is anti-invariant under both remaining sign changes because alpha_0=1 and alpha_4=61 are odd. Therefore this eigenspace is not in the pullback of ordinary cohomology from X_35^4.

Equivalently, projection to the invariant part under either of those deck involutions annihilates the target eigenspace. Hence the known Hodge conjecture for degree-35 Fermat fourfolds cannot by itself certify this degree-70 class through this quotient.

## Consequence

The orbit can be transferred to a smaller weighted quotient, but not reduced to a known ordinary Fermat class by elementary finite pullback/pushforward. A useful next route is to exploit the weighted quotient's branched-cover geometry or search for a weighted Delsarte correspondence whose relevant eigenspace is known algebraic.

This is a structural simplification, not a proof of algebraicity.