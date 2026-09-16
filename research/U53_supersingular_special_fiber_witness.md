# U53: the missing block is algebraic in characteristic 139, but only through new supersingular divisor directions

**Status:** positive special-fiber result plus a precise lifting obstruction for the divisor-product realization. This does not construct a characteristic-zero cycle and does not solve the Hodge conjecture.

Date: 2026-09-16.

## 1. Supersingular prime

Take p=139. Then

    139 == -1 mod 70,
    139^2 == 1 mod 70.

Since p does not divide 70, the degree-70 Fermat varieties have good reduction.

Shioda-Katsura prove that if p^nu == -1 mod m for some nu and the Fermat variety has even dimension, then it is unirational; equivalently in their cycle-theoretic formulation, its even cohomology is spanned by algebraic cycles (the variety is fully rigged / Shioda-supersingular).

Therefore both

- the degree-70 Fermat surface F_70^2 over the algebraic closure of F_139, and
- the degree-70 Fermat fourfold X_70^4 over the algebraic closure of F_139

have all even l-adic cohomology spanned by algebraic cycles.

In particular the reduction of the target alpha block is algebraic in characteristic 139.

## 2. Relation to the U46 Horikawa reduction

U46 realizes the characteristic-zero missing block through two quotient characters on the same Fermat surface:

    beta  = (1,42,62,35),
    gamma = (20,24,61,35).

The quotient maps from F_70^2 to the canonical models S5_bar and S7_bar are generically finite of degree 4900, and resolution adds only divisor classes.

After reduction mod 139 and passage to the algebraic closure, H^2(F_70^2) is entirely algebraic. Pullback along each generically finite quotient is injective on rational l-adic H^2, while normalized pushforward is a left inverse. Hence every H^2 class on the quotient surfaces is algebraic after reduction; exceptional resolution classes are algebraic as well.

Thus the reductions of S5 and S7 are supersingular in the strong Picard-rank sense:

    rho(S5_barF_139)=b2(S5)=33,
    rho(S7_barF_139)=b2(S7)=33.

By comparison with the characteristic-zero ranks from U46,

    rho(S5_C)=5,
    rho(S7_C)=3,

there are respectively 28 and 30 additional divisor directions in the supersingular special fibers.

## 3. A concrete algebraic realization of the mixed block in the special fiber

Because every H^2 direction of each reduced surface is algebraic, the rank-24 pieces R5 and R7 become spanned by divisor classes after reduction. Consequently every class in

    R5 tensor R7 subset H^4(S5 x S7)

is represented over the algebraic closure of F_139 by rational combinations of products of divisors.

Under the algebraic correspondences of U46, this transports to an algebraic representative of the reduction of the original W_alpha block on X_70^4.

This is a genuine positive witness in characteristic 139. It is stronger than merely knowing that a Frobenius eigenvalue is a Tate eigenvalue: an explicit geometric reason supplies algebraic spanning, namely supersingularity of the Fermat source and the quotient correspondences.

## 4. Why the obvious lift fails

The divisor-product witness is intrinsically characteristic-p.

In characteristic zero, U46 proves that R5 and R7 are transcendental simple Hodge structures with no nonzero rational (1,1) subspace. Therefore no characteristic-zero divisor class on S5 or S7 can have nonzero R5 or R7 projection.

Hence the special divisors spanning R5 and R7 at p=139 cannot lift individually to divisor classes with the same cohomological components in characteristic zero. Any successful characteristic-zero lift of the mixed codimension-two class would have to be a genuinely coupled codimension-two cycle; it cannot be obtained by simply lifting the two divisor factors separately.

This is exactly compatible with U47-U48, which already rule out broad product/fibrewise constructions in characteristic zero.

## 5. Numerical checks

Exact arithmetic gives

    p mod 70 = 69,
    p^2 mod 70 = 1.

For reference, the degree-70 Fermat surface has

    b2 = m^3 - 4m^2 + 6m - 2 = 323818.

The quotient surfaces retain only 33 H^2 dimensions, all of which become algebraic in the supersingular reduction.

## 6. Research consequence

The existence problem has now been separated cleanly into two statements:

1. **special-fiber existence:** solved at p=139 (and at every prime satisfying p^nu == -1 mod 70);
2. **characteristic-zero lifting:** still open.

The next high-value route is therefore a lifting theorem for one of these special cycles, most plausibly through semiregularity/deformation of coherent sheaves or through an explicit matrix factorization whose reduction realizes the supersingular class and whose coefficients lift to characteristic zero.

A purely divisorwise lift cannot work because the needed divisor directions disappear from NS in characteristic zero.

## 7. Source

T. Shioda and T. Katsura, *On Fermat varieties*, Tohoku Math. J. 31 (1979), 97-115, especially the theorem that if p^nu == -1 mod m then an even-dimensional Fermat variety is unirational, together with their algebraic-cycle criterion for supersingularity. The same equivalence is restated in later literature as: an even-dimensional Fermat variety is fully rigged iff such a nu exists.
