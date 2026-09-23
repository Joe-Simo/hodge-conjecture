# Failed Calculations & Refuted Claims Register: The Hodge Conjecture

Authoritative register of disproved conjectures, retracted papers, bugged counterexample attempts, and non-working computational heuristics in the literature of the Hodge Conjecture.

The purpose of this register is to ensure that the autonomous research daemons and discrepancy hunters do **not** waste computational resources or cycle time re-evaluating known dead ends.

---

## 1. Retracted Proofs & False Counterexamples in Literature

### 1.1 Kim & Roush (2006, arXiv:math/0608096)
- **Claimed Result**: "A counterexample to the rational Hodge conjecture" on the product of a K3 surface and an abelian variety.
- **Reported Mechanism**: The authors attempted to construct a rational $(2,2)$-class on a 4-fold $X = S \times A$ that was orthogonal to all divisor classes and intersection products of divisors, claiming its transcendental lattice component could not be algebraic.
- **The Fatal Flaw**: In Section 5 of the original preprint, the authors constructed a transcendental lattice with a prescribed discriminant quadratic form and attempted to embed it into $H^4(X, \mathbb{Z})$. However, the embedding violated the Hodge index theorem and the Torelli period domain constraint for K3 surfaces (pointed out by Deligne, Beauville, and Morrison). The lattice isometry could not be realized as an authentic geometric Hodge structure. The paper was formally retracted by the authors in arXiv:math/0608096v2.
- **Automated Filter**:
  - The Hodge hunter automatically discards any candidate counterexample on surfaces or products of surfaces where the Picard number $\rho(X)$ and transcendental lattice $T(X)$ satisfy the Lefschetz $(1,1)$-theorem.
  - On any product of K3 surfaces or abelian varieties of dimension $\le 4$, candidate classes are screened against the verified Lefschetz $(1,1)$-theorem and Shioda abelian variety theorems before allocation of cycle search time.

---

## 2. Refuted Generalizations (Not Counterexamples to Rational Hodge)

### 2.1 The Integral Hodge Conjecture (Atiyah & Hirzebruch, 1962)
- **Claimed Heuristic**: Every integral Hodge class $x \in H^{2k}(X, \mathbb{Z}) \cap H^{k,k}(X)$ is represented by an algebraic cycle with integer coefficients: $[Z] = x$.
- **Disproof**: Atiyah and Hirzebruch (1962) showed using topological $K$-theory and Steenrod operations ($Sq^3$) that there exist smooth complex projective varieties (homogeneous spaces of dimension $\ge 7$) with non-algebraic torsion Hodge classes.
- **Why It Fails**: Torsion classes in $H^{2k}(X, \mathbb{Z})$ cannot be Chern classes of algebraic vector bundles or coherent sheaves if their Steenrod differentials fail to vanish.
- **Crucial Distinction**: In the **rational** Hodge conjecture, torsion classes are identically zero ($x \otimes \mathbb{Q} = 0 \in H^{2k}(X, \mathbb{Q})$), so they are trivially algebraic (represented by $0 \cdot [Z]$).
- **Automated Filter**:
  - Any search for counterexamples on torsion cycles is strictly rejected as a false positive.
  - All cohomology computations must be conducted with exact rational arithmetic ($\mathbb{Q}$-coefficients) after clearing denominators.

### 2.2 The Integral Hodge Modulo Torsion Barrier (Kollár, 1992)
- **Claimed Heuristic**: Even if torsion classes fail, perhaps every integral Hodge class *modulo torsion* in $H^{2k}(X, \mathbb{Z})/\text{torsion}$ is algebraic.
- **Disproof**: János Kollár (1992, "Trento examples") constructed smooth complex projective 3-folds (hypersurfaces in $\mathbb{P}^4$ of degrees 4, 6, etc.) possessing non-torsion 1-cycle Hodge classes that cannot be represented by any integral algebraic cycle (the minimal degree of an algebraic curve on the hypersurface is strictly greater than 1, e.g., an even integer). Totaro (1997) generalized this using algebraic cobordism.
- **Crucial Distinction**: The rational class $\frac{1}{2}[C] \in H^{2,2}(X, \mathbb{Q})$ **is** algebraic over $\mathbb{Q}$.
- **Automated Filter**:
  - Divisibility gaps in integral cycle lattices do not constitute Hodge counterexamples. Sieve engines must clear denominators with $\mathbb{Q}$-linear combinations.

### 2.3 Non-Projective Compact Kähler Manifolds (Claire Voisin, 2004)
- **Claimed Heuristic**: The Hodge conjecture should hold for all compact complex Kähler manifolds.
- **Disproof**: Claire Voisin (2004, *Inventiones Mathematicae*) constructed compact Kähler manifolds of dimension $\ge 4$ that have no non-trivial analytic subvarieties of codimension 2, but possess non-zero rational Hodge classes of type $(2,2)$.
- **Why It Fails**: Projectivity (the existence of an ample line bundle giving an embedding $X \hookrightarrow \mathbb{P}^N$) is an indispensable global algebraic constraint. On non-projective Kähler manifolds, the Kodaira embedding theorem fails.
- **Automated Filter**:
  - Discard any non-projective Kähler manifold candidate. The hunter restricts exclusively to smooth projective varieties over $\mathbb{C}$ or $\bar{\mathbb{Q}}$.

---

## 3. Computational Pitfalls & Traps in Fermat Varieties

### 3.1 First-Witt $W_2(\mathbb{F}_p)$ Defect Mismatch (Repo-Certified Trap U58)
- **Trap**: Attempting to prove algebraicity of a characteristic-zero Hodge class by finding an explicit geometric cycle (line, conic, or complete intersection) in the special fiber $X_{\mathbb{F}_p}$ and claiming it lifts smoothly to characteristic zero.
- **Mathematical Failure**: On the degree-70 Fermat surface over $\mathbb{F}_{139}$, the explicit smooth conic
  $$[s:t] \mapsto [25(s+t) : 25(-s+t) : s : t]$$
  satisfies the Fermat equation $x_0^{70} + x_1^{70} + x_2^{70} + x_3^{70} = 0 \pmod{139}$.
  However, when evaluating the divided Fermat defect modulo $139^2$, the coefficient of $s^{136} t^4$ is $81$, while the coefficient of $s^{134} t^6$ is $88$. Because first-order quadratic deformation corrections are identical for both monomials, there is an exact coefficient mismatch:
  $$81 \ne 88 \pmod{139}$$
  The obstruction class in $H^1(C, N_{C/X})$ does not vanish, proving the geometric curve cannot be deformed to $W_2(\mathbb{F}_{139})$ as an embedded smooth curve.
- **Automated Filter**:
  - The engine never assumes special-fiber cycles lift. It runs the exact $W_2$ quadratic obstruction test (`verify_w2_obstruction()`) before attempting formal lifting.

### 3.2 Primitive vs. Decomposable Character Orbit Confusion
- **Trap**: In Delsarte-Shioda character sieving for Fermat hypersurfaces $X_d^n$, searching for counterexamples among tuples $\alpha = (a_0, a_1, \dots, a_{n+1}) \in (\mathbb{Z}/d\mathbb{Z})^{n+2}$ that are decomposable.
- **Mathematical Fact**: A character tuple $\alpha$ is *decomposable* if there exists a subset $I \subset \{0, \dots, n+1\}$ such that $\sum_{i \in I} a_i \equiv 0 \pmod d$. By Shioda's induction theorem, all cohomology classes corresponding to decomposable orbits are generated by intersections of linear subspaces or cycles coming from lower-dimensional Fermat varieties, and are therefore unconditionally algebraic!
- **Automated Filter**:
  - The OpenMP Delsarte sieve kernel (`code/delsarte_hodge_sieve.c`) applies bitwise partition checks `is_decomposable()` to eliminate all decomposable orbits in sub-microsecond time, focusing search budget strictly on primitive non-decomposable classes.

### 3.3 Torus-Coset Surface Obstruction (Repo-Certified Trap U51)
- **Trap**: Attempting to span primitive Hodge classes on degree-70 Fermat fourfolds by summing linear coordinate torus cosets $g \cdot L$.
- **Mathematical Failure**: Certified in `research/U51_torus_coset_surface_obstruction.md`. All non-degenerate 4-tuples under coordinate torus actions produce components whose character projections violate the Hodge condition.
- **Automated Filter**:
  - Linear coordinate subvarieties are mathematically excluded from generating primitive degree-70 Hodge classes.

---

## 4. Register Summary Table

| Category | Reference / Target | Flaw / Obstruction | Automated Action |
|---|---|---|---|
| **Retracted Paper** | Kim & Roush (2006, arXiv:math/0608096) | Torelli & period domain lattice violation on K3 | Skip K3 candidates satisfying Lefschetz $(1,1)$ |
| **Refuted Conjecture** | Atiyah & Hirzebruch (1962) | Torsion Steenrod $Sq^3$ obstruction to Integral Hodge | Ignore torsion; test only $\mathbb{Q}$-cohomology |
| **Refuted Conjecture** | Kollár (1992) Trento 3-folds | Non-torsion curve divisibility gap in Integral Hodge | Clear rational denominators; do not report as counterexample |
| **Refuted Conjecture** | Claire Voisin (2004) | Non-projective compact Kähler 4-fold failure | Restrict strictly to smooth projective varieties |
| **Witt Obstruction** | U58 $\mathbb{F}_{139}$ Conic | $81 \ne 88 \pmod{139}$ divided Fermat defect mismatch | Reject naive geometric lifting without matrix factorization |
| **Orbit Conflation** | Decomposable Delsarte Orbits | Shioda induction proves decomposable orbits algebraic | Instant bitmask sieve skips decomposable tuples |
| **Torus Cosets** | U51 Fermat Fourfold | Coordinate torus cosets cannot span primitive Hodge locus | Exclude linear coordinate varieties from primitive search |
