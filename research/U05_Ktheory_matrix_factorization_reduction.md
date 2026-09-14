# U05: rational K-theory reformulation and hypersurface matrix-factorization engine

Status: verified partial reformulation and route checkpoint only. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## 1. Universal rational K-theory reformulation

Let X be a smooth projective complex variety. There are two rational Chern-character descriptions:

1. Topological K-theory:

   ch_top : K^0_top(X) \otimes Q -> H^{even}(X,Q)

   is an isomorphism.

2. Algebraic K-theory / Chow theory: for smooth X, the rational Chern character identifies the associated rational gamma filtration on K_0^alg(X) with CH^*(X)_Q; composing with the cycle-class map gives the ordinary cohomological Chern character of algebraic vector bundles/coherent sheaves.

Deligne's official Clay description, Remark 2(ii), states the corresponding geometric fact directly: integral linear combinations of algebraic cycle classes coincide with integral linear combinations of products of Chern classes of algebraic vector bundles. Thus, after tensoring with Q, the span of algebraic cycle classes equals the span of rational cohomological Chern characters of algebraic K-classes degree-by-degree.

Define

  K_Hdg^0(X)_Q := ch_top^{-1}( \bigoplus_p (H^{2p}(X,Q) \cap H^{p,p}(X)) ).

Then the rational Hodge conjecture for X is equivalent to:

  every element of K_Hdg^0(X)_Q lies in the rational topological-realization image of K_0^alg(X)_Q.

Proof sketch of the equivalence:

- If the Hodge conjecture holds, every diagonal rational cohomology component is a rational combination of algebraic cycle classes. Deligne's Chern-class description (or rational GRR/gamma filtration) realizes those components through algebraic K-classes. By induction on codimension one can cancel unwanted lower/higher degree components and obtain a preimage for any Hodge-diagonal topological K-class.
- Conversely, if every Hodge-diagonal topological K-class has an algebraic K-preimage, take a pure class alpha in H^{2p}(X,Q) cap H^{p,p}(X), apply ch_top^{-1}, and realize it algebraically. Its degree-2p Chern-character component is then a rational combination of algebraic cycle classes, giving alpha.

This is not a solution: the hard problem has become the existence of algebraic (equivalently holomorphic coherent) K-classes representing Hodge-diagonal topological K-classes.

## 2. Why this is more useful on hypersurfaces

Favero–Kelly, arXiv:2609.12759v1 (2026), prove an explicit formula for the primitive Chern character of a coherent sheaf on a smooth projective hypersurface X=Z(Q) in terms of a matrix factorization A,B with

  AB=BA=Q id.

For dim X=2k, under the Griffiths residue identification

  H^{k,k}_prim(X) ~= Jac(Q)_{(k+1)deg Q-(2k+2)},

the primitive kth Chern character is an explicit trace polynomial built from alternating partial derivatives of A and B (Theorem 1.3 / 3.6 of that preprint).

They deduce that for a smooth even-dimensional hypersurface, the Hodge conjecture is equivalent to spanning every primitive Hodge polynomial in the Jacobian ring by rational linear combinations of these matrix-factorization trace polynomials (their Conjecture 1.4 and Corollary 1.5).

This converts algebraic-cycle construction on hypersurfaces into a concrete commutative-algebra / matrix-factorization problem.

## 3. Scope limitation

The matrix-factorization criterion is presently a hypersurface criterion. An arbitrary smooth projective variety is not canonically a projective-space hypersurface, and no valid reduction from the universal Hodge conjecture to this hypersurface criterion has been established here.

Therefore the route is used as:

- a construction engine for concrete hypersurface families;
- a falsification laboratory for proposed universal mechanisms;
- a way to seek new algebraic cycles whose geometry might later generalize.

It must not be promoted to a universal proof without a separate theorem transferring arbitrary Hodge classes to and back from the hypersurface setting through algebraic correspondences.

## 4. Current executable target

A recent conditional-preprint census isolates the degree-70 Fermat-fourfold character

  alpha = (1,20,24,42,61,62) mod 70

as a class for which its tested join/curve-pair/pair-descent/Aoki/level-change constructions fail. This claim is not yet a primary peer-reviewed theorem and is treated only as a lead.

Because Favero–Kelly give an exact matrix-factorization formula, this orbit is a useful concrete stress test: construct a coherent sheaf or matrix factorization whose primitive Chern character has nonzero projection onto its Galois orbit, or prove that a proposed restricted ansatz cannot do so.

## Primary sources

- P. Deligne, official Clay Hodge problem description, especially Remark 2(ii): https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf
- D. Favero and T. L. Kelly, `The Chern character of a coherent sheaf on a smooth projective hypersurface`, arXiv:2609.12759v1, 2026: https://arxiv.org/abs/2609.12759
