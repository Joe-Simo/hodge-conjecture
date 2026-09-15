# U16: no coordinatewise level-140 Hodge lift of the degree-70 target

Status: verified finite obstruction for the simplest level-doubling lift. This does not rule out general level changes and does not solve the Hodge conjecture.

Date: 2026-09-14.

## Motivation

U15 corrected the interpretation of the unique 35/35 triple partition and proposed testing whether the order-two defect disappears after doubling the Fermat level from 70 to 140.

For the power map

    X_140^4 -> X_70^4,

an elementary coordinatewise character lift of

    alpha=(1,20,24,42,61,62) mod 70

has each coordinate independently equal to

    beta_i = alpha_i  or  alpha_i+70

modulo 140. There are exactly 2^6=64 such lifts.

## Exact Hodge test

For a level-140 Fermat-fourfold character beta to define a rational middle Hodge block of type (2,2), every unit u in (Z/140Z)^* must satisfy

    sum_i <u beta_i>_140 = 3*140 = 420,

where `< >_140` denotes the least positive residue.

Exact Wolfram enumeration tested all 64 coordinate lifts against every unit modulo 140.

Result:

    totalLifts -> 64
    validHodgeLifts -> 0

Thus not even one elementary coordinatewise lift remains of Hodge type (2,2) throughout its Galois orbit at level 140.

Consequently there is also no such lift that can split into two zero-sum triples modulo 140.

## Consequence

The simplest level-doubling repair of the 35/35 defect fails before algebraicity is considered: the target rational Hodge block does not lift coordinatewise to a rational (2,2) Hodge block at level 140.

This rules out only the direct character lifts beta_i congruent alpha_i modulo 70 associated with the elementary coordinatewise power map. It does NOT rule out:

- adding auxiliary cancelling coordinates before lifting;
- a higher multiple of the level such as 210, 280, etc.;
- non-coordinate Delsarte/Shioda maps;
- stacky or twisted equivariant matrix factorizations;
- direct nonseparable matrix factorizations at level 70.

## Research implication

The 35/35 partition is now substantially less promising: both its ordinary Fermat-curve interpretation (U15) and its simplest level-140 repair fail. Return priority to genuinely nonseparable level-70 constructions, or perform a bounded search over higher level multiples with a mathematically justified descent map rather than arbitrary lifting.
