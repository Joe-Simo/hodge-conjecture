# Hodge conjecture research checkpoint — 2026-09-14

## Status

No complete proof or counterexample of the rational Hodge conjecture has been verified.

## Exact target

For every smooth projective complex algebraic variety X and every p, every rational cohomology class alpha in H^{2p}(X,Q) whose complexification lies in H^{p,p}(X) should lie in the Q-span of codimension-p algebraic cycle classes. This is the rational projective Hodge conjecture, not the integral, Kähler-only, generalized, variational, or noncommutative variants.

## Official status checked

- Clay current problem page: https://www.claymath.org/millennium/hodge-conjecture/ — Unsolved.
- Pierre Deligne official description: https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf.
- Current rules: https://www.claymath.org/millennium-problems/rules/ — qualifying publication, two-year wait, and general acceptance are required before CMI consideration.

## Verified boundary theorem: dimension <= 3

Let h=c1(O_X(1)). The Lefschetz (1,1) theorem says every rational Hodge class in H^2(X,Q) is a rational divisor class: after multiplying by an integer it is an integral (1,1)-class, hence c1 of a line bundle.

For dim_C X=n, Hard Lefschetz gives L^{n-2}:H^2(X,Q)->H^{2n-2}(X,Q), beta |-> h^{n-2} cup beta. It is a rational Hodge isomorphism. Thus every rational (n-1,n-1)-class is h^{n-2} times a rational (1,1)-class and therefore a rational linear combination of codimension-(n-1) algebraic cycle classes.

Consequently every smooth projective complex variety of dimension at most 3 satisfies the rational Hodge conjecture: the only nontrivial codimensions are p=1 and, for threefolds, p=2=n-1.

## Audit of a 2025 purported Fermat-quintic counterexample

Fujioka Tomori, SSRN 5180689, claims a rational Hodge counterexample on a Fermat quintic threefold. A smooth Fermat quintic is a projective threefold, so the verified theorem above rules out any genuine rational Hodge counterexample there.

The accessible abstract also says that a nonzero Abel-Jacobi value for a proposed H^{2,2}(X,Q) class proves it lies outside the cycle-class image. This is not a valid general obstruction: the classical Abel-Jacobi map applies to homologically trivial algebraic cycles (or refinements thereof), whereas the Hodge conjecture asks whether a cohomology class is represented by a rational algebraic cycle class. The accessible abstract therefore does not change the official open status.

Source: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5180689

## Deformation/Hodge-locus route: current limitation

Cattani-Deligne-Kaplan algebraicity of Hodge loci controls where a flat rational class remains Hodge in a family; it does not itself produce an algebraic cycle representing that class. Buchweitz-Flenner semiregularity gives deformation machinery for algebraic cycles/perfect complexes under additional hypotheses, but an arbitrary Hodge class is not known to admit a suitable algebraic or semiregular witness anywhere on its Hodge locus.

## Active routes

1. Construction: cycle-producing mechanisms beyond the divisor/hard-Lefschetz boundary, starting with middle H^4 classes on fourfolds.
2. Deformation: Hodge loci plus semiregularity, with existence and propagation audited separately.
3. Falsification: explicit rational (2,2) classes on smooth projective fourfolds, requiring a structural obstruction excluding every rational algebraic-cycle combination.

## Next obligation

Analyze the first genuinely open dimensional frontier: codimension-2 rational Hodge classes on smooth projective fourfolds. Decompose H^4 into the hyperplane-generated and primitive pieces and audit whether standard correspondence/deformation arguments genuinely prove algebraicity of the primitive part or import an unproved algebraic correspondence.
