# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

**Status: no complete proof or counterexample has been verified.**

## Current checkpoint: U43 (2026-09-15)

[U43: full tensor block and rational rank-one reduction](research/U43_full_tensor_block_and_rank_one_reduction.md) supplies a 31-term integral correspondence certificate connecting all 24 conjugate character motives. Combined with U42, this proves algebraicity of the full 576-dimensional W tensor W block on X x X, not just the 24 matched squares. Its new rational consequence is End_Chow(Wcal)=Mat_24(Q) and Wcal=N^(direct sum 24), with N a rational rank-one Chow motive satisfying N tensor N=L^4.

No algebraic cycle representing the original target on X has been constructed. The remaining problem is a nonzero realized morphism L^2 -> N, equivalently trivializing T=N tensor L^(-2) itself, not its tensor square. Diagonal restriction and contraction with ambient surface classes were checked and do not furnish that morphism. A general invertible-motive classification found in the literature is conjectural and is not used.

[Standalone exact checker](research/computations/U43/verify_u43.py), [verification](research/computations/U43/verification.json), [separate Wolfram check](research/computations/U43/independent_wolfram.json), [source and self-review](research/computations/U43/source_and_self_review.md), and [validation record](research/computations/U43/validation_status.json).

Ten new tests and eight inherited U42 tests pass; all 24 differences and 576 mixed certificates are checked with exact integers. Syntax compilation passes. Ruff and mypy are unavailable in the current runtime, so lint and static type checking remain unperformed. The optional Smith discovery and separate stateless Wolfram check were corrected and rerun successfully; the discarded execution errors are documented. Mathematical review is by the same assistant, not a formal kernel or independent expert.

**Next obligation:** construct a surface-supported source correspondence for N or a surface Z on X with nonzero W projection; do not confuse an algebraic projector on the product with an algebraic vector on X. Earlier mathematical files are preserved unchanged.

## Preserved checkpoint: U42 (2026-09-15)

[U42: algebraicity of the diagonal tensor-square block](research/U42_tensor_square_algebraicity.md) proves, using characteristic-zero Chow correspondences of Otsubo–Yamazaki and an exact integer certificate, that M_alpha tensor M_alpha is isomorphic to L^4 for the degree-70 target alpha=(1,20,24,42,61,62). Consequently the simultaneous 24-dimensional rational orbit block in H^8(X x X) is algebraic. This concerns codimension-four cycles on the product of two fourfolds, not the original codimension-two target on X.

An exact parity functional kills all 347 admissible level-70 multiplication relations and all reflection relations but not the unsquared normalized target. It identifies order two in this formal relation quotient only; additional geometric relations may kill it. No nonalgebraicity or nontriviality of the actual normalized Chow motive is asserted.

[Proof](research/U42_tensor_square_algebraicity.md), [exact Python checker](research/computations/U42/verify_u42.py), [run summary](research/computations/U42/run_summary.json), [test log](research/computations/U42/test_run.log), [independent Wolfram input](research/computations/U42/independent_wolfram.wl), [source/application audit](research/computations/U42/source_record.md), and [self-review](research/computations/U42/self_review.md).

Eight focused tests pass, including the complete integer certificate, all 24 conjugates, the parity checks, and all 343000 cocycle-case dictionaries. Separate Wolfram arithmetic agrees. Syntax compilation passes; ruff and mypy remain unavailable, so native lint/static type checks were not run. The mathematical proof is self-reviewed, not formally verified or independently expert-reviewed. No polynomial equations for a cycle on the original X have been constructed.

Regenerate the detailed certificate and secondary surface-profile census with:

    python research/computations/U42/verify_u42.py --output research/computations/U42/verification.json

**Next obligation:** construct a nonzero algebraic correspondence L^2 -> M_alpha, rather than another tensor square. Do not infer the original Hodge class is algebraic merely from its tensor square or from a trivialized Galois representation.

## Preserved checkpoints

- [U40: arithmetic reconciliation and diagonal normalization](research/U40_twist_reconciliation_and_normalization.md) identifies the residual quadratic factor and appropriate coefficient fields; this is not a cycle construction.
- [U41: proper tensor and raw-retract obstructions](research/U41_tensor_and_retract_obstructions.md) leaves coupled constructions and retracts of nontrivial cones open. It concerns factorizations on X, not the new correspondence on X x X.
- [U39: necessary Kummer subfield and abelian-coefficient obstruction](research/U39_exact_Kummer_subfield_and_abelian_obstruction.md), [U38: cycle-field restriction](research/U38_degree70_field_of_definition_obstruction.md), and [U37: toric component obstruction](research/U37_toric_component_obstruction.md) remain preserved with their original evidence and scopes.
- [U36: uniform vanishing of the U35 surface family](research/U36_U35_uniform_vanishing.md) rules out that family uniformly; do not restart its parameter search.

Historical mathematical files were not modified by U42 and are not globally revalidated by it. The previous README is preserved in parent commit 489b743689ac96345ea56ec49f4a1568623236cc.
