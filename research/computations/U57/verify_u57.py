"""Exact arithmetic checks for U57.

This verifies the explicit conic identities, the first-Witt obstruction, and the
finite diagonal-incidence/Fourier detection. It does not prove the deformation-
theoretic interpretation or the Hodge conjecture.
"""
from __future__ import annotations

from math import comb

P = 139
MOD = 140
BETA = (2, 84, 124, 70)      # pullback 2*beta at level 140
GAMMA = (40, 48, 122, 70)    # pullback 2*gamma at level 140


def mul(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    # F_{139^2}=F_139[u]/(u^2-2), where 2 is a nonsquare mod 139.
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % P,
            (x[0] * y[1] + x[1] * y[0]) % P)


def inv(x: tuple[int, int]) -> tuple[int, int]:
    den = (x[0] * x[0] - 2 * x[1] * x[1]) % P
    di = pow(den, P - 2, P)
    return (x[0] * di % P, (-x[1]) * di % P)


def div(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return mul(x, inv(y))


def fpow(x: tuple[int, int], n: int) -> tuple[int, int]:
    out = (1, 0)
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n >>= 1
    return out


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def sub(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return ((x[0] - y[0]) % P, (x[1] - y[1]) % P)


def scalar(c: int, x: tuple[int, int]) -> tuple[int, int]:
    return (c * x[0] % P, c * x[1] % P)


def poly_remainder_monic(coeffs: list[int], divisor: list[int]) -> list[int]:
    out = coeffs[:]
    while len(out) >= len(divisor):
        lead = out[-1]
        if lead:
            shift = len(out) - len(divisor)
            for i, c in enumerate(divisor):
                out[i + shift] -= lead * c
        while out and out[-1] == 0:
            out.pop()
    return out


def phi140_coeffs() -> list[int]:
    # ascending coefficients of Phi_140(x)
    out = [0] * 49
    for e, c in {
        0: 1, 2: 1, 10: -1, 12: -1, 14: -1, 16: -1,
        20: 1, 22: 1, 24: 1, 26: 1, 28: 1,
        32: -1, 34: -1, 36: -1, 38: -1, 46: 1, 48: 1,
    }.items():
        out[e] = c
    return out


def intersection_triples() -> list[tuple[int, int, int]]:
    # w=(136+137u) has exact order 140 in F_{139^2}.
    w = (136, 137)
    assert fpow(w, 140) == (1, 0)
    assert fpow(w, 70) == (138, 0)
    powers = [fpow(w, e) for e in range(140)]
    log = {z: e for e, z in enumerate(powers)}
    assert len(log) == 140

    zero = (0, 0)
    out: list[tuple[int, int, int]] = []
    for e0, l0 in enumerate(powers):
        for e1, l1 in enumerate(powers):
            den = sub((2, 0), add(l0, l1))
            num = sub(add(l0, l1), scalar(2, mul(l0, l1)))
            if den == zero:
                if num == zero:
                    out.extend((e0, e1, e2) for e2 in range(140))
                continue
            l2 = div(num, den)
            if l2 in log:
                out.append((e0, e1, log[l2]))
    return out


def fourier_remainder(chi: tuple[int, int, int, int], triples: list[tuple[int, int, int]]) -> list[int]:
    counts = [0] * MOD
    for e0, e1, e2 in triples:
        k = (chi[0] * e0 + chi[1] * e1 + chi[2] * e2) % MOD
        counts[k] += 1
    # identity was counted as an ordinary transverse intersection +1; replace by L^2=-138.
    counts[0] -= 139
    return poly_remainder_monic(counts, phi140_coeffs())


def defect_coefficient(k: int) -> int:
    # coefficient of s^(140-k)t^k in (sum q_i^70)/139, reduced mod 139.
    total = 69**70 * comb(140, k) * (((-1) ** k) + 1)
    if k == 0:
        total += 1
    if k == 140:
        total += 1
    assert total % P == 0
    return (total // P) % P


def linear_power_coeff(sign: int, k: int) -> int:
    # coefficient of s^(138-k)t^k in 69^69(s + sign*t)^138 mod p.
    return pow(69, 69, P) * comb(138, k) * pow(sign, k, P) % P


def correction_functional_values() -> list[int]:
    # ell = coeff_{s^136 t^4} - coeff_{s^134 t^6}
    values: list[int] = []
    for i in range(4):
        for shift in range(3):  # multiply by s^2, st, t^2
            if i == 0:
                def base(j: int) -> int: return linear_power_coeff(-1, j)
            elif i == 1:
                def base(j: int) -> int: return linear_power_coeff(1, j)
            elif i == 2:
                def base(j: int) -> int: return 1 if j == 0 else 0
            else:
                def base(j: int) -> int: return 1 if j == 138 else 0
            c4 = 70 * (base(4 - shift) if 0 <= 4 - shift <= 138 else 0) % P
            c6 = 70 * (base(6 - shift) if 0 <= 6 - shift <= 138 else 0) % P
            values.append((c4 - c6) % P)
    return values


def main() -> None:
    # Basic explicit conic identities.
    assert 25 * 25 % P == 69
    # q0+q1+q2+q3 and (q0-q1)^2-4q2q3 vanish coefficientwise mod p;
    # the scalar reductions are 2*69+1 = 0 and (-4*69)^2 = 4.
    assert (2 * 69 + 1) % P == 0
    assert ((-4 * 69) ** 2 - 4) % P == 0

    d4 = defect_coefficient(4)
    d6 = defect_coefficient(6)
    assert (d4, d6) == (81, 88)
    assert (d4 - d6) % P == 132
    vals = correction_functional_values()
    assert vals == [0] * 12

    triples = intersection_triples()
    assert len(triples) == 19739
    rb = fourier_remainder(BETA, triples)
    rg = fourier_remainder(GAMMA, triples)
    assert any(rb)
    assert any(rg)

    print({
        "p": P,
        "intersecting_diagonal_translates": len(triples),
        "beta_fourier_remainder_nonzero": bool(any(rb)),
        "gamma_fourier_remainder_nonzero": bool(any(rg)),
        "defect_coefficients_t4_t6": [d4, d6],
        "defect_functional": (d4 - d6) % P,
        "all_12_correction_functionals_zero": all(v == 0 for v in vals),
        "beta_remainder": rb,
        "gamma_remainder": rg,
    })


if __name__ == "__main__":
    main()
