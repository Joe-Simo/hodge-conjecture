# U06: exact triage of the degree-70 Fermat-fourfold orbit

Status: verified finite combinatorial facts about one Hodge orbit only. This does not solve the Hodge conjecture and does not prove algebraicity or non-algebraicity of the orbit.

Date: 2026-09-14.

## 1. Candidate orbit

Consider the Fermat fourfold

  X_70^4 : x0^70+x1^70+x2^70+x3^70+x4^70+x5^70=0 in P^5

and the character

  alpha=(1,20,24,42,61,62) mod 70.

A recent conditional preprint by M. F. Islam (Zenodo 10.5281/zenodo.22701510, 2026-09-11) reports this as the sole orbit left by its tested join/curve-pair/pair-descent/Aoki/level-change constructions in its degree <=100 census. Because that source is a very recent preprint and not an independent verification, this project treats the orbit only as a research lead.

## 2. Exact Hodge-orbit check

For a Fermat fourfold character, the rational Hodge-orbit condition requires the least-positive-residue sum of u*alpha to remain 3m=210 for every unit u mod 70.

Exact Wolfram computation over all 24 units of (Z/70Z)^* gives:

  sum_i <u alpha_i>_70 = 210

for every u in

  {1,3,9,11,13,17,19,23,27,29,31,33,37,39,41,43,47,51,53,57,59,61,67,69}.

Thus every Galois conjugate in the unit orbit has middle Hodge type (2,2). The 24 unit multiples give 24 distinct sorted multisets, so no collapse was found at the multiset level.

This verifies that the character is a genuine rational-Hodge-block candidate in the standard Fermat character formalism; it does not establish any statement about algebraicity.

## 3. No zero-sum-triple split

A recent criterion used for odd-degree Fermat fourfolds says that if the six-character multiset can be partitioned into two triples, each summing to 0 modulo m, then the associated rational Hodge block is algebraic by transport from a (1,1) structure on a product of Fermat curves.

There are C(6,3)=20 triples. Exact enumeration for alpha found none with sum 0 modulo 70.

Because multiplication by a unit preserves zero-sum relations modulo 70, no Galois conjugate of alpha has such a split either.

Therefore this particular sufficient criterion does not apply.

## 4. No simple level descent to a proper divisor of 70

The proper nontrivial prime-factor levels are controlled by divisors 2,5,7,10,14,35. A direct coordinatewise Fermat level descent from level 70 to a proper divisor would require, after an allowed unit action, all character coordinates to acquire the corresponding common factor.

This is impossible already because alpha contains the coordinate 1. For every unit u mod 70, the residue u*1 is itself a unit and hence is divisible by none of 2,5,7.

Exact enumeration over all 24 units confirms no uniform proper-factor descent.

Thus alpha is not the pullback of a lower-level character through the elementary coordinatewise power maps X_70 -> X_d for d|70, d<70.

This does not exclude more general Shioda/Delsarte maps.

## 5. Pair obstruction

The 15 pair sums modulo 70 are

  21,25,43,62,63,44,62,11,12,66,15,16,33,34,53.

None is 0. Hence alpha is not decomposable by a vanishing pair a_i+a_j=0 mod 70.

## 6. Consequence for the matrix-factorization route

Favero-Kelly (arXiv:2609.12759v1) show that primitive Chern characters on a smooth hypersurface are encoded by matrix-factorization trace polynomials. For Fermat hypersurfaces, standard complete-intersection cycles arise from Koszul/Tate matrix factorizations associated to decompositions

  Q = sum a_i b_i.

The finite checks above show that alpha is outside the simplest pair-split and level-descent mechanisms. The recent census further claims it lies outside its tested Aoki and related constructions.

Therefore a useful next construction target is genuinely nontrivial:

  find a matrix factorization (A,B) of Q=sum x_i^70 whose Favero-Kelly primitive trace polynomial has nonzero projection onto the Galois orbit of alpha.

A rank-1 matrix factorization cannot help: for the smooth irreducible Fermat polynomial Q, AB=Q in rank 1 is trivial up to a unit/factor of Q and yields no new primitive class. Standard Koszul factorizations reproduce complete-intersection-type classes already covered by existing constructions. A successful certificate is therefore expected to require a higher-rank, non-Koszul factorization or a geometric cycle such as a pullback from a suitable Delsarte/higher-symmetry model.

## Exact computation record

Wolfram Language checks used exact integer/modular arithmetic only:

- all 24 units modulo 70;
- least-positive-residue Hodge sums;
- all 20 size-3 subsets;
- all 15 pair sums;
- uniform proper-factor descent under every unit action.

No numerical approximation was used.

## Sources

- D. Favero and T. L. Kelly, `The Chern character of a coherent sheaf on a smooth projective hypersurface`, arXiv:2609.12759v1 (2026).
- R. Jumagulov, `The Hodge conjecture for Fermat fourfolds of odd degree at most 199`, arXiv:2608.18134v1 (2026), for recent split/two-pair/level-lift criteria in the odd-degree setting.
- M. F. Islam, `A Proof of the Hodge Conjecture Derived from One Semiregular Witness Axiom...`, Zenodo 10.5281/zenodo.22701510 (2026), used only as a lead for the degree-70 orbit, not as verified authority.
