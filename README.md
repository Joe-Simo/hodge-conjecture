# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

Status: no complete proof or counterexample has been verified.

## Current checkpoint: U40–U41 (2026-09-15)

[U40: exact arithmetic reconciliation and diagonal normalization](research/U40_twist_reconciliation_and_normalization.md) identifies the quadratic factor left open in the repository's U39, reconciles the two different U39 arguments, and gives a degree-12 real coefficient presentation for an arithmetic-normalized diagonal fourfold. It also proves that no all-rational diagonal coefficient choice gives this normalization over K. These are representation and field results, not an algebraic-cycle construction.

[U41: tensor and retract obstructions](research/U41_tensor_and_retract_obstructions.md) proves that every proper disjoint-variable tensor product of graded factorizations has zero target coefficient, and proves the same for all direct summands of raw six-factor rank-one univariate tensors. An explicit 4-by-4 positive control shows why zero total Chern character does not imply zero for a direct summand. Retracts of nontrivial cones and genuinely coupled constructions remain outside the obstruction.

[Arithmetic checker](research/computations/U40/verify_u40.py), [factorization checker](research/computations/U41/verify_u41.py), [evidence manifest](research/computations/U40/verification.json), [validation record](research/computations/U40/validation_status.json), and [self-review](research/computations/U41/self_review.md).

Fifteen new tests and 22 inherited local tests pass, with separate Wolfram arithmetic corroboration. Syntax compilation passes; native lint and static type checking remain unavailable because ruff and mypy are not installed. The proofs are self-reviewed, not formally verified or independently expert-reviewed. The two U39 versions are explicitly distinguished; no earlier historical claim is globally revalidated.

Next obligation: construct an actual target-bearing cycle or a coupled graded matrix factorization, or an even closed projector on a nontrivial cone with a nonzero inserted trace. Do not infer algebraicity from arithmetic normalization or infer summand vanishing from a parent's zero trace. The historic unresolved quadratic question below is answered by U40.

## Preserved checkpoint: U39 (2026-09-15)

[U39: exact necessary field and abelian-coefficient obstruction](research/U39_exact_Kummer_subfield_and_abelian_obstruction.md) proves a uniform squared Jacobi-sum identity for the degree-70 target. Its normalized Galois representation has a cyclic degree-70 kernel field E containing the explicit degree-35-over-K field M=K((2*5^30*7^14)^(1/35)), K=Q(zeta_70). Every nonzero target cycle defined over a number field containing K requires that field to contain E. Since M/Q is nonabelian, cycles or coherent-sheaf Chern characters defined over any cyclotomic number field have zero target projection.

This is a necessary condition, not a cycle construction or a solution of the Hodge conjecture. The proof is self-reviewed, not formally or independently expert-verified. The tempting field K(C^(1/70)), where C^2=-2^32*5^15/7^7 is the specified cyclotomic square root, is separately ruled out; a nontrivial quadratic character remains to be identified.

[Exact Python checker](research/computations/U39/verify_u39.py), [run certificate](research/computations/U39/verification.json), [independent Wolfram input](research/computations/U39/independent_wolfram.wl), [source audit](research/computations/U39/source_record.md), and [self-review](research/computations/U39/self_review.md).

The outstanding [U37 toric component proof](research/U37_toric_component_obstruction.md) and [U38 degree-70 cycle-field restriction](research/U38_degree70_field_of_definition_obstruction.md) are retained with their original evidence. No old research note is globally revalidated by U39.

Next obligation: identify the remaining quadratic factor and attempt an actual nonambient cycle or characteristic-zero Fermat correspondence over an adequate nonabelian field. Do not infer algebraicity from a finite-order Galois representation. Purely cyclotomic-coefficient searches and the U35 parameter family are excluded for different, proved reasons.

## Preserved checkpoint: U36 (2026-09-15)

[U36: uniform vanishing of the U35 surface family](research/U36_U35_uniform_vanishing.md) proves that every nonzero-parameter member is irreducible and has class 12h^2, hence zero primitive class. U35's lattice facts survive, but its proposed nonzero target projection is ruled out. Historical notes are retained and are not all revalidated by this checkpoint.

[Exact checker](research/computations/U36/verify_u36.py), [run certificate](research/computations/U36/verification.json), and [independent Wolfram arithmetic](research/computations/U36/independent_wolfram.json).
