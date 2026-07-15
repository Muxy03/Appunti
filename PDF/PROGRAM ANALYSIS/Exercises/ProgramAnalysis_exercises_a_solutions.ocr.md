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

requires

Thus, for the proposed axiom we would need

<!-- formula-not-decoded -->

is sound when every terminating execution from a state satisfying P ends in a state satisfying Q . Since executing b ? does not modify the state, every reachable state satisfies both P and b . In fact:

<!-- formula-not-decoded -->

Hence the axiom is sound for Hoare Logic.

Incorrectness Logic. A valid Incorrectness Logic triple

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This is false in general: as a simple counterexample, let

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence the axiom is not sound. The axiom becomes sound iff

<!-- formula-not-decoded -->

Since it is always the case that P ∧ b ⊆ P ∨ b, , the condition is equivalent to

<!-- formula-not-decoded -->

Then

and thus equivalent to

<!-- formula-not-decoded -->

where b ? is an atomic boolean guard command and the brackets denote, depending on the logic, Hoare Logic (HL), Incorrectness Logic (IL), Necessary Condition Logic (NC), or Sufficient Incorrectness Logic (SIL). Operationally, the command b ? succeeds without modifying the state exactly when b evaluates to true; otherwise it blocks, i.e., J b ? K P = P ∧ b.

## Hoare Logic. A Hoare triple

Since

and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

the axiom is sound for NC logic iff b ⊆ P . As a simple counterexample, let

<!-- formula-not-decoded -->

Sufficient Incorrectness Logic. SIL also requires an under-approximation condition:

<!-- formula-not-decoded -->

Thus the axiom is sound for SIL iff

<!-- formula-not-decoded -->

which is false in general. As a simple counterexample, let

<!-- formula-not-decoded -->

[Solution Ex. 2] We consider the concrete domain

<!-- formula-not-decoded -->

and the abstract domain

<!-- formula-not-decoded -->

## 1. Galois connection maps

The concretization map is:

The abstraction map is:

<!-- formula-not-decoded -->

or

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

̸

̸

<!-- formula-not-decoded -->

2. Hasse diagram

--

hence

<!-- formula-not-decoded -->

3. Best correct approximation of multiplication

The abstract multiplication is defined as

a

×

A

×

A

⊥

= 0

≤

0

&gt;

10

&gt;

0

⊤

×

A

⊥

= 0

≤

0

&gt;

10

&gt;

0

⊤

=

⊥

⊥

⊥

⊥

⊥

⊥

⊥

⊥

⊥

⊥

⊥

⊥

⊥

⊥

(

x

{

·

= 0

⊥

= 0

= 0

= 0

= 0

= 0

= 0

⊥

= 0

= 0

= 0

= 0

= 0

x

y

|

≤

0

⊥

= 0

⊤

≤

0

≤

0

⊤

≤

0

⊥

= 0

⊤

≤

0

≤

0

⊤

Note that the operation is symmetric.

4. BCA is non-complete

Consider

Then

b

α

∈

γ

(

a

)

&gt;

10

⊥

= 0

≤

0

&gt;

10

&gt;

10

⊤

&gt;

10

⊥

= 0

≤

0

&gt;

10

&gt;

10

⊤

,

y

∈

&gt;

0

⊥

= 0

≤

0

&gt;

10

&gt;

0

⊤

&gt;

0

⊥

= 0

≤

0

&gt;

10

&gt;

0

⊤

γ

(

b

)

}

⊤

⊥

= 0

⊤

⊤

⊤

⊤

⊤

⊥

= 0

⊤

⊤

⊤

⊤

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Concrete multiplication gives

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

)

.

However,

Therefore

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

because we must consider all non-positive integers. The products may be either 0 or positive values. Since the abstract domain has no element representing 'non-negative', the best abstraction is

<!-- formula-not-decoded -->

̸

proving that the abstract multiplication is not complete.

## [Solution Ex. 3]

<!-- formula-not-decoded -->

2.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

An acceptable solution is

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The key point is

<!-- formula-not-decoded -->

0-CFA merges different calling contexts, thus loosing precision.

3. If we add the extra flow

<!-- formula-not-decoded -->

where label 1 is the occurrence of f in the body of apply , the acceptability relation may still hold, provided that the additional abstraction is propagated consistently through the analysis.

The result is still sound, because it over-approximates the possible flows. However, it is less precise, because fn w =&gt; w is not a function that can actually flow to f in any concrete execution.

This illustrates that acceptability expresses soundness, not optimal precision.

4. The changes induced by the the syntax-directed version of the acceptability relation | = s are that the body of a function is analyzed once at definition time and not in relation to the application. This means that there is no need to analyze it more than once in case of multiple applications, but that it is analyzed also in the case the function is never applied.
5. The syntax-directed way of analysis prescribes to use only terms occurring in the expression under investigation.
6. These are the constraints extracted from the acceptability relation:

<!-- formula-not-decoded -->

From ( apply 13 inc 14 ) 15

<!-- formula-not-decoded -->

From ( apply 16 dbl 17 ) 18

<!-- formula-not-decoded -->

From ( f 1 2 2 ) 3

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The corresponding constraint system is generated compositionally from the syntax-directed rules.

<!-- formula-not-decoded -->

For functional abstractions:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For the nested let :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For variables:

<!-- formula-not-decoded -->

Arithmetic operators do not generate any flow:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For the applications, the constraint generation mechanism considers all function abstractions in

<!-- formula-not-decoded -->

Hence we obtain:

<!-- formula-not-decoded -->

Similarly:

<!-- formula-not-decoded -->

7.

<!-- formula-not-decoded -->

Note that

<!-- formula-not-decoded -->

| [ let ]   | ( ˆ C, ˆ ρ ) &#124; = ce δ ( let x = t ℓ 1 1 in t ℓ 2 2 ) ℓ iff ( ˆ C, ˆ ρ ) &#124; = ce δ t ℓ 1 1 ∧ ( ˆ C, ˆ ρ ) &#124; = ce ′ δ t ℓ 2 2 ∧ ˆ C ( ℓ 1 , δ ) ⊆ ˆ ρ ( x, δ ) ∧ ˆ C ( ℓ 2 , δ ) ⊆ ˆ C ( ℓ, δ ) where ce ′ = ce [ x ↦→ δ ]                                                                                                             |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ fn ]    | ( ˆ C, ˆ ρ ) &#124; = ce δ ( fn x ⇒ e 0 ) ℓ iff { ( fn x ⇒ e 0 , ce 0 ) } ⊆ ˆ C ( ℓ, δ ) where ce 0 = ce ↾ FV ( fn x ⇒ e 0 )                                                                                                                                                                                                                       |
| [ app ]   | ( ˆ C, ˆ ρ ) &#124; = ce δ ( t ℓ 1 1 t ℓ 2 2 ) ℓ iff ( ˆ C, ˆ ρ ) &#124; = ce δ t ℓ 1 1 ∧ ( ˆ C, ˆ ρ ) &#124; = ce δ t ℓ 2 2 ∧ ( ∀ ( fn x ⇒ t ℓ 0 0 , ce 0 ) ∈ ˆ C ( ℓ 1 , δ ) : ( ˆ C, ˆ ρ ) &#124; = ce ′ 0 δ 0 t ℓ 0 0 ∧ ˆ C ( ℓ 2 , δ ) ⊆ ˆ ρ ( x, δ ) ∧ ˆ C ( ℓ 0 , δ ) ⊆ ˆ C ( ℓ, δ )) where δ 0 = [ δ, ℓ ] k and ce ′ 0 = ce 0 [ x ↦→ δ 0 ] |

<!-- formula-not-decoded -->

where δ 0 = ϵ is the empty call string, ce 0 is the initial context environment (initially empty). The calling context changes at function applications, while the context environment changes when variables are bound.

For the outer binding we get:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then, for the two calls:

with k = 1 :

and therefore:

<!-- formula-not-decoded -->

we obtain two different call strings:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The first call gives:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where ce 1 = ce [ f ↦→ δ 1 ] .

The second call gives:

where ce 2 = ce [ f ↦→ δ 2 ] .

Hence:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So, under 1-CFA, the two calls to apply are analyzed in two different calling contexts:

<!-- formula-not-decoded -->

Hence the formal parameter f of apply is no longer represented by a single abstract variable:

<!-- formula-not-decoded -->

but by two context-dependent versions:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Therefore, in the body of apply:

<!-- formula-not-decoded -->

the occurrence f 1 is interpreted differently in the two contexts:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So the spurious flows disappear:

<!-- formula-not-decoded -->

ˆ C (15) contains only the result of inc ,

ˆ C (18) contains only the result of dbl .

In words: 0-CFA merges the two calls to apply; 1-CFA separates them by call site, so the first call propagates only inc to f , while the second propagates only dbl .

Consequently: