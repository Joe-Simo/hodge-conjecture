# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

Status: no complete proof or counterexample has been verified.

## Current checkpoint: U39 (2026-09-15)

[U39: exact necessary field and abelian-coefficient obstruction](research/U39_exact_Kummer_subfield_and_abelian_obstruction.md) proves a uniform squared Jacobi-sum identity for the degree-70 target. Its normalized Galois representation has a cyclic degree-70 kernel field E containing the explicit degree-35-over-K field M=K((2*5^30*7^14)^(1/35)), K=Q(zeta_70). Every nonzero target cycle defined over a number field containing K requires that field to contain E. Since M/Q is nonabelian, cycles or coherent-sheaf Chern characters defined over any cyclotomic number field have zero target projection.

This is a necessary condition, not a cycle construction or a solution of the Hodge conjecture. The proof is self-reviewed, not formally or independently expert-verified. The tempting field K(C^(1/70)), where C^2=-2^32*5^15/7^7 is the specified cyclotomic square root, is separately ruled out; a nontrivial quadratic character remains to be identified.

[Exact Python checker](research/computations/U39/verify_u39.py), [run certificate](research/computations/U39/verification.json), [independent Wolfram input](research/computations/U39/independent_wolfram.wl), [source audit](research/computations/U39/source_record.md), and [self-review](research/computations/U39/self_review.md).

The outstanding [U37 toric component proof](research/U37_toric_component_obstruction.md) and [U38 degree-70 cycle-field restriction](research/U38_degree70_field_of_definition_obstruction.md) are retained with their original evidence. No old research note is globally revalidated by U39.

Next obligation: identify the remaining quadratic factor and attempt an actual nonambient cycle or characteristic-zero Fermat correspondence over an adequate nonabelian field. Do not infer algebraicity from a finite-order Galois representation. Purely cyclotomic-coefficient searches and the U35 parameter family are excluded for different, proved reasons.

## Preserved checkpoint: U36 (2026-09-15)

[U36: uniform vanishing of the U35 surface family](research/U36_U35_uniform_vanishing.md) proves that every nonzero-parameter member is irreducible and has class 12h^2, hence zero primitive class. U35's lattice facts survive, but its proposed nonzero target projection is ruled out. Historical notes are retained and are not all revalidated by this checkpoint.

[Exact checker](research/computations/U36/verify_u36.py), [run certificate](research/computations/U36/verification.json), and [independent Wolfram arithmetic](research/computations/U36/independent_wolfram.json).
