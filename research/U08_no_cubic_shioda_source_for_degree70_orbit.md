# U08: no ordinary cubic Shioda source for the degree-70 orbit

Status: verified finite obstruction for one construction ansatz only. This does not solve the Hodge conjecture and does not prove the degree-70 orbit non-algebraic.

Date: 2026-09-14.

## Target

Let

    alpha=(1,20,24,42,61,62) mod 70

be the degree-70 Fermat-fourfold Hodge character from U06-U07.

Favero-Kelly prove the unresolved degree-33 orbit by a Shioda map from the Fermat cover to a cubic fourfold whose Hodge classes are algebraic. The natural question is whether the same architecture can close alpha.

For an ordinary Delsarte cubic in P^5, let A be its 6x6 exponent matrix. Each row of A is a nonnegative integer vector of total degree 3. If the degree-70 Fermat fourfold maps to this cubic by a Shioda monomial map and a cubic Hodge character gamma pulls back to alpha, then

    A^T alpha = 70 gamma.

For a primitive middle (2,2) character on a cubic fourfold, every coordinate of gamma is either 1 or 2 and sum gamma_i=9.

Thus every column c of A must satisfy

    alpha dot c = 70 or 140,

with each coordinate of c in {0,1,2,3}.

## Exact enumeration

Enumerate all 4^6=4096 possible column vectors c in {0,1,2,3}^6.

Exact integer arithmetic gives:

- exactly one vector with alpha dot c=70, namely

      c=(2,1,2,0,0,0);

- no vector with alpha dot c=140.

Therefore no 6x6 matrix A can satisfy the required column equations with gamma_i in {1,2}. In particular there is no invertible Delsarte cubic exponent matrix giving a Shioda map whose pullback contains this degree-70 eigenspace.

This obstruction is independent of smoothness of the cubic: the character equation already fails before geometry is considered.

## Level lifts do not repair the cubic ansatz

Suppose one first lifts alpha from level 70 to level 70k by the coordinatewise power map. The lifted character is k alpha. A Shioda cover of degree 70k to the same cubic would require

    A^T(k alpha)=(70k) gamma,

which cancels to the same condition

    A^T alpha=70 gamma.

Hence passing to any scalar level multiple of 70 cannot produce an ordinary cubic Shioda source for this orbit.

## Consequence

Favero-Kelly's degree-33 cubic-source mechanism does not transfer directly to the degree-70 orbit. Any successful Shioda/Delsarte construction must use a non-cubic source, a weighted source, a different correspondence, or a genuinely non-Shioda matrix factorization.

The computation is exhaustive only for this ordinary cubic-source ansatz; it is not evidence of non-algebraicity.