# U50: infinitesimal Hodge locus of the degree-70 target and independent literature convergence

**Status:** exact infinitesimal calculation plus scoped literature checkpoint. This does not construct an algebraic cycle and does not solve the Hodge conjecture.

Date: 2026-09-15. Base: U49 on `main`.

## Target

For the Fermat fourfold

    X = {x0^70+...+x5^70=0} in P^5

keep

    alpha=(1,20,24,42,61,62).

Its Griffiths-Jacobian monomial is

    P_alpha = x1^19 x2^23 x3^41 x4^60 x5^61,

with exponent vector

    p=(0,19,23,41,60,61)

and total degree 204=3*70-6, as required for primitive H^(2,2).

## Infinitesimal Hodge-locus map

The Fermat Jacobian ring is

    R = C[x0,...,x5]/(x0^69,...,x5^69).

The tangent space to degree-70 hypersurface deformations is R_70. For a primitive (2,2) residue represented by P_alpha, the infinitesimal Hodge condition is the kernel of multiplication

    mu_P : R_70 -> R_274,
    Q |-> Q P_alpha.

Because P_alpha is a monomial, distinct standard monomials Q have distinct products. A degree-70 standard monomial Q=x^q survives multiplication exactly when

    q_i+p_i <= 68

for all i. Hence

    q_i <= (68,49,45,27,8,7).

Inclusion-exclusion gives the exact counts

    dim R_70 = 17,259,354,
    rank(mu_P) = 2,521,854,
    dim ker(mu_P) = 14,737,500.

A separate Wolfram calculation reproduces all three numbers exactly.

Therefore this target is very far from infinitesimally rigid: its first-order Hodge locus has tangent dimension 14,737,500 and codimension 2,521,854 in the degree-70 deformation space.

This does not obstruct semiregularity. It only rules out any strategy that hoped the target Hodge class was isolated/rigid in moduli.

## Independent literature convergence

A web literature check on 2026-09-15 found Mohammad F. Islam, *A Proof of the Hodge Conjecture Derived from One Semiregular Witness Axiom: A Conditional Proof, the Deletion Test of Its Clauses, and the Open Fermat Orbit at Degree Seventy Outside Aoki's Lattice*, Zenodo DOI 10.5281/zenodo.22701510, version 1.1, published 2026-09-11.

Its public abstract reports an exhaustive census of 47,695 Galois orbits for Fermat fourfold degrees 3<=m<=100 and states that after joins, curve pairs, pair descents, Aoki standard cycles and level changes, the sole remaining orbit after an additional Aoki-lattice closure is exactly

    (1,20,24,42,61,62) at m=70.

This is independent external convergence on the same stress-test orbit selected by this project. The paper does **not** claim to construct its algebraic cycle. Instead it gives a conditional reduction to the existence of a semiregular witness. Its abstract explicitly says whether the needed witness exists for this orbit remains open.

The exact PDF theorem/application has not been fully audited here; only the public Zenodo metadata/abstract and the classical Buchweitz-Flenner semiregularity literature were checked. Therefore no theorem from that preprint is imported as a proved dependency in this project.

## Research consequence

1. Do not spend further effort on rigidity of alpha: the exact tangent calculation rejects it decisively.
2. The project's repeated failure of classical Fermat constructions is consistent with an independent 2026 census, rather than evidence of a missed elementary pair/join/Aoki witness.
3. The semiregular-witness direction is now a legitimate distinct route, but it requires an actual lci surface or coherent sheaf whose Chern character has nonzero alpha projection and whose semiregularity map is injective. Merely restating that requirement is not progress.
4. Continue prioritizing constructions outside the exhausted formal relation subgroup: genuinely coupled sheaves/matrix factorizations or mixed-surface correspondences.

## Exact arithmetic record

For bounded-sum counting with six variables, inclusion-exclusion uses

    count(T;b_i) = sum_{S subset {0,...,5}} (-1)^|S|
                   binomial(T-sum_{i in S}(b_i+1)+5,5),

with terms having negative upper residual omitted.

Applied to b_i=68 gives 17,259,354. Applied to b=(68,49,45,27,8,7) gives 2,521,854.

No numerical approximation is used.
