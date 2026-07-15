8

## Program Properties

We specify program properties by their extension , that is , the set of elements that have such a property , and more precisely , properties of the trace semantics of programs . We introduce the program collecting semantics as the strongest property of a program . We consider abstractions of the collecting semantics such as trace and reachability properties .

## Contents

|   8.1 | What is a Program Property ?                                               |
|-------|----------------------------------------------------------------------------|
|   8.2 | What is a Formal Property ?                                                |
|   8.3 | What is a Formal Semantic Property ?                                       |
|   8.4 | Collecting Semantics                                                       |
|   8.5 | What is a Formal Trace Property ?                                          |
|   8.6 | Abstraction of a Semantic Property into a Trace Property                   |
|   8.7 | Trace Property Semantics                                                   |
|   8.8 | Invariance / Reachability Property                                         |
|   8.9 | Abstraction of a Trace Property into an Invariance / Reachability Property |
|  8.10 | Invariance / Reachability Semantics                                        |
|  8.11 | Hierarchy of Program Properties                                            |
|  8.12 | Conclusion                                                                 |
|  8.13 | Solutions to Selected Exercises                                            |

## 8.1 What is a Program Property ?

By the term program property we could mean a property of the program text P , such as a ten-line program or a syntax error at line 12. In that case , we instead use the term of a program syntax property .

Here , however , by program property , we mean a program semantic property that is a property of its maximal fi nite or infinite trace semantics 𝒮 +∞ ⟦ P ⟧ ∈ 𝕋 + → ℘ ( 𝕋 +∞ ).

## 8.2 What is a Formal Property ?

When speaking of properties we have to say 'Properties of what ? ' This what is a given set ℰ of entities ( individuals , things , elements , objects , etc .) of interest . Logicians would say elements of a universe ( or universal set or universe of discourse 𝕌 ).

By formal property we mean the set of entities that have this property . So , if ℰ is a set of entities then the properties of these entities are sets belonging to ℘ ( ℰ ).

An entity has the formal property if and only if it belongs to the formal property , that is , to the set of entities which have this property . Formally , an entity e ∈ ℰ has property P ∈ ℘ ( ℰ ) if and only if e ∈ P , or equivalently , { e } ⊆ P where { e } is the strongest property of element e and ⊆ is implication .

A property P is stronger than a property P ʹ ( or P ʹ is weaker than P ) if and only if P implies P ʹ that is P ⊆ P ʹ. The strongest property is ∅ ( false ) and the weakest property is ℰ ( true ). The strongest property of an entity e ∈ ℰ is { e }, that is to be that entity ( and nothing else ).

Example 8.1 ( even / odd ) Take ℰ = ℤ . The properties of integers are elements of ℘ ( ℤ ). For example ,  ∅ is false ( no integer has the false property ). ℤ is true ( all integers have the true property ). 2 ℤ ≜ { z ∈ ℤ | ∃ k ∈ ℤ . z = 2 k } is the even property , and 2 ℤ +1 ≜ { z ∈ ℤ | ∃ k ∈ ℤ . z = 2 k + 1} is the odd property . An integer z is either odd z ∈ 2 ℤ or even z ∈ 2 ℤ + 1 ( i . e ., ℤ = 2 ℤ ∪ 2 ℤ +1 ).

The stronger a property P of entities is , the more information / knowledge we have about the entities that have this property . The abstraction of a property P into a weaker property P ʹ loses information about these entities in that there are more entities satisfying P ʹ than P . For example , abstracting 'even positive integers' into 'positive integers' loses the evenness information .

Remark 8.2 ( properties as sets ) Representing properties by sets , we do not have to consider a specific logic to describe these properties . Moreover , we avoid the confusion between a program variable x and the denotation of its value by the same name x ( unfortunately , also often denoted x ). So , 'the variable x has an even value' ( in environment ρ) is ρ( x ) ∈ 2 ℤ instead of the predicate ∃ k ∈ ℤ . x =  2 k ( in which x implicitly denotes ρ( x )). Of course , the sets representing properties of x can be defined by predicates p ( x ) ( such as x ∈ 2 ℤ or ∃ k ∈ ℤ . x = 2 k ) considered to be a shorthand for {ρ( x ) | p (ρ( x ))}.

Exercise 8.3  ( constancy ) What is the property that means 'to be an integer constant . '

Remark 8.4 ( on the interpretation of logics ) Consider a fi rst-order language with variables x ∈ 𝕍 , functions f to build terms t ::= x | f ( t 1 ,…, t n )  ( e . g ., the arithmetic expressions defined in section 3.4); and predicates p ( e . g .,, the Boolean expressions of section 3.4), logical connectives ⇒, ¬, and so forth , and quantifiers ∀ and ∃ to build logic formulas φ ::= p ( t 1 ,…, t m ) | φ 1 ⇒ φ 2 | ¬φ 1 | … | ∀ x . φ 1 | ∃ x . φ 1 .

Let ℰ be a universe of discourse and ℐ be an interpretation of the functions and predicates such that ℐ ( f ) ∈ ℰ n ℰ and ℐ ( p ) ∈ ℘ ( ℰ m ). Let ρ ∈ ≜ 𝕍 → ℰ be environments assigning values to variables . The semantics 𝒮 ⟦ φ ⟧ of a formula φ is defined structurally as 𝒮 ⟦ x ⟧ ρ ≜ ρ( x ), 𝒮 ⟦ f ( t 1 ,…, t n ) ⟧ ρ ≜ ℐ ( f )( 𝒮 ⟦ t 1 ⟧ ρ,…, 𝒮 ⟦ t n ⟧ ρ), 𝒮 ⟦ p ( t 1 ,…, t m ) ⟧ ≜ {ρ  | ⟨ 𝒮 ⟦ t 1 ⟧ ρ,…, 𝒮 ⟦ t n ⟧ ρ ⟩ ∈ ℐ ( p )}, 𝒮 ⟦ φ 1 ⇒ φ 2 ⟧ ≜ 𝒮 ⟦ φ 1 ⟧ ⊆ 𝒮 ⟦ φ 2 ⟧ ∅  , 𝒮 ⟦ ¬φ 1 ⟧ ≜ ∖ 𝒮 ⟦ φ 1 ⟧ , …, 𝒮 ⟦ ∀ x . φ 1 ⟧ ≜ {ρ | {ρ ⟦ x ← v ⟧ | v ∈ ℰ } ⊆ 𝒮 ⟦ φ 1 ⟧ ρ}, and 𝒮 ⟦ ∃ x . φ 1 ⟧ ≜ {ρ | {ρ ⟦ x ← v ⟧ | v ∈ ℰ }∩ 𝒮 ⟦ φ 1 ⟧ ρ ≠ ∅}.

Observe that 𝒮 ⟦ φ ⟧ ∈ ℘ ( ) is what we called a property of environments in . So instead of reasoning on formulas φ, we reason on their semantics 𝒮 ⟦ φ ⟧ .

Logicians would object that such reasonings are then dependent upon a particular interpretation ℐ . This is true because this interpretation ℐ is determined by the semantics of the programming language of chapters 3 and 6 so ℰ = ℤ in discussing expressions ( or ℰ = 𝕋 +∞ in discussing programs ).

For full generality , we could have left the expressions in section 3.4 uninterpreted with very few hypotheses on their possible interpretations ( such as 𝒜 ⟦ A ⟧ ∈ → ℰ and ℬ ⟦ B ⟧ ∈ ℘ ( )), as logicians do . However , with regards to verification as discussed in part VIII , most results depend on which specific interpretation is chosen . Nevertheless , we can still write φ to be understood as 𝒮 ⟦ φ ⟧ for this interpretation . However , it is more difficult in static analysis to abstract formulas φ rather than their semantics 𝒮 ⟦ φ ⟧ .

## 8.3 What is a Formal Semantic Property ?

In the case of a formal program property , the entity is 𝒮 +∞ ⟦ P ⟧ . 𝒮 +∞ ⟦ P ⟧ belongs to 𝕋 + → ℘ ( 𝕋 +∞ ), so a program property is an element of ℘ ( 𝕋 + → ℘ ( 𝕋 +∞ )). This is the traditional notion of property in abstract interpretation . Because a relation in ℘ ( 𝕋 + × 𝕋 +∞ ) is isomorphic to its right image in 𝕋 + → ℘ ( 𝕋 +∞ ), a program property can also be understood as an element of ℘ ( ℘ ( 𝕋 + × 𝕋 +∞ )). ℘ ( ℘ ( 𝕋 +∞ )). It was later called hyperproperty [194] but we stick to the original set theoretic definition of property in abstract interpretation . 1

Example 8.5 Assume that π 0 is a given initialization and that we are interested in the properties of 𝒮 +∞ ⟦ P ⟧ π 0 ∈ ℘ ( 𝕋 +∞ ). The formal program property 'all executions of P from π 0 always terminate with x = 0 or all executions of P from π 0 always terminate with x =  1 ' is the formally defined as P ≜ ℘ ({π ∈ 𝕋 + |  ρ(π) x =  0})  ∪ ℘ ({π ∈ 𝕋 + |  ρ(π) x =  1})  ∈ ℘ ( ℘ ( 𝕋 +∞ )).

<!-- image -->

Assume program P has this property so that 𝒮 +∞ ⟦ P ⟧ π 0 ∈ P . Executing program P from π 0 once , we know the result of all other executions possible from π 0 . If the execution terminates with x = 0 ( respectively x =  1) the property P implies that all other possible executions will always terminate with x = 0 ( respectively x = 1).

## 8.4 Collecting Semantics

By definition of properties in section 8.1, the strongest semantic property of program P is therefore { 𝒮 +∞ ⟦ P ⟧ }. It is traditionally called the static or collecting semantics of program P .

Therefore program P has property P ∈ ℘ ( 𝕋 + → ℘ ( 𝕋 +∞ )) is 𝒮 +∞ ⟦ P ⟧ ∈ P , or equivalently , { 𝒮 +∞ ⟦ P ⟧ } ⊆ P , that is , 𝒮 [ P ] ⊆ P meaning that P is implied by the collecting semantics of program P . This trivial remark allows us to use implication ⊆ ( ⇒) instead of membership ∈ . This is useful in static analysis in which ⊆ is generally easy to abstract but not ∈ .

## 8.5 What is a Formal Trace Property ?

A trace property is a property of the continuation traces for a given initialization trace hence an element of 𝕋 + → ℘ ( 𝕋 +∞ ). The program semantics is a trace property because 𝒮 +∞ ⟦ P ⟧ ∈ 𝕋 + → ℘ ( 𝕋 +∞ ). Isomorphically , a trace property is an element of ℘ ( 𝕋 + × 𝕋 +∞ ), inappropriately called property in [194] with the consequence of confusing program semantics and program properties .

Example 8.7 Continuing example 8.5, {π ∈ 𝕋 + | ρ(π) x = 0} ∈ ℘ ( 𝕋 +∞ ) is the trace property of 'terminating with x =0. ' Program component S terminates with a Boolean value for initialization π 0 is 𝒮 +∞ ⟦ S ⟧ π 0 ∈ {π ∈ 𝕋 + | ρ(π) x = 0}∪{π ∈ 𝕋 + | ρ(π) x = 1}. Contrary to example 8.5, knowing that one execution π of S from π 0 returns 0  (/1) does not guarantee that no other execution πʹ from π 0 returns 1  (/0). So the semantic property of example 8.5 is more expressive than a trace property .

Examples 8.5 and 8.7 show that trace properties are less expressive than semantic properties . This is made clear by showing that a trace property is an abstraction of a semantic property .

## 8.6 Abstraction of a Semantic Property into a Trace Property

Any semantic property P can be abstracted into a less precise trace property α 𝕋 ( P ) defined as follows

Exercise 8.9 Prove that ⟨ ℘ ( 𝕋 + → ℘ ( 𝕋 +∞ )), , and , more generally , ⟨ ℘ ( S → ℘ ( S ʹ)), , ⟩ What is for any sets S and S ʹ.

Example 8.10 Continuing example 8.5, let P ≜ ℘ ({π ∈ 𝕋 + |  ρ(π) x = 0}) ∪ ℘ ({π ∈ 𝕋 + | ρ(π) x = 1}) ∈ ℘ ( ℘ ( 𝕋 +∞ )). We have = α 𝕋 ( P ) = {π ∈ 𝕋 + |   ρ ( π) x ∈ {0,1}}.

<!-- image -->

Hence P and both express that program executions always terminate with a Boolean value for x . However , P is stronger because it expresses that the result is always the same , whereas doesn't . No abstract trace property in 𝕋 + → ℘ ( 𝕋 +∞ ) can express this ( unless the result is constant ).

Exercise 8.11 Assume that program P has property P = {{ ⟨ π 0 , π 1 ⟩ }, { ⟨ π 0 , π 2 ⟩ }}. What is α 𝕋 ( P )?, γ 𝕋 (α 𝕋 ( P ))? Why is this an information loss ?

## 8.7 Trace Property Semantics

The trace property semantics of a program is the strongest trace property of the trace semantics of that program , that is , the trace semantics itself .

## 8.8 Invariance / Reachability Property

An invariance or reachability property is a relational between values of variables attached to each program point that does hold whenever execution reaches that program point .

Example 8.13 An invariant for the program (4.1) is the following ( x denotes the value of variable x . The local invariant attached to a program point is given as a comment / * … * / at that program point . For iteration and conditional statements the local invariant holds at that statement , just before the test . We assume all variables are initialized to 0.)

Formally , the strongest invariant ℐ is

## 8.11

An invariant is a property of the program variables that remains unchanged under a program step computation . Methods for proving that a property is invariant were introduced by A . M . Turing [933], P . Naur [742], R . W . Floyd [376], and C . A . R . Hoare [501, 504]. They are developed by abstract interpretation in part VIII , 'Specification and Verification . '

## 8.9 Abstraction of a Trace Property into an Invariance / Reachability Property

The trace to invariance / reachability property abstraction α 𝕀 abstracts a trace semantics 𝒮 to an invariant collecting at each program point on the trace the possible values of the variables at that point for executions satisfying a precondition P .

Exercise 8.14 Prove that α 𝕀 is the lower adjoint of a Galois connection .

## Invariance Reachability Semantics

## 8.10 /

The invariance / reachability semantics of a program P is the trace to invariant abstraction of its trace semantics . This is the strongest invariant in that it implies all other invariants . In example 8.13, I is the invariance semantics of program (4.1).

## Hierarchy of Program Properties

The abstraction of program properties into less expressive ones , as formalized by Galois connections , gives raise to a hierarchy of program properties . This induces a corresponding hierarchy of program semantics .

<!-- image -->

The idea that the specification of the properties of programs defines their semantics goes back to Robert Floyd 'Assigning meaning to programs' [376]. The organization of various semantics in a hierarchy appeared in [49, 505] and in [227] as part of the lattice of abstract domains [241, section 8].

## 8.12 Conclusion

We have defined properties ( of programs ) as sets ( of semantics ), which is not unusual in mathematics ( e . g ., [880, ch . 2, § 1]). We have defined a hierarchy of more or less expressive semantic program properties related by abstractions . In verifying a program semantic property , it is important to do so at an appropriate level of abstraction , that is , precise enough to verify the semantic property and abstract enough not to consider irrelevant details of the semantics . This is the objective of , for example , the design of program proof methods given in chapters 25 and 26. Properties as sets is also a fruitful point of view in static analysis , in which sets are easier to abstract than logical formulas ( see , for example , chapters 21 and 27).

## 8.13 Solutions to Selected Exercises

Solution to exercise 8.3     {{ n } | n ∈ ℤ }.

Solution to exercise 8.9

Solution to exercise 8.11    α 𝕋 ( P ) = { ⟨ π 0 , π 1 ⟩ , ⟨ π 0 , π 2 ⟩ }, γ 𝕋 (α 𝕋 ( P )) = {∅, { ⟨ π 0 ,  π 1 ⟩ },  { ⟨ π 0 ,  π 2 ⟩ },  { ⟨ π 0 ,  π 1 ⟩ , ⟨ π 0 ,  π 2 ⟩ }}. The information that the program P has one and only one execution ( either π 1 or π 2 ) from π 0 is lost .

## Solution to exercise 8.15 Let be the pointwise inclusion ⊆. We have

1. Hence a property of a semantic property is a property in ℘ ( ℘ ( 𝕋 + → ℘ ( 𝕋 +∞ ))), not a hyperhyperproperty .

## 9

## Undecidability and Rice Theorem

The problem of proving the termination of a program or , more generally , of verifying its correctness is shown to be undecidable . This means that it is impossible to construct always-terminating algorithms to solve these problems correctly .

## Contents

- 9.1 Decidability , Semidecidability , and Undecidability
- 9.2 Turing Completeness
- 9.3 Undecidability of the Termination Problem
- 9.4 Examples of Algorithmically Undecidable Problems
- 9.5 Semidecidability
- 9.6 Rice's Theorem
- 9.7 Conclusion
- 9.8 Solutions to Selected Exercises

## 9.1 Decidability , Semidecidability , and Undecidability

A question ( for instance , on the semantics of a program ) with Boolean answer is

- Decidable if and only if there exists an algorithm that takes the program as input and effectively computes the answer to the question in fi nite time ;

- Semidecidable if and only if there exists an algorithm that takes the program as input and effectively computes the answer to the question in fi nite time when the answer is true and may be not terminating when it is false ;
- Undecidable if and only if there exists no algorithm that takes the program as input and effectively computes the answer to the question in fi nite time ( any algorithm providing correct answers will therefore answer true , false , I don't know , or will not terminate ).

Turing's theorem 9.1 states that the halting / termination problem is algorithmically undecidable . Rice's theorem 9.12 states that the problem of whether a program has a given nontrivial semantic property is algorithmically undecidable . Our proofs are informal sketches in the style of Neil Jones [537] and Bernhard Reus [825]; see [841, 902] for rigorous proofs .

## 9.2 Turing Completeness

A programming language is Turing complete if and only if it is possible to write an interpreter for this language in this language . For example , a language without iteration or recursion is not Turing complete since it cannot read arbitrarily long programs .

A programming language is deterministic if any input ( i . e ., given initial values of variables ) has a unique outcome ( including the possibility of nontermination ). The language of chapters 4 and 7 is deterministic .

The language of chapters 4 and 7 is Turing complete ( because the initial values of variables are not sequences of characters but integers , an interpreter written in this language would have to encode programs as naturals , for example , the natural obtained by concatenating the fixed-size character codes of the sequence of characters constituting the program ).

## 9.3 Undecidability of the Termination Problem

The halting / termination problem is to write a program termination that takes as input an arbitrary program P ( represented as a string or fi le or an integer encoding ) and its input data D ( also represented as a string or file or an integer encoding ) such that termination(P,D) always terminates for all programs P and input data D and returns tt if the execution of the program P on the data D does terminate and ff if the execution of the program P on the data D does not terminate .

The halting / termination problem is undecidable because no such algorithm does exist . The proof of the halting / termination problem undecidability is credited to Alan Turing [931, 932]. Similar arguments had been used to prove undecidability of other problems ( e . g .,, in number theory by Alonzo Church [184] or the incompleteness theorems in logic by Kurt Gödel [420]), but the originality of Turing is that his theorem explicitly refers to the halting problem of a ( Turing ) machine modeling computers .

Theorem 9.1 ( Turing's theorem ) The halting / termination problem is undecidable for a deterministic Turing complete language .

Proof Sketch The proof that such a program termination cannot exist is by reductio ad absurdum . Let interpret be an interpreter for the language such that interpret(P,D) is the result of running the program P on the input data D .

Assume termination does exist . Define the deterministic program contradiction ≜

function P =  if  (termination(P,P))  {  while  (tt);  }

and run the program contradiction on its own text , that is , contradiction(contradiction).

More precisely , that is computed by running the interpreter interpret(contradiction,contradiction).

Then termination(contradiction, contradiction) is computed by running the interpreter

and always terminates

interpret(termination,  (contradiction,contradiction)) .

- If contradiction(contradiction) does terminate then

termination(contradiction,  contradiction)

terminates and returns true , which is a contradiction because the iteration while  (tt); does not terminate or

- contradiction(contradiction) does not terminate and then

termination(contradiction,  contradiction)

terminates and returns false , which is a contradiction because the iteration while  (tt); is not entered and the program terminates .

A more rigorous proof must precisely define what is a program and what is the execution of this program , for which Alonzo Church introduced the lambda calculus and Alan Turing introduced the notion of Turing machine . Equivalently , we can formally define the semantics of programs , which is the objective of chapter 7, 'Maximal Trace Semantics . '

## 9.4 Examples of Algorithmically Undecidable Problems

Other decision problems for programs can be proved undecidable by reduction to the halting / termination problem .

Example 9.2  ( constancy ) Constancy analysis ( see exercise 3.45) is the problem of deciding whether a program P assigns a value different from the initial value 0 to a variable x . It is undecidable because otherwise , given a program P , consider a fresh variable x not in P and the witness program P ʹ  = P ; x = 1 ;. P ʹ assigns a value different from the initial value 0 to the variable x if and only if P terminates . Hence if the constancy problem were decidable , termination would also be decidable , in contradiction to Turing's theorem 9.1.

Exercise 9.3 ( absence of runtime error ) Prove that the problem of proving the absence of runtime error in an execution of a program P is undecidable .

Exercise 9.4  ( sign ) Prove that the problem of deciding whether a numerical variable has a given sign is undecidable .

Exercise 9.5  ( type ) Prove that the problem of deciding whether a variable has a given type is undecidable ( it follows that the more difficult typing problem of inferring the type of a variable is also undecidable ).

Corollary 9.6 ( failures of algorithms 'solving' undecidable problems ) Let A(P, d) be an algorithm to solve an undecidable problem on program P for input data d . Assume that the algorithm is sound ( otherwise , giving wrong answers is easy ). Soundness means that A(P,d) correctly answers true , false , or fails , that is , answers I don't know or does not terminate .

Then A(P,d) must fail on infinitely many input data d .

Proof By reductio ad absurdum , assume that A(P,d) fails on fi nitely many input data d i , i ∈  Δ only . Then ask mathematicians to solve these finitely many problems and provide an Answer(P,d i ) ∈ { true , false }. Formally check the correctness of their answers for each of d i , i ∈ Δ, with a proof assistant or theorem prover .

Consider the witness program :

A'(P,d) always terminates and never fails to solve the undecidable problem , in contradiction to Turing's theorem 9.1.

An example was given in remark 3.43.

## 9.5 Semidecidability

A problem with Boolean answer is semidecidable if and only if there exists an algorithm that terminate with true when the answer is true and might not terminate when the answer is false .

Example 9.7 ( termination ) The termination problem is semidecidable . Simply run the program and answer true upon termination . If the program does not terminate then there is no answer that is allowed by semidecidability .

Theorem 9.8 ( Emil L . Post , [805]) Decidable ( P ) ⇔ ( semidecidable ( P ) and Semidecidable ( not P )).

Proof For (⇒), we have either Decidable ( P )  ⇒ Semidecidable ( P ), or not Decidable ( P ) ⇒ Decidable ( not P ) ⇒ Semidecidable ( not P ). For (⇐), alternatively execute one step of the algorithms for Semidecidable ( P ) and Semidecidable ( not P ) and stop when one has an answer

Theorem 9.9 ( nontermination is undecidable ) The nontermination question : 'Will execution of program P on data d never terminate ? ' is not semidecidable ( hence not decidable ) for a deterministic Turing complete language .

Proof Sketch By reductio ad absurdum , Semidecidable ( Termination ) and Semidecidable ( not Termination ) would imply that Decidable ( Termination ).

## 9.6 Rice's Theorem

As shown by example 9.2 and exercises 9.3,  9.4, and 9.5 the proof that a specific program semantic property is undecidable is always by the same reduction to the nontermination problem that was proved to be undecidable in section 9.3. Rice's theorem [830] is a generalization from these particular semantics properties to all nontrivial semantic properties : Rice's theorem states that all nontrivial semantic properties of programs are undecidable .

## 9.6.1 Semantics

The functional semantics 𝒮 pf ⟦ S ⟧ of program components S ∈ ( as defined in chapter 4) considered in Rice's theorem is an integer partial function 𝒮 pf ⟦ S ⟧ ∈ ℕ ℕ . 1

This is an abstraction 𝒮 pf ⟦ S ⟧≜ α pf ( 𝒮 +∞ ⟦ S ⟧ ) of the maximal trace semantics 𝒮 +∞ ⟦ S ⟧ ∈ 𝕋 + → 𝕋 +∞ ( as defined in definition (7.7) of chapter 7 and later refined in section 17.2).

Assume that the set of states is enumerable so that , by definition , there exists a bijective encoding ι ∈ ℕ of states to naturals .

The abstraction of 𝒮 ∈ 𝕋 + → 𝕋 +∞ is α pf ( 𝒮 ) n ≜ m if and only if for any finite initialization trace πσ ending in an initial state σ for which encoding is ι(σ)  = n , the execution is continued by a fi nite maximal trace σπʹσʹ ending in a fi nal state σʹ for which encoding ι(σʹ) is m . Otherwise , if a different fi nal state σʹʹ is reachable from a different initialization trace πʹσ or πσ is continued by a infinite maximal trace in 𝕋 ∞ then α pf ( 𝒮 ) n is undefined .

Formally , α pf ( 𝒮 ) n = m if and only if ∀πσ ∈ 𝕋 + . ∀σπʹ ∈ 𝒮 (πσ).(ι(σ) = n ) ⇒ (∃σπʹ σʹ ∈ 𝕋 + .σπʹ = σπʹ σʹ ∧ ι(σʹ) = m ).

## 9.6.2 Program Properties

In conformity with chapter 8, a program property is the set of all programs that have this property . Therefore , program properties belong to ℘ ( ). The trivial properties are either the empty set ∅ of programs or the set of all programs .

## 9.6.3 Semantic Program Properties

A program property P ∈ ℘ ( ) is a semantic property if and only if S ∈ P ⇔ 𝒮 pf ⟦ S ⟧ ∈  γ 𝒮 pf ( P ) where the semantic meaning γ 𝒮 pf ( P ) of a property P ∈ ℘ ( ) is γ 𝒮 pf ( P ) ≜ { 𝒮 pf ⟦ S ʹ ⟧ | S ʹ ∈ P } ∈ ℘ ( ℕ ℕ ).

Only the ⇐ direction is not trivial . For example , 'S has 42 minus operations -' is not a functional semantic property because given a statement S having 42 minus operations -, we can certainly find another program with a different number of minus operations -but with the same functional semantics .

## 9.6.4 Extensional Program Properties

Rice's theorem considers only program properties P ∈ ℘ ( S ) that are

extensional .

A property P ∈ ℘ ( ) is extensional if and only if ∀ S 1 , S 2 ∈ . 𝒮 pf ⟦ S 1 ⟧ = 𝒮 pf ⟦ S 2 ⟧ ⇒ ( S 1 ∈ P ⇔ S 2 ∈ P ).

## 9.6.5 Extensional and Functional Semantic Program Properties are Equivalent

The extensional properties are exactly the functional semantics properties :

Lemma 9.10 A property P ∈ ℘ ( S ) is extensional if and only if P is a semantic property .

Proof (⇒) Assume that property P ∈ ℘ ( S ) is extensional .

If 𝒮 pf ⟦ S ⟧ ∈ γ 𝒮 pf ( P ) = { 𝒮 pf ⟦ S ʹ ⟧ | S ʹ ∈ P } then there exists S ʹ ∈ P such that 𝒮 pf ⟦ S ⟧ = 𝒮 pf ⟦ S ʹ ⟧ and so , by extensionality , S ∈ P .

Conversely , if S ∈ P then 𝒮 pf ⟦ S ⟧ ∈ { 𝒮 pf ⟦ S ʹ ⟧ | S ʹ ∈ P } ≜ γ 𝒮 pf ( P ).

We conclude that S ∈ P ⇔ 𝒮 pf ⟦ S ⟧ ∈ γ 𝒮 pf ( P ) so that , by definition , P is a functional semantic property .

( ⇐ ) Assume that P is a functional semantic property that is ∀ S ∈ . 𝒮 pf ⟦ S ⟧ ∈ γ 𝒮 pf ( P )  ⇔ S ∈ P . Let S 1 , S 2 ∈ such that 𝒮 pf ⟦ S 1 ⟧ = 𝒮 pf ⟦ S 2 ⟧ . Then ( S 1 ∈ P ⇔ S 2 ∈ P ) is equivalent to ( 𝒮 pf ⟦ S 1 ⟧ ∈ γ 𝒮 pf ( P ) ⇔ 𝒮 pf ⟦ S 2 ⟧ ∈ γ 𝒮 pf ( P ) which is true because 𝒮 pf ⟦ S 1 ⟧ = 𝒮 pf ⟦ S 2 ⟧ . It follows that P is extensional .

Lemma 9.11 The termination and nontermination properties are nontrivial and extensional .

Proof Expressed with 𝒮 +∞ ⟦ S ⟧ , termination is 𝒮 +∞ ⟦ S ⟧ πσ  ∈ 𝕋 + . For deterministic programs this is equivalent to 𝒮 pf ⟦ S ⟧ n ∈ ℕ where n =

ι(σ). This is the semantic property { f ∈ ℕ ℕ | n ∈ dom ( f )}, which by lemma 9.10 is extensional .

Similarly for nontermination , we consider 𝒮 +∞ ⟦ S ⟧ πσ ∈ 𝕋 ∞ abstracted in { f ∈ ℕ ℕ | ι(σ) dom ( f )}.

There are programs that terminates on given data and others that don't so the termination and nontermination properties are nontrivial .

## 9.6.6 Undecidability of Semantic Property Verification

Theorem 9.12 ( Rice's theorem ) Let P be a nontrivial and extensional / functional semantics property of a program S in a deterministic Turing complete language . Then the Boolean question S ∈ P ? is undecidable .

In short , an extensional / functional semantic property P is decidable if and only if it is trivial .

Proof Sketch of 9.12 We let i S be the variable in which statement S finds its input data ν and let r S be the variable in which statement S writes its final result ξ in the case of termination . The functional semantics of statement S is therefore ν dom ( 𝒮 pf ⟦ S ⟧ ) if S does not terminate and 𝒮 pf ⟦ S ⟧ ν = ξ in the case of termination .

To define this abstraction more formally , let be the initialization trace such that 𝝔 (π 0 ) i S = ν ( the existence of A ν such that ∀ρ. 𝒜 [ A ν ]ρ = ν is proved in exercise 3.8). Let π = 𝒮 +∞ ⟦ S ⟧ π 0 be the trace continuing π 0 when executing S so that the execution is π 0 π. If π 0 π ∈ 𝕋 ∞ then 𝒮 pf ⟦ S ⟧ is undefined for ν i . e . ν dom ( 𝒮 pf ⟦ S ⟧ ). Otherwise π 0 π ∈ 𝕋 + and 𝒮 pf ⟦ S ⟧ ν = 𝝔 (π 0 π) r S .

We want to determine whether statement S terminates for the value ν of its input variable i S . Formally , the termination question is 𝒮 +∞ ⟦ S ⟧ π 0 ∈ 𝕋 + ? By the preceding definition of the abstraction of the maximal trace into functional semantics , this question is equivalent to ν ∈ dom ( 𝒮 pf ⟦ S ⟧ )?

The proof is by reduction ad absurdum , assuming that ∀ S ∈ . S ∈ P ? is decidable . Under this hypothesis , there would be an effective algorithm in P ( S ) returning tt if S ∈ P and false otherwise .

Because P is not trivial , there are programs S t ∈ P and S f P . Moreover S d ≜ while ( tt ); never terminates on any input x S d and so dom ( 𝒮 pf [ S d ]) = ∅.

Consider the witness program ( the value of expression A ν is ν)

The termination program is

This program always terminates by hypothesis that P is decided by in P which therefore always terminates .

It remains to prove that termination is correct . There are two cases .

- Assume that the divergent program S d ∈ P has property P so in P ( S d ) = tt . In that fi rst case , S w behaves as i S = A ν ; S i S f = i S w ; S f r S w = r S f ;. There are two subcases .
- ν dom ( 𝒮 pf ⟦ S ⟧ ) if and only if S does not terminate on input ν.

In that case S w does not terminate on any input ( in i S w which is not used ). Therefore S w behaves as S d ∈ P i . e . 𝒮 pf [ S w ]  = 𝒮 pf [ S d ] and S d ∈ P so S w ∈ P by extensionality .

- ν ∈ dom ( 𝒮 pf ⟦ S ⟧ ) if and only if S does terminate on input ν.

In that case S w behaves as S f P i . e . 𝒮 pf [ S w ] = 𝒮 pf [ S f ] so that S w P by extensionality .

In this fi rst case S d ∈ P , S terminates on input ν if and only if S w P , so termination ( S ,ν) = ¬ in P ( S w ) is correct .

- Otherwise , the divergent program S d P does not have property P . In that second case S w behaves as i S = A ν ; S i S t = i S w ; S t r S w = r S t ;. Again , there are two subcases .

- ν dom ( 𝒮 pf ⟦ S ⟧ ) if and only if S does not terminate on input ν.

In that case S w does not terminate on any input ( in i S w which is not used ). Therefore S w behaves as S d for all its inputs i . e . 𝒮 pf [ S w ] = 𝒮 pf [ S d ]. ThenS d P so S w P by extensionality .

- ν ∈ dom ( 𝒮 pf ⟦ S ⟧ ) if and only if S does terminate on input ν.

In that case S w behaves as S t for all its inputs i . e . 𝒮 pf [ S w ] = 𝒮 pf [ S t ]. ThenS t ∈ P implies S w ∈ P by extensionality .

In this second case S d P , S terminates on input ν if and only if S w ∈ P , so termination ( S ,ν) = in P ( S w ) is correct .

We have shown that termination ( S ,ν) solves the termination problem in contradiction to Turing's theorem 9.1.

The following exercise shows , using Rice's theorem , that precise static analysis is infeasible .

Exercise 9.13 Prove that there is no algorithm for examining a program P and determining infallibly whether P is an implementation of a partial function f , which takes an integer n and returns f ( n ) ( whenever f is well defined for n ).

Rice's theorem 9.12 remains valid when restricting the considered programs ( e . g .,, programs of a given complexity class [55]).

## 9.7 Conclusion

By Rice's theorem 9.12, checking that a program semantics has any nontrivial semantic property is undecidable . This means that when a sound algorithm automatically checks for a program's properties , the algorithm may not terminate ; or if it always terminates , then either there are restrictions on the considered programs ( such as finite states only , e . g .,, model checking ), a human interaction is necessary ( e . g .,, theorem proving ), or the result may be true , false , or undetermined , that is , I don't know . This is an indication that the verification and static program analysis problems are very difficult , even with approximate solutions [613], but not impossible , although without limit on the perfection of verification and static program analysis .

Rice's theorem 9.12 was extended to program verification and analysis by [277] to show that , from a computability perspective , and for infinite abstract properties , static program analysis is harder than checking / verification . Another extension in [74] is to abstract semantics more general than the extensional / functional semantics property of Rice's theorem 9.12.

## 9.8 Solutions to Selected Exercises

Solution to exercise 9.3 By reductio ad absurdum , let P be a program and X be a variable not in P . Define P'

$$var  X  :  int  =  0;$$

P;

X  :  =  1  /  X;

P terminates if and only if P' has a runtime error ( division by 0, because P does not use or modify X ). So if the absence of runtime error were decidable then termination would be decidable , which is a contradiction .

Solution to exercise 9.4 Sign analysis in section 3.2 is undecidable because otherwise , given a program P , consider a fresh variable x not in P and the derived program P ʹ  = P ; x = 1 ;. P ʹ assigns a strictly positive value to the variable x different from the initial value 0 of x if and only if P terminates . Therefore , if the sign problem were decidable , termination would also be decidable , which is a contradiction .

1. Denotational semantics is similar but encodes ν dom ( 𝒮 pf ⟦ S ⟧ by 𝒮 d ⟦ S ⟧ ν  =  ⊥ where ⊥ denotes nontermination . It also considers the case of parameters for which evaluation may not terminate so 𝒮 d ⟦ S ⟧ ∈ ℕ ∪{⊥} ℕ ∪{⊥}. Lazy evaluation of parameters allows 𝒮 d ⟦ S ⟧ ⊥ ≠ ⊥

## Posets , Lattices , and Complete

## 10 Lattices

Partial order theory emerged from the work of George Boole , Ernst Schröder , Charles Peirce , and it was mainly developed by Garrett Birkhoff [120]. Partial order theory is an abstraction of set theory in which ∈ is expressed in terms of ⊆ and ⊆ ( e . g ., property implication ) is abstracted as a partial order ⊑ ( e . g ., abstract property implication ). The abstract partial order ⊑ retains the essential properties of inclusion ( reflexive , antisymmetric , and transitive ). Many theorems of set theory remain valid , but not all , and this widely broadens the scope of applicability of order theory ( see introductions in [121,  295, 445]). The poset representation ⟨ℙ , ⊑⟩ of program properties ℙ with an abstract implication ⊑ provides a unified theory of program properties and their abstraction while giving us much more freedom and diversity in the choice of the possible encodings of abstract properties .

## Contents

- 10.1 Posets
- 10.2 Hasse Diagrams
- 10.3 Least Upper Bound ( lub ), Greatest Lower Bound ( glb ), Minimum , Maximum , Infimum , and Supremum
- 10.4 Duality Principle
- 10.5 Lattices
- 10.6 Complete Lattices

- 10.7 Pointwise Extension
- 10.8 Chain
- 10.9 CPO
- 10.10 Conclusion
- 10.11 Solutions to Selected Exercises

## 10.1 Posets

A poset ⟨ℙ , ⊑⟩ is a set ℙ equipped with a partial order ⊑ that is

Reflexive

: ∀ x ∈ ℙ . x ⊑ x ;

Antisymmetric

: ∀ x , y ∈ ℙ . (( x ⊑ y ) ∧ ( y ⊑ x )) ⇒ ( x = y ) and

Transitive

$$: ∀ x , y , z ∈ ℙ . (( x ⊑ y ) ∧ ( y ⊑ z )) ⇒ ( x ⊑ z ).$$

Two elements x and y are comparable when either x ⊑ y or y ⊑ x and incomparable when neither x ⊑ y nor y ⊑ x . A partial order ⊑ is total whenever any two elements are comparable .

$$Total : ∀ x , y ∈ ℙ . ( x ⊑ y ) ∨ ( y ⊑ x ).$$

A strict partial order ⊏ is irreflexive ( ∀ x ∈ ℙ . x / ⊏ x ) and transitive . If ⊑ is a partial order then x ⊏ y ≜ x ⊑ y ∧ x ≠ y is strict . If ⊏ is a strict partial order then x ⊑ y ≜ x ⊏ y ∨ x = y is a partial order .

A preorder ⪯ is reflexive and transitive . Then x ≡ y ≜ x ⪯ y ∧ y ⪯ x is an equivalence relation ( reflexive , symmetric (∀ x , y ∈ ℙ . x ≡ y ⇒ y ≡ x ), and transitive ). The equivalence class of x ∈ ℙ for the equivalence relation ≡ is [ x ] ≡ ≜ { y ∈ ℙ | x ≡ y }. The quotient of ℙ by ≡ is ℙ | ≡ ≜ {[ x ] ≡ | x ∈ ℙ }. The extension of the preorder ⪯ to the quotient ℙ | ≡ is [ x ] ≡ ⪯ ≡ [ y ] ≡ ⇔∃ x ʹ ∈ [ x ] ≡ , y ʹ ∈ [ y ] ≡ . x ʹ ⪯ y ʹ. If ⪯ is a preorder on ℙ then ⪯ ≡ is a partial order on ℙ | ≡ .

Exercise 10.1 Prove that the equality = on a nonempty set is the only nonempty relation that is both a partial order and an equivalence relation .

## [10.2 Hasse Diagrams](https://en.wikipedia.org/wiki/Hasse_diagram)

Finite posets ⟨ℙ , ⊑⟩ can be represented by a Hasse diagram , which is a set of points { p x | x ∈ ℙ } in the plane , different two by two , and such that

- if x ⊏ y then p x is strictly below p y and
- p x and p y are linked by a segment when x ⋖ y ( y covers x ) where x ⋖ y ≜ x ⊏ y ∧ ∄ z ∈ ℙ . x ⊏ z ∧ z ⊏ y .

⊑ is derived from ⋖ by reflexivity and transitivity . Two unlinked elements are incomparable . Examples are given in section 3.12,

exercise 3.45, and section 8.11.

## 10.3 Least Upper Bound ( lub ), Greatest Lower Bound ( glb ), Minimum , Maximum , Infimum , and Supremum

Let ⟨ℙ , ⊑⟩ be a poset and S ∈ ℘ ( ℙ ) be a subset . This subset S has

An upper bound u : if and only if u ∈ ℙ and ∀ x ∈ S . x ⊑ u ;

A least upper bound ( lub / join ) ⊔ S : if and only if ⊔ S is an upper bound of S smaller that other upper bound of S ( i . e ., ⊔ S ∈ ℙ and ∀ x ∈ S . x ⊑⊔ S and ∀ u ∈ ℙ .  (∀ x ∈ S . x ⊑ u )  ⇒ ( ⊔ S ⊑ u )). ⊔ { x , y } is

denoted with the infix notation x ⊔ y ;

A maximum M : if and only if M = ⊔ S ∈ S ;

A supremum ⊤ : if and only if

⊤ = ⊔ℙ ∈ ℙ .

## 10.4

## Duality Principle

The order dual of an order-theoretic definition or statement is obtained by replacing ⊑ by its inverse ⊒ , upper by lower , least by greatest , ⊔ by ⊓ , ⊓ by ⊔ , join by meet , meet by join , maximum by minimum , and so forth .

The duality principle states that if a definition or statement is valid for all partially ordered sets then the dual definition or dual statement is also valid for all partially ordered sets [121].

Example 10.2 Let be increasing that is , ∀ x , y ∈ A . ( x ≤ y ) ⇒ ( f ( x ) ⊑ f ( y )). The dual of ' f is increasing' is ' f is increasing . ' Note that if duality is applied to ⟨ A ,  ≤ ⟩ or ⟨ B , ⊑⟩ only , then the semidual of ' f is increasing' would be ' f is decreasing , ' that is , ∀ x , y ∈ A . ( x ≤ y ) ⇒ ( f ( x ) ⊒ f ( y )).

## 10.5 Lattices

Lattices are posets with the following properties .

Join semilattice : ∀ x , y ∈ ℙ . x ⊔ y exists in ℙ ( hence any nonempty finite subset of ℙ has a lub );

Meet semilattice : ∀ x , y ∈ ℙ . x ⊓ y exists in ℙ ( hence any nonempty finite subset of ℙ has a glb );

Lattice : ∀ x , y ∈ ℙ . x ⊔ y and x ⊓ y exist in ℙ ( hence any nonempty finite subset of ℙ has a lub / join and a glb / meet ).

## Example 10.3

Exercise 10.4 Consider the following diagram · a · b . Is it the Hasse diagram of a poset ?

<!-- image -->

Lattices have unique joins / meets of two-elements hence , by associativity of the union of finite sets . lattices have unique joins / meets of fi nite subsets . For example , ⟨ℕ , ≤ ⟩ is a lattice where the glb / meet is min and the lub / join is max taken on nonempty finite subsets of ℕ .

Exercise 10.5 Show that the lub ⊔ and glb ⊓ of a lattice ⟨ℙ , ⊑⟩ have the following properties :

|    |
|----|

Conversely , show that a set equipped with binary operations ⊔ and ⊓ satisfying these properties is a lattice by defining x ⊑ y ≜ x ⊓ y = x ( or equivalently , x ⊔ y = y ).

Let S be a subset of a lattice ⟨ L , ⊑ , ⊔ , ⊓⟩ . If ∀ x , y ∈ S . x ⊔ y ∈ S ∧ x ⊓ y ∈ S , then ⟨ S , ⊑ , ⊔ , ⊓⟩ is a sublattice of L . It is also a lattice .

Exercise 10.6 Show that a subset S of a lattice ⟨ L , ⊑ , ⊔ , ⊓⟩ may be a lattice ⟨ S , ⊑⟩ although not a sublattice of L .

## 10.6 Complete Lattices

A complete lattice is a poset ⟨ℙ , ⊑⟩ in which any subset S ∈ ℘ ( ℙ ) has a lub / join ⊔ S ( not only the fi nite ones ). Therefore a complete lattice has a supremum ⊤ = ⊔ℙ and an infinum ⊥ = ⊔ ∅. ( Any element x of ℙ is an upper bound of ∅ since ∀ y ∈ ∅ . y ⊑ x . Hence the lub of ∅ is the least element of ℙ .)

For example , ⟨ℕ , ≤ ⟩ is not a complete lattice because ℕ has no lub . ⟨ℕ ∪{∞},  ≤ ⟩ where ∀ n ∈ ℕ . n &lt;  ∞  ≤  ∞ is a complete lattice with supremum ∞ and infimum 0. The powerset of a set S is a complete lattice ⟨ ℘ ( S ), ⊆, ∅, S , ∪, ∩ ⟩ .

Exercise 10.7 Prove that a complete lattice ⟨ℙ , ⊑ , ⊥, ⊤ , ⊔⟩ has a glb ⊓ for arbitrary subsets .

Exercise 10.8 Prove that in a complete lattice ⟨ℙ , ⊑ , ⊥, ⊤ , ⊔⟩ , if X , Y ∈ ℘ ( ℙ ) and X ⊆ Y then ⊔ X ⊑⊔ Y .

Exercise 10.9 Prove that a pair ⟨ P ,  ≤ ⟩ and ⟨ Q , ⊑⟩ of posets ( respectively semilattices , lattices , and complete lattices ) is a poset ⟨ P × Q , ≤× ⊑⟩ ( respectively semilattice , lattice , complete lattice ) for the componentwise ordering ⟨ x , y ⟩ ≤× ⊑ ⟨ x ʹ, y ʹ ⟩ if and only if x ≤ x ʹ∧ y ⊑ y ʹ. Generalize to Cartesian products .

## 10.7 Pointwise Extension

Let ⟨ℙ , ⊑⟩ be a poset and S be a set . The pointwise extension of ⊑ to S is ⟨ S → ℙ , ⟩ where f g if and only if ∀ x ∈ S . f ( x ) ⊑ g ( x ). The pointwise join is f g ≜ x ∈ [ S ] f ( x ) ⊔ g ( x ), the meet is f g ≜ x ∈ [ S ] f ( x ) ⊓ g ( x ), and so on . The pointwise extension of is denoted that of is , and so forth .

Exercise 10.10 Show that the pointwise extension of a poset ( respectively semilattice , lattice , complete lattice , etc .) is a poset ( respectively semilattice , lattice , complete lattice , etc .).

Exercise 10.11 Let ⟨ℙ , ⊑ ,  ⊥, ⊤ , ⊔ , ⊓⟩ be a complete lattice . Prove that the functions ℙ → ℙ , increasing functions , y ∈ ℙ .  ( x ⊑ y )  ⇒ f ( x ) ⊑ f ( y ))}, arbitrary join preserving functions .  ( ⊔ S ∈ ℙ )  ⇒ ( ⊔ f ( S )  ∈ ℙ ∧ f ( ⊔ S )  = ⊔ f ( S ))} where f ( S ) ≜ { f ( x ) | x ∈ S }, and dually arbitrary meet preserving functions are a complete lattice for the pointwise ordering f g ⇔∀ x ∈ ℙ . f ( x ) ⊑ g ( x ).

## 10.8 Chain

A chain C of a poset ⟨ℙ , ⊑⟩ is a subset of the poset ℙ such that any two elements of the chain are comparable , that is , C ⊆ ℙ ∧ ∀ x , y ∈ C . x ⊑ y ∨ y ⊑ x . A denumerable ascending / increasing chain is a sequence ⟨ x i , i ∈ ℕ⟩ such that x 0 ⊑ x 1 ⊑ … x n ⊑ x n +1 …, that is , ∀ i &lt; j ∈ ℕ . x i ⊑ x j ( so . A denumerable sequence ⟨ x i , i ∈ ℕ⟩ is ultimately stationary if and only if ∃ ∈ ℕ . ∀ i ≥ . x i = x . A poset ⟨ℙ , ⊑⟩ is Noetherian ( or satisfies the increasing chain condition ( also called ascending chain condition ( ACC ) 1 )) if and only if any increasing chain is ultimately stationary ( so that any strictly ascending chain is finite ). The descending chain condition ( DCC ) is dual .

Exercise 10.12 Is any nonempty chain a lattice ? Is it a complete lattice ?

Exercise 10.13 Show that any Noetherian lattice is a complete lattice .

## 10.9 CPO

A complete partial order ( CPO ) ( or countably chain-complete poset ) is a poset ⟨ℙ , ⊑ ,  ⊥, ⊔⟩ with infimum ⊥ such that any denumerable ascending chain ⟨ x i , i ∈ ℕ⟩ has a least upper bound ⊔ i ∈ ℕ x i ∈ ℙ . A dual CPO is defined dually .

Exercise 10.14    (fl at domain ) Let ℙ be a set . Let ⊥ ℙ . Define ⊥ ⊑ ⊥ ⊑ x ⊑ x for all x ∈ ℙ . Show that ⟨ℙ ∪{⊥}, ⊑⟩ is a CPO .

Exercise 10.15  ( prefix order ) Consider the prefix relation on traces ∀π,πʹ  ∈ 𝕋 +∞ .(π ⋖ πʹ) ≜ (∃πʹʹ  ∈ 𝕋 +∞ .π πʹʹ  = πʹ) where trace concatenation is π πʹ = π when π ∈ 𝕋 ∞ . For example , ∋ ⋖ a ⋖ aa ⋖ aaa ⋖ … ⋖ a n ⋖ …. Define the limit of increasing chains ⟨ π i , i ∈ ℕ⟩ . For example , { a n | n ∈ ℕ } = a ω . Prove that ⟨𝕋 +∞ ∪{ ∋ }, , ∋ , ⟩ is a CPO .

Exercise 10.16 Let X k , k ∈ ℕ by an infinite increasing chain in a CPO ⟨ L , ⊑ , ⊔⟩ . Let f ∈ ℕ → ℕ be a strictly increasing function on naturals . Prove that ⊔ k ∈ ℕ X k = ⊔ k ∈ ℕ X f ( k ) .

Exercise 10.17 Let f ∈ P → P be an extensive operator on a CPO ⟨ P , ⊑ , ⊥, ⊔⟩ , that is , ∀ x ∈ P . x ⊑ f ( x ). Prove that f may have a fi xpoint but ( contrary to the claim [295,  8.23 Fixpoint Theorem III ]) may not have a minimal one .

## 10.10 Conclusion

Abstract program properties can be represented by posets . Finite Boolean lattices appeared in dataflow analysis [27,  29]. Gary Kildall [572] ( and independently , Ben Wegbreit [967]) introduced the use of non-Boolean finite lattices in dataflow analysis . Gary Kildall [572] required the lattice to be distributive , which is not true of his main example : constant propagation . In many examples of dataflow analysis , lattices are used dually , the infimum is tt ( true ) and the supremum is ff(∅)  [472]. Hassan Aït-Kaci et al .  [15] provides an example of efficient implementation of fi nite lattices .

The use of complete lattices not satisfying the increasing chain condition ( every strictly increasing chain is fi nite ) in program static analysis was introduced in [234, 235].

## 10.11 Solutions to Selected Exercises

Solution to exercise 10.1 Let r ∈ ℘ ( S × S ) be a nonempty relation on a nonempty set S which is both a partial order and an equivalence relation . By reflexivity , ∀ x ∈ S . ⟨ x , x ⟩ ∈ r , proving that S ⊆ r . Assume by reductio ad absurdum that r ≠ S . Then ∃ ⟨ x , y ⟩ ∈ r . x ≠ y . By symmetry ⟨ y , x ⟩ ∈ r so by antisymmetry x = y , a contradiction .

Solution to exercise 10.4

Solution to exercise 10.6

Yes , the poset is ⟨ { a , b }, { ⟨ a , a ⟩ , ⟨ b , b ⟩ } ⟩ .

<!-- image -->

Solution to exercise 10.7 Let L = { x ∈ ℙ |  ∀ y ∈ S . x ⊑ y } be the set of lower bounds of S . ∀ y ∈ S . ∀ x ∈ L . x ⊑ y , i . e . y is an upper bound of L . So , by existence and definition of ⊔ L

- ⊔ L is an upper bound of L , that is , ∀ x ∈ L . x ⊑⊔ L
- it is the least one , so ∀ y ∈ S . ⊔ L ⊑ y

It follows that ⊔ L is

- a lower bound of S
- the greatest one ( since any lower bound x of S belongs to L so x ⊆ ⊔ L

Hence , by definition of a glb , ⊓ S = ⊔ L .

Solution to exercise 10.8 By definition of ⊆,  ∀ x ∈ X . x ∈ Y , so x ⊑⊔ Y by definition of the lub ⊔ . It follows that ⊔ Y is an upper bound of X , so ⊔ X ⊑⊔ Y , by definition of the lub ⊔ .

Solution to exercise 10.12 Any fi nite nonempty subset S of a chain has a lub ( max S ) and a glb ( min S ) so is a lattice . However it may not be a complete lattice , as shown by the chain of naturals ⟨ℕ ,  ≤ ⟩ with their natural order ≤ such that the subset ℕ has no lub .

Solution to exercise 10.15 Denote the limit of the -increasing denumerable chain ⟨ π i , i ∈ ℕ⟩ by πʹ = i ∈ ℕ π i . If ⟨ π i , i ∈ ℕ⟩ is ultimately stationary at rank n , then πʹ = π n . This includes the case of an infinite trace π n since then ∀ m &gt; n .π m = π n . Otherwise the chain is infinite such that ∀ n ∈ ℕ .  ∃ m &gt; n .π n ⋖ π m so all π i , i ∈ ℕ are fi nite . In that case , πʹ ∈ 𝕋 ∞ is such that ∀ n ∈ ℕ .  πʹ[0..|π i |-  1]  = π i where | π| is the length of the fi nite trace π.

Solution to exercise 10.16 We have { X f ( k ) | k ∈ ℕ }⊆{ X k | k ∈ ℕ } so ⊔ k ∈ ℕ X f ( k ) ⊑⊔ k ∈ ℕ X k . Assume the inequality is strict . Then there exists an ∈ ℕ such that ⊔ k ∈ ℕ X f ( k ) ⊏ X . However X ⊑ X f ( ) , a contradiction .

Solution to exercise 10.17 Consider the negative integers ordered naturally with infimum -∞. This is a CPO . Let f (-∞) = 0 and f ( n ) = n otherwise . f has infinitely many fi xpoints but no minimal one .

1. Voraussetzung des Teilerkettensatz [755, Satz I ], [756, Satz II ].

## 11

## Galois Connections and Abstraction

Galois connections ( or Galois adjunctions ) formalize the correspondence between concrete properties ( e . g ., sets of traces ) and abstract properties ( e . g ., sets of reachable states ) in case there is always a most precise abstract property overapproximating any concrete property .

## Contents

- 11.1 Definitions of Galois Connections
- 11.2 Galois Correspondences
- 11.3 Duality of Galois Connections
- 11.4 Order , Join , and Meet Preservation
- 11.5 Order Properties of Galois Connections
- 11.6 Galois Retraction
- 11.7 Closure Operators
- 11.8 Composition of Galois Connections
- 11.9 Galois Connection in a Complete Boolean Algebra
- 11.10 Complete Heyting Algebra
- 11.11 Sound Abstraction
- 11.12 Best Abstraction
- 11.13 Combinations of Galois Connections
- 11.14 Galois Connection , Logical Relation , Tensor Product , Soundness Relation
- 11.15 Hierarchy of Abstractions

- 11.16 Moore Families
- 11.17 Conclusion
- 11.18 Solutions to Selected Exercises

## 11.1 Definitions of Galois Connections

The Galois connection between powersets of section 3.19 generalizes to posets .

Definition 11.1  ( Galois connection ) Given posets ⟨𝒞 , ⊑⟩ ( the concrete domain ) and ⟨𝒜 , ≼⟩ ( the abstract domain ), the pair ⟨ α, γ ⟩ of functions α ∈ 𝒞 → 𝒜 ( the lower adjoint or abstraction ) and γ ∈ 𝒜 → 𝒞 ( the upper adjoint or concretization ) is a Galois connection ( GC ) if and only if

Such Galois connections , introduced by Jürgen Schmidt [861, § 8], are sometimes called increasing , because α is increasing ; see lemma 11.33 ( as opposed to Galois correspondences , discussed in section 11.2, also called decreasing Galois connections , which were introduced by Oystein Ore [762] after Evarist Galois [388] and Garrett Birkhoff's polarities [120] of exercise 11.11). Definition 11.1 also applies to preorders ( and most , but not all , properties considered below are preserved ).

The intuition is that the concrete properties in 𝒞 are approximated by abstract properties in 𝒜 . The concretization γ provides the concrete meaning / semantics / representation γ( )  ∈ 𝒞 of abstract properties ∈ 𝒜 . γ( ) is the least precise element of 𝒞 that can be overapproximated by . Therefore any element of 𝒞 , ⊑ -less than γ( ) can also be overapproximated by .

which we write An abstract property ∈ 𝒜 is a sound overapproximation of a concrete property P ∈ 𝒞 whenever P ⊑ γ( ). ⊑ is understood as implication , so P is a stronger property than γ( ). We choose α( P ) ∈ 𝒜 to be the abstraction of the concrete property P . The stronger is the abstract property , the more precise is the abstraction .

- The implication α( P ) ≼ ⇒ P ⊑ γ( ) holds when = α( P ) so P ⊑ γ(α( P )), meaning that α( P ) is a sound overapproximation of the concrete property P and
- The converse implication P ⊑ γ( ) ⇒ α( P ) ≼ means that for any sound overapproximation of the concrete property P ,  α( P ) is stronger , that is , more precise than .

It follows that α( P ) is the best ( most precise ) sound overapproximation of P in the abstract domain 𝒜 . Moreover γ is increasing and so preserves the abstract implication ≼ in the concrete . This implies that a proof in the abstract is valid in the concrete : if 1 ≼ 2 ≼ … ≼ n then γ( 1 ) ⊑ γ( 2 ) ⊑ … ⊑ γ( n ).

We say that the abstraction of a concrete property P is exact whenever γ(α( P ))  = P . This means that the abstraction α( P ) of the property P loses no information at all , perhaps merely changing the abstract encoding of the concrete property P . For example , the sign abstraction of the property {0}, ℕ , ℕ + , or ℤ mentioned in section 3.15 is exact whereas that of {0, 2} is not .

We write ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ when α is surjective ( see section 11.6, Galois retraction ), ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ when γ is surjective , and ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ for a bijection ( Galois isomorphism ).

Exercise 11.1 Given n ∈ ℤ , define α n ∈ ℤ → ℤ as α n ( x )  = x -n . Prove that this is a Galois isomorphism on ⟨ℤ , ≤ ⟩ .

Exercise 11.2 What is the Galois connection following from n ≤ ⌊ x ⌋ ⇔ n ≤ x ?

Exercise 11.3 ([722, 889]) Define x ÷ y = max { z | z × y ≤ x } to be the largest natural number that , when multiplied by y is at most x .

Obviously , ∀ x , z , y &gt; 0. z × y ≤ x ⇔ x ÷ y . Show that this is a Galois connection .

Exercise 11.4 Let 𝕂 be a fi eld , 𝕂 [ x 1 , …, x n ] be the ring of n variate polynomials , and I = ( f 1 , …, f s ) be an ideal defining a variety 𝒱 ( see [616]). Show that α( I ) = { x ∈ 𝕂 n |  ∀ f ∈ I . f ( x ) = 0} and γ( 𝒱 ) = { f ∈ 𝕂 [ x 1 , …, x n ] | ∀ x ∈ 𝒱 . f ( x ) = 0} defines a Galois connection between ⟨𝕂 [ x 1 , …, x n ], ⊆ ⟩ and ⟨𝕂 n , ⊆ ⟩ .

Exercise 11.5 ( exclusion abstraction ) Let C be a set with subset S ⊊ C . Define α S ∩ ( X ) = X ∩ S . Prove that .

Exercise 11.6 ( homomorphic / elementwise / right image abstraction ) Given f ∈ C → A , define ∀ X ∈ ℘( C ).α f ( X ) ≜ f ( X ) ≜ { f ( x ) | x ∈ X } and ∀ Y ∈ ℘( A ).γ f ( Y ) ≜ f -1 ( Y ) ≜ { x | f ( x ) ∈ Y }. Prove that . 1

Exercise 11.7 Continuing exercise 11.6, prove that ⟨ ℘( C ), is equivalent to the existence of μ ∈ A → ℘( C ) such that ∀ x ∈ C . ∀ y ∈ A . x ∈ μ( y ) ⇔ f ( x ) = y [292].

Exercise 11.8 ( join homomorphic / partitioning abstraction ) 2 Let C be a set , ⟨ A , ⊑ , ⊔⟩ be a complete lattice , and h ∈ C → A . Define α( X ) ≜⊔ { h ( x ) | x ∈ X }. Prove that α is the lower adjoint of a Galois connection . Which choice of A and h allows to recover exercise 11.6?

Exercise 11.9 ( inclusion checking ) Let S be a set , R ∈ ℘( S ) ∖ { S }, and α ⊆ ( X ) ≜ ( X ⊆ R ). Prove that ℘( S ), .

Exercise 11.10 ( cover abstraction ) Let C be a set and A ∈ ℘(℘( C )) be a cover of C that is C = ⋃ A . For all X ∈ C define α( X ) ≜ { Y ∈ A | X ∩ Y ≠  ∅}. Prove that α is the lower adjoint of a Galois connection . Prove that if A is a partition of C that is ∀ Y , Y ʹ ∈ A . Y ∩ Y ʹ ≠ ∅ ⇒ Y = Y ʹ then γ is injective [249, section 5].

Exercise 11.11 ( polarities ) Given a relation R ∈ ℘( ℙ × ℚ ), define the polarities R * ( P ) ≜ { y ∈ ℚ |  ∀ x ∈ P . ⟨ x , y ⟩ ∈ R } and R † ( Q ) ≜ { x ∈ ℙ |  ∀ y ∈ Q . ⟨ x , y ⟩ ∈ R } [120, p . V .7]. Prove that ⟨ ℘( ℙ ), .

Exercise 11.12 Let A and B be sets . Define α fr ( F ) ≜ { ⟨ a , b ⟩ | b ∈ F ( a )} and γ fr ( R ) ≜ a { b | ⟨ a , b ⟩ ∈ R }. Prove that ⟨ A →  ℘( B ), .

Exercise 11.13  ( partition abstraction ) A partition of a set S is a family P = { B i | i ∈ Δ} of disjoint nonempty blocks (∀ i , j ∈ Δ.( i ≠ j ) ⇒ ( B i ∩ B j = ∅)) covering S ( ⋃ P = ⋃ { B i | i ∈ Δ} = S ). If x ∈ S , we let P ( x ) be the unique block of P to which x belongs to . Define α P π ( X ) ≜ Π i ∈Δ X ∩ B i .

<!-- formula-not-decoded -->

Δ | X ∩ B i ≠ ∅}. Prove that . Which abstraction is the most abstract ?

Exercise 11.14 ( language quotient ) Given a fi nite alphabet Σ, let Σ * be the possibly empty fi nite strings of letters of alphabet Σ called sentences ( or words ), and L 1 , L 2 ∈ ℘(Σ * ) be languages , that is , sets of sentences . Sentence and language concatenation is denoted by juxtaposition . Given a sentence w ∈  Σ * and a language L ∈ ℘(Σ * ), define the left quotient Lw -1 ≜ { x ∈ Σ * | xw ∈ L } and the right w -1 L ≜ { x ∈ Σ * | wx ∈ L }. Show that concatenation and the quotients give rise to Galois connections .

Exercise 11.15  ( big 𝒪 notation ) Show that the Bachmann-Landau notation 𝒪 ( f ) [463, § 1.6, 'Some Notations' ] ( in which one writes f ( x ) = 𝒪 ( g ( x )) as x →∞ if and only if for all sufficiently large values of x , the absolute value of f ( x ) is at most a positive constant multiple of g ( x )) is an abstraction of properties of real functions ℝ → ℝ by the positive real function f ∈ ℝ → ℝ * where ℝ * is the set of all positive reals .

Exercise 11.16 ( expected value ) Let X be a variable taking its values in a set 𝕍 . A set property P X of X is an element of ℘( 𝕍 ). For example , P X = {0} states that X is constant equal to 0. A probabilistic property P X of X is an element of 𝕍 → [0,1]. P X ( x ) ( often written P [ X = x ]) is the probability that variable X takes value x ∈ 𝕍 . For example , P X (0) = 1 whereas P X ( x ) = 0 whenever x ≠ 0 states that X is constant equal to 0. Statistics deal with large data sets and probabilistic distributions that are too large to consider individually each possible values . Statistical measures are used to represent meaningful properties of the distribution , with some loss of information , as a basis for best-guess predictions . Thus statistical measures are abstract interpretations of properties of distributions . An example is the expected value or mean . Show that this is a Galois connection .

Exercise 11.17 Let ⟨ L , ⊑⟩ be a poset . Given A ∈ ℘( L ), define α( A ) ≜ { x ∈ L | ∀ y ∈ A . y ⊑ x } ( the upper bounds of A ) and γ( A ) ≜ { x ∈ L | ∀ y ∈ A . x ⊑ y } ( the lower bounds of A ). Show that ⟨ ℘( L ), .

Exercise 11.18 ( lub abstraction ) Let ⟨𝒞 , ≤ ⟩ be a poset and ⟨𝒜 , ⊑ , ⊔ , ⊓⟩ be a complete lattice . Assume that . Define and , pointwise . Prove that .

Exercise 11.19  ( projection abstraction ) Let ⟨𝒞 1 ,  ≤ 1 , ⊤ 1 ⟩ and ⟨𝒞 2 ,  ≤ 2 , ⊤ 2 ⟩ be posets with respective suprema ⊤ 1 and ⊤ 2 . Prove that where the partial order ⟨ x , y ⟩ ≤ 1 × ≤ 2 ⟨ x ʹ, y ʹ ⟩ ≜ ( x ≤ 1 x ʹ) ∧ ( y ≤ 2 y ʹ) on pairs is componentwise , α 1 ( ⟨ x , y ⟩ ) = x is the first projection , and γ 1 ( x ) = ⟨ x , ⊤ 2 ⟩ . Generalize to the projection of any component of a Cartesian product .

Exercise 11.20 Considering a function f ∈ 𝒳 𝒴 as the relation { ⟨ x , f ( x ) ⟩ | x ∈ 𝒳 }, show that if and only if α ⨟ ⊑ = ≤ ⨟ γ -1 .

Exercise 11.21  ( pointwise extension of a Galois connection ) Show that the pointwise extension of a Galois connection where ( f ) ≜ x α( f ( x )) is a Galois

connection .

Exercise 11.22 ( abstraction of an increasing function at a point ) Let ⟨𝒟 , ⊑ , ⊤⟩ be a poset with supremum ⊤ and p ∈ 𝒟 . Given an increasing function f on 𝒟 , define α p ( f ) = f ( p ). Prove that where is the pointwise extension of ⊑ .

Exercise 11.23  ( pointwise homomorphic abstraction ) Let A , B , and C be sets . Assume f ∈ A → B → C . Define α h ( X ) a ≜ { f ( a ) x | x ∈ X }. Prove that ⟨ ℘( B ), ⟨ A → ℘( C ), .

Exercise 11.24 ( projection abstraction ) Prove that ⟨ ℘( 𝒞 1 )×… ×℘( 𝒞 n )× … ×℘( 𝒞 m ), for the projection abstraction α ∃ n , m ( ⟨ X 1 , …, X n , …, X m ⟩ ) = ⟨ X 1 , …, X n ⟩ where m ≥ n &gt; 0 and is the componentwise inclusion for k -tuples , k &gt; 0.

## 11.2 Galois Correspondences

A Galois correspondence is a Galois connection ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≽⟩ , that is , the adjoint functions are decreasing with 1 𝒞 ⊑ α ˚ γ and 1 𝒜 ≽ γ ˚ α. So a Galois correspondence is the semidual of a Galois connection . Their composition is not a Galois correspondence but is a Galois connection . It is the original notion inherited from Evarist

Galois' work .

We prefer Galois connections because they compose .

Galois correspondences are sometimes called decreasing Galois connections . Many other alternative names can be found in the literature , for example , residuated mappings for Galois connections [128, section 1.3] and Galois connections for Galois correspondences [128, section 1.6].

## 11.3 Duality of Galois Connections

Lemma 11.25 ( duality ) The order dual of an order-theoretic definition or statement is obtained by replacing ⊑ by its inverse ⊒ , upper by lower , least by greatest , ⊔ by ⊓ , join by meet , maximum by minimum , ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ by ⟨𝒞 , ⊒⟩ α γ ⟨𝒜 , ≽⟩ or equivalently by ⟨𝒜 , ≼⟩ ⟨𝒞 , ⊑⟩ , and so forth .

Therefore , dualization of a definition / statement / formula involving Galois connections consists of exchanging the adjoints .

## Proof of lemma 11.25

## The dual statement is

Exercise 11.26 Prove that that if ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ and ⟨𝒞 , ⊑⟩ has an infimum ⊥ then ⟨𝒜 , ≼⟩ has an infimum . What is the dual ?

Example 11.27 An example of duality is [190]. The fi rst part recalls results of overapproximation by abstract interpretation . The second part on underapproximation is the dual of the fi rst part .

## 11.4 Order , Join , and Meet Preservation

## Definition 11.28

Let ⟨ P 1 , ⊑ 1 ⟩ and ⟨ P 2 , ⊑ 2 ⟩ be posets and f ∈ P 1 → P 2 be a total function . A standard example is ⟨ P 1 , ⊑ 1 ⟩ = ⟨ ℘( S 1 ),  ⊆ ⟩ , ⟨ P 2 , ⊑ 2 ⟩ = ⟨ ℘( S 2 ), ⊆ ⟩ , and f ∈ ℘( S 1 ) ℘( S 2 ) is a set transformer .

- f is order preserving or increasing when ∀ x , y ∈ P 1 . x ⊑ 1 y implies f ( s ) ⊑ 2 f ( y ). This is written f ∈ P 1 P 2 . The dual of increasing is increasing .
- f preserves fi nite joins ( respectively fi nite meets ) if and only if for all x , y ∈ P 1 such that the lub x ⊔ 1 y exists , the lub f ( x ) ⊔ 2 f ( y ) exists , and f ( x ⊔ 1 y ) = f ( x ) ⊔ 2 f ( y ) ( respectively for the glb , f ( x ⊓ 1 y ) = f ( x ) ⊓ 2 f ( y ) when x ⊓ 1 y exists ).
- f preserves the infimum or is infimum strict whenever if P 1 has an infimum ⊥ 1 then P 2 has an infimum ⊥ 2 such that f (⊥ 1 )  =  ⊥ 2 . Supremum preservation or supremum strictness is dual .

- f preserves nonempty joins if and only if given any nonempty indexing set Δ and index X ∈ Δ P 1 such that the lub ⊔ 1 { X ( i ) | i ∈ Δ} exists in P 1 , we have ⊔ 2 { f ( X ( i )) | i ∈  Δ} exists in P 2 and f ( ⊔ 1 { X ( i ) | i ∈ Δ}) = ⊔ 2 { f ( X ( i )) | i ∈ Δ} ( which is often written f ( ⊔ 1 i ∈Δ X i ) = ⊔ 2 i ∈Δ f ( X i ) where X i denotes the family X ( i ), i ∈ Δ). Nonempty meet preservation is dual .
- f preserves ( arbitrary ) joins or is strictly join preserving if and only if it preserves both the infimum ⊥ = ⊔ 1 ∅ and nonempty joins . This is written f ∈ P 1 P 2 Dually , meet preservation is denoted P 1 P 2 .

Exercise 11.29 Let f be an increasing function on a poset ⟨ P , ⊑ , ⊔⟩ . Assume that X ∈ ℘( P ) and the lubs ⊔ X and ⊔ f ( X ) do exist ( with f ( X ) ≜ { f ( x ) | x ∈ X }. Prove that ⊔ f ( X ) ⊑ f ( ⊔ X ).

Exercise 11.30 Prove that a function f on posets preserving joins or meets is increasing .

Exercise 11.31 Prove that if ⟨ P 1 , ⊑ 1 ⟩ and ⟨ P 2 , ⊑ 2 ⟩ be posets , f ∈ P 1 P 2 is increasing , and X ⊆ P 1 then ⊔ 2 { f ( x ) | x ∈ X } ⊑ 2 f ( ⊔ 1 X ) whenever the lubs do exist .

Exercise 11.32 Let ⟨ D , ⊑ , ⊥, ⊤ , ⊔ , ⊓⟩ be a complete lattice . Prove that the set D D of ( arbitrary ) joins functions ordered pointwise ( f g if and only if ∀ x ∈ D . f ( x ) ⊑ g ( x )) is a complete lattice where and are respectively and , pointwise .

## 11.5 Order Properties of Galois Connections

Lemma 11.33  ( increasingness ) If ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ then α and γ are increasing .

Proof Assume P ⊑ P ʹ. By α( P ʹ) ≼ α( P ʹ) we have P ʹ ⊑ γ(α( P ʹ)) so that P ⊑ γ(α( P ʹ)) by transitivity , hence α( P ) ≼ α( P ʹ) by definition of a GC , proving that α is increasing .

Increasing is self-dual , so the dual of 'In ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ , the lower adjoint α is increasing' is 'In ⟨𝒜 , ≼⟩ ⟨ 𝒞 , ⊑⟩ , the lower adjoint γ is increasing , ' proving that γ is increasing in ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ .

Exercise 11.34 Prove that in a Galois connection ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ we have α ˚ γ ˚ α = α. Express the dual .

Exercise 11.35 ( equivalent definition of Galois connections ) Prove that ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ if and only if α ∈ 𝒞 → 𝒜 and γ ∈ 𝒜 → 𝒞 satisfy

- (1) α is increasing ;
- (2) γ is increasing ;
- (3) ∀ x ∈ 𝒞 . x ⊑ γ ˚ α( x ) ( i . e ., γ ˚ α is extensive );
- (4) ∀ y ∈ 𝒜 . α ˚ γ( y ) ≼ y ( i . e ., α ˚ γ is reductive ).

Exercise 11.36 ( equivalent definition of a Galois connection [61]) Show that ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ if and only if α is increasing , ∀ x ∈ 𝒜 . α ˚ γ( x ) ⊑ x and ∀ x , y .α( x ) ≼ y ⇒ x ⊑ γ( y ).

Exercise 11.37 Prove that there is no Galois connection ⟨ℕ ,  ≤ ⟩ ⟨ { }, = ⟩ where is the only element of the singleton domain { }.

Lemma 11.38 ( existing join preservation ) If ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ then α preserves lubs that may exist in 𝒞 ; that is , let ⊔ be the partially defined lub for ⊑ in 𝒞 and ⋎ be the partially defined lub for ≼ in 𝒜 . Let S ∈ ℘( 𝒞 ) be any subset of 𝒞 . If ⊔ S exists in 𝒞 then the upper bound ⋎ {α( e ) | e ∈ S } exists in 𝒞 and is equal to α( ⊔ S ).

Proof By existence and definition of the lub ⊔ S , we have ∀ e ∈ S . e ⊑⊔ S so α( e ) ≼ α( ⊔ S ) because α is increasing . It follows that α( ⊔ S ) is an upper bound of {α( e ) | e ∈ S }. Let u be any upper bound of this set {α( e ) | e ∈ S } so that ∀ e ∈ S .α( e ) ≼ u . By definition of a GC , ∀ e ∈ S . e ⊑ γ( u ). Hence γ( u ) is an upper bound of S . By existence and definition of the lub ⊔ S , ⊔ S ⊑ γ( u ) so α( ⊔ S ) ≼ u , proving that α( ⊔ S ), which exists because α is a total function , is the lub of {α( e ) | e ∈ S } denoted ⋎ {α( e ) | e ∈ S }.

By duality , γ preserves existing meets .

Exercise 11.39 ([795]) Prove that if α preserves existing lubs and γ( y ) ≜ ⊔ { x ∈ 𝒞 | α( x ) ≼ y } is well defined then ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ .

Exercise 11.40 Consider the following concretization function . Prove that there is no corresponding Galois connection .

Exercise 11.41 Consider the following concretization function . Prove that there is no corresponding Galois connection .

<!-- image -->

Lemma 11.42 In a Galois connection one adjoint uniquely determines the other i . e . α( P ) = ⊓ { | P ⊑ γ( )} and γ( ) = ⊔ { P | α( P ) ≼ }.

<!-- image -->

Proof of Lemma 11.42 Observe that ∀ P ∈ 𝒞 .α( P ) = ⊓ { |  α( P ) ≼ } so , by definition of a GC , α( P )  = ⊓ { | P ⊑ γ( )}, that is , γ uniquely determines α. Dually α uniquely determines γ because ∀ ∈ 𝒜 .γ( ) = ⊔ { P | α( P ) ≼ }.

It immediately follows that

Corollary 11.43 If ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ and ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ then γ = γʹ. If ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ and ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ then α = αʹ. An alternative proof is the following .

Proof of Corollary 11.43 By exercise 11.35.3, ∀ x ∈ 𝒞 . x ⊑ γʹ ˚ α( x ) so in particular γ( y ) ⊑ γʹ ˚ α ˚ γ( y ). By exercise 11.35.4, α ˚ γ( y ) ≼ y so , by exercise 11.35.2, γʹ ˚ α ˚ γ( y ) ⊑ γʹ( y ). By transitivity , γ( y ) ⊑ γʹ( y ). By exchanging the rôles of γ and γʹ, a similar proof yields γʹ( y ) ⊑ γ( y ). By antisymmetry γ = γʹ. The proof for α and αʹ is dual .

Lemma 11.42 and corollary 11.43 are useful in situations where only one adjoint is defined explicitly because then the other is also uniquely determined . It is important to note that the two Galois connections must have the same concrete and abstract partial orders . If these orders differ , this may no longer be true .

Exercise 11.44 Which Galois connection can be derived from the arithmetic property ∀ x , y , z ∈ ℕ . z × y ≤ x ⇔ z ≤ x ÷ y ? Prove that this implies that x ÷ y = max { z | x × y ≤ x }. Perform the same exercise with z -y ≤ x ⇔ z ≤ x + y on ℤ .

Exercise 11.45 Let ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ . Prove that γ ˚ α ˚ γ = γ. What is the dual ?

Exercise 11.46 Let ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ . Following exercise 11.45, prove that ⟨ γ( 𝒜 ), ⊑⟩ ⟨ α( 𝒞 ), ≼⟩ ( where f ( X ) = { f ( x ) | x ∈ X }, ≜ α ⌉ γ( 𝒜 ) is the restriction of α to γ( 𝒳 ) and ≜ γ ⌉ α( 𝒜 )).

Exercise 11.47 The corresponding fi xpoints of the Galois connection ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ are ⟨ x , y ⟩ ∈ 𝒞 × 𝒜 such that α( x ) = y and γ( y ) = x . Following exercise 11.45, show that for all x ∈ 𝒞 and y ∈ 𝒜 , the pairs ⟨ γ ˚ α( x ), α( x ) ⟩ and ⟨ γ( y ), α ˚ γ( y ) ⟩ are corresponding fi xpoints .

Exercise 11.48 Let ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ . Prove that γ( a ) = max α -1 (↓ a ) = ⊔ α -1 (↓ a ) where max C is the maximum of the set C ∈ ℘( 𝒞 ), α -1 ( A ) ≜ { c ∈ 𝒞 | α( c ) ∈ A }, and ↓ a ≜ { x ∈ 𝒜 | x ≼ a }. State the dual property ( using ↑ c ≜ { x ∈ 𝒞 | c ⊑ x }).

## 11.6 Galois Retraction

A Galois connection ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ such that α is surjective is called a Galois retraction . 3 ( or Galois surjection , Galois insertion , Galois reflexion [353] or 'perfect Galois connection' [762,  831]) denoted ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ .

Example 11.49 A simple example of Galois connection that is not a retraction is

<!-- image -->

The abstract property b in 𝒜 is useless because any concrete property P in 𝒞 overapproximated by b in 𝒜 ( i . e ., α( P ) ≼ b ) can be overapproximated more precisely by a ( because α( P ) ≼ b implies α( P ) ≼ a ) and a and b have the same concretization A . Hence the abstract domain 𝒜 can be reduced by eliminating b ; see section 36.3.3.

Exercise 11.50 ( Galois retraction [762, THEOREM 3]) Show that if ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ then α is surjective if and only if γ is injective if and only if ∀ ∈ 𝒜 .α ˚ γ( ) = if and only if γ( Q ) = max { P ∈ 𝒞 | α( P ) = Q } for all Q ∈ A . Express the dual ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ . Why is any isomorphism between 𝒞 and 𝒜 not a Galois isomorphism ( denoted ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ )?

Exercise 11.51 Let ρ be an upper closure on ⟨𝒞 , ⊑⟩ ( that is , increasing , extensive , and idempotent ; see next section 11.7). Prove that ⟨𝒞 , ⊑⟩ ⟨ ρ( 𝒞 ), ⊑⟩ where ρ( 𝒞 ) is the image of 𝒞 by ρ ( called a retract of 𝒞 ).

Exercise 11.52 Define α and γ such that ⟨ ℘( 𝒟 × 𝒞 ),⊆ ⟩ ⟨𝒟 ℘( 𝒞 ), ⟩ .

→

Exercise 11.53 Let ⟨ L , ⊑ , ⊥, ⊤ , ⊔ , ⊓⟩ be a complete lattice , let ⟨ L L , , , , , ⟩ be the complete lattice of increasing maps on L ordered pointwise . Define α( f ) ≜ { x ∈ L | f ( x ) ⊑ x }. Prove that ⟨ L L , ⟩ ⟨ ℘( L ), ⊇ ⟩ .

Exercise 11.54 A subset 𝒜 of 𝒳 is said to be a retract of 𝒳 if there is a so-called retraction f ∈ 𝒳 → 𝒜 such that ∀ a ∈ 𝒜 . f ( a ) = a . Show that in a Galois retraction ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ , 𝒜 is a retract of α( 𝒞 ).

Exercise 11.55 Let d ∈ 𝒞 × 𝒞 → ℝ * be a distance on a set 𝒞 , meaning that for all x , y , z ∈ 𝒞 , we have d ( x , y ) = 0 ⇔ x = y , d ( x , y ) ≤ d ( x , z ) + d ( z , y ), and d ( x , y )  = d ( y , x ). Assume that ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ is a Galois retraction . Prove that D ( , ) ≜ d (γ( ), γ( )) is a distance on 𝒜 .

## 11.7 Closure Operators

An upper closure operator ρ ∈ L → L on a poset ⟨ L , ⊑⟩ is increasing , idempotent (ρ ˚ ρ = ρ), and extensive ∀ x ∈ L . x ⊑ ρ( x ). The dual lower closure operator is increasing , idempotent , and reductive ∀ x ∈ L . ρ( x ) ⊑ x . The closed elements x ∈ L of a closure operator ρ ∈ L → L are such that ρ( x ) = x . The closed subsets of a closure operator ρ ∈ L → L are such that ρ( S ) ≜ {ρ( x ) | x ∈ S } = S . For example ,

Exercise 11.57 Prove that in a Galois connection ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ , γ ˚ α is an upper closure operator on 𝒞 and α ˚ γ is a lower closure operator on 𝒜 .

Exercise 11.58 Continuing exercise 11.57, let the ceiling ⌈ x ⌉ of x ∈ ℝ be the least integer greater than or equal to x . Show that ⟨ ℝ , ≤ ⟩ ⟨ℤ , ≤ ⟩ where α( x ) ≜⌈ x ⌉ and γ( y ) = y . Prove that ⌈ x ⌉ is an upper closure on ℝ .

Exercise 11.59 Let ⟨𝒞 , ⊑⟩ and ⟨𝒜 , ≼⟩ be posets , α ∈ 𝒞 → 𝒜 and γ ∈ 𝒜 → 𝒞 be such that γ ˚ α is an upper closure operator on 𝒞 and α ˚ γ is a lower closure operator on 𝒜 . Is ⟨ α, γ ⟩ a Galois connection ?

Exercise 11.60 Prove that if ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ is a Galois connection , then ⟨𝒞 , ⊑⟩ ⟨ γ ˚ α( 𝒞 ), ⊑⟩ is a Galois connection where γ ˚ α( 𝒞 ) = {γ(α( x )) | x ∈ 𝒞 } is the image of 𝒞 by the upper closure γ ˚ α. What is the dual ?

Exercise 11.61  ( upper closure operator ) Prove that ρ is an upper closure operator on ⟨ L , ⊑⟩ if and only if ⟨ L , ⊑⟩ ⟨ ρ( L ), ⊑⟩ where 1 L is the identity function on L and ρ( L ) = {ρ( x ) | x ∈ L } is the right image of L by ρ. What is the dual ?

Exercise 11.62 ([719]) Using exercise 11.61, prove that ρ is an upper closure operator on ⟨ L , ⊑⟩ if and only if x ⊑ ρ( y ) ⇔ ρ( x ) ⊑ ρ( y ).

Exercise 11.63 Prove that ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ if and only if {γ( y ) | y ∈ 𝒜 } is the image of 𝒞 by an upper closure operator . What is the dual ?

Exercise 11.64  ([964, THEOREM 4.1]) Prove that the image of a complete lattice ⟨ℒ , ⊑⟩ by a closure operator ρ is a complete lattice . Extend this result to Galois retractions .

Let ⟨𝒫 , ⊑⟩ and ⟨𝒬 , ≼⟩ be posets . An order embedding of ⟨𝒫 , ⊑⟩ into ⟨𝒬 , ≼⟩ is map f ∈ 𝒫 → 𝒬 such that ∀ x , y ∈ 𝒫 . x ⊑ y ⇔ f ( x ) ≼ f ( y ).

The Dedekind-MacNeille completion order embed any poset ⟨𝒫 , ⊑⟩ into a complete lattice ⟨ℒ , ≼⟩ so that distinct elements of 𝒫 are be mapped to distinct elements of ℒ , and each pair of elements in ⟨𝒫 , ⊑⟩ has the same ordering in ⟨ℒ , ≼⟩ as they do in ⟨𝒫 , ⊑⟩ . This construction is sometimes used to construct abstract domains , for example , [530].

Exercise 11.65  ( Dedekind-MacNeille completion ) Let ⟨𝒫 , ⊑⟩ be a poset . Define ( X ) ≜ { y ∈ 𝒫 |  ∀ x ∈ X . y ⊑ x } and ( X ) ≜ { x ∈ 𝒫 |  ∀ y ∈ X . y ⊑ x }. Prove that ⟨ ℘( 𝒫 ), ⊆ ⟩ ⟨ ℘( 𝒫 ), ⊇ ⟩ . Prove that is an upper closure operator on ℘( 𝒫 ). Its fi xpoints in (℘( 𝒫 )) are called stable elements . Prove that ⟨ (℘( 𝒫 )),  ⊆ ⟩ is a complete lattice ( called the Dedekind-MacNeille completion of ⟨𝒫 , ⊑⟩ ). Prove that the map is an embedding of ⟨𝒫 , ⊑⟩ into ⟨ (℘( 𝒫 )), ⊇ ⟩ . Prove that distinct elements of 𝒫 are be mapped to distinct elements of (℘( 𝒫 )). Prove that each pair of elements in ⟨𝒫 , ⊑⟩ has the same ordering in ⟨ (℘( 𝒫 )),  ⊇ ⟩ as they do in ⟨𝒫 , ⊑⟩ . Prove that ⟨𝒫 , ⊑⟩ ⟨ (℘( 𝒫 )), ⊇ ⟩ .

The ideas of exercise 11.65 also apply to the completion of posets into chain-complete posets ( where increasing chains have lubs ) [656, 657].

## 11.8 Composition of Galois Connections

Exercise 11.66  ( composition of Galois connections ) Prove that the composition of Galois connections ⟨𝒫 1 , ⊑⟩ ⟨𝒫 2 , ≼⟩ and ⟨𝒫 2 , ≼⟩ ⟨𝒫 3 , ⟩ is the Galois connection ⟨𝒫 1 , ⊑⟩ ⟨𝒫 3 , ⊲⟩ .

## 11.9

## Galois Connection in a Complete Boolean Algebra

## 11.9.1 Complete Boolean Algebra

Let ⟨ L , ⊑ ,  ⊥, ⊓ ,  ¬ ⟩ be a meet semilattice with infimum ⊥ such that every element y ∈ L has a pseudocomplement ¬ y such that , by definition , x ⊓ y = ⊥ if and only if x ⊑ ¬ y , that is , for any x ∈ L the set of elements y disjoint from x has a largest element ¬ y .

It follows that y ⊓ (¬ y ) = ⊥.

Assume that ¬¬ y is another pseudocomplement of y . (¬¬ y ) ⊓ y = ⊥ implies (¬¬ y ) ⊑ ¬ y and (¬ y ) ⊓ y = ⊥ implies (¬ y ) ⊑ ¬¬ y proving ¬¬ y = ¬ y by antisymmetry so that the pseudocomplement is unique .

Moreover x ⊓ ⊥  =  ⊥ so that x ⊑ ¬  ⊥ proving that ¬  ⊥  = ⊤ is the supremum of L .

A complete Boolean algebra is a complete lattice such that any element x has a unique complement such that x ⊓ ¬ x = ⊥ and x ⊔ ¬ x = ⊤ . For example , the powerset is a complete Boolean algebra ⟨ ℘( S ), ⊆, ∅, ⋂ , ¬ ⟩ where ¬ X ≜ S ∖ X .

We have x ⊑ y implies x ⊓ ¬ y ⊑ y ⊓ ¬ y = ⊥, which implies x ⊓ ¬ y = ⊥ so ¬ y ⊑ ¬ x .

Because y ⊓ (¬ y ) = ⊥, y ⊑ (¬¬ y ).

By exercise 11.35, it follows that ⟨ L , ⊑⟩ ⟨ L , ⊒⟩ .

## 11.9.2

## Conjugate Galois Connection

Let ⟨ L , ⊑ ,  ⊥, ⊤ , ⊓ , ⊔ ,  ¬ ⟩ be a complete Boolean algebra and ⟨ L , ⊑⟩ ⟨ L , ⊑⟩ . Then , by the composition of Galois connections defined in section 11.8, we have the conjugate Galois connection ⟨ L , ⊑⟩ ⟨ L , ⊑⟩ .

Similarly , ⟨ L , ⊑⟩ ⟨ L , ⊒⟩ , and by the duality lemma 11.25, ⟨ L , ⊑⟩ ⟨ L , ⊒⟩ .

We write and for the conjugates ≜ ¬ ˚ α ˚ ¬ and ≜ ¬ ˚ γ ˚ ¬.

## 11.9.3 Characterization of Galois Connections in a

## Complete Boolean Algebra

Lemma 11.67 Let be a pointwise extension of the complete Boolean algebra . Then , if and only if .

## Proof of lemma 11.67

## 11.10 Complete Heyting Algebra

In propositional calculus , we have ( a ∧ x ) ⇒ y if and only if x ⇒ ( a ⇒ y ), that is , (α a ( x ) ⇒ y ) ⇔( x ⇒ γ a ( y )) where α a ( x ) ≜ a ∧ x and γ a ( y ) ≜ a ⇒ y . Considering ⇒ has a partial order , this extends to posets .

A complete Heyting algebra is a complete lattice ⟨ L , ⊑ , ⊓⟩ such that for all elements a ∈ L , α a ( y ) ≜ a ⊓ y is the lower adjoint of a Galois connection ⟨ L , ⊑⟩ ⟨ L , ⊑⟩ . Arend Heyting used such algebras to formalize intuitionist logic [495, CH VII ].

Exercise 11.68 Show that the definition of a complete Heyting algebra ⟨ L , ⊑ , ⊓ , ⊔⟩ is equivalent to ∀ x ∈ L . ∀ S ∈ ℘( L ). x ⊓⊔ s ∈ S s = ⊔

s ∈ S ( x ⊓ s ).

## 11.11 Sound Abstraction

Assume that ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ is a Galois connection between concrete properties in 𝒞 with implication ⊑ and abstract properties in 𝒜 with abstract implication ≼ .

Definition 11.69 ( sound abstraction ) We say that ∈ 𝒜 is a sound abstraction of P ∈ 𝒞 if and only if P ⊑ γ( ).

The intuition is that the meaning γ( ) of the abstract property is weaker than the concrete property P hence is an overapproximation . The dual is underapproximation .

## Example 11.70 Consider the lattice of abstract properties

<!-- image -->

The sound abstractions of {1, 42} are ≥0 and because {1, 42}⊆{ z | z ≥ 0} = γ ± (≥0) and {1, 42}⊆ ℤ = γ ± ( ).

## 11.12 Best Abstraction

Definition 11.71  ( better abstraction ) Let 1 , 2 ∈ 𝒜 be sound abstractions of the concrete property P ∈ 𝒞 . We say that 1 is better / more precise / stronger / less abstract than 2 if and only if 1 ≼ 2 .

Theorem 11.72 ( best abstraction ) If ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ then α( P ) is the best / most precise / strongest / least abstract property which is a sound abstraction of the concrete property P .

Proof By definition 11.69, α( P ) is a sound abstraction of P because P ⊑ γ(α( P )).

Let be any sound abstraction of P so that , by definition 11.69, P ⊑ γ( ). Then by definition of a Galois connection , α( P ) ≼ proving that α( P ) is the least sound abstraction of P , that is , α( P ) = ⊓ { | P ⊑ γ( )}, as shown in lemma 11.42.

Exercise 11.73 Prove a converse of theorem 11.72.

Example 11.74 Continuing example 11.70, the best abstraction of {1, 42} is ≥0 because {1, 42} ⊆ γ ± (≥0), {1, 42} ⊆ γ ± ( ), and ≥0 ⊑ ± [ ].

The sound abstractions of {0} are ≤0, ≥0, and [ ] because {0} ⊆ { z | z ≤  0}  =  γ ± (≤0),  {0}  ⊆  { z | z ≥  0}  = γ ± (≥0), and {0}  ⊆ ℤ = γ ± ([ ]). However , there is no best approximation because ≤0 and ≥0 are not ±

comparable by the partial order ⊑ .

By the contraposition of theorem 11.72, it follows that there is no Galois connection between ⟨ ℘( ℤ ), ⊆ ⟩ and ⟨ ℙ ± , ⊑ ± ⟩ .

## 11.13 Combinations of Galois Connections

## 11.13.1 Galois Connections Pairing

The following theorem shows that Galois connections on domains can be extended to a Galois connection between their Cartesian product .

Theorem 11.75 If ⟨𝒞 1 , ⊑ 1 ⟩ ⟨𝒜 1 , ≼ 1 ⟩ and ⟨𝒞 2 , ⊑ 2 ⟩ ⟨𝒜 2 , ≼ 2 ⟩ then ⟨𝒞 1 × 𝒞 2 , ⟩ ⟨𝒜 1 × 𝒜 2 , ⟩ where and are componentwise , and α( ⟨ x , y ⟩ ) = ⟨ α 1 ( x ), α 2 ( y ) ⟩ , γ( ⟨ , ⟩ ) = ⟨ γ 1 ( ), γ 2 ( ) ⟩ .

## Proof of theorem 11.75

Exercise 11.76 Let ⊩ 1 ∈ ⟨𝒞 1 , ⊑ 1 ⟩ ⊗ ⟨𝒜 1 , ≼ 1 ⟩ and ⊩ 2 ∈ ⟨𝒞 2 , ⊑ 2 ⟩ ⊗ ⟨𝒜 2 , ≼ 2 ⟩ . Define ⟨ x , y ⟩⊩⟨ , ⟩ if and only if x ⊩ 1 ∧ y ⊩ 1 . Prove that ⊩ is a logical relation .

## 11.13.2 Higher-order Galois

## Connections

The following theorem shows that Galois connections on the domain and codomain of increasing functions can be extended to a Galois connection between these functions , as shown in fi gure 11.77.

<!-- image -->

## Figure 11.77

Higher-order Galois connection

<!-- formula-not-decoded -->

## Proof of theorem 11.78

Exercise 11.79 Let ⊩ 1 ∈ ⟨𝒞 1 , ⊑ 1 ⟩ ⊗ ⟨𝒜 1 , ≼ 1 ⟩ and ⊩ 2 ∈ ⟨𝒞 2 , ⊑ 2 ⟩ ⊗ ⟨𝒜 2 , ≼ 2 ⟩ . Define f ⊩ if and only if ∀ x ∈ 𝒞 1 , ∈ 𝒜 1 . x ⊩ 1 ⇒ f ( x ) ⊩ 2 ( ). Prove that ⊩ is a logical relation .

## 11.14 Galois Connection , Logical Relation , Tensor Product , Soundness Relation

We formalize best abstractions by Galois connections . Soundness relation are mathematically equivalent formalizations useful to prove soundness ( what is true in the abstract holds in the concrete ), but , by experience , not as convenient to prove completeness ( i . e ., what is true in the abstract is provable in the abstract ; see chapter 52, 'Semantic Soundness , Completeness , and Definedness' ).

Definition 11.80 ( logical relation ) A relation ⊩ ∈ ℘( 𝒞 × 𝒜 ) between complete lattices ⟨𝒞 , ⊑ , ⊔ ⟩ and ⟨𝒜 , ≼ , ⋏ ⟩ is a logical relation if and only if

Definition 11.81  ( tensor product )  [887] The tensor product ⟨𝒞 , ⊑⟩ ⊗ ⟨𝒜 , ≼⟩ of two complete lattices ⟨𝒞 , ⊑⟩ and ⟨𝒜 , ≼⟩ is

Definition 11.82  ( soundness relation ) Assume that ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ then the relation P ⊩ ≜ ( P ⊑ γ( )), or equivalently , P ⊩ ≜ (α( P ) ≼ ) is called the soundness relation .

The following theorem shows that the use of Galois connections or logical relations is mathematically equivalent in abstract interpretation .

Theorem 11.83 Let ⟨𝒞 , ⊑⟩ and ⟨𝒜 , ≼⟩ be complete lattices . ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ if and only if ⊩ ∈ ⟨𝒞 , ⊑⟩ ⊗ ⟨𝒜 , ≼⟩ .

Proof of theorem 11.83 Assume ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ .

## Conversely , assume that ⊩ ∈ ⟨𝒞 , ⊑⟩ ⊗ ⟨𝒜 , ≼⟩ . Define

## 11.15 Hierarchy of Abstractions

In a Galois connection ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ , γ ˚ α is , by exercise 11.57, an upper closure operator on ⟨𝒞 , ⊑⟩ . Moreover , ⟨𝒞 , ⊑⟩ ⟨ α( 𝒞 ), ≼⟩ where α( 𝒞 ) ≜ {α( x ) | x ∈ 𝒞 }, in which case γ ˚ α( 𝒞 ) and α( 𝒞 ) are isomorphic by α according to exercise 11.45. It is therefore possible , at least in theory , to eliminate the redundant elements from the abstract domain ⟨𝒜 , ≼⟩ to get ⟨𝒞 , ⊑⟩ ⟨ α( 𝒞 ), ≼⟩ and then to reason in the concrete on ⟨ γ ˚ α( 𝒞 ), ⊑⟩ which is the isomorphic image of the abstract domain ⟨ α( 𝒞 ), ≼⟩ in the concrete . The mathematical advantage is to get rid of the specific representation of abstract properties in ⟨𝒜 , ≼⟩ in order to reason uniquely in the concrete ⟨𝒞 , ⊑⟩ and the concrete representation ⟨ γ ˚ α( 𝒞 ), ⊑⟩ of the abstract properties . Of course , in practice this problem cannot be escaped for static analysis .

This motivates mathematically the study of upper closure operators ( and lower closure operators by duality ).

A closure operator is fully determined by its closed elements . This shows that if the abstract domain is known then the abstraction is uniquely known .

Theorem 11.86  ([712, th .  5.2]) Let ⟨ L , ⊑ ,  ⊥, ⊤ , ⊔ , ⊓⟩ be a complete lattice and ρ, ρʹ ∈ L → L be closure operators on L . If ρ( L ) = ρʹ( L ), then ρ = ρʹ.

Figure 11.85

<!-- image -->

Galois connection ⟨𝒞 , ⊑⟩ ⟨𝒜 , ≼⟩ , upper closure operator γ ˚ α, and lower closure operator α ˚ γ

Proof of theorem 11.86 ∀ z ∈ L . z ⊑ ρ( z ) so ρʹ( z ) ⊑ ρʹ(ρ( z )). By ρ( L ) = ρʹ( L ) and idempotence , ρ and ρʹ have the same fi xpoints . So ρ(ρ( z )) = ρ( z ) implies ρʹ(ρ( z )) = ρ( z ) proving ρʹ( z ) ⊑ ρ( z ). Exchanging ρʹ and ρ, we get ρ( z ) ⊑ ρʹ( z ), that is , ρ( z ) = ρʹ( z ) by antisymmetry .

Theorem 11.87 Let ⟨ L , ⊑ , ⊥, ⊤ , ⊔ , ⊓⟩ be a complete lattice and f ∈ L → L be an operator on L . Define uco ( f ) ≜ x ⊓ { y ∈ L | x ⊔ f ( y ) ⊑ y }. uco ( f ) is an upper closure operator that is smaller than any upper closure operator on L and greater than or equal to f .

If f ∈ L L is increasing then uco ( f ) x = lfp ⊑ y x ⊔ f ( y ) is the -least upper closure operator on L which is greater than or equal to f .

A dual result for lco ( f ) ≜ x ⊔ { y ∈ L | y ⊑ ( x ⊓ f ( y ))}.

## Proof of theorem 11.87

- -∀ y ∈ { y ∈ L | x ⊔ f ( y ) ⊑ y } . x ⊑ y so x ⊑ ⊓ { y ∈ L | x ⊔ f ( y ) ⊑ y } = uco ( f ) x so uco ( f ) is extensive .
- -If x ⊑ x ʹ then x ʹ ⊔ f ( y ) ⊑ y implies x ⊔ f ( y ) ⊑ y so { y | x ʹ ⊔ f ( y ) ⊑ y }⊆ { y | x ⊔ f ( y ) ⊑ y }, proving that uco ( f ) x = ⊓ { x ⊔ f ( y ) ⊑ y } ⊑⊓ { y | x ʹ ⊔ f ( y ) ⊑ y } = uco ( f ) x ʹ so uco ( f ) is increasing .
- -By extensivity and increasingness , x ⊑ uco ( f )( x ) ⊑ uco ( f )( uco ( f ) x ).
- -If f ( y ) ⊑ y then y ⊔ f ( y ) ⊑ y so y ∈ { z ∈ L | y ⊔ f ( z ) ⊑ z }, in which case uco ( f ) y = ⊓ { z ∈ L | y ⊔ f ( z ) ⊑ z } ⊑ y . It follows that x ⊔ f ( y ) ⊑ y implies x ⊑ y and uco ( f ) y ⊑ y so x ⊔ uco ( f ) y ⊑ y and therefore { y | x ⊔ f ( y ) ⊑ y } ⊆ { y | x ⊔ uco ( f ) y ⊑ y }, proving that uco ( f )( uco ( f ) x ) = ⊓ { y | x ⊔ uco ( f ) y ⊑ y } ⊑⊓ { y | x ⊔ f ( y ) ⊑ y } = uco ( f ) x .
- -By antisymmetry uco ( f )( uco ( f ) x )  = uco ( f ) x so uco ( f ) x is idempotent , hence an upper closure operator .
- -Let ρ be a closure operator on L such that f ρ. We have x ⊑ ρ( x ) and f (ρ( x )) ρ(ρ( x )) = ρ( x ) so x ⊔ f (ρ( x )) ⊑ ρ( x ) which implies ρ( x ) ∈ { y | x ⊔ f ( y ) ⊑ y } and therefore uco ( f ) x = ⊓ { y | x ⊔ f ( y ) ⊑ y } ⊑ ρ( x ) proving that uco ( f ) is smaller than any upper closure operator on L greater than or equal to f .

-If f is increasing then the map y ( x ⊔ f ( y )) is increasing so uco ( f ) x ≜ lfp ⊑ y ( x ⊔ f ( y )) is well defined by theorem 15.6 and equal to ⊓ { y | x ⊔ f ( y ) ⊑ y }.

-If f is increasing and y ∈{ y | x ⊔ f ( y ) ⊑ y } then x ⊑ y so f ( x ) ⊑ f ( y ) and f ( y ) ⊑ y so f ( x ) ⊑ y and therefore f ( x ) ⊑⊓ { y | x ⊔ f ( y ) ⊑ y } = uco ( f ) x , proving that uco ( f ) is the -least upper closure operator on L which is greater than or equal to f .

Theorem 11.88 The image of a complete lattice ⟨ L , ⊑ , ⊥, ⊤ , ⊔ , ⊓⟩ by a closure operator ρ ∈ L → L is a complete lattice ⟨ ρ( L ), ⊑ , ρ(⊥), ⊤ , X ρ( ⊔ X ), ⊓⟩ .

For example , in fi gure 11.56, ρ( L )  =  {2,  5,  6,  8} is the set of circled bullets . The join of 5 and 6 in L is 5 ⊔ 6 = 7. The join of 5 and 6 in ρ( L ) is ρ(5 ⊔ 6) = ρ(7) = 8. The meet 5 ⊓ 6 = 2 is the same in L and ρ( L ).

<!-- image -->

## Figure 11.56

Upper closure operator

Theorem 11.88 explains why abstract domains discussed in chapter 3 are complete lattices . The collecting semantics ⟨ ℘(( 𝕍 → ℤ ) → ℤ ),  ⊆ ⟩ of arithmetic expressions is a complete lattice , so all its abstractions ⟨ ρ(℘(( 𝕍 → ℤ ) → ℤ )), ⊆ ⟩ by upper closure operators ( or Galois retractions ) ρ on expression properties ℘(( 𝕍 → ℤ ) → ℤ ) are complete lattices . 4

Proof of theorem 11.88 We have ρ( L ) = {ρ( x ) | x ∈ L } ⊆ L so ⊑ is a partial order on ρ( L )  .  ∀ y ∈ ρ( L )  .  ∃ x ∈ L .ρ( x )  = y so ⊥ ⊑ x ⊑ ⊤ and increasingness imply ρ(⊥) ⊑ ρ( x )  = y ⊑ ρ( ⊤ )  = ⊤ because ρ is extensive and ⊤ is the supremum , proving that ρ(⊥) is the infimum and ⊤ is the supremum of ρ( L ). Let ⟨ x i , i ∈ Δ ⟩ be a family of elements of ρ( L ). Let us prove that ⊓ i ∈Δ x i ∈ ρ( L ). We have ⊓ i ∈Δ x i ⊑ x j so ρ( ⊓ i ∈Δ x i ) ⊑ ρ( x j )  = x j because ρ is increasing , x j ∈ ρ( L ), and idempotence . By definition of glb , ρ( ⊓ i ∈Δ x i ) ⊑ ⊓ j ∈Δ x j . Moreover , ⊓ j ∈Δ x j ⊑ ρ( ⊓ i ∈Δ x i ) because ρ is extensive and therefore ρ( ⊓ i ∈Δ x i ) = ⊓ i ∈Δ x i by antisymmetry , proving that ⊓ i ∈Δ x i ∈ ρ( L ) so that ⊓ is the glb in ⟨ L , ⊑⟩ . For the lub , let ⟨ x i , i ∈ Δ ⟩ be a family of elements of ρ( L ). We have x i = ρ( x i ) ⊑ ρ( ⊔ i ∈Δ x i ) by x i ∈ ρ( L ), definition of the lub ⊔ , and ρ increasing , proving that ρ( ⊔ i ∈Δ x i ) ∈ ρ( L ) is an upper bound of the ⟨ x i , i ∈ Δ ⟩ . Let u ∈ ρ( L ) be another one . We have x i ⊑ u and so ⊔ i ∈Δ x i ⊑ u that implies ρ( ⊔ i ∈Δ x i ) ⊑ ρ( u )  = u , proving that ρ( ⊔ i ∈Δ x i ) is smaller than any other upper bound of the ⟨ x i , i ∈ Δ ⟩ , hence their lub .

## 11.16 Moore Families

By theorem 11.88, the image of a complete lattice by a closure operator is closed by arbitrary meets . A subset ℳ ∈ ℘( 𝒫 ) of a poset ⟨𝒫 , ⊑⟩ that is closed by arbitrary meets ( i . e .,  ∀ S ∈ ℳ . ⊓ S exists in ⟨𝒫 , ⊑⟩ and ⊓ S ∈ ℳ ) is called a Moore family ( after [713]). So , by the dual of exercise 10.7, a Moore family ⟨ℳ , ⊑⟩ is a complete lattice

( which includes the supremum ⊤ = ⊓ ∅ of the poset ⟨𝒫 , ⊑⟩ for the meet of the empty set ).

Reciprocally , a Moore family of a complete lattice uniquely defines a closure operator ( exercise 11.89), that is to say , an abstraction . Hence an abstraction can be uniquely defined by choosing an arbitrary subset of the concrete properties and then completing it to a Moore family by adding missing meets ( including the supremum ).

Exercise 11.89 ( Moore family [712, Th . 5.3]) Let ⟨ L , ⊑ , ⊥, ⊤ , ⊔ , ⊓⟩ be a complete lattice and M ∈ ℘( L ). Then there exists an upper closure operator on L such that ρ( L )  = M if and only if M is a Moore family . Then ρ( x ) = ⊓ { y ∈ M | x ⊑ M }.

The following theorem 11.90 shows that all possible abstractions by an upper closure operator ( or Galois retractions ) of a given collecting semantics ( that is a complete lattice ) form a complete lattice called 'the hierarchy of abstractions . ' Part of this complete lattice of abstractions is illustrated in section 8.11.

Theorem 11.90  ( Ward's theorem on upper closure operators [964]) Let ⟨ L , ⊑ ,  ⊥, ⊤ , ⊔ , ⊓⟩ be a complete lattice . Let Uco ( L ) be the set of all upper closure operators on L . ⟨ Uco ( L ), , x x , x ⊤ , R uco ( R ), ⟩ is a complete lattice ( where uco ( f ) x = lfp ⊑ y x ⊔ f ( y ) for f ∈ L L increasing ). A dual theorem holds for the lower closure operators Lco ( L ) on L .

Proof of theorem 11.90 By exercise 10.11, the set ⟨ L L , ⊑ , x ⊥, x ⊤ , , ⟩ of increasing functions on L ordered pointwise is a complete lattice . By theorem 11.87, uco () maps any f ∈ L L to an upper closure operator uco ( f ) ∈ Uco ( L ). Any ρ ∈ Uco ( L ) is increasing so ρ ∈ L L with uco (ρ) = ρ by theorem 11.87. It follows that Uco ( L ) is the image of L L by the closure operator uco . It follows by theorem 11.88 that ⟨ Uco ( L ) = uco ( L L ), , uco ( x ⊥), x ⊤ , X uco ( X ), ⟩ is a complete lattice with uco ( x ⊥) = x ⊓ { y ∈ L | x ⊔ ⊥ ⊑ y } = x x .

More results on closure operators , Moore families , and equivalent formalizations of abstraction are given in [221, ch . 4] and [241].

## 11.17 Conclusion

We can represent abstract program properties by posets and , in case of existence of a best abstraction , establish the correspondence with the concrete properties using a Galois connection . The concrete order structure is preserved in the abstract and inversely . Otherwise stated , concrete and abstract implications coincide up to the Galois connection . Hence proofs in the abstract domain ⟨𝒜 , ≼⟩ using the abstract implication / order ≼ are valid in the concrete ⟨𝒞 , ⊑⟩ for ⊑ , up to this Galois connection .

The original definition of Galois correspondences originating from the work of Evarist Galois [388] were between powersets and decreasing ⟨ ℘( C ), ⊆ ⟩ ⟨ ℘( A ), ⊇ ⟩ so they do not compose as their semidual Galois connections . The order-theoretical Galois connection is credited to Oystein Ore [762]  ( spelled connexion ). Galois connections have numerous applications in mathematics [309], including number theory [609], modal logic [344], fuzzy logic [159,  949], fuzzy sets [993], μ -calculus [132], topology [19], metric spaces [154], formal concept analysis [394, 600], computability [146], constraint satisfaction problems [382, 383], entropy in thermodynamics [607], and others . Galois connections [492, 554] and closure operators [167] have been generalized in category theory . One can also study pairs of functions ⟨ α, γ ⟩ with α increasing / decreasing , γ increasing / decreasing , γ ˚ α which is extensive / reductive , and α ˚ γ which is reductive / extensive ; Galois connections being for the fi rst choice [106, 281, 341, 364, 680].

The results on Galois connections apply to preorders ( reflexive and transitive ) when partially ordered up to the equivalence x ≡ ⊑ y ≜ ( x ⊑ y ∧ y ⊑ x ), in which case equalities must be replaced by the equivalence ≡ ⊑ .

Abstract interpretation with best abstraction has many equivalent formalizations equivalent to Galois connections [241]. For example , Moore families ( exercise 11.89), closure operators ( exercise 11.61), covers ( exercise 11.10), logical relations [828], and soundness relations [738]. The advantage of Galois connections is that the abstraction α is explicit ( and useful in discussing completeness ) and abstract properties may be different from the concrete properties .

Logical relations are mathematically equivalent to Galois connections ( section 11.14) and so can be used to establish the soundness of verification methods , static analyses , and types [738, 828].

Completeness involves considering the best abstraction given in section 11.12. By (11.84), this best abstraction involves considering all possible overapproximations specified by the logical relation , which is impractical ( a point made in [249] and misinterpreted in [60], in which completeness is not considered ). This is also the problem with completeness whenever considering only a concretization function , using lemma 11.42 to determine the best abstraction ( e . g .,  [546] provides no completeness proof of Hoare logic ). This situation is further studied in [245].

The combinations of Galois connections in section 11.13 can be extended to a Galois connection calculus [264] to build complex Galois connections out of basic ones . As shown in the following chapters , a proof method or a static analysis is uniquely defined by a program semantics and a Galois connection .

## 11.18 Solutions to Selected Exercises

Solution to exercise 11.1 Define γ n ( x ) = x + n so that α n ( x ) ≤ y ⇔ x -n ≤ y ⇔ x ≤ y + n ⇔ γ n ( x ) ≤ y . Moreover , α n is bijective .

## Solution to exercise 11.5

## Solution to exercise 11.6

Solution to exercise 11.7 (⇒) Define μ( y ) ≜ γ f ({ y }) so that x ∈ μ( y ) ⇔ x ∈ γ f ({ y })  ⇔ x ∈{ x ʹ | f ( x ʹ)  ∈{ x }}⇔ x = f ( y ). Conversely (⇐), define γ f ( Y ) ≜⋃ y ∈ Y μ( y ) so that X ⊆ γ f ( Y ) ⇔ X ⊆ ⋃ y ∈ Y μ( y ) ⇔ ∀ x ∈ X . ∃ y ∈ Y : x ∈ μ( y ) ⇔∀ x ∈ X . ∃ y ∈ Y : f ( x ) = y ⇔∀ x ∈ X . f ( x ) ∈ Y ⇔α f ( X ) ⊆ Y .

Solution to exercise 11.9 Define γ ⊆ ( b ) ≜ .

Solution to exercise 11.13 We can define the Galois retraction ⟨ Π i ∈Δ ℘( B i ), , ⊆ ⟩ by α P πΔ (Π i ∈Δ X i ) = { i ∈ Δ | X i ≠ ∅} such that α Δ = α πΔ ˚ α π .

Solution to exercise 11.15 We have ⟨ ℘( ℝ → ℝ ), where

and | g |, , and min are pointwise

.

Conversely ,

Solution to exercise 11.32 That is a partial order on D D follows directly from the hypothesis that ⟨ D , ⊑⟩ is a poset . Define because

That is a pointwise lub in D D for follows directly from the fact that ⊔ is a lub in D for ⊑ . By exercise 10.7, ⟨ D D , , ⟩ is a complete lattice . = x ⊥ ∈ D D and = x ⊤ ∈ D D are the infimum and supremum for .

Solution to exercise 11.34 In a Galois connection ⟨𝒞 , ⊑⟩ $ ⟨𝒜 , ≼⟩ , we have

Solution to exercise 11.37 By α ∈ ℕ → { }, we have ∀ n ∈ ℕ .α( n ) = . By γ ∈{ } → ℕ , we have γ( ) = n for some n ∈ ℕ . Then γ(α( n + 1))

= n n + 1, in contradiction to γ ˚ α is extensive in exercise 11.35. A fi x is to consider ℕ ∪{∞} with γ( ) = ∞.

## Solution to exercise 11.39

Solution to exercise 11.40 γ does not preserve meets .

Solution to exercise 11.41 γ preserves fi nite meets but not infinite ones .

Solution to exercise 11.52 For R ∈ ℘( 𝒟 × 𝒞 ), we let α( R ) ≜ x ∈ 𝒟 { y ∈ 𝒞 | ⟨ x , y ⟩ ∈ R }, and for f ∈ 𝒟 → ℘( 𝒞 ), we let γ( f ) ≜ { ⟨ x , y ⟩ | x ∈ 𝒟 ∧ y ∈ f ( x )}.

Solution to exercise 11.53 γ( P ) x ≜⊓ { y ∈ P | x ⊑ y }.

Solution to exercise 11.57 By exercise 11.35 (1) and (2), α and γ are increasing so their composition γ ˚ α is increasing . By exercise 11.45, γ ˚ α ˚ γ = γ so γ ˚ α ˚ γ ˚ α = γ ˚ α proving idempotence . By reflexivity α( x ) ≼ α( x ) so x ⊑ γ ˚ α( x ) by definition 11.1, proving extensivity . By duality , α ˚ γ is a lower closure operator .

Solution to exercise 11.64 By exercise 11.61 and and lemma 11.38, ρ( ℒ ) has arbitrary joins and a supremum , hence by exercise 10.7, it has arbitrary meets , so is a complete lattice .

Solution to exercise 11.89 We have ∀ y ∈{ y ∈ M | x ⊑ y } . x ⊑ y so x is a lower bound of { y ∈ M | x ⊑ y } hence less than or equal to the greatest lower bound ρ( x ), proving that ρ is extensive because x ⊑ ρ( x ).

If x ⊑ x ʹ then x ʹ ⊑ y implies x ⊑ y so { y ∈ M | x ʹ ⊑ y }⊆{ y ∈ M | x ⊑ y } proving ρ( x )  = ⊓ { y ∈ M | x ⊑ y } ⊑ ⊓ { y ∈ M | x ʹ ⊑ y } = ρ( x ʹ) by definition of the glb , proving ρ to be increasing .

Because x ⊑ ρ( x ), ρ( x ) ⊑ ρ(ρ( x )). Inversely , by reflexivity , ρ( x ) ∈{ y ∈ M | ρ( x ) ⊑ y } so by definition of the glb , ρ(ρ( x )) = ⊓ { y ∈ M | ρ( x ) ⊑ y } ⊑ ρ( x ). By antisymmetry , ρ( x ) = ρ(ρ( x )) so ρ is idempotent .

ρ being extensive , increasing and idempotent is an upper closure operator on L .

For all x ∈ L , we have ρ( x ) = ⊓ { y ∈ M | x ⊑ y } ∈ M because the y ∈ M and M is a Moore family closed by ⊓ . So ρ( L ) ⊆ M . If x ∈ M then x ∈ L and x ∈{ y ∈ M | x ⊑ y } so x = ⊓ { y ∈ M | x ⊑ y } = ρ( x ) proving M ⊆ ρ( L ). By antisymmetry , ρ( L ) = M .

Notice that M is closed by arbitrary meets so ⊓ ∅ ∈ M ⊆ L and ⊓ ∅ is a supremum for ⊑ so L has a supremum ( which also belongs to M ). Moreover , ⊓ M is the infimum of M . So , as shown in section 10.6, ⟨ M , ⊑ , ⊓ M , ⊓ ∅, ⊓⟩ is a dual complete lattice , which by exercise 10.7 has a lub ⊔ and so is a complete lattice . Notice that the join in M is in general not the join in L . If the join ∨ X exists in L , then by exercise 11.61 and join preservation in Galois connections , ⊔ ( X ) = ρ(∨ X ) in M . Here is an example .

<!-- image -->

- 1 We call this abstraction 'homomorphic' because it is a structure-preserving map ( homomorphic / partitioning abstractions of sets are sets , of joins are joins , of meets are meets , of functions are functions , of relations are relations , etc .).

2 Exercise 11.8 is the basis for formal concept analysis [335,  393,  394] to classify data symbolically . C is a set of studied objects , A is a set of descriptions h ( x ) ∈ A of objects x ∈ C , and d ⊑ d ʹ means that d ʹ is more general than d . The pairs ⟨ c , d ⟩ s . t . c = γ( d ) and d = α( c ) are called conceptual classes and , ordered componentwise , form a complete lattice .

3 We use this terminology by reference to a retraction in topology , which is a continuous mapping from a topological space into a subspace that preserves the position of all points in that subspace . In particular , given any idempotent continuous map , a retraction onto the image of the map is obtained by restricting the codomain ; see exercise 11.51

A similar terminology is used in category theory . If α ∈ 𝒞 → 𝒜 , γ ∈ 𝒜 → 𝒞 , and γ ˚ α ∈ 𝒞 → 𝒞 then α is called a section of γ and γ is a retraction of α [614, p . 19].

4 More generally in chapter 21, the collecting semantics ⟨ ℘(℘( 𝕋 + × 𝕋 +∞ )),  ⊆ ⟩ is a complete lattice , so its abstractions ⟨ ρ(℘(℘( 𝕋 +  × 𝕋 +∞ ))),  ⊆ ⟩ by upper closure operators ( or Galois retractions ) ρ on program properties ℘(℘( 𝕋 + × 𝕋 +∞ )) are also complete lattices .