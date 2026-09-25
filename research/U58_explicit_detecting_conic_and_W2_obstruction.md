# U58: an explicit conic detects both target surface characters but does not lift to W2

**Status:** the explicit character-detection and first-Witt nonlifting statements below are proved by exact finite-field/intersection arithmetic and a two-coefficient deformation obstruction. The conic and its product are special-fiber witnesses only; this does not construct the characteristic-zero target cycle or solve the Hodge conjecture.

Date: 2026-09-16. Base checkpoint: U57.

## 1. One explicit Hermitian line and its conic image

Work over an algebraic closure of F_139. Let

    H=X_140: x0^140+x1^140+x2^140+x3^140=0,
    F=X_70 : y0^70 +y1^70 +y2^70 +y3^70 =0,

and let pi:H->F be the coordinate-square map.

Since 25^2=69 and 2*69=-1 in F_139, the line

    L: [s:t] |-> [25(s+t):25(-s+t):s:t]                  (1.1)

lies on H. Indeed, in characteristic 139,

    (s+t)^140+(t-s)^140 = 2(s^140+t^140),

and multiplying by 25^140=25^2=69 gives exactly -(s^140+t^140).

Its square-map image is

    C: [s:t] |-> [69(s+t)^2:69(t-s)^2:s^2:t^2].          (1.2)

The image satisfies

    y0+y1+y2+y3=0,
    (y0-y1)^2=4 y2 y3.                                   (1.3)

Because the coordinate quadrics in (1.2) span s^2,st,t^2 and char(k)!=2, this is the 2-uple Veronese embedding of P^1 into its plane. Thus C is a smooth plane conic and pi|_L has degree one.

## 2. Exact Fourier test for beta and gamma

Keep the U46 surface characters

    beta =(1,42,62,35),
    gamma=(20,24,61,35) mod70.

Under the square map the corresponding characters upstairs are

    2 beta =(2,84,124,70),
    2 gamma=(40,48,122,70) mod140.

Let G_140=mu_140^4/mu_140. Fix representatives

    g=diag(x,y,z,1),  x,y,z in mu_140.

For L from (1.1), an exact 4x4 determinant gives

    L intersects gL

if and only if

    2xy-xz-x-yz-y+2z=0.                                  (2.1)

Choose F_139^2=F_139[i], i^2=-1, and zeta=3+39i. Exact arithmetic verifies that zeta has order 140. For x=zeta^i,y=zeta^j, equation (2.1) has

    z=(x+y-2xy)/(2-x-y)

unless (x,y)=(1,1), in which case every z in mu_140 is a solution.

The complete enumeration gives

    19,599 regular solutions,
    140 exceptional solutions,
    19,739 total diagonal translates meeting L (including L itself).

For distinct lines on the smooth degree-140 surface, the intersection is 1 if they meet and 0 otherwise, while

    L^2=2-140=-138.

For a character chi of G_140 define the Fourier pairing numerator

    S_chi = sum_(g in G_140) chi(g) <L,gL>.               (2.2)

If the chi-projector of [L] were zero, then S_chi would be zero.

To certify nonvanishing exactly without numerical complex approximations, reduce Z[zeta_140] modulo 281. The element 5 in F_281 has exact order 140, so zeta_140 |-> 5 defines a cyclotomic specialization. The exact census gives

    S_(2 beta)  mod281 = 134,
    S_(2 gamma) mod281 = 175.                             (2.3)

Both are nonzero. Hence [L] has nonzero 2 beta and 2 gamma eigenspace projections on H.

The kernel of G_140 -> G_70 induced by squaring has order 8, and both 2 beta and 2 gamma are trivial on it. For a finite quotient,

    pi^* pi_* = sum_(h in kernel) h_*,

so on either of these eigenspaces pi^*pi_* acts as multiplication by 8. Therefore pi_* cannot kill either nonzero component. Since pi|_L has degree one,

    **the single conic C has nonzero beta projection and nonzero gamma projection in H^2(F).**

Thus Z=C x C in F x F already has a nonzero beta tensor gamma component.

## 3. The conic does not lift to the first Witt thickening

Now take the standard smooth Fermat model over W_2(F_139). Use the integer lift of (1.2)

    y0=69(s+t)^2,
    y1=69(t-s)^2,
    y2=s^2,
    y3=t^2.                                               (3.1)

Every first-order deformation of this embedded conic is represented, after trivializing the abstract deformation of P^1, by

    Y_i = y_i + 139 q_i,

where each q_i is a binary quadratic. This 12-parameter description surjects onto the embedded Hilbert tangent space: the four quadratic sections give 12 parameters, and quotienting by common scaling plus the 3-dimensional infinitesimal automorphism group of P^1 leaves 8=h^0(N_(C/P3)).

Modulo 139^2, the Fermat equation becomes

    (F(y)/139) + 70 sum_i y_i^69 q_i = 0 mod139.           (3.2)

Compare the coefficients of

    s^136 t^4  and  s^134 t^6.

For **every** choice of the twelve coefficients of q_i, the two coefficient rows of the linear correction term in (3.2) are identical:

    (70,69,70,70,70,70,0,0,0,0,0,0).                    (3.3)

But the divided Fermat defect F(y)/139 has respective coefficients

    81 and 88 mod139.                                     (3.4)

Therefore (3.2) is inconsistent. Consequently

    **C has no embedded lift to W_2(F_139) inside the degree-70 Fermat surface.**

The obstruction certificate is only the difference of these two equations: every possible first-order correction contributes zero to their difference, whereas the fixed defect contributes

    81-88 = 132 !=0 mod139.

A separate Wolfram expansion independently reproduces (3.3)-(3.4).

## 4. The raw product witness also cannot lift

Let P=P^3 x P^3 and Z=C x C. Its ambient normal bundle splits:

    N_(Z/P)=p_1^*N_(C/P3) direct-sum p_2^*N_(C/P3).

Since H^0(C,O_C)=k,

    H^0(N_(Z/P))=H^0(N_(C/P3)) direct-sum H^0(N_(C/P3)).

The two defining Fermat equations of F x F depend on separate coordinate factors. Hence the first-order containment equations for an embedded W_2-lift of Z split into two copies of the conic lifting system (3.2). Since that system is inconsistent, Z itself has no embedded W_2 lift.

This is compatible with U57: Z is semiregular **as a special-fiber lci**, but the all-obstruction semiregularity theorems used in characteristic zero do not apply to this mixed-characteristic lifting problem.

## 5. Research consequence

U58 gives an unusually explicit picture of the remaining gap:

- one low-degree conic simultaneously detects beta and gamma;
- its product has a nonzero target mixed component;
- the product is semiregular on the special fiber by U57;
- nevertheless the actual conic and raw product fail already over W_2;
- U55 still gives a formal K_0 lift of the **character-projected target class**.

Therefore the correct mixed-characteristic object cannot simply be the raw geometric product C x C. It must exploit cancellation between translates/complexes after projecting to the rational beta tensor gamma orbit, exactly where the K_0 formal lift exists.

The next constructive target is an actual perfect complex on the special fiber whose K_0 class is the rational target projection of [O_(C x C)] and whose deformation obstructions can be controlled objectwise. A compatible formal perfect complex would algebraize by formal GAGA and would close the degree-70 block.

## 6. Exact checker

`research/computations/U58/verify_u58.py` is a standard-library implementation of:

- F_139^2 arithmetic and the full 19,739-line incidence census;
- the exact mod-281 Fourier certificates 134 and 175;
- the W_2 coefficient obstruction 81 versus 88.

## Literature correction (2026-09-24)

Kang (2016), Corollary 3.2, proves the rational Hodge conjecture for every four-dimensional Fermat variety `X_m^4`, all positive degrees; Remark 4.4(1) makes the unrestricted degree scope explicit. Thus the degree-70 target Hodge class is algebraic over `C`, even though this particular conic and its raw product do not lift as embedded subschemes to `W_2`. U58's obstruction is construction-specific and does not show that no other characteristic-zero cycle represents the target class. The theorem and exact notation translation are recorded in [U59](U59_kang_closes_degree70_fermat_fourfold.md).

Python syntax compilation passes in the local runtime. Ruff and mypy are not installed there, so no lint/static-type success is claimed.
