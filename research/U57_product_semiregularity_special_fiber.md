# U57: the product of the U56 line/conic witnesses is semiregular on the special fiber

**Status:** the special-fiber semiregularity statement below is proved by Bloch's algebraic definition and an explicit product calculation. It does **not** prove a mixed-characteristic lift: the available all-obstruction/variational semiregularity theorems verified in this checkpoint are characteristic-zero theorems. No characteristic-zero target cycle is constructed.

Date: 2026-09-16. Base checkpoint: U56 at `a1d6181a5e0448d1e101041675dcabce484cb1ff`.

## 1. Setup

Let k be an algebraic closure of F_139 and let

    F = {x0^70+x1^70+x2^70+x3^70=0} in P^3_k,
    X = F x_k F.

By U56, choose smooth rational curves

    C_beta subset F,
    C_gamma subset F,

of degree 1 or 2 whose divisor classes have nonzero beta and gamma character projections, respectively. Each is the image of a line under the coordinate-square map from the degree-140 Hermitian surface.

Put

    Z = C_beta x C_gamma subset X.

It is a smooth lci surface of codimension 2.

## 2. Normal bundle and obstruction space

For smooth closed embeddings C subset A and D subset B,

    N_(C x D)/(A x B)
      = p_C^* N_(C/A) direct-sum p_D^* N_(D/B).          (2.1)

Here C_beta and C_gamma are P^1 and are rigid by U56. Also H^1(P^1,O)=0. Kunneth therefore gives

    H^1(Z,N_(Z/X))
      = H^1(C_beta,N_(C_beta/F))
        direct-sum H^1(C_gamma,N_(C_gamma/F)).            (2.2)

For a degree delta=1 or 2 curve on F,

    N_(C/F)=O_P1(-2-66 delta),

so the summand dimensions are 67 for a line and 133 for a conic.

## 3. Product formula for Bloch's semiregularity map

Bloch's semiregularity map is algebraically defined for an lci Z of codimension q in a smooth projective variety over an algebraically closed field:

    sigma_Z:H^1(N_(Z/X)) -> H^(q+1)(X,Omega_X^(q-1)).

For q=2 our target is H^3(X,Omega_X^1).

Because Z is the transverse product/intersection of the pullbacks of C_beta and C_gamma, its conormal map is the direct sum of the two conormal maps. In Bloch's definition the map is dual to the morphism obtained by wedging q-1 conormal differentials with ambient forms. Expanding this wedge for the direct sum in (2.1) gives the product rule

    sigma_Z(eta,theta)
      = sigma_Cbeta(eta) cup cl(C_gamma)
        + cl(C_beta) cup sigma_Cgamma(theta).             (3.1)

Under Kunneth, these two terms lie in the distinct direct summands

    H^2(F,O_F) tensor H^1(F,Omega_F^1),
    H^1(F,Omega_F^1) tensor H^2(F,O_F),                  (3.2)

of H^3(X,Omega_X^1). Thus they cannot cancel each other.

The same product rule follows from the Atiyah-class description: the Atiyah class of an exterior tensor product is the sum of the pulled-back Atiyah classes, and the relevant codimension-two component of the Atiyah-Chern character obeys the Leibniz rule. No characteristic-zero obstruction-annihilation theorem is used in deriving (3.1).

## 4. Injectivity

U56 proves the divisor semiregularity maps

    sigma_Cbeta:H^1(N_Cbeta/F)->H^2(O_F),
    sigma_Cgamma:H^1(N_Cgamma/F)->H^2(O_F)

are injective.

The divisor classes cl(C_beta),cl(C_gamma) are nonzero in H^1(Omega_F^1). Indeed, if H denotes the hyperplane class, then

    Tr(cl(C) cup cl(H)) = deg(C) in k,

which is 1 or 2 and hence nonzero in characteristic 139.

Therefore tensoring either injective divisor semiregularity map with the other nonzero divisor class remains injective. Since the images occupy the two distinct Kunneth summands in (3.2), equation (3.1) implies

    ker(sigma_Z)=0.

Hence

    **Z=C_beta x C_gamma is a semiregular codimension-two lci surface in F x F.**

This holds for every choice of U56 detecting line/conic pair, not merely a generic choice.

## 5. Why this does not yet give a Witt-vector lift

The verified obstruction-annihilation theorems needed to conclude that injective semiregularity forces actual deformations are characteristic-zero/complex results:

- Iacono-Manetti, *Semiregularity and obstructions of complete intersections*, assumes an algebraically closed field of characteristic 0.
- Pridham, *Semiregularity as a consequence of Goodwillie's theorem* (Forum Math. Sigma 2024), proves the full semiregularity conjecture using derived/negative-cyclic methods in the complex/characteristic-zero setting.
- Buchweitz-Flenner's classical deformation applications are likewise formulated for complex spaces/manifolds; they explicitly note positive-characteristic deformation phenomena beyond the reach of that analytic argument.

Bloch's **definition** of the lci semiregularity map is algebraic over an algebraically closed field, which is enough for Sections 2-4. It is not by itself a theorem that every obstruction to lifting Z through W_n(k) lies in its kernel.

Thus the current implication chain is

    low-degree supersingular divisors C_beta,C_gamma
      -> rigid + divisor-semiregular
      -> Z=C_beta x C_gamma is codimension-two semiregular over k
      -> [Z] has nonzero beta x gamma component
      -/-> Z lifts through W(k) (missing mixed-characteristic theorem).

U55 independently gives a formal **K_0 class** lifting the projected target, but does not turn it into a compatible formal lci subscheme/perfect complex. U57 narrows the object-level problem to the absence of a mixed-characteristic obstruction-annihilation theorem or a direct calculation of the relative Hilbert obstruction.

## 6. Next exact problem

Compute the obstruction to lifting Z from F x F to the first Witt thickening W_2(k) directly. If the obstruction vanishes, repeat structurally for all W_n; because H^0(N_Z)=0, any embedded lift is rigid/unique at each stage. A uniform vanishing argument would produce a compatible formal subscheme, after which Grothendieck existence algebraizes it over W(k).

The alternative is to construct a compatible formal perfect complex representing the Adams-projected U55 class; formal GAGA would then algebraize the object.

## 7. Sources

- S. Bloch, *Semi-regularity and de-Rham cohomology*, Invent. Math. 17 (1972), 51-66: algebraic lci semiregularity.
- A. Dan, I. Kaur, *Semi-regular varieties and variational Hodge conjecture*, C. R. Math. 354 (2016), Section 2 recalls Bloch's definition over an algebraically closed field.
- D. Iacono, M. Manetti, *Semiregularity and obstructions of complete intersections*, Adv. Math. 235 (2013), 92-125: all-obstruction result in characteristic 0.
- J. P. Pridham, *Semiregularity as a consequence of Goodwillie's theorem*, Forum Math. Sigma 12 (2024), e126: modern all-obstruction theorem in characteristic zero.

No formal verification or independent expert review is claimed.
