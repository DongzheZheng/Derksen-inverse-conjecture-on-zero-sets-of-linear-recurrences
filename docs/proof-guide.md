# Proof guide

All declarations below belong to the namespace `ArithDyn.Derksen`. The public entry point is [`realization`](../ArithDyn/Derksen/Main.lean), which expands the conclusion of `theorem22` into a recurrence over `RatFunc (ZMod p)` and exact equality of zero sets.

## Definitions and conventions

[`Normal.lean`](../ArithDyn/Derksen/Normal.lean) defines `ElementaryData`, `elementarySet`, `IsPNormalBase`, and `IsPNormal`. Membership in an elementary set equates a rational sum to a natural number, so negative values are excluded after the sum is formed. `IsPNormal` allows a finite symmetric difference with a finite union of elementary sets, finite sets, and arithmetic progressions.

One-sided sequences use Mathlib's `LinearRecurrence.IsSolution`. Fundamental sequences at integer times use `IsFundRec`, with a nonzero constant term in an annihilating polynomial, or the equivalent representation `LinRepZ` by an invertible state matrix. Their integer zero sets form `RClass`. Mathlib permits order-zero recurrences; the only solution in that case is the zero sequence, which also satisfies a positive-order recurrence.

## From the paper to Lean

The module names and identifiers `Theorem22`, `Prop26`, `Prop27`, `theorem22`, `prop26`, and `prop27` retain the numbering of the original combined paper. Numbered references in source comments follow that convention. The table below uses the numbering of the standalone paper, *Derksen's inverse conjecture on zero sets of linear recurrences*.

| Standalone statement | Principal declarations | Source |
| --- | --- | --- |
| Definition 1.1: elementary and normal sets | `ElementaryData`, `elementarySet`, `IsPNormalBase`, `IsPNormal` | [Normal](../ArithDyn/Derksen/Normal.lean) |
| Theorem 1.2: inverse realization over $\mathbb F_p(t)$ | `realization`, `theorem22` | [Main](../ArithDyn/Derksen/Main.lean), [Prop26](../ArithDyn/Derksen/Prop26.lean) |
| Lemma 2.1: integer-time closure operations | `RClass.union_mem`, `RClass.affine_preimage_mem`, `RClass.affine_image_mem` | [ZRec](../ArithDyn/Derksen/ZRec.lean), [FundRec](../ArithDyn/Derksen/FundRec.lean) |
| Lemma 2.2: descent of constants | `IsFundRec.norm`, `IsLinRecSeq.norm`, `RClass.descent_ratFunc` | [Descent](../ArithDyn/Derksen/Descent.lean), [RatFuncGalois](../ArithDyn/Derksen/RatFuncGalois.lean) |
| Lemma 2.3: combining equations | `RClass.inter_mem_ratFunc`, `RClass.finset_iInter_mem_ratFunc` | [RatFuncGalois](../ArithDyn/Derksen/RatFuncGalois.lean) |
| Lemma 3.1: signed Frobenius reconstruction | `reconstruct`, `reconstruct_aux`, `star_identity`, `fk_irreducible` | [Reconstruct](../ArithDyn/Derksen/Reconstruct.lean), [Frobenius](../ArithDyn/Derksen/Frobenius.lean) |
| Lemma 4.3: descent from evaluations | `exists_coeff_descent`, `coeff_descent_eq` | [CoeffDescent](../ArithDyn/Derksen/CoeffDescent.lean) |
| Proposition 4.4: small signed weights | `Eset_mem_RClass_ratFunc`, `prop26`, `mem_Eset_of_aeval_Pn_eq_zero` | [Prop26](../ArithDyn/Derksen/Prop26.lean), [TorusBackward](../ArithDyn/Derksen/TorusBackward.lean) |
| Proposition 5.2: arbitrary signed weights | `prop27`, `prop27_of_prop26`, `exists_gap`, `Eset_eq_iUnion_faces` | [Prop26](../ArithDyn/Derksen/Prop26.lean), [Decomposition](../ArithDyn/Derksen/Decomposition.lean) |
| Section 6: rational weights and finite modifications | `theorem22_of_prop27`, `mem_elementarySet_iff`, `IsLinRecSeq.modify` | [Normal](../ArithDyn/Derksen/Normal.lean), [LinRec](../ArithDyn/Derksen/LinRec.lean) |

## Algebraic reconstruction

[`Frobenius.lean`](../ArithDyn/Derksen/Frobenius.lean) establishes the coefficientwise Frobenius map, irreducibility of the factors used in the descent, and a differential identity obtained from evaluation data. [`Reconstruct.lean`](../ArithDyn/Derksen/Reconstruct.lean) uses well-founded induction on the pair $(\deg_X N+\deg_X D,|n|)$. Removing one numerator or denominator factor reduces the degree; when no such factor remains, taking coefficient roots reduces $|n|$. The case $n=0$ follows from sufficiently many evaluations. The paper groups repeated factor removals into full signed multiplicities, while the formal proof removes one factor at a time.

The formal statement uses numerator and denominator polynomials in `F[t][X]`, after clearing coefficient denominators. Its evaluation bound is $p^{e-1}+\deg N+\deg D<|\mathcal A|$. It gives the algebraic form needed in the realization proof.

## Specialization and the original weights

[`Torus.lean`](../ArithDyn/Derksen/Torus.lean) defines the evaluation ideal and proves the forward orbit-membership implication. Polynomial evaluation along an orbit gives a recurrence. For the converse, [`ValuationPoint.lean`](../ArithDyn/Derksen/ValuationPoint.lean) extends a specialization to a valuation subring. [`TorusBackward.lean`](../ArithDyn/Derksen/TorusBackward.lean) uses its residues to recover ratios of evaluations at a boundary point.

[`CoeffDescent.lean`](../ArithDyn/Derksen/CoeffDescent.lean) recovers coefficients over a common field from the evaluation equations. [`Grouping.lean`](../ArithDyn/Derksen/Grouping.lean) and [`BackwardAux.lean`](../ArithDyn/Derksen/BackwardAux.lean) compare the reconstructed factors with groups of equal parameters. Groups whose total weight is zero may cancel completely. A root-of-unity congruence, together with the weight bound, forces the total weight of parameters at infinity to be zero.

This proves the boundary implication directly with valuation rings. It does not formalize the paper's projective graph closure as a scheme, nor provide separate declarations for every explanatory example. The final theorem has no remaining small-weight or geometric premise.

## The final reductions

[`Decomposition.lean`](../ArithDyn/Derksen/Decomposition.lean) uses a common origin on a residue circle to divide an arbitrary signed-weight set into finitely many small-weight pieces and lower-dimensional pieces. The construction follows the circle-gap method of Lee and Nam.

The recurrence modules supply products, affine changes of time, finite modifications, Galois norm descent, and finite intersections. The intersection proof iterates binary combinations rather than selecting one coefficient-field basis for all equations at once. [`Prop26.lean`](../ArithDyn/Derksen/Prop26.lean) assembles these results into `prop26`, `prop27`, and `theorem22`.

The forward direction of the paper's classification corollary relies on Derksen's theorem in the literature. The linear-orbit corollary is not a separate named endpoint here; the state-representation equivalence used in its deduction is formalized.
