# U56: Hermitian lines span the special fiber and produce semiregular line/conic witnesses downstairs

**Status:** the line-span and low-degree semiregularity statements below are proved from the cited extremal-surface incidence theorem plus exact linear algebra. They produce explicit *types* of special-fiber divisor witnesses but do not lift the coupled codimension-two target to characteristic zero. This does not solve the Hodge conjecture.

Date: 2026-09-16.

## 1. The Hermitian cover

Work over an algebraic closure of F_139. Put

    H = X_140 = {x0^140+x1^140+x2^140+x3^140=0} in P^3,
    F = X_70  = {y0^70 +y1^70 +y2^70 +y3^70 =0} in P^3.

Because 140=139+1, H is the Hermitian/extremal surface of degree q+1 with q=139.

There is a finite morphism

    pi:H -> F,   [x0:x1:x2:x3] |-> [x0^2:x1^2:x2^2:x3^2].

It is finite because it is the restriction of the coordinate-square map on P^3. Since pi^*O_F(1)=O_H(2), intersection with the hyperplane classes gives

    deg(pi)*70 = (2H_H)^2 = 4*140,

hence

    deg(pi)=8.                                             (1.1)

## 2. Rank of the full line-intersection matrix on H

Page–Ryan–Smith, *Smooth surfaces with maximally many lines* (Forum Math. Sigma, 2026), prove that an extremal surface of degree d=q+1 contains

    v=d^2(d^2-3d+3)=(q+1)(q^3+1)

lines, and that its lines and star planes form a generalized quadrangle with parameters

    (s,t)=(q,q^2).

They also record that whenever two lines meet, the plane they span is a star plane. Thus two surface lines meet iff the corresponding points in the point graph of this generalized quadrangle are adjacent.

For a generalized quadrangle GQ(s,t), its point graph is strongly regular with

    v=(s+1)(st+1),
    k=s(t+1),
    lambda=s-1,
    mu=t+1.

The adjacency eigenvalues are

    k=s(t+1),
    r=s-1,
    u=-(t+1).

For s=q,t=q^2 their multiplicities are

    mult(r)=q^2(1+q^2),
    mult(u)=q(1-q+q^2),

as follows from 1+mult(r)+mult(u)=v and trace(A)=0.

A line L on a smooth degree-d surface has

    L^2=2-d=1-q=-(q-1).

Distinct intersecting lines have intersection number 1 and skew lines have intersection number 0. Therefore the complete line-intersection Gram matrix is

    G=A-(q-1)I.

Its eigenvalues are

    k-(q-1)   (multiplicity 1),
    0         (multiplicity q^2(1+q^2)),
    -(q^2+q)  (multiplicity q(1-q+q^2)).

Hence

    rank(G)=1+q(1-q+q^2)=1+q-q^2+q^3.                   (2.1)

For a smooth degree d=q+1 surface in P^3,

    b2=d^3-4d^2+6d-2=1+q-q^2+q^3.                      (2.2)

Thus the line classes span a subspace of NS(H)_Q of rank exactly b2(H). Since NS(H)_Q embeds into H^2 and cannot have rank larger than b2, we obtain

    NS(H)_Q = H^2(H,Q_l)(1)

at the level of dimensions, and **the classes of lines span NS(H)_Q**.

For q=139 the exact numbers are

    number of lines = 375,986,800,
    b2(H)            = 2,666,438,
    zero multiplicity in G = 373,320,362,
    negative-eigenvalue multiplicity = 2,666,437.

Independent Wolfram arithmetic reproduced (2.1)-(2.2) symbolically and these numerical values.

## 3. Images of lines span NS(F)_Q

For every divisor class D on F,

    pi_* pi^* D = 8 D.                                   (3.1)

Since pi^*D lies in the rational span of line classes on H, equation (3.1) shows that NS(F)_Q is spanned by the curves pi(L) as L ranges over lines on H.

The restriction pi|_L:P^1->P^3 is given by quadratic forms. Therefore

    deg(pi|_L) * deg(pi(L)) = 2.

As the image is irreducible, pi(L) is either

- a line, with pi|_L of degree 2; or
- a smooth plane conic, with pi|_L birational.

Consequently **NS(F)_Q is spanned by smooth rational curves of degree 1 or 2**.

In characteristic 139 the beta- and gamma-character lines from U46 are algebraic divisor eigenspaces in H^2(F). Hence, because the pi(L)-classes span NS(F)_Q, there exists at least one line/conic C_beta with nonzero beta projection and at least one line/conic C_gamma with nonzero gamma projection. This is an existence statement; explicit equations for the two detecting curves have not yet been selected.

## 4. Every such line/conic is rigid and divisor-semiregular

Let C subset F be a smooth rational curve of degree delta=1 or 2. Since

    K_F=O_F(70-4)=O_F(66),

adjunction gives

    C^2=-2-K_F.C=-2-66 delta.

Thus

    N_{C/F}=O_{P^1}(-2-66 delta),

so H^0(N_{C/F})=0: C is rigid on the special fiber.

For a divisor on a smooth surface, Bloch's semiregularity map

    H^1(N_{C/F}) -> H^2(O_F)

is Serre-dual to restriction

    H^0(K_F) -> H^0(K_F|_C).                              (4.1)

Now H^0(K_F)=H^0(P^3,O(66)), because 66<70 and the intermediate cohomology of line bundles on P^3 vanishes. For a line, restriction of degree-66 polynomials is surjective. For a smooth conic, restrict first to its plane and then to the conic; the standard exact sequence for a plane conic gives surjectivity as well. Hence (4.1) is surjective, so the divisor semiregularity map is injective.

Therefore every pi(L) is a **rigid semiregular line or conic** on the supersingular special fiber F.

The obstruction-space dimensions are

    h^1(N_{C/F})=67   for a line,
    h^1(N_{C/F})=133  for a conic.

## 5. What this changes and what remains open

U55 produced a pure Adams-weight-2 formal K_0 lift of the target but left algebraization open. U56 supplies geometrically simple actual divisor representatives on the special fiber whose classes span the entire supersingular H^2, including beta and gamma.

Thus one may choose C_beta and C_gamma and consider

    Z=C_beta x C_gamma subset F x F.

Its class has a nonzero beta tensor gamma component, and Z is an lci surface built from rigid semiregular rational curves. This is a substantially more concrete input than an arbitrary special-fiber cycle.

However, neither C_beta nor C_gamma can lift as a divisor to characteristic zero in the required transcendental directions. The next load-bearing question is whether the **coupled codimension-two object Z**, or an appropriate character-projected perfect complex built from its translates, has injective codimension-two semiregularity and therefore admits an object-level formal lift compatible with U55. A mixed-characteristic semiregularity theorem or a direct obstruction calculation is required; it is not supplied by the divisor argument above.

## 6. Sources

- J. Page, T. Ryan, K. E. Smith, *Smooth surfaces with maximally many lines*, Forum of Mathematics, Sigma (2026), Theorem 1.1, Example 3.3, Proposition 3.11 / the generalized-quadrangle description. DOI 10.1017/fms.2026.10243.
- T. Shioda, T. Katsura, *On Fermat varieties*, Tohoku Math. J. 31 (1979), 97–115, for the classical extremal/supersingular Fermat context used elsewhere in the project.

No claim of formal verification or independent expert review is made.
