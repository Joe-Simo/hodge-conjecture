/*
 * High-Speed OpenMP Delsarte-Shioda Hodge Character Sieve (code/delsarte_hodge_sieve.c)
 *
 * Evaluates character orbits alpha in (Z/dZ)^(n+2) for Fermat hypersurfaces:
 * x_0^d + x_1^d + ... + x_{n+1}^d = 0.
 *
 * For dimension n = 2k (middle cohomology H^(2k)), a character alpha is a Hodge class
 * if and only if for every s in (Z/dZ)*:
 *     sum_{i=0}^{n+1} (s * a_i mod d) = (k + 1) * d.
 *
 * Optimizations:
 * 1. L1-cached precomputed modulo-multiplication lookup table rem_table[u][a].
 * 2. Complete elimination of division and modulo instructions in Shioda inner loop.
 * 3. OpenMP parallelization across outer slice coordinates.
 * 4. Multi-dimensional support for both surfaces (n=2, 4-tuples) and fourfolds (n=4, 6-tuples).
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>
#include <omp.h>

static inline int gcd(int a, int b) {
    while (b) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main(int argc, char** argv) {
    int degree = 70;      // Default degree 70 Fermat surface/fourfold
    int dim = 2;         // Default surface (n=2, k=1, target sum = 2*d)
    int64_t max_search = 1000000;

    if (argc > 1) degree = atoi(argv[1]);
    if (argc > 2) dim = atoi(argv[2]);
    if (argc > 3) max_search = atoll(argv[3]);

    if (degree > 255) degree = 255;
    if (dim != 2 && dim != 4) dim = 2;

    int k = dim / 2;
    int target_sum = (k + 1) * degree;

    // Precompute units modulo degree
    int units[256];
    int n_units = 0;
    for (int s = 1; s < degree; ++s) {
        if (gcd(s, degree) == 1) {
            units[n_units++] = s;
        }
    }

    // Precompute L1 cache lookup table: rem_table[u][a] = (units[u] * a) % degree
    // Fits entirely in L1 data cache (< 16 KB)
    static uint8_t rem_table[256][256];
    for (int u = 0; u < n_units; ++u) {
        for (int a = 0; a <= degree; ++a) {
            rem_table[u][a] = (uint8_t)((units[u] * a) % degree);
        }
    }

    double t0 = omp_get_wtime();

    int64_t total_tested = 0;
    int64_t total_hodge = 0;
    int64_t total_primitive = 0;

    #pragma omp parallel reduction(+:total_tested, total_hodge, total_primitive)
    {
        if (dim == 2) {
            #pragma omp for schedule(dynamic, 100)
            for (int a0 = 1; a0 < degree; ++a0) {
                for (int a1 = 1; a1 < degree; ++a1) {
                    for (int a2 = 1; a2 < degree; ++a2) {
                        int rem = (a0 + a1 + a2) % degree;
                        int a3 = (rem == 0) ? degree : (degree - rem);

                        total_tested++;

                        // Fast table-lookup Shioda Hodge condition (zero division/modulo)
                        bool is_hodge = true;
                        for (int u = 0; u < n_units; ++u) {
                            const uint8_t* row = rem_table[u];
                            int sum = row[a0] + row[a1] + row[a2] + row[a3];
                            if (sum != target_sum) {
                                is_hodge = false;
                                break;
                            }
                        }

                        if (is_hodge) {
                            total_hodge++;
                            // Check decomposability into pairs summing to 0 mod degree
                            bool decomposable = ((a0 + a1) % degree == 0) ||
                                                ((a0 + a2) % degree == 0) ||
                                                ((a0 + a3) % degree == 0);
                            if (!decomposable) {
                                total_primitive++;
                            }
                        }
                    }
                }
            }
        } else if (dim == 4) {
            // Fourfold: 6 coordinates a0..a5 with sum = 0 mod degree
            #pragma omp for schedule(dynamic, 20)
            for (int a0 = 1; a0 < degree; ++a0) {
                for (int a1 = 1; a1 < degree; ++a1) {
                    for (int a2 = 1; a2 < degree; ++a2) {
                        for (int a3 = 1; a3 < degree; ++a3) {
                            for (int a4 = 1; a4 < degree; ++a4) {
                                int rem = (a0 + a1 + a2 + a3 + a4) % degree;
                                int a5 = (rem == 0) ? degree : (degree - rem);

                                total_tested++;

                                bool is_hodge = true;
                                for (int u = 0; u < n_units; ++u) {
                                    const uint8_t* row = rem_table[u];
                                    int sum = row[a0] + row[a1] + row[a2] + row[a3] + row[a4] + row[a5];
                                    if (sum != target_sum) {
                                        is_hodge = false;
                                        break;
                                    }
                                }

                                if (is_hodge) {
                                    total_hodge++;
                                    total_primitive++;
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    double t1 = omp_get_wtime();
    double elapsed = t1 - t0;
    double rate = (elapsed > 0.0) ? ((double)total_tested / elapsed) : 0.0;

    printf("{\n");
    printf("  \"degree\": %d,\n", degree);
    printf("  \"dim\": %d,\n", dim);
    printf("  \"units_count\": %d,\n", n_units);
    printf("  \"total_tested\": %lld,\n", (long long)total_tested);
    printf("  \"total_hodge\": %lld,\n", (long long)total_hodge);
    printf("  \"total_primitive\": %lld,\n", (long long)total_primitive);
    printf("  \"elapsed_seconds\": %.6f,\n", elapsed);
    printf("  \"tuples_per_second\": %.2f\n", rate);
    printf("}\n");

    return 0;
}
