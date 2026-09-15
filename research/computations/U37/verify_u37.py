"""Finite checks for U37; the general component theorem is proved in prose."""
from __future__ import annotations

import json
import math
import unittest
from collections import Counter
from itertools import combinations
from pathlib import Path

import sympy as sp

ALPHA = (1, 20, 24, 42, 61, 62)


def conic_orders() -> list[int]:
    """All 90 disjoint-triple partitions, with a middle coordinate in each."""
    orders = []
    for first in combinations(range(6), 3):
        if 0 not in first:
            continue
        second = tuple(i for i in range(6) if i not in first)
        for mid1 in first:
            for mid2 in second:
                e1 = tuple(i for i in first if i != mid1)
                e2 = tuple(i for i in second if i != mid2)
                defects = (ALPHA[e1[0]] - ALPHA[e1[1]],
                           ALPHA[mid1] + 2 * ALPHA[e1[0]],
                           ALPHA[e2[0]] - ALPHA[e2[1]],
                           ALPHA[mid2] + 2 * ALPHA[e2[0]])
                orders.append(70 // math.gcd(70, *defects))
    return orders


class Checks(unittest.TestCase):
    def test_no_complementary_pairs(self) -> None:
        self.assertTrue(all((ALPHA[i] + ALPHA[j]) % 70 for i, j in combinations(range(6), 2)))

    def test_segre_factorization(self) -> None:
        a, b, c, d, e = sp.symbols("a b c d e")
        self.assertEqual(sp.expand(a*d + b*d + c*d + a*e + b*e + c*e
                                   - (a+b+c)*(d+e)), 0)
        # a,b,c stand for s_i^m and d,e for t_j^m. This identity is uniform in m.

    def test_conic_join_factorization(self) -> None:
        a, b, c, d = sp.symbols("a b c d")
        self.assertEqual(sp.expand(a*a+2*a*b+b*b+c*c+2*c*d+d*d
                                   - (a+b+sp.I*(c+d))*(a+b-sp.I*(c+d))), 0)

    def test_all_conic_join_character_orders(self) -> None:
        orders = conic_orders()
        self.assertEqual(len(orders), 90)
        self.assertEqual(Counter(orders), {70: 78, 35: 12})
        self.assertTrue(all(q > 2 for q in orders))
        # Direct modular membership, separately, for the standard labelling.
        r = (1, -2, 1, 0, 0, 0)
        s = (0, 0, 0, 1, -2, 1)
        span = {tuple((u*a+v*b) % 70 for a, b in zip(r, s))
                for u in range(70) for v in range(70)}
        first = next(q for q in range(1, 71)
                     if tuple(q*a % 70 for a in ALPHA) in span)
        self.assertEqual(first, 70)


def main() -> int:
    folder = Path(__file__).resolve().parent
    with (folder / "test_run.log").open("w", encoding="utf-8") as stream:
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(
            unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    report = {"tests": result.testsRun, "passed": result.wasSuccessful(),
              "conic_join_configurations": 90,
              "character_order_counts": dict(Counter(conic_orders())),
              "arithmetic": "exact integers and polynomial identities",
              "non_claim": "No cycle with a nonzero target projection constructed"}
    (folder / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
