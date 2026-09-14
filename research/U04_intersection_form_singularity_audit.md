# U04: audit of forcing a normal-function singularity from intersection nondegeneracy

Status: failed direct forcing lemma, with the precise circular step identified. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## 1. Proposed lemma under test

Let X be a smooth projective complex fourfold, L very ample, and let

    0 != zeta in H^4(X,Q) cap H^{2,2}(X)

be primitive. U03 reduced the normal-function route to finding some sufficiently positive singular hypersurface section X_p such that the boundary singularity/restriction associated with zeta is nonzero.

A tempting idea is:

    nondegeneracy of the Hodge-Riemann/intersection pairing
        => some vanishing-cycle or singular-hypersurface pairing detects zeta.

This unit audits that implication.

## 2. What nondegeneracy really gives

Poincare duality and the Hodge-Riemann relations give a nondegenerate pairing on the relevant rational Hodge classes. Hence for nonzero zeta there exists another rational Hodge class alpha with

    integral_X alpha cup zeta != 0.

This step is unconditional.

But alpha is only known to be a Hodge class. It is not known to be algebraic.

## 3. The exact step in the known conditional proof

BFNP, Section 6, prove under the Hodge conjecture that a nonzero primitive Hodge class has nonzero restriction to a sufficiently positive hypersurface. Their argument explicitly does the following:

1. Choose a Hodge class alpha with alpha cup zeta != 0 using the perfect Hodge pairing.
2. Invoke the Hodge conjecture to write alpha as a rational linear combination of algebraic cycle classes [Z_i].
3. Since alpha cup zeta != 0, at least one Z_i has nonzero pairing/restriction with zeta.
4. Choose a sufficiently positive hypersurface containing that algebraic subvariety Z_i; then zeta restricts nontrivially to that hypersurface.
5. Translate the nonzero restriction into the required boundary singularity via the perverse/normal-function machinery.

Therefore the geometric hypersurface is obtained only after alpha has been replaced by an actual algebraic cycle.

## 4. Why a purely cohomological substitute is insufficient

Knowing alpha abstractly in H^4(X,Q) gives no subvariety Z whose containment can be imposed as a linear condition on |L^m|. A cohomology class cannot simply be said to lie inside a hypersurface.

Consequently, the following inference is invalid:

    alpha cup zeta != 0
        => there exists a singular/high-degree hypersurface D with zeta|_D != 0.

The known proof of this implication goes through an algebraic representative of alpha. Producing such a representative for arbitrary alpha is precisely a Hodge-conjecture instance.

## 5. Relation to the active fourfold target

For a fourfold, alpha and zeta are both codimension-2 Hodge classes. Thus trying to solve zeta by first selecting a dual alpha does not lower codimension or dimension. It merely replaces one unknown codimension-2 algebraicity problem by another.

This is why the intersection form alone cannot close the normal-function route.

## 6. What would constitute genuinely new progress

A successful replacement for the circular step would need a theorem of one of these forms:

A. Cohomological localization theorem:
   for every nonzero primitive rational (2,2)-class zeta, construct a controlled singular divisor D with zeta|_D != 0 directly from zeta, without first representing a dual Hodge class algebraically.

B. Vanishing-cycle spanning theorem with arithmetic control:
   prove that the boundary singularity functionals arising from algebraic Lefschetz degenerations span the full dual of the primitive rational Hodge subspace in a way that forces one nonzero functional on every zeta.

C. Independent correspondence theorem:
   construct an algebraic correspondence whose image contains a dual detector alpha for each zeta from a source where algebraicity is already known.

Any such theorem must be audited to ensure it does not hide the Hodge conjecture in a support/coniveau or correspondence assumption.

## 7. Result of this attempt

The direct 'intersection nondegeneracy forces a normal-function singularity' lemma is not proved and the standard proof is circular for our purpose. The earliest unsupported implication is exactly the passage from a dual Hodge class alpha to geometric support by algebraic cycles.

The normal-function route remains viable only if we can construct boundary detection without that algebraic-anchor step.
