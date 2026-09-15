# U20: level-lift route reassessment after correcting the character map

Status: research-program checkpoint. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## What changed

U19 identifies the actual pullback under the coordinatewise k-th power map X_{70k}->X_70 as beta_k=k alpha. This immediately explains two facts uniformly:

1. rational Hodge type is preserved for every k;
2. pair and zero-sum-triple decomposability are preserved exactly, so no pure scaling level lift can create the missing elementary decomposition.

Thus the arbitrary-lift discovery at level 210 from U17 is not on the pullback line of alpha and should not drive the main route.

## Uniform obstruction

For any subset I of coordinates,

    sum_{i in I} (k a_i) == 0 mod 70k

if and only if

    sum_{i in I} a_i == 0 mod 70.

Hence every construction criterion expressed solely through vanishing sums of fixed coordinate subsets is invariant under pure level scaling. This includes complementary-pair and two-zero-sum-triple tests.

Therefore no search over k can improve alpha with respect to those criteria.

## Consequence for research allocation

Stop brute-force searches over pure multiples 70k unless the upstairs construction uses genuinely new geometry not encoded by the same coordinate-subset congruences.

The active high-information routes are now:

A. Non-coordinate Delsarte/Shioda maps: search exponent matrices that mix coordinates and map a source fourfold with known algebraic Hodge lattice into X_70 or vice versa.

B. Direct higher-rank nonseparable matrix factorization at level 70: use Favero-Kelly's trace criterion and target the monomial x1^19 x2^23 x3^41 x4^60 x5^61.

C. Normal-function boundary detection for arbitrary primitive fourfold classes (U03-U04): broader but currently blocked by the need to manufacture a detecting singularity without assuming a dual algebraic class.

Route A has the cheapest next discriminating computation because an exponent-matrix candidate can be rejected by integer linear algebra before any geometry. Route B remains the strongest direct construction route if no useful Delsarte source exists.

## Next bounded attempt

Generalize U08's cubic-source search to small Delsarte degrees d=4,5,6 with invertible nonnegative 6x6 exponent matrices whose row sums are d and whose character pullback relation can hit alpha after an allowed level multiplier. Search first at the column-vector arithmetic level; only candidates passing that filter should be tested for invertibility, quasismoothness and known Hodge algebraicity of the source.

A finite failure at d<=6 will be recorded only as a bounded obstruction, not as evidence against the Hodge conjecture.
