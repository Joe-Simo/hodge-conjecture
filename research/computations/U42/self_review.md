# U42 adversarial self-review

Claim reviewed: M_alpha tensor M_alpha is isomorphic to L^4 in characteristic-zero Chow motives with coefficients Q(zeta_70), hence the 24-dimensional simultaneous-orbit block in H^8(X x X,Q) is algebraic. The unsquared target on X is not asserted algebraic.

**Verdict: proved as written using the specified external correspondence theorems.** This is self-review by the same assistant, not formal verification or a fresh expert review. Exact code and a separate Wolfram kernel corroborate the finite identities only.

## Dependency chain

OY Proposition 4.8 + Proposition 4.11 + coordinate symmetries
-> a symmetric Jacobi cocycle valued in the Picard group of actual invertible Chow motives
-> an abelian extension in which that Picard group injects
-> OY Theorem 7.2 evaluates the nine formal multiplication relations as zero
-> the explicit 69-coordinate integer certificate evaluates to M_alpha^2=L^4
-> a nonzero Chow correspondence L^4 -> M_alpha^2
-> the rational simultaneous-orbit projector gives the 24-dimensional rational algebraic block.

The U40 splitting-field theorem, finite-field Tate conjecture, rational Hodge conjecture, numerical-motive conservativity, and U41 obstruction are not dependencies.

## Obligations and resolutions

| Obligation | Verdict | Evidence / limit |
|---|---|---|
| Characteristic zero, not finite-field lifting | Passed | OY Theorem7.2 explicitly uses an arbitrary suitable field; Section4.2 is geometric |
| Nonzero Chow isomorphisms | Passed | Primary proof uses finite covers/projectors and nonzero composite; invertibility gives cancellation |
| Individual Gauss symbols | Passed after explicit construction | They are formal elements of P x Z/70, not falsely assumed individual characteristic-zero Gauss motives |
| Picard group versus Grothendieck group | Passed | P consists of isomorphism classes of tensor-invertible objects; equality means isomorphism |
| Symmetry and cocycle | Passed | Nondegenerate surface factorization, cyclic projective permutations, and dual-curve pairing handle all cases; all 343000 residue triples classified |
| Degenerate curve input | Passed | J(a,-a)=L is a definition, not a use of a nonexistent primitive character |
| Partial sums/admissibility | Passed | Nine DH instances and four target binary steps all satisfy the source hypotheses |
| Minus signs/coefficient twists | Passed | zeta_140 and roots of 2,5,7 in F suffice; basis-field and correspondence-coefficient fields kept distinct |
| Exact certificate | Passed | Eight native tests; independent Wolfram computation returns zero in all 70 bookkeeping coordinates |
| Weight and codimension | Passed | Theta=M_alpha+L, 2Theta=6L gives M_alpha^2=4L; product dimension8, cycle codimension4, cohomological degree8 |
| Rational coefficient descent | Passed | Simultaneous orbit projector rational; coefficient conjugates of K-linear cycles span all its lines; expand in a Q-basis and project |
| Square versus dual pairing | Passed | The orbit is (u alpha,u alpha), not (u alpha,-u alpha); they are different for every unit |
| Square-root extraction | Not proved, explicitly excluded | Rep(C2) sign object refutes the purely tensor-categorical implication; no claim that this is a Hodge counterexample |
| Parity obstruction scope | Passed | Kills 347 admissible multiplication instances and 69 reflection instances, but target evaluates to1; establishes order2 only in the formal relation quotient |
| 'No other relations' overstatement | Avoided | Extra geometric relations can kill the formal order2 element; no nontriviality of the normalized actual motive is asserted |
| Secondary surface-product route | Out of main theorem | Exact Hodge profiles recorded; no algebraic correspondence asserted from equality of profiles |

## Current gap

No morphism L^2 -> M_alpha with nonzero realization has been constructed. The U42 isomorphism has domain L^4 and target M_alpha tensor M_alpha on X x X. Extracting a geometric 'square root' is a separate, unresolved problem; pulling the cycle back along a diagonal or composing its two factors does not supply such a morphism automatically. Continue with additional characteristic-zero geometry, not another even multiple of the same formal certificate.
