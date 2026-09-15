# U18: exact character check for the cube map X_210 -> X_70

Status: verified character-theoretic descent criterion for the unique level-210 lift. This does not prove algebraicity of the lift and does not solve the Hodge conjecture.

Date: 2026-09-14.

## Map

Consider the finite coordinatewise cube map

    pi : X_210^4 -> X_70^4,
    [x_0:...:x_5] |-> [x_0^3:...:x_5^3].

The deck transformations are given before projectivizing by independent cube roots of unity on the coordinates. Modulo the common scalar, the deck group is a quotient of (mu_3)^6 by the diagonal mu_3.

A Fermat eigenspace character beta=(b_0,...,b_5) at level 210 restricts to a deck character determined by b_i mod 3. For the eigenspace to descend nontrivially through pi_* (equivalently to lie in the invariant summand seen from the base), its deck character must be trivial modulo the projective diagonal. In particular, if every b_i is divisible by 3, the condition is satisfied.

## Unique lift

U17 found

    beta=(141,90,24,42,201,132).

Exact Wolfram arithmetic gives

    beta mod 3 = (0,0,0,0,0,0).

Hence V(beta) is deck-invariant for the coordinatewise cube covering.

Dividing the character by 3 in the exponent group gives

    beta/3 = (47,30,8,14,67,44) mod 70,

whereas reducing beta modulo 70 gives the original alpha=(1,20,24,42,61,62). These are different coordinate tuples, so the precise identification of the descended eigenspace requires care with the convention for character pullback under the power map.

The correct functorial rule is: a base character a modulo 70 pulls back along x -> x^3 to the level-210 character 3a modulo 210 (up to the standard quotient by the diagonal character). Therefore a level-210 character descends to a base character only if it lies in the image of multiplication by 3 in the character lattice, and the candidate base character is beta/3 modulo 70.

For our beta this candidate is

    alpha'=(47,30,8,14,67,44),

not the original alpha.

## Consequence

The earlier statement that beta 'lies above alpha because beta reduces to alpha modulo 70' was too weak for geometric descent and is corrected here. Reduction modulo 70 is not the character pullback rule for the cube map.

Thus algebraicity of V(beta) would imply algebraicity of V(alpha'), not automatically V(alpha).

The level-210 lift remains an interesting rational Hodge class, but it does not presently solve the degree-70 target block.

## Next obligation

Search for a rational Hodge character beta at level 210 satisfying the stronger exact pullback relation

    beta == 3 alpha (mod 210)

up to permutation, Galois unit action, and the diagonal-character equivalence appropriate to Fermat primitive cohomology. If no such beta exists, the simple cube-map descent route to V(alpha) is closed.
