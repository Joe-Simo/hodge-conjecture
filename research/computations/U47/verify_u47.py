"""Exact algebraic checks for U47, not a proof assistant for its geometry.

The complete finite inputs are the two stated curves, their two explicit
covers, and all units modulo 5 and 7. Symbolic identities hold over Q or Q(i).
The Picard-Lefschetz and Picard/Jacobian comparison steps are proved/cited in
the accompanying note, not inferred from these tests.
"""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

u, t, r, w, v = sp.symbols('u t r w v')
e, k = sp.symbols('e k', integer=True)
F7 = u**5 + t**7*u + 1
DELTA7 = 256*t**35 + 3125
CUBIC = u**3 + 2*r*u**2 + 3*r**2*u + 4*r**3


def cm_stabilizer(prime: int, phi: tuple[int, ...]) -> tuple[int, ...]:
    """Compute the stabilizer of the explicitly supplied primitive CM type."""
    if not sp.isprime(prime) or prime < 3:
        raise ValueError('Require an odd prime')
    full = set(range(1, prime))
    subset = set(phi)
    if (len(phi) != (prime-1)//2 or len(subset) != len(phi)
            or not subset <= full or subset & {(-a) % prime for a in subset}):
        raise ValueError('Require exactly one embedding in each conjugate pair')
    return tuple(a for a in range(1, prime)
                 if {(a*b) % prime for b in subset} == subset)


def cyclic_genus(n: int, valuations: tuple[int, ...]) -> int:
    """Riemann-Hurwitz arithmetic for a connected cyclic cover of P1.

    Include infinity. Connectedness for the actual polynomials follows from
    a simple zero. The gcd test here is an arithmetic consistency check.
    """
    if n < 2 or not valuations or 0 in valuations or sum(valuations) != 0:
        raise ValueError('Supply nonzero valuations, including infinity, summing to zero')
    if gcd(n, *valuations) != 1:
        raise ValueError('The supplied cyclic-cover datum is not primitive')
    twice_genus_minus_two = -2*n + sum(n-gcd(n, a) for a in valuations)
    if twice_genus_minus_two < -2 or twice_genus_minus_two % 2:
        raise ValueError('Invalid Riemann-Hurwitz datum')
    return 1 + twice_genus_minus_two//2


def cover_residual(q: int) -> sp.Expr:
    """Substitute the finite product map; reduce by its two curve equations."""
    if q == 5:
        image_x, image_y, image_z = t, w**2*u, sp.I*w**5*v
        raw = image_z**2 + image_y**5 + image_x**9 + image_x**2
        raw = sp.expand(raw).subs(v**2, u**5+1)
        return sp.expand(raw).subs(w**10, t**2*(1+t**7)).expand()
    if q == 7:
        image_x, image_y, image_z = w**2*u/t, t, sp.I*w**7*v/t**3
        raw = image_z**2 + image_y**5 + image_x**7*image_y + 1
        raw = sp.expand(raw).subs(v**2, u**7+1)
        raw = sp.together(raw).subs(w**14, t**6*(1+t**5))
        return sp.cancel(raw)
    raise ValueError('Only the two actual cover maps are in scope')


class U47Tests(unittest.TestCase):
    def test_discriminant_and_all_finite_nodal_parameters(self) -> None:
        self.assertEqual(sp.discriminant(F7, u), DELTA7)
        self.assertEqual(sp.degree(DELTA7, t), 35)
        self.assertEqual(sp.gcd(DELTA7, sp.diff(DELTA7, t)), 1)
        self.assertEqual(DELTA7.subs(t, 0), 3125)
        # At infinity in the hyperelliptic variable, the compactification is smooth.
        x, z = sp.symbols('x z')
        at_infinity = z**2 + x + t**7*x**5 + x**6
        self.assertEqual(sp.diff(at_infinity, x).subs({x: 0, z: 0}), 1)

    def test_unique_double_root_and_normalization(self) -> None:
        specialized = u**5-5*r**4*u+4*r**5
        self.assertEqual(sp.expand(specialized-(u-r)**2*CUBIC), 0)
        self.assertEqual(sp.discriminant(CUBIC, u), -200*r**6)
        self.assertEqual(CUBIC.subs(u, r), 10*r**3)
        self.assertEqual(sp.diff(specialized, u, 2).subs(u, r), 20*r**3)
        # The double root is uniquely r=-5/(4t^7); no root-choice scan is used.
        rr = -sp.Rational(5, 4)/t**7
        for expression in [rr**5-sp.Rational(1, 4), t**7+5*rr**4]:
            numerator = sp.fraction(sp.cancel(expression))[0]
            self.assertEqual(sp.rem(numerator, DELTA7, t), 0)
        self.assertEqual(sp.diff(F7, t).subs(u, r), 7*t**6*r)

    def test_monodromy_all_base_change_indices(self) -> None:
        n = sp.zeros(4)
        n[0, 1] = 1
        identity = sp.eye(4)
        omega = sp.diag(sp.Matrix([[0, 1], [-1, 0]]),
                        sp.Matrix([[0, 1], [-1, 0]]))
        self.assertEqual(n.rank(), 1)
        self.assertEqual(n*n, sp.zeros(4))
        # This polynomial identity and induction, not finite sampling, give T^e=I+eN.
        self.assertEqual((identity+e*n)*(identity+k*n), identity+(e+k)*n)
        self.assertEqual((identity+e*n).T*omega*(identity+e*n), omega)
        self.assertEqual((identity+e*n)[0, 1], e)
        self.assertEqual(identity+0*n, identity)  # boundary: e=0 is deliberately excluded

    def test_constant_curve_types_and_imprimitive_control(self) -> None:
        self.assertEqual(cm_stabilizer(5, (1, 2)), (1,))
        self.assertEqual(cm_stabilizer(7, (1, 2, 3)), (1,))
        # An induced CM type must not be labeled simple by the same test.
        self.assertEqual(cm_stabilizer(7, (1, 2, 4)), (1, 2, 4))
        self.assertEqual(sp.degree(sp.cyclotomic_poly(5, u)), 4)
        self.assertEqual(sp.degree(sp.cyclotomic_poly(7, u)), 6)

    def test_both_explicit_surface_maps(self) -> None:
        self.assertEqual(cover_residual(5), 0)
        self.assertEqual(cover_residual(7), 0)
        # Inverse coordinate recovery after adjoining w (on the dense torus).
        self.assertEqual(sp.cancel((w**2*u)/w**2), u)
        self.assertEqual(sp.cancel((sp.I*w**5*v)/(sp.I*w**5)), v)
        self.assertEqual(sp.cancel((w**2*u/t)*t/w**2), u)
        self.assertEqual(sp.cancel((sp.I*w**7*v/t**3)*t**3/(sp.I*w**7)), v)

    def test_cover_actions_and_connectedness(self) -> None:
        # Exponents under eta: w has weight1, u weight-2, v weight-q.
        for q in (5, 7):
            n = 2*q
            self.assertEqual((2-2) % n, 0)
            self.assertEqual((q-q) % n, 0)
            self.assertEqual((-2*q) % n, 0)
            self.assertEqual(sum(all((a*b) % n == 0 for b in (1, -2, -q))
                                 for a in range(n)), 1)
        # Both radicands have simple nonzero roots, forcing full Kummer degrees.
        for p in (1+t**7, 1+t**5):
            self.assertEqual(sp.gcd(p, sp.diff(p, t)), 1)
            self.assertEqual(p.subs(t, 0), 1)

    def test_cover_genera(self) -> None:
        self.assertEqual(cyclic_genus(10, (2,)+(1,)*7+(-9,)), 31)
        self.assertEqual(cyclic_genus(14, (6,)+(1,)*5+(-11,)), 32)
        self.assertEqual(cyclic_genus(2, (1,)*5+(-5,)), 2)
        self.assertEqual(cyclic_genus(2, (1,)*7+(-7,)), 3)

    def test_elliptic_normalization_invariant(self) -> None:
        a2, a4, a6 = 2, 3, 4
        b2, b4, b6, b8 = 4*a2, 2*a4, 4*a6, 4*a2*a6-a4*a4
        c4 = b2*b2-24*b4
        discriminant = -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
        self.assertEqual(discriminant, -3200)
        self.assertEqual(sp.Rational(c4**3, discriminant), 160)

    def test_reject_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            cm_stabilizer(5, (1, 4))
        with self.assertRaises(ValueError):
            cm_stabilizer(9, (1, 2, 3, 4))
        with self.assertRaises(ValueError):
            cyclic_genus(10, (2, 2, -4))
        with self.assertRaises(ValueError):
            cyclic_genus(14, (6, 1, -6))
        with self.assertRaises(ValueError):
            cover_residual(11)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    start = time.perf_counter()
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(U47Tests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    report = {
        'status': 'specified exact algebraic checks passed; geometric proof self-reviewed separately',
        'python': platform.python_version(), 'sympy': sp.__version__,
        'coefficient_domains': ['Q', 'Q(i)', 'integer unit groups modulo 5 and 7'],
        'tests': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors),
        'runtime_seconds': time.perf_counter()-start,
        'nodal_discriminant': str(DELTA7), 'finite_nodal_parameters': 35,
        'node_factor': str(CUBIC), 'node_factor_discriminant': '-200*r**6',
        'node_normalization_j': 160,
        'cm_types': {'5': [1, 2], '7': [1, 2, 3]},
        'cm_stabilizers': {'5': cm_stabilizer(5, (1, 2)), '7': cm_stabilizer(7, (1, 2, 3))},
        'covers': {'S5': {'degree': 10, 'base_genus': 31, 'fibre_genus': 2},
                   'S7': {'degree': 14, 'base_genus': 32, 'fibre_genus': 3}},
        'nonclaims': ['No original Hodge class was represented.',
                      'Tests do not prove Picard-Lefschetz or Picard/Jacobian comparison.',
                      'No exclusion of correspondences dominating both base parameters.',
                      'No numerical approximation, random sampling, or formal proof kernel was used.'],
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
