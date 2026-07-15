## Program Analysis 2025/26

Exercises - May 21, 2026

## [Ex. 1] Consider the following code fragment c :

```
x := [y]; if (x != nil) then { free(y); y := x; } else { x := alloc(); [y] := x; }
```

Using Incorrectness Separation Logic, find a suitable (non-trivial) postcondition Q for the triple [ y ↦→ z ∗ z ↦→ nil ] c [ ok : Q ] and inline the intermediate derivation steps that lead to such conclusion.

- [Ex. 2] Given a function f : Z → Z , let L f : ℘ ( Z ) → ℘ ( Z ) denote its ordinary powerset lifting defined as L f ( X ) ≜ { f ( x ) | x ∈ X } and let I f : ℘ ( Z ) → ℘ ( Z ) be defined as I f ( Y ) ≜ { x | f ( x ) ∈ Y } the inverse image function of f .
1. Prove that L f and I f form a Galois connection.
2. Under which condition on f they form a Galois insertion?
- [Ex. 3] Consider the following expression e :

```
let n = 5 in let choose = if n > 0 then (fn x => x + 1) else (fn y => y * 2) in choose 4
```

Assume a sign analysis with

<!-- formula-not-decoded -->

1. Add labels to all subexpressions and function abstractions.
2. Guess a possible Pure 0-CFA analysis result and verify it using the acceptability relation | = .

In particular, determine the possible closures flowing to choose at the application

( choose 4) .

3. Explain why Pure 0-CFA cannot determine that one branch of the conditional is unreachable.
4. Perform the DFA using abstract values as powersets:

<!-- formula-not-decoded -->

Compute the abstract values associated with:

<!-- formula-not-decoded -->

5. Explain how the DFA refines the CFA result. Which branch becomes unreachable?
6. Repeat the DFA using the complete lattice formulation of the same sign information and compare the two analyses.
7. Explain why the refined CFA+DFA result is still sound.