# U29: coordinate-boundary cycles cannot contribute to the target alpha eigenspace

Status: exact representation-theoretic obstruction. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## Setup

On the degree-70 Fermat fourfold

    X_70 = {z0^70+...+z5^70=0} subset P^5,

the diagonal group acts by independently scaling coordinates by 70th roots of unity (modulo the scalar diagonal). The target primitive character is

    alpha=(1,20,24,42,61,62),

and every coordinate alpha_j is nonzero mod 70.

U28 shows that the singular loci of the two degree-7 Delsarte quotients lie entirely in the coordinate boundary.

## Lemma

Let Z be an algebraic cycle on X_70 whose support is contained in the coordinate hyperplane

    H_j = {z_j=0} intersect X_70.

Then the cohomology class [Z] has zero projection onto V(alpha).

### Proof

Let g_j(lambda) be the diagonal automorphism that multiplies z_j by lambda in mu_70 and fixes the other coordinates.

Every point of H_j is fixed pointwise by g_j(lambda), because z_j=0 there. Hence every cycle supported on H_j is fixed as a cycle, so its cohomology class lies in the eigenvalue-1 subspace for this mu_70 factor.

On V(alpha), the same element acts by

    lambda^(alpha_j).

Since alpha_j is nonzero mod 70, choose lambda with lambda^(alpha_j) != 1. Thus V(alpha) has no invariant vector for the full j-th coordinate factor. Therefore an invariant boundary-supported class cannot have a V(alpha) component.

The same argument applies to any cycle supported in a union of coordinate boundary strata: decompose it into irreducible components, each contained in at least one H_j, and apply the corresponding coordinate action.

## Consequence for the quotient-resolution route

The obvious algebraic surfaces found inside the singular loci in U28 cannot directly certify alpha after pulling back to X_70 if their pullbacks remain supported on coordinate boundary strata. Likewise, exceptional cycles arising purely over coordinate-boundary strata are not promising alpha-certificates for the same character reason.

This sharpens the quotient route: because alpha has all six coordinates nonzero, any successful algebraic cycle representing its eigenspace must have a component that meets the dense torus where all coordinates are nonzero. Boundary geometry alone cannot generate the target character.

## Scope caveat

A full resolution correspondence may contain components not literally supported in a single coordinate hyperplane upstairs. Therefore this lemma does not by itself prove that every exceptional class on an arbitrary resolution has zero alpha projection. It does rigorously eliminate all certificates whose pullback support is contained in the Fermat coordinate boundary.

## Research implication

The singular planes of U28 are useful for understanding the quotient but are not themselves the missing cycle. The next constructive search should target a torus-meeting algebraic surface, either:

1. directly on X_70 through a nonseparable matrix factorization; or
2. on one of the degree-7 quotients, with a pullback that meets the dense Fermat torus.
