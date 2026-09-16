"""Exact finite checks for U58. Standard library only.

This verifies:
- the explicit Hermitian line and conic equations in characteristic 139;
- the line-intersection census under the diagonal mu_140^4/mu_140 action;
- nonzero 2*beta and 2*gamma Fourier pairings, certified modulo 281;
- the two-coefficient obstruction to lifting the conic to W_2(F_139).

It does not verify the external geometric facts about cycle projectors or formal GAGA.
"""
from __future__ import annotations

from math import comb

P = 139
MOD = 140
ELL = 281
ROOT_ELL = 5  # exact order 140 mod 281
BETA = (1, 42, 62, 35)
GAMMA = (20, 24, 61, 35)

# F_{139^2}=F_139[i], i^2=-1 (irreducible because 139 == 3 mod 4).
F = tuple[int, int]


def add(x: F, y: F) -> F:
    return ((x[0] + y[0]) % P, (x[1] + y[1]) % P)


def sub(x: F, y: F) -> F:
    return ((x[0] - y[0]) % P, (x[1] - y[1]) % P)


def mul(x: F, y: F) -> F:
    return ((x[0] * y[0] - x[1] * y[1]) % P,
            (x[0] * y[1] + x[1] * y[0]) % P)


def power(x: F, n: int) -> F:
    out = (1, 0)
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n //= 2
    return out


def inv(x: F) -> F:
    den = (x[0] * x[0] + x[1] * x[1]) % P
    if not den:
        raise ZeroDivisionError
    d = pow(den, -1, P)
    return (x[0] * d % P, -x[1] * d % P)


def div(x: F, y: F) -> F:
    return mul(x, inv(y))


def order_mod(a: int, m: int) -> int:
    x = 1
    for n in range(1, m + 1):
        x = x * a % m
        if x == 1:
            return n
    raise AssertionError("order not found")


def intersection_census() -> tuple[list[tuple[int, int, int]], int]:
    # zeta=3+39i has exact order 140.
    zeta = (3, 39)
    assert power(zeta, 140) == (1, 0)
    for q in (2, 4, 5, 7):
        assert power(zeta, 140 // q) != (1, 0)
    roots = [power(zeta, i) for i in range(140)]
    index = {z: i for i, z in enumerate(roots)}
    assert len(index) == 140

    # For g=diag(x,y,z,1), L intersects gL iff
    # 2xy-xz-x-yz-y+2z=0. Away from x=y=1 solve uniquely for z.
    two = (2, 0)
    regular: list[tuple[int, int, int]] = []
    exceptional_all = 0
    for i, x in enumerate(roots):
        for j, y in enumerate(roots):
            den = sub(two, add(x, y))
            num = sub(add(x, y), mul(two, mul(x, y)))
            if den == (0, 0):
                assert i == 0 and j == 0 and num == (0, 0)
                exceptional_all += 140
                continue
            zz = div(num, den)
            k = index.get(zz)
            if k is not None:
                regular.append((i, j, k))
    assert len(regular) == 19_599
    assert exceptional_all == 140
    return regular, exceptional_all


def pairing_mod_281(char: tuple[int, int, int, int],
                    regular: list[tuple[int, int, int]]) -> int:
    # Sum chi(g)<L,gL>. Distinct intersecting lines contribute 1;
    # L^2=2-140=-138, so replace the identity's provisional +1 by -138.
    value = 0
    for i, j, k in regular:
        e = (char[0] * i + char[1] * j + char[2] * k) % 140
        value = (value + pow(ROOT_ELL, e, ELL)) % ELL
    # Exceptional x=y=1: every k works.
    for k in range(140):
        e = (char[2] * k) % 140
        value = (value + pow(ROOT_ELL, e, ELL)) % ELL
    value = (value - 139) % ELL
    return value


def derivative_row(k: int) -> tuple[int, ...]:
    # Coefficient of s^(140-k)t^k in 70*y_i^69*q,
    # q in {s^2,st,t^2}, with
    # y0=69(s+t)^2, y1=69(t-s)^2, y2=s^2,y3=t^2.
    row: list[int] = []
    for which in range(4):
        for shift in (0, 1, 2):
            kk = k - shift
            if not 0 <= kk <= 138:
                row.append(0)
                continue
            if which == 0:
                c = 70 * pow(69, 69, P) * comb(138, kk)
            elif which == 1:
                c = 70 * pow(69, 69, P) * comb(138, kk) * ((-1) ** (138 - kk))
            elif which == 2:
                c = 70 if kk == 0 else 0
            else:
                c = 70 if kk == 138 else 0
            row.append(c % P)
    return tuple(row)


def defect(k: int) -> int:
    # Coefficient of s^(140-k)t^k in F(y)/139 mod139.
    # For 0<k<140 even only the first two coordinates contribute.
    assert k % 2 == 0 and 0 < k < 140
    coefficient = 2 * (69 ** 70) * comb(140, k)
    assert coefficient % P == 0
    return (coefficient // P) % P


def main() -> None:
    # a=b=25 gives a^2+b^2=-1 mod139, so the line
    # [25(s+t):25(-s+t):s:t] lies on X_140.
    assert (25 * 25) % P == 69
    assert (2 * 69) % P == P - 1

    # The square image is the smooth conic
    # y0+y1+y2+y3=0, (y0-y1)^2=4y2y3.
    assert (4 * 69) % P == -2 % P

    regular, exceptional = intersection_census()
    assert exceptional == 140
    assert order_mod(ROOT_ELL, ELL) == 140

    beta2 = tuple((2 * a) % 140 for a in BETA)
    gamma2 = tuple((2 * a) % 140 for a in GAMMA)
    beta_pair = pairing_mod_281(beta2, regular)
    gamma_pair = pairing_mod_281(gamma2, regular)
    assert beta_pair == 134
    assert gamma_pair == 175
    assert beta_pair and gamma_pair

    # W2 obstruction: all first-order corrections have equal k=4 and k=6
    # derivative rows, but the divided Fermat defect does not.
    row4 = derivative_row(4)
    row6 = derivative_row(6)
    expected_row = (70, 69, 70, 70, 70, 70, 0, 0, 0, 0, 0, 0)
    assert row4 == row6 == expected_row
    d4, d6 = defect(4), defect(6)
    assert (d4, d6) == (81, 88)
    assert d4 != d6

    print({
        "regular_intersections": len(regular),
        "exceptional_intersections": exceptional,
        "total_intersections_including_identity": len(regular) + exceptional,
        "beta_fourier_pairing_mod_281": beta_pair,
        "gamma_fourier_pairing_mod_281": gamma_pair,
        "w2_derivative_row_4": row4,
        "w2_derivative_row_6": row6,
        "w2_defect_4": d4,
        "w2_defect_6": d6,
        "conic_lifts_to_W2": False,
    })


if __name__ == "__main__":
    main()
