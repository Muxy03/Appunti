## A Basic Introduction to Static Program Analysis

## Francesco Ranzato

University of Padova, Italy, francesco.ranzato@unipd.it

## Abstract

These notes are intended to provide a (very) basic introduction to static program analysis by abstract interpretation. Some familiarity with basic order theory and denotational program semantics is required. This document is used as teaching material within the 'Software Verification' course of the MSc in Computer Science, at the University of Padova, Italy.

| 1 Introduction to Static Program Analysis   | 1 Introduction to Static Program Analysis         | 1 Introduction to Static Program Analysis           | 1 Introduction to Static Program Analysis                                         | 2     |
|---------------------------------------------|---------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------------------------------------|-------|
|                                             | 1.1                                               | What is Static Program Analysis?                    | . . . . . . . . . . . . . . . .                                                   | 2     |
|                                             | 1.2                                               | An Introductory Example                             | . . . . . . . . . . . . . . . . . . . . .                                         | 2     |
|                                             | 1.3                                               | Example: the Termination                            | . . . . . . . . .                                                                 | 5     |
|                                             | 1.4                                               | Optimizing Compilers                                | Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | 8     |
|                                             | 1.5                                               | Designing Static Analyses                           | . . . . . . . . . . . . . . . . . . . . .                                         | 9     |
| 2                                           | Introduction to Abstract Interpretation           | Introduction to Abstract Interpretation             | Introduction to Abstract Interpretation                                           | 10    |
|                                             | 2.1 . . . .                                       | Tools . . . . .                                     | . . . . . . . .                                                                   | 10    |
|                                             | 2.2                                               | Basic Ideas . . . . .                               | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | 12    |
|                                             | 2.3                                               | Basic Definition                                    | . . . . . . . . . . . . . . . . . . . . .                                         | 13    |
|                                             | 2.4                                               | Correctness Verification                            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | 15    |
| 3                                           | Abstract Interpretation of Arithmetic Expressions | Abstract Interpretation of Arithmetic Expressions   | Abstract Interpretation of Arithmetic Expressions                                 | 17    |
|                                             | 3.1                                               | Sign Analysis of Arithmetic Expressions             | . . . . . . . . . . . . .                                                         | 17    |
|                                             | 3.2                                               | Abstract                                            | Domains . . . . . . . . . . . . . . . . . . . . . . . . .                         | 21    |
|                                             | 3.3                                               | Galois                                              | Connections . . . . . . . . . . . . . . . . . . . . . . . . .                     | 23    |
|                                             | 3.4                                               | Abstract                                            | Operations . . . . . . . . . . . . . . . . . . . . . . . .                        | 25    |
|                                             | 3.5                                               | Soundness Theorem . .                               | . . . . . . . . . . . . . . . . . . . . . .                                       | 26    |
| 4                                           | Abstract Interpretation of Programs               | Abstract Interpretation of Programs                 | Abstract Interpretation of Programs                                               | 27    |
|                                             | 4.1                                               | Collecting Denotational Semantics                   | . . . . . . . . . . . . . . . .                                                   | 27    |
|                                             | 4.2 Abstract                                      | Abstract Semantics of Expressions Program Semantics | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | 29 30 |
|                                             | 4.3 4.4                                           | Sign Analysis of Programs .                         | . . . . . . . . . . . . . . . . . . . .                                           | 32    |
| 4.6                                         | 4.5 Analysis of Programs .                        | Interval Widening . . . . . . .                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 37 39 |
| Bibliography                                | Bibliography                                      | Bibliography                                        | Bibliography                                                                      | 42    |

## 1 Introduction to Static Program Analysis

## 1.1 What is Static Program Analysis?

According to Wikipedia, Static Program Analysis is the analysis of computer software performed without running any programs, as opposed to dynamic analysis, which is performed on programs during their execution. The term is usually applied to an analysis carried out by an automated tool, with human analysis called program understanding, program comprehension, or code review. In most cases the analysis is performed on some versions of the source code and in other cases by using some form of its object code.

A static analysis aims at proving with a '100% guarantee' that some programs are correct, i.e., do not have bugs. To be more precise, it makes use of some automatic techniques to deduce in the compilation phase, therefore statically, approximate information on the dynamic behaviour of the program in its execution phase.

What we want to analyze are some relevant dynamic properties of the programs, such as the values stored by variables, the properties related to program termination, or the ones related to the shape of the used memory, etc. However, there are other 'easy' properties that can be statically inferred, such as the number of used variables, the number of function calls, the number of different classes that compose our program, etc. These latter type of properties can be derived through a 'trivial' static analysis and some of them can also be automatically inferred by well-known automatic tools such as Lint .

Practical applications of static program analysis include: bug detection, program verification, program parallelization, type inference, etc. Despite all these diverse applications, the original motivation for static analysis was not program verification or bug detection, rather to compile efficient programs, an objective also known as code optimization. Later on, static program analysis was also applied to the aforementioned application areas.

## 1.2 An Introductory Example

Let us consider the following factorial program written as a while loop in imperative pseudo-code:

```
Input: integer n { n = k ∧ n ≥ 0 } m := 2 while n > 1 do m := m ∗ n n := n -1 { m = 2( k !) }
```

Observe that the accumulation variable m is initialized to 2. We expect that for the precondition n = k ∧ n ≥ 0, if the program terminates then the postcondition m = 2( k !) holds. Informally, this means that if an input store σ satisfies the precondition, i.e. before executing the program, and the program with input σ terminates, then the postcondition holds for the final store of the program. To reason about this program, we consider its control flow graph (CFG) depicted in Figure 1, whose nodes are called program points and decorate the pseudo-code as follows:

```
Input: (1) n (2) m := 2 while (3) n > 1 do (4) m := m ∗ n (5) n := n -1 Output: (6) m
```

Figure 1: Control Flow Graph of the factorial program.

<!-- image -->

The nodes of the CFG contain the atomic statements of the program, namely variable assignments and Boolean guards. The crucial program point is indeed (3), namely the loop invariant program point: this is the main program property that we want to infer. Note that for the point (3) we have two incoming edges, i.e., (2) → (3) and (5) → (3).

We can infer by static analysis that at the exit point (6) the value stored in m will be even for any input value n . To conclude this, the analysis must propagate 'parity information'. We therefore assign at each program variable one of these parity values:

- (i) Even: meaning that the stored value is even;
- (ii) Odd: meaning that the stored value is odd;

- (iii) DontKnow: meaning that the stored value can be either even or odd; this therefore represents lack of parity information.

Informally, we can state that we will always get an even number as output thanks to a simple inductive reasoning: at the beginning m stores 2, that, of course, is even; then, this value is updated by m := m ∗ n , so that once we have an even value as base case, this even value is multiplied with any other number, so that the result stored in m will remain even. The key point in this reasoning is indeed the assignment m := m ∗ n at the program point (4). The following table describes the expected parity values for the two variables n and m at each program point:

| Point   | Value n   | Value m   | Point   | Value n   | Value m   |
|---------|-----------|-----------|---------|-----------|-----------|
| (1)     | DontKnow  | DontKnow  | (4)     | DontKnow  | Even      |
| (2)     | DontKnow  | DontKnow  | (5)     | DontKnow  | Even      |
| (3)     | DontKnow  | Even      | (6)     | DontKnow  | Even      |

Actually, for a given positive n &gt; 0, this factorial program computes the double of the factorial of n , namely, 2( n !):

- -input n = 1 ⇒ output m = 2 -input n = 2 ⇒ output m = 4 -input n = 3 ⇒ output m = 12 -input n = 4 ⇒ output m = 48 -· · ·

Let us consider now the 'right' factorial problem with the initialization m := 1, that for a given positive n , computes the factorial n !.

```
Input: (1) n (2) m := 1 while (3) n > 1 do (4) m := m ∗ n (5) n := n -1 Output: (6) m
```

For this program, the previous informal analysis provides no useful information on the parity of m in (6). Here, we need to take into account the cases where n is initialized with either 0 or 1, and in these cases the final m will not be even.

| Point   | Value n   | Value m   | Point   | Value n   | Value m   |
|---------|-----------|-----------|---------|-----------|-----------|
| (1)     | DontKnow  | DontKnow  | (4)     | DontKnow  | DontKnow  |
| (2)     | DontKnow  | DontKnow  | (5)     | DontKnow  | DontKnow  |
| (3)     | DontKnow  | DontKnow  | (6)     | DontKnow  | DontKnow  |

Let us remark that this informal analysis is trivially correct, since it outputs DontKnow everywhere. Even if the input is restricted to even numbers n or to n &gt; 1, the analysis cannot be precise: in (3) both n and m are DontKnow, although in (6) m will be always even.

This loss of precision is a common attribute of static analysis techniques: some property of interest actually holds but the analysis algorithm for inferring this class of properties is unable to prove it. Most interesting dynamic properties of programs are undecidable, as a consequence of Rice's Theorem, so that we cannot automatically infer them with full precision or in a reasonable time. Nevertheless, we need to ensure the correctness, also known as soundness , of the output of static analyses of some program property pr :

- -If the program analysis of P outputs YES then the property pr surely holds for P .
- -If the program analysis of P does not output YES then it may happen that the property pr does not hold for P , therefore ¬ YES actually means DontKnow.

## 1.3 Example: the Termination Problem

The halting problem in computability theory is the problem of determining, from a description of an arbitrary computer program and a given input, whether the program will finish running, or continue to run forever. Turing proved in 1936 that this problem is undecidable.

Assume that the program has as input an integer variable. As a consequence of the undecidability of the halting problem, it turns out that the set K ≜ { P ∈ Prog | P (0) terminates } is not recursive.

Let us consider Figure 2, where the blue oval represents all the possible programs and the purple oval denotes the programs in K . A sound termination analysis can be done in two orthogonal ways: the set of programs which the analysis infers are terminating is determined either by the yellow area or by the green one. In the yellow case, if the analysis Y infers that a program P terminates on input 0 then P definitely terminates. In the green case, if the analysis G infers that a program P on input 0 then P may possibly terminate. Therefore, the analysis Y is sound for termination: Y ( P ) = YES ⇒ P terminates on input 0. On the other hand, the analysis G is sound for nontermination: Y ( P ) = NO ⇒ P does not terminate on input 0. In order to distinguish these two orthogonal types, the first analysis is called a definite analysis as it provides as output programs that definitely terminate, while the second analysis is called a possible analysis because it computes as output programs that possibly terminate.

Figure 2: Sound Termination Analyses.

<!-- image -->

On the other hand, an unsound termination analysis U is depicted in the following Figure 3.

Figure 3: Unsound Termination Analysis.

<!-- image -->

This analysis U infers that the programs in the blue oval are terminating. However, this information is unsound: if U ( P ) = YES then P could be terminating as well as non-terminating. This means that we do not have any guarantee on the output of this analysis, and so the information inferred from U ( P ) is useless.

To summarize, we have two types of sound termination analysis:

- (A) 'Definite' termination analysis:
- YES: the input program definitely terminates.
- NO: the input program could not terminate.
- (B) 'Possible' termination analysis:
- YES: the input program could terminate.
- NO: the input program definitely does not terminate.

This simple example shows that we need to leverage a semantics-based static analysis to provide a proof of correctness (or soundness) for the output information with respect to a ground-truth program semantics.

There exist several unsound static analysis tools such as Coverity . According to Wikipedia, Coverity is a static code analysis tool from Synopsys which enables engineers and security teams to quickly find and fix defects and security vulnerabilities in custom source code written in C, C++, Java, C#, JavaScript and more. Before its acquisition by Synopsys, Coverity was an organization founded in the Computer system Laboratory at Standford Univerity in Palo Alto, California. In June 2008, Coverity acquired Solidware Technologies and, in February 2014, announced an agreement to be acquired by Synopsis, an electronic design automation company, for $ 350 millions. The developers of Coverity discussed their product claiming that Coverity is deliberately unsound meaning that it does not verify the absence of errors but rather tried to find as many of them as possible. However, we stress that that soundness is the indispensable property of a static analysis based on a scientific approach to static analysis and we cannot give up on it.

Example 1.3.1. Consider an hypothetical static program analysis that for detecting divisions by zero syntactically finds whether the string /0 occurs in the program. Of course, this analysis is unsound. Let us see some instances of it.

| x = 100 /0            | ⇒ true alarm     |
|-----------------------|------------------|
| print('25 /0 9/2016') | ⇒ false alarm    |
| y = 100 /0 2          | ⇒ false alarm    |
| z = 0 print(5 /z )    | ⇒ false negative |

This analysis is unsound because false negatives may occur.

## 1.4 Optimizing Compilers

Static analysis was originally conceived for designing optimizing compilers. An optimizing compiler transforms the program code to improve its (space and/or time) efficiency without affecting its input/output behaviour. Dataflow Analysis is the most used static analysis technique in optimizing compilers. Let us describe some major program transformations that might improve the code efficiency.

- (1) Removal of common sub-expressions : if some sub-expression is computed more than once then we can avoid re-computations. This is illustrated by the following example.
- (2) Dead-code elimination : remove code which is unreachable. Let us see an example.
- (3) Constant folding : if the operands of some expression E turn out to be constant then the computation of E can be done at compile-time. This is illustrated by the following example.

```
1 a := b * c + g; 2 d := b * c * e; // The code is transformed as follows 3 tmp := b * c; 4 a := tmp + g; 5 d := tmp * e;
```

```
1 Function foo() 2 int a := 24; 3 int c; 4 c := a * 4; 5 return c; // Unreachable code 6 b := 24; 7 return 0;
```

Example 1.4.1. With no optimization option -O , the gcc compiler aims at reducing the cost of compilation. When optimization flags are turned on, the compiler attempts to improve the performance and/or code size at the expense of compilation time and, possibly, threatening the chance to debug the program.

By default, the optimization level of gcc is -O0 . Some options of optimization are as follows:

- -O1 : optimization for code size and execution time.
- -O2 : Optimize even more. gcc performs nearly all supported optimizations that do not involve a space-speed tradeoff. As compared to -O0 , this option

```
1 int x := 14; 2 int y := 7 - x / 2; 3 return y * (28 / x +2); // Propagation of x yields 4 int x := 14; 5 int y := 7 - 14 / 2; 6 return y * (28 / 14 +2); // Compile-time computation yields 7 int x := 14; 8 int y := 0;
```

- 9 return 0;

increases both compilation time and the performance of the generated code.

- -O3 : Optimize yet more. -O3 turns on all optimizations specified by -O2 plus others.
- -Os : Optimize for size. -Os enables all -O2 optimizations except those that often increase code size.
- -Ofast : Disregard strict standards compliance. -Ofast enables all -O3 optimizations. It also enables optimizations that are not valid for all standardcompliant programs.

The manual https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html provides more details on these optimizations.

One could ask whether optimal compilers exist. A fully size-optimizing compiler could be defined as a compiler that transforms an input program P into the program Opt( P ) which is 'the smallest' program having the same input/output behaviour as P . Given a program Q that does not terminate on all inputs, it is simple to find Opt( Q ): this is the program L1:goto L1; . Now, assume that a fully optimizing compiler exists. We could use it to solve the halting problem: to determine if there exists an input in such that a program P terminates on input in , it is enough to check whether Opt( P ) coincides with L1:goto L1; . Since the halting problem is undecidable, it turns out that a fully optimizing compiler cannot exist.

## 1.5 Designing Static Analyses

To design a sound static analysis SA we need to:

- (1) have a reference program semantics Sem ;
- (2) specify what and how the static analysis SA computes;
- (3) prove the correctness of SA with respect to Sem ;

(4) efficiently implement a static analyzer for SA .

Static analysis techniques include:

- Abstract interpretation;
- Dataflow Analysis, aforementioned for optimizing compilers;
- Model Checking;
- Logical Deductive Systems (e.g., separation logic and SMT/SAT solvers);
- Type Systems.

In these notes, we will consider mainly abstract interpretation.

## 2 Introduction to Abstract Interpretation

According to Wikipedia, abstract interpretation is a theory of sound approximation of the semantics of computer programs, based on monotonic functions over ordered sets, especially lattices. It can be viewed as a partial execution of a computer program which gains information about its semantics without performing all the calculations. Its main concrete application is formal static analysis. Such analyses have two main usages: (1) inside compilers to analyse programs to decide whether certain optimizations or transformations are applicable; (2) for debugging or even as certification of programs against classes of bugs.

Abstract interpretation was put forward by the French computer scientist working couple Patrick Cousot and Radhia Cousot in the late 1970s. This technique has been very influential in the fundamental and applied research on programming languages. The original paper introducing abstract interpretation has been published in the ACM Symposium on Principles of Programming Languages (POPL) conference [Cousot and Cousot, 1977], which is the top conference in programming languages, and it is the most cited POPL paper ever (POPL was established in 1973).

## 2.1 Tools

A lot of tools based on Abstract Interpretation have been designed, some of them are mentioned below.

Polyspace, from MathWorks, is a C/C++ analyzer. A remarkable feature of this analysis tool is that is strictly based on abstract interpretation. Polyspace statically detects run-time errors, concurrency issues, security vulnerabilities, and other defects in C and C++ embedded software. Polyspace analyzes software control flow, data flow, and interprocedural behaviour.

Astr´ ee is a static program analyzer aiming at proving the absence of runtime errors in programs written in C. It analyzes structured C programs, with complex memory usages, but without dynamic memory allocation and recursion. This encompasses many embedded programs as found in earth transportation, nuclear energy, medical instrumentation, aeronautic, and aerospace applications, in particular synchronous control/command such as electric flight control or space vessels maneuverers. Astr´ ee is always sound: if no error is signaled, then the absence of errors has been proved.

Interproc is not a realistic analysis tool but it is good for learning abstract interpretation-based program analysis because it is available through a simple web interface. It is an interprocedural analyzer for a small imperative language with (recursive) procedure calls. It infers invariants on the numerical variables of analyzed program. It also demonstrates the features of the APRON library and the use of the Fixpoint libraries. It is implemented in OCaml. You can easily play with Interproc online.

Infer is a popular analysis tool developed and maintained by Meta (former Facebook). It is a static program analyzer for Java, C, and Objective-C, written in OCaml. It is running continuously to verify selected properties of every code modification for the main Facebook apps but it may be also used for analyzing C code, and Java code that is not Android. It is open source and its source code is available on a GitHub repository.

Ikos is an abstract interpretation tool designed by NASA researchers that started as a C++ library designed to facilitate the development of sound static analyzers based on abstract interpretation. Ikos also provides a C and C++ static analyzer based on LLVM and it implements scalable analyses for detecting and proving the absence of runtime errors in C and C++ programs. It is open source and the code is available on Github.

Sparta is a library of software components specially designed for building high-performance static analyzers based on abstract interpretation. The purpose of SPARTA is to drastically simplify the engineering of abstract interpretation by providing a set of software components that have a simple API, are highly performant and can be easily assembled to build a production-quality static analyzer. This tool is open source and can be found on Github.

In recent years, abstract interpretation has been applied to the analysis of some machine learning algorithms, such as neural networks, support vector machines, decision trees, with the goal of formally verifying their robustness properties. A major project was carried on at ETH Zurich, where some tools to be applied in Adversarial Machine Learning were developed. More details can be found on the SafeAI webpage and the corresponding Github repository.

One could ask why static analysis tools are not so widespread in software engineering. A possible answer is that computer engineering is the only technology field where developers are not responsible for their errors, even the trivial ones. However, we could foresee that static analysis will become more and more widespread, to the point that software manufacturers will be forced to provide legal guarantees to the customers.

## 2.2 Basic Ideas

The general idea is that we are interested in providing an approximation of a concrete program property. Moreover, these approximated properties can be related through a partial order that intuitively states when a given approximated property is more precise than a second one. As an example, consider the following Figure 4 where the blue crosses denote the stores ( x, y ) ∈ R 2 computed by a program with two floating point variables x and y . Hence, this concrete program property could be a (finite or infinite) set such as S = { (0 , 3) , (5 . 5 , 0) , (12 , 7 . 1) , · · · } , and this set S could not be finitely computable.

Figure 4: Approximations of a set of points in R 2 .

<!-- image -->

Several approximations of S can be taken into account, some of them are depicted in Figure 4:

- Intervals: this approximation is depicted in green; for instance, an interval approximation could be x ∈ [0 , 12] ∧ y ∈ [0 , 8]. This is given by an interval [ l, u ] for each program variable that defines its range of variation between the lower bound l and the upper bound u .
- Octagons: this approximation is depicted in yellow; for instance, an octagonal approximation could be x + y ≤ 3 ∧ y ≤ 0 ∧ x -y ≤ -2. This is given by a set of linear inequalities between two program variables of type ± x ± y ≤ k or by an interval of variation for a variable.
- Convex Polyhedra: this approximation is depicted in red; for instance, a polyhedral approximation could be 6 x -2 y ≤ 3 ∧-x -4 y ≤ -1. This is a system of linear inequalities between program variables.

It should be remarked that the reason why we may want to choose an approximation which is less precise than another one is that we need a tradeoff between the cost and precision of an approximation domain. For instance, the convex polyhedra approximation is the most precise but its computation needs takes exponential time w.r.t. the number of program variables, octagons are a cubic time approximation, while intervals can be computed in linear time. There are many other methods of abstracting, not only these three, as shown in Figure 5, taken from [Min´ e, 2004], depicts further numerical approximations used in program analysis.

Figure 5: Numerical Abstract Domains.

<!-- image -->

## 2.3 Basic Definition

Abstract interpretation can be viewed as a unifying formal technique for systematically design abstractions and approximations. Moreover, in the original POPL77 paper, Cousot and Cousot [1977] stated:

' Most program analysis techniques may be understood as abstract interpretations of programs. There is a fundamental unity between all apparently unrelated program analysis techniques (flow analysis in optimizing compilers, type verification, program testing,...): a new interpretation is given to the program text which allows to built an often implicit system of equations. The problem is either to verify that a solution provided by the user is correct, or to discover or approximate such solution. The starting point is concrete semantics that provides the meaning of program commands into a given computational domain. We need also an abstract domain, which models some properties of interest of concrete computations and leaves out the remaining information. We then have an abstract semantics that allows us to 'abstractly execute' a program on the abstract domain in order to compute the program properties modeled by the abstract domain. The computation of the abstract semantics typically involves fixpoint computations and, when necessary, one could perform further correct approximations of the abstract semantics '.

```
1 ( S 0 ) Input: y ∈ [0 , 1000] 2 ( S 1 ) 3 i := 2 4 ( S 2 ) 5 while ( S 3 ) i < y do 6 ( S 4 ) 7 i := i +2 8 ( S 5 ) 9 ( S 6 )
```

Example 2.3.1. Let us consider the following program P :

where ( S i ) 6 i =0 denote the program points of P . Let D ≜ ℘ ( { i, y } → Z ). A solution { X i } 6 i =0 ∈ D 6 of the following set of equations induced by P represents an invariant for the corresponding program points of P :

<!-- formula-not-decoded -->

For any program point S i , the most precise invariant is given by the set of states that P can compute in S i , where, for the two integer variables of P , a state can be viewed as a pair ( i, y ) ∈ Z 2 of integers. Hence, for point S i , the function F i ( X 0 , ..., X 6 ) collects all possible states in S i . At the entry point S 0 we have no information, so that X 0 = Z 2 . For S 1 , we know that y ranges in [0 , 1000] and i depends on X 0 , so that X 1 depends on X 0 . The most interesting program point is S 3 which is point of the loop invariant: X 3 is given by the union of what we get from S 2 and the contribution of each loop iteration coming from point S 5 . The above system consists of recursive equations since the information flows from each node to some other nodes. This system of equations will define our pointwise concrete collecting program semantics where each fixpoint solution provides a program invariant while the least fixpoint defines the most precise invariant.

This set of concrete equations ( ∗ ) is abstracted into a corresponding set of equations X ♯ i = F i ( X ♯ 0 , ..., X ♯ 6 ) between abstract states X ♯ i ranging in some abstract domain A where transfer functions F i are approximated by corresponding abstract transfer functions F ♯ i defined over A that simulate in a sound way the behaviour of F i .

<!-- formula-not-decoded -->

We will study how to define one such system of abstract equations and how to compute effective solutions.

## 2.4 Correctness Verification

Let us consider the following figure where the crosses represent the states computed by some program P , also called reachable states , and the red area represents the incorrect states, also called bad states .

<!-- image -->

We want to verify that P is indeed correct, namely that any execution of P will never reach a bad state. This correctness verification can be performed by leveraging an over-approximation of the reachable states computed by a static analysis of P

<!-- image -->

- (i) The blue area represents a (indeed the least) convex polyhedra that overapproximates the reachable states. Since the blue area does not intersect the red area, we can conclude that the program P is correct.
- (ii) The green area represents the least interval abstraction of the reachable states. In this case we cannot conclude that P is correct because the intersection of the green and red areas is not empty. Therefore, the analysis of P raises an alarm of incorrectness telling us to check the states in that nonempty intersection. However, these actually are false alarms because the program P is correct. This is a major issue of correctness verification based on static analyses, because if an alarm is raised then human intervention is needed to check if this is a true or false alarm.

Thus, the success or failure of verifying the correctness of P depends on the precision of the approximation of reachable states. Consider now the scenario described by the following diagram where the program P is incorrect since it can reach a bad state.

<!-- image -->

Assume that the analysis of P computes the grey area: this is an unsound analysis because the grey area is not an over-approximation of the reachable states. A correctness verification exploiting this unsound analysis will conclude that the program P is correct, because the intersection between the grey and red areas is empty. On the other hand, if the scenario is instead given by the diagram below, then the correctness verification will infer that the program P is correct, as it is indeed the case. However, this is just a 'lucky' output of this verification check. In both cases, this example shows that we cannot trust the output of an unsound static analyses.

<!-- image -->

## 3 Abstract Interpretation of Arithmetic Expressions

## 3.1 Sign Analysis of Arithmetic Expressions

Let us begin with basic integer expressions that only allow to multiply integer numbers.

<!-- formula-not-decoded -->

The concrete semantics of these expressions is given by a function S : Exp → Z defined as follows:

<!-- formula-not-decoded -->

Then, we consider an abstract semantics σ : Exp → {-, 0 , + } that computes the sign of expressions.

<!-- formula-not-decoded -->

where the abstract multiplication × a : {-, 0 , + } 2 →{-, 0 , + } is defined by the following table:

<!-- image -->

This abstract semantics σ is sound, namely, it correctly computes the sign of expressions. This proof relies on an easy structural induction on the expression e and exploits some basic properties of integer multiplications, e.g., plus times minus is minus, minus times minus is plus, etc. Thus, correctness means that for any e ∈ Exp :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Actually, in this case, it turns out that an equivalence holds, so that ⇔ can replace ⇒ .

Let us define a function γ : {-, 0 , + } → ℘ ( Z ) mapping each abstract symbol in {-, 0 , + } to the set of concrete values that it represents:

<!-- formula-not-decoded -->

γ is called concretization function and each abstract symbol a ∈ {-, 0 , + } represents a concrete property of integers as given by γ ( a ) ⊆ Z . The scenario can be summarized by the following diagram where {·} : Z → ℘ ( Z ) denotes the singleton function mapping each z ∈ Z to { z } :

}

Figure 6: Concretization function.

<!-- image -->

With reference to the diagram in Figure 6, the abstract semantics σ turns out to be correct, namely σ provides a sound over-approximation of the concrete semantics S . This means that the following inclusion holds:

<!-- formula-not-decoded -->

Thus, for any expression e , the concrete meaning of the abstract semantics σ ( e ) is a set of integers that must include the concrete semantics S ( e ).

## 3.1.1 Adding Opposites

Let us add the unary operator that changes the sign of an expression to its opposite:

<!-- formula-not-decoded -->

so that concrete and abstract semantics are extended as follows:

<!-- formula-not-decoded -->

where -a : {-, 0 , + } → {-, 0 , + } is defined by:

<!-- formula-not-decoded -->

It turns out that this extension preserved the soundness of the abstract semantics σ .

## 3.1.2 Adding Additions

The addition operation

<!-- formula-not-decoded -->

needs some care because the abstract domain is not closed with respect to this operation. We define

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and then it is not clear how to fill the question marks ? in this table that sketches a definition of the abstract addition:

| + a   | -   | 0   | +   |
|-------|-----|-----|-----|
| -     | -   | -   | ?   |
| 0     | -   | 0   | +   |
| +     | ?   | +   | +   |

The issue here is which abstract value in {-, 0 , + } should be used for the sum of two integer numbers having opposite sign. Of course, the sum of two integers can be positive (e.g., -2 + 4), negative (e.g., -4 + 2), or zero (e.g., -2 + 2). Thus, in order to define a sound over-approximating abstract addition we need a novel abstract value ⊤ that represents any integer number, that is, such that γ ( ⊤ ) ≜ Z . Hence, ⊤ means that we have no sign information. The table defining + a can be therefore extended as follows:

<!-- image -->

Since the abstract domain includes a new element ⊤ , we need to extend all the abstract operations to this new element as follows:

| × a   | -   |   0 | +   | ⊤   |
|-------|-----|-----|-----|-----|
| -     | +   |   0 | -   | ⊤   |
| 0     | 0   |   0 | 0   | 0   |
| +     | -   |   0 | +   | ⊤   |
| ⊤     | ⊤   |   0 | ⊤   | ⊤   |

<!-- formula-not-decoded -->

It is worth remarking that 0 × a ⊤ = 0 = ⊤× a 0: this definition is correct and more precise than defining 0 × a ⊤ ≜ ⊤ .

Example 3.1.1. A loss of information in the abstract semantics may happen, as in the following case:

<!-- formula-not-decoded -->

On the other hand, the abstract computation is as precise as possible, i.e., the abstract semantics σ turns out to be complete :

<!-- formula-not-decoded -->

## 3.1.3 Adding Divisions

Integer division does not raise issues except for the case of division by zero. As no division by zero yields a number, the result of dividing a set of integer numbers by zero is the empty set, which therefore represents a run-time error. Thus, we need to add to our abstract domain a further new element ⊥ which represents the empty set, i.e., γ ( ⊥ ) = ∅ . Hence, ⊥ means termination with an error (and, later, will also represent nontermination). The abstract operations are therefore defined and extended as follows.

| / a   | -   | 0   | +   | ⊤   | ⊥   |
|-------|-----|-----|-----|-----|-----|
| -     | ⊤   | 0   | ⊤   | ⊤   | ⊥   |
| 0     | ⊥   | ⊥   | ⊥   | ⊥   | ⊥   |
| +     | ⊤   | 0   | ⊤   | ⊤   | ⊥   |
| ⊤     | ⊤   | 0   | ⊤   | ⊤   | ⊥   |
| ⊥     | ⊥   | ⊥   | ⊥   | ⊥   | ⊥   |

<!-- formula-not-decoded -->

Example 3.1.2. To take into account errors generated by division by zero, we consider the concrete semantics S c : Exp →{{ z } | z ∈ Z } ∪ { ∅ } defined as follows:

<!-- formula-not-decoded -->

Hence, we have the following examples:

<!-- formula-not-decoded -->

## 3.2 Abstract Domains

The set of symbolic values Sign ≜ {⊥ , -, 0 , + , ⊤} that we incrementally defined in Section 3.1 is called abstract domain . An abstract domain is endowed with a partial order relation ≤ modelling the notion of relative precision between its elements, called abstract values, where a ≤ a ′ intuitively means that a is more precise than a ′ , that is, the concrete property represented by a is stronger than that represented by a ′ . The abstract values -, 0 , + are not comparable with each other; ⊥ represents the empty set, i.e. the strongest integer property, and therefore is the bottom of the abstract domain; ⊤ represents the weakest integer property, i.e. the whole set Z , so that it is the top of the abstract domain. The Hasse diagram of ⟨ Sign , ≤⟩ is therefore as follows:

<!-- image -->

The partial order must be coherent with the concretization map, namely the following equivalence must hold:

<!-- formula-not-decoded -->

Let us observe that Sign is a (finite) lattice since all lub's and glb's exist. We define a function α : ℘ ( Z ) → Sign, called abstraction map , which is the counterpart of γ and, intuitively, maps a set S of integers into the most precise abstract value in Sign, w.r.t. the partial order ≤ , that represents S . For all S ∈ ℘ ( Z ),

̸

<!-- formula-not-decoded -->

̸

The relationship between the concretization map γ and the abstraction map α will be formalized as a Galois Connection , that will guarantee that the most precise abstract value representing a given concrete property always exists.

Example 3.2.1. Let us the following Hasse diagram defining an abstract domain denoted by Sign + :

<!-- image -->

Notice that ⟨ Sign + , ≤⟩ is a lattice. The concretization map γ : Sign + → ℘ ( Z ) is defined as follows:

<!-- formula-not-decoded -->

On the other hand, the abstraction map α : ℘ ( Z ) → Sign + is defined by leveraging γ as follows:

<!-- formula-not-decoded -->

For instance, α and γ act as follows:

```
α ( { 0 , 1 , 3 } ) = 0+ γ (0+) ⊇ { 0 , 1 , 3 } , { 2 , 3 , 5 } , { z ∈ Z | z > 2 } γ ( α ( { 0 , 1 , 3 } )) ⊇ { 0 , 1 , 3 } α ( γ (0+)) = 0+
```

## 3.3 Galois Connections

A Galois connection (GC) is a correspondence between two posets finding several applications both in mathematics and computer science. GCs generalize the fundamental theorem of Galois theory about the correspondence between subgroups and subfields, discovered by ´ Evariste Galois.

Definition 3.3.1. A tuple ( α, C, A, γ ) is a Galois connection when:

- (i) ⟨ C, ≤ C ⟩ and ⟨ A, ≤ A ⟩
- (ii) α : C → A and γ : A → C

<!-- formula-not-decoded -->

```
are posets; are monotone functions; C ));
```

<!-- formula-not-decoded -->

In abstract interpretation terminology, C is the concrete domain, A is the abstract domain, α is the abstraction map, γ is the concretization map. The intuition from an abstract interpretation perspective is as follows: Point (ii) means that α and γ preserve their precision ordering relations, respectively, ≤ C and ≤ A ; Point (iii) means that α ( c ) is a correct abstract approximation in A for the concrete value c ; Point (iv) means that γ ( a ) is correctly approximated in A by a .

## 3.3.1 Adjunctions

It turns out that Galois connections are equivalent to adjunctions , which are defined as follows.

Definition 3.3.2. A tuple ( α, C, A, γ ) is an adjunction when:

- (a) ⟨ C, ≤ ⟩ and ⟨ A, ≤ ⟩
- (b) α : C → A and γ : A → C

```
C A are posets; ;
```

<!-- formula-not-decoded -->

It is worth remarking that this definition does not require that α and γ are monotonic functions. The key condition here is (c) stating that the two relations α ( c ) ≤ A a and c ≤ C γ ( a ) are equivalent. The intuition is that if we want to compare c ∈ C with some a ∈ A for inferring whether a is an approximation in A of c , then it is equivalent comparing them either in the concrete domain C through c ≤ C γ ( a ) or in the abstract domain A through α ( c ) ≤ A a .

Theorem 3.3.3. ( α, C, A, γ ) is a GC if and only if ( α, C, A, γ ) is an adjunction.

## 3.3.2 Galois Insertions

Definition 3.3.4. A Galois connection ( α, C, A, γ ) is called Galois insertion (GI) if one of the following equivalent conditions holds:

- (1) α is surjective.
- (2) γ is injective.

<!-- formula-not-decoded -->

From the abstract interpretation viewpoint, a GC is indeed a GI when the abstract domain contains no 'useless' abstract value. In fact, if α is not surjective then there is some abstract element u ∈ A which is not reachable by α , so that u is useless. Equivalently, if γ is not injective then we have at least two different abstract values that represent the same concrete value, so that one of these abstract values would be enough.

Example 3.3.5. Consider the following abstract domain Sign u for sign analysis:

<!-- image -->

whose concretization map γ : Sign u → ℘ ( Z ) is as follows:

<!-- formula-not-decoded -->

It turns out that Sign u is defined by a GC which is not a GI. The abstract values u and + represent the same concrete value, so one of them is useless and could be safely removed.

We can transform any GC ( α, C, A, γ ) into a GI by removing its 'useless' abstract values. More precisely, this is achieved by considering a 'reduced'

Figure 7: Concrete and abstract operations.

<!-- image -->

abstract domain A red ≜ α ( C ) and the corresponding restrictions on A red of the abstraction and concretization maps:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

It turns out that ( α red , C, A red , γ red ) is a GI which has the same 'expressive power' of the original GC, namely, α red ( c ) = α ( c ) holds.

Let us highlight that if the abstract domain is defined by a Galois connection, then we have two equivalent ways of stating that the abstract semantics is sound because

<!-- formula-not-decoded -->

holds.

## 3.4 Abstract Operations

The diagram in Figure 7 considers a concrete n -ary operation op that is considered as a function on sets of integers rather than integers. This is commonly defined by the so-called collecting lifting of a given operation o : Z n → Z which is defined as follows:

<!-- formula-not-decoded -->

Hence, the collective lifting of an integer operation o allows us to view that operation as a transformer of concrete integer properties. Then, we consider a domain A that abstracts ℘ ( Z ) through a GC, so that the Cartesian product A n provides a pointwise abstraction of ℘ ( Z ) n through an abstraction α and a concretization γ . Finally, we consider an abstract operation op a that should soundly approximate on A the concrete behaviour of op .

More in general, we consider a concrete n -ary operation op : C n → C , which is assumed to be monotonic, and a corresponding abstract n -ary operation op a : A n → A which is also required to be monotonic.

Definition 3.4.1. The abstract operation op a is a correct approximation of op when for all ⟨ a 1 , ..., a n ⟩ ∈ A n ,

<!-- formula-not-decoded -->

Lemma 3.4.2. op a is a correct approximation of op if and only if one of the following equivalent conditions holds:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Correctness guarantees that the output of applying an abstract operation is a sound approximation of the result of applying the corresponding concrete operation. For any concrete operation op , one can always define the so-called best correct approximation op A of op on the abstract domain A as follows: for all a i ∈ A ,

<!-- formula-not-decoded -->

Definition 3.4.3. The abstract operation op a is a complete approximation of op when for all ⟨ c 1 , ..., c n ⟩ ∈ C n ,

<!-- formula-not-decoded -->

Thus, by Lemma 3.4.2, completeness is a stronger requirement than correctness for abstract operations. The intuition is that if op a turns out to be complete then op a is able to mimic on A the behaviour of the concrete operation op with no loss of precision. For example, the abstract multiplication × a on Sign, as defined in Section 3.1.2, turns out to be a complete abstract operation, while the abstract addition is, of course, correct but incomplete, as shown by the following conuterexample:

<!-- formula-not-decoded -->

## 3.5 Soundness Theorem

Let us prove that the concrete semantics of arithmetic expressions is correctly approximated by the above defined abstract semantics.

Theorem 3.5.1 (Soundness) . For all e ∈ Exp ,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Proof. Let op s be a binary (the proof for a generic n -ary operation is analogous) syntactic operation, that is, using infix notation, e 1 op s e 2 ∈ Exp. Let op : Z × Z → Z be the corresponding binary integer operation. Let op c : ℘ ( Z ) × ℘ ( Z ) → ℘ ( Z ) be the collecting lifting of op , that is,

<!-- formula-not-decoded -->

or, equivalently, Observe that op c is monotonic. Let op a : A × A → A be a correct approximation of op c on the abstract domain A . We proceed by structural induction on e ∈ Exp.

Basis. We have that {S ( n ) } = { n Z } ⊆ γ ( α ( { n Z } )) = γ ( σ ( n )), by Galois connection.

Inductive step.

We have that

<!-- formula-not-decoded -->

By inductive hypothesis on e 1 and e 2 , we have that

<!-- formula-not-decoded -->

By monotonicity of op c , we have that

<!-- formula-not-decoded -->

By correctness of op a ,

<!-- formula-not-decoded -->

Therefore,

<!-- formula-not-decoded -->

We can therefore conclude that {S ( e 1 op s e 2 ) } ⊆ γ ( σ ( e 1 op s e 2 )).

## 4 Abstract Interpretation of Programs

## 4.1 Collecting Denotational Semantics

Let us recall the syntactic definition of our while programs

Aexp ∋ e ::= x | n | e op e

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

```
1 2 1 2 1 2
```

whose denotational semantic functions are:

A : Aexp → State → Z

$$B : Bexp → State → T$$

S ds : While → State ↪ →

```
State
```

We define the collecting versions of these semantic functions that are therefore viewed as transformers of state properties in ℘ ( State ).

For arithmetic expressions we have:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus, A J e K transforms a state property into an integer property.

For Boolean expressions:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence, B c J b K T selects those states in T which make the guard b true. B c J b K T can also be viewed as a filtering of its argument T .

The collecting semantics of programs D : While → ℘ ( State ) → ℘ ( State ) is compositionally defined as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

D J S K can be viewed as a state property transformer where the argument T is a precondition for the program S which is transformed into the strongest postcondition of S .

We need to finalize the above definition with the collecting semantics of while loops. This is defined as a least fixpoint of a continuous function on the complete lattice ⟨ ℘ ( State ) , ⊆⟩ . For all T ∈ ℘ ( State ), we define:

<!-- formula-not-decoded -->

It turns out that the least fixpoint lfp( λT ′ .T ∪ ( D J S K ◦B c J b K ) T ′ ) is the strongest loop invariant. Initially, before evaluating the Boolean guard b , the precondition T holds. Next, an iteration of the while loop for an input condition T ′ first selects those states in T ′ that make b true and then applies the body S . This transform λT ′ .T ∪ ( D J S K ◦ B c J b K ) T ′ must be therefore iterated until a fixpoint is reached, which is therefore the strongest loop invariant viewed as state property. Since λT ′ .T ∪ ( D J S K ◦ B c J b K ) T ′ turns out to be continuous, by Kleene-Knaster-Tarski theorem, this latter fixpoint will be the least fixpoint. Finally, the strongest postcondition of the while loop is obtained by filtering the strongest loop invariant with the exit condition ¬ b .

Let us remark that any X ∈ ℘ ( State ) which is a fixpoint, i.e., such that X = T ∪D J S K ( B c J b K X ), is a loop invariant, because T ⊆ X and D J S K ( B c J b K X ) ⊆ X both hold.

Example 4.1.1. Consider the program P ≜ while ¬ ( x = 0) do x := x -2 and the precondition T ≜ {{ x → 5 } , { x → 6 }} ∈ ℘ ( State ). Then,

̸

<!-- formula-not-decoded -->

Thus, it turns out that:

<!-- formula-not-decoded -->

so that

<!-- formula-not-decoded -->

If we execute P with input x = 5 then the exit condition x = 0 will never be reached, the strongest loop invariant is

<!-- formula-not-decoded -->

and P does not terminate. On the other hand, with input x = 6, the strongest loop invariant is { x ↦→ 6 } , { x ↦→ 4 } , { x ↦→ 2 } , { x ↦→ 0 } , and then the execution terminates with output x = 0.

̸

Theorem 4.1.2. For any S ∈ While , T ∈ ℘ ( State ) , D J S K T = {S ds J S K s ∈ State | s ∈ T, S ds J S K s = undef } .

Thus, it turns out that D J S K T = ∅ iff, for any s ∈ T , the evaluation of S from s does not terminate.

## 4.2 Abstract Semantics of Expressions

To design an abstract program semantics we need:

1. an abstraction A of the concrete domain of value properties ⟨ ℘ ( Z ) , ⊆⟩ ;
2. an abstraction S of the concrete domain of state properties ⟨ ℘ ( State ) , ⊆⟩ .

We therefore assume that that these abstract domains are defined by the GIs ( α A , ℘ ( Z ) , A, γ A )) and ( α S , ℘ ( State ) , S , γ S ).

## 4.2.1 Arithmetic Expressions

The abstract semantics of arithmetic expressions is defined by a function

<!-- formula-not-decoded -->

that abstractly evaluates an expression on a given abstract state by providing as output an abstract value. We require the soundness of this abstract semantics A ♯ : for all e ∈ Aexp and s ♯ ∈ S ,

<!-- formula-not-decoded -->

The intuition is that the abstract semantics of an expression provides an overapproximation of its concrete collecting semantics. By Galois connection, this soundness requirement can be equivalently stated as follows: for all e ∈ Aexp , for all T ∈ ℘ ( State ),

<!-- formula-not-decoded -->

Here, the approximation comparison between abstract and concrete semantics is done in the abstract domain of values.

## 4.2.2 Boolean Expressions

The abstract semantics of Boolean expressions is given by

<!-- formula-not-decoded -->

that must be sound: for all b ∈ Bexp and s ♯ ∈ S :

<!-- formula-not-decoded -->

Similarly to arithmetic expressions, this abstract semantics therefore yields an over-approximation on the concrete filtering semantics of Boolean expressions. Equivalently, by GC, for all b ∈ Bexp and T ∈ ℘ ( State ):

<!-- formula-not-decoded -->

## 4.2.3 Abstract State Update

We also need an abstract version of the concrete state update s [ x ↦→ z ]. This is therefore an abstract operation which, given an abstract state s ♯ ∈ S , a variable x ∈ Var , an abstract value a ∈ A , provides an updated abstract state s ♯ [ x ↦→ a ] ∈ S . This update of abstract states must be correct: for all s ♯ ∈ S , x ∈ Var , a ∈ A :

<!-- formula-not-decoded -->

The intuition is that if s ♯ abstracts a state s and a abstracts a value z then s [ x ↦→ z ] is approximated by s ♯ [ x ↦→ a ].

## 4.3 Abstract Program Semantics

The abstract semantics of programs

<!-- formula-not-decoded -->

is a transformer of abstract states. This is compositionally defined as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Definition (1) leverages the abstract semantics of expressions A ♯ J e K s ♯ which is then used for updating the abstract state s ♯ . The soundness of this definition follows from the assumption that the abstract semantics of arithmetic expressions and the update of abstract states are both sound.

The abstract semantics of no-op in (2) is, as expected, the identity on abstract states.

Definition (3) states the analysis propagates forward in the control flow graph of the program. the analysis proceeds by visiting that graph. This definition is correct because it turns out that the composition of abstract functions preserves their soundness.

Definition (4) handles conditional branching. This stipulates that we analyze the true and false branches independently, by composing the abstract semantics of their Boolean guards with the abstract semantics of their bodies. Then, these two abstract states for the true and false branches are joined together through the lub of the abstract domain of states, which is therefore the least common approximation, i.e. lub, of them. Hence, the abstract lub ∨ S can be viewed as a sound approximation of (actually, this turns out to be the best correct approximation of) its concrete counterpart, namely the union of property states, which is their logical disjunction.

The abstract semantics of the while loop in (5) relies on the least fixpoint of the function

<!-- formula-not-decoded -->

which is a transformer of abstract states. This abstract function F ♯ b,S accumulates the abstract information in the loop invariant program point, namely the initial abstract state s ♯ is joined through the lub with the abstract information derived from the analysis of (one iteration of) the body of the loop. A fixpoint of F ♯ b,S -which turns out to be continuous-can be viewed as an abstract invariant of the loop, i.e., it is an (over-)approximation of the strongest concrete loop invariant. Thus, the least fixpoint can be understood as the best approximation derivable in the abstract domain S of the strongest loop invariant. By assuming that ⟨ S , ≤ S ⟩ , since the abstract transformer turns out to be continuous, this least fixpoint can be characterized by Kleene-Knaster-Tarski theorem:

<!-- formula-not-decoded -->

If S is an ACC CPO then this lub of the Kleene iterates of F ♯ b,S can be reached in finitely many states, and, by assuming that all the abstract operations are computable, therefore provides an effective algorithm. Finally, the abstract post-condition of the while loop is obtained by the abstract filtering of the least fixpoint of F ♯ b,S through the abstract semantics of the exit condition ¬ b .

Theorem 4.3.1 ( Soundness ) . For all S ∈ While , s ♯ ∈ S :

<!-- formula-not-decoded -->

By Galois connection, the soundness statement can be equivalently given as follows: For all S ∈ While and T ∈ ℘ ( State ),

<!-- formula-not-decoded -->

## 4.3.1 Fixpoint Soundness and Completeness

The proof of Theorem 4.3.1 crucially relies on the following result.

Lemma 4.3.2 ( Fixpoint Soundness ) . Let ( α, C, A, γ ) be a GC between complete lattices, f : C → C be a monotonic function, and f ♯ : A → A be a correct approximation of f , i.e., f ( γ ( a )) ≤ C γ ( f ♯ ( a )) for all a ∈ A . Then,

<!-- formula-not-decoded -->

Thus, this result states that the soundness of abstract operations as defined in Section 3.4 can be lifted to fixpoints.

It is also worth remarking that also the completeness of abstract operations (cf. Definition 3.4.3) can be lifted to fixpoints, as stated by the following result.

Lemma 4.3.3 ( Fixpoint Completeness ) . Let ( α, C, A, γ ) be a GC between complete lattices, f : C → C be a monotonic function, and f ♯ : A → A be a complete approximation of f , i.e., α ◦ f = f ♯ ◦ α holds. Then,

<!-- formula-not-decoded -->

## 4.4 Sign Analysis of Programs

Let us recall that the abstract domain Sign is defined by the following Hasse diagram

<!-- image -->

and represents sign properties of integer program variables. This domain is defined by a GI ( α, ℘ ( Z ) , Sign , γ ), where, for instance, we have that:

<!-- formula-not-decoded -->

This abstraction of integer values induces a corresponding abstraction of program states defined by:

<!-- formula-not-decoded -->

that is, S consists of all the maps associating to variables a corresponding abstract sign in Sign. The set Var is considered to be defined by the set of variables syntactically occurring in the program under analysis, so that Var is always a finite set. It turns out that ⟨ S , ⊑ , ⊥ S , ⊤ S ⟩ is a finite lattice (as Var is a finite set) where:

<!-- formula-not-decoded -->

Thus, s ♯ 1 ⊑ s ♯ 2 holds when for any variable x , the sign information stored in s ♯ 1 is more precise (w.r.t. the partial order ≤ Sign ) of the sign information given by s ♯ 2 . Hence, ⊑ simply lifts in a variable-wise fashion the partial order of Sign.

We define α S : ℘ ( State ) → S and γ S : S → ℘ ( S ) as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus, given a state property T , we collect the values stored in some variable x for some state in T and this value property is abstracted in Sign. On the other hand, an abstract state s ♯ represents all the states s such that, for any variable x , the sign of the value stored in x is approximated by the abstract sign s ♯ ( x ). This definition gives rise to a Galois connection.

Lemma 4.4.1. ( α S , ℘ ( State ) , S , γ S ) is a GC.

However, we do not have a GI as γ is not injective, as shown by the following example.

## Example 4.4.2. We have that:

<!-- formula-not-decoded -->

Since there is no value z ∈ Z such that α ( { z } ) = ⊥ , it turns out that:

<!-- formula-not-decoded -->

namely, γ is not injective.

The above example hints that as soon as a sign analysis infers that some variable is flagged as ⊥ , the analysis can safely stop and outputs the bottom abstract state ⊥ S .

## 4.4.1 Abstract Semantics of Arithmetic Expressions

The abstract semantics A ♯ : Aexp → S → Sign providing the sign analysis of arithmetic expressions is compositionally defined as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where op Sign : Sign × Sign → Sign is a correct abstract operation for a binary operation op , with correctness is defined in Section 3.4. For the sake of simplicity, this definition considers binary operations, but, of course, this applies to generic n -ary arithmetic operations.

Example 4.4.3. We have the following abstract semantics:

<!-- formula-not-decoded -->

## 4.4.2 Abstract Semantics of Boolean Expressions

Let us define the abstract semantics B ♯ : Bexp → S → S of Boolean expressions in a compositional fashion as follows:

̸

<!-- formula-not-decoded -->

It must be remarked that definition (6) may not provide the best correct approximation of B c J e 1 = e 2 K . The first condition of (6) requires that the abstract evaluations of e 1 and e 2 are different signs in {-, 0 , + } , so that, since different signs have an empty intersection (e.g., γ ( -) ∩ γ (+) = ∅ = γ ( -) ∩ γ (0)), the abstract evaluation of e 1 = e 2 can be correctly defined as the bottom abstract state. not ⊥ or ⊤ and they are not the same) are mutually exclusive. Moreover, the second condition of (6) assumes that either e 1 or e 2 (including both of them) are abstractly evaluated to ⊥ , representing an error, so that the abstract evaluation of e 1 = e 2 can be safely defined as bottom. In the third case, the abstract evaluation is simply the identity: it turns out that the identity id is always correct as abstract semantics of any Boolean expression b , because here the requirement is soundness for the collecting filtering function

and the containment

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

always holds. However, this is a correct approximation which may well not be the best, as shown by the following example.

Example 4.4.4. We have that

<!-- formula-not-decoded -->

while, according to definition (6),

<!-- formula-not-decoded -->

because A ♯ J x +1 K { x ↦→ + } = + and A ♯ J x K { x ↦→ + } = +. Thus, in this case, definition (6) does not coincide with the best correct approximation

<!-- formula-not-decoded -->

Let us continue the compositional definition of B ♯ as follows:

̸

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In the first condition of definition (7), where A ♯ J e i K s ♯ ∈ {-, 0 , + } , the meaning of the relation ≻ on {-, 0 , + } is as expected: + ≻ 0, 0 ≻ -; that is, positive is 'greater' than zero, and zero is 'greater' than negative. Moreover, in (8), logical conjunction is abstractly evaluated as composition of the corresponding abstract semantics, while in (9), disjunction boils down to the least upper bound between abstract states.

Example 4.4.5. According to the above definitions, we have that:

̸

<!-- formula-not-decoded -->

Of course, this definition of B ♯ can be made much more precise. For instance, we should aim at a definition such that

<!-- formula-not-decoded -->

holds.

## 4.4.3 Abstract Update

The abstract update ( · )[( · ) ↦→ ( · )] : S × Var × Sign → S is defined as follows:

̸

<!-- formula-not-decoded -->

Thus, if y = x then the sign of the variable y is updated and the other variables are left unchanged. This is the best approximation we can make because the abstract states are updated variable by variable. It is worth remarking that this definition (10) is not specifically tailored for Sign but can be applied to any domain A abstracting ℘ ( Z ).

## 4.4.4 An Example of Sign Analysis

Let us consider the program

̸

<!-- formula-not-decoded -->

whose abstract semantics is:

<!-- formula-not-decoded -->

Consider s ♯ 1 = { x ↦→-} . We have that:

̸

<!-- formula-not-decoded -->

In turn, we obtain

<!-- formula-not-decoded -->

Observe that (11) is justified by the fact that A ♯ J x +1 K s ♯ 1 = ⊤ . Moreover, since { x ↦→⊤} is the top of S then in (12) it is trivially the least fixpoint. Thus, this analysis of P carries no interesting information: it simply tells us that if we execute P with a negative input value for x and P terminates then x will store the value 0; but this information is obvious because x = 0 is exit condition.

Consider now s ♯ 2 = { x ↦→ 0 } . In this case we have that:

̸

<!-- formula-not-decoded -->

̸

Hence, also in this case the analysis of P infers just trivial information.

Finally, let us consider s ♯ = { x ↦→ + }

̸

<!-- formula-not-decoded -->

Hence, here we obtain

<!-- formula-not-decoded -->

This output abstract state is obtained because a positive number can never be zero, so that the abstract semantics of the x = 0 can infer the bottom state ⊥ representing unreachability. Here, the analysis is able to derive some nontrivial information: if we execute P with a positive input value for x then P definitely does not terminate.

̸

̸

̸

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

.

.

.

⊤

·

.

.

.

.

.

.

<!-- image -->

.

.

.

.

Figure 8: The Interval Abstract Domain Int.

## 4.5 Interval Analysis of Programs

We consider the complete lattice Int of integer intervals depicted in Figure 8. We extend integer numbers to Z ∞ ≜ Z ∪ {-∞ , + ∞} where for all z ∈ Z ∞ , -∞≤ z ≤ + ∞ holds. Thus,

<!-- formula-not-decoded -->

where [ -∞ , + ∞ ] is also denoted by ⊤ . The intuition is that an interval [ l, u ] represents a range of variation for an integer program variable, where l is a lower bound and u is an upper bound for the values that can be stored in that variable. The ordering ⪯ of Int is defined as follows:

<!-- formula-not-decoded -->

It turns out that ⟨ Int , ⪯⟩ is a complete lattice whose glb ⋏ is given by intersection. Int is defined by a GI ( α, ℘ ( Z ) , Int , γ ) GI where:

̸

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

.

.

For example, we have that

<!-- formula-not-decoded -->

̸

A corresponding domain of abstract states is defined variable-wise as follows:

<!-- formula-not-decoded -->

where for all s ♯ , t ♯ ∈ S , s ♯ ⊑ t ♯ iff for all x ∈ Var , s ♯ ( x ) ⪯ t ♯ ( x ).

## 4.5.1 An Example of Interval Analysis

In these notes, we will not provide an explicit and precise definition of the main abstract operations on Int. In the following example, we will simply use what appears to be the natural best approximation in the domain of intervals of abstract operations.

We consider the program

<!-- formula-not-decoded -->

whose abstract semantics is therefore:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Let us consider as input abstract state s ♯ ≜ { x ↦→ [10 , 10] , y ↦→ [0 , 0] } . Let us compute the Kleene iteration sequence of the function

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence, the Kleene iteration sequence { F n ( ⊥ ) } n ∈ N does not finitely converge, because for all n ≥ 12 it turns out that

<!-- formula-not-decoded -->

so that the lub in S of this infinite increasing chain { F n ( ⊥ ) } n ∈ N turns out to be:

<!-- formula-not-decoded -->

which is the abstract loop invariant of P . Clearly, the problem is that while the interval for the variable x is lower bounded by the Boolean guard x ≥ 0, no upper bound can be inferred for the variable y , so that the abstract semantics infers as abstract invariant for y the interval [ -, + ∞ ].

As abstract post-condition we therefore get:

<!-- formula-not-decoded -->

Hence, in this case, it turns out that the analysis of P is not terminating. We therefore need a technique to extrapolate, in a fi nite number of steps, the interval [0 , + ∞ ] for the variable y .

## 4.6 Widening

The notion of widening is central in abstract interpretation.

Definition 4.6.1. A binary operator ∇ : L × L → L , commonly used in infix notation, on a complete lattice ( L, ≤ L ) is called a widening if:

<!-- formula-not-decoded -->

- (1) it is a finite upper bound, i.e., for all x, y ∈ L , x, y ≤ L x ∇ y
- (2) it enforces convergence, i.e., for any ascending chain ( x n ) n ∈ N in L , the induced ascending chain ( y n ) n ∈ N , inductively defined by:

<!-- formula-not-decoded -->

is not strictly increasing, i.e., ( y n ) n ∈ N finitely converges.

Let us stress that the y n +1 is defined by using the predecessor element y n which is widened with the corresponding element x n +1 of the original chain ( x n ) n ∈ N .

Let us consider the complete lattice of integer intervals Int whose binary lub ⋎ turns out to be as follows:

<!-- formula-not-decoded -->

Let K ∈ Int be a given interval and let us define a binary operator Ω K : Int × Int → Int as follows:

<!-- formula-not-decoded -->

Thus, if the lub [ l 1 , u 1 ] ⋎ [ l 2 , u 2 ] = [min( l 1 , l 2 ) , max( u 1 , u 2 )] is included in K then the operator Ω K acts as the lub of Int, otherwise it widens this lub to the top interval [ -∞ , + ∞ ].

Example 4.6.2. Let K = [0 , + ∞ ] ∈ Int. The following example shows that Ω [0 , + ∞ ] is not a widening. In fact, the transform of Definition 4.6.1 (2) leaves the infinite ascending chain ([0 , n ]) n ∈ N unchanged, because for all n ,

<!-- formula-not-decoded -->

Hence, this identity transform of the chain does not finitely converge, meaning that Ω [0 , + ∞ ] does not satisfy the requirement of Definition 4.6.1 (2) (requirement (1) is instead satisfied).

It turns out that if K is a finite interval then Ω K is a widening.

Example 4.6.3. Let us consider K = [ -2 , 4] ∈ Int. The operator Ω [ -2 , 4] turns out to be a widening. For instance, the diverging chain ([0 , n ]) n ∈ N is transformed by Definition 4.6.1 (2) into the increasing chain

<!-- formula-not-decoded -->

that finitely converges to [ -∞ , + ∞

].

## 4.6.1 Standard Interval Widening

The standard widening ∇ : Int × Int → Int on intervals is defined as follows:

```
⊥∇ [ l, u ] ≜ [ l, u ] [ l, u ] ∇⊥ ≜ [ l, u ] [ l 1 , u 1 ] ∇ [ l 2 , u 2 ] ≜ [if l 1 ≤ l 2 then l 1 else -∞ , if u 2 ≤ u 1 then u 1 else + ∞
```

<!-- formula-not-decoded -->

Thus, with this standard widening the unstable left (i.e., l 2 &lt; l 1 ) and right (i.e., u 1 &lt; u 2 ) bounds are widened, respectively, to -∞ and + ∞ .

For instance, we have that:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence, it turns out that this standard widening is neither monotonic in its first argument (by example (13)) nor commutative (by example (14)).

Let f be a continuous function f : L → L on a complete lattice ⟨ L, ≤⟩ and consider a widening ∇ on L . We inductively define the following widened Kleene iteration sequence ( x n ) n ∈ N induced by ∇ :

<!-- formula-not-decoded -->

Therefore, in the inductive step, if the application of f to the previous element of the chain x n is a prefix point (i.e., f ( x n ) is bounded by x n ) then we keep x n as next element and therefore the chain is converging, otherwise we consider the widening of x n with f ( x n . The following result can be proved.

Theorem 4.6.4. The ascending chain { x n } n ∈ N finitely converges to an element z ∈ L such that: (1) f ( z ) ≤ z and (2) lfp( f ) ≤ z hold.

Thus, the widened Kleene iteration sequence is guaranteed to finitely converge to an element which is prefix point and an over-approximation of the least fixpoint of f .

## 4.6.2 An Example of Interval Analysis with Widening

Let us consider the program:

```
P ≜ int x := 1; while x ≤ 100 do x := x +1
```

The interval analysis D ♯ J P K ⊤ boils down to compute the least fixpoint of the function F P : Int → Int defined as follows:

<!-- formula-not-decoded -->

where: [1 , 1] is the interval after the initialization int x := 1; I ⋏ [ -∞ , 100] is the input interval I fi ltered by the Boolean guard x ≤ 100; I 1 ⊕ I 2 is the binary addition of two intervals.

We compute the widened Kleene iteration sequence ( I n ) n ∈ N of F P leveraging the standard widening defined in Section 4.6.1. By Theorem 4.6.4 we know that this widened sequence finitely converges to an interval that overapproximated lfp( F P ).

<!-- formula-not-decoded -->

Hence, in four iterations, the widened Kleene iteration sequence converges to the interval [1 , + ∞ ], which is an approximation of the true least fixpoint lfp( F P ) = [1 , 101], that actually is the strongest loop invariant of the whileloop with precondition [1 , 1]. This allows us to conclude that

<!-- formula-not-decoded -->

namely, x &gt; 100 is a correct post-condition for P .

## Bibliography

- P. Cousot and R. Cousot. Abstract interpretation: A unified lattice model for static analysis of programs by construction or approximation of fixpoints. In Proc. ACM POPL'77 , pages 238-252. ACM, 1977. doi: 10.1145/512950. 512973. URL https://doi.org/10.1145/512950.512973 .
- A. Min´ e. Weakly Relational Numerical Abstract Domains . PhD thesis, ´ Ecole Normale Sup´ erieure, Paris, France, 2004.