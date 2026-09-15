"""Check the exact U39 certificate and its finite arithmetic corroboration.

The global field/cycle conclusions require the proof in U39; passing this
checker is not a formal proof of those geometric conclusions. Run from any
working directory. Existing U38 files are read, never rewritten.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import platform
import sys
import time
import unittest
from fractions import Fraction
from pathlib import Path
from types import ModuleType

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ALPHA = (1, 20, 24, 42, 61, 62)
BASE_COMMIT = "467188a3d6c10a08ab2476fc65c12d14c78771de"
X = sp.Symbol("x")
PHI = sp.Poly(sp.cyclotomic_poly(70, X), X, domain=sp.QQ)
D = Fraction(-(2**32) * 5**15, 7**7)
RADICAND = 2 * 5**30 * 7**14
REFLECTIONS = (
    (8, 2), (9, 1), (10, 1), (11, 1), (12, 1), (13, -2), (18, -1),
    (20, 4), (21, -1), (22, -2), (24, 2), (26, 2), (28, 1), (29, -2),
    (30, -1), (32, -1), (34, 1),
)
DISTRIBUTIONS = (
    (2, 1, -1), (2, 3, 1), (2, 5, 2), (2, 6, 1), (2, 7, 1),
    (2, 8, -2), (2, 9, -1), (2, 10, 1), (2, 11, -2), (2, 13, 2),
    (2, 14, 1), (2, 15, -3), (2, 16, -1), (2, 17, 1),
    (5, 1, 2), (5, 2, -1), (5, 3, -1), (7, 1, 1),
)


def load_prior_checker() -> ModuleType:
    """Load the pinned U38 implementation without invoking its output writer."""
    path = HERE.parent / "U38" / "verify_u38.py"
    spec = importlib.util.spec_from_file_location("hodge_u38", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PRIOR = load_prior_checker()


def formal_certificate(
    reflections: tuple[tuple[int, int], ...] = REFLECTIONS,
    distributions: tuple[tuple[int, int, int], ...] = DISTRIBUTIONS,
) -> tuple[tuple[int, ...], tuple[int, int, int, int]]:
    """Coordinates 0..68 encode G(1)..G(69); coordinate 69 encodes q."""
    result = [0] * 70
    rhs = [0, 0, 0, 0]  # exponents of chi(-1), chi(2), chi(5), chi(7)
    for a, power in reflections:
        if not 1 <= a <= 35:
            raise ValueError("Reflection index outside declared range")
        result[a - 1] += power
        result[70 - a - 1] += power
        result[69] -= power
        rhs[0] += a * power
    for n, a, power in distributions:
        if n not in (2, 5, 7) or not 1 <= a < 70 // n:
            raise ValueError("Davenport-Hasse index violates nontriviality")
        for j in range(n):
            index = (a + j * (70 // n)) % 70
            if index == 0:
                raise ValueError("Unexpected trivial Gauss character")
            result[index - 1] += power
        result[(n * a) % 70 - 1] -= power
        for j in range(1, n):
            result[j * (70 // n) - 1] -= power
        rhs[(2, 5, 7).index(n) + 1] -= n * a * power
    return tuple(result), (rhs[0], rhs[1], rhs[2], rhs[3])


def expected_vector() -> tuple[int, ...]:
    vector = [0] * 70
    for a in ALPHA:
        vector[a - 1] += 2
    vector[-1] = -6
    return tuple(vector)


def tau_polynomial() -> sp.Poly:
    """An explicit square root of -35, checked by reduction, not assumed."""
    value = sum(int(sp.jacobi_symbol(a, 35)) * X**(2*a) for a in range(35))
    return sp.Poly(value, X, domain=sp.QQ).rem(PHI)


def fraction_mod(value: Fraction, p: int) -> int:
    return value.numerator * pow(value.denominator, -1, p) % p


def prime_row(p: int) -> tuple[int, int, int, int, int, int]:
    g, logs = PRIOR.logs_at(p, 70)
    jacobi = PRIOR.factored_jacobi(ALPHA, p, 70)
    exponent, _ = PRIOR.normalized_root(jacobi, p, 70)
    zeta = pow(g, (p - 1) // 70, p)
    tau = int(tau_polynomial().eval(zeta)) % p
    c = fraction_mod(Fraction(2**16 * 5**7, 7**4), p) * tau % p
    d = fraction_mod(D, p)
    if tau * tau % p != (-35) % p or c * c % p != d:
        raise ArithmeticError("Cyclotomic square-root comparison failed")
    return p, g, exponent, logs[d], logs[c], (exponent - logs[c]) % 70


class U39Tests(unittest.TestCase):
    def test_exact_formal_gauss_certificate(self) -> None:
        lhs, rhs = formal_certificate()
        self.assertEqual(lhs, expected_vector())
        self.assertEqual(rhs, (71, 32, 15, -7))

    def test_corrupted_certificate_rejected(self) -> None:
        corrupted = ((8, 3),) + REFLECTIONS[1:]
        self.assertNotEqual(formal_certificate(corrupted)[0], expected_vector())
        with self.assertRaises(ValueError):
            formal_certificate((), ((2, 35, 1),))

    def test_cyclotomic_square_root(self) -> None:
        tau = tau_polynomial()
        self.assertTrue((tau*tau + sp.Poly(35, X)).rem(PHI).is_zero)
        self.assertEqual(Fraction(2**16 * 5**7, 7**4)**2 * (-35), D)

    def test_radical_field_change_of_generator(self) -> None:
        factor = Fraction(-(2**21) * 5**9, 7**5)
        self.assertEqual(D**23, RADICAND * factor**35)
        self.assertEqual(math.gcd(23, 35), 1)
        self.assertEqual(math.gcd(32, 35), 1)

    def test_eisenstein_and_cyclotomic_discriminant(self) -> None:
        self.assertEqual(RADICAND % 4, 2)
        discriminant = int(PHI.discriminant())
        self.assertEqual(discriminant, 5**18 * 7**20)
        self.assertEqual(discriminant % 2, 1)
        # This arithmetic corroborates the separate local Eisenstein proof.

    def test_five_existing_primes_and_wolfram(self) -> None:
        rows = [list(prime_row(p)) for p in (71, 211, 281, 421, 491)]
        external = json.loads((HERE / "independent_wolfram.json").read_text())
        self.assertEqual(rows, external["prime_rows"])
        self.assertTrue(external["integer_certificate_zero"])
        self.assertEqual(external["rhs_exponents"], [71, 32, 15, -7])
        for _, _, j, d, c, residual in rows:
            self.assertEqual(2*j % 70, d)
            self.assertEqual(2*c % 70, d)
            self.assertIn(residual, (0, 35))

    def test_holdout_primes(self) -> None:
        # New primes test the uniform identity; their outcomes were not fitted.
        for p in (631, 701, 911):
            _, _, j, d, _, residual = prime_row(p)
            self.assertEqual(2*j % 70, d)
            self.assertIn(residual, (0, 35))

    def test_decisive_prime_independent_additive_convolution(self) -> None:
        self.assertEqual(PRIOR.factored_jacobi(ALPHA, 491, 70),
                         PRIOR.direct_jacobi(ALPHA, 491, 70))
        self.assertEqual(PRIOR.normalized_root(
            PRIOR.direct_jacobi(ALPHA, 491, 70), 491, 70), (57, 70))

    def test_all_unit_conjugates(self) -> None:
        for u in range(1, 70):
            if math.gcd(u, 70) != 1:
                continue
            a = tuple(u*v % 70 for v in ALPHA)
            k, order = PRIOR.normalized_root(PRIOR.factored_jacobi(a, 491, 70),
                                            491, 70)
            self.assertEqual(k, 57*u % 70)
            self.assertEqual(order, 70)

    def test_same_kernel_candidate_is_rejected(self) -> None:
        # Two faithful cyclic-order-70 characters with the same kernel differ
        # by a fixed unit power. Check every such power, not just equality.
        rows = [prime_row(p) for p in (71, 211, 281, 421, 491)]
        possible = [u for u in range(1, 70) if math.gcd(u, 70) == 1
                    and all((u*row[4]-row[2]) % 70 == 0 for row in rows)]
        self.assertEqual(possible, [])
        self.assertEqual(prime_row(421)[-1], 35)

    def test_finite_field_sign_benchmark(self) -> None:
        self.assertEqual(PRIOR.point_count_fermat(7, 3), 3690)
        self.assertEqual(3690 - sum(7**i for i in range(5)), 889)

    def test_target_orbit_and_character_kernel(self) -> None:
        units = tuple(u for u in range(1, 70) if math.gcd(u, 70) == 1)
        orbit = {tuple(u*a % 70 for a in ALPHA) for u in units}
        self.assertEqual(len(orbit), 24)
        self.assertEqual({sum(a) for a in orbit}, {210})
        for t in range(1, 70):
            self.assertTrue(all(t*u % 70 != 0 for u in units))


def main() -> int:
    started = time.perf_counter()
    with (HERE / "test_run.log").open("w", encoding="utf-8") as log:
        result = unittest.TextTestRunner(stream=log, verbosity=2).run(
            unittest.defaultTestLoader.loadTestsFromTestCase(U39Tests))
    if not result.wasSuccessful():
        print((HERE / "test_run.log").read_text(), file=sys.stderr)
        return 1
    paths = [Path(__file__), HERE.parent / "U38" / "verify_u38.py",
             HERE / "independent_wolfram.json"]
    report = {
        "claim": "Exact squared Gauss/Jacobi identity and arithmetic certificates",
        "base_commit": BASE_COMMIT,
        "tests": result.testsRun,
        "passed": True,
        "rhs_exponents_minus_one_two_five_seven": formal_certificate()[1],
        "tau_polynomial": str(tau_polynomial().as_expr()),
        "D": str(D), "radicand": str(RADICAND),
        "prime_rows": [prime_row(p) for p in (71, 211, 281, 421, 491, 631, 701, 911)],
        "finite_test_domains": "Eight prime fields; all 24 unit conjugates at 491",
        "arithmetic": "Exact integer relation vectors, rational/cyclotomic arithmetic; U38 bounded int64 convolution at 491",
        "python": sys.version, "sympy": sp.__version__, "platform": platform.platform(),
        "input_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in paths},
        "elapsed_seconds": time.perf_counter()-started,
        "non_claims": ["No algebraic cycle constructed", "Not a formal verification of U39",
                       "No resolution of rational Hodge conjecture", "No field sufficiency theorem for cycles"],
    }
    (HERE / "verification.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"tests": result.testsRun, "passed": True,
                      "prime_rows": report["prime_rows"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
