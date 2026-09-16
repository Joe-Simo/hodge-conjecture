# U60: coordinate-P3 nonlinear-factor screen on the degree-7 quotients

**Status:** exact factorization screen for surfaces obtained as non-boundary factors of coordinate P3 sections. No target-bearing surface is found. This is not a proof excluding arbitrary nonlinear surfaces and does not solve the Hodge conjecture.

Date: 2026-09-16. Base checkpoint: U59.

## Goal

U59 proves that every linear P2 on the two U25 degree-7 Delsarte quotients is coordinate-boundary supported and hence cannot hit alpha. The next cheapest nonlinear possibility is a surface component inside a coordinate P3: set two ambient coordinates to zero and factor the restricted degree-7 equation. A non-coordinate irreducible factor of degree >=2 defines a nonlinear surface in that P3.

## Exact census

There are 15 coordinate P3 subspaces. Exact rational factorization gives the following nonmonomial factors.

For A2:

1. on coordinates {x0,x1,x4,x5}:

    f2| = x0*x5*(x1^5 + x0^3*x4^2).

   The nonlinear factor has degree 5.

2. on {x0,x3,x4,x5}:

    f2| = x4^2*x5*(x0^4 + x3^2*x5^2).

   The nonlinear factor has degree 4.

3. on {x2,x3,x4,x5}:

    f2| = x3*x4*x5^2*(x2^3 + x3*x4*x5).

   The nonlinear factor has degree 3.

All other nonzero coordinate-P3 restrictions are monomials; several P3s are contained entirely in the singular boundary because the restriction vanishes identically.

For A3:

1. on {x0,x2,x3,x5}:

    f3| = x0*x2*x5*(x3^4 + x0^3*x5).

   The nonlinear factor has degree 4.

2. on {x2,x3,x4,x5}:

    f3| = x2*x3*x4^2*x5*(x2*x4 + x3*x5).

   The nonlinear factor is the quadric x2*x4+x3*x5.

All other nonzero coordinate-P3 restrictions are monomials; again several coordinate P3s lie in the singular boundary.

## Why these do not solve the target

Every surface listed above lies in a coordinate P3, hence at least two ambient coordinates vanish identically on it. Its pullback to the degree-70 Fermat cover is therefore supported on the coordinate boundary. U29's diagonal-character argument applies: alpha has a nontrivial character in every coordinate, so any cycle fixed by a coordinate diagonal factor has zero alpha projection.

Thus even the explicit A3 quadric

    x0=x1=0,
    x2*x4+x3*x5=0

and the cubic/quartic/quintic factors above cannot furnish the target eigenspace.

## Consequence

Combining U59 and U60 eliminates the cheapest low-degree quotient-side constructions:

- all linear planes;
- every nonlinear component obtained by factoring a coordinate-P3 section.

A successful quotient-side surface must therefore meet the dense torus and be nonlinear. The next bounded search should examine non-coordinate P3 sections whose restricted equation has a quadratic or cubic factor, or move directly to low-degree Hilbert-scheme ansatzes.

The computation uses exact polynomial substitution and factorization over Q; no floating-point arithmetic is used. No formal proof assistant or independent expert review is claimed.