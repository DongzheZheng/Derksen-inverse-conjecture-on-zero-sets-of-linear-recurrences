# Verification

The project uses Lean 4.29.0 and Mathlib commit `8a178386ffc0f5fef0b77738bb5449d50efeea95`. `lean-toolchain` selects Lean, and `lake-manifest.json` fixes all external dependency revisions.

## Reproducing the checks

From the repository root, run:

```sh
lake exe cache get
lake build ArithDyn
python3 scripts/check_axioms.py
```

The first command downloads the compiled Mathlib cache for the pinned revision. The second builds the proof library, including the public theorem in `ArithDyn/Derksen/Main.lean`. The third runs Lean on [`Checks/Axioms.lean`](../Checks/Axioms.lean) and checks the axiom reports for the public theorem and 34 principal declarations.

To inspect the reports directly, run:

```sh
lake env lean Checks/Axioms.lean
```

The audit fails if Lean exits unsuccessfully, a declaration's report is missing or repeated, or a reported axiom falls outside the following list:

- `propext`
- `Classical.choice`
- `Quot.sound`

These are the standard Lean axioms used by the formal proof. The final theorem has only the prime hypothesis and `IsPNormal p S` as inputs; its conclusion is exact equality with a recurrence zero set over `RatFunc (ZMod p)`.

## Continuous integration

The [Lean workflow](../.github/workflows/lean.yml) builds the pinned library and runs the same axiom audit on pushes to `main`, on pull requests, and on manual requests. Build output and axiom reports are available in the [Actions runs](https://github.com/DongzheZheng/Derksen-inverse-conjecture-on-zero-sets-of-linear-recurrences/actions/workflows/lean.yml).

These checks concern elaboration, kernel acceptance, and transitive axiom dependencies. They do not independently rebuild Lean or all of Mathlib from source. The formalization's correspondence with the paper is described in the [proof guide](proof-guide.md).
