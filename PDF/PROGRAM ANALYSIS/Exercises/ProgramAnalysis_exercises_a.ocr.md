## Program Analysis 2025/26

Exercises - May 21, 2026

[Ex. 1] Let us consider the following axiom for atomic boolean guards b ? , where the parentheses ⟨ | · | ⟩ ∈ { {·} , [ · ] , ( · ) , ⟨·⟩ } are used to denote a generic program logic triple of either Hoare logic, IL, NC or SIL.

<!-- formula-not-decoded -->

Explain for which logics (HL, IL, NC, SIL) the axiom is sound (for any precondition P and boolean guard b ):

- if the axiom is sound, prove its validity;
- if it is not sound, first provide a concrete counterexample and then say under which conditions on P and b the axiom would become sound.
- [Ex. 2] Let us consider the usual concrete domain ( ℘ ( Z ) , ⊆ ) of sets of integers ordered by inclusion and the abstract domain A = { ⊥ , = 0 , ≤ 0 , &gt; 10 , &gt; 0 , ⊤ } with the obvious concretization function.
1. Define the GC maps γ : A → ℘ ( Z ) and α : ℘ ( Z ) → A .
2. Draw the Hasse diagram of A .
3. Define the bca · × A · for the product of integers · × · .
4. Show that · × A · is not complete by exhibiting a counterexample.
- [Ex. 3] Consider the following expression e :
1. Add labels to all subexpressions and function abstractions.
2. Guess a possible analysis result for Pure 0-CFA and verify it using the corresponding acceptability relation | = . In particular, comment on the abstract values associated with the two calls to apply .
3. Consider the following additional abstract flow:

```
let apply = fn f => f 2 in let inc = fn x => x + 4 in let dbl = fn y => y * 2 in (apply inc) - (apply dbl)
```

<!-- formula-not-decoded -->

Does the acceptability relation | = still hold? What does this say about the difference between soundness and precision?

4. Discuss how the analysis changes using the syntax-directed version of the acceptability relation | = s .
5. Extract the corresponding system of constraints.
6. Explain how the result changes under 1-CFA. Which spurious flows disappear, and why?