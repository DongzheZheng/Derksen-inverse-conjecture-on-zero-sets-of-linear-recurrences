import ArithDyn.Derksen.Prop26

/-!
# Derksen's inverse conjecture

Every `p`-normal subset of the natural numbers is the zero set of a linear recurrence
with coefficients in the fixed rational function field `𝔽_p(t)`.
-/

set_option autoImplicit false

namespace ArithDyn.Derksen

/-- Every `p`-normal set is realized over `𝔽_p(t)`, with equality of zero sets. -/
theorem realization (p : ℕ) [Fact p.Prime] (S : Set ℕ)
    (hS : IsPNormal p S) :
    ∃ (recurrence : LinearRecurrence (RatFunc (ZMod p)))
      (u : ℕ → RatFunc (ZMod p)),
      recurrence.IsSolution u ∧ {n | u n = 0} = S :=
  theorem22 p S hS

end ArithDyn.Derksen
