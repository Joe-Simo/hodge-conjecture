# U02: deformation-anchor obstruction for primitive fourfold Hodge classes

Status: verified partial route audit only. This does not solve the Hodge conjecture.

Date: 2026-09-14.

## 1. Active target

By U01, for a smooth projective complex fourfold X it is enough to prove algebraicity of every primitive rational class

    alpha in H^4(X,Q) cap H^{2,2}(X),   h cup alpha = 0.

This unit audits a natural deformation strategy: place (X,alpha) in a smooth projective family, move to a fiber where the corresponding class is represented by an algebraic cycle, and transport that cycle back.

## 2. Exact transport lemma

Let pi: mathcal X -> S be a smooth projective morphism over a connected smooth complex base. Let alpha be a flat section of R^{2p} pi_* Q such that alpha_s is of type (p,p) at every point s in S.

Assume:

1. for some s0 in S, alpha_{s0}=cl(Z0) for a rational codimension-p algebraic cycle Z0 on X_{s0}; and
2. the variational Hodge conjecture is known for this family/class (or a theorem supplies the same conclusion).

Then alpha_s is algebraic for every s in S, in particular on the target fiber.

This is simply the contract of the variational Hodge principle: it is a propagation theorem from an algebraic anchor. It is not a construction theorem for the anchor itself.

A stronger elementary statement holds whenever Z0 extends to an actual relative algebraic cycle Z on mathcal X over a connected neighborhood: proper smooth Ehresmann/Gauss-Manin identification makes cl(Z_s) locally flat, so the cycle classes of the fibers give the transported cohomology class. Again, existence of the relative cycle is the nontrivial input.

## 3. Earliest unsupported implication in the naive strategy

For an arbitrary primitive Hodge class alpha on X, one can form its Hodge locus in a deformation family: the locus where the flat continuation of alpha remains of type (2,2). Cattani-Deligne-Kaplan implies such Hodge loci are algebraic (more precisely countable unions of algebraic subvarieties in the standard VHS setup).

But algebraicity of the Hodge locus does not imply that it contains a point where alpha is the class of an algebraic cycle. That implication is essentially the missing Hodge problem along the component.

Therefore the following proposed bridge is invalid without an additional theorem:

    'alpha remains Hodge along an algebraic locus'
        =>
    'some point of that locus has an algebraic cycle representing alpha'.

No such general implication is presently verified.

## 4. Semiregularity does not remove the anchor requirement

Known semiregularity theorems control deformations of an existing subvariety/sheaf/cycle. Results such as Buchweitz-Flenner and later applications show that, under semiregularity hypotheses, an algebraic cycle can deform when its cohomology class remains Hodge.

Logically their input already contains an algebraic object Z0. Thus they can establish

    existing algebraic Z0 + Hodge persistence + semiregularity
        => deformation of Z0,

but not

    bare Hodge class alpha
        => existence of Z0.

Using semiregularity to assert the latter would be circular for the universal Hodge conjecture.

## 5. Updated abelian-fourfold test case

Historically abelian fourfolds, especially varieties of Weil type, were a central first-open test family because their exceptional middle-dimensional Weil classes were not known to be algebraic.

Eyal Markman, arXiv:2502.03415 (2025), proves algebraicity of Weil classes for abelian sixfolds of Weil type of discriminant -1 and derives algebraicity for all abelian fourfolds of Weil type (all discriminants and imaginary quadratic fields) via Schoen degeneration. Corollary 1.6.1 of the preprint states that the Hodge conjecture holds for abelian fourfolds, using the known classification of Hodge classes on simple/non-simple abelian fourfolds.

This means abelian fourfolds are no longer an appropriate unresolved counterexample-search frontier if Markman's theorem chain is accepted. The general fourfold problem remains open.

## 6. Consequence for route selection

The deformation route is retained only in forms that explicitly solve the anchor problem. A viable new lemma would need to do at least one of the following without assuming Hodge:

- force a Hodge-locus component to meet a fiber where the class is independently known algebraic;
- construct an algebraic correspondence carrying the class to/from a class in a solved family;
- produce a genuine cycle from additional geometric structure on the target fiber itself.

Merely proving the Hodge locus algebraic, smooth, dense, or positive-dimensional is insufficient.

## 7. Next obligation

Search for a universal or sufficiently general correspondence mechanism for primitive H^4 of fourfolds whose algebraicity is independently established. The immediate audit question is whether coniveau/cylinder/normal-function constructions can produce an algebraic correspondence onto an arbitrary primitive rational (2,2)-class without assuming a standard conjecture or Hodge itself.
