# U59: Kang's theorem closes the degree-70 Fermat fourfold target

**Date checked:** 2026-09-24

**Status:** published theorem proves the rational Hodge conjecture for the project's specific degree-70 Fermat fourfold. This does not prove the global Hodge conjecture for arbitrary smooth projective varieties.

## Exact source theorem

Su-Jeong Kang, “Refined Motivic Dimension of Some Fermat Varieties,” *Bulletin of the Australian Mathematical Society* 93 (2016), 223–230, DOI [10.1017/S0004972715001379](https://doi.org/10.1017/S0004972715001379), defines the Fermat hypersurface `X_m^n` as

```text
x_0^m + x_1^m + ... + x_(n+1)^m = 0  in P^(n+1),
```

so `dim(X_m^n)=n`. The project's target is exactly `X_70^4`, given by six degree-70 coordinates in `P^5_C`.

Kang's Corollary 3.2 states that the generalized Hodge conjecture holds for every Fermat variety of dimension three or four and every positive degree. In Kang's definitions, the classical codimension-`p` Hodge conjecture is the case `GHC(H^(2p)(X,Q),p)`. For dimension four, codimension two is the middle case `GHC(H^4(X,Q),2)`. The proof chain is explicit: Lemma 2.1 upgrades `GHC(H^4,1)` to `GHC(H^4,2)`, Theorem 3.1 establishes the codimension-one generalized Hodge statement, and Corollary 3.2 gives the full dimension-four conclusion. Remark 4.4(1) restates that Kang proves the Hodge conjecture for `X_m^4` without a degree restriction.

Therefore the rational `(2,2)` target block `W_alpha` on `X_70^4` is algebraic. This conclusion applies to the whole rational Hodge conjecture for this particular Fermat fourfold, not only to the named alpha block.

## Effect on U55–U58

- U55's crystalline special-fiber cycle and formal `K_0` lift remain valid as route-specific results. Its formal-to-algebraic `K_0` step is **not** an open existence obligation for the Hodge class on `X_70^4`: Kang already proves that an algebraic cycle class exists over `C`.
- U58's W2 obstruction still proves that its specific conic and raw product do not lift as embedded subschemes through the first Witt thickening. It is not evidence that the characteristic-zero Hodge class is nonalgebraic; another cycle exists by Kang's theorem.
- The U55/U58 construction may still be useful if an explicit characteristic-zero representative compatible with that particular special-fiber class is wanted. It does not advance a proof of the general Clay Hodge conjecture unless a separate theorem reduces arbitrary Hodge classes to this Fermat fourfold, and no such reduction is present in this project.

## Scope and primary locators

This is a literature correction, not a new proof of the Hodge conjecture. The relevant source locations in the published Cambridge PDF are: definition of `X_m^n`, pp. 223–224; GHC and classical Hodge conventions, p. 224; Theorem 3.1, p. 226; Corollary 3.2, p. 227; Remark 4.4(1), p. 229. Primary PDF: [Kang (2016)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EEBE2D9F98935C50BED5E3AD71DAEF59/S0004972715001379a.pdf/refined-motivic-dimension-of-some-fermat-varieties.pdf).
