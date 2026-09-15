"""Verify the finite certificate behind U45, using exact integers only.

The checker does not import discovery code, prove the geometric Hodge
conjecture, or verify an external Chow-motive theorem. The unbounded
integer-word conclusion is proved separately in U45 from this certificate.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import cache
from hashlib import sha256
from itertools import chain
import json
from math import gcd
from pathlib import Path
import platform
import sys
import time
import unittest

LEVEL = 420
ALPHA = (1, 20, 24, 42, 61, 62)
DUAL_UNITS = (11, 23, 37, 59, 71)
SQUARE_R = ((1, 1), (4, 1), (9, 1), (16, 1), (22, -1),
            (24, 2), (26, 1), (28, -1), (30, 1))
SQUARE_D = ((2, 1, 1), (2, 9, -1), (2, 26, 1), (2, 34, -1),
            (5, 4, -1), (5, 6, 1), (5, 12, -1), (7, 2, 1), (7, 6, -1))
BOUNDARY_WORD = ((24, 61, 55), (20, 15, 35), (35, 42, 63), (7, 62, 1))
Triple = tuple[int, int, int]


def units(m: int) -> tuple[int, ...]:
    if m < 2:
        raise ValueError("The level must be at least two")
    return tuple(u for u in range(1, m) if gcd(u, m) == 1)


def profile(m: int, beta: Triple) -> bytes:
    if len(beta) != 3 or any(not 0 < a < m for a in beta) or sum(beta) % m:
        raise ValueError("Require three nonzero residues with zero sum modulo m")
    return bytes(sum(u * a % m for a in beta) // m - 1 for u in units(m))


def psi(m: int, a: int) -> int:
    if not 0 < a < m:
        raise ValueError("Zero and out-of-range formal symbols are excluded")
    return int(m // gcd(m, a) in (7, 21))


def triples() -> tuple[Triple, ...]:
    """Independent coverage: split by the two possible ordinary sums."""
    found: list[Triple] = []
    for total in (LEVEL, 2 * LEVEL):
        for a in range(1, LEVEL):
            for b in range(a, LEVEL):
                c = total - a - b
                if b <= c < LEVEL:
                    found.append((a, b, c))
    return tuple(sorted(found))


@cache
def census() -> tuple[dict[Triple, bytes], dict[bytes, int], dict[bytes, int], Counter[int]]:
    """Use complete unit translates, rather than half-unit profile matching."""
    us = units(LEVEL)
    idx = {u: i for i, u in enumerate(us)}
    actions = tuple(tuple(idx[u * v % LEVEL] for v in us) for u in us)
    residues = {a: tuple(u * a % LEVEL for u in us) for a in range(1, LEVEL)}
    by_triple: dict[Triple, bytes] = {}
    by_profile: dict[bytes, int] = {}
    for beta in triples():
        a, b, c = beta
        p = bytes((x + y + z) // LEVEL - 1
                  for x, y, z in zip(residues[a], residues[b], residues[c]))
        eps = sum(psi(LEVEL, t) for t in beta) % 2
        if p in by_profile and by_profile[p] != eps:
            raise AssertionError("psi is not constant on a profile")
        by_triple[beta] = p
        by_profile[p] = eps
    pending = set(by_profile)
    dimension: dict[bytes, int] = {}
    orbit_counts: Counter[int] = Counter()
    while pending:
        p = min(pending)
        orbit = {bytes(p[i] for i in permutation) for permutation in actions}
        if not orbit <= by_profile.keys() or len(orbit) % 2:
            raise AssertionError("Invalid or incomplete unit orbit")
        g = len(orbit) // 2
        for q in orbit:
            if q in dimension:
                raise AssertionError("Repeated orbit")
            dimension[q] = g
        orbit_counts[g] += 1
        pending.difference_update(orbit)
    return by_triple, by_profile, dimension, orbit_counts


def dual_value(p: bytes, selected: tuple[int, ...] = DUAL_UNITS) -> int:
    idx = {u: i for i, u in enumerate(units(LEVEL))}
    return sum(p[idx[u]] - p[0] for u in selected) % 2


def direct_orbit_dimension(beta: Triple) -> int:
    """Orthogonal orbit-stabilizer check, with a new profile at each unit."""
    original = profile(LEVEL, beta)
    us = units(LEVEL)
    stabilizer = sum(profile(LEVEL, tuple(u * a % LEVEL for a in beta)) == original
                     for u in us)
    quotient, remainder = divmod(len(us), 2 * stabilizer)
    if remainder:
        raise AssertionError("Odd orbit")
    return quotient


def dh(n: int, a: int) -> list[tuple[int, int]]:
    if n < 2 or LEVEL % n or n * a % LEVEL == 0:
        raise ValueError("Inadmissible multiplication relation")
    result = [( (a + j * (LEVEL // n)) % LEVEL, 1) for j in range(n)]
    result += [(n * a % LEVEL, -1)]
    result += [(j * (LEVEL // n), -1) for j in range(1, n)]
    if any(idx == 0 for idx, _ in result):
        raise AssertionError("Unexpected zero symbol")
    return result


class U45Tests(unittest.TestCase):
    def test_01_domains_and_small_cm_control(self) -> None:
        for beta in ((0, 1, 419), (1, 1, 1)):
            with self.assertRaises(ValueError):
                profile(LEVEL, beta)
        with self.assertRaises(ValueError):
            dh(5, 84)
        with self.assertRaises(ValueError):
            psi(LEVEL, 0)
        p = profile(7, (1, 2, 4))
        self.assertEqual(tuple(p), (0, 0, 1, 0, 1, 1))
        self.assertEqual(direct_orbit_dimension((60, 120, 240)), 1)

    def test_02_full_population_and_orbit_census(self) -> None:
        ts, ps, dims, counts = census()
        self.assertEqual(len(ts), 29400)
        self.assertEqual(len(ts), len(set(ts)))
        self.assertEqual(len(ps), 27404)
        self.assertEqual(sum(counts.values()), 447)
        self.assertEqual(dict(counts), {1: 5, 2: 2, 3: 3, 4: 5, 6: 16,
                                       8: 4, 12: 60, 24: 170, 48: 182})
        self.assertEqual(sum(2 * g * n for g, n in counts.items()), len(ps))
        self.assertEqual(sum(g <= 8 for g in dims.values()), 332)
        for p in ps:
            self.assertEqual(set(p), {0, 1})
            self.assertTrue(all(a + b == 1 for a, b in zip(p, reversed(p))))

    def test_03_complete_small_profile_certificate(self) -> None:
        ts, ps, dims, _ = census()
        small = [beta for beta, p in ts.items() if dims[p] <= 8]
        self.assertTrue(small)
        for beta in small:
            p = ts[beta]
            self.assertEqual(sum(psi(LEVEL, a) for a in beta) % 2, dual_value(p), beta)
        # For all 35 small type orbits, also use a direct stabilizer calculation.
        seen: set[bytes] = set()
        us = units(LEVEL)
        for beta in small:
            p = ts[beta]
            if p in seen:
                continue
            orb = {profile(LEVEL, tuple(u * a % LEVEL for a in beta)) for u in us}
            self.assertEqual(direct_orbit_dimension(beta), dims[p])
            self.assertTrue(all(ps[q] == dual_value(q) for q in orb))
            seen.update(orb)
        self.assertEqual(len(seen), 332)

    def test_04_deliberately_incomplete_certificate_fails(self) -> None:
        ts, _, dims, _ = census()
        failures = [beta for beta, p in ts.items() if dims[p] <= 8
                    and dual_value(p, DUAL_UNITS[1:]) != sum(psi(LEVEL, a) for a in beta) % 2]
        self.assertTrue(failures, "Dropping the first term should break the certificate")
        beta = (2, 140, 278)
        p = profile(LEVEL, beta)
        self.assertEqual(direct_orbit_dimension(beta), 12)
        self.assertEqual(sum(psi(LEVEL, a) for a in beta) % 2, 0)
        self.assertEqual(dual_value(p), 1)

    def test_05_all_classical_rows_and_target(self) -> None:
        reflection_count = 0
        for a in range(1, LEVEL):
            self.assertEqual((psi(LEVEL, a) + psi(LEVEL, LEVEL - a)) % 2, 0)
            reflection_count += 1
        dh_count = 0
        for n in range(2, LEVEL + 1):
            if LEVEL % n:
                continue
            for a in range(1, LEVEL):
                if n * a % LEVEL:
                    self.assertEqual(sum(sign * psi(LEVEL, idx) for idx, sign in dh(n, a)) % 2, 0)
                    dh_count += 1
        self.assertEqual((reflection_count, dh_count), (419, 8317))
        for u in units(LEVEL):
            target = tuple(6 * a * u % LEVEL for a in ALPHA)
            self.assertEqual(sum(target), 1260)
            self.assertEqual(sum(psi(LEVEL, a) for a in target) % 2, 1)

    def test_06_exact_square_certificate(self) -> None:
        v = [0] * LEVEL  # index zero denotes ell, not e_0
        for a, coeff in SQUARE_R:
            v[6 * a] += coeff
            v[LEVEL - 6 * a] += coeff
            v[0] -= coeff
        for n, a, coeff in SQUARE_D:
            for i, sign in dh(n, 6 * a):
                v[i] += coeff * sign
        for a in ALPHA:
            v[6 * a] -= 2
        v[0] += 6
        self.assertEqual(v, [0] * LEVEL)

    def test_07_boundary_word_is_hodge_and_formally_target(self) -> None:
        betas = tuple(tuple(6 * a for a in beta) for beta in BOUNDARY_WORD)
        profiles = tuple(profile(LEVEL, beta) for beta in betas)
        self.assertTrue(all(sum(vals) == 2 for vals in zip(*profiles)))
        self.assertEqual(tuple(direct_orbit_dimension(beta) for beta in betas), (12, 3, 2, 12))
        self.assertEqual(sum(psi(LEVEL, a) for a in chain.from_iterable(betas)) % 2, 1)
        # w - t(alpha) is exactly R(90)+R(210)+R(42), including ell.
        residual = Counter(chain.from_iterable(betas))
        residual.subtract(6 * a for a in ALPHA)
        residual[0] = -3
        for a in (90, 210, 42):
            residual[a] -= 1
            residual[LEVEL - a] -= 1
            residual[0] += 1
        self.assertTrue(all(v == 0 for v in residual.values()))


def report() -> dict[str, object]:
    ts, ps, dims, counts = census()
    small_counts = Counter(dims[p] for p in ts.values() if dims[p] <= 8)
    selected = [(beta, p, dims[p]) for beta, p in ts.items() if dims[p] <= 8]
    serialized = "".join(f"{','.join(map(str,beta))}:{p.hex()}:{g}\n" for beta, p, g in selected)
    broken = next(beta for beta, p, _ in selected
                  if dual_value(p, DUAL_UNITS[1:]) != sum(psi(LEVEL, a) for a in beta) % 2)
    return {
        "level": LEVEL, "base_commit": "bfdb70edaae96b5ec0aaef8782ab3baffd448826",
        "unit_count": len(units(LEVEL)), "sorted_triple_count": len(ts),
        "distinct_profiles": len(ps), "profile_orbits": sum(counts.values()),
        "orbits_by_g": dict(sorted(counts.items())),
        "small_g_cutoff": 8, "small_profiles": len({p for _, p, _ in selected}),
        "small_profile_orbits": sum(n for g, n in counts.items() if g <= 8),
        "small_triples": len(selected), "small_triples_by_g": dict(sorted(small_counts.items())),
        "five_certificate_units": DUAL_UNITS, "certificate_failures": sum(
            sum(psi(LEVEL, a) for a in beta) % 2 != dual_value(p) for beta, p, _ in selected),
        "certificate_table_serialization": "sorted triple:hex(full96bitprofile):g\\n",
        "certificate_table_sha256": sha256(serialized.encode("ascii")).hexdigest(),
        "broken_certificate_witness": broken,
        "dimension12_counterexample": {"triple": [2, 140, 278], "psi": 0, "formula": 1},
        "odd_hodge_boundary_word_level70": BOUNDARY_WORD,
        "boundary_profile_dimensions": [12, 3, 2, 12],
        "tests": 7, "python": platform.python_version(),
        "self_review_only": True, "source_theorems_machine_verified": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(U45Tests))
    if not result.wasSuccessful():
        return 1
    data = report()
    data["elapsed_seconds"] = round(time.monotonic() - start, 3)
    encoded = json.dumps(data, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded)
    return 0


if __name__ == "__main__":
    sys.exit(main())
