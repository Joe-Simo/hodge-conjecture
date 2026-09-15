"""Exact arithmetic for U42, not a proof assistant for Chow correspondences.

Run from any directory with Python >= 3.10. No network or third-party package
is used. Output JSON is written only when --output PATH is explicitly given.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import sys
import time
import unittest
from collections import Counter
from typing import TypedDict

MODULUS = 70
ALPHA = (1, 20, 24, 42, 61, 62)
UNITS = tuple(u for u in range(1, MODULUS) if math.gcd(u, MODULUS) == 1)
REFLECTION_POWERS = ((1, 1), (4, 1), (9, 1), (16, 1), (22, -1),
                     (24, 2), (26, 1), (28, -1), (30, 1))
MULTIPLICATION_POWERS = ((2, 1, 1), (2, 9, -1), (2, 26, 1), (2, 34, -1),
                         (5, 4, -1), (5, 6, 1), (5, 12, -1),
                         (7, 2, 1), (7, 6, -1))
SELECTED = (14, 28, 42, 56)
Vector = tuple[int, ...]


class SurfaceRow(TypedDict):
    indices_zero_based: tuple[int, ...]
    left: tuple[int, ...]
    right: tuple[int, ...]
    left_profile: tuple[int, ...]
    right_profile: tuple[int, ...]
    hodge_numbers_20_11_02: list[int]


def exponent_vector(terms: list[tuple[int, int]]) -> Vector:
    """Coordinates 0..68 are e_1..e_69; coordinate 69 is ell."""
    result = [0] * 70
    for residue, coefficient in terms:
        residue %= MODULUS
        if residue == 0:
            raise ValueError("A nonzero Gauss exponent was required")
        result[residue - 1] += coefficient
    return tuple(result)


def reflection(a: int) -> Vector:
    return exponent_vector([(a, 1), (-a, 1)])


def multiplication(n: int, a: int) -> Vector:
    if n <= 1 or MODULUS % n or (n * a) % MODULUS == 0:
        raise ValueError("Invalid multiplication parameters")
    h = MODULUS // n
    return exponent_vector(
        [(a + h * j, 1) for j in range(n)]
        + [(n * a, -1)]
        + [(h * j, -1) for j in range(1, n)]
    )


def linear_combination(terms: list[tuple[int, Vector]]) -> Vector:
    return tuple(sum(c * v[i] for c, v in terms) for i in range(70))


def target_vector() -> Vector:
    v = list(exponent_vector([(a, 1) for a in ALPHA]))
    v[-1] = -3
    return tuple(v)


def certificate_vector() -> Vector:
    terms: list[tuple[int, Vector]] = []
    for a, power in REFLECTION_POWERS:
        v = list(reflection(a))
        v[-1] = -1
        terms.append((power, tuple(v)))
    terms.extend((power, multiplication(n, a))
                 for n, a, power in MULTIPLICATION_POWERS)
    return linear_combination(terms)


def epsilon(v: Vector) -> int:
    return sum(v[a - 1] for a in SELECTED) % 2


def admissible_multiplications() -> list[tuple[int, int]]:
    return [(n, a) for n in range(2, 71) if MODULUS % n == 0
            for a in range(1, 70) if n * a % MODULUS != 0]


def canonical_triple(a: int, b: int) -> tuple[int, ...]:
    return tuple(sorted((a % 70, b % 70, (-a - b) % 70)))


def cocycle_case_audit() -> dict[str, int]:
    """Check coverage and character dictionaries, not the external theorems."""
    counts: Counter[str] = Counter()
    for a, b, c in itertools.product(range(70), repeat=3):
        ab, bc, total = (a + b) % 70, (b + c) % 70, (a + b + c) % 70
        if 0 in (a, b, c):
            label = "zero_input"
        elif ab == 0 and bc == 0:
            label = "both_partial_sums_zero"
        elif ab == 0:
            label = "left_partial_sum_zero"
            assert canonical_triple(a, bc) == tuple(
                sorted((-t) % 70 for t in canonical_triple(b, c)))
        elif bc == 0:
            label = "right_partial_sum_zero"
            assert canonical_triple(ab, c) == tuple(
                sorted((-t) % 70 for t in canonical_triple(a, b)))
        elif total == 0:
            label = "total_zero"
            assert canonical_triple(a, b) == canonical_triple(b, c)
        else:
            label = "nondegenerate_surface_factorization"
            assert all(t != 0 for t in (a, b, c, ab, bc, total))
        counts[label] += 1
    return dict(sorted(counts.items()))


def surface_census() -> list[SurfaceRow]:
    rows: list[SurfaceRow] = []
    for chosen in itertools.combinations(range(6), 3):
        if 0 not in chosen:
            continue
        other = tuple(i for i in range(6) if i not in chosen)
        balance = sum(ALPHA[i] for i in chosen) % 70
        left = tuple(ALPHA[i] for i in chosen) + ((-balance) % 70,)
        right = tuple(ALPHA[i] for i in other) + (balance,)
        grades = tuple(sum(u * a % 70 for a in left) // 70 for u in UNITS)
        reverse = tuple(sum(u * a % 70 for a in right) // 70 for u in UNITS)
        rows.append({"indices_zero_based": chosen, "left": left, "right": right,
                     "left_profile": grades, "right_profile": reverse,
                     "hodge_numbers_20_11_02": [grades.count(k) for k in (1, 2, 3)]})
    return rows


class Verification(unittest.TestCase):
    def test_target_and_square_orbits(self) -> None:
        orbit = {tuple(u * a % 70 for a in ALPHA) for u in UNITS}
        self.assertEqual(len(orbit), 24)
        self.assertTrue(all(sum(v) == 210 and 0 not in v for v in orbit))
        self.assertEqual(len({(v, v) for v in orbit}), 24)
        self.assertFalse(any(v == tuple((-a) % 70 for a in v) for v in orbit))

    def test_full_integer_certificate(self) -> None:
        self.assertEqual(certificate_vector(), tuple(2 * x for x in target_vector()))
        self.assertEqual(sum(power for _, power in REFLECTION_POWERS), 6)
        self.assertEqual(len(REFLECTION_POWERS) + len(MULTIPLICATION_POWERS), 18)

    def test_source_admissibility_and_telescope(self) -> None:
        self.assertEqual([sum(ALPHA[:i]) % 70 for i in range(1, 6)], [1, 21, 45, 17, 8])
        self.assertEqual(sum(ALPHA) % 70, 0)
        for n, a, _ in MULTIPLICATION_POWERS:
            self.assertIn((n, a), admissible_multiplications())
            self.assertTrue(all(k * a % 70 for k in range(1, n + 1)))
            h = 70 // n
            self.assertTrue(all(a and h * j % 70 and (a + h * j) % 70
                                for j in range(1, n)))
        # Four binary Jacobi factors, then one reflection for the full sextuple.
        terms = [(1, exponent_vector([(sum(ALPHA[:i]) % 70, 1), (ALPHA[i], 1),
                                      (sum(ALPHA[:i + 1]) % 70, -1)]))
                 for i in range(1, 5)]
        terms.append((1, reflection(8)))
        self.assertEqual(linear_combination(terms), exponent_vector([(a, 1) for a in ALPHA]))

    def test_certificate_negative_controls(self) -> None:
        original = certificate_vector()
        for n, a, power in MULTIPLICATION_POWERS:
            altered = linear_combination([(1, original), (-power, multiplication(n, a))])
            self.assertNotEqual(altered, tuple(2 * x for x in target_vector()))
        wrong = list(ALPHA)
        wrong[0] += 1
        self.assertNotEqual(original[:69], tuple(2 * x for x in exponent_vector([(a, 1) for a in wrong])[:69]))

    def test_all_parity_relations(self) -> None:
        for a in range(1, 70):
            self.assertEqual(epsilon(reflection(a)), 0)
        for n, a in admissible_multiplications():
            self.assertEqual(epsilon(multiplication(n, a)), 0, (n, a))
            h = 70 // n
            selected_numerator = sum((a + h * j) % 70 in SELECTED for j in range(n))
            selected_denominator = sum(h * j % 70 in SELECTED for j in range(1, n))
            if n % 5:
                self.assertEqual(selected_numerator, int(n * a % 70 in SELECTED))
                self.assertEqual(selected_denominator, 0)
            else:
                self.assertEqual(selected_numerator, 0)
                self.assertNotIn(n * a % 70, SELECTED)
                self.assertEqual(selected_denominator, 4)
        self.assertEqual(epsilon(target_vector()), 1)
        self.assertEqual(epsilon(certificate_vector()), 0)

    def test_every_unit_conjugate(self) -> None:
        for u in UNITS:
            changed = [0] * 70
            for a in range(1, 70):
                changed[(u * a % 70) - 1] = certificate_vector()[a - 1]
            changed[-1] = certificate_vector()[-1]
            expected = list(exponent_vector([(u * a, 2) for a in ALPHA]))
            expected[-1] = -6
            self.assertEqual(changed, expected)
            self.assertEqual(sum((u * a % 70) in SELECTED for a in ALPHA) % 2, 1)

    def test_complete_cocycle_case_dictionary(self) -> None:
        counts = cocycle_case_audit()
        self.assertEqual(sum(counts.values()), 70 ** 3)
        self.assertEqual(len(counts), 6)
        self.assertTrue(all(count > 0 for count in counts.values()))

    def test_secondary_surface_profiles(self) -> None:
        rows = surface_census()
        self.assertEqual(len(rows), 10)
        self.assertEqual(sum(row["hodge_numbers_20_11_02"] == [1, 22, 1] for row in rows), 3)
        for row in rows:
            self.assertEqual(tuple(x + y for x, y in zip(row["left_profile"], row["right_profile"])), (4,) * 24)
        beta, gamma = (1, 42, 61, 36), (25, 23, 4, 18)
        self.assertEqual(tuple(sum(u * a % 70 for a in beta) // 70 for u in UNITS),
                         tuple(sum(u * a % 35 for a in gamma) // 35 for u in UNITS))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Verification))
    record = {
        "checkpoint": "U42", "base_commit": "489b743689ac96345ea56ec49f4a1568623236cc",
        "python": sys.version, "platform": platform.platform(),
        "arithmetic": "exact Python integers; no floating-point mathematics",
        "passed": result.wasSuccessful(), "test_count": result.testsRun,
        "failures": len(result.failures), "errors": len(result.errors),
        "runtime_seconds": time.monotonic() - start,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "target": ALPHA, "unit_count": len(UNITS),
        "certificate_reflection_powers": REFLECTION_POWERS,
        "certificate_multiplication_powers": MULTIPLICATION_POWERS,
        "certificate_residual": tuple(x - 2 * y for x, y in zip(certificate_vector(), target_vector())),
        "parity_selected_residues": SELECTED,
        "all_admissible_DH_count": len(admissible_multiplications()),
        "DH_counts_by_divisor": dict(Counter(n for n, _ in admissible_multiplications())),
        "cocycle_case_dictionary": cocycle_case_audit(), "secondary_surface_census": surface_census(),
        "non_claims": ["Code does not verify the Chow-correspondence theorems",
                       "Code does not prove the source-to-motive argument",
                       "No unsquared target cycle or full Hodge solution is constructed"]}
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
