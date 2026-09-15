# Hodge Conjecture Research

Private working repository for a rigorous attempt to resolve the rational Hodge conjecture in the official Clay Millennium formulation.

Status: no complete proof or counterexample has been verified.

## Current checkpoint: U36 (2026-09-15)

[U36: uniform vanishing of the U35 surface family](research/U36_U35_uniform_vanishing.md) proves that every nonzero-parameter member is irreducible and has class 12h^2, hence zero primitive class. U35's lattice facts survive, but its proposed nonzero target projection is ruled out. Historical notes are retained and are not all revalidated by this checkpoint.

[Exact checker](research/computations/U36/verify_u36.py), [run certificate](research/computations/U36/verification.json), and [independent Wolfram arithmetic](research/computations/U36/independent_wolfram.json).

Next obligation: construct a genuinely nonambient component or a nonseparable matrix factorization with a nonzero target coefficient. Do not rerun the U35 parameter search: the obstruction is uniform.
