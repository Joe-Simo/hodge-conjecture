# U14: exact arithmetic for the first potentially viable 3+3 block ansatz

Status: finite arithmetic checkpoint only. This does not rule out genuine three-variable matrix factorizations and does not solve the Hodge conjecture.

Date: 2026-09-14.

After U13, every separable ansatz containing an elementary two-variable block is excluded because alpha has no complementary coordinate pair. The first block decomposition not immediately killed is therefore 3+3.

There are 10 unordered partitions of the six indexed coordinates into two triples. Exact Wolfram arithmetic gives the ordinary integer triple sums:

    45 / 165
    63 / 147
    82 / 128
    83 / 127
    67 / 143
    86 / 124
    87 / 123
    104 / 106
    105 / 105
    124 / 86.

Modulo 70 these are respectively

    45 / 25,
    63 / 7,
    12 / 58,
    13 / 57,
    67 / 3,
    16 / 54,
    17 / 53,
    34 / 36,
    35 / 35,
    54 / 16.

Thus no partition gives two zero-sum triples, reproducing U06 in partition form. More strongly, no triple sum is 70 or 140, the positive multiples compatible with a naive three-coordinate Fermat character sum.

The symmetric partition

    {1,42,62} and {20,24,61}

has sums 105 and 105, i.e. both are 35 modulo 70. This is the unique displayed partition with equal sums and is structurally interesting because 35 is the order-two character at level 70.

This does not by itself yield an algebraic construction. It suggests a targeted three-variable factorization search in the order-two sector: determine whether a genuinely ternary factorization can carry a block whose character sum is 35, and whether tensoring two such blocks can contribute to the middle (2,2) target. Any such claim must be checked from the equivariant matrix-factorization grading and the Favero-Kelly trace formula, not inferred from the arithmetic coincidence alone.

Next obligation: derive the exact equivariant grading constraints for a three-variable factorization of x^70+y^70+z^70 and test the 35/35 partition first.
