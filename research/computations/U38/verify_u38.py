"""Exact Jacobi-sum certificate; no Hodge/Tate conjecture is assumed by the code.

Run: python research/computations/U38/verify_u38.py
Outputs are confined to this script's directory. See U38 for the separate
geometric implication. Two genuinely different sum algorithms are compared.
"""
from __future__ import annotations

import hashlib
import json
import math
import platform
import sys
import time
import unittest
from dataclasses import asdict, dataclass
from functools import lru_cache
from itertools import product
from pathlib import Path

import numpy as np
import sympy as sp
from numpy.typing import NDArray

ALPHA = (1, 20, 24, 42, 61, 62)
M = 70
PRIMES = (71, 211, 281, 421, 491)
EXPECTED_ROOTS = (40, 12, 32, 50, 57)
BASE_COMMIT = "467188a3d6c10a08ab2476fc65c12d14c78771de"
X = sp.Symbol("x")


def validate(a: tuple[int, ...], p: int, m: int) -> None:
    if m < 2 or not sp.isprime(p) or (p - 1) % m:
        raise ValueError("Require m >= 2, p prime, and m dividing p-1")
    if len(a) != 6 or any(not 0 < v < m for v in a) or sum(a) % m:
        raise ValueError("Require six nonzero characters with sum zero modulo m")


@lru_cache(maxsize=None)
def logs_at(p: int, m: int) -> tuple[int, tuple[int, ...]]:
    """Use the least primitive root, and check the complete multiplicative orbit."""
    g = int(sp.primitive_root(p))
    logs = [-1] * p
    v = 1
    for k in range(p - 1):
        if logs[v] != -1:
            raise ArithmeticError("Primitive-root orbit repeated too early")
        logs[v] = k % m
        v = (v * g) % p
    if v != 1 or any(k < 0 for k in logs[1:]):
        raise ArithmeticError("Primitive-root orbit failed coverage")
    return g, tuple(logs)


def reduce_cyclotomic(coeffs: tuple[int, ...], m: int) -> tuple[int, ...]:
    """Ascending coefficients in the power basis of Q[zeta_m]."""
    phi = sp.Poly(sp.cyclotomic_poly(m, X), X, domain=sp.ZZ)
    poly = sp.Poly.from_list(list(reversed(coeffs)), X, domain=sp.ZZ)
    rem = poly.rem(phi)
    return tuple(int(rem.nth(i)) for i in range(int(phi.degree())))


def cyclic_product(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    """Arbitrary-precision Python integer convolution in Z[C_m]."""
    if len(a) != len(b):
        raise ValueError("Group-ring factors must have the same order")
    m = len(a)
    out = [0] * m
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[(i + j) % m] += av * bv
    return tuple(out)


def binary_jacobi(a: int, b: int, p: int, m: int) -> tuple[int, ...]:
    _, logs = logs_at(p, m)
    out = [0] * m
    for t in range(2, p):
        out[(a * logs[t] + b * logs[(1 - t) % p]) % m] += 1
    if sum(out) != p - 2:
        raise ArithmeticError("Binary Jacobi sum failed term count")
    return tuple(out)


def factored_jacobi(a: tuple[int, ...], p: int, m: int) -> tuple[int, ...]:
    """S_0/(p-1) = chi^a5(-1) times four binary sums.

    This shortcut is used only when all intermediate prefix characters are
    nontrivial, a hypothesis checked below rather than silently presumed.
    """
    validate(a, p, m)
    _, logs = logs_at(p, m)
    prefixes = tuple(sum(a[:i]) % m for i in range(1, 6))
    if 0 in prefixes:
        raise ValueError("Binary-product formula requires nonzero prefix sums")
    result = [0] * m
    result[(a[-1] * logs[p - 1]) % m] = 1
    out = tuple(result)
    for i in range(1, 5):
        out = cyclic_product(out, binary_jacobi(prefixes[i - 1], a[i], p, m))
    return reduce_cyclotomic(out, m)


def direct_jacobi(a: tuple[int, ...], p: int, m: int) -> tuple[int, ...]:
    """Independent sixfold additive convolution on F_p x Z/mZ.

    Nonnegative counts and (p-1)^6 < 2^63 prove that EVERY entry, intermediate
    addition and total fits int64. The check rejects larger unsafe inputs.
    """
    validate(a, p, m)
    if (p - 1) ** len(a) > np.iinfo(np.int64).max:
        raise OverflowError("Unsafe int64 population; use a different algorithm")
    _, logs = logs_at(p, m)
    counts: NDArray[np.int64] = np.zeros((p, m), dtype=np.int64)
    counts[0, 0] = 1
    for i, ai in enumerate(a, start=1):
        nxt = np.zeros_like(counts)
        for v in range(1, p):
            nxt += np.roll(counts, (v, ai * logs[v]), axis=(0, 1))
        counts = nxt
        if int(counts.sum()) != (p - 1) ** i:
            raise ArithmeticError("Sixfold convolution population mismatch")
    raw = tuple(int(v) for v in counts[0, :])
    if any(v % (p - 1) for v in raw):
        raise ArithmeticError("Diagonal scaling quotient failed integrality")
    return reduce_cyclotomic(tuple(v // (p - 1) for v in raw), m)


def normalized_root(j: tuple[int, ...], p: int, m: int) -> tuple[int, int]:
    if any(v % (p * p) for v in j):
        raise ArithmeticError("Normalized Jacobi sum not integral in power basis")
    norm = tuple(v // (p * p) for v in j)
    matches = []
    for k in range(m):
        rep = reduce_cyclotomic((0,) * k + (1,), m)
        if rep == norm:
            matches.append(k)
    if len(matches) != 1:
        raise ArithmeticError("No unique exact m-th root of unity was found")
    k = matches[0]
    return k, m // math.gcd(k, m)


def point_count_fermat(p: int, m: int) -> int:
    """Enumerate P^5(F_p) once, with first nonzero coordinate normalized to 1."""
    total = 0
    for first in range(6):
        for tail in product(range(p), repeat=5 - first):
            total += (1 + sum(pow(v, m, p) for v in tail)) % p == 0
    return total


@dataclass(frozen=True)
class PrimeRecord:
    p: int
    primitive_root: int
    root_exponent: int
    exact_order: int
    normalized_power_basis: tuple[int, ...]
    binary_power_bases: tuple[tuple[int, ...], ...]
    algorithms_agree: bool
    conjugate_orders: tuple[int, ...]
    integer_population_bound: int


@lru_cache(maxsize=1)
def compute_records() -> tuple[PrimeRecord, ...]:
    records = []
    for p in PRIMES:
        primary = factored_jacobi(ALPHA, p, M)
        independent = direct_jacobi(ALPHA, p, M)
        if primary != independent:
            raise ArithmeticError(f"Algorithms disagree at p={p}")
        k, order = normalized_root(primary, p, M)
        factors = tuple(
            reduce_cyclotomic(binary_jacobi(a, b, p, M), M)
            for a, b in ((1, 20), (21, 24), (45, 42), (17, 61))
        )
        orders = tuple(sorted({M // math.gcd(k * u, M) for u in range(M)
                               if math.gcd(u, M) == 1}))
        records.append(PrimeRecord(p, logs_at(p, M)[0], k, order,
                                   tuple(v // p**2 for v in primary), factors,
                                   True, orders, (p - 1)**6))
    return tuple(records)


class CertificateTests(unittest.TestCase):
    def test_target_hodge_orbit(self) -> None:
        orbit = {tuple(u * a % M for a in ALPHA)
                 for u in range(1, M) if math.gcd(u, M) == 1}
        self.assertEqual(len(orbit), 24)
        self.assertEqual({sum(a) for a in orbit}, {210})

    def test_two_algorithms_and_root_orders(self) -> None:
        rows = compute_records()
        self.assertEqual(tuple(r.root_exponent for r in rows), EXPECTED_ROOTS)
        self.assertEqual(tuple(r.exact_order for r in rows), (7, 35, 35, 7, 70))
        self.assertEqual(tuple(r.primitive_root for r in rows), (7, 2, 3, 2, 2))
        self.assertTrue(all(r.algorithms_agree for r in rows))

    def test_order70_certificate_at_491(self) -> None:
        phi = sp.Poly(sp.cyclotomic_poly(M, X), X)
        root = sp.Poly(-X**22, X)
        self.assertTrue(((root**70) - 1).rem(phi).is_zero)
        for d in (1, 2, 5, 7, 10, 14, 35):
            self.assertFalse(((root**d) - 1).rem(phi).is_zero)
        self.assertEqual(compute_records()[-1].conjugate_orders, (70,))

    def test_frobenius_sign_by_small_point_count(self) -> None:
        chars = tuple(a for a in product((1, 2), repeat=6) if sum(a) % 3 == 0)
        jvals = tuple(direct_jacobi(a, 7, 3) for a in chars)
        trace = tuple(sum(v[i] for v in jvals) for i in range(2))
        actual = point_count_fermat(7, 3)
        self.assertEqual(len(chars), 22)
        self.assertEqual(trace, (889, 0))
        self.assertEqual(actual, 3690)
        self.assertEqual(actual, sum(7**i for i in range(5)) + trace[0])

    def test_permutation_and_character_inverse(self) -> None:
        a = tuple(reversed(ALPHA))
        self.assertEqual(direct_jacobi(a, 71, M), direct_jacobi(ALPHA, 71, M))
        inverse = tuple(M - v for v in ALPHA)
        self.assertEqual(normalized_root(direct_jacobi(inverse, 491, M), 491, M),
                         ((-57) % M, 70))

    def test_all_24_galois_conjugate_sums_at_491(self) -> None:
        for u in range(1, M):
            if math.gcd(u, M) != 1:
                continue
            a = tuple(u * v % M for v in ALPHA)
            self.assertEqual(normalized_root(factored_jacobi(a, 491, M), 491, M),
                             (57 * u % M, 70))

    def test_independent_wolfram_factor_vectors(self) -> None:
        path = Path(__file__).resolve().parent / "independent_wolfram.json"
        external = json.loads(path.read_text())
        record = compute_records()[-1]
        self.assertEqual([list(v) for v in record.binary_power_bases],
                         external["p491_binary_coefficient_lists_ascending"])
        self.assertEqual([[r.p, r.primitive_root, r.root_exponent, r.exact_order]
                          for r in compute_records()],
                         external["prime_primitive_root_exponent_order"])

    def test_input_hypotheses(self) -> None:
        with self.assertRaises(ValueError):
            direct_jacobi(ALPHA, 72, M)
        with self.assertRaises(ValueError):
            direct_jacobi(ALPHA, 73, M)
        with self.assertRaises(ValueError):
            direct_jacobi((0, 21, 24, 42, 61, 62), 71, M)
        with self.assertRaises(ValueError):
            factored_jacobi((1, 69, 1, 69, 1, 69), 71, M)


def main() -> int:
    started = time.perf_counter()
    folder = Path(__file__).resolve().parent
    with (folder / "test_run.log").open("w", encoding="utf-8") as log:
        result = unittest.TextTestRunner(stream=log, verbosity=2).run(
            unittest.defaultTestLoader.loadTestsFromTestCase(CertificateTests))
    if not result.wasSuccessful():
        print((folder / "test_run.log").read_text(), file=sys.stderr)
        return 1
    report = {
        "claim": "Five exact Jacobi sums and necessary field-of-definition filter",
        "base_commit": BASE_COMMIT,
        "alpha": ALPHA, "m": M,
        "arithmetic": "Python unbounded integers; bounded exact int64 counts; Q[zeta_70]",
        "software": {"python": sys.version, "sympy": sp.__version__,
                     "numpy": np.__version__, "platform": platform.platform()},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "tests": result.testsRun, "test_status": "passed",
        "elapsed_seconds": time.perf_counter() - started,
        "records": [asdict(r) for r in compute_records()],
        "non_claims": ["No algebraic cycle is constructed", "No Hodge/Tate conjecture is proved",
                       "No assertion about field degree sufficiency", "No global novelty claim"],
    }
    (folder / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"tests": result.testsRun, "passed": True,
                      "prime_root_exponent_order": [(r.p, r.primitive_root, r.root_exponent,
                                                      r.exact_order) for r in compute_records()]},
                     indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
