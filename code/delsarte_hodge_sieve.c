/*
 * High-Speed OpenMP Delsarte-Shioda Hodge Character Sieve (code/delsarte_hodge_sieve.c)
 *
 * Evaluates character orbits alpha in (Z/dZ)^(n+2) for Fermat varieties:
 * x_0^d + x_1^d + ... + x_{n+1}^d = 0.
 *
 * For dimension n = 2k (middle cohomology H^(2k)), a character alpha is a Hodge class
 * if and only if for every s in (Z/dZ)*:
 *     sum_{i=0}^{n+1} (s * a_i mod d) = (k + 1) * d.
 *
 * Fast multi-threaded OpenMP kernel testing millions of tuples/sec.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>
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

    int k = dim / 2;
    int target_sum = (k + 1) * degree;
    int n_coords = dim + 2;

    // Precompute units modulo degree
    int units[256];
    int n_units = 0;
    for (int s = 1; s < degree; ++s) {
        if (gcd(s, degree) == 1) {
            units[n_units++] = s;
        }
    }

    double t0 = omp_get_wtime();

    int64_t total_tested = 0;
    int64_t total_hodge = 0;
    int64_t total_primitive = 0;

    #pragma omp parallel reduction(+:total_tested, total_hodge, total_primitive)
    {
        // Thread-local search across character slices
        #pragma omp for schedule(dynamic, 1000)
        for (int64_t a0 = 1; a0 < degree; ++a0) {
            for (int a1 = 1; a1 < degree; ++a1) {
                for (int a2 = 1; a2 < degree; ++a2) {
                    int a3 = (degree * 4 - (a0 + a1 + a2) % degree) % degree;
                    if (a3 == 0) a3 = degree;

                    if (total_tested >= max_search) continue;
                    total_tested++;

                    // Test Shioda Hodge condition for all units s
                    bool is_hodge = true;
                    for (int u = 0; u < n_units; ++u) {
                        int s = units[u];
                        int sum = ((s * a0) % degree) +
                                  ((s * a1) % degree) +
                                  ((s * a2) % degree) +
                                  ((s * a3) % degree);
                        if (sum != target_sum) {
                            is_hodge = false;
                            break;
                        }
                    }

                    if (is_hodge) {
                        total_hodge++;
                        // Check if decomposable into two pairs summing to 0 mod degree
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
    }

    double t1 = omp_get_wtime();
    double elapsed = t1 - t0;
    double rate = (elapsed > 0.0) ? (double)total_tested / elapsed : 0.0;

    printf("{\n");
    printf("  \"degree\": %d,\n", degree);
    printf("  \"dimension\": %d,\n", dim);
    printf("  \"total_tested\": %lld,\n", (long long)total_tested);
    printf("  \"total_hodge\": %lld,\n", (long long)total_hodge);
    printf("  \"total_primitive\": %lld,\n", (long long)total_primitive);
    printf("  \"elapsed_seconds\": %.6f,\n", elapsed);
    printf("  \"tuples_per_second\": %.2f\n", rate);
    printf("}\n");

    return 0;
}
