# Provenance and references

The sixteen proof modules originate in the Derksen portion of [*Realization, Extension, and Orbit Obstructions in Arithmetic Dynamics*](https://github.com/veridiscoverLab/arithmetic-dynamics-realization-extension-obstructions), at commit [`e127ceaa02f1003e59b1b5c772583a6e80d04ce5`](https://github.com/veridiscoverLab/arithmetic-dynamics-realization-extension-obstructions/tree/e127ceaa02f1003e59b1b5c772583a6e80d04ce5).

This repository retains the original module names, declarations, and proof code. Documentation comments have been corrected where they contained outdated scope claims or incomplete references. `Main.lean` adds the expanded public theorem `realization`; the library entry point, axiom audit, build workflow, and reader documentation make the Derksen formalization independently usable. The package name in the lock file has been aligned with `lakefile.toml`; all external dependency revisions are retained. Mathlib is also pinned by its exact commit in `lakefile.toml`.

## Mathematical background

- H. Derksen, *A Skolem–Mahler–Lech theorem in positive characteristic and finite automata*, Inventiones Mathematicae **168** (2007), 175–224. [DOI](https://doi.org/10.1007/s00222-006-0031-0), [preprint](https://arxiv.org/abs/math/0510583). The paper proves the forward classification, formulates the inverse conjecture, and develops recurrence closure constructions.
- P. Corvaja, D. Ghioca, T. Scanlon, and U. Zannier, *The dynamical Mordell–Lang conjecture for endomorphisms of semiabelian varieties defined over fields of positive characteristic*, Journal of the Institute of Mathematics of Jussieu **20** (2021), 669–698. [DOI](https://doi.org/10.1017/S1474748019000318), [preprint](https://arxiv.org/abs/1802.05309). Proposition 4.3 supplies the positive-weight finite-field evaluation construction adapted here.
- J. Lee and G. Nam, *A converse of dynamical Mordell–Lang conjecture in positive characteristic*, Proceedings of the American Mathematical Society **153** (2025), 603–609. [DOI](https://doi.org/10.1090/proc/17004), [preprint](https://arxiv.org/abs/2403.05107). Section 3 supplies the finite circle-gap decomposition used for arbitrary signed weights.

The formalization uses established algebra in Mathlib, including finite fields, Galois norms, Cayley–Hamilton, Noetherian rings, fraction fields, and valuation subrings.

## License status

The cited source revision contains no project license file. No license has been inferred or assigned to the inherited proof sources here. Mathlib and its dependencies retain their respective licenses; their source code is fetched through Lake and is not included in this repository.
