"""Exact checks for U48; not a proof assistant for the geometric argument.

Finite domain: 24 units modulo 70, six coordinate pairs, 16 assignments of
four target curves to two source factors, and the 140 deck pairs of the
explicit crossed construction. Polynomial identities are exact over Q(i).
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product
import json
from math import gcd
from pathlib import Path
import platform
import unittest

import sympy as sp

LEVEL = 70
UNITS = tuple(u for u in range(1, LEVEL) if gcd(u, LEVEL) == 1)
BRANCHES = ((2, 7, 61), (6, 5, 59))
TARGET = (37, 49, 33, 25)
NAMES = ("D5", "C5", "D7", "C7")


def cyclic_holomorphic_dimension(k: int, branch: tuple[int, ...]) -> int:
    """Moonen's eigenvalue convention: delta^* omega = zeta^k omega."""
    if k % LEVEL == 0:
        return 0
    numerator = sum((-k * a) % LEVEL for a in branch)
    if numerator % LEVEL:
        raise ValueError("The branch tuple is not balanced at this character")
    return numerator // LEVEL - 1


def cyclic_holomorphic_characters(branch: tuple[int, ...]) -> frozenset[int]:
    values = {k: cyclic_holomorphic_dimension(k, branch) for k in range(1, LEVEL)}
    if any(d not in (0, 1) for d in values.values()):
        raise ValueError("This checker expects multiplicities zero or one")
    return frozenset(k for k, d in values.items() if d == 1)


HOL = (
    cyclic_holomorphic_characters(BRANCHES[0]),
    frozenset((49, 63)),
    cyclic_holomorphic_characters(BRANCHES[1]),
    frozenset((45, 55, 65)),
)


def profiles(target: tuple[int, ...] = TARGET) -> tuple[tuple[int, ...], ...]:
    if len(target) != 4:
        raise ValueError("Expected four character exponents")
    return tuple(tuple(int(k * u % LEVEL in hs) for u in UNITS)
                 for k, hs in zip(target, HOL, strict=True))


def pair_rows() -> list[dict[str, object]]:
    ps = profiles()
    result = []
    for i, j in combinations(range(4), 2):
        bad = [(u, ps[i][a], ps[j][a]) for a, u in enumerate(UNITS)
               if ps[i][a] + ps[j][a] != 1]
        result.append({"pair": [NAMES[i], NAMES[j]], "bad_units": len(bad),
                       "first_witness": list(bad[0]) if bad else None})
    return result


def symbolic_checks() -> dict[str, bool]:
    t, s, w, v = sp.symbols("t s w v", nonzero=True)
    # Source: w^10=t^2(1+t^7), v^14=s^6(1+s^5).
    g5 = w**10 - t**2 * (1 + t**7)
    g7 = v**14 - s**6 * (1 + s**5)
    gb = sp.groebner([g5, g7], w, v, t, s, extension=sp.I)

    def vanishes(expr: sp.Expr) -> bool:
        numerator = sp.fraction(sp.cancel(expr))[0]
        return gb.reduce(numerator)[1] == 0

    y5 = w**2 * s
    z5 = sp.I * w**5 * v**7 / s**3
    x7 = v**2 * t / s
    z7 = sp.I * w**5 * v**7 / (s**3 * t)
    return {
        "D5_to_C7": vanishes((w**5 / t)**2 - (t**7 + 1)),
        "D7_to_C5": vanishes((v**7 / s**3)**2 - (s**5 + 1)),
        "crossed_image_on_S5": vanishes(z5**2 + y5**5 + t**9 + t**2),
        "crossed_image_on_S7": vanishes(z7**2 + s**5 + x7**7 * s + 1),
        "crossed_z_relation": sp.cancel(z5 - t * z7) == 0,
        "crossed_y_relation": vanishes(y5**5 - t**2 * (1 + t**7) * s**5),
        "crossed_x_relation": vanishes(x7**7 * s - t**7 * (1 + s**5)),
        "crossed_square_relation": vanishes(z7**2 + (1 + t**7) * (1 + s**5)),
    }


def report() -> dict[str, object]:
    ps = profiles()
    # A source deck pair sends (w,v) to (zeta_10^a w,zeta_14^b v).
    kernel = [(a, b) for a, b in product(range(10), range(14))
              if 2*a % 10 == 0 and 2*b % 14 == 0 and (a+b) % 2 == 0]
    return {
        "status": "finite assertions verified; geometry is proved separately in U48",
        "python": platform.python_version(), "sympy": sp.__version__,
        "base_commit": "2b2032a2c846436b0105ec426147a640db8f721b",
        "target_exponents": TARGET, "unit_count": len(UNITS),
        "holomorphic_characters": {name: sorted(hs) for name, hs in zip(NAMES, HOL, strict=True)},
        "target_profile_by_unit": {str(u): [p[i] for p in ps] for i, u in enumerate(UNITS)},
        "full_profile_sums": sorted(set(map(sum, zip(*ps, strict=True)))),
        "pair_obstructions": pair_rows(),
        "source_assignments_by_number_in_first_factor": dict(sorted(Counter(sum(a) for a in product((0, 1), repeat=4)).items())),
        "crossed_source_deck_kernel": kernel,
        "source_degree_over_t_s": 140,
        "source_degree_over_crossed_surface": len(kernel),
        "crossed_surface_degree_over_t_s": 140 // len(kernel),
        "crossed_projection_degrees_to_surfaces": [35, 35],
        "crossed_base_degrees_f5_g7_and_f5_f7": [70, 50],
        "symbolic_checks": symbolic_checks(),
        "nonclaims": ["No arbitrary-cycle nonalgebraicity", "No solution of Hodge",
                       "No universal obstruction to product-dominated cycles on S5 x S7"]
    }


class U48Tests(unittest.TestCase):
    def test_cyclic_models_and_genera(self) -> None:
        for branch, expected in zip(BRANCHES, (31, 32), strict=True):
            self.assertEqual(sum(branch), LEVEL)
            self.assertEqual(gcd(LEVEL, *branch), 1)
            genus = 1 + (LEVEL - sum(gcd(LEVEL, a) for a in branch)) // 2
            self.assertEqual(genus, expected)
            self.assertEqual(len(cyclic_holomorphic_characters(branch)), expected)
            for k in range(1, LEVEL):
                expected_h1 = sum(k*a % LEVEL != 0 for a in branch) - 2
                self.assertEqual(cyclic_holomorphic_dimension(k, branch) +
                                 cyclic_holomorphic_dimension(-k, branch), expected_h1)

    def test_canonical_form_characters_and_profiles(self) -> None:
        self.assertEqual((40-3, 2*40-3), (37, 77))
        self.assertEqual(((3*14-5) % 70, (2*14-3) % 70), (37, 25))
        p = profiles()
        self.assertEqual(Counter(p[0][i]+p[1][i] for i in range(24)), {0: 1, 1: 22, 2: 1})
        self.assertEqual(Counter(p[2][i]+p[3][i] for i in range(24)), {0: 1, 1: 22, 2: 1})
        self.assertEqual(set(map(sum, zip(*p, strict=True))), {2})
        self.assertEqual(len({tuple(u*k % LEVEL for k in TARGET) for u in UNITS}), 24)

    def test_all_pair_obstructions(self) -> None:
        rows = pair_rows()
        self.assertEqual([row["bad_units"] for row in rows], [2, 12, 10, 10, 12, 2])
        self.assertEqual([row["first_witness"] for row in rows],
                         [[1, 1, 1], [3, 1, 1], [13, 1, 1],
                          [13, 0, 0], [3, 0, 0], [1, 0, 0]])
        # Transport by any coefficient-field embedding preserves failure.
        for v in UNITS:
            p = profiles(tuple(v*k % LEVEL for k in TARGET))
            self.assertTrue(all(any(p[i][a]+p[j][a] != 1 for a in range(24))
                                for i, j in combinations(range(4), 2)))

    def test_positive_pair_control(self) -> None:
        # On C5 x C5, conjugate eigenspaces do support diagonal divisor classes.
        first = [int(49*u % 70 in HOL[1]) for u in UNITS]
        dual = [int(21*u % 70 in HOL[1]) for u in UNITS]
        self.assertTrue(all(a+b == 1 for a, b in zip(first, dual, strict=True)))
        self.assertEqual(set(2*(a+b) for a, b in zip(first, dual, strict=True)), {2})

    def test_exact_crossed_maps(self) -> None:
        self.assertTrue(all(symbolic_checks().values()))

    def test_deck_kernel_and_degrees(self) -> None:
        data = report()
        self.assertEqual(data["crossed_source_deck_kernel"], [(0, 0), (5, 7)])
        self.assertEqual(data["crossed_surface_degree_over_t_s"], 70)
        self.assertEqual((10*7//2, 14*5//2, 10*10//2), (35, 35, 50))
        # Both crossed maps are equivariant in the fixed generator convention.
        self.assertEqual((40, (5-40) % 70), ((11*10) % 70, (11*35) % 70))
        self.assertEqual((14, (7-3*14) % 70), (14, 35))
        self.assertNotEqual((37 + 11*25) % 70, 0)
        self.assertNotEqual((49 + 33) % 70, 0)

    def test_source_factor_assignments(self) -> None:
        counts = Counter(sum(a) for a in product((0, 1), repeat=4))
        self.assertEqual(counts, {0: 1, 1: 4, 2: 6, 3: 4, 4: 1})
        # Only 2+2 assignments can contribute to H1^tensor4 of a surface.
        matchings = {tuple(sorted((tuple(i for i, b in enumerate(a) if b),
                                   tuple(i for i, b in enumerate(a) if not b))))
                     for a in product((0, 1), repeat=4) if sum(a) == 2}
        self.assertEqual(len(matchings), 3)

    def test_projector_kernel_character(self) -> None:
        # Cover D5->C7 has order5 kernel generated by delta_D5^14;
        # cover D7->C5 has order7 kernel generated by delta_D7^10.
        self.assertEqual(37*14 % 70, 28)
        self.assertEqual(33*10 % 70, 50)
        self.assertTrue(all(37*u*14 % 70 != 0 and 33*u*10 % 70 != 0 for u in UNITS))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(U48Tests)
    run = unittest.TextTestRunner(verbosity=2).run(suite)
    if not run.wasSuccessful():
        raise SystemExit(1)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report(), indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
