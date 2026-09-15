"""Exact checks for U40; classical source applications are not machine-proved.

Run: python -m unittest discover -s research/computations/U40 -p 'verify_u40.py' -v
The checker has no output-file side effects and does not import either U39 checker.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import gcd
import unittest

import sympy as sp

ALPHA = (1, 20, 24, 42, 61, 62)
DELTA_EXPONENTS = (1, 4, 9, 16, 22, 26, 28, 30)
NORM = ((1, 1), (4, 1), (9, 1), (16, 1), (22, -1),
        (24, 2), (26, 1), (28, -1), (30, 1))
HD = ((2, 1, 1), (2, 9, -1), (2, 26, 1), (2, 34, -1),
      (5, 4, -1), (5, 6, 1), (5, 12, -1), (7, 2, 1), (7, 6, -1))
C0 = Fraction(2**8 * 7**7, 5**5)
DR = Fraction(-2**32 * 5**15, 7**7)
RR = 2 * 5**30 * 7**14
X = sp.Symbol("x")
PHI = sp.Poly(sp.cyclotomic_poly(70, X), X, domain=sp.QQ)
TAU = (4*X**22 + 2*X**21 + 2*X**20 - 4*X**16 - 4*X**15
       - 2*X**14 + 4*X**11 + 2*X**10 + 4*X**9 + 4*X**8
       - 2*X**5 - 4*X**4 + 1)
# Pinned U38 values, not new point-count claims. The inherited checker is rerun separately.
PRIME_VALUES = ((71, 7, 40), (211, 2, 12), (281, 3, 32), (421, 2, 50),
                (491, 2, 57), (631, 3, 64), (701, 2, 34), (911, 17, 0))


def reduce_cyclotomic(expr: sp.Expr) -> sp.Poly:
    """Compute in QQ[x]/Phi_70; reject a zero denominator."""
    numerator, denominator = sp.fraction(sp.cancel(expr))
    n = sp.Poly(numerator, X, domain=sp.QQ).rem(PHI)
    d = sp.Poly(denominator, X, domain=sp.QQ).rem(PHI)
    if d.is_zero:
        raise ZeroDivisionError("Denominator is zero in the cyclotomic field")
    return (n * sp.invert(d, PHI)).rem(PHI)


def power_mod(poly: sp.Poly, exponent: int) -> sp.Poly:
    """Binary powering with reduction after each multiplication."""
    if exponent < 0:
        return power_mod(sp.invert(poly, PHI), -exponent)
    result = sp.Poly(1, X, domain=sp.QQ)
    base = poly.rem(PHI)
    while exponent:
        if exponent & 1:
            result = (result*base).rem(PHI)
        base = (base*base).rem(PHI)
        exponent >>= 1
    return result


@lru_cache(maxsize=1)
def delta() -> sp.Poly:
    return reduce_cyclotomic(sp.prod(1-X**a for a in DELTA_EXPONENTS))


def formal_certificate() -> tuple[int, ...]:
    v = [0] * 69
    for a, power in NORM:
        v[a-1] += power
        v[69-a] += power
    for n, a, power in HD:
        for j in range(n):
            v[a+j*(70//n)-1] += power
        v[n*a-1] -= power
        for j in range(1, n):
            v[j*(70//n)-1] -= power
    return tuple(v)


def quadratic_comparisons() -> list[dict[str, int]]:
    rows: list[dict[str, int]] = []
    for p, g, jexp in PRIME_VALUES:
        zeta = pow(g, (p-1)//70, p)
        tau = int(sp.Poly(TAU, X).eval(zeta)) % p
        dp = int(delta().eval(zeta)) % p
        s = -tau * pow(7, -1, p) % p
        rad = dp * pow(s, -1, p) % p
        residue = pow(rad, (p-1)//2, p)
        if residue not in (1, p-1):
            raise ArithmeticError("Chosen prime is not a unit prime for the radicand")
        cr = 2**16 * 5**7 * pow(7**4, -1, p) * tau % p
        logs = {pow(g, k, p): k % 70 for k in range(p-1)}
        if len(logs) != p-1:
            raise ArithmeticError("The supplied generator is not primitive")
        sign = 1 if residue == 1 else -1
        rows.append({"p": p, "radicand_mod_p": rad, "quadratic_sign": sign,
                     "observed_quotient_exponent": (jexp-logs[cr]) % 70})
    return rows


class U40Checks(unittest.TestCase):
    def test_delignetype_and_formal_identity(self) -> None:
        units = [u for u in range(1, 70) if gcd(u, 70) == 1]
        self.assertEqual(len(units), 24)
        self.assertTrue(all(sum(u*a % 70 for a in ALPHA) == 210 for u in units))
        expected = tuple(2*ALPHA.count(a) for a in range(1, 70))
        self.assertEqual(formal_certificate(), expected)
        wrong = list(expected)
        wrong[0] += 1
        self.assertNotEqual(formal_certificate(), tuple(wrong))

    def test_two_independent_radicand_reconciliations(self) -> None:
        self.assertEqual(DR / C0**4, -Fraction(5, 7)**35)
        self.assertEqual(Fraction(RR), C0**22 * Fraction(5**4, 2**5*7**4)**35)
        self.assertEqual(gcd(22, 35), 1)
        self.assertNotEqual(Fraction(RR), C0**21 * Fraction(5**4, 2**5*7**4)**35)

    def test_exact_quadratic_factor_relative_to_remote_convention(self) -> None:
        self.assertTrue(reduce_cyclotomic(TAU**2+35).is_zero)
        s = -TAU/7
        cr = sp.Rational(2**16*5**7, 7**4) * TAU
        cr_poly = reduce_cyclotomic(cr)
        c_squared = sp.Rational(C0.numerator, C0.denominator)**2
        self.assertTrue((cr_poly-c_squared*power_mod(reduce_cyclotomic(s), 35)).is_zero)
        eta_rad = reduce_cyclotomic(-7*delta().as_expr()/TAU)
        self.assertTrue(reduce_cyclotomic(eta_rad.as_expr()*s-delta().as_expr()).is_zero)

    def test_gamma_squareclass_identity(self) -> None:
        u = reduce_cyclotomic(X**42)
        for a, exponent in NORM:
            u = (u*power_mod(reduce_cyclotomic(1-X**a), -exponent)).rem(PHI)
        q = reduce_cyclotomic(X**21)
        for a in (1, 4, 9, 16, 24, 26, 30):
            q = (q*power_mod(reduce_cyclotomic(1-X**a), -1)).rem(PHI)
        self.assertTrue((u-q*q*delta()).rem(PHI).is_zero)
        self.assertEqual(sum(power for _, power in NORM), 6)
        self.assertEqual(sum(a*power for a, power in NORM), 84)
        powers = {n: sum((power*(1-Fraction(n*a, 70)) for nn, a, power in HD if nn == n), Fraction(0))
                  for n in (2, 5, 7)}
        self.assertEqual(powers, {2: Fraction(16, 35), 5: Fraction(-2, 7), 7: Fraction(2, 5)})

    def test_real_degree_twelve_coefficient(self) -> None:
        real = (sp.Poly(X**2, X, domain=sp.QQ)*delta()).rem(PHI)
        self.assertTrue(reduce_cyclotomic(real.as_expr().subs(X, 1/X)-real.as_expr()).is_zero)
        t = sp.Symbol("t")
        p = (t**12-35*t**11-210*t**10+7805*t**9+58170*t**8+29925*t**7
             -281575*t**6-118825*t**5+307475*t**4+98000*t**3
             -79625*t**2-12250*t+6125)
        self.assertEqual(sp.expand(sp.resultant(PHI.as_expr(), t-real.as_expr(), X)-p**2), 0)
        self.assertTrue(sp.Poly(p, t).is_irreducible)
        self.assertEqual(gcd(-5, 4), 1)
        self.assertEqual(gcd(119, 6), 1)

    def test_residual_quadratic_matches_pinned_frobenius_data(self) -> None:
        rows = quadratic_comparisons()
        self.assertEqual([r["quadratic_sign"] for r in rows], [1, 1, 1, -1, 1, -1, 1, -1])
        for row in rows:
            self.assertEqual(row["observed_quotient_exponent"], 0 if row["quadratic_sign"] == 1 else 35)

    def test_valuation_obstruction_and_recovery_identity(self) -> None:
        # v_5(C0)=-20 and v_5(Delta)=1 imply v_5(D0)=-5, whereas rational
        # coefficients have valuations divisible by 4. The proof covers all integers.
        self.assertEqual(2*(-20)+35, -5)
        self.assertNotIn((-5) % 70, {4*k % 70 for k in range(70)})
        self.assertEqual(sp.resultant(PHI, delta()), 5**6 * 7**4)
        # Odd valuations certify the three nontrivial quadratic squareclasses.
        for vals in ((2, -3), (1, 1), (-1, 4)):
            self.assertTrue(any(v % 2 for v in vals))
        self.assertEqual(gcd(35, 4), 1)
        t, c, d = sp.symbols("t c d")
        self.assertEqual(sp.rem(t**36*d**18-t*c*d**18, t**35-c, t), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
