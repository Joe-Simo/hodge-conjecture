# U54: the two order-70 Horikawa models are rigid inside their symmetry-fixed hypersurface families

**Status:** exact finite monomial classification plus elementary coordinate-scaling argument. This rules out only deformations preserving the specified order-70 actions; it does not rule out arbitrary deformations or solve the Hodge conjecture.

Date: 2026-09-16.

## 1. Models and actions

Use the U46 canonical models in P(1,1,2,5), with variables (T,X,Y,Z):

    S5_bar: Z^2 + Y^5 + X^9 T + X^2 T^8 = 0,
    S7_bar: Z^2 + Y^5 + X^7 Y T + T^10 = 0.

On the affine chart T=1, U46 records the residual order-70 actions

    S5: (X,Y,Z) -> (zeta^60 X, zeta^52 Y, zeta^25 Z),
    S7: (X,Y,Z) -> (zeta^32 X, zeta^56 Y, zeta^35 Z).

Choose the projective lift with T-character 0. Then the S5 defining polynomial is semi-invariant of character 50 mod 70, while the S7 polynomial is invariant (character 0).

## 2. Complete monomial enumeration

A weighted-degree-10 monomial has the form

    T^a X^b Y^c Z^d,
    a+b+2c+5d=10.

Exact enumeration gives the following.

For S5, the degree-10 monomials of character 50 are exactly

    Z^2,
    Y^5,
    X^9 T,
    X^2 T^8.

There are no others.

For S7, the degree-10 invariant monomials are exactly

    Z^2,
    Y^5,
    X^7 Y T,
    T^10.

There are no others.

Both Python and a separate Wolfram enumeration give count 4 in each case.

## 3. Moduli consequence

Thus the full symmetry-preserving degree-10 linear system for each specified action is the four-dimensional coefficient space spanned by the four monomials already present in the defining equation.

On the open set where all four coefficients are nonzero, diagonal rescaling of the four weighted coordinates together with overall rescaling of the equation normalizes the coefficients to the displayed model. Equivalently, after quotient by the effective diagonal coordinate torus, there is no nontrivial parameter left.

Therefore each of S5_bar and S7_bar is isolated in the moduli of degree-10 hypersurfaces carrying its specified order-70 action with the same character.

## 4. Consequence for the diagonal-deformation strategy

A strategy that attempts to connect S5 and S7 to a common surface while preserving the order-70 eigenspace decomposition cannot work through a positive-dimensional symmetry-fixed family: there is no such local family at either endpoint.

Any variational-Hodge construction relating the missing R5--R7 class to a diagonal graph must therefore break the visible order-70 symmetry along the deformation and track the Hodge class by a different mechanism.

This result does not rule out such a symmetry-breaking Hodge locus, nor does it prove the Hodge locus is zero-dimensional.
