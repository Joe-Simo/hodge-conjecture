# U10: branched-cover anti-invariant obstruction for the degree-70 quotient

Status: verified route audit using the standard double-cover Hodge decomposition. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## Setup

U09 factors the degree-70 character through the intermediate weighted quotient

    Y_2: x_0^70+x_4^70+y_1^35+y_2^35+y_3^35+y_5^35=0

in P(1,1,2,2,2,2).

Squaring x_0 and x_4 gives a finite (Z/2)^2-cover of the ordinary degree-35 Fermat fourfold X_35^4. The target character is odd in x_0 and x_4, hence lies in the (-1,-1) deck-character sector.

A tempting shortcut is to identify that sector with ordinary cohomology of the branch divisors or their intersection, where lower-dimensional Hodge theory would be known. This shortcut is not valid in general.

## Standard double-cover formula

For a smooth double cover pi:Y->X branched along a smooth divisor D with covering line bundle L satisfying L^2=O_X(D), the anti-invariant Hodge summand is described by logarithmic forms:

    H^q(Y,Omega_Y^p)^- = H^q(X, Omega_X^p(log D) tensor L^{-1}).

The invariant summand is the ordinary H^q(X,Omega_X^p).

Thus the anti-invariant part is not, in general, the cohomology of D or a Tate twist of it. It depends on a logarithmic complex and the nontrivial covering line bundle.

Applying this successively to the two sign covers in U09 shows that the (-1,-1) sector carrying the target class is an iterated logarithmic/twisted Hodge piece on X_35^4. There is no formal identification of that sector with ordinary Hodge classes on either branch divisor or their intersection.

## Consequence

The known rational Hodge conjecture for the ordinary degree-35 Fermat fourfold, together with the dimension-three theorem for its branch divisors, does not by itself establish algebraicity of the degree-70 target eigenspace.

A successful cover-theoretic route would need an additional theorem showing algebraicity for the relevant logarithmic/twisted eigenspace or an explicit correspondence converting that eigenspace into ordinary algebraic-cycle cohomology. No such theorem has been established in this project.

## Sources

The double-cover eigenspace formula is the standard Esnault-Viehweg description: for a double cover, the anti-invariant differential forms are logarithmic forms twisted by L^{-1}. Modern abelian-cover Hodge theory likewise decomposes cohomology into deck-character eigenspaces rather than reducing nontrivial characters to branch cohomology automatically.
