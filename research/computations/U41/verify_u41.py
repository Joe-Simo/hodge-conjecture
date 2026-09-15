"""Exact corroboration for U41; tests are not a proof of the uniform theorem.

Run: python -m unittest discover -s research/computations/U41 -p 'verify_u41.py' -v
Inputs are exact integers, rational numbers, and QQ(i). No numerical tolerances.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from math import gcd
import unittest

import sympy as sp

ALPHA = (1, 20, 24, 42, 61, 62)
GAMMA = sp.diag(1, -1)
SWAP = sp.Matrix([[0, 1], [1, 0]])
ODD_CLOSED = sp.Matrix([[0, 1], [-1, 0]])
Partition = tuple[tuple[int, ...], ...]


def partitions(items: tuple[int, ...]) -> tuple[Partition, ...]:
    if not items:
        return ((),)
    first, *tail = items
    result: list[Partition] = []
    for part in partitions(tuple(tail)):
        result.append(((first,),) + part)
        for j, block in enumerate(part):
            result.append(part[:j] + ((first,) + block,) + part[j+1:])
    return tuple(result)


def kron(factors: list[sp.MatrixBase]) -> sp.MatrixBase:
    if not factors:
        return sp.ones(1, 1)
    out = factors[0]
    for factor in factors[1:]:
        out = sp.kronecker_product(out, factor)
    return out


def embedded_odd(matrix: sp.MatrixBase, index: int, count: int) -> sp.MatrixBase:
    if not 0 <= index < count:
        raise ValueError("Variable index is out of range")
    return sp.MutableSparseMatrix(kron([GAMMA]*index + [matrix] + [sp.eye(2)]*(count-index-1)))


def zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(v) == 0 for v in matrix)


def toy_data() -> dict[str, sp.MatrixBase]:
    x, y = sp.symbols("x y")
    d = x*embedded_odd(SWAP, 0, 2) + y*embedded_odd(SWAP, 1, 2)
    a = embedded_odd(ODD_CLOSED, 0, 2)
    b = embedded_odd(ODD_CLOSED, 1, 2)
    e = (sp.eye(4)+sp.I*a*b)/2
    p = d.diff(y)*d.diff(x)
    return {"d": d, "e": e, "p": p, "grading": kron([GAMMA, GAMMA]), "a": a, "b": b}


@lru_cache(maxsize=1)
def clifford6() -> tuple[tuple[sp.MatrixBase, ...], tuple[sp.MatrixBase, ...], sp.MatrixBase]:
    k = tuple(embedded_odd(SWAP, i, 6) for i in range(6))
    t = tuple(embedded_odd(ODD_CLOSED, i, 6) for i in range(6))
    return k, t, kron([GAMMA]*6)


def product_reverse(matrices: tuple[sp.MatrixBase, ...]) -> sp.MatrixBase:
    out = sp.eye(matrices[0].rows)
    for matrix in reversed(matrices):
        out = out*matrix
    return out


class U41Checks(unittest.TestCase):
    def test_partition_coverage_and_binary_support(self) -> None:
        parts = partitions(tuple(range(6)))
        canonical = {tuple(sorted(tuple(sorted(b)) for b in p)) for p in parts}
        self.assertEqual(len(parts), 203)
        self.assertEqual(len(canonical), 203)
        proper = [p for p in parts if len(p) > 1]
        odd = [p for p in proper if any(len(b) % 2 for b in p)]
        even = [p for p in proper if all(len(b) % 2 == 0 for b in p)]
        self.assertEqual((len(proper), len(odd), len(even)), (202, 172, 30))
        self.assertTrue(all(any(len(b) == 2 for b in p) for p in even))
        self.assertEqual(sum(sorted(map(len, p)) == [2, 2, 2] for p in even), 15)
        self.assertEqual(sum(sorted(map(len, p)) == [2, 4] for p in even), 15)

    def test_all_galois_targets_fail_binary_and_balanced_support(self) -> None:
        for u in range(1, 70):
            if gcd(u, 70) != 1:
                continue
            a = tuple(u*v % 70 for v in ALPHA)
            self.assertEqual(sum(a), 210)
            self.assertTrue(all((a[i]+a[j]) % 70 != 0 for i, j in combinations(range(6), 2)))
            self.assertTrue(any(v-1 < 34 for v in a))
            self.assertNotEqual(a, (35,)*6)

    def test_odd_times_odd_tensor_trace_symbolically(self) -> None:
        a = sp.symbols("a0:6")
        b = sp.symbols("b0:6")
        odd = [sp.Matrix([[0, a[i]], [b[i], 0]]) for i in range(6)]
        derivatives = [sp.kronecker_product(odd[i], sp.eye(2)) for i in range(3)]
        derivatives += [sp.kronecker_product(GAMMA, odd[i]) for i in range(3, 6)]
        p = product_reverse(tuple(derivatives))
        self.assertEqual(sp.expand(sp.trace(kron([GAMMA, GAMMA])*p)), 0)
        # Even-variable factors need not have zero trace: do not prove a false universal zero.
        x, y = sp.symbols("x y")
        d = sp.Matrix([[0, x-y], [x+y, 0]])
        self.assertTrue(zero(d*d-(x*x-y*y)*sp.eye(2)))
        self.assertEqual(sp.trace(GAMMA*d.diff(y)*d.diff(x)), -2)

    def test_explicit_retract_breaks_zero_of_parent(self) -> None:
        data = toy_data()
        d, e, p, gamma = (data[k] for k in ("d", "e", "p", "grading"))
        x, y = sp.symbols("x y")
        self.assertTrue(zero(d*d-(x*x+y*y)*sp.eye(4)))
        self.assertTrue(zero(e*e-e))
        self.assertTrue(zero(e*d-d*e))
        self.assertTrue(zero(e*gamma-gamma*e))
        self.assertEqual(sp.trace(gamma*p), 0)
        self.assertEqual(sp.trace(gamma*e*p), 2*sp.I)
        self.assertEqual(sp.trace(gamma*(sp.eye(4)-e)*p), -2*sp.I)
        wrong = (sp.eye(4)+data["a"]*data["b"])/2
        self.assertFalse(zero(wrong*wrong-wrong))

    def test_univariate_endomorphism_relations_for_all_69_exponents(self) -> None:
        x = sp.Symbol("x")
        for a in range(1, 70):
            k = min(a, 70-a)
            c = sp.Integer(3)
            d = sp.Matrix([[0, x**k], [c*x**(70-k), 0]])
            theta = sp.Matrix([[0, 1], [-c*x**(70-2*k), 0]])
            self.assertTrue(zero(d*d-c*x**70*sp.eye(2)))
            self.assertTrue(zero(d*theta+theta*d))
            self.assertTrue(zero(theta*theta+c*x**(70-2*k)*sp.eye(2)))
            # Exact radical dichotomy in the quotient by x^k.
            if k == 35:
                self.assertTrue(zero(theta*theta+c*sp.eye(2)))
            else:
                power = 2*((k + (70-2*k)-1)//(70-2*k))
                self.assertTrue(all(sp.rem(v, x**k, x) == 0 for v in theta**power))

    def test_nilpotent_idempotent_conjugacy_formula(self) -> None:
        epsilon = sp.Symbol("epsilon")
        e0 = sp.diag(1, 0)
        e = sp.Matrix([[1, -epsilon], [0, 0]])
        u = e*e0+(sp.eye(2)-e)*(sp.eye(2)-e0)
        self.assertTrue(zero(e*e-e))
        self.assertTrue(zero(e*u-u*e0))
        self.assertEqual(u.det(), 1)
        self.assertTrue(zero(u*e0*u.inv()-e))

    def test_clifford_idempotent_and_balanced_nonzero_control(self) -> None:
        k, t, gamma = clifford6()
        identity = sp.eye(64)
        for i in range(6):
            self.assertTrue(zero(k[i]*k[i]-identity))
            self.assertTrue(zero(t[i]*t[i]+identity))
            for j in range(6):
                self.assertTrue(zero(t[i]*k[j]+k[j]*t[i]))
        e = identity
        for i in (0, 2, 4):
            e = e*(identity+sp.I*t[i]*t[i+1])/2
        self.assertTrue(zero(e*e-e))
        self.assertTrue(zero(e*gamma-gamma*e))
        for matrix in k:
            self.assertTrue(zero(e*matrix-matrix*e))
        value = sp.trace(gamma*e*product_reverse(k))
        self.assertNotEqual(value, 0)
        self.assertEqual(sp.trace(gamma*product_reverse(k)), 0)
        # Every derivative of z_i^35 K_i has factor 35 z_i^34. Even polynomial
        # idempotents cannot lower these exponents in the monomial Jacobian quotient.
        self.assertEqual(6*34, 204)
        self.assertEqual([v-1 for v in ALPHA], [0, 19, 23, 41, 60, 61])

    def test_unbalanced_variable_kills_balanced_retract_trace(self) -> None:
        k, t, gamma = clifford6()
        e = sp.eye(64)
        for i in (1, 3):
            e = e*(sp.eye(64)+sp.I*t[i]*t[i+1])/2
        # Variable 0 is unbalanced. Its derivative is arbitrary odd; the
        # lifted quotient idempotent contains no theta_0, so this trace is zero.
        a, b = sp.symbols("a b")
        first = embedded_odd(sp.Matrix([[0, a], [b, 0]]), 0, 6)
        self.assertEqual(sp.expand(sp.trace(gamma*e*product_reverse((first,)+k[1:]))), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
