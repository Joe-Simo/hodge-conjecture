# U03: normal-function boundary reformulation of the primitive fourfold problem

Status: verified route reformulation only. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## 1. Why this route is different from U02

U02 showed that ordinary variational/semiregularity arguments require an algebraic anchor cycle and therefore cannot by themselves construct a cycle representing an arbitrary primitive Hodge class.

There is, however, a different deformation-theoretic route due to Green-Griffiths and Brosnan-Fang-Nie-Pearlstein (BFNP): associate a normal function to a primitive Hodge class and study its singularities at singular hyperplane sections. BFNP prove that the existence of the required singularities for all primitive Hodge classes is equivalent to the Hodge conjecture.

Primary reference used here:
Patrick Brosnan, Hao Fang, Zhaohu Nie, Gregory Pearlstein, "Singularities of admissible normal functions", Invent. Math. 177 (2009), arXiv:0711.0964. In the arXiv text, Theorem 1.3 / Section 6 establishes the equivalence.

## 2. Specialization to the active fourfold frontier

Let X be a smooth projective complex fourfold, L a very ample line bundle, and

    zeta in H^4(X,Q) cap H^{2,2}(X)

be primitive:

    zeta cup c1(L) = 0.

For a positive integer m, let

    P_m = |L^m|

be the complete linear system and let U_m be the open subset parametrizing smooth hypersurface sections X_p.

The primitive class zeta gives, after the standard construction over U_m, an admissible normal function nu_zeta (equivalently AJ(zeta) in the terminology of BFNP/Green-Griffiths).

The decisive statement is not that nu_zeta vanishes somewhere. It is that for some m the normal function acquires a non-torsion singularity at a boundary point p in P_m corresponding to a singular hypersurface section.

BFNP prove, globally over all smooth projective varieties, that:

    Hodge conjecture
        <=>
    every non-torsion primitive Hodge class has such a singular normal function for some sufficiently positive hypersurface system.

Thus for the fourfold frontier, a valid attack can target the singularity directly, without first postulating a codimension-2 algebraic cycle on X.

## 3. Equivalent restriction formulation used in the proof

BFNP Section 6 records the Thomas/Totaro reduction underlying the normal-function statement. In the relevant middle-dimensional situation, the Hodge conjecture is equivalent to the assertion that every nonzero primitive Hodge class zeta has nonzero restriction to a suitable sufficiently positive singular hypersurface section X_p (one may arrange controlled singularities such as nodes in the Thomas formulation).

The reason this avoids the U01 smooth-hyperplane dead end is important:

- for a smooth hyperplane i:Y->X, algebraicity of i^*zeta on the threefold Y does not recover zeta because i_* i^* zeta = c1(L) cup zeta = 0;
- at a singular boundary fiber, vanishing-cycle/perverse-cohomology data records additional information lost by smooth Gysin pushforward;
- the singularity of the normal function is precisely designed to detect that boundary contribution.

So singular hypersurfaces are not a cosmetic variation: they supply the missing channel through which a primitive class can be detected.

## 4. Exact toy consistency check on P^2 x P^2

For X=P^2 x P^2 with a,b the two hyperplane generators and L corresponding to h=a+b, U01 found

    zeta = a^2 - a b + b^2

as a generator of primitive H^4.

Its self-intersection is

    zeta^2 = 3 a^2 b^2,

so integral_X zeta^2 = 3 != 0.

This confirms that the primitive class is genuinely nonzero even though

    h cup zeta = 0.

In this toy model zeta is already algebraic, so the BFNP theorem predicts that for sufficiently positive powers of L there must exist a boundary hypersurface where the associated normal function has the required singularity. This is a consistency check only, not a new proof of BFNP or a universal construction.

## 5. Earliest open implication for a direct proof attempt

The equivalence theorem does not itself locate the singularity for an arbitrary zeta. The new concrete obligation is:

Given (X,L,zeta) with zeta a nonzero primitive rational (2,2)-class, prove that for some m there exists a boundary point p in |L^m| for which the BFNP singularity class sigma_p(nu_zeta) is non-torsion (equivalently, in the theorem's formulation, the relevant restriction/vanishing-cycle class is nonzero).

This is still equivalent in difficulty to Hodge in full generality, but it has two advantages for research:

1. it replaces the unknown space of all codimension-2 cycles by a geometric degeneration problem in a linear system;
2. the obstruction is localized at singular hypersurfaces and can be attacked using vanishing cycles, Picard-Lefschetz theory, perverse sheaves, and explicit degenerations.

## 6. Current 2026 literature signal

Green and Griffiths published "Singularities of the infinitesimal invariant of normal functions" in 2026 (Atti Accad. Naz. Lincei, DOI 10.4171/RLM/1080). It studies an identification between singularities of a normal function and of its infinitesimal invariant; the abstract explicitly says the formal proof of that new identification will appear separately. This is relevant technique, not a claimed resolution of Hodge.

## 7. Next executable step

Develop a controlled degeneration test for primitive H^4 on fourfolds: choose a Lefschetz pencil/high-degree linear system, write the local Picard-Lefschetz/vanishing-cycle pairing that would force sigma_p(nu_zeta) != 0, and determine whether nondegeneracy of the primitive intersection form can force at least one such boundary pairing without secretly using Hodge.
