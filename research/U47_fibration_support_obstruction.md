# U47: pencil-supported correspondences vanish; explicit fixed-curve covers

**Status:** restricted geometric statements proved below using classical inputs, explicit equations and an adversarial self-review; exact algebra corroborated independently in SymPy and Wolfram. Not formally verified or independently expert-reviewed. No algebraic cycle representing the degree-70 target, and no complete Hodge solution, has been constructed.

Date: 2026-09-15. Pinned remote input: `Joe-Simo/hodge-conjecture@50cbb2c7839121abc193f57ced6e880ed4e4a23b`, specifically `research/U46_explicit_Horikawa_product_reduction.md`, blob `128627a7f7b80a83ac2e61f2622adcdbff5f2348`. Work and outputs are confined to `/mnt/data/hodge-conjecture` and the dedicated private repository.

## 1. Input reconciliation and exact new question

There are **two distinct U46 records**, not two interchangeable versions of one theorem:

- The supplied local `U46_degree35_CM19_source_reduction.md` transfers the target to a degree-35 CM source of dimension nineteen. It and its evidence archive remain unchanged.
- The newer remote U46 specifies two actual surfaces and a mixed-product problem. This note pursues that route. Its full proof, not only the README, was read at the pinned revision.

No renumbering, replacement of the local evidence, or global revalidation of historical claims is intended. The local inventory records this distinction and all restored checker files.

Over C, retain the canonical models in P(1,1,2,5), with coordinates [T:X:Y:Z]:

    S5_bar: Z^2+Y^5+X^9 T+X^2 T^8=0,
    S7_bar: Z^2+Y^5+X^7 Y T+T^10=0.

Let S5,S7 be their minimal resolutions. Let `T(S)` mean the orthogonal complement of NS(S)_Q in H^2(S,Q). Remote U46 identifies simple rank-24 summands R5,R7 and transfers the unresolved original block

    W, alpha=(1,20,24,42,61,62), on X70={sum z_i^70=0} in P^5

to the 24-dimensional rational Hodge space in R5 tensor R7. That prior transfer remains a named input; the new vanishing proof below does not assume the desired cycle exists.

Resolve the rational pencils, taking a common smooth resolution when necessary:

    f5 = X/T on S5,       f7 = X/T on S7,
    g7 = Y/T^2 on S7.

Their generic fibres have genera 2, 2 and 3, respectively. All statements about support below are on these resolved models; point blowups add only algebraic H^2 and do not change the transcendental conclusion.

The first uncertain step in U46 was whether a fibrewise correspondence between the **canonical** genus-two pencils could supply the missing map. U46 already knew the isotrivializing radical for f5 and the discriminant for f7. Recomputing those formulas is a check, not the new result.

## 2. The restricted support theorem

**Theorem A.** Let B be a smooth projective connected complex curve with nonconstant maps a,b:B -> P^1. For geometric generic fibres after these base changes,

    Hom(J(f5_a), J(f7_b)) = 0,
    Hom(J(f7_b), J(f5_a)) = 0.                       (2.1)

This remains true after any further finite cover of B. The same assertions hold with g7 in place of f7.

**Theorem B.** Let Gamma be a rational codimension-two algebraic cycle on S5 x S7. If every irreducible surface in its support has image of dimension at most one under f5 x f7, its induced map on transcendental cohomology has zero R5-to-R7 component. In fact its entire T(S5)-to-T(S7) component is zero. The same conclusion holds with f5 x g7.

Consequently a cycle with a nonzero target component must contain a surface dominating P^1 x P^1 under f5 x f7; the same is necessary under f5 x g7, though the required dominating components need not be the same in a reducible cycle. Each such dominant surface is generically finite over the base product.

This excludes a specified **support class**, not all algebraic correspondences. It is not a nonalgebraicity theorem. In particular it does not turn the abstract Hodge isomorphism R5 ~= R7 into a contradiction. Using U46's Hodge-space calculation, pencil-supported cycles in Theorem B lie in the known 17-dimensional point/divisor part, not the missing 24-dimensional part.

## 3. The constant genus-two Jacobian is simple

On T=1, write t=X. The first pencil is

    Z^2+Y^5+t^2(1+t^7)=0.

Adjoin w with w^10=t^2(1+t^7). The substitution

    Y=w^2 u,       Z=i w^5 v

identifies its generic fibre with the fixed curve

    C5: v^2=u^5+1.                                    (3.1)

The five finite branch points and infinity are distinct; the smooth completion has genus two. The order-five automorphism u -> zeta_5 u acts on the holomorphic differentials du/v and u du/v with eigenvalues zeta_5,zeta_5^2. Together with the conjugate eigenvalues these exhaust Phi_5, so Q(zeta_5) embeds in End^0(J(C5)) and has degree 2 dim J(C5).

Its CM type {1,2} has trivial stabilizer in (Z/5)^*. In a Galois CM field, an induced type is a union of cosets of a nontrivial subgroup; thus this type is primitive. Equivalently Q(zeta_5) has no proper CM subfield: its only quadratic subfield is real. The CM classification [1, Propositions 3.12-3.13] proves that J(C5) is simple.

This simplicity is geometric. Homomorphisms of abelian varieties over an algebraically closed field are unchanged by an algebraically closed extension, by rigidity; equivalently a purported new idempotent spreads in a discrete Hom scheme and specializes to the constant variety. Thus J(C5) stays simple over the algebraic closure of any complex function field used below. No theorem about arbitrary genus-two Jacobians is being asserted.

## 4. A nonseparating node survives every finite base change

For the second canonical pencil put

    F_t(u)=u^5+t^7 u+1,       C_t: Z^2+F_t(u)=0.

Its discriminant is

    disc_u(F_t)=3125+256t^35.                           (4.1)

The polynomial (4.1) has exactly 35 distinct roots in C, none zero. For each root t0, a repeated root r of F_t0 necessarily satisfies

    r^5=1/4,       t0^7=-5r^4,       r=-5/(4t0^7).       (4.2)

The last identity proves uniqueness. Conversely it supplies a double root for every root of (4.1). There is an exact factorization

    F_t0(u)=(u-r)^2 (u^3+2r u^2+3r^2 u+4r^3).         (4.3)

The cubic on the right has discriminant -200r^6, and its value at u=r is 10r^3. These are nonzero. Thus the special fibre is irreducible, with precisely one ordinary node in its affine chart. Its normalization is the double cover defined by that squarefree cubic, so is connected of genus one. In particular the node is **nonseparating**, not a separating degeneration invisible on H^1.

There are no singularities at the hyperelliptic point at infinity in this local family. With u=1/x, Z=z/x^3, the equation becomes

    z^2+x+t^7 x^5+x^6=0,

whose x derivative at x=z=0 is 1. At the node the derivatives are

    F_uu(r,t0)=20r^3 != 0,       F_t(r,t0)=7t0^6 r != 0.

The total space is therefore smooth near the node and this is a simple smoothing. The local model is analytically xy=s, up to units and coordinate changes. Picard-Lefschetz [2, Section 4.9, especially (4.9.16)] gives on rational H^1 a transvection

    T=I+N,       rank(N)=1,       N^2=0.                (4.4)

Here N is nonzero because the normalization is connected; pinching the nonseparating loop supplies a nonzero vanishing cycle. This is also immediate from the single-loop dual graph in [2, (4.9.1)]. Reversing a homology/cohomology or orientation convention can reverse the sign of N but cannot affect its rank or nonvanishing.

A finite base change of ramification index e >= 1 replaces a small loop by its e-th power. Consequently

    T^e=I+eN != I over Q.                               (4.5)

This is a uniform argument, not a finite test of selected degrees. The checker corroborates N^2=0 and the polynomial identity (I+eN)(I+kN)=I+(e+k)N; induction proves (4.5) for every e. The zero index, which would give the identity, is excluded precisely because the base map is nonconstant.

As an additional exact diagnostic, scaling u=r a in the normalization makes all these elliptic normalizations geometrically isomorphic to

    b^2=a^3+2a^2+3a+4,

which has j=160. This is not used to deduce a correspondence between surfaces and is not a claim about the CM status of that elliptic curve.

## 5. Proof of Theorem A for the canonical pencils

Assume a nonzero homomorphism of the two geometric generic Jacobians exists. It is defined over a finite extension of C(B), since its graph is specified by finitely many algebraic coefficients. Extend further to make J(f5_a) the constant J(C5).

A nonzero homomorphism from a simple abelian surface to an abelian surface is an isogeny: its connected kernel cannot be a proper positive-dimensional abelian subvariety. A nonzero homomorphism in the opposite direction is likewise an isogeny, since its image is a nonzero abelian subvariety of the simple target and both dimensions are two.

Normalize B in this extension and compactify. The map to the second P^1 is still nonconstant, hence finite and surjective. Choose a point above any one of the 35 parameters (4.1). On a punctured disk there, the supposed generic isogeny spreads to an isogeny of the smooth Jacobian families after shrinking. It induces an invertible map of rational H^1 local systems intertwining monodromy.

The constant side has identity monodromy. The other side has the nonidentity operator I+eN for the total positive ramification index e, by (4.5). These cannot be conjugate by an invertible map. This contradiction proves both Hom vanishing statements and proves their invariance under all further finite covers.

The argument does **not** infer Hom vanishing merely from varying moduli: a nonsimple constant Jacobian could map through a constant elliptic factor. Simplicity and equal dimensions are essential here. Nor is a number-field good-reduction criterion applied without translation to the present complex function-field setting; the proof uses local systems directly.

## 6. From generic Hom vanishing to cycle-support vanishing

We state the support argument explicitly so that absence of a fibre isogeny is not mistaken for absence of every surface correspondence.

Let F1:S1 -> B1 and F2:S2 -> B2 be fibrations of smooth projective complex surfaces with smooth connected generic fibres. Suppose that, for every curve B mapping nonconstantly to both bases, the geometric generic Jacobians of the pulled-back curves have no Hom between them.

Consider one irreducible surface Gamma in S1 x S2 whose base image has dimension at most one.

If the image is a point, or a curve constant in either coordinate, Gamma is supported in D x S2 or S1 x E for a curve D or E in a surface. Such correspondences have zero transcendental-to-transcendental action. For support D x S2, the action factors through H^2 of the normalization of D, and restriction of T(S1) there is zero by orthogonality to [D]. For support S1 x E, the image lies in the span of the divisor classes of E's components. Normalizing curves and pushing their cycles justifies the same argument for singular/reducible supports.

Otherwise normalize the base-image curve to B. Over a nonempty open part of B, the fibre product

    V=(S1 x_B1 B) x_B (S2 x_B2 B)

is a smooth family of products of curves, with dimension three. The strict transform of Gamma is a divisor on V, whose geometric generic fibre is a divisor on C1 x C2 over F=C(B). All fibres under consideration here have a rational point at infinity. More generally a finite extension supplies points, and rational coefficients allow division by the eventual pushforward degree.

For pointed curves, subtracting the restrictions to C1 x {P2} and {P1} x C2 normalizes a line bundle to a divisorial correspondence. By [3, Corollary 6.3], the group of these normalized classes is Hom(J(C1),J(C2)). Hence its vanishing gives the exact generic-fibre statement

    [Gamma_F]=pr1^*[D1]+pr2^*[D2] in Pic(C1 x C2).      (6.1)

This is equality of line-bundle/divisor classes, not just equality of numerical degrees. A rational function realizes the difference. Spread that function and the divisors over an open subset of B, then take their closures in a proper model of V. The remaining difference of cycle classes is supported in finitely many fibres. These operations can be performed on a resolution; exceptional terms either push to lower dimension or to the same vertical support.

After pushforward to S1 x S2, the closure of pr1^*D1 is supported in a curve of S1 times S2: D1 is a finite divisor in the generic fibre, and its closure is a multisection curve over B. The other term is supported in S1 times a curve of S2. Vertical surfaces map into products of fibre curves. All have zero transcendental-to-transcendental action by the preceding support calculation. Linearity handles arbitrary rational cycles. This proves the support lemma, and (2.1) applies it to f5 x f7.

Only generic divisor classes on a product of **two curves** were reduced by Picard/Jacobian theory. The argument is not applied to a divisor of a surface product dominating the two-dimensional base, which is precisely the remaining case.

## 7. Executed follow-up: a second pencil and actual fixed-curve covers

The failure of the canonical fibrewise route does not end the construction program. A different pencil on S7 becomes constant, and both surfaces admit explicit product-of-fixed-curves covers.

Let D5 and D7 be the smooth projective normalizations of

    D5: w^10=t^2(1+t^7),
    D7: w^14=t^6(1+t^5).

Let C5 be (3.1), and let C7 be the smooth projective curve

    C7: v^2=u^7+1.                                     (7.1)

There are generically finite rational maps, defined over Q(i),

    phi5: D5 x C5 -> S5_bar,
      (t,w;u,v) |-> [1:t:w^2 u:i w^5 v],               (7.2)

    phi7: D7 x C7 -> S7_bar,
      (t,w;u,v) |-> [1:w^2 u/t:t:i w^7 v/t^3].         (7.3)

In (7.3), t is **Y**, not X. Direct substitution into the two weighted equations gives zero; all denominators are restricted to the stated dense torus. Thus there is no conflict between (7.3) and the nonisotrivial canonical X pencil.

Each D cover is connected with the indicated full degree: its radicand has a simple finite root, which forces ramification index ten or fourteen in the Kummer extension. The inverse reconstructions on the dense image are obtained by choosing w and then recovering u,v from (7.2) or (7.3). The faithful actions

    (w,u,v) |-> (eta w, eta^(-2)u, eta^(-q)v),
    eta^(2q)=1,      q=5 or 7,

fix the image. They yield respectively ten and fourteen distinct generic preimages. Thus deg(phi5)=10 and deg(phi7)=14, not just upper bounds from radical equations.

For a connected degree-n cyclic cover of P^1 with valuations a_j of the radicand (including infinity), the local ramification calculation gives n-gcd(n,a_j) in the Riemann-Hurwitz sum. Here the data are

    D5: n=10; valuations (2,1,1,1,1,1,1,1,-9),
    D7: n=14; valuations (6,1,1,1,1,1,-11).

Consequently

    2g(D5)-2=-20+(8+7*9+9)=60,     g(D5)=31,
    2g(D7)-2=-28+(12+5*13+13)=62,  g(D7)=32.

C5 and C7 have genera two and three. Resolving the rational surface maps changes source H^2 only by algebraic point-blowup terms. The usual proper push-pull identity, restricted to transcendental H^2, gives

    phi5_* phi5^*=10 id,       phi7_* phi7^*=14 id.     (7.4)

The transcendental pullbacks lie in H^1(D5) tensor H^1(C5) and H^1(D7) tensor H^1(C7), respectively; the other Kunneth terms in H^2 of a product of curves are algebraic. Hence (7.2)-(7.4) give an explicit injective algebraic transport of the unresolved mixed block to

    H^1(D5) tensor H^1(C5) tensor H^1(D7) tensor H^1(C7)
      subset H^4(D5 x C5 x D7 x C7),                   (7.5)

with inverse on its image obtained by dividing pushforward by 140. This is a degree-preserving, codimension-two construction, not a Tate-shift inference. Together with the pinned U46 transfer it is another exact source for W. It does **not** exhibit a cycle in that image.

### 7.1 A second support obstruction

The order-seven automorphism of C7 has holomorphic eigencharacters {1,2,3}. Its type has trivial stabilizer in (Z/7)^*, so [1] makes J(C7) a simple abelian threefold. An explicit negative control is {1,2,4}, whose stabilizer {1,2,4} would instead be an induced type; our checker distinguishes them.

J(C5) and J(C7) are simple of different dimensions. They therefore have no nonzero homomorphisms over any algebraically closed extension. After arbitrary finite base changes making the f5 and g7 fibres constant, their Hom vanishes. The support lemma of Section6 proves Theorems A and B also for f5 x g7.

Thus merely replacing the second canonical pencil by its new isotrivial pencil does not supply a fibrewise cycle. The surviving construction must genuinely couple the two base parameters, or use a different geometric mechanism.

## 8. Scope, sources and self-review

The argument chain is

    explicit simple constant C5
      + one irreducible nonseparating nodal degeneration of f7
      -> no geometric generic Jacobian Hom after any finite cover
      -> exact generic Picard decomposition
      -> vanishing for correspondences supported over base curves.

The alternate chain uses the simple nonisogenous C5,C7 and the same support lemma. The maps (7.2)-(7.4) are an additional positive geometric reduction.

The algebraic input needed for the **global Hodge target** is still absent. Neither a nontrivial Hodge isomorphism nor domination by a product of curves implies its algebraicity. A correspondence dominating P^1 x P^1 is not examined by the fibrewise Picard argument. Arithmetic coefficient restrictions from U39-U40 are not bypassed by defining cover maps over Q(i).

**Adversarial self-review:**

- Constants, base variables and fibre variables have been distinguished; (7.5) is a product of four curves of complex dimension four, not a surface or the earlier nineteen-dimensional abelian source.
- The discriminant is not used alone: uniqueness, irreducibility, nonseparating character, total-space smoothness and infinity were all checked before applying Picard-Lefschetz.
- A finite cover multiplies a nonzero unipotent logarithm; it cannot kill it in characteristic zero. No bounded enumeration stands in for arbitrary cover degree.
- Simplicity of the constant genus-two Jacobian is proved before inferring isogeny from a nonzero Hom.
- The support implication passes through equality in Pic, spreading and pushforward, not merely fibrewise equality of degrees; vertical terms are accounted for.
- Blowups and map resolutions add algebraic H^2 only; (7.4) is claimed on transcendental cohomology, not as an unqualified isomorphism of Chow motives.
- Theorem B concerns cohomological projection. It does not claim every excluded correspondence is rationally zero.
- No expert or formal verification has occurred. Separate Wolfram arithmetic checks the same explicit inputs, not the topological or Picard theorems.

### Sources read directly in this run

[1] J. S. Milne, *Complex Multiplication*, v0.10, 14 July2020, Propositions3.12-3.13, printed p.30 (PDF index29), and the definition of primitive CM type. The classification of primitive CM pairs is applied to the explicitly computed types above. Author-hosted PDF, accessed15 September2026: https://www.jmilne.org/math/CourseNotes/CM.pdf

[2] L. Illusie, *Grothendieck and vanishing cycles*, author-hosted 36-page manuscript corresponding to Ann. Fac. Sci. Toulouse30(2021),83-115, DOI10.5802/afst.1667. Section4.9, especially(4.9.1),(4.9.12),(4.9.16), manuscript pp.18-20 (PDF indices17-19), and Section6.1. The single irreducible nodal fibre yields a nonzero symplectic transvection. The formula and its diagrams were inspected in rendered pages. The proof here uses the complex local-system version, and checks the nonseparating hypothesis directly. https://www.imo.universite-paris-saclay.fr/~luc.illusie/Illusie-Grothendieck-nearby-cycles12.pdf

[3] J. S. Milne, *Jacobian Varieties*, original article1986, corrected author version12 June2021, definition of divisorial correspondence in Section1 and Corollary6.3 with proof, printed p.20 (PDF index19). This identifies normalized line bundles on a pointed curve product with Hom of its Jacobians; subtracting the two point restrictions gives(6.1). https://www.jmilne.org/math/xnotes/JVs.pdf

Source scope: these classical implications were checked directly; no global novelty claim is made for them or for the displayed specialized consequences. The modern preliminary motivic Picard-Lefschetz preprint was a discovery aid only and supplies no load-bearing theorem here. A number-field good-reduction corollary was not silently extended to C(B). Source PDFs were read online, not redistributed in the evidence package.

### Reproducibility and next obligation

    python research/computations/U47/verify_u47.py --output research/computations/U47/verification.json

Nine focused tests cover the exact polynomial, local and covering identities and the complete small CM-type stabilizers. The symbolic e,k identity, combined with the written induction, covers all positive local base-change indices. The finite checker does not certify Picard-Lefschetz, complex multiplication classification, or the spreading proof.

The supplied local CM19 U46 checker is rerun separately and labeled as that **distinct** input. It does not count as a reproduction of remote Horikawa U46. Actual tool/version/validation results, hashes and separate Wolfram input/output are stored beside the checker.

**Executable next research problem:** construct a codimension-two cycle in the explicitly identified image(7.5), equivalently a surface correspondence with nonzero mixed projection on S5 x S7, whose base image has dimension two for both pencil pairs. One can start with the fixed-curve equations and the two cyclic quotient actions in Section7; assembling only generic fibre divisors is now excluded. No such cycle is claimed in this checkpoint.
