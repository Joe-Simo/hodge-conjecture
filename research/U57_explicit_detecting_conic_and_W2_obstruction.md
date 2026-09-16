# U57: an explicit beta/gamma-detecting conic and its first Witt obstruction

**Status:** the explicit special-fiber conic, its nonzero beta/gamma character projections, and its failure to lift as a conic even to W_2 are proved below by exact arithmetic and deformation theory. This is a construction obstruction, not a proof or counterexample to the Hodge conjecture.

Date: 2026-09-16.

## 1. Setup

Work over k=\bar F_139. Put

    F : y0^70+y1^70+y2^70+y3^70=0 in P^3_k.

Use the U46 surface characters

    beta  = (1,42,62,35),
    gamma = (20,24,61,35)          mod 70.

U56 used the finite square map from the Hermitian surface

    H=X_140 -> F,
    [x_i] |-> [x_i^2].

Since 25^2=69=-1/2 mod 139, the line

    L : [s:t] |-> [25(s-t):25(s+t):s:t]

lies on H. Indeed in characteristic 139,

    (s+t)^140+(s-t)^140 = 2(s^140+t^140)

because 140=139+1, while 25^140=(25^2)^70=69. Hence the four 140th powers sum to

    69*2(s^140+t^140)+s^140+t^140=0.

Its image C=pi(L) is the smooth conic parametrized by

    q0=69(s-t)^2,
    q1=69(s+t)^2,
    q2=s^2,
    q3=t^2.

Equivalently C is cut out by

    y0+y1+y2+y3=0,
    (y0-y1)^2=4 y2 y3.

The two displayed equations and the Fermat equation hold identically mod 139.

## 2. Exact character detection upstairs

Let A=(mu_140)^4/mu_140 act diagonally on H. Fix the fourth diagonal coordinate to 1. If

    g=diag(lambda0,lambda1,lambda2,1),

then L and gL meet exactly when

    2 lambda0 lambda1 - lambda0 lambda2 - lambda0
      - lambda1 lambda2 - lambda1 + 2 lambda2 = 0.      (2.1)

This is the determinant of the four column vectors spanning L and gL, up to a nonzero scalar. The diagonal stabilizer of L is trivial after fixing lambda3=1, so the intersection number is -138 at the identity, 1 for every other solution of (2.1), and 0 otherwise.

The exact checker works in F_{139^2}, chooses a primitive 140th root w, and enumerates (e0,e1) in (Z/140)^2. Except at (0,0), equation (2.1) determines at most one lambda2; at (0,0) every lambda2 is a solution. There are exactly

    19,739

intersecting diagonal translates, including the identity.

For a level-140 character chi define the Fourier intersection sum

    S_chi = sum_g (L . gL) chi(g).

Reducing the corresponding Laurent sum modulo Phi_140 gives a nonzero element for both

    2 beta  = (2,84,124,70),
    2 gamma = (40,48,122,70).

Therefore the 2beta and 2gamma projections of [L] are nonzero: if one projection vanished, its pairing with the inverse-character projection would force the corresponding Fourier sum to vanish.

The square map is the quotient by the sign deck group (mu_2)^4/mu_2 of order 8. Both 2beta and 2gamma are trivial on this deck group, and L has trivial deck stabilizer. Thus

    pi^*[C] = sum_h h[L]

has nonzero 2beta and 2gamma components. Equivalently, the conic C itself has nonzero beta and gamma projections in H^2(F).

This makes C a single explicit low-degree detector for both factors of the missing U46 mixed class.

## 3. No lift to the first Witt thickening

Let W_2=W_2(k). Suppose C lifted flatly as a degree-two curve inside the degree-70 Fermat surface over W_2. The special fiber is a smooth conic, hence any such flat lift is smooth over W_2. It has a lifted point, so it is P^1_{W_2}; the embedding line bundle has degree 2. After choosing homogeneous coordinates on P^1, every embedded lift is therefore parametrized by four quadratic forms

    Q_i = q_i + 139 r_i,

where each r_i is an arbitrary quadratic binary form over k. Changes of parameter and of the chosen coefficient lifts are included in these r_i.

Expand the Fermat equation modulo 139^2. Since sum q_i^70=0 mod 139, write

    D = (sum Q_i^70)/139 mod 139

for the defect of the displayed integer lifts q0=69(s-t)^2, q1=69(s+t)^2, q2=s^2, q3=t^2. The first-order lifting equation is

    D + 70 sum_i q_i^69 r_i = 0                      (3.1)

in k[s,t]_{140}.

Consider the linear functional

    ell(P)=coeff_{s^136 t^4}(P)-coeff_{s^134 t^6}(P).

Exact binomial arithmetic gives

    coeff_{s^136 t^4}(D)=81,
    coeff_{s^134 t^6}(D)=88,

so

    ell(D)=81-88=132 != 0 mod 139.                  (3.2)

On the other hand, for every one of the 12 basis corrections

    q_i^69 * s^2,
    q_i^69 * s t,
    q_i^69 * t^2,

one has ell=0. Thus ell annihilates the entire correction term in (3.1), contradicting (3.2).

Hence **C does not lift as a degree-two subscheme of F even to W_2**.

This is stronger than merely saying its beta/gamma divisor components cannot survive to characteristic zero.

## 4. Consequence for the most obvious coupled surface

Let

    Y=F x F,
    Z=C x C subset Y.

Then [Z] has a nonzero beta tensor gamma projection because [C] has both nonzero components.

The normal bundle splits

    N_{Z/Y}=pr_1^* N_{C/F} direct-sum pr_2^* N_{C/F}.

Since C is rational and N_{C/F}=O_{P^1}(-134) (U56), H^0(N_{C/F})=0 and H^1(O_C)=0. Therefore

    H^1(N_{Z/Y}) = H^1(N_{C/F}) direct-sum H^1(N_{C/F}).

For the product Witt deformation Y/W_2, the embedded obstruction of Z is the ordered pair of the two embedded obstructions of C. Section 3 proves each component is nonzero. Consequently **Z itself has no embedded W_2 lift**, even allowing a non-product first-order deformation of Z inside Y.

The natural codimension-two semiregularity map for this product splits into the two divisor semiregularity maps tensored with the nonzero class of the other conic; the two images lie in distinct Kunneth summands. Since U56 proved divisor semiregularity for C, this product map is injective on the special fiber. Thus ordinary characteristic-zero semiregularity intuition cannot be transplanted naively to this mixed-characteristic lifting problem.

## 5. Research consequence

U55 proves that the **pure Adams-weight-2 K_0 target class** has a compatible formal p-adic lift. U57 proves that an explicit effective lci surface with the correct target component does not lift even to first order.

Therefore the U55 formal lift cannot be represented by this obvious effective product surface. Any successful object-level realization must use a genuinely virtual/coupled perfect complex or a different special-fiber cycle whose first Witt obstruction cancels internally.

The next high-value problem is to construct such a perfect complex from several diagonal translates of C (or their cones/extensions) and compute its Ext^2 obstruction and Buchweitz-Flenner semiregularity character-by-character.

## 6. Verification scope

The finite-field incidence/Fourier calculation and the two-coefficient Witt obstruction were independently reproduced in Wolfram Language. The geometric implications use standard deformation theory of smooth conics and products. No formal proof assistant or independent expert review is claimed.
