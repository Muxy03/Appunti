<!-- image -->

## A Correctness and Incorrectness Program Logic

ROBERTO BRUNI, University of Pisa, Italy

ROBERTO GIACOBAZZI, University of Verona, Italy

ROBERTA GORI, University of Pisa, Italy

FRANCESCO RANZATO, University of Padova, Italy

Abstract interpretation is a well-known and extensively used method to extract over-approximate program invariants by a sound program analysis algorithm. Soundness means that no program errors are lost and it is, in principle, guaranteed by construction. Completeness means that the abstract interpreter reports no false alarms for all possible inputs, but this is extremely rare because it needs a very precise analysis. We introduce a weaker notion of completeness, called local completeness , which requires that no false alarms are produced only relatively to some fixed program inputs. Based on this idea, we introduce a program logic, called Local Completeness Logic for an abstract domain A , for proving both the correctness and incorrectness of program specifications. Our proof system, which is parameterized by an abstract domain A , combines over- and underapproximating reasoning. In a provable triple ⊢ A [ p ] c [ q ], c is a program, q is an under-approximation of the strongest post-condition of c on input p such that their abstractions in A coincide. This means that q is never too coarse, namely, under some mild assumptions, the abstract interpretation of c does not yield false alarms for the input p iff q has no alarm . Therefore, proving ⊢ A [ p ] c [ q ] not only ensures that all the alarms raised in q are true ones, but also that if q does not raise alarms, then c is correct. We also prove that if A is the straightforward abstraction making all program properties equivalent, then our program logic coincides with O'Hearn's incorrectness logic, while for any other abstraction, contrary to the case of incorrectness logic, our logic can also establish program correctness.

CCS Concepts: · Theory of computation → Logic and verification ; Abstraction ; Programming logic ; Semantics and reasoning ; Program analysis ; Hoare logic ; Axiomatic semantics; Abstraction ; Program reasoning;

Additional Key Words and Phrases: Abstract interpretation, abstract domain, program analysis, program verification, program logic, local completeness, best correct approximation, incorrectness logic

## ACMReference format:

Roberto Bruni, Roberto Giacobazzi, Roberta Gori, and Francesco Ranzato. 2023. A Correctness and Incorrectness Program Logic. J. ACM 70, 2, Article 15 (March 2023), 45 pages.

[https://doi.org/10.1145/3582267](https://doi.org/10.1145/3582267)

The authors have been funded by the Italian MIUR , under the PRIN2017 project no. 201784YSZ5 'AnalysiS of PRogram Analyses (ASPRA)' and by a Meta research gift. Roberto Giacobazzi and Francesco Ranzato have been partially funded by Facebook Research , under a 'Probability and Programming Research Award,' by an Amazon Research Award for 'AWS Automated Reasoning,' and by a WhatsApp Research Award on 'Privacy-aware Program Analysis.'

Authors' addresses: R. Bruni and R. Gori, University of Pisa, Pisa, Italy; emails: bruni@di.unipi.it, gori@di.unipi.it; R. Giacobazzi, University of Verona, Verona, Italy; email: roberto.giacobazzi@univr.it; F. Ranzato, University of Padova, Padova, Italy; email: ranzato@math.unipd.it.

Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s).

© 2023 Copyright held by the owner/author(s).

## 1 INTRODUCTION

'The only effective way to raise the confidence level of a program significantly is to give a convincing proof of its correctness' [Dijkstra 1972b]. This statement, given by E. W. Dijkstra in 1972 in his Turing Award lecture [Dijkstra 1972c], is universally valid and nowadays felt as an indispensable necessity and still a major challenge in modern information societies [Hoare 2003; Jones et al. 2006]. The idea of having programs that certify other programs is due to A. M. Turing [Turing 1989] and put forward by McCarthy [1962], Floyd [1967], and Hoare [1969] in the 1960s. The past 50 years have witnessed an incredible flourishing of formal methods and tools for achieving this ambitious goal. These include, among others, certified compilers [Leroy 2006], certified analyzers [Jourdan et al. 2015], advanced type checkers [Pierce 2002], software model checkers [Ball et al. 2005], and abstract interpretation-based methods for static program analysis [Cousot 2021; Cousot and Cousot 1977; Giacobazzi and Ranzato 2022]. Proving program correctness means inferring an adequate invariant that has to be strong enough to imply the desired correctness property for our code. In program correctness proofs, the ambition to automate the inference of a 'good' invariant immediately leads us to the need of some sort of over-approximation, making tractable (e.g., decidable) problems that are otherwise intractable. The well-known and inherent undecidability of all non-straightforward extensional properties of programs provides an intrinsic limitation in the use of approximated and decidable formal methods for proving program properties [Rice 1953] (see also Cousot et al. [2018]). This is particularly clear in program analysis, where the necessary termination of the analysis algorithm may introduce false alarms. The soundness of a program analyser, which is guaranteed by construction in abstract interpretation, means that all true alarms (also called true positives) are caught, but it is often the case that false alarms (also called false positives) are reported. There exists a range of successful applications of formal methods for proving the absence of bugs in programs [Calcagno et al. 2015; Cousot 2021; Distefano et al. 2019; Hoare 1969; O'Hearn 2018; Rival and Yi 2020; Sadowski et al. 2018]. Of course, as in all verification systems, program analysis is credible when few false alarms are reported, ideally none. Completeness holds when no false alarm is ever raised, and this represents in many ways the holy grail of program analysis and verification [Jones et al. 2006].

Understanding whether an alarm corresponds to a true bug, i.e., indirectly whether our approximation method is complete, boils down to the challenge of proving some sort of program incorrectness. The same E. W. Dijkstra asserted in 1972 that 'Program testing can be used to show the presence of bugs, but never to show their absence' [Dijkstra 1972a]. Proving that our program contains a true bug therefore means isolating those states that will eventually trigger the fault, i.e., will make our program violating a correctness assertion. This means propagating along the computation properties of states that are strong enough to isolate those states that will produce a fault. This is the key idea in O'Hearn [2020]'s incorrectness logic (IL) and its subsequent application to separation logic in Raad et al. [2020]. By exploiting under-approximations, any violation exposed by such program analysis corresponds to a true alarm. This makes IL a credible support for code-review and test-driven software development, although a correctness condition can still be violated even when no alarm is reported by the analysis.

The tension between proving the absence of bugs and exhibiting their actual presence shaped the research in programming languages and software engineering for decades. Nevertheless, the problem is far from being solved and static reasoning should be extended to bug catching, rather than only for proving absence of bugs, as advocated by O'Hearn [2020].

## The Problem

In this work, we consider abstract interpretation [Cousot and Cousot 1977] as the reference theory to design and validate algorithms capable to infer over-approximate program invariants. The problem is how to guarantee that the approximation is precise enough to avoid false alarms. Next we explain why completeness is crucial to ensure precision of the analysis and why it is hard to achieve it. The ingredients are as follows: an abstract domain A of abstract program properties, e.g., some properties of stores, which is connected with the concrete domain of program properties C by a pair of monotone functions α : C → A and γ : A → C , respectively the abstraction and concretization map, such that A = α ( C ) and for any concrete property p ∈ C , p ⊆ A ( p ) ≜ γα ( p ) . 1 Program verification by abstract interpretation means that instead of verifying whether the strongest post-condition post [ c ] ( p ) for a program c and a pre-condition p , satisfies a correctness specification spec , we verify whether a sound abstract over-approximation post A [ c ] : A → A satisfies spec . Using denotational semantics symbols, the original verification problem can be stated more concisely as checking if /llbracket c /rrbracket p ⊆ spec holds, while its abstract counterpart becomes the property γ ( /llbracket c /rrbracket ♯ A α ( p )) ⊆ spec , where /llbracket c /rrbracket denotes the strongest post-condition function for c and /llbracket c /rrbracket ♯ A is called the abstract interpretation of c on A .

As observed above, the problem here is that computing /llbracket c /rrbracket ♯ A may degrade the approximation and make the computed abstract program property too weak to imply the desired specification. This may be a consequence of the fact that abstract interpretation analysis is done by composing functions. Consider the abstract interpretation of c on A defined as /llbracket c /rrbracket A ≜ α ◦ /llbracket c /rrbracket ◦ γ , commonly called best correct approximation (bca) of c in A . This is the best possible approximate semantics, namely any abstract interpretation /llbracket c /rrbracket ♯ A is sound if and only if /llbracket c /rrbracket A ⊆ /llbracket c /rrbracket ♯ A [Cousot and Cousot 1979]. It is known that, in general, the composition of two bcas is not necessarily a bca itself. Consider the case of the abstract domain of integer intervals Int whose elements approximate any property p ∈ ℘ ( Z ) of the integer values that a variable x may assume by the least interval Int ( p ) = [ a , b ] such that p ⊆ [ a , b ], where a ≤ b , a ∈ Z ∪ {-∞} and b ∈ Z ∪ { + ∞} and the commands

```
c 1 ≜ if even ( x ) then 0 else 1 and c 2 ≜ if even ( x ) then x else x + 1.
```

In this case, it turns out that /llbracket c 2 /rrbracket Int ( [0 , 1] ) = [0 , 2] and /llbracket c 1 /rrbracket Int ◦ /llbracket c 2 /rrbracket Int ( [0 , 1] ) = /llbracket c 1 /rrbracket Int ( [0 , 2] ) = [0 , 1], while ( /llbracket c 1 /rrbracket ◦ /llbracket c 2 /rrbracket ) Int ( [0 , 1] ) = [0 , 0] and [0 , 0] ⊊ [0 , 1]. The lack of compositionality is the main cause of the interdependence between the precision of an abstract interpretation and the way programs are written [Bruni et al. 2020]. While it is obvious that if /llbracket c /rrbracket ♯ A α ( p ) satisfies spec (i.e., γ ( /llbracket c /rrbracket ♯ A α ( p )) ⊆ spec holds), then the program is correct, it may happen that /llbracket c /rrbracket ♯ A α ( p ) does not satisfy spec even if the program is correct, hence producing a false alarm. In this case, if γ ( /llbracket c /rrbracket ♯ A α ( p )) ⊈ spec , then we cannot conclude that the Hoare triple { p } c { spec } is not valid, because any witness in γ ( /llbracket c /rrbracket ♯ A α ( p )) ∖ spec could be a false alarm .

Complete abstract interpretations, instead, do not raise false alarms. Technically, this also requires the assumption that the specification spec is expressible in A , namely that spec = A ( spec ) holds. For example, the property x ≥ 0 is expressible by the infinite interval [0 , + ∞ ]. By contrast, x /nequal 0 is not expressible in Int , since the least over-approximating interval is Int ( x /nequal 0 ) = Z ⊋ Z ∖ { 0 } . If spec is expressible in A , then completeness guarantees that a Hoare triple { p } c { spec } is valid iff γ ( /llbracket c /rrbracket ♯ A α ( p )) ⊆ spec holds. Thus, any complete abstract verification of spec by means of the (complete) abstract semantics /llbracket c /rrbracket ♯ A is the same as verifying spec with respect to the concrete semantics. Notably, when the abstract interpretation is complete, then /llbracket c /rrbracket ♯ A always coincides with the bca /llbracket c /rrbracket A [Giacobazzi et al. 2000]. According to a well-established definition [Cousot and Cousot

1 Abstract interpretation is more general than this [Cousot and Cousot 1977]. There are weaker abstract interpretation frameworks where only the concretization function is assumed to exist [Cousot and Cousot 1992]. We consider the stronger formulation based on Galois insertions because it is the most widely known and, as observed later, this provides enough mathematical structure to define the key notion of completeness in abstract interpretation.

1977, 1979], completeness is a global notion , meaning that it involves all possible pre-conditions. More precisely, A is complete for a program c when /llbracket c /rrbracket ♯ A ◦ α = α ◦ /llbracket c /rrbracket , namely

<!-- formula-not-decoded -->

This form of completeness is extremely hard to achieve. Giacobazzi et al. [2015] proved that for any non-straightforward abstraction A there always exists a program c for which any sound abstract interpretation of c on A yields at least one false alarm. Later, Bruni et al. [2020] showed that any program equivalence induced by an abstract interpreter built over a non-straightforward abstraction violates extensionality. Here, non-straightforward abstractions correspond to those abstract domains A that are able to distinguish at least two programs, i.e., there exist two programs c 1 and c 2 such that /llbracket c 1 /rrbracket ♯ A /nequal /llbracket c 2 /rrbracket ♯ A , and A does not coincide with the identical abstraction, i.e., /llbracket · /rrbracket ♯ A /nequal /llbracket · /rrbracket . In particular, it is known [Giacobazzi et al. 2015] that the main sources of incompleteness lie in the abstract interpretation of store assignments and Boolean guards. The case of Boolean guards is striking. The semantics of a Boolean guard is a predicate transformer /llbracket b ? /rrbracket : ℘ (Σ) → ℘ (Σ) , where Σ denotes the set of concrete stores. Completeness of a Boolean guard b ? in the abstract domain A means that for all p ∈ ℘ (Σ) , A ( /llbracket b ? /rrbracket p ) = A ( /llbracket b ? /rrbracket A ( p )) . Of course, because both branches of a conditional or loop statement guarded by b must be taken into account, the same condition applies to the negative test ¬ b ?. For example, Int is complete for a simple rectifier program, known as ReLU in neural networks,

<!-- formula-not-decoded -->

even if its Boolean guards are not complete in Int . In fact, for the pre-condition p ≜ x ∈{-1 , 1 } , we have that

<!-- formula-not-decoded -->

meaning that Int is not complete for the guard x ≥ 0?. This happens even if both guards x &lt; 0? and x ≥ 0? are expressible in Int as x ∈ [ -∞ , -1] and x ∈ [0 , + ∞ ], respectively. However, Int is instead trivially complete for both commands x : = 0 and skip of ReLU . Hence, it is the lack of completeness of the abstract interpretation of the two guards x &lt; 0? and x ≥ 0? that prevents us to inductively prove completeness for the simple program ReLU . Abstraction refinement does not help either. The complete shell of Int , as described in Giacobazzi et al. [1998, 2000], for the guards x &lt; 0? and x ≥ 0? blows up to nearly the concrete domain of all program stores. In fact, we should refine the interval abstraction by adding denotations that describe any pair of intervals ( I 1 , I 2 ) such that I 1 ∩ I 2 = ∅ and I 1 ∪ I 2 is not an interval where I 1 ⊆ Z &lt; 0 and I 2 ⊆ Z ≥ 0. This would give us a complete abstract domain for x &lt; 0? and x ≥ 0? that is barely equivalent to the concrete domain and therefore useless for a practical program verification.

## Roadmap to Main Contributions

The main theme of the article is to combine under- and over-approximations via abstract interpretation and the novel notion of local completeness to define a program logic whose triples either prove correctness or incorrectness.

After some background on abstract interpretation in Section 2, in Section 3 we give necessary and sufficient conditions that guarantee completeness of Boolean guards on an abstract domain A . These conditions require that both b ? and ¬ b ? are expressible in the abstract domain and the same has to apply to the join of any two concretizations of abstract points below α ( /llbracket b ? /rrbracket ) and α ( /llbracket ¬ b ? /rrbracket ) . This requirement turns out to be very strong: For example, this condition allows us to prove that any Boolean guard on the interval abstraction Int is incomplete (cf. Example 3.7).

Since completeness is rare, in Section 4 we introduce locally complete abstract interpretations , a natural weakening of completeness. Instead of requiring completeness on all possible inputs, a locally complete abstract interpretation is complete just for some given subset of possible inputs. In the case of a guard b ? with input p , local completeness amounts to checking whether /llbracket b ? /rrbracket ♯ A α ( p ) = α ( /llbracket b ? /rrbracket p ) holds for that particular p ∈ C . For example, any guard is locally complete for any input p that is expressible in the abstract domain. In our example of ReLU , it is easy to check that when the input is any interval or any set of integers all having the same sign, e.g., either all nonnegative or all negative, then both guards x &lt; 0? and x ≥ 0? turn out to be locally complete in Int , so that we can inductively infer that ReLU is locally complete in Int with respect to any such input.

By means of local completeness we can prove the absence of false alarms for programs that are globally incomplete on a given abstract domain. As a simple example, consider the following program AbsVal for computing the absolute value of integer variables:

<!-- formula-not-decoded -->

AbsVal is globally incomplete on the abstract domain Int . For instance, for a pre-condition p ≜ x ∈ {-7 , 7 } , we have that Int ( /llbracket AbsVal /rrbracket p ) = [7 , 7] while Int ( /llbracket AbsVal /rrbracket Int ( p )) = Int ( /llbracket AbsVal /rrbracket [ -7 , 7] ) = [0 , 7]. Therefore, even if the pre-condition p does not include zero, an interval analysis of AbsVal yields a false alarm when checking the expressible specification spec ≜ x &gt; 0. Similarly to ReLU , this is not the case when the inputs all have the same sign, no matter if positive or negative. Instead, a true alarm for spec can be raised only if the set of input values truly contains zero. This means that to use AbsVal in our code and not having false alarms in an interval analysis, e.g., within a loop, we need to make sure that AbsVal ( x ) will be called with x always having the same sign.

Our main contribution is in Section 5, where we present a logical proof system ⊢ A called Local Completeness Logic on A (LCL A ) for locally complete abstract interpretations parameterized on an arbitrary abstract domain A . Our assertions are Hoare-like triples ⊢ A [ p ] c [ q ] establishing that

- (i) q is an under-approximation of post [ c ] p (i.e., of /llbracket c /rrbracket p );
- (ii) post [ c ] is locally complete for input p on A ;
- (iii) q and post [ c ] p have the same over-approximation in A .

These properties of any provable triple ⊢ A [ p ] c [ q ] allow us to distinguish between true and false alarms raised by an abstract interpreter /llbracket c /rrbracket ♯ A α ( p ) for verifying any correctness specification spec that is expressible in A . The key rules in LCL A are as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The rule ( transfer ) checks that a basic expression e , such as a Boolean test b ? or an assignment x : = a is locally complete for p before inferring the output of post [ e ] on p as post-condition. The consequence rule ( relax ) is the key principle of LCL A and combines an over- and under-approximating reasoning: ( relax ) allows us to infer a post-condition that defines an under-approximation q of the exact behavior as well as a sound over-approximation A ( q ) of it, i.e., such that q ⇒ post [ c ] ( p ) ⇒ A ( post [ c ] ( p )) = A ( q ) holds. Likewise, in the consequence rules of the reverse Hoare logic by de Vries and Koutavas [2011], incorrectness logic by O'Hearn [2020], and incorrectness separation logic by Raad et al. [2020], the logical ordering between pre-conditions p ′ ⇒ p and post-conditions q ⇒ q ′ in the premises of ( relax ) is reversed w.r.t. the canonical consequence rule of classical Hoare logic, and this is needed because our post-conditions q are always underapproximations.

Fig. 1. Relation among LCL A , O'Hearn's Incorrectness Logic and Hoare's partial correctness logic.

<!-- image -->

The key feature of ( relax ) is to constrain the under-approximating post-condition q to have the same abstraction as the strongest post-condition, which is needed for preserving local completeness. This twist is fundamental to guarantee that any triple derivable in LCL A either proves correctness or incorrectness. Figure 1 illustrates the relations between different proof systems. On the left, it is shown that Hoare logic for correctness derives any over-approximation of post [ c ] ( p ) (i.e., any provable triple { p } c { q } is such that q belongs to the blue dotted upper diamond region) while O'Hearn logic for incorrectness is able to derive any under-approximation of post [ c ] ( p ) (i.e, any provable triple ⊢ IL [ p ] c [ q ] is such that q belongs to the blue dotted lower diamond region). On the right, we show the interplay between approximations derived using locally complete abstract interpretation A (the red bordered region, comprising any q such that A ( q ) = A ( post [ c ] p ) ) and LCL A under-approximations (i.e., any provable triple ⊢ A [ p ] c [ q ] is such that q belongs to the red-filled region, still with A ( q ) = A ( post [ c ] p ) ). We show that by the ( relax ) rule we can shrink the post-condition of any triples, up to some boundary that fringes the assertions of O'Hearn logic. This is made without much loss of precision: Under mild conditions on spec , any approximation q in the red-filled region guarantees that if the over-approximation A ( q ) reports some alarm, then q contains a true alarm and, conversely, any alarm in q is a true one. The key point is that any derivable triple ⊢ A [ p ] c [ q ] of LCL A provides an under-approximation q that is not too coarse. More precisely, given a correctness specification spec expressible in A , the following two scenarios can occur:

- (a) spec is satisfied: Abstract interpretation in A , as well as any triple ⊢ A [ p ] c [ q ] derivable in LCL A , allow to conclude that spec holds. This is not true in Hoare logic: Although { p } c { spec } is a valid triple, since post-conditions in Hoare triples can always be weakened, it is also possible to derive some triple { p } c { q } whose post-condition q includes some false alarm. Using IL, no true alarm can be found and no conclusion can be drawn about the validity of spec .
- (b) spec is violated: Since spec is expressible in A , then any derivable triple ⊢ A [ p ] c [ q ] of LCL A will expose a true alarm witnessing that spec is violated. On the contrary, abstract interpretation in A , as well as Hoare logic, can also expose false alarms that cannot be distinguished

from true ones. In IL, although it is possible to derive triples ⊢ IL [ p ] c [ q ] where q exhibits some (true) alarms, since post-conditions can always be strengthened, other triples for p and c may have no alarm at all, e.g., ⊢ IL [ p ] c [ff].

We prove in Theorem 5.5 that LCL A is sound with respect to the above properties (i)-(iii). To prove a result of logical completeness 2 of LCL A for a program c , we add two more ingredients:

- (1) as in incorrectness logic [O'Hearn 2020], an infinitary rule ( limit ) for iteration; and
- (2) the assumption that all the basic instructions occurring in the program c of a provable triple ⊢ A [ p ] c [ q ] are globally complete on A .

In Section 6, we show that IL coincides with LCL A when the straightforward abstraction A tr that is unable to distinguish any two programs is considered. In fact A tr is globally complete for every transfer function, hence for every program, and therefore the premises of the rule ( transfer ) are always satisfied. We also prove that A tr is the only abstraction A for which the proof system LCL A can be logically complete for a Turing complete programming language.

In Section 7, we observe that for iterative commands guarded by a Boolean guard b ?, e.g., in while loops, it is not necessary to require the proof obligations of local completeness for b ? at every iteration provided that local completeness is met when the loop invariant is reached. Therefore, to improve the expressiveness of the logical system in handling while programs, we introduce two additional sound rules that are specific to while loops.

In Section 8, we consider the possibility of refining the abstract domain to complete the proof when some proof obligations of local completeness are not met by the current abstraction. Proving a triple ⊢ A [ p ] c [ q ] in a refined domain can no longer guarantee the local completeness of /llbracket c /rrbracket ♯ A on input p , but we can still prove the local completeness of the best correct approximation /llbracket c /rrbracket A so that /llbracket c /rrbracket A α ( p ) = α ( /llbracket c /rrbracket p ) = α ( q ) holds. From the viewpoint of program verification w.r.t. a correctness specification spec that is expressible in A , this means that we retain all the potential of LCL A for finding bugs (i.e., any element in q \ spec ) or proving correctness (when q ⊆ spec holds) even if the abstract interpretation /llbracket c /rrbracket ♯ A α ( p ) is not as precise as the bca /llbracket c /rrbracket A α ( p ) .

Finally, Section 9 discusses some related work, and Section 10 concludes by outlining some directions of future work expanding the ideas of this article.

This article is a full and revised version of the LICS 2021 paper [Bruni et al. 2021], extended to include all the technical proofs, further examples, and some entirely novel contributions reported in Section 4.1 concerning a local completeness characterization for Boolean guards, Section 7 concerning a relaxation of local completeness requirements for while loops, and Section 8 concerning a program logic for best correct approximations.

## 2 BACKGROUND

As a matter of notation, given two sets X and Y , X ∖ Y denotes the set-difference between X and Y , while X ⊊ Y denotes strict inclusion. Given two functions f : X → Y and д : Y → Z , we denote with д ◦ f , or simply дf , their composition. For f : X → X and n ∈ N , we let f n : X → X be defined inductively as usual: f 0 ≜ id X and f n + 1 ≜ f ◦ f n , where id X denotes the identity function on X (often abbreviated id ).

In ordered structures such as posets and complete lattices over a set of elements C , we typically use ≤ C to denote a partial order relation, ∨ C for least upper bound (lub), ∧ C for greatest lower bound (glb), ⊤ C and ⊥ C for, respectively, greatest and least elements. We use ℘ ( X ) to denote the powerset complete lattice over a set X ordered by inclusion. If f : X → Y , then f is overloaded to denote its powerset lifting f : ℘ ( X ) → ℘ ( Y ) , where f ( S ) ≜ { f ( x ) | x ∈ S } . If C is a complete lattice and X ⊆ C , then the Moore closure of X is defined as M ( X ) ≜ {∧ C Y | Y ⊆ X } , that is, M ( X ) is the least superset of X closed under glbs of its subsets (also called Moore closed); in particular, notice that X ⊆ M ( X ) and ∧ C ∅ = ⊤ C ∈ M ( X ) . If C is a poset and l , u ∈ C , then [ l , u ] ≜ { x ∈ C | l ≤ C x ≤ C u } denotes the segment between l and u in C . For f , д : C 1 → C 2 between posets, f ≤ д denotes that for all x ∈ C 1, f ( x ) ≤ C 2 д ( x ) , while f is monotone when x ≤ C 1 y implies f ( x ) ≤ C 2 f ( y ) . A function f between complete lattices is additive (respectively co-additive) when f preserves arbitrary lubs (respectively, glbs). The least fixpoint of a function f : C → C on a poset C is denoted, when it exists, by lfp ( f ) . Let us recall that if f is (Scott) continuous on a complete lattice then lfp ( f ) = ∨ C { f n ( ⊥ ) | n ∈ N } .

2 The term logical is used here to distinguish the standard notion of completeness for a proof system from the notion of completeness in abstract interpretation.

## 2.1 Abstract Interpretation

2.1.1 Abstract Domains. If the concrete semantics of our programming language is specified on a given concrete domain of properties C , then abstract interpretation [Cousot 2021; Cousot and Cousot 1977] is the method to specify abstract semantics, namely approximate semantics defined on an abstract domain of approximate program properties A . Concrete and abstract domains are typically complete lattices. This guarantees the existence of the basic lattice operators of join and meet used in the definition of concrete and abstract semantics. Since several abstractions are possible, we use subscripts such as ≤ A and ∨ A to disambiguate the underlying carrier set A and omit the subscripts in the case of C . Given complete lattices C and A , a pair of functions α : C → A and γ : A → C forms a Galois connection (GC, a special case of an adjunction) when for all c ∈ C , a ∈ A , α ( c ) ≤ A a ⇔ c ≤ γ ( a ) holds. In a GC the lattices C and A are called, respectively, concrete and abstract domain, and α and γ are called, respectively, abstraction and concretization maps. We only consider GCs such that αγ = id A , called Galois insertions (GIs), where α is surjective and γ is injective. Let us recall that α is additive, γ is co-additive, and γα is an (upper) closure operator, that is, γα : C → C is a monotone, idempotent and extensive (i.e., id C ≤ C γα holds) function, and γ ( A ) ⊆ C is Moore closed. Moreover, if X ⊆ C is Moore closed, then X can be viewed as an abstraction of C through the maps α = λc . ∧ C { x ∈ X | c ≤ C x } and γ = id X . The class of abstract domains of C is given by Abs ( C ) ≜ {〈 A , ≤ A , α , γ 〉 | α : C → A , γ : A → C is a GI } , and we write A α , γ ∈ Abs ( C ) to mean that A is an abstract domain related to C by the abstraction and concretization maps α and γ . When convenient, we simply use A in place of the function γα : C → C , e.g., Int ( {-7 , 7 } ) = [ -7 , 7]. For example, since γ is injective, a condition such as α ( c ) ≤ A α ( d ) can be written as (and is equivalent to) A ( c ) ≤ A ( d ) . An abstract domain A α , γ ∈ Abs ( C ) is called strict when γ ( ⊥ A ) = ⊥ , and a concrete value c ∈ C is expressible in A when A ( c ) = c , while if c &lt; A ( c ) holds, then c is (strictly) approximated in A . Notice that γ ( A ) and C ∖ γ ( A ) are the sets of concrete values that are, respectively, expressible and approximated in A . Given two abstract domains A α A , γ A , B α B , γ B ∈ Abs ( C ) , B is a refinement of A , denoted by B ⪯ A , when γ A ( A ) ⊆ γ B ( B ) holds, i.e., when B is at least as expressive as A . An abstract domain A α , γ ∈ Abs ( C ) is trivial if either (a) γα = id C holds, i.e., all the concrete values are expressible in A or (b) γα = λx . ⊤ C holds, i.e., A is a singleton domain that can express the greatest element ⊤ C only. A is called the identity abstraction in the case (a) and the top abstraction in the case (b).

2.1.2 Correctness. Given an abstract domain A α , γ ∈ Abs ( C ) and a concrete operation f : C → C (a generalization to n -ary functions of type C n → C can be easily done pointwise), an abstract function f ♯ : A → A is a correct (or sound ) approximation (or abstract interpretation) of f when α f ≤ f ♯ α holds. It is known that if f ♯ is a correct approximation of f , then we also have fi xpoint correctness when least fixpoints exist, i.e., α ( lfp ( f )) ≤ lfp ( f ♯ ) holds. The bca of f in A is defined as the abstract function f A ≜ α f γ : A → A . The term 'best correct approximation' is justified by the well-known fact [Cousot and Cousot 1979] that an abstract function f ♯ : A → A is a correct approximation of f iff f A ≤ f ♯ holds, so that f A is the most precise, w.r.t. the pointwise ordering ≤ A , among the correct approximations of f on A .

2.1.3 Completeness. The abstract function f ♯ is a complete approximation of f (or just complete) if α f = f ♯ α holds. The abstract domain A is called a complete abstraction for f if there exists a complete approximation f ♯ : A → A of f on the abstract domain A . Completeness intuitively encodes the greatest possible precision for an abstract function f ♯ defined on A , meaning that the abstract behaviour of f ♯ on A , i.e., f ♯ α , exactly matches the abstraction in A of the concrete behaviour of f , i.e., α f . In a complete approximation f ♯ the only loss of precision is due to the abstract domain and not to the definition of the abstract function itself. Analogously to soundness, completeness transfers to fixpoints, meaning that if f ♯ is complete for f , then fi xpoint completeness α ( lfp ( f )) = lfp ( f ♯ ) holds. It turns out that there exists an abstract function f ♯ : A → A such that completeness α f = f ♯ α holds iff α f = α f γ α iff ( γα ) f = ( γα ) f ( γα ) iff Af = Af A iff γα f = γ f A α . Hence, the chance of defining a complete approximation f ♯ of f on some abstract domain A only depends upon the bca f A of f in A , i.e., completeness is a property of the abstract domain only. Moreover, let us observe that any trivial abstract domain is always complete for any f . In the following, we say both ' A is complete for f ' and ' f is complete on A , ' and we write C A ( f ) to denote that A is complete for f :

<!-- formula-not-decoded -->

## 2.2 Regular Commands

Following O'Hearn [2020] for incorrectness logic, we consider a language of regular commands :

<!-- formula-not-decoded -->

which is general enough to cover deterministic imperative languages as well as other programming paradigms that include, e.g., nondeterministic and probabilistic computations. The language is parametric on the syntax of basic expressions e ∈ Exp , which provide the basic commands and can be instantiated with different kinds of instructions such as (nondeterministic or parallel) assignments, (Boolean) guards or assumptions, error generation primitives, local variable primitives, and so on. The term r 1; r 2 represents sequential composition, the term r 1 ⊕ r 2 represents a nondeterministic choice command, and the term r ∗ is the Kleene iteration of r where r can be executed 0 or any finite number of times. As a shorthand, we write r n for the sequence r ; . . . ; r of n instances of r and let Exp ( r ) denote the set of basic expressions occurring in r ∈ Reg .

2.2.1 Concrete Semantics. We assume that basic expressions have a semantics /llparenthesis · /rrparenthesis : Exp → C → C on a complete lattice C such that /llparenthesis e /rrparenthesis is an additive function. This assumption can be done w.l.o.g. in Hoare-like (or collecting) program semantics, since their basic functions are always defined by an additive lifting. The concrete semantics /llbracket · /rrbracket : Reg → C → C of regular commands is inductively defined as follows:

<!-- formula-not-decoded -->

2.2.2 Abstract Semantics. The abstract semantics /llbracket · /rrbracket ♯ A : Reg → A → A of regular commands on an abstract domain A α , γ ∈ Abs ( C ) is inductively defined as follows:

<!-- formula-not-decoded -->

where it is worth emphasizing that as abstract semantics /llbracket e /rrbracket ♯ A of basic expressions we consider their bcas on A , namely /llbracket e /rrbracket A ≜ α ◦ /llbracket e /rrbracket ◦ γ , i.e., we assume that no additional loss of precision is due to their interpretation. It is easy to check by structural induction that the abstract semantics in Equation (3) is monotonic (provided that /llbracket e /rrbracket are monotone functions) and correct, i.e.,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Let us remark that Equation (3) is the standard definition by structural induction of abstract semantics used in abstract interpretation, adapted to the language of regular commands. Therefore, it turns out that the abstract semantics of the choice command preserves bcas, namely

<!-- formula-not-decoded -->

As observed above in Section 1, this property of preserving bcas, in general, does not hold for sequential composition and Kleene iteration: For example, /llbracket r 2 /rrbracket A ◦ /llbracket r 1 /rrbracket A is not guaranteed to be the bca /llbracket r 1; r 2 /rrbracket A . However, it can be easily seen, by structural induction, that all the definitions in Equation (3) preserve the property of being complete, meaning that if /llbracket r 1 /rrbracket ♯ A , /llbracket r 2 /rrbracket ♯ A , /llbracket r /rrbracket ♯ A are complete, then /llbracket r 1; r 2 /rrbracket ♯ A , /llbracket r 1 ⊕ r 2 /rrbracket ♯ A and /llbracket r ∗ /rrbracket ♯ A are complete as well. In the following, as a shorthand, we write C A ( r ) instead of C A ( /llbracket r /rrbracket ) to denote that A is complete for /llbracket r /rrbracket .

In our proofs, we will exploit some standard properties of abstract and concrete semantics, as summarized by the following lemma.

Lemma 2.1. Let A α , γ ∈ Abs ( C ) . For all r ∈ Reg and c , d ∈ C :

- (a) /llbracket r /rrbracket A α ( c ) ≤ A /llbracket r /rrbracket ♯ A α ( c ) ;
- (c) /llbracket r /rrbracket ♯ A α ( c ) ≤ A α ( c ) ⇒ /llbracket r ∗ /rrbracket ♯ A α ( c ) = α ( c ) ;
- (b) /llbracket r /rrbracket ♯ A α ( c ) = α ( /llbracket r /rrbracket c ) ⇒ α ( /llbracket r /rrbracket c ) = α ( /llbracket r /rrbracket γα ( c )) ;
- (d) /llbracket r /rrbracket A α ( c ) ≤ A α ( c ) ⇒ /llbracket r ∗ /rrbracket A α ( c ) = α ( c ) ;
- (e) d ≤ /llbracket r /rrbracket c ⇒ /llbracket r ∗ /rrbracket ( c ∨ d ) = /llbracket r ∗ /rrbracket c .

Proof. Let us recall that A = γα .

- (a) By correctness (4), and by definition of bca /llbracket r /rrbracket A .
- (b) By (a), α ( /llbracket r /rrbracket c ) ≤ A α ( /llbracket r /rrbracket γα ( c )) = /llbracket r /rrbracket ♯ A α ( c ) ≤ A /llbracket r /rrbracket ♯ A α ( c ) = α ( /llbracket r /rrbracket c ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- (d) The proof is analogous to that of (c) and therefore omitted.
- (c) Let us assume that /llbracket r /rrbracket ♯ A α ( c ) ≤ α ( c ) . The following property can be proved by an easy induction on n ≥ 1:

Thus,

- (e) Let us assume that d ≤ /llbracket r /rrbracket c . Then

<!-- formula-not-decoded -->

□

- 2.2.3 Programs. We consider standard basic expressions used in deterministic while programs: no-op instruction, assignments, and Boolean guards, as defined below:

<!-- formula-not-decoded -->

where a ranges over arithmetic expressions on integer values in Z and variables x ∈ Var , and b ranges over Boolean expressions in BExp including negation. Hence, a standard deterministic imperative language Imp (cf. Winskel [1993]) can be defined using guarded branching and loop commands as syntactic sugar as follows (cf. Kozen [1997, Section 2.2]):

<!-- formula-not-decoded -->

The syntax of Imp commands is defined by the following grammar:

<!-- formula-not-decoded -->

To improve readability, in our running examples we will often use this syntactic sugar.

A program store σ : V → Z is a total function from a finite set of variables of interest V ⊆ Var to values and Σ ≜ V → Z denotes the set of stores on the variables ranging in a set V that, for simplicity, is left implicit. This definition of stores allows us to compose logical proofs for regular commands by choosing a finite set of variables V that is large enough to include all the variables occurring in a finite set of commands. The concrete domain is S ≜ ℘ (Σ) , ordered by inclusion.

The semantics /llparenthesis · /rrparenthesis : Exp → S → S of basic expressions is defined as follows:

<!-- formula-not-decoded -->

where store update σ [ x ↦→ v ] and the semantics of arithmetic expressions { | a | } : Σ → Z and Boolean expressions { | b | } : Σ →{ tt , ff } are defined as expected.

For brevity, we overload b to denote the set /llparenthesis b ? /rrparenthesis Σ of all and only stores that satisfy b , so that /llparenthesis b ? /rrparenthesis p = p ∩ b fi lters the concrete stores in p making b true. The usual strongest post-condition for r for a pre-condition p ∈ S is therefore post [ r ] p ≜ /llbracket r /rrbracket p . Analogously, we define post A [ r ] α ( p ) ≜ /llbracket r /rrbracket ♯ A α ( p ) .

In the following, we will present some simple running examples involving programs with just one variable, so that V = { x } . In these cases, to simplify the notation, ℘ ( Z ) will be used to represent sets of stores in S , i.e., p ∈ ℘ ( Z ) represents the set { σ ∈ Σ | σ ( x ) ∈ p } ∈ S . Accordingly, Abs ( ℘ ( Z )) will represent Abs ( S ) . For example, {-2 , 2 } will be used to represent a verbose expression such as x = -2 ∨ x = 2.

Fig. 2. A basic proof system ⊩ A for global completeness [Giacobazzi et al. 2015, Figure 5].

<!-- image -->

Fig. 3. Abstract domains for sign analysis.

<!-- image -->

## 3 ONTHE LIMITS OF (GLOBAL) COMPLETENESS

Giacobazzi et al. [2015, Theorem 4.5] proved that completeness holds for all programs in a Turing complete programming language only for trivial abstract domains. This means that the only abstract domains that are complete for all programs are the straightforward ones: the identical abstraction, making abstract and concrete semantics the same, and the top abstraction, making all programs equivalent by abstract semantics. Giacobazzi et al. [2015] observed that since skip is always trivially complete and composition, conditional and loop statements all preserve the completeness of their subprograms, the only sources of incompleteness may arise from assignments and Boolean guards. Nevertheless, one can prove the completeness of specific programs by structural induction on their syntax, through the basic proof system by Giacobazzi et al. [2015], recalled in Figure 2, where a proof of ⊩ A c entails the completeness of a program c in an abstract domain A . Hence, the completeness of (the semantic functions associated with) assignments and Boolean guards occurring in a program is a sufficient condition to guarantee the completeness of the whole program.

Example 3.1. As a simple example, consider the abstract domain Sign for sign analysis depicted in Figure 3 and the Imp program

<!-- formula-not-decoded -->

It turns out that all the guards and assignments occurring in c are complete on Sign , i.e., C Sign ( x &lt; 0? ) , C Sign ( x ≥ 0? ) , C Sign ( x : = x ∗ 2 ) , and C Sign ( x : = x ∗ 3 ) hold. Thus, one can easily prove ⊩ Sign c , entailing that c is complete on Sign .

While the completeness of assignments has been extensively studied (e.g., the completeness conditions for assignments in major numerical domains such as intervals, congruences, octagons and affine relations have been fully settled [Giacobazzi et al. 2015; Miné 2017; Ranzato 2020]), the case of Boolean guards is troublesome and largely unexplored. In particular, in the case of conditional and loop statements, the completeness on a store abstraction A calls for the validity of the conditions C A ( b ? ) and C A ( ¬ b ? ) :

<!-- formula-not-decoded -->

that is,

<!-- formula-not-decoded -->

The term global in the section title refers to the universal quantification over any possible set S of stores in Equation (7), which we prove to be a major limitation. The following results provide a sufficient and necessary condition on the abstract domain A for guaranteeing both C A ( b ? ) and C A ( ¬ b ? ) . We first observe that when the functions /llbracket b ? /rrbracket and /llbracket ¬ b ? /rrbracket are complete in a strict abstract domain A , then b and ¬ b are expressible in A , that is, A ( b ) = b and A ( ¬ b ) = ¬ b hold.

Lemma 3.2. Let A ∈ Abs ( S ) be strict. If C A ( b ? ) and C A ( ¬ b ? ) hold, then b and ¬ b are expressible in A .

Proof. Let us show the contrapositive, so we assume that either A ( b ) /nequal b or A ( ¬ b ) /nequal ¬ b . Since, for all p ∈ S , p ⊆ A ( p ) holds, we have that b ⊊ A ( b ) or ¬ b ⊊ A ( ¬ b ) , so that either A ( b ) ∩¬ b /nequal ∅ or A ( ¬ b ) ∩ b /nequal ∅ . Assume that A ( b ) ∩¬ b /nequal ∅ holds. Then A ( b ∩¬ b ) = A ( ∅ ) = ∅ while ∅ ⊊ A ( b ) ∩ ¬ b ⊆ A ( A ( b ) ∩ ¬ b ) , so that C A ( ¬ b ) does not hold. The case A ( ¬ b ) ∩ b /nequal ∅ is symmetric. □

Furthermore, when b and ¬ b are both expressible in A , it turns out that the completeness of /llbracket b ? /rrbracket and /llbracket ¬ b ? /rrbracket boils down to a co-additivity condition for the abstraction map α , or, equivalently, an additivity condition for the concretization map γ . This is clearly a way too strong requirement in abstract interpretation as co-additive abstraction maps imply that the abstract domain is (isomorphic to) a complete sublattice of the concrete domain, namely it is a disjunctive abstraction [Giacobazzi and Ranzato 1996, 1998].

Lemma 3.3. Let b and ¬ b be expressible in A α , γ ∈ Abs ( S ) . Then, C A ( b ? ) and C A ( ¬ b ? ) hold iff

<!-- formula-not-decoded -->

Proof. We show that Equation (7) is equivalent to Equation (8). Observe that for all p ∈ S ,

```
α ( γα ( p ) ∩ b ) = [because b is expressible in A ] α ( γα ( p ) ∩ γα ( b )) = [by GI, γ is co-additive] αγ ( α ( p ) ∧ A α ( b )) = [by GI, αγ = id ] α ( p ) ∧ A α ( b ) .
```

Thus, when b and ¬ b are expressible, it turns out that α ( γα ( p ) ∩ b ) = α ( p ∩ b ) iff α ( p ) ∧ A α ( b ) = α ( p ∩ b ) . Symmetrically, α ( γα ( p ) ∩ ¬ b ) = α ( p ∩ ¬ b ) iff α ( p ) ∧ A α ( ¬ b ) = α ( p ∩ ¬ b ) . We have therefore proved (7) ⇔ (8). □

The next characterization result provides an effective way to check whether an abstract domain A is complete w.r.t. a Boolean guard b . It amounts to check that b and ¬ b are both expressible in A and that the union of the concretizations of any two abstract points in A below, respectively, α ( b ) and α ( ¬ b ) , is also expressible in A (see Example 3.5).

Theorem 3.4 (Complete Guards). Let b and ¬ b be expressible in A α , γ ∈ Abs ( S ) . Then, C A ( b ? ) and C A ( ¬ b ? ) hold iff

<!-- formula-not-decoded -->

Proof. Let us first show that C A ( b ) ∧ C A ( ¬ b ) is equivalent to Condition (9). We know that γα ( b ) = b and γα ( ¬ b ) = ¬ b . By co-additivity of γ , for any p ∈ S , we have that

<!-- formula-not-decoded -->

By Lemma 3.3, to prove our statement we show that (8) ⇔ (9) holds.

( ⇒ ) By contraposition we prove that if Equation (9) is not satisfied, then Equation (8) does not hold. Let us assume that there exist a 1 ≤ A α ( b ) and a 2 ≤ A α ( ¬ b ) such that γ ( a 1 ∨ A a 2 ) ⊋ γ ( a 1 ) ∪ γ ( a 2 ) , so that there exists σ ∈ γ ( a 1 ∨ A a 2 ) such that σ /nelement γ ( a 1 ) ∪ γ ( a 2 ) . Clearly, either σ ∈ b or σ ∈ ¬ b . Without loss of generality we assume that σ ∈ b (the case σ ∈ ¬ b is symmetric). Let p ≜ γ ( a 1 ) ∪ γ ( a 2 ) so that:

<!-- formula-not-decoded -->

Thus, σ /nelement γα ( p ∩ b ) = γ ( a 1 ) , because σ /nelement γ ( a 1 ) ∪ γ ( a 2 ) . Moreover,

<!-- formula-not-decoded -->

so that σ ∈ γ ( α ( p ) ∧ A α ( b )) because we have assumed σ ∈ γ ( a 1 ∨ A a 2 ) and σ ∈ b . Thus, γα ( p ∩ b ) /nequal γ ( α ( p ) ∧ A α ( b )) . Since γ is injective, α ( p ∩ b ) /nequal α ( p ) ∧ A α ( b ) , i.e., Equation (8) does not hold.

( ⇐ ) By contraposition, we prove that if Equation (8) fails, then Equation (9) does not hold. If Equation (8) does not hold, then there must exist some p ∈ S such that

<!-- formula-not-decoded -->

Thus, by applying γ , which, by GI, is injective, γα ( p ∩ b ) ⊊ γ ( α ( p ) ∧ A α ( b )) or γα ( p ∩ ¬ b ) ⊊ γ ( α ( p ) ∧ A α ( ¬ b )) . In turn, since γ is co-additive and b , ¬ b are expressible in A , γα ( p ∩ b ) ⊊ γ ( α ( p )) ∩ b or γα ( p ∩ ¬ b ) ⊊ γ ( α ( p )) ∩ ¬ b . Hence, we obtain that

<!-- formula-not-decoded -->

Let us now consider a 1 ≜ α ( p ∩ b ) and a 2 ≜ α ( p ∩ ¬ b ) . Then,

<!-- formula-not-decoded -->

thus proving that Equation (9) does not hold.

□

Let us illustrate through some examples how Theorem 3.4 can be applied to check the completeness of some guards.

Example 3.5. Let Sign , Sign 1 , Sign 2 ∈ Abs ( ℘ ( Z )) be the abstract domains depicted in Figure 3 and consider the programs AbsVal and ReLU defined in Section 1.

In Sign , all expressible Boolean guards are complete and the completeness of both the programs AbsVal and ReLU can be proved inductively.

In Sign 1 , no expressible Boolean guard is complete (except the trivial ones tt and ff). Indeed, only the elements ∅ and Z satisfy Condition (9). The negation of Z = 0 is Z /nequal 0, which does not belong to Sign 1 . For the guard Z &lt; 0, its negation Z ≥ 0 is in Sign 1 , but the join of Z &lt; 0 with Z &gt; 0 ≤ Sign 1 Z ≥ 0 is again Z /nequal 0 /nelement Sign 1 . Dually for Z &gt; 0.

In Sign 2 , the guards Z ≥ 0 and Z &lt; 0 are complete, while Z ≤ 0 and Z = 0 are not. For example, for Z = 0 ≤ Sign 2 Z ≥ 0 and Z &lt; 0 we have γ ( Z = 0 ∨ Sign 2 Z &lt; 0 ) = γ ( Z ≤ 0 ) = γ ( Z = 0 ) ∪ γ ( Z &lt; 0 ) . It follows that, even if both ReLU and AbsVal are complete in Sign 2 , only ReLU can be inductively proved to be complete, because all its basic expressions are complete in Sign 2 . In the case of AbsVal instead, the assignment x : = -x is not complete, e.g., for p ≜ x &gt; 0 (the fact that such input will never be provided to that branch of code is irrelevant).

It is worth remarking that Condition (9) of Theorem 3.4 suggests a strategy to make a given abstract domain A complete for b and ¬ b : We can either add to A the concrete values γ ( a 1 ) ∪ γ ( a 2 ) that are missing in A or remove either a 1 or a 2 from A when γ ( a 1 ) ∪ γ ( a 2 ) is not in A .

Example 3.6. Consider the domain Int N ∈ Abs ( ℘ ( N )) of (possibly infinite) intervals on natural numbers N [Cousot and Cousot 1977] and assume we are interested in testing equality to 0. The Boolean guards x = 0? and x /nequal 0? are expressible in Int N as the intervals [0 , 0] and [1 , ∞ ], respectively. However, ∅ is the only (trivial) interval below [0 , 0] and, besides ∅ , any element of the form [ a , b ], with 1 &lt; a ≤ b , is below [1 , ∞ ]. Theorem 3.4 requires that any element in the set { [0 , 0] ∪ [ a , b ] | 1 &lt; a ≤ b } is also exactly represented. Therefore, an abstract domain that is complete for the guards x = 0? and x /nequal 0? can be obtained by adding to Int N all the elements in { [0 , 0] ∪ [ a , b ] | 1 &lt; a ≤ b } . Observe that Int N ∪ { [0 , 0] ∪ [ a , b ] | 1 &lt; a ≤ b } is Moore closed (see Section 2.1.1) and therefore it is an abstract domain of ℘ ( N ) (cf. Section 2.1.1). Note that only the guards x = 0? and x /nequal 0? are complete on this refined abstract domain.

Because all interesting programs include Boolean guards, complete abstract domains refining a given domain may indeed become very close to the concrete domain, therefore limiting the effectiveness of this notion of completeness in program analysis. The following example, similar to Example 3.6, shows that this phenomenon can be a major drawback of refining an abstract domain to achieve completeness for the Boolean guards occurring in a given program.

Example 3.7. Consider the abstract domain Int ∈ Abs ( ℘ ( Z )) of integer intervals [Cousot and Cousot 1977]. The only Boolean guards b such that both b and ¬ b are expressible in Int are the infinite intervals [ -∞ , k ] and [ k , ∞ ], for some k ∈ Z , together with the trivial intervals Z and ∅ . In fact, in Int , the complement of any finite interval [ a , b ] ∈ Int , with a ≤ b , must be necessarily approximated. However, if we consider b = [ -∞ , k ] and, correspondingly, ¬ b = [ k + 1 , ∞ ], then Condition (9) of Theorem 3.4 is not satisfied. As an example, let us fix k = -1, i.e., b = [ -∞ , -1] and, correspondingly, ¬ b = [0 , ∞ ]. Condition (9) of Theorem 3.4 would require the presence of all the concrete joins [ n 1 , n 2] ∪ [ m 1 , m 2] with n 1 ≤ n 2 &lt; 0 ≤ m 1 ≤ m 2, because [ n 1 , n 2] ≤ Int [ -∞ , -1] and [ m 1 , m 2] ≤ Int [0 , ∞ ], but these joins are not intervals, unless n 2 = 0 and m 1 = 1. If we add all such joins [ n 1 , n 2] ∪ [ m 1 , m 2] to Int , then we obtain a Moore closed subset of ℘ ( Z ) and therefore we achieve a complete abstraction for the guards x &lt; 0? and x ≥ 0?.

Even a basic guard such as b ≜ Z = 0 = [0 , 0] would need its complement ¬ b = Z /nequal 0 = [ -∞ , -1] ∪ [1 , ∞ ] as well as the concrete joins [ n 1 , n 2] ∪ [0 , 0] for any n 1 ≤ n 2 &lt; -1 or 1 &lt; n 1 ≤ n 2, because any such interval [ n 1 , n 2] is below [ -∞ , -1] ∪ [1 , ∞ ]. Moreover, notice that the intersection of ¬ b with any interval [ n , m ] with n &lt; 0 &lt; m is [ n , -1] ∪ [1 , m ], and since abstract domains are Moore closed, all these sets must be included as well.

## 4 LOCAL COMPLETENESS

Section 3 shows that the standard notion of (global) completeness (1) for Boolean guards is a too strong requirement for abstract domains, often met in practice just by trivial guards or domains.

While completeness can be hard/impossible to achieve globally , i.e., for all possible sets of stores, it could well happen that completeness holds locally , i.e., just for some store properties. We therefore put forward a notion of local completeness , which in program analysis corresponds to considering completeness only along certain program executions.

Definition 4.1 (Local Completeness). An abstract domain A ∈ Abs ( C ) is locally complete for f : C → C at a concrete value c ∈ C , written C A c ( f ) , if the following condition holds:

<!-- formula-not-decoded -->

Accordingly, ordinary completeness as defined by Equation (1) is also referred to as global completeness . Note that global completeness amounts to the universal quantification of local completeness, in the sense that C A ( f ) ⇔ ∀ c ∈ C . C A c ( f ) . Let us also observe that A is trivially locally complete for any f on any abstract value A ( c ) (i.e., C A A ( c ) ( f ) always holds). As discussed in Section 1, in program analysis it may well happen that /llbracket r /rrbracket is not globally complete w.r.t. the abstract domain A but it is locally complete for a particular class of inputs p (that is a value in the concrete domain of powerset of stores). In the following, we write C A p ( r ) instead of the more verbose C A p ( /llbracket r /rrbracket ) .

Example 4.2. Consider the following Imp program

<!-- formula-not-decoded -->

and the interval abstraction Int . While the transfer function /llbracket 0 &lt; x ? /rrbracket is not globally complete (see Example 3.7), it is locally complete for any set p ∈ ℘ ( Z ) satisfying one of the following conditions:

<!-- formula-not-decoded -->

Since the transfer functions for constant addition and multiplication are globally complete, the program c is locally complete for any p satisfying one of the above conditions (1)-(3), meaning that its abstract interpretation in Int will not lose precision. For example, if p = { 0 , 1 , 4 } , then condition (3) holds and we have that Int ( /llbracket c /rrbracket p ) = Int ( {-1 , 0 , 2 } ) = [ -1 , 2] and Int ( /llbracket c /rrbracket Int ( p )) = Int ( /llbracket c /rrbracket [0 , 4] ) = Int ( {-1 , 0 , 1 , 2 } ) = [ -1 , 2]. As an example of local incompleteness, if p = { 0 , 4 } , then we have that Int ( /llbracket c /rrbracket p ) = Int ( { 0 , 2 } ) = [0 , 2], but Int ( /llbracket c /rrbracket Int ( p )) = [ -1 , 2].

Let us remark that, with respect to compositional reasoning, there is a significant key difference between global and local completeness: While the composition (via generic regular commands operators, and consequently via conditionals and loops) of globally complete transfer functions is always globally complete, the same does not necessarily hold for local completeness that depends on a given input property. Equivalently, local completeness of a composite program may well depend on the partial store properties met during the computation, as shown by the following example.

Example 4.3. Consider a composition c ; c , where c is defined in Example 4.2. Int is locally complete for c on the input property p = { 2 , 6 } , because condition (1) of Example 4.2 holds. However, Int is not locally complete for c ; c on p , because Int ( /llbracket c ; c /rrbracket { 2 , 6 } ) = Int ( /llbracket c /rrbracket { 0 , 4 } ) = [0 , 2] while Int ( /llbracket c ; c /rrbracket Int ( { 2 , 6 } )) = Int ( /llbracket c ; c /rrbracket [2 , 6] ) = Int ( /llbracket c /rrbracket [0 , 4] ) = Int ( {-1 , 0 , 1 , 2 } ) = [ -1 , 2].

## 4.1 Locally Complete Boolean Guards

By focussing on Boolean guards, we can characterize the local completeness of both positive b ? and negative ¬ b ? branches of a conditional statement b ∈ BExp for a given input store property.

Theorem 4.4 (Locally Complete Guards). Let b ∈ BExp , A ∈ Abs ( S ) and p ∈ S . Then, A is locally complete for both /llbracket b ? /rrbracket and /llbracket ¬ b ? /rrbracket on p iff ( A ( p ∩ b ) ∩ b ) ∪ ( A ( p ∩ ¬ b ) ∩ ¬ b ) ∈ A .

Proof. ( ⇒ ) : We assume that C A p ( b ) and C A p ( ¬ b ) and prove that ( A ( p ∩ b ) ∩ b ) ∪ ( A ( p ∩¬ b ) ∩¬ b ) is expressible in A . We have that

<!-- formula-not-decoded -->

so that, by exploiting the hypothesis of local completeness of /llbracket b ? /rrbracket on p ,

A (( A ( p ∩ b ) ∩ b ) ∪ ( A ( p ∩ ¬ b ) ∩ ¬ b )) ∩ b ⊆ A ( p ) ∩ b ⊆ A ( A ( p ) ∩ b ) ∩ b = A ( p ∩ b ) ∩ b . Likewise,

<!-- formula-not-decoded -->

Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

meaning that ( A ( p ∩ b ) ∩ b ) ∪ ( A ( p ∩ ¬ b ) ∩ ¬ b ) ∈ A .

( ⇐ ) : For the converse implication, we assume that ( A ( p ∩ b ) ∩ b ) ∪ ( A ( p ∩ ¬ b ) ∩ ¬ b ) ∈ A and prove that both C A p ( b ) and C A p ( ¬ b ) hold. It turns out that p = ( p ∩ b ) ∪ ( p ∩¬ b ) ⊆ ( A ( p ∩ b ) ∩ b ) ∪ ( A ( p ∩ ¬ b ) ∩ ¬ b ) .

Therefore, by exploiting the hypothesis, we obtain that

<!-- formula-not-decoded -->

Thus, A ( p ) ∩ b ⊆ A ( p ∩ b ) ∩ b ⊆ A ( p ∩ b ) , in turn entailing that local completeness A ( A ( p ) ∩ b ) = A ( p ∩ b ) holds. Analogously, we obtain that A ( A ( p ) ∩ ¬ b ) = A ( p ∩ ¬ b ) . □

Example 4.5. Let us apply Theorem 4.4 to show that for the interval abstraction Int , the Boolean guard 0 &lt; x is locally complete for any p ∈ ℘ ( Z ) such that (1) p ⊆ Z &gt; 0, or (2) p ⊆ Z ≤ 0, or (3) { 0 , 1 } ⊆ p . In fact, it turns out that positive and negative branches /llbracket x &gt; 0? /rrbracket and /llbracket x ≤ 0? /rrbracket are both locally complete on p iff

<!-- formula-not-decoded -->

Since x &gt; 0 and x ≤ 0 both belong to Int , condition ( ∗ ) boils down to

<!-- formula-not-decoded -->

Now, it is just a matter of noticing that ( ⋆ ) holds iff either Int ( p ∩ x ≤ 0 ) is empty (condition (1)), or Int ( p ∩ x &gt; 0 ) is empty (condition (2)) or Int ( p ∩ x ≤ 0 ) and Int ( p ∩ x &gt; 0 ) are contiguous nonempty intervals, and this happens iff p includes both cut points 0 and 1 of the guard 0 &lt; x .

Likewise Theorem 3.4 can be used to construct domains that are complete for some Boolean guards, Theorem 4.4 gives a way to construct domains that are locally complete for some Boolean guards. The next example shows that, as expected, making an abstract domain locally complete for some guards is less demanding than making it (globally) complete for the same guards.

Example 4.6. In Example 3.7 we have shown that to make the domain Int globally complete for the guards b ≜ x &lt; 0 = x ∈ [ -∞ , -1] and ¬ b ≜ x ≥ 0 = [0 , ∞ ] would require the addition of all the concrete joins [ n 1 , n 2] ∪ [ m 1 , m 2] with n 1 ≤ n 2 &lt; 0 ≤ m 1 ≤ m 2.

Given any input p , Theorem 4.4 shows that Int is made locally complete for the guards b and ¬ b by adding the unique element ( Int ( p ∩ b ) ∩ b ) ∪ ( Int ( p ∩¬ b ) ∩¬ b ) and taking the Moore closure. For example, when p ≜ { n | n odd } then ( Int ( p ∩ b ) ∩ b ) ∪ ( Int ( p ∩¬ b ) ∩¬ b ) = [ -∞ , -1] ∪ [1 , ∞ ] = Z /nequal 0 is the unique element to add (and, by Moore closure, any concrete join of the form [ n , -1] ∪ [1 , m ] with n ≤ -1 and m ≥ 1). Thus, we get the domain that contains all the intervals, possibly with a hole in 0.

## 5 LOCAL COMPLETENESS LOGIC

Wedefine a proof system for program analysis of regular commands, parameterized by an abstraction A , whose provable triples ⊢ A [ p ] r [ q ] guarantee that

- (i) q is an under-approximation of /llbracket r /rrbracket p (i.e., q ⊆ /llbracket r /rrbracket p );
- (ii) /llbracket r /rrbracket is locally complete for input p and abstraction A (i.e., C A p ( r ) holds);
- (iii) q and /llbracket r /rrbracket p have the same over-approximation in A (i.e., A ( q ) = A ( /llbracket r /rrbracket p ) ).

Given a correctness specification spec , we recall that abstract interpretation raises an alarm when γ ( /llbracket r /rrbracket ♯ A α ( p )) ⊈ spec : Such alarm is false if /llbracket r /rrbracket p ⊆ spec and true otherwise. It turns out that the above three properties of any provable triple ⊢ A [ p ] r [ q ] allow us to distinguish between true and false alarms, as described below:

- Case 1: If the over-approximation /llbracket r /rrbracket ♯ A α ( p ) does not raise alarms, i.e., γ ( /llbracket r /rrbracket ♯ A α ( p )) ⊆ spec holds, then the program r does not exhibit unwanted behaviours. It should be remarked that this already holds for any sound and possibly incomplete over-approximating abstract interpretation.
- Case 2: If spec is expressible in A and the abstract interpretation /llbracket r /rrbracket ♯ A α ( p ) raises some alarms because γ ( /llbracket r /rrbracket ♯ A α ( p )) ⊈ spec , then, by local completeness, any provable triple ⊢ A [ p ] r [ q ] is such that q ∖ spec /nequal ∅ and all the stores in q ∖ spec are true alarms. As discussed in the Introduction, let us recall that by relying on generic, thus possibly incomplete, abstract interpretation we could not distinguish which alarms in γ ( /llbracket r /rrbracket ♯ A α ( p )) ∖ spec are true ones and which are false.
- Case 3: If spec is expressible in A , some alarm is raised because γ ( /llbracket r /rrbracket ♯ A α ( p )) ⊈ spec but any attempt to derive a triple ⊢ A [ p ] r [ q ] for some under-approximation q fails because some proof obligations of local completeness C A c ( f ) are not met, then the abstraction A is not precise enough to distinguish between true and false alarms in a compositional way (for r on p ). In this case, one could refine the abstraction A to enhance its precision and repeat the analysis, possibly guided by the failed proof obligations (see Example 5.9 and also Section 8).

The logical proof system ⊢ A is defined in Figure 4 and called LCL A . Our objective in designing this deductive system has been to track the assumptions of local completeness needed for having a compositional proof. The distinctive rules are ( transfer ) and ( relax ) whose premises depend directly on the underlying abstraction A . For the readers' convenience, we copy rule ( relax ) as follows:

<!-- formula-not-decoded -->

The combined consequence rule ( relax ) is the key principle that allows us to adapt and generalize partial proofs to broader contexts. The novelty of ( relax ) lies in combining an over- and under-approximating reasoning: ( relax ) allows us to infer a post-condition q that is an under-approximation of the exact behaviour but whose abstraction A ( q ) is a sound over-approximation of it, i.e., such that q ⊆ /llbracket r /rrbracket p ⊆ A ( /llbracket r /rrbracket p ) = A ( q ) holds. Likewise in the consequence rules of de Vries and Koutavas [2011], O'Hearn [2020], and Raad et al. [2020], the logical ordering between pre-conditions p ′ ≤ p and post-conditions q ≤ q ′ in the premises of ( relax ) is reversed w.r.t. the canonical consequence rule of Hoare logic and this is needed because our post-conditions q are always under-approximations. Let us also remark that the premises of ( relax ) imply that A ( p ) = A ( p ′ ) and A ( q ) = A ( q ′ ) . Example 5.10 will show that a dual version of ( relax ) with p strengthening p ′ and q weakening q ′ as in the classical consequence rule of Hoare logic would not be sound w.r.t. local completeness.

Fig. 4. The proof system LCL A .

|    |
|----|

The crux of ( relax ) is to constrain this under-approximating post-condition q to have the same abstraction as the exact behaviour to preserve the precision of the deduction. This opens up an interesting perspective about the generality of our proof system that will be tackled in Section 6 for showing how to recover O'Hearn [2020]'s IL as an instance of our proof system. Moreover, in Section 5.3 we also show how an easy dualization of LCL A allows us to accomodate backward abstract reasoning as used in backward program analysis.

Technically, the validity of the rule ( relax ) relies on observing that local completeness is a kind of 'abstract convex property,' meaning that if A is locally complete for some c ∈ C , then A is locally complete for all d ∈ C such that c ≤ d ≤ A ( c ) holds.

<!-- formula-not-decoded -->

Proof. Since c ≤ d ≤ A ( c ) , by monotonicity of f and A , we obtain that Af ( c ) ≤ Af ( d ) ≤ Af A ( c ) and Af A ( d ) ≤ Af AA ( c ) = Af A ( c ) . Since Af A ( c ) = Af ( c ) , we have that Af ( c ) = Af ( d ) . Finally, Af ( d ) ≤ Af A ( d ) ≤ Af ( c ) = Af ( d ) . □

The rule ( transfer ) checks that the basic expressions e are locally complete on p and, in that case, provides the output of the corresponding transfer function /llbracket e /rrbracket on p as post-condition,

<!-- formula-not-decoded -->

Of course, for no-ops, Boolean guards and assignments, the rule ( transfer ) can be equivalently stated in symbolic form as follows:

<!-- formula-not-decoded -->

where [ v / x ] denotes the substitution for replacing x by v .

The rule ( seq ) for sequential composition and the rule ( join ) for choice are standard. The rule ( rec ) allows us to unfold one step of Kleene iteration, until the rule ( iterate ) can be applied.

The rule ( iterate ) is a distinguishing rule of LCL A and is as much fundamental as rule ( relax ) for several reasons: Both rules have premises depending on the abstraction A ; under-approximated post-conditions are only introduced by these two rules (all the other rules are otherwise 'exact'); while the concrete semantics of r ∗ can be infinitary (e.g., consider ( x : = x + 1 ) ∗ ), using ( iterate )

Fig. 5. Derivation of ⊢ Int [ p = { 1 , 999 } ] r [ { 0 , 2 , 1000 } ] for Example 5.2, where the label ( tr . ) stands for ( transfer ) .

<!-- image -->

we can exploit the abstraction A to stop the proof when the abstraction of a finitary input p is already an infinitary abstract invariant 3 (cf. Lemma 5.4), returning a finite under-approximation of the concrete invariant; the combination of under- and over-approximations in the rule ( iterate ) is therefore more expressive than the sum of its parts, as it allows us to speed up both program analysis and alarm detection.

The next two examples illustrate the key features of LCL A : The first one exploits all the rules, and the second one is applied to a classical while-loop. They will be revisited in Section 5.1 to show how LCL A can help in program analysis.

Example 5.2. Let us consider the interval domain Int , the pre-condition p ≜ { 1 , 999 } and the command r ≜ ( r 1 ⊕ r 2 ) ∗ , where

<!-- formula-not-decoded -->

The triple ⊢ Int [ p ] r [ { 0 , 2 , 1000 } ] can be derived as shown in Figure 5, where for brevity we let

<!-- formula-not-decoded -->

Notably, each instance of rule ( transfer ) used in the derivation exposes a proof obligation (such as C Int p ( e 2 ) , C Int p 1 ( b 1? ) , etc.) concerning the local completeness of a basic command. This proof needs just one application of ( rec ) to compute an under-approximation of post [ r ] p = /llbracket r /rrbracket p , because the rule ( iterate ) can stop the unfolding of the Kleene iterate operator as soon as an abstract invariant is detected, before the actual concrete invariant is fully computed (in this case the abstract invariant is detected by { 0 , 1 , 2 , 998 , 999 , 1000 } ⊆ [0 , 1000]). Moreover, ( relax ) is exploited to reduce the number of values to be taken into account (along the pre-conditions by navigating the derivation tree bottom-up and along the post-conditions when the tree is explored top-down).

Finally, a similar result is soon obtained on any input p k ≜ { k , 999 } for some k ∈ N by applying the rule ( rec ) for k times: Then the rule ( iterate ) can be used.

Example 5.3. Let us consider the domain Sign , the pre-condition p ≜ {-10 , -1 , 100 } , and the following Imp program,

<!-- formula-not-decoded -->

3 A maybe non-obvious consequence of the condition q ≤ A ( p ) .

Let us verify that c does not satisfy the correctness specification spec ≜ x &lt; 10, even if the loop c diverges on inputs {-10 , -1 } . The derivation in Figure 6 proves the triple ⊢ Sign [ p ] c [ { 100 } ]. As the post-condition { 100 } is an under-approximation of /llbracket r /rrbracket p (cf. Theorem 5.5 (1)), we conclude that 100 /nelement spec is a true alarm. Observe that all proof obligations about local completeness due to rule ( transfer ) are satisfied, as, e.g., letting b ≜ x ≤ 0, for C Sign p ( b ? ) , we have that

<!-- formula-not-decoded -->

Of course, let us point out that some additional valid rules could be added to our proof system, for example the following two rules can be easily proved to be valid:

<!-- formula-not-decoded -->

Lemma 5.4. The rules ( invariant ) and ( abs -fix ) can be derived in LCL A .

Proof. We first show that ( invariant ) is a derived rule. If q ≤ p , then we have A ( p ∨ q ) = A ( p ) . Since ⊢ A [ p ] r [ q ], by ( iterate ) it follows ⊢ A [ p ] r ∗ [ p ∨ q ], i.e., ⊢ A [ p ] r ∗ [ p ].

For ( abs -fix ) , since γ is 1-1, if A ( q ) = A ( p ) , then α ( p ) = α ( q ) . Therefore, A ( p ∨ q ) = A ( p ) , because α is additive and thus A ( p ∨ q ) = γ ( α ( p ∨ q )) = γ ( α ( p ) ∨ A α ( q )) = γα ( q ) = A ( q ) . Since ⊢ A [ p ] r [ q ] and q ≤ A ( q ) = A ( p ) , by ( iterate ) it follows ⊢ A [ p ] r ∗ [ p ∨ q ]. Since q ≤ ( p ∨ q ) ≤ A ( p ∨ q ) = A ( q ) , by ( relax ) , we conclude ⊢ A [ p ] r ∗ [ q ]. □

The rule ( invariant ) is the analogous of the loop invariant rule in Hoare logic, while ( abs -fix ) allows us to accelerate the convergence of Kleene iteration to an abstract fixpoint.

It is worth remarking that indeed ( invariant ) and ( iterate ) are equivalent rules within LCL A . In fact, the proof of Lemma 5.4 shows that the rule ( invariant ) can be derived from the rule ( iterate ) , and, vice versa, ( iterate ) can be derived using the rules ( invariant ) , ( rec ) and ( relax ) , as shown by the following inferences:

<!-- formula-not-decoded -->

where the proof obligation q ≤ p ∨ q trivially holds, while p ≤ ( p ∨ q ) ≤ A ( p ) holds because the assumption q ≤ A ( p ) of the rule ( iterate ) implies that p ≤ ( p ∨ q ) ≤ ( p ∨ A ( p )) = A ( p ) .

## 5.1 Soundness

Our program logic LCL A turns out to be sound for the target properties (i)-(iii) stated at the beginning of Section 5, as formalized by the following soundness result, where Conditions (1) and (2) embody, respectively, items (i) and (ii)+(iii).

Theorem 5.5 (Soundness of LCL A ). Let A α , γ ∈ Abs ( C ) . For all r ∈ Reg , p , q ∈ C , if ⊢ A [ p ] r [ q ] , then

<!-- formula-not-decoded -->

Proof. For the sake of simplicity, let us refer to the equality /llbracket r /rrbracket ♯ A α ( p ) = α ( q ) as (2a) and use (2b) for the equality /llbracket r /rrbracket ♯ A α ( p ) = α ( /llbracket r /rrbracket p ) . Then we note that (2b) follows immediately from (1) and (2a) because, by monotonicity of α and correctness (4), we have that

<!-- formula-not-decoded -->

Fig. 6. Derivation of ⊢ Sign [ p = {-10 , -1 , 100 } ] c [ { 100 } ] for Example 5.3.

<!-- image -->

Therefore, in some cases we just prove (1) and (2a) and leave the proof of (2b) implicit. We proceed by induction on the derivation tree of ⊢ A [ p ] r [ q ], by distinguishing the various cases on the basis of the last rule that is applied.

( transfer ) : If rule ( transfer ) is applied as last rule, then it must be r ≡ e ∈ Exp such that C A p ( e ) and q = /llbracket e /rrbracket p . We have that (1) /llbracket e /rrbracket p ≤ /llbracket e /rrbracket p trivially holds, while /llbracket e /rrbracket ♯ A α ( p ) = /llbracket e /rrbracket A α ( p ) = α ( /llbracket e /rrbracket γα ( p )) = α ( /llbracket e /rrbracket p ) holds by C A p ( e ) , so that we also have (2).

( relax ) : If the last rule applied is ( relax ) , then we assume by induction that ⊢ A [ p ′ ] r [ q ′ ] can be derived and let p , q such that p ′ ≤ p ≤ A ( p ′ ) and q ≤ q ′ ≤ A ( q ) .

- (1) By inductive hypothesis (1) and monotonicity of /llbracket r /rrbracket we have the following:

<!-- formula-not-decoded -->

- (2) Let us observe that from p ∈ [ p ′ , A ( p ′ ) ] and q ′ ∈ [ q , A ( q ) ], we derive α ( p ′ ) = α ( p ) and α ( q ′ ) = α ( q ) . Therefore:

<!-- formula-not-decoded -->

so that, /llbracket r /rrbracket ♯ A α ( p ) = α ( q ) = α ( /llbracket r /rrbracket p ) follows.

( seq ) : If the last rule applied is ( seq ) , then it must be r ≡ r 1; r 2 and we can assume by induction that ⊢ A [ p ] r 1 [ w ] and ⊢ A [ w ] r 2 [ q ], can be derived for some w . We need to prove the thesis for the conclusion ⊢ A [ p ] r 1; r 2 [ q ].

- (1) By inductive hypotheses (1) and monotonicity of /llbracket r 2 /rrbracket :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

so that /llbracket r 1; r 2 /rrbracket ♯ A α ( p ) = α ( q ) = α ( /llbracket r 1; r 2 /rrbracket p ) follows.

Journal of the ACM, Vol. 70, No. 2, Article 15. Publication date: March 2023.

- (2) We have that

( join ) : If the last rule applied is ( join ) , then it must be r ≡ r 1 ⊕ r 2 and we assume by induction that ⊢ A [ p ] r 1 [ q 1] and ⊢ A [ p ] r 2 [ q 2] can be derived for some suitable q 1 and q 2 such that q = q 1 ∨ q 2. We need to prove the thesis for the conclusion ⊢ A [ p ] r 1 ⊕ r 2 [ q 1 ∨ q 2].

- (1) By inductive hypothesis, q i ≤ /llbracket r i /rrbracket p , therefore

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

so that /llbracket r 1 ⊕ r 2 /rrbracket ♯ A α ( p ) = α ( q 1 ∨ q 2 ) = α ( /llbracket r 1 ⊕ r 2 /rrbracket p ) follows by (1) and (2a).

( iterate ) : If the last rule applied is ( iterate ) , then it must be r ≡ r ∗ 1 , and we assume by induction that ⊢ A [ p ] r 1 [ q 1] for some q 1 such that q 1 ≤ A ( p ) and q = p ∨ q 1. Note that α ( q 1 ) ≤ A α ( A ( p )) = α ( p ) . We need to prove the thesis for the conclusion ⊢ A [ p ] r ∗ 1 [ p ∨ q 1].

- (1) By inductive hypothesis (1), we have that

<!-- formula-not-decoded -->

(2a) By inductive hypothesis (2) and hypothesis q 1 ≤ A ( p ) , we have /llbracket r 1 /rrbracket ♯ A α ( p ) = α ( q 1 ) ≤ A α ( p ) , so that Lemma 2.1 (c) is applicable. Therefore,

<!-- formula-not-decoded -->

so that, /llbracket r ∗ 1 /rrbracket ♯ A α ( p ) = α ( p ∨ q 1 ) = α ( /llbracket r ∗ 1 /rrbracket p ) follows by (1) and (2a).

( rec ) : If the last rule applied is ( rec ) , then it must be r ≡ r ∗ 1 and we assume by induction that ⊢ A [ p ] r 1 [ w ] and ⊢ A [ p ∨ w ] r ∗ 1 [ q ] can be derived for some w . We need to prove the thesis for the conclusion ⊢ A [ p ] r ∗ 1 [ q ].

- (1) By inductive hypothesis (1) and Lemma 2.1 (e) we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

so that /llbracket r ∗ 1 /rrbracket ♯ A α ( p ) = α ( q ) = α ( /llbracket r ∗ 1 /rrbracket p ) follows.

□

As a consequence, if a correctness specification spec is expressible in A , i.e., if spec = γ ( a ) for some abstract value a ∈ A , then any provable triple ⊢ A [ p ] r [ q ] allows us to use q to witness either the correctness or the incorrectness of r for the pre-condition p , as stated by the following result.

(2a) We have that

- (2) We have that

Corollary 5.6 (Precision). For all A α , γ ∈ Abs ( C ) , r ∈ Reg , p , q ∈ C , if ⊢ A [ p ] r [ q ] , then:

<!-- formula-not-decoded -->

Example 5.7. In Example 5.3, we already noticed that, by Theorem 5.5 (1), /llbracket c /rrbracket p does not satisfy spec . Note that for p ′ ≜ {-10 , -1 , 5 , 100 } we could also prove, e.g., ⊢ Sign [ p ′ ] c [ { 5 } ], where the postcondition { 5 } has no alarm, even if spec is not satisfied: Since spec is not expressible in Sign , then Corollary 5.6 is not applicable.

Example 5.8. Let us consider again Example 5.2 and the triple ⊢ Int [ p ] r [ { 0 , 2 , 1000 } ] (see Figure 5.2) to discuss the cases of three different correctness specifications: spec 1 ≜ x /nequal 2, spec 2 ≜ x ≤ 1000 and spec 3 ≜ 100 ≤ x .

By Theorem 5.5 (2), we know that /llbracket r /rrbracket p satisfies spec 2 , because Int ( /llbracket r /rrbracket p ) = Int ( { 0 , 2 , 1000 } ) = [0 , 1000] ⊆ spec 2 . Since spec 2 is expressible in Int , by Corollary 5.6, any other provable triple ⊢ Int [ p ] r [ q ] will guarantee that spec 2 holds.

Despite that spec 1 is not expressible in Int , the triple ⊢ Int [ p ] r [ { 0 , 2 , 1000 } ] exposes the true alarm 2 /nelement spec 1 , since 2 ∈ { 0 , 2 , 1000 } ⊆ /llbracket r /rrbracket p (cf. Theorem 5.5 (1)).

Finally, the triple ⊢ Int [ p ] r [ { 0 , 2 , 1000 } ] exposes two true alarms 0 , 2 /nelement spec 3 . Likewise spec 2 , by Corollary 5.6, the post-condition q of any provable triple ⊢ Int [ p ] r [ q ] will contain a true alarm for spec 3 . In particular, any such triple ⊢ Int [ p ] r [ q ], is such that 0 ∈ q , therefore contradicting the assertion spec 3 , because it must be Int ( q ) = [0 , 1000] = Int ( /llbracket r /rrbracket p ) .

Example 5.9. Let us consider the program r ≜ r ∗ 1 ; r 2, where

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Consider the correctness specification spec ≜ x /nequal -1, and two pre-conditions p 1 ≜ { 10 } and p 2 ≜ { 11 } . In the case of p 1, the value 30 for x is actually computed by the Kleene iteration r ∗ 1 , causing a violation of spec . In the case p 2, any alarm raised by a static analysis would be a false positive since r ∗ 1 will never store the value 30 in x . Let us use the abstract domain Sign for the analysis of r .

First, consider p 1 and observe that by applying ( rec ) and ( iterate ) we can derive ⊢ Sign [ { 10 } ] r ∗ 1 [ { 10 , 20 , 30 } ]. Then, by ( relax ) , we prove ⊢ Sign [ { 10 } ] r ∗ 1 [ { 10 , 30 } ]. Note that C Sign { 10 , 30 } ( x = 30? ) and C Sign { 10 , 30 } ( x /nequal 30? ) , so that ⊢ Sign [ { 10 , 30 } ] r 2 [ {-1 , 10 } ] can be proved. Finally, by applying ( seq ) , we derive the triple ⊢ Sign [ { 10 } ] r ∗ 1 ; r 2 [ {-1 , 10 } ], whose post-condition includes the true alarm -1 violating spec . The whole derivation is in Figure 7.

Consider now the pre-condition p 2. Here, we apply ( rec ) , ( iterate ) and ( relax ) so as to derive ⊢ Sign [ { 11 } ] r ∗ 1 [ { 11 , 31 } ]. In this case, since local completeness C Sign { 11 , 31 } ( x = 30? ) does not hold (indeed note that any nonempty subset of { 11 , 31 } is not locally complete for x = 30? on Sign ), the proof cannot be completed in Sign . It is worth observing that to prove that r satisfies spec for input p 2 we need to resort to a more precise abstract domain where the guard x = 30? is locally complete for { 11 , 31 } . In this sense, we remark that the failed proof obligation C Sign { 11 , 31 } ( x = 30? ) could be exploited to find a refinement of the current abstraction Sign where the derivation can be completed. For example, a possible choice is to extend the abstract domain Sign by taking Sign 30 as the Moore closure of Sign ∪ { x /nequal 30 } : Then, the triple ⊢ Sign 30 [ p 2] r [ { 11 } ] could be derived to witness that r satisfies spec (by Corollary 5.6).

The next example shows that the classical consequence rule of Hoare logic for strengthening preconditions and weakening post-conditions is in general not compatible with the local completeness property (2) of Theorem 5.5.

Fig. 7. Derivation of ⊢ Sign [ p 1 = { 10 } ] r [ {-1 , 10 } ] for Example 5.9.

Example 5.10. Consider the abstract domain Int , the absolute value program from the Introduction

<!-- formula-not-decoded -->

and the pre-conditions p ≜ {-5 , 5 } and p ′ ≜ {-5 , -1 , 0 , 5 } . By applying ( transfer ) (to x &lt; 0?, x ≥ 0?, x : = -x and skip ), ( seq ) twice and ( join ) , one can easily derive ⊢ Int [ p ′ ] AbsVal ( x ) [ q ′ ] with q ′ = { 0 , 1 , 5 } . In fact, Int is locally complete for /llbracket AbsVal ( x ) /rrbracket on p ′ , because Int ( /llbracket AbsVal ( x ) /rrbracket Int ( p ′ )) = [0 , 5] = Int ( q ′ ) .

Imagine now to replace the rule ( relax ) by its dual (convex) version, inspired by the consequence rule of Hoare logic,

<!-- formula-not-decoded -->

If we let q = Int ( q ′ ) , since p ⊆ p ′ ⊆ Int ( p ) = [ -5 , 5], and q ′ ⊆ q = Int ( q ′ ) , then we could derive, e.g., ⊢ Int [ p ] AbsVal ( x ) [ q ]. However, Int is not locally complete for /llbracket AbsVal ( x ) /rrbracket on p , because Int ( /llbracket AbsVal ( x ) /rrbracket p ) = [5 , 5] /nequal [0 , 5] = Int ( /llbracket AbsVal ( x ) /rrbracket Int ( p )) .

## 5.2 On the Logical Completeness of LCL A

We now study the completeness of LCL A as a proof system. In this context, completeness is intended in the logical sense, that is the ability of the proof system to derive any valid triple. To avoid the clash of terminology with completeness in abstract interpretation, we call it logical (in)completeness. Our logic LCL A is not logically complete in general, i.e., the converse of Theorem 5.5 does not hold, as shown by the following example.

Example 5.11 (Logical Incompleteness). Let e 1 ≜ x : = x -1, e 2 ≜ x : = x + 1, and p ≜ Z ≥ 2. The abstract domain A = Sign is locally complete for /llbracket e 1; e 2 /rrbracket on p :

<!-- formula-not-decoded -->

but the triple ⊢ Sign [ p ] e 1; e 2 [ p ] cannot be derived. This is because, in the attempt to derive the triple ⊢ Sign [ p ] e 1 [ /llbracket e 1 /rrbracket p ] by rule ( transfer ) , the proof obligation C Sign p ( e 1 ) fails: α ( /llbracket e 1 /rrbracket p ) = α ( Z ≥ 1 ) = Z &gt; 0 /nequal Z ≥ 0 = α ( Z ≥ 0 ) = α ( /llbracket e 1 /rrbracket Sign ( p )) . Note that the rule ( relax ) cannot help. In fact, let us assume that there exists some p ′ such that p ′ ⊆ p ⊆ Sign ( p ′ ) and the triple ⊢ Sign [ p ′ ] e 1 [ /llbracket e 1 /rrbracket p ′ ] is provable by ( transfer ) . Then, Sign ( p ′ ) = Sign ( p ) = Z &gt; 0 and p ′ ⊆ p = Z ≥ 2 imply that /llbracket e 1 /rrbracket p ′ ⊆ Z ≥ 1.

Hence, we would have that α ( /llbracket e 1 /rrbracket p ′ ) ≤ α ( Z ≥ 1 ) = Z &gt; 0 while α ( /llbracket e 1 /rrbracket Sign ( p ′ )) = α ( /llbracket e 1 /rrbracket Z &gt; 0 ) = Z ≥ 0. Thus, C Sign p ′ ( e 1 ) does not hold, contradicting the hypothesis that ⊢ Sign [ p ′ ] e 1 [ /llbracket e 1 /rrbracket p ′ ] is provable.

For a result of logical completeness for LCL A , we need the following:

- (1) to add the infinitary rule ( limit ) for Kleene star, whose soundness is shown by Lemma 5.12:

<!-- formula-not-decoded -->

- (2) to assume that all the basic expressions occurring in a command r ∈ Reg are globally complete on A .

Lemma 5.12. The proof system extended with rule ( limit ) is sound.

Proof. We extend the inductive proof of Theorem 5.5 by considering the case where the last rule applied to derive ⊢ A [ p ] r [ q ] is ( limit ) . As in the proof of Theorem 5.5, we refer to the equality /llbracket r /rrbracket ♯ A α ( p ) = α ( q ) as (2a) and use (2b) for the equality /llbracket r /rrbracket ♯ A α ( p ) = α ( /llbracket r /rrbracket p ) . Then we recall that (2b) follows immediately by (1) and (2a).

( limit ) : If the last rule applied is ( limit ) , then it must be r ≡ r 1 , and we can assume by induction that ∀ n ∈ N . ⊢ A [ p n ] r 1 [ p n + 1]. We need to prove the thesis for the conclusion ⊢ A [ p 0] r ∗ 1 [ ∨ i ∈ N p i ]. (1) We have that for every n ∈ N , p n ≤ /llbracket r 1 /rrbracket n p 0: obvious for n = 0; then, by inductive hypothesis, p n + 1 /llbracket r 1 /rrbracket p n /llbracket r 1 /rrbracket ( /llbracket r 1 /rrbracket n p 0 ) = /llbracket r 1 /rrbracket n + 1 p 0. Thus, n N p n n N /llbracket r 1 /rrbracket n p 0 = /llbracket r ∗ 1 /rrbracket p 0.

(2a) We have that for every n ∈ N , /llbracket r 1 /rrbracket ♯ A n α ( p 0 ) = α ( p n ) . In fact, by induction on n , this is obvious

∗ ≤ ≤ ∨ ∈ ≤ ∨ ∈ for the base case n = 0. Then, for the inductive case:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We are therefore able to obtain a result of logical completeness for LCL A when this includes the powerful infinitary rule ( limit ) and under an assumption of global completeness for the basic expressions occurring in the program. Let us remark that incorrectness logic [O'Hearn 2020] also includes this infinitary rule ( limit ) , there called backwards variant rule. Likewise ( limit ) , the backwards variant rule of IL allows us to derive other finitary rules (e.g., Iterate zero ) and plays a crucial role for proving the logical completeness of IL [O'Hearn 2020, Theorem 6].

Lemma 5.13. Let A α , γ ∈ Abs ( C ) and r ∈ Reg . Then:

<!-- formula-not-decoded -->

Consequently, Proof. We proceed by structural induction on r ∈ Reg . ( r ≡ e ) :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

( r ≡ r 1 ⊕ r 2 ) : Let us take an arbitrary p ∈ C .

<!-- formula-not-decoded -->

( r ≡ r ∗ 1 ) : Let us first prove the following property:

<!-- formula-not-decoded -->

For n = 0: α ◦ /llbracket r 1 /rrbracket 0 = α = /llbracket r 1 /rrbracket ♯ A 0 ◦ α . For n + 1,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

( r ≡ r 1; r 2 ) :

Thus, for any p ∈ C ,

This closes the proof.

□

Theorem 5.14 (Logical Completeness). Let A α , γ ∈ Abs ( C ) and r ∈ Reg such that any e ∈ Exp ( r ) is globally complete on A . For any p , q ∈ C , if q ≤ /llbracket r /rrbracket p and /llbracket r /rrbracket ♯ A α ( p ) = α ( q ) , then the triple ⊢ A [ p ] r [ q ] can be derived in the proof system extended with the ( limit ) rule.

Proof. We proceed by structural induction on r .

( r ≡ e ) : By hypothesis, /llbracket e /rrbracket ♯ A α ( p ) = α ( /llbracket e /rrbracket p ) , thus, by Lemma 2.1 (b), α ( /llbracket e /rrbracket p ) = α ( /llbracket e /rrbracket γα ( p )) . Hence, C A p ( /llbracket e /rrbracket ) holds, so that by ( transfer ) , ⊢ A [ p ] e [ /llbracket e /rrbracket p ].

( r ≡ r 1; r 2 ) : Assume that q ≤ /llbracket r 1; r 2 /rrbracket p and /llbracket r 1; r 2 /rrbracket ♯ A α ( p ) = α ( q ) = α ( /llbracket r 1; r 2 /rrbracket p ) . Let w ≜ /llbracket r 1 /rrbracket p . Then, we have that:

<!-- formula-not-decoded -->

Thus, by induction, we derive ⊢ A [ p ] r 1 [ w ] and ⊢ A [ w ] r 2 [ q ], so that by ( seq ) , ⊢ A [ p ] r 1; r 2 [ q ] follows.

( r ≡ r 1 ⊕ r 2 ) : Assume that q ≤ /llbracket r 1 ⊕ r 2 /rrbracket p and /llbracket r 1 ⊕ r 2 /rrbracket ♯ A α ( p ) = α ( q ) = α ( /llbracket r 1 ⊕ r 2 /rrbracket p ) . Let q i ≜ /llbracket r i /rrbracket p . Then, we have that q i ≤ /llbracket r i /rrbracket p and, by Lemma 5.13, /llbracket r i /rrbracket ♯ A p = α ( /llbracket r i /rrbracket p ) = α ( q i ) . Thus, by induction, ⊢ A [ p ] r i [ q i ] so that by ( join ) , ⊢ A [ p ] r 1 ⊕ r 2 [ q 1 ∨ q 2]. Then, because q ≤ /llbracket r 1 ⊕ r 2 /rrbracket p = /llbracket r 1 /rrbracket p ∨ /llbracket r 2 /rrbracket p = ( q 1 ∨ q 2 ) ≤ γα ( /llbracket r 1 ⊕ r 2 /rrbracket p ) = γα ( q ) , by ( relax ) , ⊢ A [ p ] r 1 ⊕ r 2 [ q ] follows.

( r ≡ r ∗ 1 ) : Assume that q ≤ /llbracket r ∗ 1 /rrbracket p and /llbracket r ∗ 1 /rrbracket ♯ A α ( p ) = α ( q ) = α ( /llbracket r ∗ 1 /rrbracket p ) . Let us consider the N -indexed sequence { p n } n ∈ N of values in C , where p n ≜ /llbracket r 1 /rrbracket n p . We have that for all n ∈ N , p n + 1 ≤ /llbracket r 1 /rrbracket p n and, by Lemma 5.13, /llbracket r 1 /rrbracket ♯ A α ( p n ) = α ( /llbracket r 1 /rrbracket p n ) = α ( p n + 1 ) . Thus, by induction, for all n ∈ N , ⊢ A [ p n ] r 1 [ p n + 1] is derivable. Hence, by ( limit ) , we derive ⊢ A [ p ] r ∗ 1 [ ∨ n ∈ N p n ]. Notice that ∨ n ∈ N p n = ∨ { /llbracket r 1 /rrbracket n p | n ∈ N } = /llbracket r ∗ 1 /rrbracket p . Therefore, q ≤ /llbracket r ∗ 1 /rrbracket p ≤ γα ( /llbracket r ∗ 1 /rrbracket p ) = γα ( q ) , and by ( relax ) it follows ⊢ A [ p ] r ∗ 1 [ q ]. □

It is worth noting that if any e ∈ Exp ( r ) is globally complete on A , then, as proved by [Giacobazzi et al. 2015, Theorem 5.1], /llbracket r /rrbracket ♯ A α = α /llbracket r /rrbracket also holds. Thus, the hypotheses of Theorem 5.14 imply that properties (1-2) of the soundness Theorem 5.5 all hold, i.e., Theorem 5.14 provides a result of (limited) logical completeness for LCL A . Vice versa, whenever the language is Turing complete, C = S and the abstraction A is not trivial, LCL A turns out to be intrinsically incomplete , meaning that it is always possible to find a valid triple (w.r.t. properties (1-2) of Theorem 5.5) but LCL A is unable to prove it.

Theorem 5.15 (Intrinsic Incompleteness). Let Reg be a Turing complete language. Let A α , γ ∈ Abs ( S ) . If γα /nequal id and γα /nequal λx . Σ , then there exist p , q ∈ S and r ∈ Reg such that q ≤ /llbracket r /rrbracket p and /llbracket r /rrbracket ♯ A α ( p ) = α ( /llbracket r /rrbracket p ) = α ( q ) , but ̸⊢ A [ p ] r [ q ] .

Proof. The assumption of Turing completeness of Reg implies the possibility of defining regular commands r = c ? , r /nequal c ? ∈ Reg , for any store c ∈ Σ , such that, for any p ∈ S , /llbracket r = c ? /rrbracket p = p ∩ { c } and /llbracket r /nequal c ? /rrbracket p = p ∩ ¬{ c } . Likewise, Turing completeness implies the possibility of defining regular commands r c ∈ Reg , for any c ∈ Σ , such that, for any σ ∈ Σ we have /llbracket r c /rrbracket { σ } = { c } . Finally, Turing completeness implies that there exists w ∈ Reg such that for any p ∈ S , /llbracket w /rrbracket p = ∅ holds. For the sake of clarity, by considering Imp programs over just one variable x so that c ∈ Z , these programs would be as follows:

<!-- formula-not-decoded -->

Consider now A α , γ ∈ Abs ( S ) such that γα /nequal id and γα /nequal λx . Σ . Then there exists p ∈ ℘ (Σ) such that p ⊊ A ( p ) (because γα /nequal id ) and w ∈ ℘ (Σ) such that A ( w ) ⊊ Σ (because γα /nequal λx . Σ ). Let r b , r = a ?, and r /nequal a ? be regular commands defined as above for some a ∈ A ( p ) \ p and b ∈ Σ \ A ( w ) . Now, take the program r ≜ r 1; w , where

<!-- formula-not-decoded -->

We have that /llbracket r /rrbracket p = /llbracket w /rrbracket ( /llbracket r 1 /rrbracket p ) = ∅ and /llbracket r /rrbracket A ( p ) = /llbracket w /rrbracket ( /llbracket r 1 /rrbracket A ( p )) = ∅ , so that local completeness A ( /llbracket r /rrbracket p ) = A ( /llbracket r /rrbracket A ( p )) holds. However, the triple ⊢ A [ p ] r [ ∅ ] cannot be derived, because we cannot derive any triple ⊢ A [ p ] r 1 [ q ] (to be used by the rule ( seq ) for r 1; w ). This is a consequence of the fact that /llbracket r 1 /rrbracket is not locally complete on p in A . In fact, /llbracket r 1 /rrbracket p = ∅ while /llbracket r 1 /rrbracket A ( p ) = /llbracket ( r = a ? ; r b ) ⊕ ( r /nequal a ? ; w ) /rrbracket A ( p ) = /llbracket r = a ? ; r b /rrbracket A ( p ) ∪ /llbracket r /nequal a ? ; w /rrbracket A ( p ) = { b } ∪ ∅ = { b } . Hence, α ( /llbracket r 1 /rrbracket p ) = α ( ∅ ) while /llbracket r 1 /rrbracket ♯ A α ( p ) ⊇ α ( /llbracket r 1 /rrbracket A ( p )) = α ( { b } ) (by soundness of /llbracket r 1 /rrbracket ♯ A and monotonicity of α ). We observe that α ( ∅ ) /nequal α ( { b } ) ; otherwise, by monotonicity of γ and extensivity of γα , we would have b ∈ γα ( { b } ) = γα ( ∅ ) ⊆ γα ( w ) = A ( w ) , which would be a contradiction. Now suppose that ⊢ A [ p ] r 1 [ q ] for some q . By Theorem 5.5 (1), it must be q ⊆ /llbracket r 1 /rrbracket p = ∅ , thus q = ∅ and by Theorem 5.5 (2), we would obtain α ( ∅ ) = α ( q ) = /llbracket r 1 /rrbracket ♯ A α ( p ) ⊇ α ( { b } ) , which is a contradiction. The rule ( relax ) cannot help here neither, because any strengthening of p , say p ′ , such that p ′ ⊆ p ⊆ A ( p ′ ) makes A ( p ) = A ( p ′ ) therefore making /llbracket r 1 /rrbracket incomplete also for p ′ in A . □

Turing completeness is crucial here because the proof relies upon the possibility of (1) specifying in Reg an arbitrary store in Σ , (2) effectively checking store inequality, and (3) specifying in Reg an undefined transfer function. The proof of Theorem 5.15 generalizes to LCL A and to Turing complete regular commands the proofs in Bruni et al. [2020] and Giacobazzi et al. [2015]: The class of all programs for which an abstract interpretation on A is globally complete is the set of all programs if and only if A is trivial. As a consequence of Theorems 5.14 and 5.15, LCL A cannot be a logically complete proof system for a Turing complete language unless the abstraction A is trivial. Of course, the identical abstraction is unfeasible here as both rules ( transfer ) and ( relax ) would become vacuous. Hence, the only meaningful straightforward abstraction for LCL A is A = λx . Σ . In light of this, we may therefore observe that logical completeness of IL [O'Hearn 2020, Theorem 6] follows from the choice made in its consequence rule of letting pre-conditions and post-conditions be, respectively, arbitrarily weakened and strengthened, i.e., the choice of the abstraction A = λx . Σ in rule ( relax ) . Section 6 provides additional details on the relationship with incorrectness logic.

## 5.3 A Backward Proof System

As pioneered by Cousot and Cousot [1977, Section 5.2], it is known that abstract interpretationbased program analysis can be defined either backward or forward (see Bourdoncle [1993]; Miné [2017] for examples of backward abstract interpretations). Instead of propagating forward an abstract store in a program control flow graph (CFG) from its entry point, a backward analysis can start from any program point q of the CFG (possibly, but not necessarily, an exit point) and from any input abstract value a it abstractly computes backward in the CFG to derive necessary abstract conditions for the executions reaching q and satisfying the store property a . Backward analysis is typically used after a preliminary forward analysis to refine its results, as acknowledged by Bourdoncle [1993] for abstract program debugging. An under-approximating backward program analysis by abstract interpretation has been put forward by Miné [2014]. In the following, we show how LCL A can be easily dualized to accomodate backward analyses.

In backward analysis, the basic expressions e ∈ Exp have a co-additive backward concrete semantics /llparenthesis e /rrparenthesis /shortleftarrow : C → C . Notably, /llparenthesis e /rrparenthesis /shortleftarrow Y ≜ { σ | ( σ , σ ′ ) ∈ R e ⇒ σ ′ ∈ Y } , where R e ≜ { ( σ , /llparenthesis e /rrparenthesis σ ) | σ ∈ Σ } is the transition relation for e . For example, for the basic commands of Imp (Section 2.2.3)

we have that

<!-- formula-not-decoded -->

Furthermore, in backward concrete and abstract semantics: (1) the control flows backwards and (2) meets replace joins. Hence, the backward semantics of regular commands is given as the following dual definition of (2):

<!-- formula-not-decoded -->

This defines a standard backward semantics, e.g., as given in Miné [2014, Section 2] for imperative programs.

By duality, the backward abstract semantics uses an under-approximating abstraction U α , γ ∈ Abs /shortleftarrow ( C ) , meaning that U is defined by a Galois insertion w.r.t. the concrete domain 〈 C , ≥〉 where the partial order is the inverse relation ≥ ≜ ≤ -1 . This means that for all c ∈ C , an under-approximation relation γα ( c ) ≤ c replaces an over-approximating relation c ≤ γα ( c ) .

Example 5.16. The interval domain Int can be viewed as an under-approximating abstraction by dualizing its abstraction and concretization maps α /shortleftarrow : ℘ ( Z ) → Int and γ /shortleftarrow : Int → ℘ ( Z ) as follows:

<!-- formula-not-decoded -->

For example, α /shortleftarrow ( { x ∈ Z | x &lt; -3 ∨ x &gt; 5 }∪{ 0 , 1 , 2 } ) = [ -3 , 5] and α /shortleftarrow ( { x ∈ Z | x &lt; -3 }∪{ 0 , 1 , 2 } = [ -3 , + ∞ ].

Accordingly, the abstract semantics /llbracket r /rrbracket ♯ U for an under-approximating abstraction U ∈ Abs /shortleftarrow ( C ) is defined from (3) by duality as follows:

<!-- formula-not-decoded -->

Correspondingly, when our proof system ⊢ U is instantiated to an under-approximating abstraction U ∈ Abs /shortleftarrow ( C ) , we need to replace ≤ , which models logical implication, with ≥ and logical disjunction ∨ with conjunction ∧ . Hence, the fundamental ( relax ) rule becomes

.

<!-- formula-not-decoded -->

Thus, here the condition p is logically stronger than p ′ and weaker than the under-approximation U ( p ′ ) , and dually for q . By duality, as a direct consequence of Theorems 5.5 and 5.14, a result of soundness and limited logical completeness for the dual logic ⊢ U can be derived. Hence, a provable triple ⊢ U [ p ] r [ q ] for an under-approximation U implies that: /llbracket r /rrbracket /shortleftarrow q ≤ p , i.e., p is an over-approximation of the backward semantics, and /llbracket r /rrbracket ♯ U α ( q ) = α ( p ) = α ( /llbracket r /rrbracket /shortleftarrow q ) , i.e., local completeness holds.

## 6 RELATIONSHIP WITH INCORRECTNESS LOGIC

The idea to reverse the direction of implication in Hoare's consequence rule was investigated by de Vries and Koutavas [2011] reverse Hoare logic to study reachability specifications for randomized algorithms. They first put forward the following consequence rule for under-approximation triples:

<!-- formula-not-decoded -->

O'Hearn's incorrectness logic extends the approach of reverse Hoare logic with an explicit handling of error detection and propagation. As pointed out by O'Hearn [2020], 'Program correctness and incorrectness are two sides of the same coin [...] Incorrectness logic is so basic that it could have been defined and studied immediately after or alongside the fundamental works of Floyd and Hoare on correctness in the 1960s.' Because IL is tailored to under-approximations, it can be used to prove the presence of bugs but not their absence.

In O'Hearn [2020], programs are regular commands that include primitives such as: the error () statement, to halt execution and raise an error signal er ; assume ( b ) statements, analogous to our Boolean guards b ?; and nondeterministic assignments x : = nond () also present in the setting of reverse Hoare logic. Thus, we set

<!-- formula-not-decoded -->

Incorrectness logic triples take the form ⊢ IL [ p ] c [ ϵ : q ], as their post-conditions are extended with labels ϵ ∈ { ok , er } (following O'Hearn [2020], we use colors for a visual differentiation) to distinguish the case of error-free termination ok : q leading to an under-approximating post-condition q , from interrupted computations er : q , meaning that some error occurred under the circumstances reported by q . We write ⊢ IL [ p ] c [ ok : q ][ er : w ] when ⊢ IL [ p ] c [ ok : q ] and ⊢ IL [ p ] c [ er : w ] are derivable for the same pre-condition p . Notably, the proof system of IL is proved to be sound and complete (in the logical sense): An error can arise iff it can be exposed by some provable triple.

Next, we sketch how IL can be seen as an instance of LCL A . Due to error handling, the domain S is not informative enough, but this is not a problem given the generality of LCL A . Therefore, we exploit the following four ingredients:

- (i) A suitable concrete domain C ≜ ℘ ( { ok , er } × Σ) that can distinguish between normal and erroneous termination. For q ∈ ℘ (Σ) and ϵ ∈ { ok , er } we write ϵ : q as a shorthand for { ϵ : σ | σ ∈ q } = { ϵ } × q . Clearly, a generic S ∈ C takes the form ok : q ∪ er : w for suitable q , w ∈ ℘ (Σ) , so we denote elements in C more concisely as ok : q , er : w .
- (ii) Transfer functions f : C → C are additive functions such that

<!-- formula-not-decoded -->

meaning that all the errors w in the argument are preserved. possibly further errors are generated by the application of f to some σ ∈ q .

- (iv) The abstract domain A tr is the trivial abstraction such that γα = λX . ⊤ = λX . ( { ok , er } × Σ) . Note that A tr is (globally) complete for every transfer function, therefore all proof obligations C A c ( e ) are trivially satisfied, and ( transfer ) becomes an axiom. Moreover, by A tr ( p ′ ) = ⊤ = A tr ( q ) , the rule ( relax ) boils down to the rule ( cons ) .
- (iii) The semantics of basic transfer functions is defined in Figure 8, where we write q [ x ↦→ v ] as a shorthand for { σ [ x ↦→ v ] | σ ∈ q } . For any r ∈ Reg and any q , w ∈ ℘ (Σ) , by structural induction on r , it follows that /llbracket r /rrbracket ( er : w ) = er : w and /llbracket r /rrbracket ( ok : q , er : w ) = /llbracket r /rrbracket ( ok : q ) ∪ er : w .

At the level of concrete semantics, we can establish a tight connection between the transfer function /llbracket r /rrbracket : C → C associated with r ∈ Reg and its relational denotational semantics that

```
Fig. 8. Basic transfer functions for additional statements.
```

was taken as a reference model for IL. Let us denote by /llbracket r /rrbracket ϵ ⊆ Σ × Σ the relational semantics defined in O'Hearn [2020, Figure 4]. To formalize the correspondence, we find it convenient to let /llbracket r /rrbracket ϵ : S → S denote the functional version of /llbracket r /rrbracket ϵ defined by:

```
/llbracket r /rrbracket ϵ p ≜ { σ ′ ∈ Σ | σ ∈ p , ( σ , σ ′ ) ∈ /llbracket r /rrbracket ϵ } . Lemma 6.1. For any r ∈ Reg and p ∈ S , we have: /llbracket r /rrbracket ( ok : p ) = ok : /llbracket r /rrbracket ok p , er : /llbracket r /rrbracket er p . Proof. The proof is by structural induction on r ∈ Reg . ( r ≡ skip ): By definition, /llbracket skip /rrbracket ( ok : p ) = ok : p , er : ∅ = ok : /llbracket skip /rrbracket ok p , er : /llbracket skip /rrbracket er p . ( r ≡ x : = a ): By definition, /llbracket x : = a /rrbracket ( ok : p ) = ok : ⋃ σ ∈ p { σ [ x ↦→{| a | } σ ] } , er : ∅ = ok : /llbracket x : = a /rrbracket ok p , er : /llbracket x : = a /rrbracket er p . ( r ≡ error () ): By definition, /llbracket error () /rrbracket ( ok : p ) = ok : ∅ , er : p = ok : /llbracket error () /rrbracket ok p , er : /llbracket error () /rrbracket er p . ( r ≡ assume ( b ) ): By definition, /llbracket assume ( b ) /rrbracket ( ok : p ) = ok : ( p ∩ b ) , er : ∅ = ok : /llbracket assume ( b ) /rrbracket ok p , er : /llbracket assume ( b ) /rrbracket er p . ( r ≡ x : = nond () ): By definition, /llbracket x : = nond () /rrbracket ( ok : p ) = ok : ⋃ v ∈ Z p [ x ↦→ v ] , er : ∅ = ok : /llbracket x : = nond () /rrbracket ok p , er : /llbracket x : = nond () /rrbracket er p . ( r ≡ r 1; r 2): Let us assume the inductive hypotheses ∀ p ∈ S . /llbracket r 1 /rrbracket ( ok : p ) = ok : /llbracket r 1 /rrbracket ok p , er : /llbracket r 1 /rrbracket er p ∀ p ′ ∈ S . /llbracket r 2 /rrbracket ( ok : p ′ ) = ok : /llbracket r 2 /rrbracket ok p ′ , er : /llbracket r 2 /rrbracket er p ′ . Then, we have /llbracket r 1; r 2 /rrbracket ( ok : p ) = /llbracket r 2 /rrbracket ( /llbracket r 1 /rrbracket ( ok : p )) = /llbracket r 2 /rrbracket ( ok : /llbracket r 1 /rrbracket ok p , er : /llbracket r 1 /rrbracket er p ) = er : /llbracket r 1 /rrbracket er p ∪ /llbracket r 2 /rrbracket ( ok : /llbracket r 1 /rrbracket ok p ) = er : /llbracket r 1 /rrbracket er p ∪ ok : /llbracket r 2 /rrbracket ok ( /llbracket r 1 /rrbracket ok p ) , er : /llbracket r 2 /rrbracket er ( /llbracket r 1 /rrbracket ok p ) = er : /llbracket r 1 /rrbracket er p ∪ ok : ( /llbracket r 1 /rrbracket ok · /llbracket r 2 /rrbracket ok ) p ) , er : ( /llbracket r 1 /rrbracket ok · /llbracket r 2 /rrbracket er ) p ) = ok : ( /llbracket r 1; r 2 /rrbracket ok p ) , er : ( /llbracket r 1 /rrbracket er p ∪ ( /llbracket r 1 /rrbracket ok · /llbracket r 2 /rrbracket er ) p )) = ok : /llbracket r 1; r 2 /rrbracket ok p , er : /llbracket r 1; r 2 /rrbracket er p .
```

( r ≡ r 1 ⊕ r 2): Let us assume the inductive hypotheses

```
∀ p ∈ S . /llbracket r 1 /rrbracket ( ok : p ) = ok : /llbracket r 1 /rrbracket ok p , er : /llbracket r 1 /rrbracket er p , ∀ p ∈ S . /llbracket r 2 /rrbracket ( ok : p ) = ok : /llbracket r 2 /rrbracket ok p , er : /llbracket r 2 /rrbracket er p . Then, we have /llbracket r 1 ⊕ r 2 /rrbracket ( ok : p ) = /llbracket r 1 /rrbracket ( ok : p ) ∪ /llbracket r 2 /rrbracket ( ok : p ) = ( ok : /llbracket r 1 /rrbracket ok p , er : /llbracket r 1 /rrbracket er p ) ∪ ( ok : /llbracket r 2 /rrbracket ok p , er : /llbracket r 2 /rrbracket er p ) = ok : ( /llbracket r 1 /rrbracket ok p ∪ /llbracket r 2 /rrbracket ok p ) , er : ( /llbracket r 1 /rrbracket er p ∪ /llbracket r 2 /rrbracket er p ) = ok : /llbracket r 1 ⊕ r 2 /rrbracket ok p , er : /llbracket r 1 ⊕ r 2 /rrbracket er p . ( r ≡ r ∗ 1 ): Let us assume the inductive hypotheses ∀ p ∈ S . /llbracket r 1 /rrbracket ( ok : p ) = ok : /llbracket r 1 /rrbracket ok p , er : /llbracket r 1 /rrbracket er p . Then, we prove by induction on n ∈ N that ∀ n ∈ N . /llbracket r 1 /rrbracket n ( ok : p ) = ok : /llbracket r n 1 /rrbracket ok p , er : /llbracket r n 1 /rrbracket er p Finally, we have that /llbracket r ∗ 1 /rrbracket ( ok : p ) = ⋃ { /llbracket r 1 /rrbracket n ( ok : p ) | n ∈ N } = ⋃ { ( ok : /llbracket r n 1 /rrbracket ok p , er : /llbracket r n 1 /rrbracket er p ) | n ∈ N } = ok : ⋃ { /llbracket r n 1 /rrbracket ok p | n ∈ N } , er : ⋃ { /llbracket r n 1 /rrbracket er p | n ∈ N } = ok : /llbracket r ∗ 1 /rrbracket ok p , er : /llbracket r ∗ 1 /rrbracket er p .
```

This therefore concludes the proof.

□

Lemma 6.1 is instrumental for proving the equivalence between IL and the particular instance LCL A tr of our logic as determined by (i)-(iv) above. This correspondence necessarily follows as a consequence of the (logical) completeness of IL [O'Hearn 2020, Theorem 6] and our Theorem 5.14 of limited completeness, which guarantee that any under-approximation of the strongest postcondition post [ r ] p is provable in both logics.

```
Corollary 6.2. For any p , q , w ∈ S and r ∈ Reg : ⊢ IL [ p ] r [ ok : q ][ er : w ] iff ⊢ A tr [ ok : p ] r [ ok : q , er : w ] .
```

It is interesting to observe that any instance LCL A of our logic using an abstraction A /nequal A tr would only be able to derive some triples of IL but not all of them (while, of course, any triple derived in ⊢ A would also be derivable in ⊢ IL). This is a consequence of the intrinsic incompleteness Theorem 5.15 that extends the impossibility results of Giacobazzi et al. [2015] and Bruni et al. [2020] to regular commands. Therefore, whenever A /nequal A tr there will always exist some program r and some triple ⊢ IL [ p ] r [ ok : q ][ er : w ] such that it will not be possible to derive ⊢ A [ ok : p ] r [ ok : q , er : w ] because some proof obligation C A c ( e ) of local completeness will fail for some basic expression e appearing in r .

The correspondence provided by Corollary 6.2 is interesting, because although the rules of IL and ours share some similarities, they also display significant differences:

- (a) The most visible difference is that the pre-conditions of the triples in ⊢ IL are elements of S while pre-conditions of triples in ⊢ A tr are elements of C , meaning that the rules in ⊢ IL are concerned only with normal inputs, while the rules in ⊢ A tr must deal also with (the propagation of) erroneous inputs.

.

Fig. 9. Abstract domain Err.

<!-- image -->

- (b) Building on (a), the rules of IL are tailored to error propagation, while our rules are designed for any concrete domain. Both logical frameworks can be extended to deal with different kinds of error and error recovery mechanisms. Because our rule ( transfer ) is parametric on basic expressions, it should not be necessary to change any rule of our proof system to implement such extensions. For example, IL exploits two rules for sequential composition while LCL A just needs a single composition rule but it delegates error propagation to the underlying concrete domain.
- (c) Some rules of IL, such as Disjunction , Choice , and Iterate zero in O'Hearn [2020, Figure 2], are designed to incrementally build the under-approximation bottom-up by composing smaller under-approximations into larger ones. On the contrary, LCL A is constrained to work in the opposite direction by the requirement of preserving the over-approximation of the strongest post-condition in the abstraction A .
- (d) Finally, incorrectness logic includes specific rules for dealing with the introduction of fresh local variables, while in the context of abstract interpretation it is typically assumed that the program variables are statically known. Of course, it would be possible to deal with dynamic allocation in LCL A although its formalization would be technically more involved.

The use of an abstract over-approximation in LCL A that constrains any under-approximation has some advantages but also carries drawbacks. The main advantages are as follows: (1) by exploiting the over-approximation, LCL A can also prove the absence of errors and (2) under the hypothesis that the correctness specification spec is expressible in the abstraction A , any provable triple will suffice to establish either spec is satisfied or violated . However, as already mentioned, whenever A is not trivial, not all the possible under-approximations can be obtained by our system. The next example shows this phenomenon by combining the interval abstraction Int with the simple error domain Err depicted in Figure 9.

Example 6.3. Let us revisit Example 5.8 (in turn using the regular command r of Example 5.2). To study spec 2 ≜ x ≤ 1000, in the context of ⊢ IL we focus on the command ̂ r 2 ≜ r ; r s 2 where

```
r s 2 ≜ if x ≤ 1000 then skip else error () = ( x ≤ 1000?; skip ) ⊕ ( 1000 < x ?; error ()) .
```

Using ⊢ Int , it was shown in Example 5.8 that ⊢ Int is expressive enough to prove that r satisfies spec 2 , so that ̂ r 2 will never issue the error signal. Since the absence of errors cannot be proved by under-approximations, incorrectness logic cannot derive any useful information in this case. Let us consider instead the abstract domain Int + ≜ Err ⊓ Int defined as reduced product [Cousot and Cousot 1979, Section 10.1] of Err and Int , that is, whose concretization map is defined as γ Int + ( 〈 a 1 , a 2 〉 ) ≜ γ Err ( a 1 ) ∩ γ Int ( a 2 ) . By mimicking the derivation of ⊢ Int [ p ] r [ { 0 , 2 , 1000 } ], it is not hard to check that ⊢ Int + [ ok : p ] ̂ r 2 [ ok : { 0 , 2 , 1000 } ] is derivable. Since Int + ( ok : { 0 , 2 , 1000 } ) = ok :[0 , 1000] over-approximates the strongest post-condition, this is enough for proving that no error will be issued by ̂ r 2 with pre-condition p . Actually, by Corollary 5.6, since spec 2 is expressible in Int , we are guaranteed that any provable triple ⊢ Int [ p ] r [ q ] in our system will be able to prove that spec 2 holds.

Fig. 10. The rules for while loops.

<!-- formula-not-decoded -->

To study spec 3 ≜ 100 ≤ x , we focus on ̂ r 3 ≜ r ; r s 3 where s 3 ≜ ≤ ≤ ⊕

We know from Example 5.8, that /llbracket r /rrbracket p ⊈ spec 3 , so that ̂ r 3 can issue some errors. Within IL we can derive triples that exhibit some erroneous situation, like ⊢ IL [ p ] ̂ r 3 [ er : { 0 } ] as well as others that do not, e.g., ⊢ IL [ p ] ̂ r 3 [ ok : { 1000 } ].

Let us consider once again the abstract domain Int + . By mimicking the derivation of ⊢ Int [ p ] r [ { 0 , 2 , 1000 } ], but applying ( rec ) 100 times to include the values 100 and 101 that are necessary to satisfy the local completeness requirements for the tests 100 ≤ x ? and x &lt; 100?, we can then derive ⊢ Int + [ ok : p ] ̂ r 3 [ ok : { 1000 } , er : { 0 , 2 } ] using the abstract domain Int + . Note that, since Int + ( ok : { 1000 } , er : { 0 , 2 } ) = ⊤ :[0 , 1000], the rule ( relax ) cannot be used to discard all the errors because this would change the abstract over-approximation of the post-condition. Since ok :[100 , + ∞ ] is expressible in Int + , by Corollary 5.6, the label ⊤ in the over-approximation provides good evidence about the occurrence of one or more errors. Moreover, because the over-approximation induced by Int is always preserved, any provable triple ⊢ Int + [ p ] ̂ r 3 [ q ] is such that q will contain the true alarm er : { 0 } (as well as ok : { 1000 } ).

To develop some tool or extend existing ones to exploit LCL A the idea is to start the analysis with somewell-known abstract domain and then collect the local completeness proof obligations arising from the analysis: When they are not satisfied, then a new abstract domain must be synthesized to carry out the proof. As discussed in the conclusions, a successful strategy outlined in Bruni et al. [2022] would be to refine the current abstract domain in a minimal way to recover local completeness of the analysis.

## 7 Imp PROGRAMS

The encoding (6) of while loops as regular commands is such that, due to the recursive rule ( rec ) , proof obligations of local completeness for the Boolean guard of the loop are required at each iteration. This turns out to be advantageous to keep the rules of the logic as simple and straightforward as possible. However, this is not strictly necessary for achieving local completeness of the loop invariant. We therefore introduce in Figure 10 two additional rules for while loops that relax the local completeness requirements needed during their recursive applications. The key new rule is ( unroll ) : it is analogous to the rule ( rec ) when applied to r = b ?; c , but the premise ⊢ A [ p ∧ b ] c [ w ] of ( unroll ) requires local completeness exclusively on the body c of the loop and not on the Boolean guard b ?. Moreover, the rule ( loopinv ) is analogous to ( iterate ) and can be used to stop a proof attempt as soon as an abstract fixpoint A ( p ) is reached. By combining these rules ( unroll ) and ( loopinv ) , the local completeness requirements for the Boolean guard b ? of the loop, namely C A p ( b ? ) and C A p ( ¬ b ? ) , are therefore needed only at the last iteration and not at each iteration.

Lemma 7.1. The proof system extended with rules ( unroll ) and ( loopinv ) is sound.

Proof. We extend the proof by induction of Theorem 5.5 by considering the case where the last rule applied to derive ⊢ A [ p ] r [ q ] is either ( unroll ) or ( loopinv ) . As in the proof of Theorem 5.5, we refer to the equality /llbracket r /rrbracket ♯ A α ( p ) = α ( q ) as (2a) and use (2b) for the equality /llbracket r /rrbracket ♯ A α ( p ) = α ( /llbracket r /rrbracket p ) , and we recall that (2b) follows immediately by (1) and (2a).

( unroll ) : If the last rule applied is ( unroll ) , then it must be r ≡ while b do c , and we can assume by induction that ⊢ A [ p ∧ b ] c [ w ] and ⊢ A [ p ∨ w ] while b do c [ q ] can be derived for some w . We need to prove the thesis for the conclusion ⊢ A [ p ] while b do c [ q ].

- (1) By inductive hypothesis (1), we have that w ≤ /llbracket c /rrbracket ( p ∧ b ) = /llbracket b ?; c /rrbracket p , so that, by Lemma 2.1 (e), it follows /llbracket ( b ?; c ) ∗ /rrbracket p = /llbracket ( b ?; c ) ∗ /rrbracket ( p ∨ w ) . Then, by inductive hypothesis (1), we derive the following:

<!-- formula-not-decoded -->

- (2) The proof is analogous to the case of rule ( rec ) in the proof of Theorem 5.5:

<!-- formula-not-decoded -->

so that /llbracket while b do c /rrbracket ♯ A α ( p ) = α ( q ) = α ( /llbracket while b do c /rrbracket p ) follows.

( loopinv ) : If the last rule applied is ( loopinv ) , then it must be r ≡ while b do c , and we can assume by induction that ⊢ A [ p ∧ b ] c [ q 1] can be derived for some q 1 such that q 1 ≤ A ( p ) and q = ( p ∨ q 1 ) ∧¬ b , with C A p ( b ) and C A p ( ¬ b ) . We need to prove the thesis for the conclusion ⊢ A [ p ] while b do c [ ( p ∨ q 1 ) ∧ ¬ b ].

(1) We first observe that, by inductive hypothesis (1), q 1 ≤ /llbracket c /rrbracket ( p ∧ b ) = /llbracket b ?; c /rrbracket p and that /llbracket b ?; c /rrbracket 0 p = p . Then

<!-- formula-not-decoded -->

From this, it immediately follows by monotonicity of /llbracket ¬ b /rrbracket :

<!-- formula-not-decoded -->

(2a) By C A p ( b ) , we get α ( p ∧ b ) = α ( /llbracket b /rrbracket p ) = /llbracket b /rrbracket ♯ A α ( p ) . Therefore, α ( q 1 ) = /llbracket c /rrbracket ♯ A α ( p ∧ b ) = /llbracket c /rrbracket ♯ A /llbracket b /rrbracket ♯ A α ( p ) = /llbracket b ?; c /rrbracket ♯ A α ( p ) . By monotonicity of α , we have that α ( q 1 ) ≤ A α ( p ) , so that Lemma 2.1 (c) is applicable to derive /llbracket ( b ?; c ) ∗ /rrbracket ♯ A α ( p ) = α ( p ) . Since C A p ( ¬ b ) and p ≤ ( p ∨ q 1 ) ≤ A ( p ) hold, by convexity, we get that C A ( p ∨ q 1 ) ( ¬ b ) holds. Therefore,

<!-- formula-not-decoded -->

□

Werefer to the next section for an example (cf. Example 8.2) showing the advantage of applying the rules ( unroll ) and ( loopinv ) because the local completeness requirements are not met at every iteration of the proof for a while loop but just at the last one.

Fig. 11. The refinement rule of LCL ⪯ A .

## 8 A LOGIC FOR LOCALLY COMPLETE BEST CORRECT APPROXIMATIONS

When a provable triple ⊢ A [ p ] r [ q ] is used for program verification, we exploit the following property:

<!-- formula-not-decoded -->

so that, by under-approximation q ≤ /llbracket r /rrbracket p , any alarm in q is a true alarm for p , and, by overapproximation /llbracket r /rrbracket p ≤ α ( q ) , the lack of alarms in α ( q ) entails the correctness of p . In LCL A , local completeness can be viewed as a technical assumption to infer ( § ), meaning that it is a necessary condition for deriving ⊢ A [ p ] r [ q ] within our proof system, since we are able to prove only triples that satisfy local completeness /llbracket r /rrbracket ♯ A α ( p ) = α ( /llbracket r /rrbracket p ) (cf. Theorem 5.5). In this section, we show that it is possible to relax our program logic so that local completeness is not required for the intensional and inductively defined abstract interpreter /llbracket r /rrbracket ♯ A but merely for the best correct approximation /llbracket r /rrbracket A ≜ α ◦ /llbracket r /rrbracket ◦ γ of the extensional concrete semantics /llbracket r /rrbracket . This is achieved by allowing different abstract domains in different sub-derivations to increase the precision of the analysis whenever necessary. Without the extension proposed in this section, whenever it would be convenient to use different abstract domains for different parts of the proof, the only possibility would be to check if it is possible to complete the derivation in the abstract domain obtained as the reduced product of all domains involved in every sub-derivation: For example, if we are able to derive ⊢ A 1 [ p ] r 1 [ w ] and ⊢ A 2 [ w ] r 2 [ q ], then we could try to derive ⊢ A 1 ⊓ A 2 [ p ] r 1; r 2 [ q ] leveraging the reduced product A 1 ⊓ A 2. One remarkable advantage of using different abstractions within the same derivation will be that it is not necessary to consider their join at every step.

This extension of LCL A is obtained by adding the rule ( refine ) in Figure 11, where we recall that ⪯ denotes the refinement relation between abstract domains and write ⊢ ⪯ A [ p ] r [ q ] for a triple that can be derived in this extended proof system LCL ⪯ A ≜ LCL A ∪ { ( refine ) } . When A is not locally complete for r on p , ( refine ) allows us to exploit an abstraction refinement A ′ of A , which is locally complete provided that the over-approximations in A and A ′ of both p and q coincide. The soundness result for LCL ⪯ A shows that any triple ⊢ ⪯ A [ p ] r [ q ] still ensures that q ≤ /llbracket r /rrbracket p ≤ α ( q ) holds. Let us remark that the only difference in soundness of LCL A and LCL ⪯ A , as stated by Theorems 5.5 and 8.1, is that the intensional abstract semantics /llbracket r /rrbracket ♯ A of Theorem 5.5 is replaced by the bca /llbracket r /rrbracket A of Theorem 8.1.

Theorem 8.1 (Soundness of LCL ⪯ A ). Let A α , γ ∈ Abs ( C ) . For all r ∈ Reg , p , q ∈ C , if ⊢ ⪯ A [ p ] r [ q ] then:

<!-- formula-not-decoded -->

Proof. As in the proof of Theorem 5.5, we refer to the equality /llbracket r /rrbracket A α ( p ) = α ( q ) as (2a) and use (2b) for the equality /llbracket r /rrbracket A α ( p ) = α ( /llbracket r /rrbracket p ) . We then recall that (2b) follows immediately by (1) and (2a).

The proof is by induction on the derivation tree of ⊢ ⪯ A [ p ] r [ q ]. For the cases where the last used rule is in LCL A (in Figure 4), the proof follows the same pattern of the proof of Theorem 5.5: for (1) there is nothing to change, while for (2) we just need to replace /llbracket · /rrbracket ♯ A with /llbracket · /rrbracket A

everywhere and slightly change the proof of (2a) for the sequence with the additional inequality /llbracket r 1; r 2 /rrbracket A α ( p ) ≤ A /llbracket r 2 /rrbracket A ( /llbracket r 1 /rrbracket A α ( p )) as follows:

```
α ( q ) ≤ A [by (1) and monotonicity of α ] α ( /llbracket r 1; r 2 /rrbracket p ) ≤ A [by correctness (4)] /llbracket r 1; r 2 /rrbracket A α ( p ) ≤ A [by definition] /llbracket r 2 /rrbracket A ( /llbracket r 1 /rrbracket A α ( p )) = [by ind.hyp. (2a), /llbracket r 1 /rrbracket A α ( p ) = α ( w ) ] /llbracket r 2 /rrbracket A α ( w ) = [by ind.hyp. (2a)] α ( q ) .
```

Analogously, we slightly change the proof of (2a) for ( iterate ) as follows:

```
/llbracket r ∗ 1 /rrbracket A α ( p ) = [by Lemma 2.1 (d)] α ( p ) = [by hyp. q ≤ A ( p ) ] α ( p ) ∨ A α ( q ) = [by additivity of α ] α ( p ∨ q ) .
```

Instead, no changes are necessary for the join, because the abstract semantics of the choice command preserves bcas (cf. Equation (5)).

Therefore, to conclude, we just need to consider the case for the new rule ( refine ) :

( refine ) : If the last rule applied is ( refine ) , then we can assume by induction that ⊢ ⪯ A ′ [ p ] r [ q ] for some abstraction refinement A ′ ⪯ A such that A ′ ( p ) = A ( p ) and A ′ ( q ) = A ( q ) . We need to prove the thesis for the conclusion ⊢ ⪯ A [ p ] r [ q ].

- (1) By inductive hypothesis (1) we already have that q ≤ /llbracket r /rrbracket p holds.
- (2) Let us recall that /llbracket r /rrbracket A α ( p ) = α ( /llbracket r /rrbracket A ( p )) . We first note that, by inductive hypothesis (2a), α ′ ( /llbracket r /rrbracket A ′ ( p )) = α ′ ( q ) , so that /llbracket r /rrbracket A ′ ( p ) ≤ A ′ ( q ) holds. Therefore:

<!-- formula-not-decoded -->

so that, /llbracket r /rrbracket A α ( p ) = α ( q ) = α ( /llbracket r /rrbracket p ) follows.

□

The following example shows how the rule ( refine ) allows us to infer a triple ⊢ ⪯ A [ p ] r [ q ] when /llbracket r /rrbracket ♯ A is not locally complete for A on p , i.e., soundness as stated by Theorem 5.5 does not hold, while the best correct approximation /llbracket r /rrbracket A turns out to be locally complete. Interestingly, the rule ( refine ) allows us to combine sub-derivations that are computed in different abstractions without the need to resort to a common more precise abstract domain such as their reduced product.

Example 8.2 (Benefits of ( refine ) ). Let us consider the Imp program c ≜ c 1; c 2, where c 1 ≜ y : = ( 2 ∗ y ) + 1; AbsVal ( y ) , c 2 ≜ x : = y ; c 3 c 3 ≜ while x &gt; 1 do { x : = x -1; y : = max ( 0 , y -1 ) } , using the syntactic sugar

<!-- formula-not-decoded -->

Consider the pre-condition p ≜ y ∈ [ -101 , 100]. It turns out that the interval domain A ≜ Int is not locally complete, because

<!-- formula-not-decoded -->

while

```
/llbracket c /rrbracket α ( p ) = /llbracket c 2 /rrbracket ( /llbracket c 1 /rrbracket ( y ∈ [ -101 , 100] )) = /llbracket c 2 /rrbracket ( /llbracket AbsVal ( y ) /rrbracket ( /llbracket y : = ( 2 ∗ y ) + 1 /rrbracket ( y ∈ [ -101 , 100] ))) = /llbracket c 2 /rrbracket ( /llbracket AbsVal ( y ) /rrbracket ( y ∈ [ -201 , 201] ∧ y odd )) = /llbracket c 3 /rrbracket ( /llbracket x : = y /rrbracket ( y ∈ [1 , 201] ∧ y odd )) = /llbracket c 3 /rrbracket ( x = y ∧ y ∈ [1 , 201] ∧ y odd ) = /llbracket x ≤ 1? /rrbracket ( /llbracket ( x > 1?; x : = x -1; y : = max ( 0 , y -1 )) ∗ /rrbracket ( x = y ∧ y ∈ [1 , 201] ∧ y odd )) = /llbracket x ≤ 1? /rrbracket ( x = y ∧ y ∈ [1 , 201] ) = x ∈ [1 , 1] ∧ y ∈ [1 , 1] ,
```

and thus /llbracket c /rrbracket A α ( p ) = α ( /llbracket c /rrbracket A ( p )) = α ( /llbracket c /rrbracket p ) = x ∈ [1 , 1] ∧ y ∈ [1 , 1]. Therefore, by Theorem 5.5 (2), it is not possible to derive in LCL A a triple ⊢ A [ p ] c [ q ], for any q . However, we show that, in this case, we can successfully resort to the rule ( refine ) to infer the triple ⊢ ⪯ A [ p ] c [ q ] with q ≜ x = 1 ∧ y = 1. To achieve this, we identify two suitable refinements of Int that are used in different subtrees of the logical derivation of ⊢ ⪯ A [ p ] c [ q ]. The lack of local completeness in Int is due to two reasons:

- (i) the presence of the value 0 introduced in the over-approximation of c 1;
- (ii) the linear relationship x = y between the variables x and y after the assignment x : = y cannot be expressed in a nonrelational abstraction such as Int .

To address (i), we enrich the interval abstraction by adding a new abstract value Z /nequal 0 expressing x /nequal 0. Let A 1 denote the Moore closure of Int with this additional point Z /nequal 0, so that A 1 contains all the intervals possibly having a 'hole' in 0 (see Example 4.6). Using A 1 ⪯ A , we can infer the triple ⊢ A 1 [ p ] c 1 [ w ] in LCL A 1 , where the post-condition is w ≜ y ∈ { 1 , 3 , 201 } , as shown by the proof in Figure 12, where the application of the rules is quite straightforward. In particular, note the use of rule ( relax ) to reduce the number of concrete points in the under-approximation and the inclusion of the value 3 in w , which will be useful for accelerating the convergence in the successive part of the proof carried out in a second abstraction refinement A 2.

To address (ii), we consider the well-known weakly relational abstract domain A 2 ≜ Oct of octagons [Miné 2006]. Oct consists of octagonal constraints between two variables x , y of type ± x ± y ≤ k and interval constraints of type ± x ≤ k , where k ∈ Z ∪ {-∞ , + ∞} , while the representation of the abstract values in Oct relies on difference bound matrices. 〈 Oct , ⊆〉 is a complete lattice and is defined by a GI such that, for all X ∈ ℘ ( Q n ) , Oct ( X ) is the least octagon containing X . Using A 2 it is possible to derive the triple ⊢ A 2 [ w ] c 2 [ q ] in LCL A 2 , as shown in Figure 13, where

Fig. 12. Derivation of ⊢ A 1 [ p ] c 1 [ w ] for Example 8.2, with w 1 ≜ y ∈ {-201 , -3 , -1 , 1 , 3 , 201 } .

Fig. 13. Derivation of ⊢ A 2 [ w ] x : = y ; c 2 [ q ] for Example 8.2, with w 2 ≜ y ∈ { 1 , 2 , 3 , 200 , 201 } and w 3 ≜ y ∈ { 2 , 3 , 200 , 201 } .

c 4 ≜ x : = x -1; y : = max ( 0 , y -1 ) is the loop body. This derivation provides an example of use of the rules ( unroll ) and ( loopinv ) , discussed in Section 7, in lieu of ( rec ) and ( iterate ) : In fact, the local completeness for the Boolean guard x &gt; 1 of c 2 is not satisfied at each iteration but only when the abstract invariant is computed.

Finally, these two proofs ⊢ A 1 [ p ] c 1 [ w ] and ⊢ A 2 [ w ] c 2 [ q ] can be combined using ( refine ) twice and then ( seq ) to infer ⊢ ⪯ A [ p ] c [ q ] in LCL ⪯ A as follows:

<!-- image -->

Note that, while the bounds of the interval p = [ -101 , 100] have been chosen so to ease the derivation, the same example would apply to any (finite) input p that contains at least a negative and a positive number.

Let us remark how the above example shows the ability of rule ( refine ) of carrying out different parts of a proof in some abstraction refinements of a domain A in a situation where local completeness would fail in the original abstraction A . Here, the combined use of two refinements A 1 and A 2 turns out to be more convenient than carrying out the whole proof in a more concrete domain that could be designed, e.g., as reduced product of A 1 and A 2, because this latter domain would not necessarily be locally complete for the whole program.

## 9 RELATED WORK

As mentioned, de Vries and Koutavas [2011] were the first to introduce under-approximation triples by proposing the backward consequence rule in reverse Hoare logic for the analysis of non-deterministic algorithms, e.g., for array shuffle. Later, the idea of defining a logic of underapproximation has been fully developed into the design of Incorrectness Logic [O'Hearn 2020], whose comparison with our work has been fully investigated in Section 6. Incorrectness logic attracted a lot of research interest and originated a recent strand of work that aims to exploit incorrectness triples for catching memory errors by moving under-approximating reasoning to separation logic for pointer analysis [Le et al. 2022; Maksimovic et al. 2022; Poskitt 2021; Poskitt and Plump 2023; Raad et al. 2020, 2022; Yan et al. 2022]. The ability of incorrectness triples for compositional bug finding strategies has been practically shown by Le et al. [2022], where 15 new real bugs in OpenSSL were discovered and reported to OpenSSL maintainers thanks to Pulse-X, an automatic program analysis tool based on incorrectness separation logic (ISL) [Raad et al. 2020]. Of course, the main benefit of Pulse-X is that all reported errors are true positives. The work by Raad et al. [2022] extends the above bug catching theory to concurrent programs by defining a parametric framework able to deal with race detection, deadlock detection, and memory safety error detection. Exact separation logic (ESL) [Maksimovic et al. 2022] relies on similar ideas but defines exact triples, in the sense that the consequences are at the same time an under- and over-approximation of the semantics: while the ISL quadruple [ p ] r [ ok : q ][ er : w ] asserts that any state satisfying either the success post-condition or the error post-condition is the outcome of executing the command r from some state satisfying the pre-condition p , the ESL quadruple ( p ) r ( ok : q )( er : w ) additionally guarantees that any terminating execution of r starting from a state satisfying the pre-condition p either leads to a success state that satisfies q or raises some fault in a state that satisfies w . A major difference is therefore that valid ISL quadruples [ p ] r [ ok : q ][ er : w ] can always be split into valid triples of the form [ p ] r [ ok : q ] and [ p ] r [ er : w ], while ESL quadruples ( p ) r ( ok : q )( er : w ) are atomic because they must account for all behaviours. Our conjecture is that ESL accounts for the case of LCL A where the trivial identity abstraction is considered, but to confirm this intuition we first plan to explore whether and how the relationship of LCL A with IL studied in Section 6 could be extended to ISL [Raad et al. 2020]. The main challenge for achieving this extension will be to engineer a suitable frame rule for heap assertions that is able to preserve local completeness for the abstraction A .

Recently, Zilberstein et al. [2023] put forward Outcome Logic (OL), a generalization of Hoare Logic that is able to find true bugs while preserving the ability of proving programs correct. OL is parametric on a monoidal structure for predicates and on a so-called outcome assertion logic, and this enables correctness and incorrectness reasoning within the same program logic. OL does not consider the chance of abstracting the predicates as we do in LCL A , so that we envisage that this challenge can be an appealing subject for future work.

Kleene algebras with tests (KAT) enriched by forward and backward box and diamond operators, so-called modal KATs, have been exploited to unify correctness and incorrectness logics in a single algebraic framework [Möller et al. 2021]. Möller and Struth [2006] already formalized the symmetries of forward and backward box and diamond operators as Galois connections, complementarities and dualities, and provided algebraic soundness and completeness proofs for Hoare logic. Later, Möller et al. [2021] showed that modal KATs with countable joins of tests can also embed incorrectness logic and can be used to draw some links between correctness and incorrectness specifications as well as to deal with backward under-approximations. Recently, Zhang et al. [2022] have shown that O'Hearn incorrectness logic cannot be formulated within a conventional KAT, but, at the same time, a full fledged modal KAT is not needed. In fact, Zhang et al. [2022] prove that a KAT including a greatest element, so-called TopKAT, is capable to encode both Hoare and O'Hearn program logics in a purely equational fashion. Milanese and Ranzato [2022] gave a further contribution within this stream of works by showing how KATs extended either with a modal diamond operator or with a top element are able to encode our local completeness logic LCL A . Thus, this latter result generalizes both the modal KAT [Möller et al. 2021] and TopKAT [Zhang et al. 2022] approaches for encoding Hoare correctness and O'Hearn incorrectness logics.

Regarding the use of under-approximation in abstract interpretation, Cousot and Cousot introduced the general framework that could be used to study both over- and under-approximations already in their seminal work [Cousot and Cousot 1977]. However, to the extent of our knowledge, there are no abstract domains thought from the ground up for under-approximation in forward program analysis. The main problems in designing significant abstract domains for under-approximation have been recently studied by Ascari et al. [2022].

## 10 CONCLUSION AND FUTURE WORK

We presented a program logic for locally complete abstract interpretations, called LCL A and parametric on an abstract domain A . LCL A can prove the presence as well as the absence of true alarms , meaning that proofs in LCL A are potentially able to infer both the correctness and incorrectness of some program specification. As far as we know, LCL A combines for the first time over- and under-approximations in a logical proof system for programs based on abstract interpretation. We think that this work opens up many promising lines of research for the automatic verification of program correctness and incorrectness.

When some proof obligation C A p ( f ) about the local completeness in the abstract domain A of some basic transfer function f fails, a natural question is whether it is possible to transform A into some A ′ to satisfy C A ′ p ( f ) and conclude the derivation in ⊢ A ′ . In particular, following [Filé et al. 1996; Giacobazzi and Ranzato 1997; Giacobazzi et al. 2000], we are interested in the problem of minimally transforming the abstract domain A to A ′ through refinements (i.e., by adding concrete values) and simplifications (i.e., by removing abstract values) to make A ′ locally complete for a set of basic transfer functions. This problem has been studied recently in [Bruni et al. 2022] where we proved that in general there is no unique minimal solution to the problem of abstract domain refinement for local completeness and a forward/backward strategy for optimally refining the abstract domain to achieve local completeness has been introduced. As sketched in Example 5.9, in program verification the strategy would be to iteratively transform the original abstract domain A 0 stepping through a sequences of abstract domains A 1 , . . . , A n , until a derivation ⊢ A n [ p ] r [ q ] can be completed in A n . Each domain A i + 1 can be designed by looking at the proof obligations of local completeness that fail in the attempt to prove ⊢ A i [ p ] r [ q ] using the current abstract domain A i . Notably, different abstraction refinements could be used by applying the rule ( refine ) of the extended proof system LCL ⪯ A , introduced in Section 8, in different subtrees of the same derivation.

Wealso aim at investigating extensions of our proof system with non-compositional rules for programs. Here, the incompleteness for a statement r may turn to completeness for an extensionally equivalent statement r ′ such that /llbracket r /rrbracket = /llbracket r ′ /rrbracket . For example, a command such as x : = xy + 1; x : = x -1 is incomplete for a simple sign analysis in Sign ± ≜ { ∅ , Z &lt; 0 , Z = 0 , Z &gt; 0 , Z } because

<!-- formula-not-decoded -->

Nevertheless, when considering an equivalent statement such as x : = xy , we achieve a complete sign analysis because /llbracket x : = xy /rrbracket ♯ Sign ± 〈 x / Z &gt; 0 , y / Z &gt; 0 〉 = 〈 x / Z &gt; 0 , y / Z &gt; 0 〉 . Patterns of this kind could be handled by a noncompositional rule for manipulating assignments such as

<!-- formula-not-decoded -->

Because x : = ( x -1 ) [ xy + 1 / x ] ≡ x : = xy + 1 -1 ≡ x : = xy , from ⊢ Sign ± [ 〈 x / Z &gt; 0 , y / Z &gt; 0 〉 ] x : = xy [ 〈 x / Z &gt; 0 , y / Z &gt; 0 〉 ], we would be able to derive ⊢ Sign ± [ 〈 x / Z &gt; 0 , y / Z &gt; 0 〉 ] x : = xy + 1; x : = x -1 [ 〈 x / Z &gt; 0 , y / Z &gt; 0 〉 ].

While completeness of abstract transfer functions is preserved by function composition, as encoded by the rule ( seq ) of LCL A , one major issue of abstract interpretation is that best correct approximations are not compositional, i.e., the composition of abstract predicate transformers may not be as precise as the abstraction of their concrete composition [Reps et al. 2004; Yorsh et al. 2004]. The lack of composition for bcas has practical consequences, because the precision of a program analysis strictly depends on the granularity of program decomposition into atomic operations. Finer decompositions commonly induce more imprecise analyses, while coarser decompositions may enhance the chance of designing bcas for larger code blocks. We plan to investigate a proof system for the property of being a bca , notably for proving when the composition of bcas is a bca.

## ACKNOWLEDGMENTS

We are grateful to the anonymous reviewers for their helpful comments.

## REFERENCES

- Flavio Ascari, Roberto Bruni, and Roberta Gori. 2022. Limits and difficulties in the design of under-approximation abstract domains. In Proceedings of 25th International Conference on Foundations of Software Science and Computation Structures, (FOSSACS'22), Lecture Notes in Computer Science , Patricia Bouyer and Lutz Schröder (Eds.), Vol. 13242. Springer, 21-39. https://doi.org/10.1007/978-3-030-99253-8\_2
- Thomas Ball, Todd D. Millstein, and Sriram K. Rajamani. 2005. Polymorphic predicate abstraction. ACM Trans. Program. Lang. Syst. 27, 2 (2005), 314-343. https://doi.org/10.1145/1057387.1057391
- [François Bourdoncle. 1993. Abstract debugging of higher-order imperative languages. In Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI'93) . ACM, 46-55. https://doi.org/10.1145/155090. 155095](https://doi.org/10.1145/155090.155095)
- Roberto Bruni, Roberto Giacobazzi, Roberta Gori, Isabel Garcia-Contreras, and Dusko Pavlovic. 2020. Abstract extensionality: On the properties of incomplete abstract interpretations. In Proceedings of the ACM Symposium on Principles of Programming Languages . 28:1-28:28. https://doi.org/10.1145/3371096
- Roberto Bruni, Roberto Giacobazzi, Roberta Gori, and Francesco Ranzato. 2021. A logic for locally complete abstract interpretations. In Proceedings of the 36th Annual ACM/IEEE Symposium on Logic in Computer Science (LICS'21), Distinguished Paper. IEEE, 1-13. https://doi.org/10.1109/LICS52264.2021.9470608
- Roberto Bruni, Roberto Giacobazzi, Roberta Gori, and Francesco Ranzato. 2022. Abstract interpretation repair. In Proceedings of the 43rd ACM SIGPLAN International Conference on Programming Language Design and Implementation (PLDI'22) , Ranjit Jhala and Isil Dillig (Eds.). ACM, 426-441. https://doi.org/10.1145/3519939.3523453
- [Cristiano Calcagno, Dino Distefano, Jérémy Dubreil, Dominik Gabi, Pieter Hooimeijer, Martino Luca, Peter W. O'Hearn, Irene Papakonstantinou, Jim Purbrick, and Dulma Rodriguez. 2015. Moving fast with software verification. In Proceedings of the NASA Formal Methods Symposium (NFM'15), LNCS , Vol. 9058. Springer, 3-11. https://doi.org/10.1007/978-3-31917524-9\_1](https://doi.org/10.1007/978-3-319-17524-9_1)
- Patrick Cousot. 2021. Principles of Abstract Interpretation . MIT Press.
- Patrick Cousot and Radhia Cousot. 1977. Abstract interpretation: A unified lattice model for static analysis of programs by construction or approximation of fixpoints. In Proceedings of the ACM Symposium on Principles of Programming Languages (POPL'77) . ACM, 238-252. https://doi.org/10.1145/512950.512973
- Patrick Cousot and Radhia Cousot. 1979. Systematic design of program analysis frameworks. In Proceedings of the ACM Symposium on Principles of Programming Languages (POPL'79) . ACM, 269-282. https://doi.org/10.1145/567752.567778
- [Patrick Cousot and Radhia Cousot. 1992. Abstract interpretation frameworks. J. Logic Comput. 2, 4 (1992), 511-547. https: //doi.org/10.1093/logcom/2.4.511](https://doi.org/10.1093/logcom/2.4.511)
- Patrick Cousot, Roberto Giacobazzi, and Francesco Ranzato. 2018. Program analysis is harder than verification: A computability perspective. In Proceedings of the 30th International Conference on Computer Aided Verification (CAV'18) Lecture Notes in Computer Science , Vol. 10982. Springer, 75-95. https://doi.org/10.1007/978-3-319-96142-2\_8
- Edsko de Vries and Vasileios Koutavas. 2011. Reverse Hoare logic. In Proceedings of the International Conference on Software Engineering and Formal Methods (SEFM'11) . Springer, 155-171. https://doi.org/10.1007/978-3-642-24690-6\_12
- Edsger W. Dijkstra. 1972a. Chapter I: Notes on Structured Programming . Academic Press Ltd., GBR, 1-82.

- [Edsger W. Dijkstra. 1972b. The humble programmer. Commun. ACM 15, 10 (1972), 859-866. https://doi.org/10.1145/355604. 361591](https://doi.org/10.1145/355604.361591)

Edsger W. Dijkstra. 1972c. Turing Award Lecture. Retrieved from https://www.youtube.com/watch?v=6sIlKP2LzbA.

- Dino Distefano, Manuel Fähndrich, Francesco Logozzo, and Peter W. O'Hearn. 2019. Scaling static analyses at Facebook. Commun. ACM 62, 8 (2019), 62-70. https://doi.org/10.1145/3338112
- G. Filé, R. Giacobazzi, and F. Ranzato. 1996. A unifying view of abstract domain design. ACM Comput. Surv. 28, 2 (1996), 333-336. https://doi.org/10.1145/234528.234742
- Robert W. Floyd. 1967. Assigning meanings to programs. In Proceedings of the Symposium on Applied Mathematics , Vol. 19, 19-32.
- [Roberto Giacobazzi, Francesco Logozzo, and Francesco Ranzato. 2015. Analyzing program analyses. In Proceedings of the 42nd Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL'15) . 261-273. https: //doi.org/10.1145/2676726.2676987](https://doi.org/10.1145/2676726.2676987)
- Roberto Giacobazzi and Francesco Ranzato. 1996. Compositional optimization of disjunctive abstract interpretations. In Proceedings of 6th European Symposium on Programming (ESOP'96), Lecture Notes in Computer Science , Vol. 1058. Springer, 141-155. https://doi.org/10.1007/3-540-61055-3\_34
- Roberto Giacobazzi and Francesco Ranzato. 1997. Completeness in abstract interpretation: A domain perspective. In Proceedings of the 6th International Conference on Algebraic Methodology and Software Technology (AMAST'97), Lecture Notes in Computer Science , Vol. 1349. Springer, 231-245. https://doi.org/10.1007/BFb0000474
- Roberto Giacobazzi and Francesco Ranzato. 1998. Optimal domains for disjunctive abstract intepretation. Sci. Comput. Program. 32, 1-3 (1998), 177-210. https://doi.org/10.1016/S0167-6423(97)00034-8
- Roberto Giacobazzi and Francesco Ranzato. 2022. History of abstract interpretation. IEEE Ann. Hist. Comput. 44, 2 (2022), 33-43. https://doi.org/10.1109/MAHC.2021.3133136
- Roberto Giacobazzi, Francesco Ranzato, and Francesca Scozzari. 1998. Complete abstract interpretations made constructive. In Proceedings of the 23rd International Symposium on Mathematical Foundations of Computer Science (MFCS'98), Lecture Notes in Computer Science , Vol. 1450. Springer, 366-377. https://doi.org/10.1007/BFb0055786
- Roberto Giacobazzi, Francesco Ranzato, and Francesca Scozzari. 2000. Making abstract interpretation complete. J. ACM 47, 2 (March 2000), 361-416. https://doi.org/10.1145/333979.333989
- [Charles A. R. Hoare. 1969. An axiomatic basis for computer programming. Commun. ACM 12, 10 (1969), 576-580. https: //doi.org/10.1145/363235.363259](https://doi.org/10.1145/363235.363259)
- Charles A. R. Hoare. 2003. The verifying compiler: A grand challenge for computing research. J. ACM 50, 1 (2003), 63-69. https://doi.org/10.1145/602382.602403
- Cliff Jones, Peter O'Hearn, and Jim Woodcock. 2006. Verified software: A grand challenge. IEEE Comput. 39, 04 (2006), 93-95. https://doi.org/10.1109/MC.2006.145
- Jacques-Henri Jourdan, Vincent Laporte, Sandrine Blazy, Xavier Leroy, and David Pichardie. 2015. A formally-verified C static analyzer. In Proceedings of the 42nd Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL'15) . 247-259. https://doi.org/10.1145/2676726.2676966
- [Dexter Kozen. 1997. Kleene algebra with tests. ACM Trans. Program. Lang. Syst. 19, 3 (May 1997), 427-443. https://doi.org/ 10.1145/256167.256195](https://doi.org/10.1145/256167.256195)
- Quang Loc Le, Azalea Raad, Jules Villard, Josh Berdine, Derek Dreyer, and Peter W. O'Hearn. 2022. Finding real bugs in big programs with incorrectness logic. In Proceedgins of the ACM SIGPLAN International Conference on Object-Oriented Programming Systems, Languages, and Applications (OOPSLA'22), Vol. 6, 1-27. https://doi.org/10.1145/3527325
- Xavier Leroy. 2006. Formal certification of a compiler back-end or: Programming a compiler with a proof assistant. In Proceedings of the 33rd ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL'06) . 42-54. https://doi.org/10.1145/1111037.1111042
- Petar Maksimovic, Caroline Cronjäger, Julian Sutherland, Andreas Lööw, Sacha-Élie Ayoun, and Philippa Gardner. 2022. Exact separation logic. arXiv.2208.07200. Retrieved from https://arxiv.org/abs/2208.07200.
- John McCarthy. 1962. Towards a mathematical science of computation. In IFIP Congress . 21-28.
- [Marco Milanese and Francesco Ranzato. 2022. Local completeness logic on Kleene algebra with tests. In Proceedings of the 29th International Static Analysis Symposium (SAS'22), LNCS , Vol. 13790. 350-371. https://doi.org/10.1007/978-3-03122308-2\_16](https://doi.org/10.1007/978-3-031-22308-2_16)
- [Antoine Miné. 2006. The octagon abstract domain. High. Order Symb. Comput. 19, 1 (2006), 31-100. https://doi.org/10.1007/ s10990-006-8609-1](https://doi.org/10.1007/s10990-006-8609-1)
- Antoine Miné. 2017. Tutorial on static inference of numeric invariants by abstract interpretation. Found. Trends Program. Lang. 4, 3-4 (2017), 120-372. https://doi.org/10.1561/2500000034
- Antoine Miné. 2014. Backward under-approximations in numeric abstract domains to automatically infer sufficient program conditions. Sci. Comput. Program. 93 (2014), 154-182. https://doi.org/10.1016/j.scico.2013.09.014

- Bernhard Möller, Peter W. O'Hearn, and Charles A. R. Hoare. 2021. On algebra of program correctness and incorrectness. In Proceedings of the 19th International Conference on Relational and Algebraic Methods in Computer Science (RAMiCS'21), Lecture Notes in Computer Science , Uli Fahrenberg, Mai Gehrke, Luigi Santocanale, and Michael Winter (Eds.), Vol. 13027. Springer, 325-343. https://doi.org/10.1007/978-3-030-88701-8\_20
- Bernhard Möller and Georg Struth. 2006. Algebras of modal operators and partial correctness. Theor. Comput. Sci. 351, 2 (2006), 221-239. https://doi.org/10.1016/j.tcs.2005.09.069
- Peter W. O'Hearn. 2018. Continuous reasoning: Scaling the impact of formal methods. In Proceedings of the ACM/IEEE Symposium on Logic in Computer Science (LICS'18) . ACM, 13-25. https://doi.org/10.1145/3209108.3209109
- Peter W. O'Hearn. 2020. Incorrectness logic. In Proceedings of the ACM Annual Symposium on Principles of Programming Languages, Vol. 4, 10:1-10:32. https://doi.org/10.1145/3371078
- Benjamin Pierce. 2002. Types and Programming Languages . MIT Press.
- [Christopher M. Poskitt. 2021. Incorrectness logic for graph programs. In Proceedings of the 14th International Conference on Graph Transformation (ICGT'21), Lecture Notes in Computer Science , Vol. 12741. Springer, 81-101. https://doi.org/10. 1007/978-3-030-78946-6\_5](https://doi.org/10.1007/978-3-030-78946-6_5)
- Christopher M. Poskitt and Detlef Plump. 2023. Monadic second-order incorrectness logic for GP 2. J. Log. Algebr. Methods Program. 130 (2023), 100825. https://doi.org/10.1016/j.jlamp.2022.100825
- Azalea Raad, Josh Berdine, Hoang-Hai Dang, Derek Dreyer, Peter W. O'Hearn, and Jules Villard. 2020. Local reasoning about the presence of bugs: Incorrectness separation logic. In Proceedings of the International Conference on Computer-Aided Verification (CAV'20), Part II, LNCS , Vol. 12225. Springer, 225-252. https://doi.org/10.1007/978-3-030-53291-8\_14
- [Azalea Raad, Josh Berdine, Derek Dreyer, and Peter W. O'Hearn. 2022. Concurrent incorrectness separation logic. In Proceedings of the ACM Annual Symposium on Principles of Programming Languages, Vol. 6 (2022), 1-29. https://doi.org/10. 1145/3498695](https://doi.org/10.1145/3498695)
- Francesco Ranzato. 2020. Decidability and synthesis of abstract inductive invariants. In Proceedings of the 31st International Conference on Concurrency Theory (CONCUR'20), LIPIcs , Vol. 171. Schloss Dagstuhl-Leibniz-Zentrum für Informatik, 30:1-30:21. https://doi.org/10.4230/LIPIcs.CONCUR.2020.30
- Thomas W. Reps, Shmuel Sagiv, and Greta Yorsh. 2004. Symbolic implementation of the best transformer. In Proceedings of the 24th International Conference on Verification, Model Checking, and Abstract Interpretation (VMCAI'04), LNCS , Vol. 2937. Springer, 252-266. https://doi.org/10.1007/978-3-540-24622-0\_21
- Henry G. Rice. 1953. Classes of recursively enumerable sets and their decision problems. Trans. Am. Math. Soc. 74 (1953), 358-366.
- Xavier Rival and Kwang Yi. 2020. Introduction to Static Analysis-An Abstract Interpretation Perspective . MIT Press.
- Caitlin Sadowski, Edward Aftandilian, Alex Eagle, Liam Miller-Cushon, and Ciera Jaspan. 2018. Lessons from building static analysis tools at Google. Commun. ACM 61, 4 (March 2018), 58-66. https://doi.org/10.1145/3188720
- Alan M. Turing. 1989. Checking a large routine. In The Early British Computer Conferences , Martin Campbell-Kelly (Ed.). MIT Press, Cambridge, MA, 70-72.
- Glynn Winskel. 1993. The Formal Semantics of Programming Languages: An Introduction . MIT Press.
- Peng Yan, Hanru Jiang, and Nengkun Yu. 2022. On incorrectness logic for Quantum programs. In Proceedings of the ACM SIGPLAN International Conference on Object-Oriented Programming Systems, Languages, and Applications (OOPSLA'22) , 1-28. https://doi.org/10.1145/3527316
- Greta Yorsh, Thomas W. Reps, and Shmuel Sagiv. 2004. Symbolically computing most-precise abstract operations for shape analysis. In Proceedings of the International Conference on Tools and Algorithms for the Construction and Analysis of Systems (TACAS'04), LNCS , Vol. 2988. Springer, 530-545. https://doi.org/10.1007/978-3-540-24730-2\_39
- [Cheng Zhang, Arthur Azevedo de Amorim, and Marco Gaboardi. 2022. On incorrectness logic and Kleene algebra with top and tests. In Proceedings of the ACM Annual Symposium on Principles of Programming Languages (POPL'22) . https: //doi.org/10.1145/3498690](https://doi.org/10.1145/3498690)
- Noam Zilberstein, Derek Dreyer, and Alexandra Silva. 2023. Outcome logic: A unifying foundation for correctness and incorrectness reasoning. Proceedings of the ACM SIGPLAN International Conference on Object-Oriented Programming Systems, Languages, and Applications (OOPSLA'23) , To appear.

Received 26 January 2022; revised 26 October 2022; accepted 4 January 2023