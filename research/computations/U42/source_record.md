# U42 source and application audit

Date checked: 2026-09-15. Remote base 489b743689ac96345ea56ec49f4a1568623236cc. This record concerns U42 only. The verifier and source reader are the same assistant; a separate Wolfram kernel checked arithmetic, not the literature application.

## Main primary source

Noriyuki Otsubo and Takao Yamazaki, *Motivic Gauss and Jacobi sums*, arXiv:2402.06072v3, 2 March 2025. Pinned full text: https://arxiv.org/html/2402.06072v3 . Published in Annales de la Faculte des sciences de Toulouse, serie 6, 35 (2026), 95–135, DOI 10.5802/afst.1842. Publication metadata was compared with https://afst.centre-mersenne.org/articles/10.5802/afst.1842/ . The preprint's numbering and formulas, not inferred journal numbering, are used.

The primary HTML was read directly, particularly Section 4.2 and the complete statement and proof of Theorem 7.2. No PDF, HTML, or extracted source copy is newly retained; there is therefore no claimed source-cache hash. The durable record preserves identifiers and notation translation rather than reproducing the paper.

## Actual geometric inputs and translation

1. Section 4.2 defines F_d^(n)<c> by sum_{i=1}^n x_i^d=c*x_0^d. It has dimension n-1. Project characters by the n affine diagonal coordinates; the omitted exponent is minus their sum. Admissibility means all n entries and their sum are nonzero modulo d. U42 uses d=70, coefficient field K=Q(zeta_70), and a characteristic-zero base containing zeta_140. Source terminology 'Lambda(1)' is translated to the Lefschetz motive L, not an oppositely signed cohomological Tate twist.

2. Proposition 4.7 gives the Artin twist for c, so F_d^(n)<n> is equivariantly isomorphic to the c=1 case after adjoining n^(1/d). The proposed field F contains the required roots for n=2,5,7. The all-plus projective Fermat convention is reached by scaling the omitted coordinate using a 70th root of -1.

3. Proposition 4.8 gives the tensor product of a curve character motive and its inverse-character motive as L. Its admissibility hypotheses are preserved in every nondegenerate use. U42's artificial J(a,-a)=L is a definition in a group extension, NOT the assertion that a degenerate primitive curve motive exists or is L.

4. Proposition 4.11(ii) supplies the iterative binary factorization when the last-two-character product is nontrivial; coordinate permutations allow the left-associated order in U42. Part (iv), equation (4.8), proves invertibility of every admissible Fermat character motive. All four intermediate pairings for alpha and all partial multiples used by the nine multiplication relations are nonzero. Their literal values are tested by the checker.

5. Theorem 7.2, equation (7.6), is explicitly a theorem in Chow(kappa,Lambda) for a field kappa containing d roots of unity, coefficient field containing Q(zeta_d), n|d, and alpha^n nontrivial. It is not restricted to a finite field. Its left side is the repeated-character motive of F_d^(n)<n>; its right side is the product of n-1 Jacobi curve motives with the nontrivial order-dividing-n characters. This gives U42 equation (5) after the coefficient twist is removed.

6. The proof of Theorem 7.2 constructs the finite covers using sum(s_i)=n and t^d=product(s_i), and the products of curves x^d+y^n=1. It uses the symmetric-group projectors and the nonzero composite 1/(n-1)! to give an isomorphism of invertible Chow motives. These are actual algebraic correspondences. Neither a finite-prime identity, Corollary 7.3 alone, nor a conservativity/Hodge conjecture is used to promote an arithmetic equality to algebraicity.

7. Proposition 4.11 plus coordinate permutations proves the nondegenerate part of the J cocycle. The zero/total-zero/partial-zero cases are verified separately in U42, with the character triples for the inverse factors explicitly checked in all 70^3 inputs. This finite check corroborates the bookkeeping; Proposition 4.8 and the geometric maps prove the isomorphisms.

## Supporting source and discarded shortcut

T. Shioda and T. Katsura, *On Fermat varieties*, Tohoku Math. J.31 (1979), 97–115, DOI 10.2748/tmj/1178229881. Primary PDF https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf . Lemma 1.1, Theorem 1.7, and Remark 1.8 were read and the first two pages (printed 97–98) were visually inspected using PDF screenshots. This checks the characteristic-zero scope and geometry behind the surface-product route. The exact character-motive statements used in the theorem are taken from Otsubo–Yamazaki.

Buskin's K3 Hodge-isometry theorem was considered in discovery, but no theorem applying it to the computed surface factors was verified, and it is not used. Literature searches for a general 'finite tensor order implies Tate' rule found no applicable verified theorem: search phrases included 'torsion invertible Chow motives', 'Picard group motives algebraically closed rational', and 'rank one motives Artin conjecture'. Several results concerned additive torsion (N id_M=0), which is a different notion and was not used. This limited search is not a proof that no suitable theorem exists.

## Provenance and limits

Search was through the available web engine, primary arXiv full text, publisher metadata, and the original Shioda–Katsura paper. No new Consensus search was necessary; earlier quota exhaustion is not treated as absence of literature. The result is classified as a specialized consequence of verified classical/source identities plus the project's explicit certificate. No global novelty, independent expert acceptance, or resolution of the original Hodge conjecture is claimed.
