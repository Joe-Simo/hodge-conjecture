# Hodge Conjecture Research — Working Instructions

**The Hodge Conjecture is not solved.** Treat every claim of a general proof or unconditional non-algebraic Hodge counterexample as unverified until audited against primary source dependencies and verified under machine-checked Lean 4 formalization.

## HARD RULE: Every research cycle STARTS with a Jev call

Not "consider using Jev" — **the first tool call of every research turn is a Jev batch.** If you are about to read, audit, compare, or choose between multiple candidate hypotheses or papers, run the screen first using `python3 code/jev_genius.py` or `python3 code/jev_hodge.py`.

Jev decisions that are fast, cheap, and mandatory:
- **Triage & ranking**: screen every candidate hypothesis with `code/jev_genius.py triage`.
- **Failure mode check**: verify arguments against the 5 canonical Hodge traps.
- **Statement fidelity**: for formal Lean 4 files, audit statement fidelity with `code/jev_genius.py lean-audit`.

## Canonical Hodge Failure Modes to Reject Immediately

1. **Integral Hodge Conflation**:
   Conflating the disproved *integral* Hodge conjecture (refuted by Atiyah & Hirzebruch in 1962 via Steenrod torsion, and Kollár in 1992 for 3-folds) with the open *rational* Hodge conjecture ($\mathbb{Q}$-coefficients).
2. **Kähler / Non-Projective Overreach**:
   Claiming the Hodge conjecture holds on general compact complex Kähler manifolds (disproved by Claire Voisin in 2004). Projectivity is required.
3. **Formal GAGA / Naked Class Algebraization Trap**:
   Assuming a compatible formal pro-class in $K_0(\widehat{X})$ automatically algebraizes without constructing a coherent sheaf / perfect complex (Grothendieck GAGA applies to geometric objects, not naked cohomology classes).
4. **First-Witt ($W_2$) Deformation Blindness**:
   Claiming a special-fiber curve or cycle over $\mathbb{F}_p$ lifts to characteristic zero without verifying the vanishing of obstruction classes in $H^2(X, \mathcal{O}_X)$ or checking the $W_2(\mathbb{F}_p)$ quadratic deformation equations.
5. **Coordinate-wise / Delsarte Torus Collapse**:
   Assuming diagonal or coordinate-wise Delsarte projections span primitive cohomology when torus-coset obstructions (U51) prove vanishing.

## Tools & Files

| Path | Role |
|---|---|
| `code/jev.py` | Stdlib-only Jev client. Reads key from `$TYPESAFE_API_KEY` or `.env.local`. Never log or commit the key. |
| `code/jev_hodge.py` | Focused Hodge Conjecture failure-mode and candidate screener. |
| `code/jev_genius.py` | Multi-tier Jev mathematical intelligence engine for Hodge. |
| `code/delsarte_hodge_sieve.c` | OpenMP-accelerated C sieve for Delsarte Hodge character orbits. |
| `code/comprehensive_hodge_discrepancy_suite.py` | Multi-track Hodge discrepancy and counterexample hunt suite. |
| `code/autonomous_hodge_engine.py` | High-throughput multi-core autonomous research daemon. |
| `formalization/HodgeCycleLattice.lean` | Lean 4 machine-checked proof of primitive Hodge decomposition and intersection pairing. |
| `sources/NO_GO_REGISTER.md` | Primary register of disproved conjectures, refuted frameworks, and mathematical barriers. |
| `sources/FAILED_CALCULATIONS_REGISTER.md` | Authoritative register of refuted literature calculations, retracted papers, and excluded heuristics. |
| `CHECKPOINT.json` | Persistent machine-readable project state. |
