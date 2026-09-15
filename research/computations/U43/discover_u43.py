"""Optional SymPy discovery of the U43 integral certificate, not its checker.

Runs a Smith decomposition of the stated 70-by-91 matrix. It reads the pinned
U42 arithmetic implementation only for generator construction. The decisive
verify_u43.py neither imports this solver nor reads this discovery output.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

from sympy import Matrix, ZZ, zeros
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.matrices import DomainMatrix


def main() -> None:
    here = Path(__file__).resolve().parent
    inherited = here.parent / "U42" / "verify_u42.py"
    spec = importlib.util.spec_from_file_location("u42_discovery_inputs", inherited)
    if spec is None or spec.loader is None:
        raise RuntimeError("Pinned U42 generator implementation was not available")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    labels: list[list[str | int]] = []
    columns: list[list[int]] = []
    for a in range(1, 36):
        v = list(module.reflection(a))
        v[-1] = -1
        labels.append(["R", a])
        columns.append(v)
    for n in (2, 5, 7):
        for a in range(1, 70 // n):
            labels.append(["D", n, a])
            columns.append(list(module.multiplication(n, a)))
    matrix = Matrix(columns).T
    d0, u0, v0 = smith_normal_decomp(DomainMatrix.from_Matrix(matrix).convert_to(ZZ))
    d, u, v = d0.to_Matrix(), u0.to_Matrix(), v0.to_Matrix()
    if u * matrix * v != d or abs(u.det()) != 1 or abs(v.det()) != 1:
        raise ArithmeticError("Smith change of basis failed exact validation")
    target = Matrix(module.exponent_vector([(3 * a % 70, 1) for a in module.ALPHA]))
    target -= Matrix(module.exponent_vector([(a, 1) for a in module.ALPHA]))
    rhs = u * target
    solution = zeros(matrix.cols, 1)
    for i in range(matrix.rows):
        if d[i, i] == 0:
            if rhs[i] != 0:
                raise ArithmeticError("Target is outside the rational relation span")
        else:
            value = rhs[i] / d[i, i]
            if value.is_Integer is not True:
                raise ArithmeticError("Target requires nonintegral coefficients")
            solution[i] = value
    coefficients = v * solution
    if matrix * coefficients != target:
        raise ArithmeticError("Discovered relation does not match target")
    result = {
        "labels": labels,
        "coefficient_for_3": [int(a) for a in coefficients],
        "smith_diagonal": [int(d[i, i]) for i in range(matrix.rows)],
        "shape": list(matrix.shape),
    }
    recorded = json.loads((here / "discovery_smith.json").read_text())
    if result != recorded:
        raise ArithmeticError("Solver output differs from the preserved discovery record")
    print("Exact Smith identity, unimodularity, integral solution, and recorded certificate match.")


if __name__ == "__main__":
    main()
