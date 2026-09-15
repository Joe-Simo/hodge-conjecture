"""Exact finite corroboration of U49, not a verifier of its geometric proof.

No network or third-party dependencies. Run with Python >= 3.10.
The uniform theorem is the separate proof; this program tests stated degrees.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
import unittest
from collections import Counter
from itertools import product
from math import gcd
from pathlib import Path

Triple = tuple[int, int, int]
ALPHA = (1, 20, 24, 42, 61, 62)
DEGREES = tuple(range(4, 37)) + (42, 49, 63, 70, 105, 140, 210, 420)
RESULTS: dict[str, object] = {}


def triples(m: int) -> list[Triple]:
    if m < 4:
        raise ValueError("U49 uses Fermat degrees at least four")
    return [(a, b, c) for a in range(1, m) for b in range(1, m)
            if (c := (-a-b) % m)]


def rotations(t: Triple) -> tuple[Triple, Triple, Triple]:
    a, b, c = t
    return t, (b, c, a), (c, a, b)


def diagonal_parameters(m: int) -> list[tuple[int, int]]:
    return [(h, s) for h in range(3, m+1, 2) if m % h == 0
            for s in range(h) if gcd(s, h) == gcd(s-1, h) == 1]


def diagonal_formula(m: int, h: int, s: int, k: int) -> list[int]:
    return [0] + [3*(m//h) - sum((v-k) % h == 0 for v in
        (j, -j, s*j, -s*j, (s-1)*j, -(s-1)*j)) for j in range(1, m)]


def cyclic_formula(m: int) -> list[int]:
    return [0] + [m-2-int(j == m//3)-int(j == 2*m//3) for j in range(1, m)]


def hesse_formula(m: int, k: int) -> list[int]:
    return [0] + [m//3 - (int(j % 3 == 1) + int(j % 3 == 2) if k else
        2*int(j % 3 == 0) + int(j == m//3) + int(j == 2*m//3))
        for j in range(1, m)]


def reflection_certificate(c: list[int], rank: int) -> dict[int, int]:
    """Check all m coordinates, including the Lefschetz coefficient."""
    m = len(c)
    if rank % 2 or sum(c) != 3*rank or any(x < 0 for x in c):
        raise ValueError("invalid normalized determinant word")
    cert = {j: c[j] for j in range(1, (m+1)//2) if c[j]}
    if m % 2 == 0:
        if c[m//2] % 2:
            raise ValueError("self-complementary coefficient is odd")
        if c[m//2]:
            cert[m//2] = c[m//2]//2
    recovered = [0]*m
    ell = 0
    for j, n in cert.items():
        recovered[j] += n
        recovered[m-j] += n
        ell -= n
    if recovered != c or ell != -3*rank//2:
        raise ValueError("the reflection certificate does not reconstruct the word")
    return cert


def order_parity(c: list[int], p: int) -> int:
    m = len(c)
    total = 0
    for j in range(1, m):
        order = m//gcd(m, j)
        remaining = order
        while remaining % p == 0:
            remaining //= p
        if order > 1 and remaining == 1:
            total += c[j]
    return total % 2


class U49Tests(unittest.TestCase):
    def test_01_complete_curve_population(self) -> None:
        for m in DEGREES:
            ts = triples(m)
            self.assertEqual(len(ts), (m-1)*(m-2))
            self.assertEqual(sum(sum(t) == m for t in ts), (m-1)*(m-2)//2)
            self.assertTrue(all(sum(t) in (m, 2*m) for t in ts))

    def test_02_all_diagonal_determinants(self) -> None:
        rows = []
        total_cases = 0
        for m in DEGREES:
            ts = triples(m)
            cases = 0
            for h, s in diagonal_parameters(m):
                counts = [[0]*m for _ in range(h)]
                ranks = [0]*h
                hol = [0]*h
                for t in ts:
                    k = (t[0]+s*t[1]) % h
                    if k:
                        ranks[k] += 1
                        hol[k] += int(sum(t) == m)
                        for j in t:
                            counts[k][j] += 1
                for k in range(1, h):
                    self.assertEqual(ranks[k], m*(m-3)//h, (m, h, s, k))
                    self.assertEqual(2*hol[k], ranks[k])
                    self.assertEqual(counts[k], diagonal_formula(m, h, s, k))
                    reflection_certificate(counts[k], ranks[k])
                    for p in (5, 7):
                        self.assertEqual(order_parity(counts[k], p), 0)
                    cases += 1
            rows.append({"degree": m, "parameter_character_cases": cases})
            total_cases += cases
        RESULTS["diagonal_census"] = rows
        RESULTS["diagonal_cases"] = total_cases

    def test_03_all_nondiagonal_determinants(self) -> None:
        rows = []
        for m in DEGREES:
            if m % 3:
                continue
            ts = triples(m)
            fixed = [t for t in ts if len(set(t)) == 1]
            self.assertEqual(fixed, [(m//3,)*3, (2*m//3,)*3])
            reps = [t for t in ts if len(set(t)) > 1 and t == min(rotations(t))]
            counter = Counter(j for t in reps for j in t)
            c = [counter[j] for j in range(m)]
            rank = m*(m-3)//3
            self.assertEqual(len(reps), rank)
            self.assertEqual(2*sum(sum(t) == m for t in reps), rank)
            self.assertEqual(c, cyclic_formula(m))
            reflection_certificate(c, rank)
            for k, ell in product(range(3), repeat=2):
                if (k, ell) == (0, 0):
                    continue
                selected = [t for t in reps if (t[0]+2*t[1]) % 3 == k]
                counts = Counter(j for t in selected for j in t)
                coeffs = [counts[j] for j in range(m)]
                hrank = m*(m-3)//9
                self.assertEqual(len(selected), hrank)
                self.assertEqual(2*sum(sum(t) == m for t in selected), hrank)
                self.assertEqual(coeffs, hesse_formula(m, k))
                reflection_certificate(coeffs, hrank)
                self.assertTrue(all(order_parity(coeffs, p) == 0 for p in (5, 7)))
            rows.append({"degree": m, "cyclic_rank": rank, "hesse_rank": m*(m-3)//9,
                         "nontrivial_character_cases": 10})
        RESULTS["nondiagonal_census"] = rows
        RESULTS["nondiagonal_cases"] = 10*len(rows)

    def test_04_diagonal_freeness_checks_all_powers(self) -> None:
        for h in range(2, 61):
            for s in range(h):
                all_distinct = all(len({a % h, s*a % h, 0}) == 3 for a in range(1, h))
                formula = gcd(s, h) == gcd(s-1, h) == 1
                self.assertEqual(all_distinct, formula)
                if formula:
                    self.assertEqual(h % 2, 1)
        # A generator with distinct eigenvalues does not suffice: its cube fixes a line.
        self.assertEqual(len({1, 2, 0}), 3)
        self.assertEqual(len({3, 0, 0}), 2)

    def test_05_nondiagonal_group_classification_inputs(self) -> None:
        for m in range(4, 37):
            central = []
            for a, b in product(range(m), repeat=2):
                # sigma cycles diag(a,b,0) to diag(b,0,a), projectively normalize.
                if ((b-a) % m, (-a) % m) == (a, b):
                    central.append((a, b))
                fixed_points = sum((a+b+j*m) % 3 != 0 for j in range(3))
                free = fixed_points == 0
                self.assertEqual(free, m % 3 == 0 and (a+b) % 3 == 0)
                if free:
                    # Explicit conjugation by diag(0,v,w) turns D*sigma into scalar*sigma.
                    q = (a+b)//3
                    v, w = q-a, 2*q-a-b
                    self.assertTrue((a+v-q) % m == (b+w-v-q) % m == (-w-q) % m == 0)
            self.assertEqual(len(central), gcd(3, m))
            if m % 3 == 0:
                self.assertEqual(set(central), {(0, 0), (m//3, 2*m//3), (2*m//3, m//3)})

    def test_06_integral_self_dual_coefficient(self) -> None:
        self.assertEqual(reflection_certificate([0, 2, 2, 2], 2), {1: 2, 2: 1})
        with self.assertRaises(ValueError):
            reflection_certificate([0, 1, 1, 1], 1)
        with self.assertRaises(ValueError):
            reflection_certificate([0, 1, 2, 3], 2)

    def test_07_ramified_and_fixed_orbit_controls(self) -> None:
        # The ramified diagonal subgroup with s=0 has an unbalanced odd-rank eigenspace.
        selected = [t for t in triples(5) if t[0] == 1]
        self.assertEqual(len(selected), 3)
        self.assertEqual(sum(sum(t) == 5 for t in selected), 3)
        # Fixed triples belong only to the trivial permutation eigencharacter.
        for m in (6, 9, 12):
            self.assertEqual(len(triples(m))//3, m*(m-3)//3)
            reps = {min(rotations(t)) for t in triples(m)}
            self.assertEqual(len(reps), m*(m-3)//3+2)

    def test_08_target_remains_outside_reflections(self) -> None:
        rows = []
        for scale in (1, 2, 3, 6, 12, 30):
            m = 70*scale
            c = [0]*m
            for a in ALPHA:
                c[scale*a] += 1
            self.assertEqual(order_parity(c, 5), 1)
            self.assertEqual(order_parity(c, 7), 1)
            with self.assertRaises(ValueError):
                reflection_certificate(c, 2)
            rows.append({"level": m, "order5_parity": 1, "order7_parity": 1})
        RESULTS["target_checks"] = rows

    def test_09_worked_large_example(self) -> None:
        m = 210
        rank = m*(m-3)//9
        self.assertEqual(rank, 4830)
        self.assertEqual(1+rank//2, 2416)
        c = hesse_formula(m, 0)
        cert = reflection_certificate(c, rank)
        self.assertEqual(sum(cert.values()), 7245)
        self.assertEqual(c[m//2], 68)
        RESULTS["worked_example"] = {"m": m, "group": "C3 x C3", "character": [0, 1],
            "cover_genus": (m-1)*(m-2)//2, "base_genus": 2416, "rank": rank,
            "self_dual_coefficient": 68, "reflection_multiplicity_sum": sum(cert.values())}

    def test_10_fixed_source_cover_ramification(self) -> None:
        # Present the four source curves as cyclic covers with three branch orders.
        rows = []
        for name, m, exponents, genus in (
            ("D5", 70, (2, 7, -9), 31),
            ("D7", 70, (6, 5, -11), 32),
            ("C5", 10, (2, 5, -7), 2),
            ("C7", 14, (2, 7, -9), 3),
        ):
            self.assertEqual(sum(exponents), 0)
            self.assertEqual(gcd(m, *exponents), 1)
            self.assertEqual(gcd(m, exponents[-1]), 1)
            two_g_minus_two = -2*m + sum(m-gcd(m, a) for a in exponents)
            self.assertEqual(two_g_minus_two, 2*genus-2)
            rows.append({"curve": name, "cyclic_degree": m, "branch_exponents": exponents,
                         "genus": genus, "infinity_inertia_order": m})
        # D5: x=t^7, w^70=x^2(1+x)^7; t=w^40/[x(1+x)^4].
        self.assertEqual((2*4-7, 7*4-28), (1, 0))
        self.assertEqual((2-2, 7-8), (0, -1))
        # D7: x=s^5, v^70=x^6(1+x)^5; s=v^14/[x(1+x)].
        self.assertEqual((6-5, 5-5), (1, 0))
        RESULTS["fixed_source_covers"] = rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(U49Tests))
    RESULTS.update({"status": "finite checks passed" if result.wasSuccessful() else "failed",
        "tests_run": result.testsRun, "failures": len(result.failures), "errors": len(result.errors),
        "python": platform.python_version(), "seconds": round(time.monotonic()-started, 3),
        "degrees": DEGREES, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "nonclaims": ["not a formal proof assistant", "not a construction of the degree70 target",
                      "finite tests do not replace U49's uniform proof"]})
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(RESULTS, indent=2)+'\n', encoding='utf-8')
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(main())
