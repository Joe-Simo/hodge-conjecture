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

    int batch = (argc > 4) ? atoi(argv[4]) : 1;
    if (batch < 1) batch = 1;

    int k = dim / 2;

    int64_t total_tested_all = 0;
    int64_t total_hodge_all = 0;
    int64_t total_primitive_all = 0;
    int last_degree = degree;
    int last_n_units = 0;

    double t0 = omp_get_wtime();

    for (int b = 0; b < batch; ++b) {
        int cur_deg = degree + b * ((dim == 4) ? 2 : 7);
        if (cur_deg > 255) break;
        last_degree = cur_deg;

        int target_sum = (k + 1) * cur_deg;

        // Precompute units modulo cur_deg
        int units[256];
        int n_units = 0;
        for (int s = 1; s < cur_deg; ++s) {
            if (gcd(s, cur_deg) == 1) {
                units[n_units++] = s;
            }
        }
        last_n_units = n_units;

        // Precompute L1 cache lookup table: rem_table[u][a] = (units[u] * a) % cur_deg
        uint8_t rem_table[256][256];
        for (int u = 0; u < n_units; ++u) {
            for (int a = 0; a <= cur_deg; ++a) {
                rem_table[u][a] = (uint8_t)((units[u] * a) % cur_deg);
            }
        }

        int64_t total_tested = 0;
        int64_t total_hodge = 0;
        int64_t total_primitive = 0;

        #pragma omp parallel reduction(+:total_tested, total_hodge, total_primitive)
        {
            if (dim == 2) {
                #pragma omp for schedule(dynamic, 100)
                for (int a0 = 1; a0 < cur_deg; ++a0) {
                    for (int a1 = 1; a1 < cur_deg; ++a1) {
                        for (int a2 = 1; a2 < cur_deg; ++a2) {
                            int rem = (a0 + a1 + a2) % cur_deg;
                            int a3 = (rem == 0) ? cur_deg : (cur_deg - rem);

                            total_tested++;

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
                                bool decomposable = ((a0 + a1) % cur_deg == 0) ||
                                                    ((a0 + a2) % cur_deg == 0) ||
                                                    ((a0 + a3) % cur_deg == 0);
                                if (!decomposable) {
                                    total_primitive++;
                                }
                            }
                        }
                    }
                }
            } else if (dim == 4) {
                #pragma omp for schedule(dynamic, 20)
                for (int a0 = 1; a0 < cur_deg; ++a0) {
                    for (int a1 = 1; a1 < cur_deg; ++a1) {
                        for (int a2 = 1; a2 < cur_deg; ++a2) {
                            for (int a3 = 1; a3 < cur_deg; ++a3) {
                                for (int a4 = 1; a4 < cur_deg; ++a4) {
                                    int rem = (a0 + a1 + a2 + a3 + a4) % cur_deg;
                                    int a5 = (rem == 0) ? cur_deg : (cur_deg - rem);

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

        total_tested_all += total_tested;
        total_hodge_all += total_hodge;
        total_primitive_all += total_primitive;
    }

    double t1 = omp_get_wtime();
    double elapsed = t1 - t0;
    double rate = (elapsed > 0.0) ? ((double)total_tested_all / elapsed) : 0.0;

    printf("{\n");
    printf("  \"start_degree\": %d,\n", degree);
    printf("  \"last_degree\": %d,\n", last_degree);
    printf("  \"batch_count\": %d,\n", batch);
    printf("  \"dim\": %d,\n", dim);
    printf("  \"units_count\": %d,\n", last_n_units);
    printf("  \"total_tested\": %lld,\n", (long long)total_tested_all);
    printf("  \"total_hodge\": %lld,\n", (long long)total_hodge_all);
    printf("  \"total_primitive\": %lld,\n", (long long)total_primitive_all);
    printf("  \"elapsed_seconds\": %.6f,\n", elapsed);
    printf("  \"tuples_per_second\": %.2f\n", rate);
    printf("}\n");

    return 0;
}
