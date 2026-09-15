# U36: U35 is an irreducible surface family with identically zero primitive class

Status: **proved by the argument below, with exact computational corroboration and self-review**; no formal verification or independent expert review. This is a restricted construction obstruction, not a proof or counterexample to the rational Hodge conjecture.

Date: 2026-09-15. Base: `Joe-Simo/hodge-conjecture@7fea00517efe485776cadc7b482ff3f426b0ecc3`, U35 blob `66828e1b1fdc2a763e86c70cf973168d87673f34`.

The supplied `Hodge_Conjecture_Astra_Research_Prompt.txt` was read in full. Its SHA-256 is `0639b0689036cee1ed7a990147fba250ee3188d5bc3143dc2625e50d4d85bbb3`. Work is confined to the existing Hodge workspace and private Hodge repository.

## 1. Exact result

Work over C. For any integer m >= 1, put

    X_m = {z0^m+z1^m+z2^m+z3^m+z4^m+z5^m=0} in P^5.

For lambda, mu in C*, let T_(lambda,mu) be the **reduced projective closure** of the torus defined by

    z0^2 z1^2 z5 = lambda z2^3 z3 z4,
    z0^3 z3 z5   = mu z2^3 z4^2,

with every coordinate nonzero. Let S_(lambda,mu,m) be the reduced closure of its intersection with X_m in the dense projective torus. Write h for the hyperplane class on X_m.

**Theorem.** S_(lambda,mu,m) is a nonempty irreducible surface for every lambda,mu != 0 and every m >= 1. Its fundamental cycle satisfies

    [S_(lambda,mu,m)] = 12 h^2 in CH^2(X_m).

In particular, for m=70 its degree is 840 and its primitive H^4 class is zero. The projection onto the character alpha=(1,20,24,42,61,62), and onto its whole rational unit orbit, is exactly zero.

This resolves U35's outstanding period question **negatively for this entire family**, not merely for a generic parameter or the sum of unknown components. It says nothing about arbitrary algebraic surfaces on X_70.

## 2. Correct parametrization and dimension

The U35 relations are

    r=(2,2,-3,-1,-1,1), s=(3,0,-3,1,-2,1).

They have sum zero, and the minor in coordinate columns 0 and 4 is -1. Thus they generate a saturated rank-two lattice. The identity

    45r+17s = alpha + 70(2,1,-3,-1,-2,0)

checks the stated stabilizer compatibility. This condition is necessary for a nonzero character projection, not sufficient.

On z5=1, take u=z1, v=z2, w=z3. Dividing the two relations and then substituting back gives an actual isomorphism of tori, not a finite cover:

    (u,v,w) |-> [(lambda^2/mu) v^3 w^3/u^4,
                 u, v, w,
                 (lambda^3/mu^2) v^3 w^5/u^6,
                 1].

The inverse reads off u,v,w. In particular, T has dimension 3, and the restricted Fermat equation is the Laurent polynomial

    F = 1+u^m+v^m+w^m
        + C u^(-4m) v^(3m) w^(3m)
        + D u^(-6m) v^(3m) w^(5m),

where C=(lambda^2/mu)^m and D=(lambda^3/mu^2)^m are nonzero. No parameter has been counted as a coordinate of a fixed surface, and projectivization is not performed a second time after z5=1.

F is not a Laurent monomial and hence not a unit. The Laurent polynomial ring over C is a finitely generated C-algebra, so its proper principal ideal has a maximal ideal corresponding to a point of (C*)^3. Its zero set is nonempty and, once irreducibility is proved, has dimension 2.

A check at lambda=mu=1: take u=v=w=a with a^m=-1. Then the restricted equation is 1+3a^m+2a^(2m)=0, and the corresponding point is [a^2:a:a:a:a^2:1].

## 3. Irreducibility for all parameters, not merely generic ones

Let P be the convex hull of the six exponent points

    p0=(-4,3,3), p1=(1,0,0), p2=(0,1,0),
    p3=(0,0,1), p4=(-6,3,5), p5=(0,0,0).

The Newton polytope of F is mP. All six coefficients are nonzero, and all six points are vertices. Exact supporting-plane checks give these facets, with the inward inequality n.p >= b:

| Facet vertices | n | b |
|---|---|---:|
| 0,1,2 | (-3,-3,-2) | -3 |
| 0,1,3,4 | (-3,-2,-3) | -3 |
| 0,2,5 | (3,0,4) | 0 |
| 0,4,5 | (3,1,3) | 0 |
| 1,2,5 | (0,0,1) | 0 |
| 1,3,5 | (0,1,0) | 0 |
| 3,4,5 | (1,2,0) | 0 |

**There are six triangular facets and one quadrilateral, not eight triangular facets.** A floating convex-hull triangulation would divide the quadrilateral; the proof uses actual facets checked by integer inequalities.

### Elementary face-propagation lemma

Suppose the Newton polytope P_f of a Laurent polynomial f has a triangular facet on which the face polynomial is irreducible. Suppose a connected chain of triangular facets, adjacent along full edges, reaches all vertices of P_f. Then f is irreducible in the Laurent polynomial ring.

Proof. If f=gh, the Newton polytope is Q+R, where Q and R are the Newton polytopes of g and h. For each supporting direction, face polynomials multiply and the corresponding faces add. These facts follow by taking the terms of maximal weight in a product; their product cannot vanish in a domain.

On the initial facet the irreducible face polynomial forces one of the factor face polynomials to be a Laurent monomial. Assume it is g, so the corresponding face of Q is a point q. Its contribution to either adjacent edge is also a point.

A Minkowski summand of a triangle is either a point or a positively homothetic triangle. To see this, an edge direction of a summand must be an edge direction of the sum. A segment would require opposite edge normals, which a triangle does not have. A nonpoint planar summand therefore has the same three edge directions as the triangle and is similar with parallel corresponding edges. In particular, such a summand cannot contribute a point to one of the triangle's edges.

Consequently, on an adjacent triangular facet the Q-face must again be a point, and it is the same q along the common edge. Propagating along the chain makes the Q-contribution to every reached vertex equal to q. Every vertex of Q occurs in the unique decomposition of some vertex of Q+R: expose it by a direction generic also for R. Since all vertices of P_f are reached, Q has only the vertex q. Thus g is a Laurent monomial, a unit. This proves the lemma.

### Applying the lemma

The face at w=0, with vertices 1,2,5, has face polynomial

    1+u^m+v^m.

It is irreducible over C: choose a simple root rho of v^m+1 and apply Eisenstein at the prime v-rho to u^m+(v^m+1) over C[v]. Characteristic zero guarantees the root is simple. Primitivity and Gauss's lemma give irreducibility in C[u,v], and localization and adjoining w^+/-1 preserve it.

The triangular facets can be reached in the order

    125 -> 012 -> 025, then 135, then 045, then 345,

where each new facet shares an edge with a previously reached facet (respectively 12, 02 or 25, 15, 05, and 35 or 45). Their vertices cover 0 through 5. The lemma applies to mP for every positive integer m. Therefore F is irreducible for **every** C,D != 0.

This is not an inference from finite factorization tests, and it does not assume that mP is integrally indecomposable. Indeed mP can split homothetically; the irreducible face polynomial prevents the corresponding polynomial factorization.

## 4. Saturation, degree, and the coordinate boundary

At lambda=mu=1, set f=z0^2 z1^2 z5-z2^3 z3 z4 and g=z0^3 z3 z5-z2^3 z4^2. The projective torus closure has homogeneous ideal

    I_T = (f,g) : (z0 z1 z2 z3 z4 z5)^infinity.

Eliminating t from (f,g,t*product(z_i)-1), independently in SymPy and Wolfram Language, gives this lexicographic Groebner basis:

    z0^3 z3 z5 - z2^3 z4^2,
    z0^2 z1^2 z5 - z2^3 z3 z4,
    z0 z1^4 z5 - z2^3 z3^3,
    z0 z3^2 - z1^2 z4,
    z1^6 z4 z5 - z2^3 z3^5.

The leading monomial exponents, ordered as written, are

    (3,0,0,1,0,1), (2,2,0,0,0,1), (1,4,0,0,0,1),
    (1,0,0,2,0,0), (0,6,0,0,1,1).

Inclusion-exclusion over the 32 subsets of these leading monomials yields

    Hilb(C[z]/I_T,t)
      = (1+2t+3t^2+3t^3+3t^4+t^5-t^6)/(1-t)^4.

Hence deg(T)=1+2+3+3+3+1-1=12. An independent exact volume calculation gives 3!*Vol(P)=12 in the full lattice Z^3 (p1,p2,p3 are its standard basis). Scaling z0 by lambda^2/mu and z4 by lambda^3/mu^2 identifies the general T with T_(1,1), so the degree does not change.

There is also a direct intersection-multiplicity explanation. The two quintics have total intersection degree 25. Their three-dimensional coordinate-boundary components in P^5 are exactly

    {z0=z2=0}, {z0=z4=0}, {z2=z5=0}, {z4=z5=0},

with respective generic multiplicities 6,3,3,1. Each follows by eliminating one of the two local variables: at the first prime the ideal becomes (z0^2,z2^3); at the second it has length 3 after solving linearly for z4; at the third it has length 3 after solving linearly for z5; at the fourth it has length 1. The remaining coefficients are units at the generic points. A one-coordinate zero leaves a monomial from f, so a three-dimensional boundary component must be one of these coordinate pairs. Therefore the residual toric degree is 25-6-3-3-1=12.

**No surface component of T intersect X_m is hidden in the boundary.** In the normalization of the projective toric variety T, boundary divisors correspond to facets of P. On their open torus orbits, the nonzero coordinate monomials are exactly the vertices on the facet. Their exponent differences are distinct characters of that orbit; multiplication by m preserves distinctness because its character lattice is torsion-free. The restriction of the Fermat polynomial is thus a nonzero sum of distinct Laurent monomials with nonzero coefficients, and cannot vanish identically on any boundary divisor. The finite normalization map preserves dimensions, so no two-dimensional boundary component can occur in T intersect X_m. Lower-dimensional boundary strata cannot supply a surface either.

Together with the torus irreducibility argument, this shows that the fundamental intersection cycle has exactly the surface S with multiplicity one. Possible embedded lower-dimensional scheme structure is irrelevant to this fundamental cycle.

## 5. Exact cycle-class calculation

Let i:X_m -> P^5 be the smooth hypersurface inclusion and H the hyperplane class of P^5. By the projective-space Chow formula [S1],

    [T] = 12 H^2 in CH^2(P^5).

T is integral and not contained in X_m. The refined Cartier-divisor pullback [S2-S3] therefore gives its actual intersection cycle on X_m, rather than just its pushforward to P^5:

    [S] = i^![T] = 12 h^2 in CH^2(X_m).

This is stronger than an equality of ambient degrees. No injectivity of the pushforward CH^2(X_m) -> CH^3(P^5) is assumed.

Passing to cohomology gives cl(S)=12h^2. Its primitive component is zero. Since h^2 is invariant under every diagonal Fermat automorphism, its projection onto any nontrivial character, including alpha, is zero. The primitive Chern character of the structure sheaf consequently cannot supply U07's target coefficient.

## 6. Follow-up: a uniform obstruction for genuine torus-coset surfaces

A separate potential repair of U34 would force its two-dimensional torus coset to lie entirely in the Fermat hypersurface, instead of cutting it by one further equation. That repair also admits a uniform classification.

**Proposition.** On X_d^(2k) in P^(2k+1), the closure of a k-dimensional translate of a connected subtorus of the ambient projective torus, contained entirely in X_d^(2k), is a classical paired linear P^k.

Proof. On the coset, write the 2k+2 homogeneous coordinates as nonzero constants times torus characters, after choosing an affine torus chart. Their exponent vectors have affine span of dimension k because the coset has that dimension. In the identically vanishing Fermat sum, group terms with identical exponent vectors. Distinct torus characters are linearly independent, and multiplying their exponents by d does not identify distinct characters. Thus every group has at least two terms. There are at most k+1 groups, but affine span k requires at least k+1 distinct vectors. Hence there are exactly k+1 groups, each of size two. The two coordinates in each group are proportional with constant ratio xi satisfying xi^d=-1. Their closure is contained in the corresponding paired P^k and, being irreducible of dimension k, equals it.

For the present alpha, no pair of coordinates sums to zero modulo 70. Such paired planes therefore have zero alpha projection. This proposition excludes **subtorus cosets contained in X**, not arbitrary toric intersections, arbitrary rational parametrizations, or all algebraic surfaces.

## 7. Audit and executable handoff

Self-review verdict: **proved as written for the nonzero-parameter family in Section 1**. The earlier U35 stabilizer facts survive; its possibility of a useful primitive class is now rejected. No complete Hodge candidate is asserted.

Key checked obligations:

- fixed parameters, dimensions, projective chart, and an actual torus isomorphism;
- saturated lattice and correct target congruence;
- exact facets (including the quadrilateral) and a connected triangular propagation certificate;
- parameter-uniform irreducibility, not just vanishing of the total class of a reducible cycle;
- saturation and boundary components, not the unsaturated quintic complete intersection;
- the class on X via refined pullback, not an unjustified inference from its ambient pushforward;
- uniform theorem versus finite certificate: computations check explicit algebra and facets; Sections 3-5 prove the universal parameter assertion.

Checks:

    python research/computations/U36/verify_u36.py
    python -m py_compile research/computations/U36/verify_u36.py

Eight focused tests pass, including a deliberately reducible triangular-prism example which fails the face-propagation criterion. The exact saturation and degree were independently reproduced using Wolfram Language 15.0.1; the local checker uses Python 3.13 and SymPy 1.14.0. No floating geometry is used in the certificate. Python syntax compilation passes. No Ruff, Mypy, or Pyright executable is installed; no lint or static-type-check success is claimed. No pre-existing Hodge code/test suite was present.

The general conjecture and the algebraicity of the alpha block remain unresolved here. Do not search more lambda,mu values in U35. A subsequent toric-intersection attempt must first evade the irreducible-face propagation criterion and then produce a genuinely nonambient irreducible component; merely passing the diagonal stabilizer test is not enough. The nonseparable matrix-factorization route remains open, with the same explicit nonzero primitive coefficient obligation.

Historical U01-U34 claims are not globally revalidated by this checkpoint.

## Sources and provenance

[S1] The Stacks Project, Lemma 42.36.2, projective space bundle formula (apply over Spec(C)): https://stacks.math.columbia.edu/tag/02TV . HTML statement and proof inspected 2026-09-15.

[S2] The Stacks Project, Definition 42.29.1 and Lemma 42.29.5, Cartier-divisor intersection as a cycle on the divisor: https://stacks.math.columbia.edu/tag/02T7 . HTML statement and proof inspected 2026-09-15.

[S3] The Stacks Project, Lemmas 42.30.2 and 42.30.4, descent through rational equivalence and compatibility with Chern classes: https://stacks.math.columbia.edu/tag/02TK . HTML statement and proof inspected 2026-09-15.

[S4] David Eisenbud and Bernd Sturmfels, *Binomial Ideals*, Duke Math. J. 84 (1996), 1-45, DOI 10.1215/S0012-7094-96-08401-X; primary arXiv record https://arxiv.org/abs/alg-geom/9401001 . Background only; no uninspected specialized theorem from this paper is needed for the explicit saturation or parametrization proof.

The Newton-face propagation proof and the torus-coset classification are written out here. No novelty claim is made. The official CMI page still labels the general problem unsolved as checked on 2026-09-15: https://www.claymath.org/millennium/hodge-conjecture/ .
