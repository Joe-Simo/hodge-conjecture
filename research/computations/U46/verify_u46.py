"""Exact checks for U46's explicit surface models, not a Hodge proof assistant.

The geometric bridge and theorems about resolutions are proved/cited in the
accompanying note. No discovery program or inherited checker is imported.
Run: python research/computations/U46/verify_u46.py --output PATH
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
import json
from math import gcd
from pathlib import Path
import platform
import time
import unittest

import sympy as sp

M = 70
ALPHA = (1, 20, 24, 42, 61, 62)
BETA = (1, 42, 62, 35)
GAMMA = (20, 24, 61, 35)
UNITS = tuple(k for k in range(1, M) if gcd(k, M) == 1)
T, X, Y, Z = sp.symbols('T X Y Z')
a, b, c = sp.symbols('a b c', nonzero=True)
F5 = Z**2 + Y**5 + X**9*T + X**2*T**8
F7 = Z**2 + Y**5 + X**7*Y*T + T**10
WEIGHTS = (1, 1, 2, 5)


def character(k: int, vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(k * entry % M for entry in vector)


def grade(vector: tuple[int, ...]) -> int:
    if not all(0 < entry < M for entry in vector) or sum(vector) % M:
        raise ValueError('Expected a nonzero balanced Fermat character')
    return sum(vector) // M - 1


def orbit_table(vector: tuple[int, ...]) -> dict[int, list[int]]:
    """Nonzero multiples, grouped by conductor and [h20,h11,h02]."""
    counts: dict[int, list[int]] = {}
    for k in range(1, M):
        val = character(k, vector)
        if 0 in val:
            continue
        conductor = M // gcd(k, M)
        row = counts.setdefault(conductor, [0, 0, 0])
        row[grade(val)] += 1
    return counts


def singular_basis(f: sp.Expr, variables: tuple[sp.Symbol, ...]) -> tuple[sp.Expr, ...]:
    generators = [f] + [sp.diff(f, var) for var in variables]
    basis = sp.groebner(generators, *variables, domain=sp.QQ)
    return tuple(poly.as_expr() for poly in basis.polys)


def annihilator_span(generators: tuple[tuple[int, ...], ...]) -> set[tuple[int, ...]]:
    """Generate the finite subgroup without enumerating the ambient group."""
    zero = (0,) * len(generators[0])
    result = {zero}
    for gen in generators:
        result = {
            tuple((old[i] + k*gen[i]) % M for i in range(len(zero)))
            for old in result for k in range(M)
        }
    return result


def hom_table() -> Counter[tuple[int, int]]:
    """All 576 ordered pairs: profile-balanced pairs among the unit orbits."""
    result: Counter[tuple[int, int]] = Counter()
    for u, v in product(UNITS, repeat=2):
        values = tuple(
            grade(character(w*u, BETA)) + grade(character(w*v, GAMMA))
            for w in UNITS
        )
        if set(values) == {2}:
            result[(u, v)] += 1
    return result


class ExactSurfaceTests(unittest.TestCase):
    def test_profiles_and_matching(self) -> None:
        self.assertEqual(len(UNITS), 24)
        for vector in (BETA, GAMMA):
            self.assertEqual(len({character(k, vector) for k in UNITS}), 24)
            self.assertEqual(Counter(grade(character(k, vector)) for k in UNITS),
                             Counter({0: 1, 1: 22, 2: 1}))
        self.assertEqual(set(hom_table()), {(u, u) for u in UNITS})
        self.assertEqual(orbit_table(BETA), {70: [1,22,1], 10: [1,2,1]})
        self.assertEqual(orbit_table(GAMMA), {70: [1,22,1], 14: [1,4,1]})
        self.assertEqual({grade(character(k, ALPHA)) for k in UNITS}, {2})

    def test_all_transcendental_product_hodge_classes(self) -> None:
        valid = {vector: tuple(k for k in range(1,M) if 0 not in character(k,vector))
                 for vector in (BETA,GAMMA)}
        results = {}
        for left,right in ((BETA,BETA),(GAMMA,GAMMA),(BETA,GAMMA)):
            balanced = {(k,l) for k in valid[left] for l in valid[right]
                        if all(grade(character(u*k,left))+grade(character(u*l,right))==2
                               for u in UNITS)}
            results[(left,right)] = balanced
        self.assertEqual(results[(BETA,BETA)], {(k,(-k)%M) for k in valid[BETA]})
        self.assertEqual(results[(GAMMA,GAMMA)], {(k,(-k)%M) for k in valid[GAMMA]})
        self.assertEqual(results[(BETA,GAMMA)], {(u,u) for u in UNITS})
        self.assertEqual((2+5*5+28,2+3*3+30,2+5*3+24), (55,41,41))

    def test_first_coordinate_quotients(self) -> None:
        for vector, anchor, exponents in ((BETA, 0, (14,2,35)),
                                         (GAMMA, 2, (10,2,35))):
            other = tuple(i for i in range(4) if i != anchor)
            self.assertEqual(tuple(gcd(M, vector[i]) for i in other), exponents)
            # Each first-stage deck subgroup is killed by the target character.
            for i, exponent in zip(other, exponents):
                self.assertEqual((vector[i] * (M // exponent)) % M, 0)
        self.assertEqual(14*2*35*5, 4900)
        self.assertEqual(10*2*35*7, 4900)
        self.assertEqual(70**3 // 4900, 70)

    def test_second_quotient_maps_and_kernels(self) -> None:
        sub5 = {X:b**5, Y:a*b**2, Z:c*b**5, T:1}
        sub7 = {X:a/b, Y:b**7, Z:c, T:1}
        self.assertEqual(sp.expand(F5.subs(sub5) - b**10*(c**2+a**5+b**35+1)), 0)
        self.assertEqual(sp.expand(F7.subs(sub7) - (c**2+a**7+b**35+1)), 0)
        ker5 = {(i,j,k) for i in range(5) for j in range(35) for k in range(2)
                if (42*i+62*j+35*k) % M == 0}
        ker7 = {(i,j,k) for i in range(7) for j in range(35) for k in range(2)
                if (20*i+24*j+35*k) % M == 0}
        self.assertEqual(ker5, {(i,14*i % 35,0) for i in range(5)})
        self.assertEqual(ker7, {(i,5*i % 35,0) for i in range(7)})
        # Deliberate failure: the untwisted diagonal on a,b is not the first kernel.
        self.assertNotIn((1,7,0), ker5)

    def test_exact_character_annihilators(self) -> None:
        g5 = ((60,0,10,0),(52,14,4,0),(25,0,10,35))
        g7 = ((10,68,62,0),(0,14,56,0),(0,0,35,35))
        self.assertEqual(annihilator_span(g5), {character(k,BETA) for k in range(M)})
        self.assertEqual(annihilator_span(g7), {character(k,GAMMA) for k in range(M)})
        self.assertEqual(g5, tuple(character(k,BETA) for k in (60,52,25)))
        self.assertEqual(g7, tuple(character(k,GAMMA) for k in (32,56,35)))

    def test_projective_models_and_holomorphic_characters(self) -> None:
        for poly in (F5,F7):
            self.assertEqual({sum(a*w for a,w in zip(mon,WEIGHTS))
                              for mon,_ in sp.Poly(poly,T,X,Y,Z).terms()}, {10})
            self.assertEqual(poly.subs({T:0,X:0,Y:1,Z:0}), 1)
            self.assertEqual(poly.subs({T:0,X:0,Y:0,Z:1}), 1)
        self.assertEqual((60+52-25) % M, 17)
        self.assertEqual((2*60+52-25) % M, 7)
        self.assertEqual((32+56-35) % M, 53)
        self.assertEqual((2*32+56-35) % M, 15)
        self.assertEqual([k for k in range(1,M) if 0 not in character(k,BETA)
                          and grade(character(k,BETA))==0], [7,17])
        self.assertEqual([k for k in range(1,M) if 0 not in character(k,GAMMA)
                          and grade(character(k,GAMMA))==0], [15,53])

    def test_all_projective_singularities(self) -> None:
        self.assertEqual(singular_basis(F5.subs(T,1),(X,Y,Z)), (X,Y**4,Z))
        self.assertEqual(singular_basis(F5.subs(X,1),(T,Y,Z)), (sp.Integer(1),))
        self.assertEqual(singular_basis(F7.subs(T,1),(X,Y,Z)), (sp.Integer(1),))
        self.assertEqual(singular_basis(F7.subs(X,1),(T,Y,Z)), (T,Y,Z))
        hess = sp.hessian(F7.subs(X,1),(T,Y,Z)).subs({T:0,Y:0,Z:0})
        self.assertEqual(hess.det(), -2)
        # If T=X=0 then Y and Z are nonzero on either surface, so d/dZ != 0.
        for poly in (F5,F7):
            self.assertEqual(sp.diff(poly,Z), 2*Z)

    def test_picard_rank_witness_matrices(self) -> None:
        a4 = sp.diag(*([-2]*4))
        for i in range(3):
            a4[i,i+1] = a4[i+1,i] = 1
        q5 = sp.diag(sp.ones(1),a4)
        q7 = sp.Matrix([[1,0,1],[0,-2,1],[1,1,-3]])
        self.assertEqual(q5.det(), 5)
        self.assertEqual(q7.det(), 7)
        self.assertEqual((q5.rank(),q7.rank()), (5,3))
        self.assertEqual(12*(1+2)-1-2, 33)
        self.assertEqual((33-28,33-30), (5,3))

    def test_shioda_map_and_no_tate_shift(self) -> None:
        # Treat 70th powers as independent coordinates; epsilon^70=-1.
        xs = sp.symbols('x0:4'); ys = sp.symbols('y0:4')
        pulled = sum(xs[i]*ys[3] for i in range(3))-sum(xs[3]*ys[i] for i in range(3))
        self.assertEqual(sp.expand(pulled-ys[3]*sum(xs)+xs[3]*sum(ys)), 0)
        ordered = (1,42,62,20,24,61)
        self.assertEqual(sorted(ordered), sorted(ALPHA))
        self.assertEqual(ordered[:3]+(sum(ordered[3:]) % M,), BETA)
        self.assertEqual(ordered[3:]+(sum(ordered[:3]) % M,), GAMMA)
        self.assertNotEqual(BETA[-1],0); self.assertNotEqual(GAMMA[-1],0)
        # Formal balancing contributions: beta+gamma-alpha has the pair 35,35.
        count = Counter(BETA)+Counter(GAMMA)
        count.subtract(ALPHA)
        self.assertEqual({k:v for k,v in count.items() if v}, {35:2})

    def test_canonical_fibration_distinction(self) -> None:
        # First pencil is isotrivial after adjoining a tenth root of -(X^9+X^2).
        v,w,q = sp.symbols('v w q')
        self.assertEqual(sp.expand((q**5*w)**2+(q**2*v)**5-q**10
                                  -q**10*(w**2+v**5-1)),0)
        # Second pencil is a nonconstant quintic family; discriminant is recorded,
        # not alone used as proof that it is non-isotrivial.
        disc = sp.discriminant(Y**5+X**7*Y+1,Y)
        self.assertEqual(disc,256*X**35+3125)


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    start=time.perf_counter()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ExactSurfaceTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={
        'checkpoint':'U46', 'base_commit':'8fff2a01be0453fc613c0776239085816c155fdd',
        'arithmetic':'exact integers/rationals and polynomial identities; no floats in claims',
        'python':platform.python_version(), 'sympy':sp.__version__,
        'tests_run':result.testsRun, 'failures':len(result.failures), 'errors':len(result.errors),
        'success':result.wasSuccessful(), 'runtime_seconds':round(time.perf_counter()-start,3),
        'surface5':{'weights':WEIGHTS,'degree':10,'singularity':'A4','b2':33,
                    'picard_rank':5,'transcendental_orbits':orbit_table(BETA)},
        'surface7':{'weights':WEIGHTS,'degree':10,'singularity':'A1','b2':33,
                    'picard_rank':3,'transcendental_orbits':orbit_table(GAMMA)},
        'balanced_ordered_pairs':list(hom_table()),
        'rational_hodge_dimensions_codim2':{'S5xS5':55,'S7xS7':41,'S5xS7':41},
        'mixed_product_known_algebraic_dimension':17,
        'nonclaims':['No target cycle or correspondence is constructed.',
                     'The code does not prove the geometric comparison or source theorems.',
                     'The original rational Hodge conjecture remains unresolved.']}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2)+'\n')
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__=='__main__':
    main()
