"""Hodge-specific Jev screening client (code/jev_hodge.py).

Screens mathematical claims, papers, and candidate proofs/counterexamples
against the 5 canonical failure modes for the Hodge Conjecture.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "code"))

import jev


def build_questions() -> dict[str, Any]:
    return {
        "avoids_integral_hodge_conflation": jev.noul(
            "Does this argument strictly work over Q-coefficients, avoiding the disproved integral Hodge conjecture?",
            true="Explicitly works with rational cohomology and cycles, respecting Atiyah-Hirzebruch and Kollar counterexamples",
            false="Relies on integral Hodge classes or torsion algebraic cycles refuted by Atiyah-Hirzebruch"
        ),
        "avoids_nonprojective_kahler_overreach": jev.noul(
            "Does the variety strictly satisfy projectivity rather than general non-projective Kähler?",
            true="Explicitly requires an ample line bundle / projective embedding, respecting Claire Voisin's 2004 counterexample",
            false="Extends Hodge conjecture to general compact complex Kähler manifolds"
        ),
        "formal_algebraization_control": jev.choice(
            "How does the argument handle the formal-to-algebraic step across Witt thickenings?",
            criteria={
                "explicit_coherent_sheaf": "Constructs a genuine coherent sheaf/complex with vanishing obstruction spaces",
                "formal_gaga_naked_class_only": "Silently assumes a K0 pro-class algebraizes without a geometric object",
                "not_applicable": "The argument does not rely on formal K-theory or Witt vectors"
            }
        ),
        "avoids_w2_deformation_trap": jev.noul(
            "Does the argument respect the explicit W2 obstruction (U58 coefficient mismatch) for special-fiber curves?",
            true="Does not claim smooth deformation to W2, or resolves the quadratic Fermat defect mismatch",
            false="Assumes special-fiber semiregular conics or lines lift to W2 without checking deformation equations"
        ),
        "viability_score": jev.score(
            "Score the research candidate's rigor and potential for Hodge Conjecture progress",
            criteria=[
                "Mathematically sound, explicit hypotheses, respects proven barriers (Atiyah-Hirzebruch, Voisin, W2 obstruction)",
                "Clear proof path, relies on established external theorems with verified scope",
                "Exploratory but contains identifiable gaps or unverified formal algebraization",
                "Contains a known fatal flaw, circularity, or unproved shortcut"
            ]
        )
    }


def screen_candidate(candidate_id: str, text: str) -> dict[str, Any]:
    questions = build_questions()
    state = {
        "project": "Hodge-Conjecture",
        "target": "Every rational Hodge class is algebraic on smooth projective varieties",
        "candidate_id": candidate_id,
        "proposal_text": text
    }
    resp = jev.ask(state, questions)
    jev.persist(candidate_id, state, questions, resp)
    return resp


def main() -> None:
    parser = argparse.ArgumentParser(description="Jev Hodge Conjecture Screener")
    parser.add_argument("command", choices=["screen", "cache-stats", "clear-cache"])
    parser.add_argument("--id", default="candidate", help="Candidate identifier")
    parser.add_argument("--text", help="Candidate text or hypothesis summary")
    args = parser.parse_args()

    if args.command == "cache-stats":
        print(json.dumps(jev.cache_stats(), indent=2))
    elif args.command == "clear-cache":
        count = jev.clear_cache()
        print(f"Cleared {count} cache entries")
    elif args.command == "screen":
        if not args.text:
            print("Error: --text required for screen", file=sys.stderr)
            sys.exit(1)
        res = screen_candidate(args.id, args.text)
        print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
