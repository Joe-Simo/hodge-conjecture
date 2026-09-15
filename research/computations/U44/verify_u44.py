"""Check U44's finite certificates using exact Python integers.

This does not prove the Hodge conjecture, verify Chow-motive theorems, or
classify arbitrary algebraic cycles. No discovery code is imported.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from functools import cache
from hashlib import sha256
from itertools import combinations_with_replacement
import json
from math import gcd
from pathlib import Path
import platform
from struct import Struct
import sys
import time
import unittest

ALPHA = (1, 20, 24, 42, 61, 62)
SQUARE_R = ((1, 1), (4, 1), (9, 1), (16, 1), (22, -1),
            (24, 2), (26, 1), (28, -1), (30, 1))
SQUARE_D = ((2, 1, 1), (2, 9, -1), (2, 26, 1), (2, 34, -1),
            (5, 4, -1), (5, 6, 1), (5, 12, -1), (7, 2, 1), (7, 6, -1))


def order(m: int, a: int) -> int:
    if m < 2 or a % m == 0:
        raise ValueError("Require a nonzero character at level m >= 2")
    return m // gcd(m, a)


def epsilon(m: int, d: int, a: int) -> int:
    """Indicator of nonzero elements in the subgroup of size d."""
    if d < 1 or m % d:
        raise ValueError("Subgroup order must divide the level")
    return int(a % m != 0 and d % order(m, a) == 0)


def psi(m: int, a: int) -> int:
    """The level-420 dual certificate, also evaluated on level-105 seeds."""
    return int(order(m, a) in (7, 21))


def divisors(m: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, m + 1) if m % d == 0)


def dh_terms(m: int, n: int, a: int) -> tuple[tuple[int, int], ...]:
    if n < 2 or m % n or (n * a) % m == 0:
        raise ValueError("Require n > 1, n | m, and n*a nonzero modulo m")
    terms = (tuple(((a + j * (m // n)) % m, 1) for j in range(n))
             + (((n * a) % m, -1),)
             + tuple((j * (m // n), -1) for j in range(1, n)))
    if any(a0 == 0 for a0, _ in terms):
        raise AssertionError("Admissibility failed to exclude a zero symbol")
    return terms


def half_units(m: int) -> tuple[int, ...]:
    return tuple(u for u in range(1, (m + 1) // 2) if gcd(u, m) == 1)


def hodge_test(m: int, tup: tuple[int, ...]) -> bool:
    if m < 2 or not tup or len(tup) % 2 or any(a <= 0 or a >= m for a in tup):
        return False
    return all(sum(u * a % m for a in tup) == (len(tup) // 2) * m
               for u in range(1, m) if gcd(u, m) == 1)


@cache
def hodge_tuples(m: int, half_length: int) -> tuple[tuple[int, ...], ...]:
    """Complete sorted Hodge tuples; split at the middle, match all profiles.

    Used only for quadruples (m<=420) and sextuples (m=105). The output is
    independent of dictionary insertion order and includes repetitions.
    """
    if not (3 <= m <= 420 and half_length in (2, 3)):
        raise ValueError("Unsupported audited range")
    if half_length == 3 and m > 105:
        raise ValueError("Sextuple census is bounded by level 105")
    units = half_units(m)
    residues = {a: tuple(u * a % m for u in units) for a in range(1, m)}
    codec = Struct("<" + "H" * len(units))
    grouped: dict[bytes, list[tuple[int, ...]]] = defaultdict(list)
    for block in combinations_with_replacement(range(1, m), half_length):
        profile = tuple(sum(row) for row in zip(*(residues[a] for a in block)))
        grouped[codec.pack(*profile)].append(block)
    answer: list[tuple[int, ...]] = []
    for key, lefts in grouped.items():
        complement = tuple(half_length * m - v for v in codec.unpack(key))
        if any(v <= 0 for v in complement):
            continue
        rights = grouped.get(codec.pack(*complement), ())
        for left in lefts:
            for right in rights:
                if left[-1] <= right[0]:
                    answer.append(left + right)
    result = tuple(sorted(answer))
    if len(result) != len(set(result)):
        raise AssertionError("Duplicate middle split")
    return result


@cache
def curve_groups() -> tuple[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]], ...]:
    """All sorted nonzero triples with zero sum modulo 420, by Hodge profile."""
    m = 420
    grouped: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for a in range(1, m):
        for b in range(a, m):
            c = (-a - b) % m
            if c < b:
                continue
            tup = (a, b, c)
            key = tuple(sum(u * x % m for x in tup) // m for u in half_units(m))
            grouped[key].append(tup)
    return tuple((key, tuple(val)) for key, val in sorted(grouped.items()))


def square_residual(k: int) -> tuple[int, ...]:
    """Lift and check the U42 square identity coefficient-by-coefficient."""
    m = 70 * k
    residual: Counter[int] = Counter()  # zero indexes the Lefschetz symbol
    for a, coefficient in SQUARE_R:
        residual[k * a] += coefficient
        residual[m - k * a] += coefficient
        residual[0] -= coefficient
    for n, a, coefficient in SQUARE_D:
        for idx, sign in dh_terms(m, n, k * a):
            residual[idx] += coefficient * sign
    for a in ALPHA:
        residual[k * a] -= 2
    residual[0] += 6
    return tuple(residual[i] for i in range(m))


def tuple_hash(tuples: tuple[tuple[int, ...], ...]) -> str:
    payload = "".join(",".join(map(str, t)) + "\n" for t in tuples)
    return sha256(payload.encode("ascii")).hexdigest()


class U44Tests(unittest.TestCase):
    def test_01_domains_and_necessary_hypotheses(self) -> None:
        with self.assertRaises(ValueError):
            order(70, 0)
        with self.assertRaises(ValueError):
            dh_terms(70, 5, 14)
        with self.assertRaises(ValueError):
            dh_terms(70, 3, 1)
        self.assertFalse(hodge_test(70, ()))
        self.assertFalse(hodge_test(1, (1, 1)))
        # Even subgroup: the oddness hypothesis really matters.
        self.assertEqual(sum(c * epsilon(6, 2, a) for a, c in dh_terms(6, 2, 1)) % 2, 1)
        # Non-direct-factor subgroup: coprimality really matters.
        self.assertEqual(sum(c * epsilon(9, 3, a) for a, c in dh_terms(9, 3, 1)) % 2, 1)

    def test_02_small_uniform_lemma_benchmarks(self) -> None:
        for m in range(3, 57):
            for d in divisors(m):
                if d % 2 == 0 or gcd(d, m // d) != 1:
                    continue
                for a in range(1, m):
                    self.assertEqual((epsilon(m, d, a) + epsilon(m, d, m - a)) % 2, 0)
                for n in divisors(m)[1:]:
                    for a in range(1, m):
                        if (n * a) % m:
                            self.assertEqual(sum(c * epsilon(m, d, j)
                                                 for j, c in dh_terms(m, n, a)) % 2, 0)

    def test_03_scaling_and_square_certificate(self) -> None:
        for k in (1, 2, 3, 6, 11, 49, 70):
            self.assertEqual(set(square_residual(k)), {0})
            for u in range(1, 70):
                if gcd(u, 70) != 1:
                    continue
                orders = tuple(order(70 * k, k * (u * a % 70)) for a in ALPHA)
                self.assertEqual(orders, (70, 7, 35, 5, 70, 35))
                for prime in (5, 7):
                    def primary(n: int) -> int:
                        while n % prime == 0:
                            n //= prime
                        return int(n == 1)
                    self.assertEqual(sum(primary(n) for n in orders) % 2, 1)

    def test_04_complete_level420_multiplication_set(self) -> None:
        count = 0
        for a in range(1, 420):
            self.assertEqual((psi(420, a) + psi(420, 420 - a)) % 2, 0)
            self.assertEqual(psi(420, a), (epsilon(420, 21, a) + epsilon(420, 3, a)) % 2)
        for n in divisors(420)[1:]:
            for a in range(1, 420):
                if n * a % 420:
                    count += 1
                    self.assertEqual(sum(c * psi(420, b) for b, c in dh_terms(420, n, a)) % 2, 0)
        self.assertEqual(count, 8317)
        self.assertEqual(sum(psi(420, 6 * a) for a in ALPHA) % 2, 1)

    def test_05_surface_census_complete_and_parity(self) -> None:
        tuples = hodge_tuples(420, 2)
        self.assertEqual(len(tuples), 23307)
        self.assertTrue(all(sum(psi(420, a) for a in t) % 2 == 0 for t in tuples))
        # Recheck all units, not just the profiles used to discover tuples.
        self.assertTrue(all(hodge_test(420, t) for t in tuples))

    def test_06_curve_products_complete_and_parity(self) -> None:
        groups = curve_groups()
        self.assertEqual(sum(len(val) for _, val in groups), 29400)
        self.assertEqual(len(groups), 27404)
        for _, tuples in groups:
            parities = {sum(psi(420, a) for a in t) % 2 for t in tuples}
            self.assertEqual(len(parities), 1)
        # Opposite profiles pair; negation preserves the certificate value.
        lookup = dict(groups)
        for key, val in groups:
            opposite = tuple(3 - v for v in key)
            self.assertIn(opposite, lookup)
            self.assertEqual(len(val), len(lookup[opposite]))
            self.assertEqual(sum(psi(420, a) for a in val[0]) % 2,
                             sum(psi(420, a) for a in lookup[opposite][0]) % 2)

    def test_07_all_degree105_sextuple_seeds(self) -> None:
        tuples = hodge_tuples(105, 3)
        self.assertEqual(len(tuples), 27690)
        self.assertTrue(all(sum(psi(420, 4 * a) for a in t) % 2 == 0 for t in tuples))
        self.assertTrue(all(hodge_test(105, t) for t in tuples))

    def test_08_independent_small_direct_censuses(self) -> None:
        for m in (6, 10, 15, 20):
            brute = tuple(t for t in combinations_with_replacement(range(1, m), 4)
                          if hodge_test(m, t))
            self.assertEqual(hodge_tuples(m, 2), brute)
        self.assertEqual(hodge_tuples(7, 3), tuple(
            t for t in combinations_with_replacement(range(1, 7), 6) if hodge_test(7, t)))

    def test_09_divisors_can_break_primary_parity(self) -> None:
        beta = (1, 4, 18, 19)
        self.assertTrue(hodge_test(21, beta))
        lifted = tuple(20 * a for a in beta)
        self.assertEqual(sum(epsilon(420, 7, a) for a in lifted) % 2, 1)
        self.assertEqual(sum(psi(420, a) for a in lifted) % 2, 0)
        # Intentional wrong claim is rejected, rather than used as a theorem.
        self.assertFalse(all(sum(epsilon(420, 7, a) for a in t) % 2 == 0
                             for t in hodge_tuples(420, 2)))


def report() -> dict[str, object]:
    surfaces = hodge_tuples(420, 2)
    sextuples = hodge_tuples(105, 3)
    groups = curve_groups()
    ordered = sum(len(val) ** 2 for _, val in groups)
    return {
        "status": "exact finite certificates checked; no algebraicity or nonalgebraicity claim",
        "python": platform.python_version(),
        "arithmetic": "unbounded Python integers; F2 parity via integer remainder",
        "level": 420,
        "target": [6 * a for a in ALPHA],
        "dual_functional": "1 iff additive order is 7 or 21; ell -> 0",
        "target_value": 1,
        "reflection_count_including_duplicate_signs": 419,
        "all_admissible_multiplication_count": 8317,
        "hodge_quadruples_sorted": len(surfaces),
        "hodge_quadruples_sha256": tuple_hash(surfaces),
        "curve_triples_sorted": sum(len(val) for _, val in groups),
        "curve_hodge_profile_groups": len(groups),
        "all_ordered_hodge_pairs_of_curve_triples": ordered,
        "all_unordered_hodge_pairs_of_curve_triples": ordered // 2,
        "degree105_hodge_sextuples_sorted": len(sextuples),
        "degree105_hodge_sextuples_sha256": tuple_hash(sextuples),
        "seed_parity_failures": 0,
        "new_tests": 9,
        "scope": "finite seed result only at level420; R/D-only theorem holds at all70k by separate proof",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(U44Tests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        return 1
    out = report()
    out["runtime_seconds"] = time.perf_counter() - started
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
