"""Exact U43 certificate checker; not a verifier of the external Chow theorems.

Uses only the Python standard library. All arithmetic is integral. The finite
population is all 24 units and all 576 ordered pairs at level 70. The discovery
Smith calculation is deliberately not imported or needed by this checker.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
import time
import unittest
from pathlib import Path

M = 70
ALPHA = (1, 20, 24, 42, 61, 62)
UNITS = tuple(u for u in range(1, M) if math.gcd(u, M) == 1)
Vector = tuple[int, ...]
ZERO: Vector = (0,) * M
NEW_R = ((8, -2), (10, 1), (11, -1), (12, -1), (13, 1),
         (14, 2), (20, -2), (21, 1), (22, 1), (24, -1),
         (26, -1), (29, 1), (30, 1), (34, -1), (35, 1))
NEW_D = ((2, 1, 1), (2, 5, -1), (2, 7, -1), (2, 8, 2),
         (2, 10, -1), (2, 11, 2), (2, 13, -1), (2, 14, -1),
         (2, 15, 2), (2, 16, 1), (2, 17, -1), (5, 1, -1),
         (5, 2, 1), (5, 3, 1), (7, 1, -1), (7, 2, 1))
# Copied explicitly from the pinned U42 proof, not from its implementation.
SQUARE_R = ((1, 1), (4, 1), (9, 1), (16, 1), (22, -1),
            (24, 2), (26, 1), (28, -1), (30, 1))
SQUARE_D = ((2, 1, 1), (2, 9, -1), (2, 26, 1), (2, 34, -1),
            (5, 4, -1), (5, 6, 1), (5, 12, -1), (7, 2, 1), (7, 6, -1))


def combine(terms: list[tuple[int, Vector]]) -> Vector:
    if any(len(v) != M for _, v in terms):
        raise ValueError("A vector must have 69 character coordinates and ell")
    return tuple(sum(c * v[i] for c, v in terms) for i in range(M))


def vector(terms: list[tuple[int, int]], ell: int = 0) -> Vector:
    v = [0] * M
    for a, c in terms:
        a %= M
        if a == 0:
            raise ValueError("No primitive e_0 symbol is permitted")
        v[a - 1] += c
    v[-1] = ell
    return tuple(v)


def reflection(a: int) -> Vector:
    return vector([(a, 1), (-a, 1)], ell=-1)


def multiplication(n: int, a: int) -> Vector:
    if n <= 1 or M % n != 0 or n * a % M == 0:
        raise ValueError("Inadmissible Davenport-Hasse relation")
    h = M // n
    return vector([(a + j * h, 1) for j in range(n)]
                  + [(n * a, -1)] + [(j * h, -1) for j in range(1, n)])


def target(u: int) -> Vector:
    if math.gcd(u, M) != 1:
        raise ValueError("Transport requires a unit modulo 70")
    return vector([(u * a, 1) for a in ALPHA], ell=-3)


def transport(v: Vector, u: int) -> Vector:
    if len(v) != M or math.gcd(u, M) != 1:
        raise ValueError("Invalid vector or nonunit transport")
    return vector([(u * a, v[a - 1]) for a in range(1, M)], v[-1])


def evaluate_certificate(r_terms: tuple[tuple[int, int], ...],
                         d_terms: tuple[tuple[int, int, int], ...]) -> Vector:
    return combine([(c, reflection(a)) for a, c in r_terms]
                   + [(c, multiplication(n, a)) for n, a, c in d_terms])


def difference_certificates() -> dict[int, Vector]:
    """Construct witnesses by paths in <3,-1>; never solve for a witness."""
    step = evaluate_certificate(NEW_R, NEW_D)
    square = evaluate_certificate(SQUARE_R, SQUARE_D)
    flip = combine([(1, reflection(a)) for a in ALPHA] + [(-1, square)])
    powers = tuple(pow(3, k, M) for k in range(12))
    result = {1: ZERO}
    for k in range(11):
        u, nxt = powers[k], powers[k + 1]
        result[nxt] = combine([(1, result[u]), (1, transport(step, u))])
    for u in powers:
        result[-u % M] = combine([(1, result[u]), (1, transport(flip, u))])
    return result


def parity(v: Vector) -> int:
    return sum(v[a - 1] for a in (14, 28, 42, 56)) % 2


class U43Tests(unittest.TestCase):
    def test_new_integral_certificate_and_negative_control(self) -> None:
        actual = evaluate_certificate(NEW_R, NEW_D)
        expected = combine([(1, target(3)), (-1, target(1))])
        self.assertEqual(actual, expected)
        self.assertEqual(sum(c for _, c in NEW_R), 0)
        self.assertEqual(len(NEW_R) + len(NEW_D), 31)
        self.assertNotEqual(combine([(1, actual), (1, reflection(8))]), expected)

    def test_inherited_square_certificate(self) -> None:
        self.assertEqual(evaluate_certificate(SQUARE_R, SQUARE_D),
                         combine([(2, target(1))]))

    def test_geometric_admissibility_at_every_used_transport(self) -> None:
        for n, a, _ in NEW_D + SQUARE_D:
            for u in UNITS:
                self.assertTrue(all(j * u * a % M for j in range(1, n + 1)))
                self.assertEqual(transport(multiplication(n, a), u),
                                 multiplication(n, u * a))
        for a, _ in NEW_R + SQUARE_R:
            for u in UNITS:
                self.assertEqual(transport(reflection(a), u), reflection(u * a))

    def test_generators_cover_exactly_all_units(self) -> None:
        powers = {pow(3, k, M) for k in range(12)}
        self.assertEqual(len(powers), 12)
        self.assertEqual(pow(3, 12, M), 1)
        self.assertNotIn(M - 1, powers)
        self.assertEqual(powers | {-u % M for u in powers}, set(UNITS))

    def test_all_24_conjugate_difference_certificates(self) -> None:
        certs = difference_certificates()
        self.assertEqual(set(certs), set(UNITS))
        for u, cert in certs.items():
            self.assertEqual(cert, combine([(1, target(u)), (-1, target(1))]))
        step = evaluate_certificate(NEW_R, NEW_D)
        self.assertEqual(combine([(1, transport(step, pow(3, k, M)))
                                  for k in range(12)]), ZERO)

    def test_all_576_mixed_tensor_certificates(self) -> None:
        certs = difference_certificates()
        square = evaluate_certificate(SQUARE_R, SQUARE_D)
        count = 0
        for u in UNITS:
            for v in UNITS:
                self.assertEqual(combine([(1, square), (1, certs[u]), (1, certs[v])]),
                                 combine([(1, target(u)), (1, target(v))]))
                count += 1
        self.assertEqual(count, 576)

    def test_hodge_types_and_projector_dimensions(self) -> None:
        orbit = {tuple(u * a % M for a in ALPHA) for u in UNITS}
        self.assertEqual(len(orbit), 24)
        self.assertEqual({sum(a) for a in orbit}, {210})
        for a in orbit:
            partial = 0
            for term in a[:-1]:
                partial = (partial + term) % M
                self.assertNotEqual(partial, 0)
        self.assertEqual(len({(a, b) for a in orbit for b in orbit}), 576)

    def test_no_single_target_from_the_same_relation_presentation(self) -> None:
        relations = [reflection(a) for a in range(1, M)]
        relations += [multiplication(n, a) for n in range(2, M + 1) if M % n == 0
                      for a in range(1, M) if n * a % M]
        self.assertTrue(all(parity(r) == 0 for r in relations))
        self.assertTrue(all(parity(target(u)) == 1 for u in UNITS))

    def test_diagonal_restriction_retains_only_opposite_pairs(self) -> None:
        survivors = {(u, v) for u in UNITS for v in UNITS
                     if all((u + v) * a % M == 0 for a in ALPHA)}
        self.assertEqual(survivors, {(u, -u % M) for u in UNITS})
        self.assertEqual(len(survivors), 24)
        self.assertFalse(any((u, u) in survivors for u in UNITS))

    def test_reject_invalid_inputs(self) -> None:
        for action in (lambda: vector([(0, 1)]), lambda: multiplication(3, 1),
                       lambda: multiplication(2, 35), lambda: target(5),
                       lambda: transport(ZERO, 5), lambda: combine([(1, (0,))])):
            with self.assertRaises(ValueError):
                action()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(U43Tests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if args.output is not None:
        summary = {
            "claim": "Integral certificate and all unit/pair transports, not a Chow proof",
            "modulus": M, "alpha": ALPHA, "arithmetic": "exact Python integers",
            "tested_units": UNITS, "ordered_pairs_checked": 576,
            "new_certificate_terms": len(NEW_R) + len(NEW_D),
            "new_certificate_L1_norm": sum(abs(c) for _, c in NEW_R)
                + sum(abs(c) for _, _, c in NEW_D),
            "tests_run": result.testsRun, "success": result.wasSuccessful(),
            "python": platform.python_version(), "platform": platform.platform(),
            "runtime_seconds": round(time.monotonic() - start, 6), "seed": None,
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "limits": "No formal or expert verification; source theorem applications reviewed in prose",
        }
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
