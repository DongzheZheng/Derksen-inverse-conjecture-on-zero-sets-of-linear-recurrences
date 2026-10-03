# Derksen's inverse conjecture on zero sets of linear recurrences

[![Lean](https://github.com/DongzheZheng/Derksen-inverse-conjecture-on-zero-sets-of-linear-recurrences/actions/workflows/lean.yml/badge.svg)](https://github.com/DongzheZheng/Derksen-inverse-conjecture-on-zero-sets-of-linear-recurrences/actions/workflows/lean.yml)

A Lean 4 formalization of the inverse theorem: every $p$-normal subset of the nonnegative integers is the zero set of a linear recurrence over the fixed rational function field $\mathbb F_p(t)$.

Derksen proved that recurrence zero sets in characteristic $p$ are $p$-normal and conjectured the converse. Here the recurrence is realized over $\mathbb F_p(t)$ for every prime $p$, with equality of zero sets. Rational shifts, signed weights, arithmetic progressions, and arbitrary finite modifications are included.

## Main theorem

Import `ArithDyn` to use `ArithDyn.Derksen.realization`:

```lean
import ArithDyn

example (p : ℕ) [Fact p.Prime] (S : Set ℕ)
    (hS : ArithDyn.Derksen.IsPNormal p S) :
    ∃ (recurrence : LinearRecurrence (RatFunc (ZMod p)))
      (u : ℕ → RatFunc (ZMod p)),
      recurrence.IsSolution u ∧ {n | u n = 0} = S :=
  ArithDyn.Derksen.realization p S hS
```

`RatFunc (ZMod p)` is the formal coefficient field $\mathbb F_p(t)$. The recurrence relation holds from time zero; its constant coefficient may vanish, which allows finite changes to the zero set. Its order is finite and may depend on `S`.

For $q=p^e$ with $e\geq1$, an elementary $p$-nested set has the form

$$
\left\{c_0+\sum_{i=1}^{r}c_iq^{k_i}:k_i\geq0\right\}\cap\mathbb N_0,
$$

Here $r\geq1$, the coefficients $c_0,\ldots,c_r$ are rational, and the variable weights $c_1,\ldots,c_r$ are nonzero with at least one positive weight. The exponents vary independently, $(q-1)c_i\in\mathbb Z$ for $0\leq i\leq r$, and $\sum_{i=0}^{r}c_i\in\mathbb Z$. A $p$-normal set differs by finitely many elements from a finite union of such sets, finite sets, and infinite arithmetic progressions. These definitions are in [Normal.lean](ArithDyn/Derksen/Normal.lean).

## Build and verify

With [Elan](https://github.com/leanprover/elan) installed, run:

```sh
lake exe cache get
lake build ArithDyn
python3 scripts/check_axioms.py
```

The project pins **Lean 4.29.0** and **Mathlib 4.29.0**. Exact dependency revisions are recorded in `lake-manifest.json`. The axiom check examines the main theorem and 34 principal declarations, accepting only `propext`, `Classical.choice`, and `Quot.sound`. GitHub Actions runs the same build and check on pushes to `main` and on pull requests.

## Reading the proof

The proof first realizes signed sums of powers at integer times. Frobenius reconstruction identifies a rational function from sufficiently many evaluations, including its signed factor multiplicities and the integer exponent. Valuation-ring specialization handles boundary parameters; an auxiliary root-of-unity condition controls the total weight at infinity. A circle-gap decomposition removes the size restriction on the weights. Closure operations and descent of constants then yield the general $p$-normal case over $\mathbb F_p(t)$.

- [Proof guide](docs/proof-guide.md): definitions, principal declarations, and correspondence with the standalone paper.
- [Verification](docs/verification.md): the build, axiom check, and their scope.
- [Provenance](docs/provenance.md): source history, mathematical references, and license status.

The formalization proves the inverse-realization theorem. Derksen's forward classification theorem is cited as background and is not formalized here. The boundary argument uses valuation rings and the evaluation ideal; the paper presents the corresponding argument through a projective graph closure.
