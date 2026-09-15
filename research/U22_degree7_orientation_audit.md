# U22: orientation audit of the first degree-7 rank-6 candidate

Status: exact matrix audit of one candidate only. This does not solve the Hodge conjecture.

Date: 2026-09-14.

U21 exhibited six degree-7 admissible exponent vectors with determinant 490. Put them as columns of A:

    A =
    [0 0 0 0 0 1
     0 0 1 2 3 0
     3 4 0 0 1 0
     2 0 2 0 3 1
     0 2 2 0 0 3
     2 1 2 5 0 2].

Exact checks give:

    column sums = (7,7,7,7,7,7),
    row sums    = (1,6,8,8,7,12),
    det(A)=490.

Thus, under the convention in which rows encode monomials of an ordinary homogeneous degree-7 polynomial, this orientation fails homogeneity. Under the transposed convention, the row sums are all 7, so the transpose is homogeneous but the character congruence used in U21 must then be re-derived with the transpose as well.

The inverse has denominators dividing 70, which is arithmetically suggestive but not sufficient for a Shioda map.

This audit prevents treating the first rank-6 subset as a geometric candidate merely from its determinant. The full search should impose both homogeneity and the correctly oriented character equation simultaneously.

Next: enumerate degree-7 matrices using a fixed exponent-matrix convention (rows = monomials, each row sum 7), require invertibility, and derive/test the exact equation relating the source character to alpha through A^{-1}. Only then inspect source geometry.
