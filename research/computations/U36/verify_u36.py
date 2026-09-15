"""Exact certificate checks for U36; the uniform proof is in the research note.

Run from the repository root:
    python research/computations/U36/verify_u36.py
Requires SymPy. No network access, numerical convex hulls, or sampling is used.
"""
from __future__ import annotations

import hashlib
import json
import platform
import sys
import time
import unittest
from itertools import combinations
from math import gcd
from pathlib import Path

import sympy as sp

BASE_COMMIT = "7fea00517efe485776cadc7b482ff3f426b0ecc3"
ALPHA = (1, 20, 24, 42, 61, 62)
R = (2, 2, -3, -1, -1, 1)
S = (3, 0, -3, 1, -2, 1)
POINTS = ((-4, 3, 3), (1, 0, 0), (0, 1, 0),
          (0, 0, 1), (-6, 3, 5), (0, 0, 0))
EXPECTED_FACETS = {
    (0, 1, 2): ((-3, -3, -2), -3),
    (0, 1, 3, 4): ((-3, -2, -3), -3),
    (0, 2, 5): ((3, 0, 4), 0),
    (0, 4, 5): ((3, 1, 3), 0),
    (1, 2, 5): ((0, 0, 1), 0),
    (1, 3, 5): ((0, 1, 0), 0),
    (3, 4, 5): ((1, 2, 0), 0),
}
EXPECTED_LEADING = {
    (3, 0, 0, 1, 0, 1), (2, 2, 0, 0, 0, 1),
    (1, 4, 0, 0, 0, 1), (1, 0, 0, 2, 0, 0),
    (0, 6, 0, 0, 1, 1),
}
Z = sp.symbols("z0:6")
T = sp.Symbol("t")


def facets(points: tuple[tuple[int, ...], ...]) -> dict:
    """Enumerate supporting planes through every noncollinear vertex triple."""
    vectors = [sp.Matrix(p) for p in points]
    result = {}
    for triple in combinations(range(len(points)), 3):
        a, b, c = [vectors[i] for i in triple]
        normal = (b - a).cross(c - a)
        if normal == sp.zeros(3, 1):
            continue
        values = [int(normal.dot(p - a)) for p in vectors]
        if all(v >= 0 for v in values):
            pass
        elif all(v <= 0 for v in values):
            normal = -normal
            values = [-v for v in values]
        else:
            continue
        divisor = gcd(*(abs(int(v)) for v in normal))
        normal = normal / divisor
        on_plane = tuple(i for i, value in enumerate(values) if value == 0)
        result[on_plane] = (tuple(int(v) for v in normal), int(normal.dot(a)))
    return result


def triangle_reach(face_data: dict, anchor: tuple[int, ...]) -> set[int]:
    """Vertices reached through triangular facets sharing full edges."""
    triangles = {face for face in face_data if len(face) == 3}
    if anchor not in triangles:
        return set()
    reached = {anchor}
    while True:
        added = {face for face in triangles - reached
                 if any(len(set(face) & set(old)) == 2 for old in reached)}
        if not added:
            return set().union(*(set(face) for face in reached))
        reached.update(added)


def saturation_basis() -> list:
    z0, z1, z2, z3, z4, z5 = Z
    aux = sp.Symbol("saturation_aux")
    f = z0**2 * z1**2 * z5 - z2**3 * z3 * z4
    g = z0**3 * z3 * z5 - z2**3 * z4**2
    basis = sp.groebner([f, g, aux * sp.prod(Z) - 1], aux, *Z, order="lex")
    return [p.as_expr() for p in basis.polys if not p.as_expr().has(aux)]


def hilbert_numerator(leading: set[tuple[int, ...]]) -> sp.Expr:
    """Inclusion-exclusion for the monomial initial ideal in six variables."""
    monomials = sorted(leading)
    result = sp.Integer(0)
    for count in range(len(monomials) + 1):
        for chosen in combinations(monomials, count):
            lcm_degree = sum(max((monomial[j] for monomial in chosen), default=0)
                             for j in range(6))
            result += (-1)**count * T**lcm_degree
    return sp.expand(result)


def normalized_volume() -> sp.Expr:
    """Exact coning to the centroid; split the sole quadrilateral along 0--3."""
    points = [sp.Matrix(p) for p in POINTS]
    normal = sp.Matrix(EXPECTED_FACETS[(0, 1, 3, 4)][0])
    diagonal = points[3] - points[0]
    side1 = diagonal.cross(points[1] - points[0]).dot(normal)
    side4 = diagonal.cross(points[4] - points[0]).dot(normal)
    if side1 * side4 >= 0:
        raise AssertionError("Quadrilateral diagonal does not separate its other vertices")
    triangles = [f for f in EXPECTED_FACETS if len(f) == 3]
    triangles += [(0, 1, 3), (0, 3, 4)]
    center = sum(points, sp.zeros(3, 1)) / 6
    return sum(abs(sp.det(sp.Matrix.hstack(*(points[i] - center for i in tri))))
               for tri in triangles)


class CertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.basis = saturation_basis()
        cls.leading = {sp.Poly(p, *Z).monoms()[0] for p in cls.basis}
        cls.faces = facets(POINTS)

    def test_01_target_and_saturation(self) -> None:
        self.assertEqual(sum(R), 0)
        self.assertEqual(sum(S), 0)
        self.assertEqual(tuple((45*r + 17*s - a) % 70
                              for r, s, a in zip(R, S, ALPHA)), (0,)*6)
        self.assertEqual(sp.Matrix([R, S])[:, [0, 4]].det(), -1)

    def test_02_parametrization(self) -> None:
        u, v, w, lam, mu = sp.symbols("u v w lam mu", nonzero=True)
        image = (lam**2/mu*v**3*w**3/u**4, u, v, w,
                 lam**3/mu**2*v**3*w**5/u**6, sp.Integer(1))
        self.assertEqual(sp.cancel(sp.prod(a**b for a, b in zip(image, R))), lam)
        self.assertEqual(sp.cancel(sp.prod(a**b for a, b in zip(image, S))), mu)
        for row in (R, S):
            self.assertEqual(tuple(sum(row[i]*POINTS[i][j] for i in range(6))
                                   for j in range(3)), (0, 0, 0))

    def test_03_saturation_and_degree(self) -> None:
        self.assertEqual(self.leading, EXPECTED_LEADING)
        numerator = hilbert_numerator(self.leading)
        hpoly = sp.cancel(numerator/(1-T)**2)
        self.assertEqual(sp.expand(hpoly), 1+2*T+3*T**2+3*T**3+3*T**4+T**5-T**6)
        self.assertEqual(hpoly.subs(T, 1), 12)
        # Independent monomial-ideal benchmark: two quintics have degree 25.
        benchmark = {(5, 0, 0, 0, 0, 0), (0, 5, 0, 0, 0, 0)}
        self.assertEqual(sp.limit(hilbert_numerator(benchmark)/(1-T)**2, T, 1), 25)

    def test_04_exact_faces(self) -> None:
        self.assertEqual(self.faces, EXPECTED_FACETS)
        self.assertEqual(sum(len(face) == 3 for face in self.faces), 6)
        self.assertEqual(sum(len(face) == 4 for face in self.faces), 1)
        self.assertEqual(sp.Matrix(POINTS[1:4]).det(), 1)

    def test_05_anchor_propagation(self) -> None:
        self.assertEqual(triangle_reach(self.faces, (1, 2, 5)), set(range(6)))
        for face, (normal, bound) in self.faces.items():
            values = [sum(a*b for a, b in zip(normal, p))-bound for p in POINTS]
            self.assertTrue(all(v >= 0 for v in values))
            self.assertEqual(tuple(i for i, v in enumerate(values) if v == 0), face)

    def test_06_reducible_prism_is_not_certified(self) -> None:
        # Newton polytope of (1+w)(1+u+v): its triangular faces are disconnected.
        prism = ((0, 0, 0), (1, 0, 0), (0, 1, 0),
                 (0, 0, 1), (1, 0, 1), (0, 1, 1))
        self.assertNotEqual(triangle_reach(facets(prism), (0, 1, 2)), set(range(6)))

    def test_07_anchor_and_nonempty_example(self) -> None:
        v, q = sp.symbols("v q")
        self.assertEqual(sp.gcd(v**70+1, 70*v**69), 1)
        self.assertEqual(sp.expand((q+1)*(2*q+1)), 1+3*q+2*q**2)
        self.assertEqual((1+3*q+2*q**2).subs(q, -1), 0)

    def test_08_exact_volume(self) -> None:
        self.assertEqual(normalized_volume(), 12)


def main() -> int:
    start = time.monotonic()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(CertificateTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        return 1
    basis = saturation_basis()
    numerator = hilbert_numerator(EXPECTED_LEADING)
    report: dict[str, object] = {
        "scope": "Exact finite certificates for the separately written U36 proof; not a proof of Hodge",
        "base_commit": BASE_COMMIT,
        "python_version": platform.python_version(),
        "sympy_version": sp.__version__,
        "arithmetic": "integers and rationals; no floating-point geometry",
        "alpha": ALPHA, "relations": [R, S], "exponent_points": POINTS,
        "saturated_groebner_basis": [str(p) for p in basis],
        "hilbert_numerator": str(numerator),
        "hilbert_h_polynomial": str(sp.cancel(numerator/(1-T)**2)),
        "toric_threefold_degree": 12,
        "normalized_polytope_volume": str(normalized_volume()),
        "surface_degree_at_70": 840,
        "facets": [{"vertices": f, "inward_normal": n, "bound": b}
                   for f, (n, b) in sorted(facets(POINTS).items())],
        "triangle_anchor": [1, 2, 5],
        "triangle_reached_vertices": sorted(triangle_reach(facets(POINTS), (1, 2, 5))),
        "tests_run": result.testsRun, "failures": len(result.failures),
        "errors": len(result.errors), "elapsed_seconds": time.monotonic()-start,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "proof_nonclaims": ["No formal verification or expert review", "No algebraicity result for alpha", "No exhaustive search of all surfaces"],
    }
    output = Path(__file__).with_name("verification.json")
    output.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
