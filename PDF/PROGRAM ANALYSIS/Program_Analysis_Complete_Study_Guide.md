# Program Analysis — Complete Study Guide

**Course:** Program Analysis 2025-26  
**Teachers:** Chiara Bodei, Roberto Bruni, Roberta Gori  
**University:** Università di Pisa  

<hr>


# Lecture 01 — Introduction

## Theory

### Software Verification

- **Correctness:** proving the absence of bugs (over-approximation)
- **Incorrectness:** proving the presence of bugs (under-approximation)

### Semantics

**Memory states:**
$$
\Sigma \triangleq \{\sigma : X \to \mathbb{Z}\}
$$

**Forward semantics (deterministic):** $\llbracket c\rrbracket : \Sigma \to \Sigma_\bot$ where $\Sigma_\bot = \Sigma \uplus \{\bot\}$

**Collecting semantics:** $\llbracket c\rrbracket : \wp(\Sigma) \to \wp(\Sigma)$

$$
\llbracket c\rrbracket P = \bigcup_{\sigma \in P} \llbracket c\rrbracket\sigma
$$

### Undecidability

**Rice's Theorem:** Let $\mathcal{P}(c)$ be a non-trivial semantic property of programs. There exists no algorithm such that, for every program $c$, it returns true iff $\mathcal{P}(c)$ holds.

> No analysis method that is **automatic**, **universal**, and **exact**!

### Approximation Spectrum

| Technique | Automatic | Sound | Complete |
|-----------|-----------|-------|----------|
| Testing | Yes | No | Yes |
| Machine-assisted proving | No | Yes | Quasi |
| Model checking | Yes | Yes* | Yes* |
| Conservative static analysis (over-approx) | Yes | Yes | No |
| Bug finding (under-approx) | Yes | No | No |

### Soundness and Completeness

- **Soundness:** $\text{analysis}(c) = \text{true} \Rightarrow \mathcal{P}(c)$
- **Completeness:** $\mathcal{P}(c) \Rightarrow \text{analysis}(c) = \text{true}$

### Over-approximation vs Under-approximation

- **Over-approximation:** Good for proving correctness (true negatives), bad for bug-finding (false positives)
- **Under-approximation:** Good for bug-finding (true positives), bad for proving correctness (false negatives)

<hr>


# Lecture 02 — Denotational Semantics

## Theory

### Concrete Domain

$$
\Sigma \triangleq \{\sigma : X \to \mathbb{Z}\} \qquad \wp(\Sigma) \triangleq \{P \mid P \subseteq \Sigma\}
$$

### State Notation

- $\sigma = [x \mapsto 2]$ — variable $x$ has value 2, all others 0
- $\sigma[n/x]$ — state update: $x$ holds $n$, any other $y$ holds $\sigma(y)$
- $(x = 1, y = 2)$ — property notation: set of all states where $x=1$ and $y=2$

### Regular Commands Syntax

$$
\begin{aligned}
c &::= e \mid c_1;c_2 \mid c_1 + c_2 \mid c^\star \\
e &::= \texttt{skip} \mid x := a \mid b? \mid \dots \\
a &::= n \mid x \mid a_1 + a_2 \mid \dots \\
b &::= a_1 \le a_2 \mid b_1 \land b_2 \mid \dots
\end{aligned}
$$

### Collecting Semantics

$$
\llbracket c\rrbracket : \wp(\Sigma) \to \wp(\Sigma)
$$

**Atomic commands:**

- $\llbracket \texttt{skip} \rrbracket P \triangleq P$
- $\llbracket x := a\rrbracket P \triangleq \{\sigma[n/x] \mid \sigma \in P, n = \llbracket a\rrbracket\sigma\}$
- $\llbracket b?\rrbracket P \triangleq \llbracket b\rrbracket P$ (states in P satisfying b)

**Compound commands:**

- $\llbracket c_1; c_2\rrbracket P \triangleq \llbracket c_2\rrbracket(\llbracket c_1\rrbracket P)$
- $\llbracket c_1 + c_2\rrbracket P \triangleq \llbracket c_1\rrbracket P \cup \llbracket c_2\rrbracket P$
- $\llbracket c^\star\rrbracket P \triangleq \bigcup_{k=0}^\infty \llbracket c\rrbracket^k P$

**Encoding conditionals and loops:**

- $\texttt{if } b \texttt{ then } c_1 \texttt{ else } c_2 \triangleq (b?;c_1) + (\neg b?;c_2)$
- $\texttt{while } b \texttt{ do } c \triangleq (b?;c)^\star; \neg b?$

### Partial Correctness

$$
\llbracket c\rrbracket P \subseteq Q
$$

Every reachable state from $P$ is in $Q$ (non-termination allowed).

### Dijkstra's Weakest Liberal Precondition (wlp)

$$
\text{wlp}(c, Q) = \{\sigma \mid \llbracket c\rrbracket\{\sigma\} \subseteq Q\}
$$

Property: $P \subseteq \text{wlp}(c, Q) \iff \llbracket c\rrbracket P \subseteq Q$

### Relational Semantics

$\llbracket c\rrbracket \subseteq \Sigma \times \Sigma$ where $\llbracket c\rrbracket = \{(\sigma, \delta) \mid \sigma \in \Sigma, \delta \in \llbracket c\rrbracket\sigma\}$

### Backward Semantics

$\overset{\leftarrow}{\llbracket c\rrbracket} = \{(\delta, \sigma) \mid (\sigma, \delta) \in \llbracket c\rrbracket\}$

Properties: $\delta \in \llbracket c\rrbracket\sigma \iff \sigma \in \overset{\leftarrow}{\llbracket c\rrbracket}\delta$

### Hoare's Weakest Possible Precondition (wpp)

$$
\text{wpp}(c, Q) = \{\sigma \mid \llbracket c\rrbracket\sigma \cap Q \neq \emptyset\}
$$

$$
\overset{\leftarrow}{\llbracket c\rrbracket} Q = \text{wpp}(c, Q)
$$

### wpp vs wlp

- $\text{wpp}(c, Q)$: largest set of input states that have a **successful** computation
- $\text{wlp}(c, Q)$: largest set of input states whose computations are **all** successful

<hr>


# Lecture 03 — Hoare Logic (HL)

## Inference Rules

### Skip Axiom
$$
\dfrac{}{\{P\}\ \texttt{skip}\ \{P\}}
$$

### Assignment Axiom (Hoare)
$$
\dfrac{}{\{Q[a/x]\}\ x := a\ \{Q\}}
$$

### Assignment Axiom (Floyd)
$$
\dfrac{}{\{P\}\ x := a\ \{\exists x'. P[x'/x] \land x = a[x'/x]\}}
$$

### Composition Rule
$$
\dfrac{\{P\}\ c_1\ \{R\} \quad \{R\}\ c_2\ \{Q\}}{\{P\}\ c_1;c_2\ \{Q\}}
$$

### Conditional Rule
$$
\dfrac{\{P \land b\}\ c_1\ \{Q\} \quad \{P \land \neg b\}\ c_2\ \{Q\}}{\{P\}\ \texttt{if } b \texttt{ then } c_1 \texttt{ else } c_2\ \{Q\}}
$$

### While Rule
$$
\dfrac{\{P \land b\}\ c\ \{P\}}{\{P\}\ \texttt{while } b \texttt{ do } c\ \{P \land \neg b\}}
$$

$P$ is the **loop invariant**.

### Consequence Rule
$$
\dfrac{P \Rightarrow P' \quad \{P'\}\ c\ \{Q'\} \quad Q' \Rightarrow Q}{\{P\}\ c\ \{Q\}}
$$

## Validity

A HL triple $\{P\}\ c\ \{Q\}$ is **valid** iff $\llbracket c\rrbracket P \subseteq Q$.

## Important Properties

- **Soundness:** Any derivable HL triple is valid (proof by induction on derivation tree)
- **Finding invariants is difficult** — requires creativity

<hr>


# Lecture 04 — Total Correctness

## Partial vs Total Correctness

- **Partial:** $\{P\}\ c\ \{Q\}$ — precondition met $\Rightarrow$ postcondition holds (if termination occurs)
- **Total:** $[P]\ c\ [Q]$ — precondition met $\Rightarrow$ **termination** + postcondition holds
- Total correctness = partial correctness + termination

## Total Correctness While Rule

$$
\dfrac{\{P \land b\}\ c\ \{P\} \quad \{P \land b \land t = z\}\ c\ \{t < z\} \quad P \Rightarrow t \ge 0}{\{P\}\ \texttt{while } b \texttt{ do } c\ \{P \land \neg b\}}
$$

Where:

- $t$ is the **variant** (termination function) — an arithmetic expression that decreases at each iteration and is bounded below
- $z$ is a fresh variable that stores the initial value of $t$

## Example: Euclidean Division

Total correctness proof with variant $t \triangleq r$:

- $P \Rightarrow t \ge 0$: $(r \ge 0 \land y > 0 \land x = r + qy) \Rightarrow r \ge 0$ ✓
- Body decreases variant: $\{r \ge y > 0 \land \dots \land r = z\}\ r:= r-y;\ q:= q+1\ \{r < z\}$ ✓

<hr>


# Lecture 05 — Incorrectness Logic (IL)

## O'Hearn's Triples

$$
[P]\ c\ [Q] \iff \llbracket c\rrbracket P \supseteq Q
$$

**Meaning:** Any output in the postcondition is reachable from some input in the precondition.

### First-order Formulas

- HL: $\llbracket c\rrbracket P \subseteq Q \equiv \forall\sigma\in P.\ \forall\delta\in\llbracket c\rrbracket\sigma.\ \delta\in Q$
- IL: $\llbracket c\rrbracket P \supseteq Q \equiv \forall\delta\in Q.\ \exists\sigma\in P.\ \delta\in\llbracket c\rrbracket\sigma$

## IL Inference Rules

### Skip
$$
\dfrac{}{[P]\ \texttt{skip}\ [P]}
$$

### Assignment (Floyd) — Same as HL!
$$
\dfrac{}{[P]\ x := a\ [\exists x'. P[x'/x] \land x = a[x'/x]]}
$$

**Note:** Hoare's axiom $[Q[a/x]]\ x := a\ [Q]$ is **unsound** for IL!

### Assume
$$
\dfrac{}{[P]\ b?\ [P \land b]}
$$

### Error
$$
\dfrac{}{[P]\ \texttt{error}()\ [\texttt{false}]}
$$

### Nondet
$$
\dfrac{}{[P]\ x := \texttt{nondet}()\ [\exists x. P]}
$$

### Sequence — Same as HL
$$
\dfrac{[P]\ c_1\ [R] \quad [R]\ c_2\ [Q]}{[P]\ c_1;c_2\ [Q]}
$$

### Choice
$$
\dfrac{[P]\ c_1\ [Q_1] \quad [P]\ c_2\ [Q_2]}{[P]\ c_1 + c_2\ [Q_1 \lor Q_2]}
$$

### Consequence — Reverse of HL!
$$
\dfrac{P' \Rightarrow P \quad [P']\ c\ [Q'] \quad Q \Rightarrow Q'}{[P]\ c\ [Q]}
$$

**For IL:** Shrink the postcondition (scalable bug detection)

### Choice Rules (Dropping Disjuncts)
$$
\dfrac{[P]\ c_1\ [Q]}{[P]\ c_1 + c_2\ [Q]} \qquad
\dfrac{[P]\ c_2\ [Q]}{[P]\ c_1 + c_2\ [Q]}
$$

### If-then-else (Derived)
$$
\dfrac{[P \land b]\ c_1\ [Q_1] \quad [P \land \neg b]\ c_2\ [Q_2]}{[P]\ \texttt{if } b \texttt{ then } c_1 \texttt{ else } c_2\ [Q_1 \lor Q_2]}
$$

### Loop: Bounded Unrolling
$$
\dfrac{[P]\ c^\star; c\ [Q]}{[P]\ c^\star\ [Q]} \quad \dfrac{}{[P]\ c^\star\ [P]}
$$

### Backwards Variant (Weak)
$$
\dfrac{\forall n\in\mathbb{N}.\ [P_n]\ c\ [P_{n+1}]}{[P_0]\ c^\star\ [\exists k.\ P_k]}
$$

### Principle of Agreement
If $[P']\ c\ [Q']$ and $P' \Rightarrow P$ and $\{P\}\ c\ \{Q\}$, then $Q' \Rightarrow Q$.

### Principle of Denial
If $[P']\ c\ [Q']$ and $P' \Rightarrow P$ and $\neg(Q' \Rightarrow Q)$, then $\neg(\{P\}\ c\ \{Q\})$.

<hr>


# Lecture 06 — Real Incorrectness Logic

See Lecture 05 — IL. This lecture covers the practical application of Incorrectness Logic with realistic programming language features, including:

- **Non-determinism:** $x := \texttt{nondet}()$
- **Error detection:** $\texttt{error}()$ kills execution path
- **Loop unrolling in practice:** finite unrolling $c^n$ for bug detection

## Key Insight for IL

| HL | IL |
|----|-----|
| You get to **forget** information as you go along a path, but you **must remember all the paths** | You **must remember** information as you go along a path, but you **get to forget** some of the paths |

<hr>


# Lecture 07 — More IL: Non-termination and Control

## Non-termination Analysis

- **Over-approximation** of reachable states: find $Q \supseteq \llbracket c\rrbracket\sigma$ such that $Q \subseteq \emptyset$ → proves non-termination
- **Under-approximation** of reachable states: find $Q \subseteq \llbracket c\rrbracket\sigma$ such that $Q \supset \emptyset$ → proves termination

## Control Flow in IL

- **Guarded commands:** $b?$ acts as filter
- **Non-deterministic choice:** $+$ represents branching
- **Encoding errors:** $\texttt{error}()$ has empty semantics $\llbracket \texttt{error}()\rrbracket P = \emptyset$

<hr>


# Lecture 08 — Symbolic Incorrectness Logic (SIL)

## Key Idea

SIL extends IL with **symbolic execution** to handle:

- Complex data structures
- Path-sensitive analysis
- Compositional reasoning

### Symbolic States

Instead of concrete states $\sigma: X \to \mathbb{Z}$, SIL uses **symbolic states** with:

- Path conditions (formulas on input variables)
- Symbolic variable bindings

### SIL Rules

Similar to IL but with symbolic substitutions and path constraints carried along through execution paths.

<hr>


# Lecture 09 — Separation Logic (SL)

## Key Idea

SL extends Hoare Logic to reason about **heap-manipulating programs** (pointers, mutable data structures).

### Heap Model

- **Stack:** variables mapped to values $\sigma: \text{Var} \to \text{Val}$
- **Heap:** memory locations mapped to values $h: \text{Loc} \rightharpoonup_\text{fin} \text{Val}$
- **State:** $(\sigma, h)$

### Separation Connectives

- **Separating conjunction:** $P \star Q$ — $P$ and $Q$ hold for **disjoint** portions of the heap
- **Separating implication (magic wand):** $P \mathrel{-\!\!*} Q$ — if a disjoint heap satisfying $P$ is added, then $Q$ holds

### Key SL Rules

$$
\dfrac{}{\{Q[e/x]\}\ x := e\ \{Q\}}
$$

$$
\dfrac{}{\{x \hookrightarrow -\}\ \texttt{ dispose}(x)\ \{\texttt{true}\}}
$$

**Frame Rule:**
$$
\dfrac{\{P\}\ c\ \{Q\}}{\{P \star R\}\ c\ \{Q \star R\}}
$$
where $c$ does not modify free variables of $R$.

<hr>


# Lecture 10 — Incorrectness Separation Logic (ISL) and Symbolic Execution Separation Logic (SepSIL)

## ISL

ISL combines Incorrectness Logic with Separation Logic for **bug finding in heap-manipulating programs**.

Key idea: Under-approximate reasoning + separation logic for heap.

## SepSIL

Symbolic execution with separation logic for bug finding:

- Tracks symbolic heap configurations
- Under-approximate: only reachable states are reported
- Can detect memory errors (dangling pointers, double free, leaks)

<hr>


# Lecture 11 — Abstract Interpretation: Basic Ideas

## Core Concept

Abstract interpretation provides a **systematic framework** for designing sound static analyses:

1. Start with **concrete semantics** $\llbracket c\rrbracket : \wp(\Sigma) \to \wp(\Sigma)$
2. Choose an **abstract domain** modeling properties of interest
3. Define **abstract semantics** $\llbracket c\rrbracket^\#$ that executes commands on the abstract domain
4. Prove **correctness**: the abstract semantics soundly approximates the concrete
5. Compute fixpoints for loops

### Why Abstraction?

Due to Rice's Theorem, we cannot have exact automatic analysis. We must:

- Trade precision for decidability
- Accept "don't know" answers (sound over-approximation)

### Abstraction Levels

```
Concrete:  infinite set of states
    ↓
Abstract:  finite/simple property (e.g., sign of variable)
```

**Soundness principle:** If the analysis says YES, the property definitely holds.

<hr>


# Lecture 12 — Abstract Interpretation: Formal Foundations

## Lattice Theory

A **complete lattice** $(L, \sqsubseteq, \bot, \top, \sqcup, \sqcap)$:

- $\sqsubseteq$: partial order
- $\bot$: least element
- $\top$: greatest element
- $\sqcup$: least upper bound (join)
- $\sqcap$: greatest lower bound (meet)

### Concrete Domain

$(\wp(\Sigma), \subseteq, \emptyset, \Sigma, \cup, \cap)$ is a complete lattice.

## Galois Connections

A **Galois connection** $(C, \alpha, \gamma, A)$ between concrete domain $C$ and abstract domain $A$:

$$
\alpha(c) \sqsubseteq_A a \iff c \sqsubseteq_C \gamma(a)
$$

- $\alpha: C \to A$ — abstraction function
- $\gamma: A \to C$ — concretization function

Properties:

- $\alpha$ and $\gamma$ are monotone
- $\gamma \circ \alpha$ is extensive ($x \sqsubseteq \gamma(\alpha(x))$)
- $\alpha \circ \gamma$ is reductive ($\alpha(\gamma(y)) \sqsubseteq y$)

## Galois Insertion

A Galois insertion adds: $\alpha \circ \gamma = \text{id}_A$ (no redundant abstract elements).

## Abstract Semantics Soundness

For each atomic command:
$$
\alpha \circ \llbracket c\rrbracket \sqsubseteq \llbracket c\rrbracket^\# \circ \alpha
$$

Or equivalently:
$$
\llbracket c\rrbracket \circ \gamma \sqsubseteq \gamma \circ \llbracket c\rrbracket^\#
$$

### Fixpoint Approximation

For loops: $\text{lfp}(F) \sqsubseteq \gamma(\text{lfp}(F^\#))$ where $F$ and $F^\#$ are the concrete and abstract transformers.

**Kleene fixpoint theorem:** $\text{lfp}(F) = \bigsqcup_{n \ge 0} F^n(\bot)$

### Widening

To ensure termination of fixpoint computation:

- **Widening operator** $\nabla$: accelerates convergence
- $x \nabla y \sqsupseteq x \sqcup y$
- Every ascending chain stabilizes after finitely many widenings

<hr>


# Lecture 13 — Galois Connections

## Properties of Galois Connections

1. $\alpha$ preserves arbitrary joins: $\alpha(\bigsqcup X) = \bigsqcup \alpha(X)$
2. $\gamma$ preserves arbitrary meets: $\gamma(\bigsqcap Y) = \bigsqcap \gamma(Y)$
3. $\alpha$ is uniquely determined by $\gamma$ and vice versa

### Closure Operators

$A \circ \gamma$ is a **closure operator**:

- Monotone: $x \sqsubseteq y \Rightarrow \rho(x) \sqsubseteq \rho(y)$
- Extensive: $x \sqsubseteq \rho(x)$
- Idempotent: $\rho(\rho(x)) = \rho(x)$

In a Galois insertion, $\rho = \gamma \circ \alpha$ is the **closure**.

<hr>


# Lecture 14 — Abstract Domains

## Sign Domain

```
       ℤ
      / \
   ℤ≤0  ℤ≥0
   / \   / \
  ℤ<0 ℤ=0 ℤ>0
       |
       ∅
```

Where:

- $\bot = \emptyset$ (impossible)
- $\top = \mathbb{Z}$ (any value)
- $ℤ_{\ge 0} = \{n \mid n \ge 0\}$
- $ℤ_{\le 0} = \{n \mid n \le 0\}$
- $ℤ_{> 0} = \{n \mid n > 0\}$
- $ℤ_{< 0} = \{n \mid n < 0\}$
- $ℤ_{= 0} = \{0\}$

### Relational vs Non-relational Domains

- **Non-relational:** Track each variable independently (e.g., Sign, Interval)
- **Relational:** Track relationships between variables (e.g., Polyhedra, Octagons)

| Domain | Expressiveness | Cost |
|--------|---------------|------|
| Sign | Signs of variables | $O(n)$ |
| Interval | $x \in [l, u]$ | $O(n)$ |
| Octagon | $\pm x \pm y \le c$ | $O(n^2)$ |
| Polyhedron | $\sum a_i x_i \le c$ | $O(2^n)$ |
| Congruence | $x \equiv a \pmod{m}$ | $O(n)$ |

<hr>


# Lecture 15 — Abstract Analysis (Fixpoint Computation)

### Computing Abstract Semantics

1. Build **control flow graph** (CFG) with program points
2. Associate **abstract invariant** with each program point
3. Compute **least fixpoint** of the abstract semantic function

### Worklist Algorithm

Initialize all program points to $\bot$ (or initial values for entry point).

Iterate:

1. Pick a program point whose abstract value changed
2. Apply abstract transformer to successors
3. Join new values with existing abstract values
4. If any successor's value changed, add to worklist

Until worklist is empty (fixpoint reached).

### Widening in Practice

At loop head: merge old and new abstract values using $\nabla$ to ensure termination.

**Example (Interval widening):**
$[l_1, u_1] \nabla [l_2, u_2] = [\text{if } l_2 < l_1 \text{ then } -\infty \text{ else } l_1, \text{ if } u_2 > u_1 \text{ then } +\infty \text{ else } u_1]$

<hr>


# Lecture 16 — Local Completeness Logic (LCL)

## Completeness in Abstract Interpretation

**Best abstract correct approximation (bca):**
$$
\llbracket c\rrbracket^\#_A = \alpha \circ \llbracket c\rrbracket \circ \gamma
$$

**Completeness equation:**
$$
\forall P.\ \alpha(\llbracket c\rrbracket P) = \alpha(\llbracket c\rrbracket(\gamma(\alpha(P))))
$$

Or equivalently:
$$
\alpha \circ \llbracket c\rrbracket = \alpha \circ \llbracket c\rrbracket \circ \gamma \circ \alpha
$$

### Local Completeness

A triple $\{P\}\ c\ \{Q\}$ is **locally complete** if the completeness equation holds when starting from $P$.

### LCL Triples

$$
\langle P \rangle\ c\ \langle Q \rangle
$$

where $\alpha_P$ is the abstraction relative to property $P$.

<hr>


# Lecture 17 — Control Flow Analysis (CFA)

## Introduction

CFA is a **constraint-based** static analysis technique for higher-order programs (functional languages, $\pi$-calculus).

### Goal

Given a program, determine **which functions may be called at each call site** and **which values may flow to which variables**.

### 0-CFA

The simplest CFA — **monovariant** (one abstract value per program point regardless of calling context).

**Algorithm:**

1. Assign each subexpression a label
2. Generate constraints based on program structure
3. Solve constraints via fixpoint computation

### AST vs CFG

The **Abstract Syntax Tree (AST)** captures the syntactic structure of a program — what the program looks like. The **Control Flow Graph (CFG)** captures the possible execution paths — how the program may execute.

For simple imperative languages, building a CFG from an AST is straightforward because procedure calls explicitly name their targets. For higher-order languages, this becomes non-trivial: **functions are values**, so we often do not know at compile time which function is called at a given call site.

### The Dynamic Dispatch Problem

Consider:

```
let f = fn x => x 1;
    g = fn y => y + 2;
    h = fn z => z + 3
in (f g) + (f h)
```

- Variable $x$ in the body of $f$ is a function variable
- At runtime, $x \in \{g, h\}$
- So `x 1` may target either `g` or `h` (from the two calls `(f g)` and `(f h)`)

We cannot know the exact target of a call statically, so we compute a **safe approximation** — an over-approximation of the possible targets of each call. This is **Control Flow Analysis (CFA)**.

### Interprocedural Analysis with Higher-Order Functions

In simple imperative languages:

- Construct a CFG for **each function**
- Glue them together via function calls and returns
- Calls have **statically known targets**

In higher-order languages:

- Several functions may be invoked at a call site
- Which functions are called depends on data flow
- But data flow analysis first requires a CFG!
- The boundary between control and data becomes unclear — **everything is both data and control**

CFA solves this circular dependency by approximating the call graph directly from program structure.

### The FUN Language (Syntax)

The core functional language used for CFA:

$$
\begin{aligned}
t &::= c \mid x \mid \texttt{fn } x \Rightarrow e_0 \mid \texttt{fun } f\,x \Rightarrow e_0 \\
e &::= t^\ell \mid (e_1\; e_2)^\ell \mid (\texttt{if } e_0 \texttt{ then } e_1 \texttt{ else } e_2)^\ell \\
  &\mid (\texttt{let } x = e_1 \texttt{ in } e_2)^\ell \mid (e_1 \texttt{ op } e_2)^\ell
\end{aligned}
$$

Each subexpression carries a **label** $\ell \in \text{Lab}$ identifying program points (call sites, expression occurrences).

### Abstract Domains

The result of a 0-CFA analysis is a pair $(\hat{C}, \hat{\rho})$:

- $\hat{C} \in \text{Cache} = \text{Lab} \to \hat{V}$ — the **cache**, mapping each label to the set of function abstractions the subexpression may evaluate to
- $\hat{\rho} \in \text{Env} = \text{Var} \to \hat{V}$ — the **abstract environment**, mapping each variable to the set of function abstractions it may be bound to
- $\hat{v} \in \hat{V} = \wp(\text{Term})$ — **abstract values** as sets of function terms (only functions, no constants in pure CFA)

0-CFA means **monovariant**: no context information is considered; the same function set is used at all call sites.

### Specification of a Solution

A guess $(\hat{C}, \hat{\rho})$ is **acceptable** for expression $e$ if it safely over-approximates all runtime behaviour. This is formalised by the **acceptability relation**:

$$
(\hat{C}, \hat{\rho}) \models e
$$

The $\models$ relation is defined by structural clauses for each syntactic form. It is a coinductively defined relation (to handle recursive function calls).

<hr>


### Acceptability Clauses (with Examples)

#### [con] Constants

$$
(\hat{C}, \hat{\rho}) \models c^\ell \iff \emptyset \subseteq \hat{C}(\ell)
$$

**Meaning:** Constants do not evaluate to functions, so there are no demands on $\hat{C}(\ell)$.

**Example:** $e = 71^1$ gives $\hat{C}(1) = \emptyset$.

#### [var] Variables

$$
(\hat{C}, \hat{\rho}) \models x^\ell \iff \hat{\rho}(x) \subseteq \hat{C}(\ell)
$$

**Meaning:** Everything the variable $x$ may be bound to must be included in what is observed at program point $\ell$. Information flows from $\hat{\rho}$ to $\hat{C}$.

**Example:** $e = x^1$, and suppose $\hat{\rho}(x) = \{\texttt{fn } y \Rightarrow y^3\}$. Then $\hat{C}(1) \supseteq \{\texttt{fn } y \Rightarrow y^3\}$.

#### [fn] Function Abstraction

$$
(\hat{C}, \hat{\rho}) \models (\texttt{fn } x \Rightarrow e_0)^\ell \iff \{\texttt{fn } x \Rightarrow e_0\} \subseteq \hat{C}(\ell)
$$

**Meaning:** The function term itself must be included in $\hat{C}(\ell)$ as it may be used as a value at that program point. The function body $e_0$ is **not** checked here — it will be checked at application time.

**Example:** $e = (\texttt{fn } x \Rightarrow x^1)^2$ gives $\hat{C}(2) \supseteq \{\texttt{fn } x \Rightarrow x^1\}$.

#### [fun] Recursive Function

$$
(\hat{C}, \hat{\rho}) \models (\texttt{fun } f\,x \Rightarrow e_0)^\ell \iff \{\texttt{fun } f\,x \Rightarrow e_0\} \subseteq \hat{C}(\ell)
$$

Same as [fn], but the function may be self-referential.

#### [if] Conditional

$$
(\hat{C}, \hat{\rho}) \models (\texttt{if } t_0^{\ell_0} \texttt{ then } t_1^{\ell_1} \texttt{ else } t_2^{\ell_2})^\ell \iff
\begin{cases}
(\hat{C}, \hat{\rho}) \models t_0^{\ell_0} \\
(\hat{C}, \hat{\rho}) \models t_1^{\ell_1} \;\land\; \hat{C}(\ell_1) \subseteq \hat{C}(\ell) \\
(\hat{C}, \hat{\rho}) \models t_2^{\ell_2} \;\land\; \hat{C}(\ell_2) \subseteq \hat{C}(\ell)
\end{cases}
$$

**Meaning:** All subexpressions are checked; values from both branches are merged (the condition is ignored — this is an over-approximation).

**Example:**
$$
e = (\texttt{if } (x^1 > 0^2)^3 \texttt{ then } (\texttt{fn } y \Rightarrow y^4)^5 \texttt{ else } (\texttt{fn } z \Rightarrow z^6)^7)^8
$$
gives $\hat{C}(5) \subseteq \hat{C}(8)$ and $\hat{C}(7) \subseteq \hat{C}(8)$, merging both possible closures.

#### [op] Binary Operation

$$
(\hat{C}, \hat{\rho}) \models (t_1^{\ell_1} \texttt{ op } t_2^{\ell_2})^\ell \iff
\begin{cases}
(\hat{C}, \hat{\rho}) \models t_1^{\ell_1} \\
(\hat{C}, \hat{\rho}) \models t_2^{\ell_2}
\end{cases}
$$

**Meaning:** Sub-expressions are checked; but no data demands on $\hat{C}(\ell)$ — pure CFA does not track data values.

**Example:** $e = (7^1 + 4^2)^3$ gives $\hat{C}(3) = \emptyset$ (no functions flow here).

#### [let] Let Binding

$$
(\hat{C}, \hat{\rho}) \models (\texttt{let } x = t_1^{\ell_1} \texttt{ in } t_2^{\ell_2})^\ell \iff
\begin{cases}
(\hat{C}, \hat{\rho}) \models t_1^{\ell_1} \\
(\hat{C}, \hat{\rho}) \models t_2^{\ell_2} \\
\hat{C}(\ell_1) \subseteq \hat{\rho}(x) \\
\hat{C}(\ell_2) \subseteq \hat{C}(\ell)
\end{cases}
$$

**Meaning:** Two flows are enforced:

1. **Binding:** values produced by $t_1$ (at $\ell_1$) flow to the variable $x$
2. **Evaluation:** values produced by the body $t_2$ (at $\ell_2$) flow to the result of the let-expression (at $\ell$)

**Example:**
$$
e = (\texttt{let } f = (\texttt{fn } x \Rightarrow x^1)^2 \texttt{ in } (f^3\; 3^4)^5)^6
$$
gives $\hat{C}(2) \subseteq \hat{\rho}(f)$ and $\hat{C}(5) \subseteq \hat{C}(6)$.

#### [app] Function Application

$$
(\hat{C}, \hat{\rho}) \models (t_1^{\ell_1}\; t_2^{\ell_2})^\ell \iff
\begin{cases}
(\hat{C}, \hat{\rho}) \models t_1^{\ell_1} \\
(\hat{C}, \hat{\rho}) \models t_2^{\ell_2} \\
\forall (\texttt{fn } x \Rightarrow t_0^{\ell_0}) \in \hat{C}(\ell_1): \\
\quad (\hat{C}, \hat{\rho}) \models t_0^{\ell_0} \\
\quad \land\; \hat{C}(\ell_2) \subseteq \hat{\rho}(x) \\
\quad \land\; \hat{C}(\ell_0) \subseteq \hat{C}(\ell) \\
\forall (\texttt{fun } f\,x \Rightarrow t_0^{\ell_0}) \in \hat{C}(\ell_1): \\
\quad (\hat{C}, \hat{\rho}) \models t_0^{\ell_0} \\
\quad \land\; \hat{C}(\ell_2) \subseteq \hat{\rho}(x) \\
\quad \land\; \hat{C}(\ell_0) \subseteq \hat{C}(\ell) \\
\quad \land\; \{\texttt{fun } f\,x \Rightarrow t_0^{\ell_0}\} \subseteq \hat{\rho}(f)
\end{cases}
$$

**Meaning:** For each function term that may reach $\ell_1$ (the operator position):

1. The function body $t_0$ must be analysed
2. The actual argument (at $\ell_2$) flows to the formal parameter $x$
3. The result of the body (at $\ell_0$) flows to the result of the application (at $\ell$)
4. For recursive functions, the function itself also flows to its name $f$

### Summary of Acceptability Clauses

| Construct | Clause |
|:---|:---|
| $c^\ell$ | $\emptyset \subseteq \hat{C}(\ell)$ |
| $x^\ell$ | $\hat{\rho}(x) \subseteq \hat{C}(\ell)$ |
| $(\texttt{fn } x \Rightarrow e_0)^\ell$ | $\{\texttt{fn } x \Rightarrow e_0\} \subseteq \hat{C}(\ell)$ |
| $(\texttt{fun } f\,x \Rightarrow e_0)^\ell$ | $\{\texttt{fun } f\,x \Rightarrow e_0\} \subseteq \hat{C}(\ell)$ |
| $(\texttt{if } t_0 \texttt{ then } t_1 \texttt{ else } t_2)^\ell$ | Sub-checks + $\hat{C}(\ell_1) \subseteq \hat{C}(\ell) \land \hat{C}(\ell_2) \subseteq \hat{C}(\ell)$ |
| $(t_1 \texttt{ op } t_2)^\ell$ | Sub-checks only |
| $(\texttt{let } x = t_1 \texttt{ in } t_2)^\ell$ | Sub-checks + $\hat{C}(\ell_1) \subseteq \hat{\rho}(x) \land \hat{C}(\ell_2) \subseteq \hat{C}(\ell)$ |
| $(t_1\; t_2)^\ell$ | Sub-checks + $\forall\texttt{fn }x\Rightarrow t_0^{\ell_0} \in \hat{C}(\ell_1):$ $\hat{C}(\ell_2) \subseteq \hat{\rho}(x) \land \hat{C}(\ell_0) \subseteq \hat{C}(\ell)$ |

### Example: Identity Function Composition

Expression:
$$
e = ((\texttt{fn } x \Rightarrow x^1)^2 \; (\texttt{fn } y \Rightarrow y^3)^4)^5
$$

**Runtime behaviour:** $(\lambda x. x)(\lambda y. y) \to (\lambda y. y)$ — evaluates to the identity function.

**CFA guess $(\hat{C}_e, \hat{\rho}_e)$:**

- $\hat{C}(1) = \{\texttt{fn } y \Rightarrow y^3\}$, $\hat{C}(4) = \{\texttt{fn } y \Rightarrow y^3\}$, $\hat{C}(5) = \{\texttt{fn } y \Rightarrow y^3\}$
- $\hat{C}(2) = \{\texttt{fn } x \Rightarrow x^1\}$, $\hat{C}(3) = \emptyset$
- $\hat{\rho}(x) = \{\texttt{fn } y \Rightarrow y^3\}$, $\hat{\rho}(y) = \emptyset$

**Verification:**

1. [fn] on label 2: $\{\texttt{fn } x \Rightarrow x^1\} \subseteq \hat{C}(2)$ ✓
2. [fn] on label 4: $\{\texttt{fn } y \Rightarrow y^3\} \subseteq \hat{C}(4)$ ✓
3. [app] on label 5: Since $\texttt{fn } x \Rightarrow x^1 \in \hat{C}(2)$:

   - $\hat{C}(4) \subseteq \hat{\rho}(x)$: $\{\texttt{fn } y \Rightarrow y^3\} \subseteq \hat{\rho}(x)$ ✓
   - $\hat{C}(1) \subseteq \hat{C}(5)$: $\{\texttt{fn } y \Rightarrow y^3\} \subseteq \hat{C}(5)$ ✓
4. [var] on label 1: $\hat{\rho}(x) \subseteq \hat{C}(1)$: $\{\texttt{fn } y \Rightarrow y^3\} \subseteq \hat{C}(1)$ ✓

<hr>


### Flow Logic Approach

CFA uses **Flow Logic** — a declarative approach that separates specification from computation:

1. **Specification** (acceptability relation $\models$): describes when analysis results are acceptable
2. **Computation** (constraint solving): computes the least solution

The approach has four steps:

1. Define acceptability (specification) — what is a correct analysis?
2. Define syntax-directed rules — more computationally oriented
3. Generate constraints — a finite set of set-inclusion constraints
4. Solve constraints — compute the least fixpoint

### Historical Context

- **Reynolds**: early analyses of LISP programs
- **Jones**: first to study lambda expressions, introduced control flow analysis
- **Shivers**: formalized CFA for Scheme, basis for constraint-based approaches
- **Nielson, Nielson, Hankin**: Principles of Program Analysis [Chapter 3] — modern constraint-based formulation

<hr>


# Lecture 18 — CFA Exercises

## Exercise 1: Identity Function

Expression:
$$
e \triangleq ((\texttt{fn } x \Rightarrow (x^1 + 12^2)^3)^4 \; (3)^5)^6
$$

**CFA guess $(\hat{C}, \hat{\rho})$:**

| Label | $\hat{C}(\ell)$ |
|:---|:---|
| $\hat{C}(1)$ | $\emptyset$ |
| $\hat{C}(2)$ | $\emptyset$ $(12)$ |
| $\hat{C}(3)$ | $\emptyset$ $(x+12)$ |
| $\hat{C}(4)$ | $\{\texttt{fn } x \Rightarrow (x^1 + 12^2)^3\}$ |
| $\hat{C}(5)$ | $\emptyset$ $(3)$ |
| $\hat{C}(6)$ | $\emptyset$ |

$\hat{\rho}(x) = \emptyset$

**Verification using $(\hat{C}, \hat{\rho}) \models e$:**

1. $(\hat{C}, \hat{\rho}) \models (\texttt{fn } x \Rightarrow (x^1+12^2)^3)^4$: $\{\texttt{fn } x \Rightarrow (x^1+12^2)^3\} \subseteq \hat{C}(4)$ ✓
2. $(\hat{C}, \hat{\rho}) \models (3)^5$: $\emptyset \subseteq \hat{C}(5)$ ✓
3. [app] for $(\hat{C}, \hat{\rho}) \models ((t_1)^4 (3)^5)^6$:

   - $\hat{C}(5) \subseteq \hat{\rho}(x)$ ✓ (both ∅)
   - $\hat{C}(3) \subseteq \hat{C}(6)$ ✓ (both ∅)
4. [var] for $\hat{\rho}(x) \subseteq \hat{C}(1)$ ✓ (both ∅)
5. [con] for $(12)^2$: $\emptyset \subseteq \hat{C}(2)$ ✓

## Exercise 2: Higher-Order Function Composition

Expression:
$$
e \triangleq ((\texttt{fn } f \Rightarrow ((f^1\; 76^2)^3 + (f^4\; 77^5)^6)^7)^8 \; (\texttt{fn } a \Rightarrow a^9)^{10})^{12}
$$

**CFA guess $(\hat{C}, \hat{\rho})$:**

- $\hat{C}(1) = \{\texttt{fn } a \Rightarrow a^9\}$, $\hat{C}(4) = \{\texttt{fn } a \Rightarrow a^9\}$
- $\hat{C}(2) = \emptyset (76)$, $\hat{C}(3) = \emptyset (76)$
- $\hat{C}(5) = \emptyset (77)$, $\hat{C}(6) = \emptyset (77)$
- $\hat{C}(7) = \emptyset (76+77)$, $\hat{C}(8) = \{\texttt{fn } f \Rightarrow ((f^1 76^2)^3 + (f^4 77^5)^6)^7\}$
- $\hat{C}(9) = \emptyset$, $\hat{C}(10) = \{\texttt{fn } a \Rightarrow a^9\}$, $\hat{C}(11) = \emptyset$, $\hat{C}(12) = \{\texttt{fn } f \Rightarrow \dots\}$
- $\hat{\rho}(f) = \{\texttt{fn } a \Rightarrow a^9\}$, $\hat{\rho}(a) = \emptyset (76, 77)$

**Verification (key steps):**

1. [fn] label 8: $\{\texttt{fn } f \Rightarrow \dots\} \subseteq \hat{C}(8)$ ✓
2. [fn] label 10: $\{\texttt{fn } a \Rightarrow a^9\} \subseteq \hat{C}(10)$ ✓
3. [app] label 12: $\hat{C}(10) \subseteq \hat{\rho}(f) \land \hat{C}(8) \subseteq \hat{C}(12)$ ✓
4. For body $(f^1 76^2)^3$:

   - [var] $\hat{\rho}(f) \subseteq \hat{C}(1)$ ✓
   - [con] $\emptyset \subseteq \hat{C}(2)$ ✓
   - [app] $\hat{C}(2) \subseteq \hat{\rho}(a) \land \hat{C}(9) \subseteq \hat{C}(3)$ ✓
5. For body $(f^4 77^5)^6$: symmetric ✓

## Exercise 3: Let Bindings with Multiple Functions

Expression:
$$
\begin{aligned}
e \triangleq \; &(\texttt{let } f = (\texttt{fn } x \Rightarrow (x^1\; 1^2)^3)^4 \\
& \texttt{in } (\texttt{let } g = (\texttt{fn } y \Rightarrow (y^5 + 2^6)^7)^8 \\
& \texttt{in } (\texttt{let } h = (\texttt{fn } z \Rightarrow (z^9 + 3^{10})^{11})^{12} \\
& \texttt{in } ((f^{13}\; g^{14})^{15} + (f^{16}\; h^{17})^{18})^{19})^{20})^{21})^{22}
\end{aligned}
$$

This is the earlier dynamic dispatch example. The 0-CFA result will merge:

- $\hat{C}(1) = \{\texttt{fn } y \Rightarrow (y^5+2^6)^7,\; \texttt{fn } z \Rightarrow (z^9+3^{10})^{11}\}$ (both functions flow to $x$)
- $\hat{C}(15) = \{\texttt{fn } y \Rightarrow (y^5+2^6)^7,\; \texttt{fn } z \Rightarrow (z^9+3^{10})^{11}\}$ (both results possible)

**Key observation:** 0-CFA cannot distinguish the two calling contexts for $f$: both `g` and `h` flow to parameter $x$.

## Semantic Correctness

### Operational Semantics for FUN

To prove that acceptable CFA results are semantically correct, we define a small-step structural operational semantics for FUN.

**Values and environments:**

- $v \in \text{Val}$: values (constants or closures)
- $\rho \in \text{Env}$: concrete environments (mapping variables to values)
- $v ::= c \mid \langle t, \rho \rangle$ (closures)
- $\rho ::= [] \mid \rho[x \mapsto v]$

**Intermediate expressions:**

$$
ie ::= it^\ell \mid ie_0\; ie_1 \mid \texttt{let } x = ie_1 \texttt{ in } ie_2 \mid \rho\; ie
$$

**Selected transition rules:**

- [var] $\rho \vdash x^\ell \to v^\ell$ if $\rho(x) = v$
- [fn] $\rho \vdash (\texttt{fn } x \Rightarrow e_0)^\ell \to \langle (\texttt{fn } x \Rightarrow e_0), \rho_0\rangle^\ell$ where $\rho_0 = \rho|_{FV(\texttt{fn } x \Rightarrow e_0)}$
- [let2] $\rho \vdash (\texttt{let } x = v_1^{\ell_1} \texttt{ in } e_2)^\ell \to (\rho_0[x \mapsto v_1]\; e_2)^\ell$ where $\rho_0 = \rho|_{FV(e_2)}$

### Subject Reduction

**Theorem (Subject Reduction):** If $(\hat{C}, \hat{\rho}) \models ie$ and $\rho \vdash ie \to ie'$ (with $\rho$ agreeing with $\hat{\rho}$), then $(\hat{C}, \hat{\rho}) \models ie'$.

The analysis information is preserved under computation — it is a sound over-approximation of all reachable states.

<hr>


# Lecture 19 — Syntax-Directed CFA

## Motivation

The original $\models$ relation has a problem: it is **coinductively defined** because of circular dependencies in recursive functions. This makes it non-constructive — we cannot directly compute from it.

The **syntax-directed** version $\models_s$ addresses this:

- It analyses each function body **once**, at its definition site
- It does not wait for applications to trigger body analysis
- It is fully determined by the **structure** of the expression (hence "syntax-directed")
- It eliminates the need for coinduction (no circular dependencies)

**Key property:** $\models_s$ is a **safe approximation** of $\models$:
$$
(\hat{C}, \hat{\rho}) \models_s e \;\Rightarrow\; (\hat{C}, \hat{\rho}) \models e \quad\text{(for program terms)}
$$

### Syntax-Directed Clauses

#### [fn] (modified)

$$
(\hat{C}, \hat{\rho}) \models_s (\texttt{fn } x \Rightarrow e_0)^\ell \iff
\begin{cases}
\{\texttt{fn } x \Rightarrow e_0\} \subseteq \hat{C}(\ell) \\
(\hat{C}, \hat{\rho}) \models_s e_0
\end{cases}
$$

**Difference from $\models$:** The function body $e_0$ is **now analysed at definition time**, even if the function is never applied.

#### [fun] (modified)

$$
(\hat{C}, \hat{\rho}) \models_s (\texttt{fun } f\,x \Rightarrow e_0)^\ell \iff
\begin{cases}
\{\texttt{fun } f\,x \Rightarrow e_0\} \subseteq \hat{C}(\ell) \\
(\hat{C}, \hat{\rho}) \models_s e_0 \\
\{\texttt{fun } f\,x \Rightarrow e_0\} \subseteq \hat{\rho}(f)
\end{cases}
$$

Self-binding is enforced immediately.

#### [app] (modified)

$$
(\hat{C}, \hat{\rho}) \models_s (t_1^{\ell_1}\; t_2^{\ell_2})^\ell \iff
\begin{cases}
(\hat{C}, \hat{\rho}) \models_s t_1^{\ell_1} \\
(\hat{C}, \hat{\rho}) \models_s t_2^{\ell_2} \\
\forall (\texttt{fn } x \Rightarrow t_0^{\ell_0}) \in \hat{C}(\ell_1): \\
\quad \hat{C}(\ell_2) \subseteq \hat{\rho}(x) \;\land\; \hat{C}(\ell_0) \subseteq \hat{C}(\ell) \\
\forall (\texttt{fun } f\,x \Rightarrow t_0^{\ell_0}) \in \hat{C}(\ell_1): \\
\quad \hat{C}(\ell_2) \subseteq \hat{\rho}(x) \;\land\; \hat{C}(\ell_0) \subseteq \hat{C}(\ell)
\end{cases}
$$

**Difference:** The body has already been analysed by [fn] at definition time, so there is no $(\hat{C}, \hat{\rho}) \models_s t_0^{\ell_0}$ here.

All other clauses are unchanged from $\models$ (just replace $\models$ with $\models_s$).

### Worked Example: Recursive Function

Consider:
$$
\text{loop} \triangleq (\texttt{let } g = (\texttt{fun } f\,x \Rightarrow (f^1\; (\texttt{fn } y \Rightarrow y^2)^3)^4)^5 \texttt{ in } (g^6\; (\texttt{fn } z \Rightarrow z^7)^8)^9)^{10}
$$

**Step-by-step validation with $\models_s$:**

1. $(\hat{C}_{lp}, \hat{\rho}_{lp}) \models_s \text{loop}^{10}$:

   - [let]: check body $(\texttt{fun } f\,x \Rightarrow \dots)^5$ and $(g^6\; (\texttt{fn } z \Rightarrow z^7)^8)^9$
   - $\hat{C}_{lp}(5) \subseteq \hat{\rho}_{lp}(g)$ and $\hat{C}_{lp}(9) \subseteq \hat{C}_{lp}(10)$

2. [fun] on label 5: $\{\texttt{fun } f\,x \Rightarrow \dots\} \subseteq \hat{C}_{lp}(5)$ and $\{\texttt{fun } f\,x \Rightarrow \dots\} \subseteq \hat{\rho}_{lp}(f)$, and analyse body $(f^1\; (\texttt{fn } y \Rightarrow y^2)^3)^4$

3. [app] on label 4 (body): $\texttt{fun } f\,x \Rightarrow \dots \in \hat{C}(1)$ triggers:

   - $\hat{C}(3) \subseteq \hat{\rho}_{lp}(x)$
   - $\hat{C}(4) \subseteq \hat{C}(4)$ (immediate)

4. [fn] on label 3: $\{\texttt{fn } y \Rightarrow y^2\} \subseteq \hat{C}_{lp}(3)$

5. [app] on label 9: with $\hat{C}(6) = \{g\}$:

   - $\hat{C}(8) \subseteq \hat{\rho}_{lp}(x)$
   - $\hat{C}(4) \subseteq \hat{C}(9)$

The solution is acceptable under $\models_s$ — no circular dependency, no need for coinduction.

### Uniqueness of $\models_s$

The syntax-directed specification is **deterministic**: there is only one relation $\models_s$ satisfying the clauses. Given the structural nature of the definition, any two relations $\models'_s$ and $\models''_s$ that satisfy the clauses must be the same.

**Proof sketch (structural induction):** For any $e$,

- Base case $c^\ell$: both relations satisfy $\emptyset \subseteq \hat{C}(\ell)$ — trivially equivalent
- Base case $x^\ell$: both require $\hat{\rho}(x) \subseteq \hat{C}(\ell)$ — equivalent
- Inductive step $(\texttt{fn } x \Rightarrow e_0)^\ell$: both require $\{\texttt{fn } x \Rightarrow e_0\} \subseteq \hat{C}(\ell)$ and $\models_s e_0$ — equivalence by IH on $e_0$
- All other cases analogous

Therefore, the least/greatest fixpoint distinction is irrelevant for $\models_s$.

### Counterexample: Non-Syntax-Directed Version

For the original $\models$ (non-syntax-directed), different relations can satisfy the same clauses. Example:

$$
a \triangleq (0^1\; 0^2)^3, \quad e \triangleq (\texttt{fn } x \Rightarrow a^4)^5
$$

Suppose $\hat{C}(1) = \{\texttt{fn } x \Rightarrow a^4\}$, $\hat{C}(2) = \hat{C}(3) = \hat{\rho}(x) = \emptyset$. Then $(\hat{C}, \hat{\rho}) \models a^3$ can be either true or false (because the body $a$ has a circular dependency). Both interpretations satisfy the $\models$ clauses, showing that $\models$ is not unique.

### Existence of Solutions

**Theorem:** For all $e \in \text{Exp}$, the set $\{(\hat{C}, \hat{\rho}) \mid (\hat{C}, \hat{\rho}) \models e\}$ is a **Moore family** (closed under greatest lower bounds).

**Corollaries:**

1. Every expression $e$ admits at least one CFA (take the intersection over the empty set $Y' = \emptyset$)
2. Every expression $e$ has a **least** (most precise) CFA: intersect all acceptable analyses

### Moore Family Proof (Idea)

The proof proceeds by coinduction on $e$:

- Assume $\forall i \in I:\; (\hat{C}_i, \hat{\rho}_i) \models e$
- Show that $(\hat{C}, \hat{\rho}) = \sqcap_i (\hat{C}_i, \hat{\rho}_i)$ satisfies each clause of $\models$
- The pointwise intersection $(\hat{C}(\ell) = \bigcap_i \hat{C}_i(\ell)$, $\hat{\rho}(x) = \bigcap_i \hat{\rho}_i(x))$ preserves all set inclusions

### Preservation of Solutions (Syntax-Directed vs Original)

The syntax-directed specification preserves solutions of the original:

$$
(\hat{C}, \hat{\rho}) \models_s e \;\Rightarrow\; (\hat{C}, \hat{\rho}) \models e
$$

**Proof idea:** A simple structural induction on $e$ shows that any pair accepted by $\models_s$ also satisfies all the clauses of $\models$. The only difference is when function bodies are checked: $\models_s$ does it upfront, $\models$ does it at application time. Since all bodies are checked by $\models_s$, they will also be available when $\models$ needs them.

<hr>


# Lecture 20 — Constraint-Based 0-CFA

## From Semantics to Constraints

The syntax-directed specification $\models_s$ can be turned into a **finite set of constraints**. The idea is to replace:

- Occurrences of $\hat{C}$ with constraint variable $C(\ell)$
- Occurrences of $\hat{\rho}$ with constraint variable $r(x)$

The function $C^*[\![e]\!]$ maps an expression to a set of constraints of two forms:

1. **Direct constraints:** $\text{lhs} \subseteq \text{rhs}$
2. **Conditional constraints:** $\{t\} \subseteq \text{rhs}' \Rightarrow \text{lhs} \subseteq \text{rhs}$

Where $\text{lhs}, \text{rhs} \in \{C(\ell), r(x), \{t\}\}$.

## Constraint Generation Rules

#### [con] Constants

$$
(\hat{C}, \hat{\rho}) \models_s c^\ell \;\Rightarrow\; C^*[\![c^\ell]\!] = \emptyset
$$

Constants generate no constraints.

#### [var] Variables

$$
(\hat{C}, \hat{\rho}) \models_s x^\ell \;\Rightarrow\; C^*[\![x^\ell]\!] = \{ r(x) \subseteq C(\ell) \}
$$

#### [fn] Functions

$$
C^*[\![(\texttt{fn } x \Rightarrow e_0)^\ell]\!] = \{\{\texttt{fn } x \Rightarrow e_0\} \subseteq C(\ell)\} \cup C^*[\![e_0]\!]
$$

#### [fun] Recursive Functions

$$
C^*[\![(\texttt{fun } f\,x \Rightarrow e_0)^\ell]\!] = \{\{\texttt{fun } f\,x \Rightarrow e_0\} \subseteq C(\ell),\; \{\texttt{fun } f\,x \Rightarrow e_0\} \subseteq r(f)\} \cup C^*[\![e_0]\!]
$$

#### [app] Application

$$
\begin{aligned}
C^*[\![(t_1^{\ell_1}\; t_2^{\ell_2})^\ell]\!] = &
C^*[\![t_1]\!] \cup C^*[\![t_2]\!] \; \cup \\
&\{ \{t\} \subseteq C(\ell_1) \Rightarrow C(\ell_2) \subseteq r(x) \mid t = (\texttt{fn } x \Rightarrow t_0^{\ell_0}) \in \text{Term}^* \} \; \cup \\
&\{ \{t\} \subseteq C(\ell_1) \Rightarrow C(\ell_0) \subseteq C(\ell) \mid t = (\texttt{fn } x \Rightarrow t_0^{\ell_0}) \in \text{Term}^* \} \; \cup \\
&\{ \{t\} \subseteq C(\ell_1) \Rightarrow C(\ell_2) \subseteq r(x) \mid t = (\texttt{fun } f\,x \Rightarrow t_0^{\ell_0}) \in \text{Term}^* \} \; \cup \\
&\{ \{t\} \subseteq C(\ell_1) \Rightarrow C(\ell_0) \subseteq C(\ell) \mid t = (\texttt{fun } f\,x \Rightarrow t_0^{\ell_0}) \in \text{Term}^* \}
\end{aligned}
$$

#### [let] Let Binding

$$
C^*[\![(\texttt{let } x = t_1^{\ell_1} \texttt{ in } t_2^{\ell_2})^\ell]\!] = C^*[\![t_1]\!] \cup C^*[\![t_2]\!] \cup \{ C(\ell_1) \subseteq r(x),\; C(\ell_2) \subseteq C(\ell) \}
$$

## Worked Example: Constraint Generation

Expression:
$$
((\texttt{fn } x \Rightarrow x^1)^2 \; (\texttt{fn } y \Rightarrow y^3)^4)^5
$$

**Term set:** $\text{Term}^* = \{\texttt{fn } x \Rightarrow x^1,\; \texttt{fn } y \Rightarrow y^3\}$

**Generated constraints:**

From [fn] on label 2: $\{\texttt{fn } x \Rightarrow x^1\} \subseteq C(2)$
From [fn] on label 4: $\{\texttt{fn } y \Rightarrow y^3\} \subseteq C(4)$
From [var] on label 1: $r(x) \subseteq C(1)$
From [var] on label 3: $r(y) \subseteq C(3)$
From [app] on label 5 (conditional constraints):

- $\{\texttt{fn } x \Rightarrow x^1\} \subseteq C(2) \Rightarrow C(4) \subseteq r(x)$
- $\{\texttt{fn } x \Rightarrow x^1\} \subseteq C(2) \Rightarrow C(1) \subseteq C(5)$
- $\{\texttt{fn } y \Rightarrow y^3\} \subseteq C(2) \Rightarrow C(4) \subseteq r(y)$
- $\{\texttt{fn } y \Rightarrow y^3\} \subseteq C(2) \Rightarrow C(3) \subseteq C(5)$

## Preservation of Solutions

**Proposition:** If $(\hat{C}, \hat{\rho}) \subseteq (\hat{C}_\top, \hat{\rho}_\top)$ and $(\hat{C}, \hat{\rho}) \models_c C^*[\![e^*]\!]$, then $(\hat{C}, \hat{\rho}) \models_s e^*$.

**Proof sketch:** By structural induction on $e^*$:

- For each sub-expression, the constraints in $C^*[\![e]\!]$ encode the exact conditions required by $\models_s$
- The condition $(\hat{C}, \hat{\rho}) \subseteq (\hat{C}_\top, \hat{\rho}_\top)$ ensures $\hat{C}(\ell_1) \subseteq \text{Term}^*$ for the application case
- Base cases (constants, variables) follow directly from the constraint definitions
- Inductive cases follow from the inductive hypothesis on sub-expressions

**Conversely:** If $(\hat{C}, \hat{\rho}) \models_s e^*$, then $(\hat{C}, \hat{\rho}) \models_c C^*[\![e^*]\!]$.

## Solving Constraints via Fixpoint Computation

Finding the least solution of the constraints amounts to computing the **least fixed point** of a monotone function:

$$
F^* : \text{Cache}^* \times \text{Env}^* \to \text{Cache}^* \times \text{Env}^*
$$

The function $F^*$ propagates constraints over $C$ and $r$ until saturation.

### Complexity

| Estimate | Direct | Conditional |
|:---|:---|:---|
| Naive | $O(n^2)$ | $O(n^4)$ |
| Refined | $O(n)$ | $O(n^2)$ |

Where $n = |e^*|$ (size of the expression). Every construct except applications gives one constraint; applications may give $O(n)$ conditional constraints.

**Solving time:**

- Least fixpoint via naive iteration: $O(n^5)$
- With graph formulation: $O(n^3)$

### Constraint Graph

A constraint system can be visualized as a **constraint graph**:

**Nodes:**

- $C(\ell)$ for each label $\ell \in \text{Lab}^*$
- $r(x)$ for each variable $x \in \text{Var}^*$

**Edges:**

- Each direct constraint $p_1 \subseteq p_2$ adds an edge $(p_1, p_2)$
- Each conditional constraint $\{t\} \subseteq p \Rightarrow p_1 \subseteq p_2$ adds:

  - A **candidate edge** $(p_1, p_2)$ with "trigger" $\{t\} \subseteq p$
  - An edge $(p, p_2)$ for trigger propagation

### Example Constraint Graph

For our running example:

```
{r(x) ⊆ C(1)}   {r(y) ⊆ C(3)}
{idx} ⊆ C(2)    {idy} ⊆ C(4)
{idx} ⊆ C(2) ⇒ C(4) ⊆ r(x)
{idx} ⊆ C(2) ⇒ C(1) ⊆ C(5)
{idy} ⊆ C(2) ⇒ C(4) ⊆ r(y)
{idy} ⊆ C(2) ⇒ C(3) ⊆ C(5)
```

Graph:

```
{idx} → C(2) → r(x) → C(1)
{idy} → C(4) → r(y) → C(3)
             C(2) → C(5) (conditional, triggered by idx)
             C(2) → C(5) (conditional, triggered by idy)
```

### Solver Algorithm

**Input:** A set of constraints $C^*[\![e^*]\!]$
**Output:** The least solution $(\hat{C}, \hat{\rho})$
**Data structures:**

- $W$: worklist (nodes whose data should be propagated)
- $D[p]$: data array (current abstract value for node $p$)
- $E[p]$: edge array (constraints that node $p$ may affect)

#### Step 1: Initialize

```
for q in Vars:
    D[q] := [];
    E[q] := [];
W := [];
```

#### Step 2: Build the Graph

```
for cc in C*[[e*]]:
    match cc:
    | {t} ⊆ p         -> add(p, {t})
    | p1 ⊆ p2         -> E[p1] := cc :: E[p1]
    | {t} ⊆ p ⇒ p1 ⊆ p2 -> E[p1] := cc :: E[p1];
                           E[p] := cc :: E[p]
```

Where `add(q, d)` inserts $d$ into $D[q]$ and adds $q$ to $W$ if $d$ is new.

#### Step 3: Propagate

```
while W ≠ nil:
    q := head(W); W := tail(W);
    for cc in E[q]:
        case cc of:
        | p1 ⊆ p2:
            add(p2, D[p1])
        | {t} ⊆ p ⇒ p1 ⊆ p2:
            if t ∈ D[p]:
                add(p2, D[p1])
```

#### Step 4: Record Solution

```
for ℓ in Lab*:  Ĉ(ℓ) := D[C(ℓ)]
for x in Var*:  ρ̂(x) := D[r(x)]
```

### Solver Trace (Example)

**Initialization:**

- $D[C(2)] = \{\texttt{idx}\}$, $D[C(4)] = \{\texttt{idy}\}$, all others empty
- $W = [C(4), C(2)]$ (nodes with initial data)

**Iteration 1 (process $C(4)$):**

- $E[C(4)] = \{\{\texttt{idx}\} \subseteq C(2) \Rightarrow C(4) \subseteq r(x),\; \{\texttt{idy}\} \subseteq C(2) \Rightarrow C(4) \subseteq r(y)\}$
- Trigger $\{\texttt{idx}\} \subseteq C(2)$ is true: $D[r(x)] \mathrel{+}= \{\texttt{idy}\}$, $W = [r(x), C(2)]$
- Trigger $\{\texttt{idy}\} \subseteq C(2)$: not yet true (no $\texttt{idy}$ in $C(2)$ yet)

**Iteration 2 (process $C(2)$):**

- Propagate $D[C(2)] = \{\texttt{idx}\}$ to all successors via direct edges
- Triggers involving $C(2)$: both $\texttt{idx}$ triggers fire
- $D[r(x)] \mathrel{+}= \{\texttt{idx}\}$, $D[C(5)] \mathrel{+}= \{\texttt{idx}\}$ ...

Fixed point is reached when $W$ is empty.

<hr>


# Lecture 21 — CFA with Data and Context

## Abstract Values as Complete Lattices

So far, $\hat{V} = \wp(\text{Term})$ only tracked function abstractions. We now extend to include **data information**, separating:

- **Term information:** which functions ($\wp(\text{Term})$)
- **Data information:** abstract data values

The combined abstract domain:

$$
\hat{v} \in \widehat{\text{Val}_d} = \wp(\text{Term} \cup \text{Data}) \cong \wp(\text{Term}) \times \wp(\text{Data})
$$

We can replace $\wp(\text{Data})$ by a **complete lattice** $L$, and perform a development closely related to Monotone Frameworks.

### A Monotone Structure

A monotone structure consists of:

- A complete lattice $L$
- A set $F$ of monotone functions $L \times L \to L$

An instance maps:

- Constants $c \in \text{Const}$ to lattice values $\iota_c \in L$
- Binary operators $\text{op} \in \text{Op}$ to functions $f_{\text{op}} \in F$

### Constant Propagation Analysis (Example)

For constant propagation, $L = \text{flat}(\mathbb{Z})$:

```
       ⊤
    ... -2 -1 0 1 2 ...
       ⊥
```

- $\iota_c = (c, \emptyset)$ for numeric constant $c$
- $f_+(l_1, l_2)$ combines constants: if both are integer values, add them; if one is $\bot$, result is $\bot$; otherwise $\top$

### Combined CFA + DFA Domains

The analysis tracks four components:

**CFA part:**

- $\hat{C} \in \text{Cache}: \text{Lab} \to \widehat{\text{Val}}$ where $\widehat{\text{Val}} = \wp(\text{Term})$
- $\hat{\rho} \in \text{Env}: \text{Var} \to \widehat{\text{Val}}$

**DFA part:**

- $\hat{D} \in \text{DCache}: \text{Lab} \to L$ (abstract data values at each label)
- $\hat{\delta} \in \text{DEnv}: \text{Var} \to L$ (abstract data values for variables)

**Acceptability relation:**
$$
(\hat{C}, \hat{D}, \hat{\rho}, \hat{\delta}) \models_D e
$$

### Extended Clauses (Selected)

#### [con] Constants
$$
(\hat{C}, \hat{D}, \hat{\rho}, \hat{\delta}) \models_D c^\ell \iff \iota_c \sqsubseteq \hat{D}(\ell)
$$

#### [op] Binary Operation
$$
(\hat{C}, \hat{D}, \hat{\rho}, \hat{\delta}) \models_D (t_1^{\ell_1} \texttt{ op } t_2^{\ell_2})^\ell \iff
\begin{cases}
(\hat{C}, \hat{D}, \hat{\rho}, \hat{\delta}) \models_D t_1^{\ell_1} \\
(\hat{C}, \hat{D}, \hat{\rho}, \hat{\delta}) \models_D t_2^{\ell_2} \\
f_{\text{op}}(\hat{D}(\ell_1), \hat{D}(\ell_2)) \sqsubseteq \hat{D}(\ell)
\end{cases}
$$

#### [if] Conditional (refined)
Provides data-dependent analysis: only analyse branches whose guard is data-possible.

### Staged Analysis

The combined CFA+DFA can be staged:

1. Solve **control flow** $(\hat{C}, \hat{\rho})$ first
2. Solve **data flow** $(\hat{D}, \hat{\delta})$ afterwards

The analysis still yields the least solution of the combined constraints.

## 0-CFA Precision Loss

Consider:
$$
e \triangleq (\texttt{let } f = (\texttt{fn } x \Rightarrow x^1)^2 \texttt{ in } ((f^3\; f^4)^5 \; (\texttt{fn } y \Rightarrow y^6)^7)^8)^9
$$

**0-CFA least solution:**

- $\hat{C}(1) = \{\texttt{fn } x \Rightarrow x^1,\; \texttt{fn } y \Rightarrow y^6\}$ (both functions merged)
- $\hat{C}(8) = \{\texttt{fn } x \Rightarrow x^1,\; \texttt{fn } y \Rightarrow y^6\}$
- $\hat{C}(9) = \{\texttt{fn } x \Rightarrow x^1,\; \texttt{fn } y \Rightarrow y^6\}$

Only $\texttt{fn } y \Rightarrow y^6$ is a possible runtime result, but 0-CFA says both are possible — **precision loss** from merging contexts.

## Context-Sensitive CFA (k-CFA)

### Motivation

Different calling contexts should produce different analyses of the same function. **k-CFA** distinguishes calling contexts up to depth $k$ using **call strings**.

### Call Strings

A **call string** $\hat{\delta} \in \Delta = \text{Lab}^{\le k}$ is a sequence of labels recording the $k$ most recent call sites. The empty call string is $\epsilon$ (or $\Lambda$).

Examples:

- $k = 0$: $\Delta = \{\epsilon\}$ (monovariant — 0-CFA)
- $k = 1$: $\Delta = \{\epsilon\} \cup \text{Lab}$ (call-site sensitivity)
- $k = 2$: $\Delta = \{\epsilon\} \cup \text{Lab} \cup \text{Lab}^2$

### Context Environment

A **context environment** records for each variable the context in which it was defined:

$$
ce \in \text{Cenv} = \text{Var} \to \Delta
$$

### Context-Sensitive Abstract Domains

$$
\begin{aligned}
\hat{v} &\in \widehat{\text{Val}} = \wp(\text{Val} \times \text{Cenv}) \quad\text{(closures paired with context environments)} \\
\hat{\rho} &\in \widehat{\text{Cenv}} = (\text{Var} \times \Delta) \to \widehat{\text{Val}} \\
\hat{C} &\in \widehat{\text{Cache}} = (\text{Lab} \times \Delta) \to \widehat{\text{Val}}
\end{aligned}
$$

### Acceptability with Contexts

The relation becomes context-dependent:

$$
(\hat{C}, \hat{\rho}) \models_{ce}^{\hat{\delta}} e
$$

Where:

- $ce$: current context environment (tracks where each variable was bound)
- $\hat{\delta}$: current calling context (changes when functions are applied)

#### [var] with Context

$$
(\hat{C}, \hat{\rho}) \models_{ce}^{\hat{\delta}} x^\ell \iff \hat{\rho}(x, ce(x)) \subseteq \hat{C}(\ell, \hat{\delta})
$$

**Meaning:** The variable $x$ carries the context $ce(x)$ where it was defined; it is used in the current context $\hat{\delta}$.

#### [fn] with Context

$$
(\hat{C}, \hat{\rho}) \models_{ce}^{\hat{\delta}} (\texttt{fn } x \Rightarrow e_0)^\ell \iff \{(\texttt{fn } x \Rightarrow e_0, ce_0)\} \subseteq \hat{C}(\ell, \hat{\delta})
$$

where $ce_0 = ce|_{FV(\texttt{fn } x \Rightarrow e_0)}$ — the closure captures its definition context environment.

#### [let] with Context

$$
(\hat{C}, \hat{\rho}) \models_{ce}^{\hat{\delta}} (\texttt{let } x = t_1^{\ell_1} \texttt{ in } t_2^{\ell_2})^\ell \iff
\begin{cases}
(\hat{C}, \hat{\rho}) \models_{ce}^{\hat{\delta}} t_1^{\ell_1} \\
(\hat{C}, \hat{\rho}) \models_{ce'}^{\hat{\delta}} t_2^{\ell_2} \\
\hat{C}(\ell_1, \hat{\delta}) \subseteq \hat{\rho}(x, \hat{\delta}) \\
\hat{C}(\ell_2, \hat{\delta}) \subseteq \hat{C}(\ell, \hat{\delta})
\end{cases}
$$

where $ce' = ce[x \mapsto \hat{\delta}]$ — $x$ is defined in the current context.

#### [app] with Context

$$
(\hat{C}, \hat{\rho}) \models_{ce}^{\hat{\delta}} (t_1^{\ell_1}\; t_2^{\ell_2})^\ell \iff
\begin{cases}
(\hat{C}, \hat{\rho}) \models_{ce}^{\hat{\delta}} t_1^{\ell_1} \\
(\hat{C}, \hat{\rho}) \models_{ce}^{\hat{\delta}} t_2^{\ell_2} \\
\forall (\texttt{fn } x \Rightarrow t_0^{\ell_0}, ce_0) \in \hat{C}(\ell_1, \hat{\delta}): \\
\quad (\hat{C}, \hat{\rho}) \models_{ce'_0}^{\hat{\delta}_0} t_0^{\ell_0} \\
\quad \land\; \hat{C}(\ell_2, \hat{\delta}) \subseteq \hat{\rho}(x, \hat{\delta}_0) \\
\quad \land\; \hat{C}(\ell_0, \hat{\delta}_0) \subseteq \hat{C}(\ell, \hat{\delta})
\end{cases}
$$

where $\hat{\delta}_0 = \ulcorner\hat{\delta}, \ell\urcorner_k$ (extend call string with the current call site) and $ce'_0 = ce_0[x \mapsto \hat{\delta}_0]$.

### Three k-CFA Variants

| Variant | Cache Domain | Complexity | Precision |
|:---|:---|:---:|:---:|
| **Uniform k-CFA** | $(\text{Lab} \times \Delta) \to \widehat{\text{Val}}$ | Moderate | Good |
| **Classical k-CFA** | $(\text{Lab} \times \text{Cenv}) \to \widehat{\text{Val}}$ | High | Highest |
| **Polynomial k-CFA** | $\widehat{\text{Val}} = \wp(\text{Val} \times \Delta)$ | Lowest | Lower |

### Worked Example: 1-CFA

For the expression:
$$
e \triangleq (\texttt{let } f = (\texttt{fn } x \Rightarrow x^1)^2 \texttt{ in } ((f^3\; f^4)^5 \; (\texttt{fn } y \Rightarrow y^6)^7)^8)^9
$$

**Contexts:** $\Delta = \{\Lambda, 5, 8\}$ (initial $\Lambda$, two call sites 5 and 8)

**Context environments:**

- $ce_0 = []$ (initial)
- $ce_1 = ce_0[f \mapsto \Lambda]$ (for let body)
- $ce_2 = ce_0[x \mapsto 5]$ (for first call)
- $ce_3 = ce_0[x \mapsto 8]$ (for second call)

**1-CFA solution (selected):**

- $\hat{C}'(1, 5) = \{(\texttt{fn } x \Rightarrow x^1, ce_0)\}$ — $x^1$ analysed in context 5 (first call)
- $\hat{C}'(1, 8) = \{(\texttt{fn } y \Rightarrow y^6, ce_0)\}$ — $x^1$ analysed in context 8 (second call)
- $\hat{C}'(9, \Lambda) = \{(\texttt{fn } y \Rightarrow y^6, ce_0)\}$ — only $\texttt{fn } y \Rightarrow y^6$ is a result

**Precision gain:** The two calls are now distinguished: $x$ gets $\texttt{fn } y \Rightarrow y^6$ only from the second call, restoring precision.

<hr>


# Lecture 22 — Cartesian Product Algorithm (CPA)

## Motivation

The Cartesian Product Algorithm (CPA) is another approach to **context-sensitive** CFA. While k-CFA uses call strings as contexts, CPA uses **tuples of argument values** as contexts.

### Multi-Argument Functions

CPA assumes a syntax with multi-argument functions:

$$
\begin{aligned}
t &::= \dots \mid \texttt{fn } (x_1, \dots, x_m) \Rightarrow e_0 \\
e &::= t^\ell \mid e_0(e_1, \dots, e_m)^\ell \mid \dots
\end{aligned}
$$

Well-formedness condition: all function abstractions are closed ($FV = \emptyset$).

### Abstract Domains for CPA

$$
\begin{aligned}
\hat{v} &\in \widehat{\text{Val}} = \wp(\text{Term}) \\
\hat{\rho} &\in \widehat{\text{Cenv}} = (\text{Var} \times \Delta) \to \widehat{\text{Val}} \\
\hat{C} &\in \widehat{\text{Cache}} = (\text{Lab} \times \Delta) \to \widehat{\text{Val}} \\
\delta &\in \Delta = \text{Term}^m
\end{aligned}
$$

**Key difference:** A context $\delta$ is a **tuple of argument values** (sets of terms), not a call string.

### Rephrasing 0-CFA as a Special Case

In 0-CFA (no context), the clauses simplify:

#### [fn] (0-CFA, multi-arg)

$$
(\hat{C}, \hat{\rho}) \models (\texttt{fn } (x_1, \dots, x_m) \Rightarrow e_b)^\ell \iff \{\texttt{fn } (x_1, \dots, x_m) \Rightarrow e_b\} \subseteq \hat{C}(\ell)
$$

#### [app] (0-CFA, multi-arg)

$$
(\hat{C}, \hat{\rho}) \models (t_0^{\ell_0}(t_1^{\ell_1}, \dots, t_m^{\ell_m}))^\ell \iff
\begin{cases}
(\hat{C}, \hat{\rho}) \models t_0^{\ell_0} \\
(\hat{C}, \hat{\rho}) \models t_1^{\ell_1}, \dots, (\hat{C}, \hat{\rho}) \models t_m^{\ell_m} \\
\forall (\texttt{fn } (x_1, \dots, x_m) \Rightarrow t_b^{\ell_b}) \in \hat{C}(\ell_0): \\
\quad \hat{C}(\ell_1) \subseteq \hat{\rho}(x_1) \land \dots \land \hat{C}(\ell_m) \subseteq \hat{\rho}(x_m) \\
\quad \land\; (\hat{C}, \hat{\rho}) \models t_b^{\ell_b} \land \hat{C}(\ell_b) \subseteq \hat{C}(\ell)
\end{cases}
$$

### Adding Context to CPA

Now, the acceptability relation is parameterized by a context $\delta$:

$$
(\hat{C}, \hat{\rho}) \models_{\delta}^{\text{CPA}} e
$$

#### [var] with CPA Context

$$
(\hat{C}, \hat{\rho}) \models_{\delta}^{\text{CPA}} x^\ell \iff \hat{\rho}(x, \delta) \subseteq \hat{C}(\ell, \delta)
$$

#### [fn] with CPA Context

$$
(\hat{C}, \hat{\rho}) \models_{\delta}^{\text{CPA}} (\texttt{fn } (x_1, \dots, x_m) \Rightarrow e_b)^\ell \iff
\{\texttt{fn } (x_1, \dots, x_m) \Rightarrow e_b\} \subseteq \hat{C}(\ell, \delta)
$$

#### [app] with CPA Context

$$
(\hat{C}, \hat{\rho}) \models_{\delta}^{\text{CPA}} (t_0^{\ell_0}(t_1^{\ell_1}, \dots, t_m^{\ell_m}))^\ell \iff
\begin{cases}
(\hat{C}, \hat{\rho}) \models_{\delta}^{\text{CPA}} t_0^{\ell_0} \\
(\hat{C}, \hat{\rho}) \models_{\delta}^{\text{CPA}} t_1^{\ell_1}, \dots, (\hat{C}, \hat{\rho}) \models_{\delta}^{\text{CPA}} t_m^{\ell_m} \\
\forall (\texttt{fn } (x_1, \dots, x_m) \Rightarrow t_b^{\ell_b}) \in \hat{C}(\ell_0, \delta): \\
\quad \forall \delta_b \in \hat{C}(\ell_1, \delta) \times \dots \times \hat{C}(\ell_m, \delta): \\
\qquad (\texttt{fn } (x_1, \dots, x_m) \Rightarrow t_b^{\ell_b}) \in \hat{C}(\ell_0, \delta) \\
\qquad \Rightarrow \{\delta_b\} \subseteq \hat{\rho}(x_1) \times \dots \times \hat{\rho}(x_m) \\
\qquad \land\; (\hat{C}, \hat{\rho}) \models_{\delta_b}^{\text{CPA}} t_b^{\ell_b} \\
\qquad \land\; \hat{C}(\ell_b, \delta_b) \subseteq \hat{C}(\ell, \delta)
\end{cases}
$$

### Worked Example (CPA)

Suppose $\hat{C}(\ell_0) = \{\texttt{fn } (x_1, x_2) \Rightarrow e_b\}$, $\hat{C}(\ell_1, \delta) = \{a, b\}$, $\hat{C}(\ell_2, \delta) = \{c, d\}$.

The Cartesian product $\hat{C}(\ell_1, \delta) \times \hat{C}(\ell_2, \delta) = \{(a, c), (a, d), (b, c), (b, d)\}$. The body $e_b$ is analysed **separately** for each of the 4 argument tuples, with no merging across tuples.

### Complexity of CPA

- The cartesian product creates **exponential** context explosion in the worst case
- **Memoisation** is essential: bodies are analysed once per template and reused
- In practice, many argument combinations never occur, so the effective number is smaller

### CPA with Non-Closed Functions

If function abstractions may have free variables ($FV \neq \emptyset$), the analysis is extended with:

- $\delta \in \Delta = \text{Term}^m$
- $ce \in \text{CEnv} = \text{Var} \to \Delta$
- $\hat{v} \in \widehat{\text{Val}} = \wp(\text{Val} \times \text{Cenv})$ (closures with context environments)

The [app] clause then uses $ce'_0 = ce_0[x_1 \mapsto \delta_b\!\downarrow_1, \dots, x_n \mapsto \delta_b\!\downarrow_n]$ (projecting components of the argument tuple).

### Evolution of CFA for FUN

| Stage | Context | Precision | Complexity |
|:---|:---|:---:|:---:|
| 0-CFA | None (monovariant) | Low | $O(n^3)$ |
| Syntax-directed | None (body-once) | Medium | $O(n)$ |
| Constraint-based | None | Same as 0-CFA | $O(n^3)$–$O(n^5)$ |
| k-CFA | Call strings ($\text{Lab}^{\le k}$) | Medium–High | $O(n^{k+1})$ |
| CPA | Argument tuples ($\text{Term}^m$) | High | Exponential (with memoisation) |

All variants preserve soundness. The choice is a **trade-off** between precision and computational cost.

<hr>


# Lecture 23 — CFA for $\pi$-Calculus (0-CFA for Process Algebras)

## Motivation

- In CCS, communication is statically defined: channels cannot be transmitted or received
- The $\pi$-calculus extends CCS by allowing channels to be treated as ordinary values
- This enables **name mobility**: channels themselves can be communicated, making the communication structure dynamic
- CFA must predict which values may flow over which channels, even when channel names are passed at runtime

## $\pi$-Calculus Syntax

### Actions (Prefixes)

$$
\begin{aligned}
\pi ::=&\ \overline{u}\langle v\rangle &&\text{(send $v$ on $u$)} \\
      &\ |\ u(x) &&\text{(receive on $u$, store in $x$)} \\
      &\ |\ \tau &&\text{(internal action)}
\end{aligned}
$$

### Processes

$$
\begin{aligned}
P ::=&\ 0 &&\text{(inactive process)} \\
     &\ |\ \pi.P &&\text{(action prefix)} \\
     &\ |\ [x=y]P &&\text{(matching: if $x=y$ then $P$)} \\
     &\ |\ (\nu n)P &&\text{(restriction: $n$ is fresh/local)} \\
     &\ |\ \Sigma_{i\in I} \pi_i.P_i &&\text{(non-deterministic guarded choice)} \\
     &\ |\ P_1 \mid P_2 &&\text{(parallel composition)} \\
     &\ |\ !P &&\text{(replication: $P \mid P \mid P \mid \dots$)}
\end{aligned}
$$

### Reduction Semantics (Key Rule)

$$
[\text{Com}]\quad
(\overline{n}\langle m\rangle.P + P') \mid (n(x).Q + Q') \to P \mid Q[m/x]
$$

A process can also reduce under restriction, parallel composition, and structural congruence.

## Name Mobility Example

```
A = (ν ab)(ab̄⟨m⟩.A')           -- A sends message m on channel ab to B
B = ab(x).B'                     -- B receives on ab
S -- secure server that establishes channels

System: (ν as)(ν bs)((ν ab) A | B | S)
```

Channel `ab` is created by A, used for communication, and can be passed to other processes.

## Abstract Domains for CFA

### Domain Definitions

$$
\begin{aligned}
\text{Val} &= \wp(\text{Const}) \\
\rho &: \text{Var} \to \wp(\text{Const}) \\
\kappa &: \text{Var} \to \wp(\text{Const})
\end{aligned}
$$

- **$\rho$ (abstract environment)**: maps each variable to the set of constants it may be bound to
- **$\kappa$ (abstract channel environment)**: maps each channel constant to the set of constants that may be communicated over it
- Both domains form complete lattices under pointwise subset ordering
- Extension to constants: $\rho(n) = \{n\}$ for any constant $n$

### Detailed Domain Structure

The name space is partitioned into:

- **Constants** $c \in \text{Const}$: channels and values whose identity is statically known (including restricted names)
- **Variables** $x \in \text{Var}$: placeholders for values that will be received

The abstract domain is built on **canonical names**:

- $\lfloor n \rfloor$ denotes the equivalence class of name $n$ under $\alpha$-renaming
- $\lfloor x \rfloor = x$ for variables
- Substitution preserves equivalence classes

### Complete Lattice Structure

The product domain $(\wp(\text{Const}) \times \wp(\text{Const}))^{\text{Var} \times \text{Var}}$ forms a complete lattice with:

- **Order:** $(\rho_1, \kappa_1) \sqsubseteq (\rho_2, \kappa_2)$ iff $\forall x: \rho_1(x) \subseteq \rho_2(x)$ and $\forall n: \kappa_1(n) \subseteq \kappa_2(n)$
- **Least element:** $\bot = (\lambda x. \emptyset, \lambda n. \emptyset)$
- **Greatest element:** $\top = (\lambda x. \text{Const}, \lambda n. \text{Const})$
- **Join:** pointwise union: $(\rho_1 \sqcup \rho_2)(x) = \rho_1(x) \cup \rho_2(x)$
- **Meet:** pointwise intersection: $(\rho_1 \sqcap \rho_2)(x) = \rho_1(x) \cap \rho_2(x)$

### CFA Guess

A **guess** $(\rho, \kappa)$ is a proposed analysis result. It is **acceptable** if it safely over-approximates all runtime behaviour.

## Validation Clauses for Actions

### Output: $\overline{u}\langle v\rangle$

$$
[\text{out}]\quad
(\rho, \kappa) \models_A \overline{u}\langle v\rangle
\iff
\forall n \in \rho(u): \rho(v) \subseteq \kappa(n)
$$

**Meaning:** Whatever value $v$ may evaluate to must be recorded as possibly communicated on every channel that $u$ may denote.

**Three subcases:** (based on whether $u$ and $v$ are constants or variables)

1. **Both constants:** $\overline{n}\langle m\rangle$
   - $\rho(n) = \{n\}$, $\rho(m) = \{m\}$
   - Claus: $m \subseteq \kappa(n)$
   - **Meaning:** The specific constant $m$ is recorded as possibly sent on channel $n$.

2. **Constant channel, variable value:** $\overline{n}\langle v\rangle$
   - $\rho(n) = \{n\}$ (channel is known statically)
   - Claus: $\rho(v) \subseteq \kappa(n)$
   - **Meaning:** All values that $v$ may contain are recorded on channel $n$.

3. **Variable channel, constant value:** $\overline{u}\langle m\rangle$
   - $\rho(m) = \{m\}$
   - Claus: $\forall n \in \rho(u): m \subseteq \kappa(n)$
   - **Meaning:** The constant $m$ is recorded on all channels that $u$ may denote.

**Intuition:** The output clause ensures that whatever value is sent is included in the abstract channel environment for every possible target channel. This is a **sound over-approximation**: it includes all actual communications, though it may include spurious ones.

### Input: $u(x)$

$$
[\text{in}]\quad
(\rho, \kappa) \models_A u(x)
\iff
\forall n \in \rho(u): \kappa(n) \subseteq \rho(x)
$$

**Meaning:** Anything that may be communicated over any channel that $u$ denotes (the abstract communication $\kappa(n)$ for each possible $n$) may be received and bound to $x$.

**Subcases:**

1. **Constant channel:** $n(x)$
   - $\rho(n) = \{n\}$
   - Clause: $\kappa(n) \subseteq \rho(x)$
   - **Meaning:** All values recorded for channel $n$ flow to $x$.

2. **Variable channel:** $u(x)$
   - Clause: $\forall n \in \rho(u): \kappa(n) \subseteq \rho(x)$
   - **Meaning:** The union of all $\kappa(n)$ for every possible $n$ flows to $x$.

**Intuition:** The [in] clause ensures that the variable $x$ receives all values that may be communicated on any channel $u$ denotes. Because $u$ is a variable that may evaluate to multiple constants, we take the union over all of them — a sound over-approximation.

### Communication as Constraint Propagation

Together, [out] and [in] model communication:

$$
\overline{u}\langle v\rangle \quad\Longrightarrow\quad \rho(v) \subseteq \kappa(\rho(u))
$$

$$
u(x) \quad\Longrightarrow\quad \kappa(\rho(u)) \subseteq \rho(x)
$$

The channel environment $\kappa$ acts as an intermediary: outputs **push** values into $\kappa$, inputs **pull** values from $\kappa$. When an output and an input agree on a channel ($\rho(u)$ overlaps), data flows from sender to receiver.

### Internal Action: $\tau$

$$
[\text{tau}]\quad
(\rho, \kappa) \models_A \tau
$$

Always satisfied (no communication effect to track).

## Validation Clauses for Processes

### Inactive Process

$$
[\text{nil}]\quad
(\rho, \kappa) \models_P 0
$$

Always satisfied.

### Prefix

$$
[\text{pref}]\quad
(\rho, \kappa) \models_P \pi.P
\iff
(\rho, \kappa) \models_A \pi \ \land\ (\rho, \kappa) \models_P P
$$

### Parallel Composition

$$
[\text{par}]\quad
(\rho, \kappa) \models_P P_1 \mid P_2
\iff
(\rho, \kappa) \models_P P_1 \ \land\ (\rho, \kappa) \models_P P_2
$$

### Sum (Non-deterministic Choice)

$$
[\text{sum}]\quad
(\rho, \kappa) \models_P \Sigma_{i\in I} \pi_i.P_i
\iff
\forall i \in I:\ ((\rho, \kappa) \models_A \pi_i \ \land\ (\rho, \kappa) \models_P P_i)
$$

### Matching: $[x=y]P$

$$
[\text{match}]\quad
(\rho, \kappa) \models_P [x=y]P
\iff
(\rho, \kappa) \models_P P
$$

**Default (oblivious) analysis:** The match is over-approximated by assuming it could always succeed. This is sound because it may analyse code that is actually unreachable, but it never misses reachable code.

**Refined match clause** (more precise): $[\text{match}^*]$

$$
(\rho, \kappa) \models_P [x=y]P
\iff
\rho(x) \cap \rho(y) \neq \emptyset \ \Rightarrow\ (\rho, \kappa) \models_P P
$$

If the two variables' abstract values have **no common elements**, the match can never succeed, and the branch is **unreachable** — we can skip analysing $P$.

**Practical example:**
Process: $a(x).c(y).[x=y].P' \mid \overline{a}\langle d\rangle.Q' \mid \overline{a}\langle b\rangle.Q'' \mid \overline{c}\langle b\rangle.R'$

- $\rho(x) = \{b, d\}$, $\rho(y) = \{b\}$
- $\rho(x) \cap \rho(y) = \{b\} \neq \emptyset$ → match may succeed, analyse $P'$

If we had $\overline{c}\langle f\rangle.R'$ instead of $\overline{c}\langle b\rangle.R'$:

- $\rho(x) = \{b, d\}$, $\rho(y) = \{f\}$
- $\rho(x) \cap \rho(y) = \emptyset$ → match never succeeds, $P'$ is unreachable

### Restriction: $(\nu n)P$

$$
[\text{res}]\quad
(\rho, \kappa) \models_P (\nu n)P
\iff
(\rho, \kappa) \models_P P
$$

**Meaning:** The analysis is **oblivious to scoping** — names are treated as global constants. This is a deliberate over-approximation: it ignores the fact that a restricted name $n$ should not be known outside $P$, and may therefore predict communications that are impossible in the concrete semantics.

**Consequences:**

- Restricted names are included in $\rho$ and $\kappa$ like any other constant
- Spurious flows may result from ignoring scope boundaries
- To refine: one could use **freshness** information to remove impossible flows

**Example with scope extrusion:**
$$
(\nu a)(\overline{a}\langle b\rangle.0 \mid a(x).\overline{c}\langle x\rangle.0) \mid \overline{c}\langle d\rangle.0
$$

Although $a$ is restricted, the analysis treats it as a global constant. The abstract result $\kappa(c) \supseteq \{b, d\}$ soundly over-approximates the actual behaviour (where $b$ is indeed forwarded to $c$ via scope extrusion).

### Replication: $!P$

$$
[\text{rep}]\quad
(\rho, \kappa) \models_P !P
\iff
(\rho, \kappa) \models_P P
$$

**Meaning:** Replication $!P \equiv P \mid P \mid P \mid \dots$ represents an unbounded number of parallel copies of $P$. The analysis treats this as a **single** copy of $P$, which is sound because the same $(\rho, \kappa)$ over-approximates all copies.

**Correctness intuition:** Since all copies of $P$ share the same abstract values, any communication possible in the replicated process is also possible in the single-copy analysis. The over-approximation is that all copies can communicate with each other (while in reality there is only one copy being analysed).

## Summary of All Validation Clauses

| Construct | Clause |
|:---|:---|
| $[\text{nil}]$ | $(\rho, \kappa) \models_P 0$ always |
| $[\text{pref}]$ | $(\rho, \kappa) \models_P \pi.P \iff (\rho, \kappa) \models_A \pi \land (\rho, \kappa) \models_P P$ |
| $[\text{par}]$ | $(\rho, \kappa) \models_P P_1 \mid P_2 \iff (\rho, \kappa) \models_P P_1 \land (\rho, \kappa) \models_P P_2$ |
| $[\text{sum}]$ | $(\rho, \kappa) \models_P \Sigma_i \pi_i.P_i \iff \forall i: (\rho, \kappa) \models_A \pi_i \land (\rho, \kappa) \models_P P_i$ |
| $[\text{match}]$ | $(\rho, \kappa) \models_P [x=y]P \iff (\rho, \kappa) \models_P P$ |
| $[\text{res}]$ | $(\rho, \kappa) \models_P (\nu n)P \iff (\rho, \kappa) \models_P P$ |
| $[\text{rep}]$ | $(\rho, \kappa) \models_P !P \iff (\rho, \kappa) \models_P P$ |
| $[\text{out}]$ | $(\rho, \kappa) \models_A \overline{u}\langle v\rangle \iff \forall n\in\rho(u): \rho(v) \subseteq \kappa(n)$ |
| $[\text{in}]$ | $(\rho, \kappa) \models_A u(x) \iff \forall n\in\rho(u): \kappa(n) \subseteq \rho(x)$ |
| $[\text{tau}]$ | $(\rho, \kappa) \models_A \tau$ always |

<hr>


# Lecture 24 — CFA for $\pi$-Calculus: Examples, Theory, and Polyadic Extension

## Worked Example 1: Simple Communication

Process:
$$
(\overline{a}\langle b\rangle.P' + \overline{a}\langle d\rangle.P'') \mid a(w).\overline{c}\langle w\rangle.Q' \mid R
$$

### Concrete Behaviour

- Output on $a$: either $b$ or $d$ is sent
- Input on $a$: $w$ receives the transmitted value
- Forwarding: whatever $w$ received is output on $c$

### CFA Guess $(\rho, \kappa)$

| Variable | $\rho$ |
|:---|:---|
| $a$ | $\{a\}$ |
| $b$ | $\{b\}$ |
| $c$ | $\{c\}$ |
| $d$ | $\{d\}$ |
| $w$ | $\{b, d\}$ |

| Channel | $\kappa$ |
|:---|:---|
| $a$ | $\{b, d\}$ |
| $b$ | $\emptyset$ |
| $c$ | $\{b, d\}$ |
| $d$ | $\emptyset$ |

### Verification

1. $\overline{a}\langle b\rangle$: $\rho(b) = \{b\} \subseteq \kappa(a) = \{b,d\}$ ✓
2. $\overline{a}\langle d\rangle$: $\rho(d) = \{d\} \subseteq \kappa(a) = \{b,d\}$ ✓
3. $a(w)$: $\kappa(a) = \{b,d\} \subseteq \rho(w) = \{b,d\}$ ✓
4. $\overline{c}\langle w\rangle$: $\rho(w) = \{b,d\} \subseteq \kappa(c) = \{b,d\}$ ✓

Analysis predicts both possible executions (sound over-approximation).

## Worked Example 2: Name Mobility

Process:
$$
(\nu a)(\overline{a}\langle b\rangle.0 \mid a(x).\overline{c}\langle x\rangle.0) \mid \overline{c}\langle d\rangle.0
$$

### Analysis

- Channel $a$ is restricted: $(\nu a)$ creates a fresh name
- Output on $a$: $b$ is communicated over $a$
- Input on $a$: $x$ receives $b$, then forwards it on $c$
- Parallel output on $c$: $d$ is also sent on $c$

### Result
$$
\kappa(c) \supseteq \{b, d\}, \qquad \rho(x) \supseteq \{b\}
$$

## The Match Clause in Practice

Consider:
$$
a(x).c(y).[x=y].P' \mid \overline{a}\langle d\rangle.Q' \mid \overline{a}\langle b\rangle.Q'' \mid \overline{c}\langle b\rangle.R'
$$

- $\rho(x) = \{b, d\}$, $\rho(y) = \{b\}$
- $\rho(x) \cap \rho(y) = \{b\} \neq \emptyset$ → the match can succeed, analyse $P'$

Now if $\overline{c}\langle f\rangle.R'$ instead of $\overline{c}\langle b\rangle.R'$:

- $\rho(x) = \{b, d\}$, $\rho(y) = \{f\}$
- $\rho(x) \cap \rho(y) = \emptyset$ → match can never succeed, $P'$ is unreachable under refined analysis

## Theoretical Properties

### Subject Reduction (Semantic Correctness)

If $(\rho, \kappa) \models_P P$ and $P \to Q$ (a reduction step), then $(\rho, \kappa) \models_P Q$.

The analysis result is preserved under computation — it is a **sound over-approximation** of all reachable states.

### Preservation under $\alpha$-renaming

Use **canonical names** (equivalence classes):

- $\lfloor n \rfloor$ is the equivalence class of $n$
- $\lfloor x \rfloor = x$ for variables
- Names may only be substituted within the same equivalence class

**Lemma**: If $P \equiv_\alpha Q$ then $(\rho, \kappa) \models_P \lfloor P \rfloor \iff (\rho, \kappa) \models_P \lfloor Q \rfloor$.

### Substitution Lemma

If $(\rho, \kappa) \models_P \lfloor P \rfloor$ then $(\rho, \kappa) \models_P \lfloor P[m/x] \rfloor$, provided $\lfloor m \rfloor \subseteq \rho(x)$.

### Existence and Moore Family

The set $\{ (\rho, \kappa) \mid (\rho, \kappa) \models_P P \}$ is a **Moore family** (closed under greatest lower bounds). Therefore:

- Every process $P$ has at least one analysis (the trivial one with everything flowing everywhere)
- There exists a **least** (most precise) solution: the intersection of all acceptable pairs

### Implementation

- The validation clauses generate a set of logical constraints (set inclusions)
- Constraints can be solved by a specialised constraint solver or by translation to first-order logic
- Complexity is low polynomial

## Nature of Imprecision in 0-CFA for $\pi$-calculus

The analysis is **context-insensitive** (0-CFA), leading to imprecision:

$$
\begin{aligned}
P_1 &\triangleq a(x) \mid \overline{a}\langle b\rangle \\
P_2 &\triangleq a(x) + \overline{a}\langle b\rangle \\
P_3 &\triangleq a(x).\overline{a}\langle b\rangle
\end{aligned}
$$

In $P_1$, $x$ can be bound to $b$. In $P_2$ and $P_3$, it cannot (no communication possible). However, the 0-CFA estimate gives $\rho(x) \supseteq \{b\}$ in **all three cases** — a safe over-approximation that does not distinguish between reachable and unreachable communications.

## Polyadic $\pi$-Calculus Extension

### Syntax

Allow tuples of values:
$$
\begin{aligned}
\pi ::=&\ \overline{u}\langle \vec{v}\rangle \\
       &\ |\ u(\vec{x}) \\
       &\ |\ \tau
\end{aligned}
$$

### Reduction with Arity

$$
[\text{Com}]\quad
(\overline{n}\langle \vec{m}\rangle.P + P') \mid (n(\vec{x}).Q + Q') \to P \mid Q[\vec{m}/\vec{x}]
$$
provided $|\vec{m}| = |\vec{x}|$ (arity must match).

### Extended Abstract Domains

$$
\begin{aligned}
\text{Val} &= \wp(\text{Const}) \\
\rho &: \text{Var} \to \wp(\text{Const}) \\
\kappa &: \text{Var} \to \wp(\text{Const}^*) \\
\psi &: \wp(\text{Const})
\end{aligned}
$$

- $\kappa$ now maps to **sequences of constants** (tuples)
- $\psi$ records the set of channels where an **arity mismatch** may occur

### Extended Validation (sketch)

$$
(\rho, \kappa) \models_A \overline{u}\langle \vec{v}\rangle \iff \forall n \in \rho(u): \rho(v_1)\times\dots\times\rho(v_k) \subseteq \kappa(n)
$$

$$
(\rho, \kappa) \models_A u(\vec{x}) \iff \forall n \in \rho(u): \kappa(n) \subseteq \rho(x_1)\times\dots\times\rho(x_k)
$$

Arity mismatches are recorded in $\psi$ for error detection.

<hr>


# Complete Formula Handbook

## F-01: Collecting Semantics
$$
\llbracket c\rrbracket P = \bigcup_{\sigma \in P} \llbracket c\rrbracket\sigma
$$
**Meaning:** The collecting semantics maps a set of input states to the union of all reachable output states.

## F-02: Weakest Liberal Precondition
$$
\text{wlp}(c, Q) = \{\sigma \mid \llbracket c\rrbracket\{\sigma\} \subseteq Q\}
$$

## F-03: Weakest Possible Precondition
$$
\text{wpp}(c, Q) = \{\sigma \mid \llbracket c\rrbracket\sigma \cap Q \neq \emptyset\}
$$

## F-04: Hoare Triple Validity
$$
\{P\}\ c\ \{Q\} \iff \llbracket c\rrbracket P \subseteq Q
$$

## F-05: Incorrectness Triple Validity
$$
[P]\ c\ [Q] \iff \llbracket c\rrbracket P \supseteq Q
$$

## F-06: Galois Connection
$$
\alpha(c) \sqsubseteq_A a \iff c \sqsubseteq_C \gamma(a)
$$

## F-07: Soundness of Abstract Semantics
$$
\alpha \circ \llbracket c\rrbracket \sqsubseteq \llbracket c\rrbracket^\# \circ \alpha
$$

## F-08: Best Abstract Correct Approximation
$$
\llbracket c\rrbracket^\#_A = \alpha \circ \llbracket c\rrbracket \circ \gamma
$$

## F-09: Completeness Equation
$$
\alpha \circ \llbracket c\rrbracket = \alpha \circ \llbracket c\rrbracket \circ \gamma \circ \alpha
$$

<hr>


# Exam Preparation Guide

## Recurring Exercise Patterns

1. **Prove a Hoare triple** using HL inference rules — find the loop invariant
2. **Prove an incorrectness triple** using IL rules — find the right under-approximation
3. **Galois connection** — define $\alpha$ and $\gamma$ for a given abstraction
4. **Abstract semantics** — define $\llbracket c\rrbracket^\#$ for a given abstract domain
5. **Fixpoint computation** — compute the least fixpoint for a loop in an abstract domain
6. **CFA constraints** — generate constraints for a functional program

## Common Proof Strategies

- **Induction on derivation trees** for proving soundness
- **Fixpoint induction** (Kleene) for loop semantics
- **Structural induction** for semantic properties
- **Coinduction** for non-termination/infinite behaviors

## Common Lattice Constructions

1. **Product lattice:** $L_1 \times L_2$ with pointwise order
2. **Flat lattice:** $L^\#$ with $\bot < a < \top$
3. **Interval lattice:** $\{[l, u] \mid l \le u, l \in \mathbb{Z} \cup \{-\infty\}, u \in \mathbb{Z} \cup \{+\infty\}\}$
4. **Sign lattice:** $\{\emptyset, <0, =0, >0, \le 0, \ge 0, \mathbb{Z}\}$ ordered by subset inclusion

## Frequently Tested Concepts

- $\text{wlp}$ vs $\text{wpp}$ and their properties
- HL vs IL duality
- Soundness and completeness
- Galois connections and insertions
- Abstract domain design
- Widening for fixpoint termination
- 0-CFA for functional programs
- Flow logic formulation of CFA

<hr>


# Final Cheat Sheet (Expanded)

## 1. Denotational Semantics

| Concept | Definition |
|:---|:---|
| State | $\Sigma \triangleq \{\sigma: X \to \mathbb{Z}\}$ |
| Collecting semantics | $\llbracket c\rrbracket : \wp(\Sigma) \to \wp(\Sigma)$, $\llbracket c\rrbracket P = \bigcup_{\sigma\in P} \llbracket c\rrbracket\sigma$ |
| Skip | $\llbracket \texttt{skip} \rrbracket P = P$ |
| Assignment | $\llbracket x := a\rrbracket P = \{\sigma[n/x] \mid \sigma\in P,\ n = \llbracket a\rrbracket\sigma\}$ |
| Sequence | $\llbracket c_1;c_2\rrbracket P = \llbracket c_2\rrbracket(\llbracket c_1\rrbracket P)$ |
| Choice | $\llbracket c_1 + c_2\rrbracket P = \llbracket c_1\rrbracket P \cup \llbracket c_2\rrbracket P$ |
| Iteration | $\llbracket c^\star\rrbracket P = \bigcup_{k=0}^\infty \llbracket c\rrbracket^k P$ |
| Guard | $\llbracket b?\rrbracket P = P \land b$ |
| Encoding if | $\texttt{if } b \texttt{ then } c_1 \texttt{ else } c_2 \equiv (b?;c_1) + (\neg b?;c_2)$ |
| Encoding while | $\texttt{while } b \texttt{ do } c \equiv (b?;c)^\star;\neg b?$ |
| wlp | $\operatorname{wlp}(c,Q) = \{\sigma \mid \llbracket c\rrbracket\{\sigma\} \subseteq Q\}$ |
| wpp | $\operatorname{wpp}(c,Q) = \{\sigma \mid \llbracket c\rrbracket\sigma \cap Q \neq \emptyset\}$ |

## 2. Program Logics — The Four Quadrants

| Logic | Triple | Direction | Approximation | Validity Condition |
|:---|:---:|:---:|:---:|:---|
| Hoare Logic (HL) | $\{P\}\ c\ \{Q\}$ | Forward | Over (⊆) | $\llbracket c\rrbracket P \subseteq Q$ |
| Incorrectness Logic (IL) | $[P]\ c\ [Q]$ | Forward | Under (⊇) | $\llbracket c\rrbracket P \supseteq Q$ |
| Necessary Condition (NC) | $\langle P\rangle\ c\ \langle Q\rangle$ | Backward | Under | $P \subseteq \llbracket c\rrbracket^{\text{op}} Q$ |
| Sufficient Incorrectness (SIL) | $(P)\ c\ (Q)$ | Backward | Over | $P \supseteq \llbracket c\rrbracket^{\text{op}} Q$ |

### First-order Characterizations

- HL: $\forall\sigma\in P.\ \forall\delta\in\llbracket c\rrbracket\sigma.\ \delta\in Q$
- IL: $\forall\delta\in Q.\ \exists\sigma\in P.\ \delta\in\llbracket c\rrbracket\sigma$

## 3. Hoare Logic Rules (Partial Correctness)

| Rule | Formula |
|:---|:---|
| Skip | $\overline{\{P\}\ \texttt{skip}\ \{P\}}$ |
| Assignment (Hoare) | $\overline{\{Q[a/x]\}\ x := a\ \{Q\}}$ |
| Assignment (Floyd) | $\overline{\{P\}\ x := a\ \{\exists x'. P[x'/x] \land x = a[x'/x]\}}$ |
| Sequence | $\dfrac{\{P\}\ c_1\ \{R\}\quad \{R\}\ c_2\ \{Q\}}{\{P\}\ c_1;c_2\ \{Q\}}$ |
| Conditional | $\dfrac{\{P\land b\}\ c_1\ \{Q\}\quad \{P\land\neg b\}\ c_2\ \{Q\}}{\{P\}\ \texttt{if } b \texttt{ then } c_1 \texttt{ else } c_2\ \{Q\}}$ |
| While | $\dfrac{\{P\land b\}\ c\ \{P\}}{\{P\}\ \texttt{while } b \texttt{ do } c\ \{P\land\neg b\}}$ |
| Consequence | $\dfrac{P\Rightarrow P'\quad \{P'\}\ c\ \{Q'\}\quad Q'\Rightarrow Q}{\{P\}\ c\ \{Q\}}$ |
| While (total) | $\dfrac{\{P\land b\}\ c\ \{P\}\quad \{P\land b\land t=z\}\ c\ \{t<z\}\quad P\Rightarrow t\ge0}{\{P\}\ \texttt{while } b \texttt{ do } c\ \{P\land\neg b\}}$ |

## 4. Incorrectness Logic Rules

| Rule | Formula |
|:---|:---|
| Skip | $\overline{[P]\ \texttt{skip}\ [P]}$ |
| Assignment (Floyd) | $\overline{[P]\ x := a\ [\exists x'. P[x'/x] \land x = a[x'/x]]}$ |
| Assume | $\overline{[P]\ b?\ [P \land b]}$ |
| Error | $\overline{[P]\ \texttt{error}()\ [\texttt{false}]}$ |
| Nondet | $\overline{[P]\ x := \texttt{nondet}()\ [\exists x. P]}$ |
| Sequence | $\dfrac{[P]\ c_1\ [R]\quad [R]\ c_2\ [Q]}{[P]\ c_1;c_2\ [Q]}$ |
| Choice | $\dfrac{[P]\ c_1\ [Q_1]\quad [P]\ c_2\ [Q_2]}{[P]\ c_1 + c_2\ [Q_1 \lor Q_2]}$ |
| Consequence (IL) | $\dfrac{P'\Rightarrow P\quad [P']\ c\ [Q']\quad Q\Rightarrow Q'}{[P]\ c\ [Q]}$ |
| Disjunction | $\dfrac{[P_1]\ c\ [Q_1]\quad [P_2]\ c\ [Q_2]}{[P_1\lor P_2]\ c\ [Q_1\lor Q_2]}$ |
| Frame (IL) | $\dfrac{[P]\ c\ [Q]}{[P\land R]\ c\ [Q\land R]}$ (modifies $\cap$ FV(R) = ∅) |
| Iteration | $\dfrac{\forall n\ge0.\ [P_n]\ c\ [P_{n+1}]}{[P_0]\ c^\star\ [\exists k.\ P_k]}$ |

## 5. Separation Logic

### Heap Model

- State: $(s, h)$ where $s: \text{Var} \to \text{Val}$, $h: \text{Loc} \rightharpoonup \text{Val}$
- $h_1 \cdot h_2$: union of disjoint heaps (domains are disjoint)
- $s, h \models \texttt{emp}$ iff $\text{dom}(h) = \emptyset$
- $s, h \models x \mapsto v$ iff $h = \{s(x) \mapsto s(v)\}$
- $s, h \models P \star Q$ iff $\exists h_1, h_2: h = h_1 \cdot h_2$, $s,h_1 \models P$, $s,h_2 \models Q$
- $s, h \models P \mathbin{-\!*} Q$ iff $\forall h' \bot h:\ s,h' \models P \Rightarrow s, h\cdot h' \models Q$

### Key SL Rules
| Rule | Formula |
|:---|:---|
| Frame | $\dfrac{\{P\}\ c\ \{Q\}}{\{P \star R\}\ c\ \{Q \star R\}}$ (no mod. var in $R$) |
| Alloc | $\{\texttt{emp}\}\ x := \texttt{alloc}()\ \{x \mapsto \_\}$ |
| Read | $\{x \mapsto v\}\ y := [x]\ \{x \mapsto v \land y = v\}$ |
| Write | $\{x \mapsto \_\}\ [x] := y\ \{x \mapsto y\}$ |
| Free | $\{x \mapsto \_\}\ \texttt{free}(x)\ \{\texttt{emp}\}$ |

### List Predicates

- $ls(a_1, a_2) \triangleq (a_1 = a_2 \land \texttt{emp}) \lor (a_1 \neq a_2 \land \exists \ell.\ a_1 \mapsto \ell \star ls(\ell, a_2))$
- $\texttt{list}(a) \triangleq ls(a, \texttt{nil})$

### ISL Heap Rules
| Rule | Formula |
|:---|:---|
| Read | $[v \mapsto w \star P]\ x := [v]\ [v \mapsto w \star P \land x = w]$ |
| Write | $[v \mapsto \_ \star P]\ [v] := y\ [v \mapsto y \star P]$ |
| Alloc | $[\texttt{emp}]\ x := \texttt{alloc}()\ [x \mapsto \_]$ |
| Free | $[v \mapsto \_]\ \texttt{free}(v)\ [\texttt{emp}]$ |

## 6. Abstract Interpretation

### Galois Connections
| Property | Formula |
|:---|:---|
| GC definition | $\alpha(c) \sqsubseteq_A a \iff c \subseteq_C \gamma(a)$ |
| $\alpha$ preserves | Least upper bounds ($\sqcup$) |
| $\gamma$ preserves | Greatest lower bounds ($\sqcap$) |
| GI condition | $\alpha$ surjective, $\gamma$ injective, $\alpha \circ \gamma = \text{id}$ |
| Closure operator | $\gamma \circ \alpha$ is extensive, monotone, idempotent |
| Expressible elements | $c = \gamma(\alpha(c))$ |

### Abstract Semantics Soundness
| Concept | Formula |
|:---|:---|
| Soundness | $\alpha(\llbracket c\rrbracket P) \sqsubseteq \llbracket c\rrbracket^\#(\alpha(P))$ |
| Equivalent | $\llbracket c\rrbracket\gamma(a) \subseteq \gamma(\llbracket c\rrbracket^\# a)$ |
| BCA | $\llbracket c\rrbracket^\#_A = \alpha \circ \llbracket c\rrbracket \circ \gamma$ |
| Completeness | $\alpha \circ \llbracket c\rrbracket = \llbracket c\rrbracket^\# \circ \alpha$ |

### Local Completeness Logic (LCL)
| Concept | Formula |
|:---|:---|
| Closure $A$ | $A = \gamma \circ \alpha$ |
| Global completeness | $\forall P.\ A(\llbracket c\rrbracket P) = \llbracket c\rrbracket^\# A(P)$ |
| Local completeness | $\mathbb{C}_P(e): A(\llbracket e\rrbracket P) = A(\llbracket e\rrbracket A(P))$ |
| LCL triple | $\vdash_A [P]\ c\ [Q]$ with $Q \subseteq \llbracket c\rrbracket P \subseteq A(Q)$ |
| Verification theorem | LCL derivation + local completeness $\Rightarrow$ global soundness |

### Abstract Domains
| Domain | Elements | ACC? | Needs Widening? |
|:---|:---|:---:|:---:|
| Sign | $\{\bot, -, 0, +, \top\}$ | Yes | No |
| Constant | $\{\bot, c, \top\}$ for $c\in\mathbb{Z}$ | No | Yes |
| Interval | $\{[l,h] \mid l\le h\} \cup \{\bot\}$ | No | Yes ($\nabla$) |
| Congruence | $a\mathbb{Z}+b$ | Yes | No |
| Octagon | $\pm x \pm y \le c$ | No | Yes |
| Polyhedron | $\sum a_i x_i \le d$ | No | Yes |

### Interval Operations

- $[l_1,h_1] + [l_2,h_2] = [l_1+l_2, h_1+h_2]$
- $[l_1,h_1] \times [l_2,h_2] = [\min(l_1l_2,l_1h_2,h_1l_2,h_1h_2),\ \max(\dots)]$
- $[a,b] \nabla [c,d] = [\text{if } c<a \text{ then } -\infty \text{ else } a,\ \text{if } d>b \text{ then } +\infty \text{ else } b]$
- $[a,b] \Delta [c,d] = [\text{if } a=-\infty \text{ then } c \text{ else } a,\ \text{if } b=+\infty \text{ then } d \text{ else } b]$

## 7. Control Flow Analysis (0-CFA for FUN)

### Abstract Domains

- $\hat{C}: \text{Lab} \to \wp(\text{Term})$ — cache: which function abstractions reach each program point
- $\hat{\rho}: \text{Var} \to \wp(\text{Term})$ — environment: which abstractions each variable may bind

### Acceptability Clauses $(\hat{C}, \hat{\rho}) \models e$

| Expression | Clause |
|:---|:---|
| $c^\ell$ | $\emptyset \subseteq \hat{C}(\ell)$ |
| $x^\ell$ | $\hat{\rho}(x) \subseteq \hat{C}(\ell)$ |
| $(\texttt{fn } x \Rightarrow t)^\ell$ | $\{\texttt{fn } x \Rightarrow t\} \subseteq \hat{C}(\ell)$ |
| $(t_1\ t_2)^\ell$ | $(\hat{C},\hat{\rho}) \models t_1 \land (\hat{C},\hat{\rho}) \models t_2 \land \forall \texttt{fn } x \Rightarrow t_0 \in \hat{C}(\ell_1):$ $\hat{C}(\ell_2) \subseteq \hat{\rho}(x) \land \hat{C}(\ell_0) \subseteq \hat{C}(\ell)$ |
| $(\texttt{let } x = t_1 \texttt{ in } t_2)^\ell$ | $(\hat{C},\hat{\rho}) \models t_1 \land \hat{\rho}(x) = \hat{C}(\ell_1) \land (\hat{C},\hat{\rho}) \models t_2$ |

### Constraint Generation $C^*[\![e]\!]$

| Expression | Constraints |
|:---|:---|
| $c^\ell$ | $\emptyset$ |
| $x^\ell$ | $r(x) \subseteq C(\ell)$ |
| $(\texttt{fn } x \Rightarrow t)^\ell$ | $\{\texttt{fn } x \Rightarrow t\} \subseteq C(\ell) \cup C^*[\![t]\!]$ |
| $(t_1\ t_2)^\ell$ | $C^*[\![t_1]\!] \cup C^*[\![t_2]\!] \cup \{\{\texttt{fn } x \Rightarrow t_0\} \subseteq C(\ell_1) \Rightarrow C(\ell_2) \subseteq r(x)\} \cup \{\{\texttt{fn } x \Rightarrow t_0\} \subseteq C(\ell_1) \Rightarrow C(\ell_0) \subseteq C(\ell)\}$ |

### Key Properties

- **Order**: $(\hat{C}_1, \hat{\rho}_1) \sqsubseteq (\hat{C}_2, \hat{\rho}_2)$ iff $\forall\ell.\ \hat{C}_1(\ell) \subseteq \hat{C}_2(\ell)$ and $\forall x.\ \hat{\rho}_1(x) \subseteq \hat{\rho}_2(x)$
- **Moore family**: the set of acceptable analyses is closed under $\sqcap$ → least (most precise) solution exists
- **0-CFA**: monovariant (one value per program point)
- **k-CFA**: context-sensitive with call strings of length $k$

### CPA (Cartesian Product Algorithm)

- Contexts: $\Delta = \text{Term}^m$ (tuples of arguments)
- $\hat{\rho}: (\text{Var} \times \Delta) \to \wp(\text{Term})$
- $\hat{C}: (\text{Lab} \times \Delta) \to \wp(\text{Term})$

## 8. 0-CFA for $\pi$-Calculus

### Abstract Domains

- $\rho: \text{Var} \to \wp(\text{Const})$ — which constants each variable may bind
- $\kappa: \text{Var} \to \wp(\text{Const})$ — which constants may be communicated over each channel
- Extension: $\rho(n) = \{n\}$ for constants $n$

### Validation Clauses

| Construct | Clause |
|:---|:---|
| $[\text{out}]$ $\overline{u}\langle v\rangle$ | $\forall n \in \rho(u): \rho(v) \subseteq \kappa(n)$ |
| $[\text{in}]$ $u(x)$ | $\forall n \in \rho(u): \kappa(n) \subseteq \rho(x)$ |
| $[\text{tau}]$ $\tau$ | Always true |
| $[\text{pref}]$ $\pi.P$ | $(\rho,\kappa)\models_A \pi \land (\rho,\kappa)\models_P P$ |
| $[\text{par}]$ $P_1 \mid P_2$ | $(\rho,\kappa)\models_P P_1 \land (\rho,\kappa)\models_P P_2$ |
| $[\text{sum}]$ $\Sigma_i \pi_i.P_i$ | $\forall i: (\rho,\kappa)\models_A \pi_i \land (\rho,\kappa)\models_P P_i$ |
| $[\text{match}]$ $[x=y]P$ | $(\rho,\kappa)\models_P P$ (or $\rho(x)\cap\rho(y)\neq\emptyset \Rightarrow (\rho,\kappa)\models_P P$) |
| $[\text{res}]$ $(\nu n)P$ | $(\rho,\kappa)\models_P P$ |
| $[\text{rep}]$ $!P$ | $(\rho,\kappa)\models_P P$ |

### Theoretical Properties

- **Subject reduction**: $P \to Q$ and $(\rho,\kappa)\models_P P \Rightarrow (\rho,\kappa)\models_P Q$
- **Substitution lemma**: $\lfloor m\rfloor \subseteq \rho(x) \Rightarrow (\rho,\kappa)\models_P \lfloor P[m/x]\rfloor$
- **Moore family**: $\{(\rho,\kappa) \mid (\rho,\kappa)\models_P P\}$ is closed under $\sqcap$ → least solution exists

## 9. Common Exam Tricks

| Pattern | Technique |
|:---|:---|
| Prove HL triple | Use consequence to weaken postcondition / strengthen precondition |
| Prove IL triple | Show every poststate has a prestate witness |
| Find loop invariant | Look for preserved relationship (e.g., $x = n!$ in factorial) |
| Find loop variant | Decreasing natural-number expression (e.g., $n-i$ in factorial) |
| Construct Galois connection | Define $\gamma$ first (most natural), then $\alpha$ as best approximation |
| Determine completeness | Check if $\alpha \circ F = \alpha \circ F \circ \gamma \circ \alpha$ holds for the given $P$ |
| Generate CFA constraints | Follow syntax-directed rules, track labels carefully |
| Predict $\pi$-calculus communications | Output: $\rho(v) \subseteq \kappa(u)$; Input: $\kappa(u) \subseteq \rho(x)$ |
| Check Moore family | Verify closure under $\sqcap$ (intersection of any set of solutions is a solution) |
| Design widening | Force unstable bounds to $\pm\infty$ |

## 10. Key Notation Summary

| Symbol | Meaning |
|:---|:---|
| $\llbracket c\rrbracket$ | Denotational semantics of command $c$ |
| $\{P\}\ c\ \{Q\}$ | Hoare triple (over, forward) |
| $[P]\ c\ [Q]$ | IL triple (under, forward) |
| $\langle P\rangle\ c\ \langle Q\rangle$ | NC triple (under, backward) |
| $(P)\ c\ (Q)$ | SIL triple (over, backward) |
| $\alpha, \gamma$ | Abstraction, concretization |
| $\sqsubseteq, \sqcup, \sqcap$ | Lattice ordering, join, meet |
| $\bot, \top$ | Bottom, top of lattice |
| $\nabla, \Delta$ | Widening, narrowing |
| $\hat{C}, \hat{\rho}$ | CFA cache, CFA environment |
| $\rho, \kappa$ | $\pi$-calculus abstract env, channel env |
| $C(\ell), r(x)$ | CFA constraint variables |
| $A = \gamma\circ\alpha$ | Closure operator |
| $(\hat{C},\hat{\rho}) \models e$ | CFA acceptability |
| $(\rho,\kappa) \models_P P$ | $\pi$-calculus CFA acceptability |

<hr>


# Algorithm Extraction

## A-01: Kleene Fixpoint Iteration

### Purpose
Compute the least fixpoint of a monotone function $F$ on a complete lattice, used to compute loop semantics in both concrete and abstract settings.

### Input

- A monotone function $F: L \to L$ on a complete lattice $(L, \sqsubseteq, \bot, \top, \sqcup, \sqcap)$

### Output

- $\operatorname{lfp}(F)$, the least fixpoint of $F$

### Pseudocode
```
x ← ⊥
repeat
  x ← F(x)
until x is a fixpoint (F(x) = x)
return x
```

### Complexity

- Termination depends on the height of the lattice $L$
- If $L$ has finite height $h$, at most $h$ iterations
- If $L$ has infinite height (e.g., intervals), may not terminate without widening

### Correctness Intuition
Kleene's fixpoint theorem: for a continuous function on a CPO, the least fixpoint equals $\bigsqcup_{n \ge 0} F^n(\bot)$.

### Common Mistakes

- Assuming termination on infinite-height lattices without widening
- Confusing least fixpoint with greatest fixpoint
- Forgetting monotonicity requirement

### Exam Relevance
Fundamental for understanding loop analysis in abstract interpretation. Used in Lectures 12, 15.

<hr>


## A-02: Abstract Fixpoint with Widening

### Purpose
Compute a sound over-approximation of the least fixpoint when the abstract lattice has infinite height (e.g., intervals).

### Input

- A monotone function $F^\#: A \to A$ on an abstract domain $A$
- A widening operator $\nabla: A \times A \to A$

### Output

- A post-fixpoint $x$ such that $F^\#(x) \sqsubseteq x$ (sound approximation of $\operatorname{lfp}(F)$)

### Pseudocode
```
x ← ⊥
repeat
  x ← x ∇ F^#(x)
until F^#(x) ⊑ x
return x
```

### Complexity
Widening guarantees termination in finite time regardless of lattice height.

### Correctness Intuition
If $x$ is a post-fixpoint ($F^\#(x) \sqsubseteq x$), then $\operatorname{lfp}(F) \sqsubseteq \gamma(x)$ by soundness.

### Common Mistakes

- Widening too early, causing precision loss
- Using $\sqcup$ instead of $\nabla$ (no termination guarantee)
- Forgetting that widening must be used at loop heads only

### Exam Relevance
Central for interval analysis. Frequently examined in combination with narrowing for precision recovery.

<hr>


## A-03: Worklist Algorithm for Abstract Interpretation

### Purpose
Efficiently compute the least fixpoint of a system of abstract semantic equations over a control flow graph.

### Input

- CFG with program points $\ell_1, \dots, \ell_n$
- Initial abstract state $a_0$ at entry point
- Abstract transfer functions $F^\#_\ell$ for each edge

### Output

- Abstract invariant $I(\ell)$ for each program point $\ell$

### Pseudocode
```
for each ℓ: I(ℓ) ← ⊥
I(ℓ_entry) ← a_0
W ← {ℓ_entry}
while W ≠ ∅:
  ℓ ← remove from W
  for each successor ℓ' of ℓ:
    new ← I(ℓ) ⊔ F^#_{ℓ→ℓ'}(I(ℓ))
    if new ≠ I(ℓ'):
      I(ℓ') ← new
      W ← W ∪ {ℓ'}
return I
```

### Complexity

- Each edge processed at most $h$ times where $h$ is lattice height
- With widening: edges processed at most once per widening point

### Correctness Intuition
Join with existing values ensures monotonic increase; termination by lattice ACC or widening.

### Common Mistakes

- Forgetting to join new and old values (instead of just assigning)
- Missing widening at loop heads
- Lattice height assumed finite when it's not

### Exam Relevance
Standard algorithm for implementing static analyses. Likely asked in exam.

<hr>


## A-04: 0-CFA Constraint Generation

### Purpose
Generate a system of constraints whose least solution gives the 0-CFA of a functional program (monovariant CFA).

### Input

- A labeled expression $e$ with labels $\ell \in \text{Lab}$
- Abstraction: set of function abstractions $\text{Term}$

### Output

- A set $C^*[\![e]\!]$ of constraints and conditional constraints over variables $C(\ell)$ and $r(x)$
- Least solution $(\hat{C}, \hat{\rho})$ is the most precise 0-CFA

### Constraint Generation Rules

**Constants:** $C^*[\![c^\ell]\!] = \emptyset$

**Variables:** $C^*[\![x^\ell]\!] = \{ r(x) \subseteq C(\ell) \}$

**Functions:** $C^*[\![(\texttt{fn } x \Rightarrow e_0)^\ell]\!] = \{ \{\texttt{fn } x \Rightarrow e_0\} \subseteq C(\ell) \} \cup C^*[\![e_0]\!]$

**Application:** $C^*[\![e_1^{\ell_1} e_2^{\ell_2})^\ell]\!] = C^*[\![e_1]\!] \cup C^*[\![e_2]\!] \cup$
$\qquad \{ \{\texttt{fn } x \Rightarrow e_0\} \subseteq C(\ell_1) \Rightarrow C(\ell_2) \subseteq r(x) \mid \forall \texttt{fn } x \Rightarrow e_0 \in \text{Term} \}$
$\qquad \cup \{ \{\texttt{fn } x \Rightarrow e_0\} \subseteq C(\ell_1) \Rightarrow C(\ell_0) \subseteq C(\ell) \mid \forall \texttt{fn } x \Rightarrow e_0 \in \text{Term} \}$

**Let:** $C^*[\![(\texttt{let } x = t_1^{\ell_1} \texttt{ in } t_2^{\ell_2})^\ell]\!] = C^*[\![t_1]\!] \cup C^*[\![t_2]\!] \cup \{ C(\ell_1) \subseteq r(x),\; C(\ell_2) \subseteq C(\ell) \}$

### Complexity

- $O(|e|^2)$ constraints generated
- Least solution computable via fixpoint in $O(|e|^3)$

### Correctness Intuition
Constraints encode the acceptability relation $(\hat{C}, \hat{\rho}) \models e$; least solution is most precise analysis.

### Common Mistakes

- Forgetting conditional constraints for applications
- Confusing $\subseteq$ direction
- Not handling all function abstractions in $\text{Term}$

### Exam Relevance
High — 0-CFA is a staple exam topic. Exercises require constraint generation and solution.

<hr>


## A-05: Interval Widening

### Purpose
Ensure termination of fixpoint iteration for the interval domain by forcing unstable bounds to $\pm\infty$.

### Input

- Two intervals $[a,b]$, $[c,d]$ with $a,b,c,d \in \mathbb{Z} \cup \{-\infty, +\infty\}$

### Output

- An interval $[a,b] \nabla [c,d]$ that over-approximates both

### Formula
$$
[a,b] \nabla [c,d] = 
\begin{cases}
[-\infty, b] & \text{if } c < a \\
[a, +\infty] & \text{if } d > b \\
[a, b] & \text{otherwise}
\end{cases}
$$

### Complexity
$O(1)$

### Correctness Intuition
Once a bound moves in a direction, it is pushed to infinity, so it cannot change again. Only finitely many changes per bound.

### Common Mistakes

- Widening from $\bot$ gives $[-\infty, +\infty]$ immediately (too imprecise)
- Widening after stabilization is unnecessary
- Forgetting that widening loses precision permanently

### Exam Relevance
High — interval widening is a classic exam question. Often combined with narrowing.

<hr>


## A-06: Syntax-Directed CFA ($\models_s$)

### Purpose
Compute CFA using a syntax-directed system that analyzes function bodies once at definition time.

### Input

- Labeled expression $e$

### Output

- $C^*[\![e]\!]$, a set of constraints

### Key Difference from Acceptability
The syntax-directed relation $\models_s$ analyzes function bodies once regardless of call count. This means:

- Functions are analyzed even if never called
- No "call-context" sensitivity (0-CFA)
- Better for modular analysis

### Rules
Same as acceptability but without runtime context: function body constraints are generated at definition time.

### Complexity
Linear in program size.

<hr>


## A-07: $k$-CFA (Call String Approach)

### Purpose
Refine 0-CFA by distinguishing calling contexts up to depth $k$.

### Input

- Expression $e$, bound $k$ on call string length

### Output

- Context-sensitive cache $\hat{C}(\ell, \delta)$ and environment $\hat{\rho}(x, \delta)$ where $\delta$ is a call string of length $\le k$

### Key Change

- Abstract values replaced by $(\hat{C}, \hat{\rho}, \delta)$ where $\delta$ tracks the call site history
- $k=0$: monovariant (0-CFA)
- $k=1$: call-site sensitivity
- $k=2$: two-level call stack

### Complexity

- $O(|e|^{k+1})$ — exponential in $k$
- $k=1$ is common practical choice

### Correctness Intuition
Different call sites create different instances of formal parameters, removing spurious flows from merged contexts.

### Common Mistakes

- Thinking $k$-CFA is always more precise (it is, but at cost)
- Forgetting that $k$-CFA still over-approximates

### Exam Relevance
Exercise E-03 asks to compare 0-CFA and 1-CFA results.

<hr>


# Complete Exercise Collection

## Source
All exercises from the official exercise PDFs and their extracted text versions.

<hr>


## Easy

### Exercise E-01: Guard Axiom Across Logics

**Source:** `ProgramAnalysis_exercises_a.txt` (Ex. 1)
**Lecture:** Lectures 03–08 (HL, IL, NC, SIL)
**Page:** 1
**Difficulty:** Easy
**Tags:** hoare logic, incorrectness logic, necessary condition logic, sufficient incorrectness logic, boolean guards

#### Statement
Let us consider the following axiom for atomic boolean guards $b?$, where the parentheses $\langle| \cdot |\rangle \in \{\{\cdot\}, [\cdot], (\cdot), \langle\cdot\rangle\}$ are used to denote a generic program logic triple of either Hoare logic, IL, NC or SIL.

$$
\langle| P |\rangle\ b?\ \langle| P \lor b |\rangle
$$

Explain for which logics (HL, IL, NC, SIL) the axiom is sound (for any precondition $P$ and boolean guard $b$):

- if the axiom is sound, prove its validity;
- if it is not sound, first provide a concrete counterexample and then say under which conditions on $P$ and $b$ the axiom would become sound.

#### Official Solution

**Hoare Logic.** A Hoare triple $\{P\}\ c\ \{Q\}$ is sound when every terminating execution from a state satisfying $P$ ends in a state satisfying $Q$. Since executing $b?$ does not modify the state, every reachable state satisfies both $P$ and $b$. In fact:

$$
\llbracket b?\rrbracket P = (P \land b) \subseteq (P \lor b).
$$

Hence the axiom is **sound** for Hoare Logic.

**Incorrectness Logic.** A valid IL triple $[P]\ c\ [Q]$ requires $Q \subseteq \llbracket c\rrbracket P$. For the proposed axiom we would need:

$$
P \lor b \subseteq \llbracket b?\rrbracket P = P \land b.
$$

This is false in general. Counterexample: $P = \texttt{true},\ b = \texttt{false}$. Then $P \lor b = \texttt{true}$, $P \land b = \texttt{false}$. The axiom becomes sound iff $P \lor b = P \land b$, i.e., iff $P = b$.

**Necessary Condition Logic.** NC requires $\llbracket c\rrbracket^{\text{op}} Q \subseteq P$. Since $\llbracket b?\rrbracket^{\text{op}} Q = Q \land b$:

$$
\llbracket b?\rrbracket^{\text{op}} (P \lor b) = (P \lor b) \land b = b.
$$

The axiom is sound for NC iff $b \subseteq P$. Counterexample: $P = \texttt{false},\ b = \texttt{true}$.

**Sufficient Incorrectness Logic.** SIL requires an under-approximation condition: $P \subseteq \llbracket c\rrbracket^{\text{op}} Q$. Thus:

$$
P \subseteq \llbracket b?\rrbracket^{\text{op}} (P \lor b) = (P \lor b) \land b = b.
$$

The axiom is sound for SIL iff $P \subseteq b$. This is false in general. Counterexample: $P = \texttt{true},\ b = \texttt{false}$.

#### Key Concepts

- HL triple validity: $\llbracket c\rrbracket P \subseteq Q$
- IL triple validity: $\llbracket c\rrbracket P \supseteq Q$
- NC triple validity: $\llbracket c\rrbracket^{\text{op}} Q \subseteq P$
- SIL triple validity: $P \subseteq \llbracket c\rrbracket^{\text{op}} Q$
- Boolean guard semantics: $\llbracket b?\rrbracket P = P \land b$

#### Typical Exam Insight
Tests understanding of the fundamental difference between over-approximation (HL) and under-approximation (IL/NC/SIL) logics.

<hr>


## Medium

### Exercise E-02: Galois Connection Design for Abstract Domain

**Source:** `ProgramAnalysis_exercises_a.txt` (Ex. 2)
**Lecture:** Lectures 12–14 (Galois Connections, Abstract Domains)
**Page:** 1
**Difficulty:** Medium
**Tags:** galois connection, abstraction map, concretization map, best correct approximation, completeness, sign domain

#### Statement
Let us consider the usual concrete domain $(\wp(\mathbb{Z}), \subseteq)$ of sets of integers ordered by inclusion and the abstract domain $A = \{ \bot, =0, \le 0, >10, >0, \top \}$ with the obvious concretization function.

1. Define the GC maps $\gamma: A \to \wp(\mathbb{Z})$ and $\alpha: \wp(\mathbb{Z}) \to A$.

2. Draw the Hasse diagram of $A$.

3. Define the bca $\cdot \times_A \cdot$ for the product of integers $\cdot \times \cdot$.

4. Show that $\cdot \times_A \cdot$ is not complete by exhibiting a counterexample.

#### Official Solution

**1. Galois connection maps:**

Concretization:
$$
\gamma(\bot) = \emptyset,\quad
\gamma(=0) = \{0\},\quad
\gamma(\le 0) = \{z \in \mathbb{Z} \mid z \le 0\},
$$
$$
\gamma(>10) = \{z \in \mathbb{Z} \mid z > 10\},\quad
\gamma(>0) = \{z \in \mathbb{Z} \mid z > 0\},\quad
\gamma(\top) = \mathbb{Z}.
$$

Abstraction:
$$
\alpha(X) = 
\begin{cases}
\bot & \text{if } X = \emptyset \\
=0 & \text{if } X = \{0\} \\
\le 0 & \text{else if } X \subseteq \{z \mid z \le 0\} \\
>10 & \text{else if } X \subseteq \{z \mid z > 10\} \\
>0 & \text{else if } X \subseteq \{z \mid z > 0\} \\
\top & \text{otherwise}
\end{cases}
$$

**2. Hasse diagram:**
```
       ⊤
      / \
    >0   ≤0
     |    |
    >10  =0
      \ /
       ⊥
```

**3. Best correct approximation of multiplication:**

$$
a \times_A b = \alpha(\{ x \cdot y \mid x \in \gamma(a),\; y \in \gamma(b) \})
$$

| $\times_A$ | $\bot$ | $=0$ | $\le 0$ | $>10$ | $>0$ | $\top$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $\bot$ | $\bot$ | $\bot$ | $\bot$ | $\bot$ | $\bot$ | $\bot$ |
| $=0$ | $\bot$ | $=0$ | $=0$ | $=0$ | $=0$ | $=0$ |
| $\le 0$ | $\bot$ | $=0$ | $\top$ | $\le 0$ | $\le 0$ | $\top$ |
| $>10$ | $\bot$ | $=0$ | $\le 0$ | $>10$ | $>10$ | $\top$ |
| $>0$ | $\bot$ | $=0$ | $\le 0$ | $>10$ | $>0$ | $\top$ |
| $\top$ | $\bot$ | $=0$ | $\top$ | $\top$ | $\top$ | $\top$ |

**4. Non-completeness:**

Take $X = \{-1\}$, $Y = \{-1\}$. Then $\alpha(X) = \le 0$, $\alpha(Y) = \le 0$. Concrete multiplication gives $X \times Y = \{1\}$, so $\alpha(X \times Y) = (>0)$. However, $\le 0 \times_A \le 0 = \top$ because the products may be $0$ or positive. Therefore $\alpha(X \times Y) \ne \alpha(X) \times_A \alpha(Y)$, proving incompleteness.

#### Key Concepts

- Galois connection definition: $\alpha(c) \sqsubseteq_A a \iff c \subseteq \gamma(a)$
- BCA formula: $F^A = \alpha \circ F \circ \gamma$
- Completeness equation: $\alpha \circ F = F^\# \circ \alpha$
- Formula F-06, F-07, F-08, F-09

#### Typical Exam Insight
Tests understanding of Galois connection construction and the distinction between soundness and completeness.

<hr>

### Exercise E-03: CFA for Higher-Order Functions

**Source:** `ProgramAnalysis_exercises_a.txt` (Ex. 3)
**Lecture:** Lectures 17–24 (CFA)
**Page:** 2
**Difficulty:** Medium
**Tags:** CFA, 0-CFA, 1-CFA, constraint generation, flow logic, acceptability

#### Statement

Consider the following expression $e$:
```
let apply = fn f => f 2
in let inc = fn x => x + 4
in let dbl = fn y => y * 2
in (apply inc) - (apply dbl)
```

1. Add labels to all subexpressions and function abstractions.

2. Guess a possible analysis result for Pure 0-CFA and verify it using the corresponding acceptability relation $\models$. In particular, comment on the abstract values associated with the two calls to apply.

3. Consider the following additional abstract flow: $\texttt{fn } w \Rightarrow w \in \hat{C}(\text{Label}(f))$. Does the acceptability relation $\models$ still hold? What does this say about the difference between soundness and precision?
4. Discuss how the analysis changes using the syntax-directed version of the acceptability relation $\models_s$.

5. Extract the corresponding system of constraints.

6. Explain how the result changes under 1-CFA. Which spurious flows disappear, and why?

#### Official Solution

**1. Labeled expression.**

$$
\begin{aligned}
e \triangleq\ & (\texttt{let } \texttt{apply} = (\texttt{fn } f \Rightarrow (f^1\ 2^2)^3)^4 \\
& \texttt{in } (\texttt{let } \texttt{inc} = (\texttt{fn } x \Rightarrow (x^5 + 4^6)^7)^8 \\
& \texttt{in } (\texttt{let } \texttt{dbl} = (\texttt{fn } y \Rightarrow (y^9 * 2^{10})^{11})^{12} \\
& \texttt{in } ((\texttt{apply}^{13}\ \texttt{inc}^{14})^{15} - (\texttt{apply}^{16}\ \texttt{dbl}^{17})^{18})^{19})^{20})^{21})^{22}
\end{aligned}
$$

**2. Acceptability relation unfolding.**

The relation $(\hat{C}, \hat{\rho}) \models e$ is checked by applying the acceptability rules:

- **[let] rule for outer let:**
  $(\hat{C}, \hat{\rho}) \models (\texttt{fn } f \Rightarrow (f^1\ 2^2)^3)^4$ and $(\hat{C}, \hat{\rho}) \models (\texttt{let inc} = \dots)^{21}$,
  with $\hat{C}(4) \subseteq \hat{\rho}(\texttt{apply})$ and $\hat{C}(21) \subseteq \hat{C}(22)$.

- **[fn] rule:**
  $\{\texttt{fn } f \Rightarrow (f^1\ 2^2)^3\} \subseteq \hat{C}(4)$.

- **[let] rule for inc:**
  $(\hat{C}, \hat{\rho}) \models (\texttt{fn } x \Rightarrow (x^5 + 4^6)^7)^8$ and $(\hat{C}, \hat{\rho}) \models (\texttt{let dbl} = \dots)^{20}$,
  with $\hat{C}(8) \subseteq \hat{\rho}(\texttt{inc})$ and $\hat{C}(20) \subseteq \hat{C}(21)$.

- **[fn] rule:**
  $\{\texttt{fn } x \Rightarrow (x^5 + 4^6)^7\} \subseteq \hat{C}(8)$.

- **[let] rule for dbl:**
  $(\hat{C}, \hat{\rho}) \models (\texttt{fn } y \Rightarrow (y^9 * 2^{10})^{11})^{12}$ and $(\hat{C}, \hat{\rho}) \models ((\texttt{apply}^{13}\ \texttt{inc}^{14})^{15} - (\texttt{apply}^{16}\ \texttt{dbl}^{17})^{18})^{19}$,
  with $\hat{C}(12) \subseteq \hat{\rho}(\texttt{dbl})$ and $\hat{C}(19) \subseteq \hat{C}(20)$.

- **[fn] rule:**
  $\{\texttt{fn } y \Rightarrow (y^9 * 2^{10})^{11}\} \subseteq \hat{C}(12)$.

- **Subtraction rule:**
  $(\hat{C}, \hat{\rho}) \models (\texttt{apply}^{13}\ \texttt{inc}^{14})^{15}$ and $(\hat{C}, \hat{\rho}) \models (\texttt{apply}^{16}\ \texttt{dbl}^{17})^{18}$,
  with $\hat{C}(15) \subseteq \hat{C}(19)$ and $\hat{C}(18) \subseteq \hat{C}(19)$.

- **[app] rule for $(\texttt{apply}^{13}\ \texttt{inc}^{14})^{15}$:**
  $(\hat{C}, \hat{\rho}) \models \texttt{apply}^{13}$ and $(\hat{C}, \hat{\rho}) \models \texttt{inc}^{14}$,
  and for each $\texttt{fn } f \Rightarrow (f^1\ 2^2)^3 \in \hat{C}(13)$:
  $\hat{C}(14) \subseteq \hat{\rho}(f)$ and $\hat{C}(3) \subseteq \hat{C}(15)$.

- **[app] rule for $(\texttt{apply}^{16}\ \texttt{dbl}^{17})^{18}$:**
  $(\hat{C}, \hat{\rho}) \models \texttt{apply}^{16}$ and $(\hat{C}, \hat{\rho}) \models \texttt{dbl}^{17}$,
  and for each $\texttt{fn } f \Rightarrow (f^1\ 2^2)^3 \in \hat{C}(16)$:
  $\hat{C}(17) \subseteq \hat{\rho}(f)$ and $\hat{C}(3) \subseteq \hat{C}(18)$.

An acceptable solution:

$$
\begin{aligned}
\hat{C}(4) &= \{\texttt{fn } f \Rightarrow (f^1\ 2^2)^3\} \\
\hat{C}(8) &= \{\texttt{fn } x \Rightarrow (x^5 + 4^6)^7\} \\
\hat{C}(12) &= \{\texttt{fn } y \Rightarrow (y^9 * 2^{10})^{11}\} \\
\hat{C}(13) &= \hat{C}(16) = \{\texttt{fn } f \Rightarrow (f^1\ 2^2)^3\} \\
\hat{C}(14) &= \{\texttt{fn } x \Rightarrow (x^5+4^6)^7\} \\
\hat{C}(17) &= \{\texttt{fn } y \Rightarrow (y^9*2^{10})^{11}\} \\
\hat{C}(1) &= \{\texttt{fn } x \Rightarrow (x^5+4^6)^7,\ \texttt{fn } y \Rightarrow (y^9*2^{10})^{11}\} \\
\hat{C}(i) &= \emptyset \text{ for all remaining labels } i
\end{aligned}
$$

$$
\begin{aligned}
\hat{\rho}(\texttt{apply}) &= \{\texttt{fn } f \Rightarrow (f^1\ 2^2)^3\} \\
\hat{\rho}(\texttt{inc}) &= \{\texttt{fn } x \Rightarrow (x^5 + 4^6)^7\} \\
\hat{\rho}(\texttt{dbl}) &= \{\texttt{fn } y \Rightarrow (y^9 * 2^{10})^{11}\} \\
\hat{\rho}(f) &= \{\texttt{fn } x \Rightarrow (x^5+4^6)^7,\ \texttt{fn } y \Rightarrow (y^9*2^{10})^{11}\}
\end{aligned}
$$

**Key observation:** Because $\hat{C}(14) \subseteq \hat{\rho}(f)$ and $\hat{C}(17) \subseteq \hat{\rho}(f)$, 0-CFA merges the two calling contexts. Both $\texttt{inc}$ and $\texttt{dbl}$ flow to $f$, losing precision.

**3. Extra flow.** Adding $\texttt{fn } w \Rightarrow w \in \hat{C}(1)$ is still sound (over-approximation) but less precise. This illustrates that acceptability expresses soundness, not optimal precision.

**4. Syntax-directed $\models_s$.** The body of a function is analyzed once at definition time, not at each application. This avoids redundant re-analysis for multiple applications, but also analyzes the body even if the function is never applied. The analysis uses only terms occurring in the expression under investigation.

**5. Constraint system.** Extracted using syntax-directed rules $C^*[\![e]\!]$:

For abstractions:
$$
\begin{aligned}
C^*[\![(\texttt{fn } f \Rightarrow (f^1\ 2^2)^3)^4]\!] &= \{\texttt{fn } f \Rightarrow (f^1\ 2^2)^3 \subseteq C(4)\} \cup C^*[\![(f^1\ 2^2)^3]\!] \\
C^*[\![(\texttt{fn } x \Rightarrow (x^5 + 4^6)^7)^8]\!] &= \{\texttt{fn } x \Rightarrow (x^5 + 4^6)^7 \subseteq C(8)\} \cup C^*[\![(x^5 + 4^6)^7]\!] \\
C^*[\![(\texttt{fn } y \Rightarrow (y^9 * 2^{10})^{11})^{12}]\!] &= \{\texttt{fn } y \Rightarrow (y^9 * 2^{10})^{11} \subseteq C(12)\} \cup C^*[\![(y^9 * 2^{10})^{11}]\!]
\end{aligned}
$$

For let-bindings:
$$
\begin{aligned}
C^*[\![(\texttt{let apply} = \dots)^{22}]\!] &= C^*[\![(\texttt{fn } f \Rightarrow \dots)^4]\!] \cup C^*[\![(\texttt{let inc} = \dots)^{21}]\!] \cup \{C(4) \subseteq r(\texttt{apply}),\ C(21) \subseteq C(22)\} \\
C^*[\![(\texttt{let inc} = \dots)^{21}]\!] &= C^*[\![(\texttt{fn } x \Rightarrow \dots)^8]\!] \cup C^*[\![(\texttt{let dbl} = \dots)^{20}]\!] \cup \{C(8) \subseteq r(\texttt{inc}),\ C(20) \subseteq C(21)\} \\
C^*[\![(\texttt{let dbl} = \dots)^{20}]\!] &= C^*[\![(\texttt{fn } y \Rightarrow \dots)^{12}]\!] \cup C^*[\![((\texttt{apply}^{13}\ \texttt{inc}^{14})^{15} - (\texttt{apply}^{16}\ \texttt{dbl}^{17})^{18})^{19}]\!] \\
&\qquad \cup \{C(12) \subseteq r(\texttt{dbl}),\ C(19) \subseteq C(20)\}
\end{aligned}
$$

For variables:
$$
\begin{aligned}
C^*[\![f^1]\!] &= \{r(f) \subseteq C(1)\} \\
C^*[\![x^5]\!] &= \{r(x) \subseteq C(5)\} \\
C^*[\![y^9]\!] &= \{r(y) \subseteq C(9)\} \\
C^*[\![\texttt{apply}^{13}]\!] &= \{r(\texttt{apply}) \subseteq C(13)\} \\
C^*[\![\texttt{inc}^{14}]\!] &= \{r(\texttt{inc}) \subseteq C(14)\} \\
C^*[\![\texttt{apply}^{16}]\!] &= \{r(\texttt{apply}) \subseteq C(16)\} \\
C^*[\![\texttt{dbl}^{17}]\!] &= \{r(\texttt{dbl}) \subseteq C(17)\}
\end{aligned}
$$

Arithmetic constants generate no flow: $C^*[\![2^2]\!] = C^*[\![4^6]\!] = C^*[\![2^{10}]\!] = \emptyset$.

For applications, the constraint generation considers all abstractions in $\textit{Term}^* = \{\texttt{fn } f \Rightarrow (f^1\ 2^2)^3,\ \texttt{fn } x \Rightarrow (x^5+4^6)^7,\ \texttt{fn } y \Rightarrow (y^9*2^{10})^{11}\}$:

From $(\texttt{apply}^{13}\ \texttt{inc}^{14})^{15}$:
$$
\begin{aligned}
C^*[\![(\texttt{apply}^{13}\ \texttt{inc}^{14})^{15}]\!] &= C^*[\![\texttt{apply}^{13}]\!] \cup C^*[\![\texttt{inc}^{14}]\!] \\
&\cup \{\texttt{fn } f \Rightarrow (f^1\ 2^2)^3 \subseteq C(13) \Rightarrow C(14) \subseteq r(f)\} \\
&\cup \{\texttt{fn } f \Rightarrow (f^1\ 2^2)^3 \subseteq C(13) \Rightarrow C(3) \subseteq C(15)\} \\
&\cup \{\texttt{fn } x \Rightarrow (x^5+4^6)^7 \subseteq C(13) \Rightarrow C(14) \subseteq r(x)\} \\
&\cup \{\texttt{fn } x \Rightarrow (x^5+4^6)^7 \subseteq C(13) \Rightarrow C(7) \subseteq C(15)\} \\
&\cup \{\texttt{fn } y \Rightarrow (y^9*2^{10})^{11} \subseteq C(13) \Rightarrow C(14) \subseteq r(y)\} \\
&\cup \{\texttt{fn } y \Rightarrow (y^9*2^{10})^{11} \subseteq C(13) \Rightarrow C(11) \subseteq C(15)\}
\end{aligned}
$$

Similarly for $(\texttt{apply}^{16}\ \texttt{dbl}^{17})^{18}$ with $C(17)$ instead of $C(14)$.

From $(f^1\ 2^2)^3$:
$$
\begin{aligned}
C^*[\![(f^1\ 2^2)^3]\!] &= C^*[\![f^1]\!] \cup C^*[\![2^2]\!] \\
&\cup \{\texttt{fn } f \Rightarrow (f^1\ 2^2)^3 \subseteq C(1) \Rightarrow C(2) \subseteq r(f)\} \\
&\cup \{\texttt{fn } x \Rightarrow (x^5+4^6)^7 \subseteq C(1) \Rightarrow C(2) \subseteq r(x),\ C(7) \subseteq C(3)\} \\
&\cup \{\texttt{fn } y \Rightarrow (y^9*2^{10})^{11} \subseteq C(1) \Rightarrow C(2) \subseteq r(y),\ C(11) \subseteq C(3)\}
\end{aligned}
$$

Note the key constraints: $C(14) \subseteq r(f)$ and $C(17) \subseteq r(f)$, which merge the two call contexts.

**6. 1-CFA.** Under 1-CFA, each application gets a distinct call string:

- $\delta_1 = \langle 15 \rangle$ for $(\texttt{apply}^{13}\ \texttt{inc}^{14})^{15}$
- $\delta_2 = \langle 18 \rangle$ for $(\texttt{apply}^{16}\ \texttt{dbl}^{17})^{18}$

The acceptability relation becomes context-sensitive:

$$
(\hat{C}, \hat{\rho}) \models^{\text{ce}}_{\delta} e
$$

where $\delta$ is the call string and ce is the context environment mapping variables to call strings.

For the outer binding:
$$
\{\texttt{fn } f \Rightarrow (f^1\ 2^2)^3, \text{ce}_0)\} \subseteq \hat{C}(4, \delta_0)
$$
$$
\hat{C}(4, \delta_0) \subseteq \hat{\rho}(\texttt{apply}, \delta_0)
$$

The two applications produce:

- $\hat{C}(14, \delta_0) \subseteq \hat{\rho}(f, \delta_1)$
- $\hat{C}(17, \delta_0) \subseteq \hat{\rho}(f, \delta_2)$

Hence:
$$
\begin{aligned}
\hat{\rho}(f, \delta_1) &= \{\texttt{fn } x \Rightarrow (x^5+4^6)^7\} \\
\hat{\rho}(f, \delta_2) &= \{\texttt{fn } y \Rightarrow (y^9*2^{10})^{11}\}
\end{aligned}
$$

In the body of $\texttt{apply}$:
$$
\begin{aligned}
\hat{C}(1, \delta_1) &= \{\texttt{fn } x \Rightarrow (x^5+4^6)^7\} \\
\hat{C}(1, \delta_2) &= \{\texttt{fn } y \Rightarrow (y^9*2^{10})^{11}\}
\end{aligned}
$$

Spurious flows disappear: $\texttt{dbl} \notin \hat{C}(1, \delta_1)$ and $\texttt{inc} \notin \hat{C}(1, \delta_2)$. Consequently:

- $\hat{C}(15)$ contains only the result of $\texttt{inc}$
- $\hat{C}(18)$ contains only the result of $\texttt{dbl}$

In summary: 0-CFA merges the two calls to apply; 1-CFA separates them by call site, so the first call propagates only $\texttt{inc}$ to $f$, while the second propagates only $\texttt{dbl}$.

#### Key Concepts

- 0-CFA acceptability relation $\models$ (Algorithm A-04)
- Syntax-directed constraint generation $C^*[\![e]\!]$
- $k$-CFA call string approach (Algorithm A-07)
- Soundness vs. precision
- Context sensitivity eliminates spurious flows

#### Typical Exam Insight

Tests the entire CFA pipeline: labeling, acceptability, constraint generation, and context sensitivity. The key point is understanding why 0-CFA merges contexts and how 1-CFA separates them.

<hr>


## Hard

### Exercise E-04: Separation Logic with Incorrectness

**Source:** `ProgramAnalysis_exercises_b.txt` (Ex. 1)
**Lecture:** Lectures 09–10 (SL, ISL)
**Difficulty:** Hard
**Tags:** separation logic, incorrectness separation logic, heap, postcondition inference

#### Statement
Consider the following code fragment $c$:

```
x := [y];
if (x != nil) then {
  free(y);
  y := x;
} else {
  x := alloc();
  [y] := x;
}
```

Using Incorrectness Separation Logic, find a suitable (non-trivial) postcondition $Q$ for the triple $[y \mapsto z \star z \mapsto \texttt{nil}]\ c\ [\texttt{ok}: Q]$ and inline the intermediate derivation steps that lead to such conclusion.

#### Generated Solution

**Preliminary observation.** In the precondition $y \mapsto z \star z \mapsto \texttt{nil}$, the variable $z$ is a valid heap location (it points to $\texttt{nil}$). Therefore $z \neq \texttt{nil}$, and since $x := [y]$ binds $x$ to $z$, we will have $x \neq \texttt{nil}$ in all reachable states. The $\texttt{else}$ branch is **unreachable** from this precondition.

Nevertheless, we analyse both branches as required by the ISL conditional rule.

**Step 1: Read.** Use the ISL read rule:
$$
\dfrac{}{[v \mapsto w \star P]\ x := [v]\ [v \mapsto w \star P \land x = w]}
$$
With $v=y$, $w=z$, $P=z \mapsto \texttt{nil}$:
$$
[y \mapsto z \star z \mapsto \texttt{nil}]\ x := [y]\
[y \mapsto z \star z \mapsto \texttt{nil} \land x = z]
$$

**Step 2: Conditional — then branch ($x \neq \texttt{nil}$).**

Precondition: $y \mapsto z \star z \mapsto \texttt{nil} \land x = z \land x \neq \texttt{nil}$.

- **free(y):** using the free rule $[v \mapsto \_] \ \texttt{free}(v) \ [\texttt{emp}]$ with frame $R = z \mapsto \texttt{nil} \land x = z \land x \neq \texttt{nil}$:
  $$
  [y \mapsto z \star z \mapsto \texttt{nil} \land x = z \land x \neq \texttt{nil}]\
  \texttt{free}(y)\
  [z \mapsto \texttt{nil} \land x = z \land x \neq \texttt{nil}]
  $$

- **y := x:** using the Floyd-style assignment rule:
  $$
  [P]\ y := x\ [\exists y'.\ P[y'/y] \land y = x[y'/y]]
  $$
  Since $y$ does not appear free in $P = (z \mapsto \texttt{nil} \land x = z \land x \neq \texttt{nil})$:
  $$
  [z \mapsto \texttt{nil} \land x = z \land x \neq \texttt{nil}]\
  y := x\
  [z \mapsto \texttt{nil} \land x = z \land y = x \land x \neq \texttt{nil}]
  $$

  Simplifying ($x = z$ and $y = x$ gives $y = z$, and $z \mapsto \texttt{nil}$ implies $z \neq \texttt{nil}$):
  $$
  Q_{\text{then}} = z \mapsto \texttt{nil} \land x = z \land y = z
  $$

**Step 3: Conditional — else branch ($x = \texttt{nil}$).**

Precondition: $y \mapsto z \star z \mapsto \texttt{nil} \land x = z \land x = \texttt{nil}$.

From $x = z$ and $x = \texttt{nil}$ we obtain $z = \texttt{nil}$, but $z \mapsto \texttt{nil}$ requires $z$ to be a valid heap location. This is a contradiction: **no state satisfies** $P_{\text{else}}$. Hence the else branch contributes nothing to the postcondition.

$$
Q_{\text{else}} = \texttt{false}
$$

**Step 4: Conditional rule.**

$$
\dfrac{[P_{\text{then}}]\ c_{\text{then}}\ [Q_{\text{then}}]\quad [P_{\text{else}}]\ c_{\text{else}}\ [Q_{\text{else}}]}
{[P]\ \texttt{if}\ x \neq \texttt{nil}\ \texttt{then}\ \dots \ \texttt{else}\ \dots \ [Q_{\text{then}} \lor Q_{\text{else}}]}
$$

Since $Q_{\text{else}} = \texttt{false}$, we have $Q_{\text{then}} \lor Q_{\text{else}} = Q_{\text{then}}$.

**Final postcondition:**
$$
Q = z \mapsto \texttt{nil} \land x = z \land y = z
$$

The triple is:
$$
[y \mapsto z \star z \mapsto \texttt{nil}]\
c\
[\texttt{ok}: z \mapsto \texttt{nil} \land x = z \land y = z]
$$

#### Key Concepts

- ISL triples: $[P]\ c\ [Q]$ with $Q \subseteq \llbracket c\rrbracket P$
- Separating conjunction $\star$ for disjoint heap portions
- Points-to predicate $x \mapsto v$
- `alloc()` creates a fresh cell
- `free(y)` disposes the cell at $y$

#### Typical Exam Insight
Tests ability to reason about heap-manipulating programs using under-approximate logic.

<hr>


### Exercise E-05: Galois Connection from Function

**Source:** `ProgramAnalysis_exercises_b.txt` (Ex. 2)
**Lecture:** Lectures 12–14 (Galois Connections)
**Difficulty:** Medium
**Tags:** galois connection, galois insertion, function lifting, inverse image

#### Statement
Given a function $f: \mathbb{Z} \to \mathbb{Z}$, let $L_f: \wp(\mathbb{Z}) \to \wp(\mathbb{Z})$ denote its ordinary powerset lifting defined as $L_f(X) \triangleq \{ f(x) \mid x \in X\}$ and let $I_f: \wp(\mathbb{Z}) \to \wp(\mathbb{Z})$ be defined as $I_f(Y) \triangleq \{ x \mid f(x) \in Y\}$ the inverse image function of $f$.

1. Prove that $L_f$ and $I_f$ form a Galois connection.

2. Under which condition on $f$ do they form a Galois insertion?

#### Generated Solution

**1. Galois connection.**

Let $(\wp(\mathbb{Z}), \subseteq)$ be both the concrete and abstract domain. We set:

- $\alpha = L_f$ (abstraction — direct image)
- $\gamma = I_f$ (concretization — inverse image)

To form a Galois connection, we must prove:
$$
L_f(X) \subseteq Y \iff X \subseteq I_f(Y)
$$

Forward direction ($\Rightarrow$): Assume $L_f(X) \subseteq Y$, i.e., $\{ f(x) \mid x \in X \} \subseteq Y$. Take any $x \in X$. Then $f(x) \in L_f(X) \subseteq Y$, so $f(x) \in Y$. By definition of $I_f$, we have $x \in I_f(Y)$. Since $x$ was arbitrary, $X \subseteq I_f(Y)$.

Backward direction ($\Leftarrow$): Assume $X \subseteq I_f(Y)$, i.e., for all $x \in X$, $f(x) \in Y$. Take any $y \in L_f(X)$. Then $y = f(x)$ for some $x \in X$. Since $x \in X \subseteq I_f(Y)$, we have $f(x) \in Y$, so $y \in Y$. Hence $L_f(X) \subseteq Y$.

Since the equivalence holds for all $X, Y$, $(L_f, I_f)$ form a Galois connection from $(\wp(\mathbb{Z}), \subseteq)$ to $(\wp(\mathbb{Z}), \subseteq)$.

**2. Galois insertion condition.**

A Galois connection is a **Galois insertion** if $\alpha$ is surjective (equivalently $\gamma$ is injective, or $\alpha \circ \gamma = \text{id}$).

$L_f$ is surjective iff every $Y \in \wp(\mathbb{Z})$ can be expressed as $L_f(X)$ for some $X \in \wp(\mathbb{Z})$. This holds iff $f$ is **surjective**:

- If $f$ is surjective, then for any $Y \subseteq \mathbb{Z}$, pick $X = f^{-1}(Y)$. Since for each $y \in Y$ there exists $x$ with $f(x)=y$, we have $L_f(f^{-1}(Y)) \supseteq Y$. In fact $L_f(I_f(Y)) = Y$ for surjective $f$.

- If $f$ is not surjective, let $y \notin \text{image}(f)$. Then $\{y\}$ cannot be expressed as $L_f(X)$ for any $X$, because $L_f(X) \subseteq \text{image}(f)$ always.

Alternatively, checking $\alpha \circ \gamma = \text{id}$:
$$
L_f(I_f(Y)) = \{ f(x) \mid f(x) \in Y \} = Y \cap \text{image}(f)
$$
This equals $Y$ for all $Y \in \wp(\mathbb{Z})$ iff $\text{image}(f) = \mathbb{Z}$, i.e., $f$ is surjective.

**Answer:** $(L_f, I_f)$ form a Galois insertion iff $f: \mathbb{Z} \to \mathbb{Z}$ is **surjective**.

#### Key Concepts

- Galois connection: $L_f(X) \subseteq Y \iff X \subseteq I_f(Y)$
- Galois insertion: $L_f \circ I_f = \text{id}$, i.e., $f$ is surjective
- Formula F-06

#### Typical Exam Insight
Tests understanding of GC beyond the standard $\alpha$/$\gamma$ pattern — uses direct and inverse image.

<hr>


### Exercise E-06: CFA + Data Flow Analysis (DFA) Integration

**Source:** `ProgramAnalysis_exercises_b.txt` (Ex. 3)
**Lecture:** Lectures 17–24 (CFA) + 14–15 (Abstract Domains)
**Difficulty:** Hard
**Tags:** CFA, DFA, sign analysis, abstract interpretation, product domain

#### Statement
Consider the following expression $e$:
```
let n = 5
in let choose =
  if n > 0
  then (fn x => x + 1)
  else (fn y => y * 2)
in choose 4
```

Assume a sign analysis with $\text{Data}_{\text{sign}} = \{\texttt{tt}, \texttt{ff}, -, 0, +\}$.

1. Add labels to all subexpressions and function abstractions.

2. Guess a possible Pure 0-CFA analysis result and verify it using the acceptability relation $\models$. In particular, determine the possible closures flowing to `choose` at the application `(choose 4)`.

3. Explain why Pure 0-CFA cannot determine that one branch of the conditional is unreachable.

4. Perform the DFA using abstract values as powersets: $\widehat{\text{Val}_d} = \wp(\text{Data}_{\text{sign}})$. Compute the abstract values associated with 5, $n$, $n>0$, and the two branches.

5. Explain how the DFA refines the CFA result. Which branch becomes unreachable?
6. Repeat the DFA using the complete lattice formulation of the same sign information and compare.

7. Explain why the refined CFA+DFA result is still sound.

#### Generated Solution

**1. Labelling.**

$$
\begin{aligned}
e \triangleq\ & (\texttt{let } n = 5^1 \\
              & \texttt{in } (\texttt{let } \texttt{choose} = \\
              & \quad (\texttt{if } (n^2 > 0^3)^4 \\
              & \quad \texttt{then } (\texttt{fn } x \Rightarrow (x^5 + 4^6)^7)^8 \\
              & \quad \texttt{else } (\texttt{fn } y \Rightarrow (y^9 * 2^{10})^{11})^{12})^{13} \\
              & \texttt{in } (\texttt{choose}^{14}\ 4^{15})^{16})^{17})^{18}
\end{aligned}
$$

**2. Pure 0-CFA result.**

Environment $\hat{\rho}$:

- $\hat{\rho}(n) = \{ 5 \}$ (constant 5)
- $\hat{\rho}(\texttt{choose}) = \hat{C}(13) = \{ \texttt{fn } x \Rightarrow x+4,\ \texttt{fn } y \Rightarrow y*2 \}$

Cache $\hat{C}$ (selected labels):

- $\hat{C}(8) = \{ \texttt{fn } x \Rightarrow (x^5+4^6)^7 \}$
- $\hat{C}(12) = \{ \texttt{fn } y \Rightarrow (y^9*2^{10})^{11} \}$
- $\hat{C}(13) = \{ \texttt{fn } x \Rightarrow (x^5+4^6)^7,\ \texttt{fn } y \Rightarrow (y^9*2^{10})^{11} \}$
- $\hat{C}(14) = \hat{C}(13)$ (identifier choose flows)
- $\hat{C}(16) = \{ \texttt{fn } x \Rightarrow (x^5+4^6)^7,\ \texttt{fn } y \Rightarrow (y^9*2^{10})^{11} \}$ (application of choose to 4)

Both closures flow to `choose` at the application site.

**3. Why CFA cannot determine branch unreachability.**

0-CFA only tracks function closure flow; it has no data abstraction. The condition $n>0$ is treated as a syntactic control-flow split, but the CFA acceptability relation requires analysing **both** branches regardless of data values. CFA has no mechanism to evaluate $5 > 0$ as true — it simply merges both branches into $\hat{C}(13)$.

**4. DFA with powerset abstract values $\widehat{\text{Val}_d} = \wp(\text{Data}_{\text{sign}})$.**

Define $\text{Data}_{\text{sign}} = \{ \texttt{tt}, \texttt{ff}, -, 0, + \}$ with the usual sign semantics.

- $\widehat{\text{Val}_d}(1) = \{ +\}$ (constant 5 is positive)
- $\widehat{\text{Val}_d}(2) = \{ +\}$ (n copies the value of 5)
- $\widehat{\text{Val}_d}(4) = \{ +\}$ (value of $n > 0$: positive > 0 is true)
  - This requires an abstract evaluation: $+ > 0$ yields $\{ \texttt{tt} \}$ because every positive integer is > 0.

- $\widehat{\text{Val}_d}(5) = \{ +\}$ (constant 4 is positive)
- $\widehat{\text{Val}_d}(15) = \{ +\}$

**Branch condition:** $\widehat{\text{Val}_d}(4) = \{ \texttt{tt} \}$. The else branch ($n \le 0$) has empty abstract value:
$$
\widehat{\text{Val}_d}(\text{condition for else}) = \{ \texttt{ff} \} \cap \text{flow from } n > 0 = \emptyset
$$
Therefore the **else branch is unreachable** under the DFA.

**5. DFA refines CFA.**

The DFA determines that $n > 0$ always evaluates to $\texttt{tt}$ (since $n=5$ is positive). Consequently, only the **then** branch ($\texttt{fn } x \Rightarrow x+4$) is reachable. The CFA result is refined: at label 14, only one closure flows:

$$
\hat{C}(14) = \{ \texttt{fn } x \Rightarrow (x^5+4^6)^7 \}
$$

The spurious closure $\texttt{fn } y \Rightarrow y*2$ is eliminated.

**6. Complete lattice formulation.**

Define the sign lattice as:

```
        ⊤
      / | \

    +   0   -
     \ / \ /
      ⊤   ⊥? 
```

Actually, the standard sign lattice:

```
           ⊤
        /  |  \

       +   0   -
        \  |  /
          ⊥
```

With the correspondence: $\wp(\{\texttt{tt},\texttt{ff},-,0,+\})$ can be mapped to a lattice where each element is a subset. The complete lattice formulation is equivalent to the powerset, but represents the same information more compactly through the ordering:

- $\{+\}$ corresponds to abstract value "positive"
- $\{+,0\}$ corresponds to "non-negative"
- $\{-,0\}$ corresponds to "non-positive"

The DFA result is identical: $n$ is $\{+\}$, $n>0$ is $\{\texttt{tt}\}$, the else branch is unreachable.

**7. Soundness of refined CFA+DFA.**

The refined analysis is still **sound** because:

- CFA soundly over-approximates closure flow: every function that may be called at runtime is included.

- DFA soundly over-approximates data values: every runtime value is included in the abstract value.

- The product CFA×DFA removes closures that are inconsistent with the data flow (e.g., closures in a branch whose guard is false).

- Since no runtime execution can take the else branch (the data DFA proves $n>0$ always holds), no runtime execution can invoke $\texttt{fn } y \Rightarrow y*2$ at the call site. Removing it preserves soundness while improving precision.

Formally: if $(\hat{C}, \hat{\rho}) \models e$ is sound and $\widehat{\text{Val}_d}$ is a sound data abstraction, then $(\hat{C}', \hat{\rho}')$ where $\hat{C}'(\ell) = \hat{C}(\ell) \cap \{ t \mid \widehat{\text{Val}_d}(\ell) \text{ is reachable} \}$ is also sound, because data-unreachable branches carry no runtime executions.

#### Key Concepts

- CFA for higher-order functions
- DFA with sign abstract domain
- Product of CFA and DFA for precision
- Soundness preservation under product

#### Typical Exam Insight
Tests integration of CFA (flow information) with DFA (data information) — the two-stage approach from Lecture 21.

<hr>


# Enhanced Formula Handbook

## F-01: Collecting Semantics

### Formula
$$
\llbracket c\rrbracket P = \bigcup_{\sigma \in P} \llbracket c\rrbracket\sigma
$$

### Meaning
The collecting semantics maps a set of input states to the union of all reachable output states.

### Variables

- $c$: command
- $P$: set of input states
- $\llbracket c\rrbracket\sigma$: output state (or $\bot$ for non-termination) when executing $c$ from $\sigma$

### Intuition
Lifts pointwise semantics to sets. The most concrete semantics used as starting point for abstraction.

### Usage
Foundation of all static analyses. Concrete semantics that gets abstracted.

### Related Lecture
Lecture 02 — Denotational Semantics

### Related Exercises
E-01, E-02

<hr>


## F-02: Weakest Liberal Precondition

### Formula
$$
\operatorname{wlp}(c, Q) = \{ \sigma \mid \llbracket c\rrbracket\{\sigma\} \subseteq Q \}
$$

### Meaning
The set of input states from which every execution (if it terminates) ends in $Q$.

### Variables

- $c$: command
- $Q$: set of output states
- $\sigma$: a single state

### Intuition
The largest precondition under which all executions are safe. The dual of strongest postcondition.

### Usage
Foundation of Hoare Logic: $\{P\}\ c\ \{Q\} \iff P \subseteq \operatorname{wlp}(c, Q)$.

### Related Lecture
Lecture 02 — Denotational Semantics

### Related Exercises
E-01

<hr>


## F-03: Weakest Possible Precondition

### Formula
$$
\operatorname{wpp}(c, Q) = \{ \sigma \mid \llbracket c\rrbracket\sigma \cap Q \neq \emptyset \}
$$

### Meaning
The set of input states that have at least one execution ending in $Q$.

### Variables

- $c$: command
- $Q$: set of output states

### Intuition
The largest precondition for which some execution reaches $Q$. The under-approximate dual of wlp.

### Usage
Foundation of Incorrectness Logic: $[P]\ c\ [Q] \iff P \supseteq \operatorname{wpp}(c, Q)$.

### Related Lecture
Lecture 02 — Denotational Semantics

### Related Exercises
E-01

<hr>


## F-04: Hoare Triple Validity

### Formula
$$
\{P\}\ c\ \{Q\} \iff \llbracket c\rrbracket P \subseteq Q
$$

### Meaning
Every terminating execution from a state in $P$ ends in a state in $Q$.

### Variables

- $P$: precondition (set of input states)
- $c$: command
- $Q$: postcondition (set of output states)

### Intuition
Over-approximation of reachable states. Partial correctness — non-termination is allowed.

### Usage
The standard correctness logic. Proves absence of bugs.

### Related Lecture
Lecture 03 — Hoare Logic

### Related Exercises
E-01

<hr>


## F-05: Incorrectness Triple Validity

### Formula
$$
[P]\ c\ [Q] \iff \llbracket c\rrbracket P \supseteq Q
$$

### Meaning
Every state in $Q$ is reachable from some state in $P$.

### Variables

- $P$: precondition
- $c$: command
- $Q$: postcondition

### Intuition
Under-approximation of reachable states. Proves presence of bugs.

### Usage
Bug finding. Dual of Hoare Logic.

### Related Lecture
Lecture 05 — Incorrectness Logic

### Related Exercises
E-01

<hr>


## F-06: Galois Connection

### Formula
$$
\alpha(c) \sqsubseteq_A a \iff c \sqsubseteq_C \gamma(a)
$$

### Meaning
Abstraction and concretization are adjoint monotone maps between concrete and abstract domains.

### Variables

- $\alpha: C \to A$: abstraction map
- $\gamma: A \to C$: concretization map
- $c \in C$: concrete element
- $a \in A$: abstract element
- $\sqsubseteq_C$, $\sqsubseteq_A$: partial orders on $C$ and $A$

### Intuition
The best abstraction of $c$ is at least as precise as any abstract element $a$ that soundly approximates $c$.

### Usage
Foundation of all abstract interpretation frameworks.

### Related Lecture
Lecture 12 — AI Formal Foundations, Lecture 13 — Galois Connections

### Related Exercises
E-02, E-05

<hr>


## F-07: Soundness of Abstract Semantics

### Formula
$$
\alpha \circ \llbracket c\rrbracket \sqsubseteq \llbracket c\rrbracket^\# \circ \alpha
$$

### Alternative form
$$
\llbracket c\rrbracket \circ \gamma \sqsubseteq \gamma \circ \llbracket c\rrbracket^\#
$$

### Meaning
Abstract execution of a command soundly over-approximates the concrete execution, when both are applied to an abstracted input.

### Variables

- $\llbracket c\rrbracket$: concrete semantics
- $\llbracket c\rrbracket^\#$: abstract semantics
- $\alpha$: abstraction
- $\gamma$: concretization

### Intuition
Abstracting-then-executing is at least as precise as executing-then-abstracting.

### Usage
Prove correctness of abstract interpreters.

### Related Lecture
Lecture 12 — AI Formal Foundations

### Related Exercises
E-02

<hr>


## F-08: Best Abstract Correct Approximation (BCA)

### Formula
$$
\llbracket c\rrbracket^\#_A = \alpha \circ \llbracket c\rrbracket \circ \gamma
$$

### Meaning
The most precise sound abstract semantics for a command, obtained by: concretize, execute concretely, then abstract back.

### Variables

- $\llbracket c\rrbracket^\#_A$: best abstraction of command $c$
- $\alpha$, $\gamma$: Galois connection maps

### Intuition
Any sound abstract semantics must be at least as imprecise as the BCA. The BCA defines the optimal precision achievable with a given abstraction.

### Usage
Benchmark for precision. If a given $F^\#$ equals BCA, it is complete.

### Related Lecture
Lecture 14 — Abstract Domains

### Related Exercises
E-02

<hr>


## F-09: Completeness Equation

### Formula
$$
\alpha \circ \llbracket c\rrbracket = \alpha \circ \llbracket c\rrbracket \circ \gamma \circ \alpha
$$

### Equivalent form
$$
\forall P.\ A(\llbracket c\rrbracket P) = A(\llbracket c\rrbracket(A(P)))
$$

### Meaning
Abstraction after concrete execution equals abstraction after executing on abstracted input. No precision loss from abstraction before execution.

### Variables

- $A = \gamma \circ \alpha$: closure operator
- $\llbracket c\rrbracket$: concrete semantics

### Intuition
If completeness holds for a command, the abstract semantics can be computed without loss of precision.

### Usage
Characterizes when an abstract domain is "precise enough" for a given command.

### Related Lecture
Lecture 16 — Local Completeness Logic

### Related Exercises
E-02

<hr>


## F-10: Galois Insertion Property

### Formula
$$
\alpha \circ \gamma = \operatorname{id}_A
$$

### Meaning
No redundant abstract elements. Every abstract element is the image of some concrete element.

### Equivalent forms

- $\alpha$ is surjective
- $\gamma$ is injective

### Usage
Simplifies the abstract domain by removing elements that cannot arise from abstraction.

### Related Lecture
Lecture 13 — Galois Connections

### Related Exercises
E-05

<hr>


## F-11: LCL Triple Validity

### Formula
$$
\vdash_A [P]\ c\ [Q] \iff Q \subseteq \llbracket c\rrbracket P \subseteq A(Q)
$$

### Meaning
The postcondition $Q$ under-approximates reachable states, while $A(Q)$ over-approximates them. Both under- and over-approximation combined.

### Variables

- $A$: abstraction (closure operator)
- $P, Q$: sets of states
- $\llbracket c\rrbracket P$: reachable states

### Intuition
LCL combines the guarantees of HL (over-approximation) and IL (under-approximation) in a single triple.

### Usage
Reasoning about programs with abstract interpretation in mind.

### Related Lecture
Lecture 16 — LCL

<hr>


## F-12: Local Completeness Condition

### Formula
$$
\mathbb{C}_P(e):\quad A(\llbracket e\rrbracket P) = A(\llbracket e\rrbracket A(P))
$$

### Meaning
The atomic expression $e$ is locally complete for input $P$ — abstraction after execution equals abstraction after abstracting the input first.

### Variables

- $e$: expression (command or guard)
- $P$: input set
- $A$: closure operator

### Intuition
Local completeness only requires the equation for a specific $P$, not for all inputs. This is a weaker (and more achievable) condition than global completeness.

### Usage
Prerequisite for the atomic rules in LCL proof system.

### Related Lecture
Lecture 16 — LCL

<hr>


## F-13: LCL Iteration Rule

### Formula
$$
\frac{\vdash_A [P]\ c\ [Q] \quad Q \implies A(P)}{\vdash_A [P]\ c^\star\ [P \lor Q]}
$$

### Meaning
If the loop body maps $P$ to $Q$, and $Q$ is abstractly equivalent to $P$, then the loop maps $P$ to $P \lor Q$.

### Variables

- $c$: loop body
- $c^\star$: iteration (Kleene star)
- $P, Q$: sets of states
- $A$: abstraction

### Intuition
The condition $Q \implies A(P)$ ensures that $P$ is an "abstract invariant" of the loop.

### Related Lecture
Lecture 16 — LCL

<hr>


## F-14: Fixpoint Approximation Theorem

### Formula
$$
\operatorname{lfp}(F) \sqsubseteq \gamma(\operatorname{lfp}(F^\#))
$$

### Meaning
The concretization of the least fixpoint of the abstract semantic function over-approximates the least fixpoint of the concrete semantic function.

### Variables

- $F$: concrete semantic function
- $F^\#$: abstract semantic function (sound)
- $\gamma$: concretization
- $\operatorname{lfp}$: least fixpoint

### Intuition
Abstract interpretation of loops is sound: the abstract loop invariant over-approximates the concrete reachable states.

### Usage
Core correctness result for loop analysis.

### Related Lecture
Lecture 15 — Abstract Analysis

<hr>


## F-15: Abstract Semantics of Iteration

### Formula
$$
\llbracket c^\star\rrbracket^\# \triangleq \lambda S.\ \operatorname{lfp}\ \lambda X.\ S \sqcup \llbracket c\rrbracket^\# X
$$

### Accelerated version (with widening)
$$
\llbracket c^\star\rrbracket^\# \triangleq \lambda S.\ \operatorname{lfp}\ \lambda X.\ S \nabla \llbracket c\rrbracket^\# X
$$

### Meaning
The abstract semantics of a loop is the least fixpoint of the function $X \mapsto S \sqcup \llbracket c\rrbracket^\# X$, accelerated with widening for non-ACC domains.

### Variables

- $c^\star$: loop (iteration)
- $S$: initial abstract state
- $\sqcup$: abstract join
- $\nabla$: widening operator

### Intuition
Loop analysis requires fixpoint computation; widening ensures termination.

### Related Lecture
Lecture 15 — Abstract Analysis

<hr>


## F-16: Correctness Condition for $F^\#$

### Formula
$$
F^\# \sqsupseteq \alpha \circ F \circ \gamma = F^A
$$

### Meaning
A sound abstract transfer function must be at least as imprecise as the best correct abstraction. Equivalently, it must over-approximate the BCA.

### Variables

- $F$: concrete operator
- $F^\#$: abstract operator
- $F^A$: best correct abstraction

### Intuition
The BCA $F^A$ defines the precision lower bound. Any $F^\#$ that is coarser than $F^A$ is still sound but less precise.

### Related Lecture
Lecture 15 — Abstract Analysis

<hr>


## F-17: Abstract Domain Operations Tables

### Sign Domain Multiplication

| $\times^\#$ | $\mathbb{Z}_{<0}$ | $\mathbb{Z}_{=0}$ | $\mathbb{Z}_{>0}$ |
|:---:|:---:|:---:|:---:|
| $\mathbb{Z}_{<0}$ | $\mathbb{Z}_{>0}$ | $\mathbb{Z}_{=0}$ | $\mathbb{Z}_{<0}$ |
| $\mathbb{Z}_{=0}$ | $\mathbb{Z}_{=0}$ | $\mathbb{Z}_{=0}$ | $\mathbb{Z}_{=0}$ |
| $\mathbb{Z}_{>0}$ | $\mathbb{Z}_{<0}$ | $\mathbb{Z}_{=0}$ | $\mathbb{Z}_{>0}$ |

### Sign Domain Addition

| $+^\#$ | $\mathbb{Z}_{<0}$ | $\mathbb{Z}_{=0}$ | $\mathbb{Z}_{>0}$ | $\mathbb{Z}$ |
|:---:|:---:|:---:|:---:|:---:|
| $\mathbb{Z}_{<0}$ | $\mathbb{Z}_{<0}$ | $\mathbb{Z}_{<0}$ | $\mathbb{Z}$ | $\mathbb{Z}$ |
| $\mathbb{Z}_{=0}$ | $\mathbb{Z}_{<0}$ | $\mathbb{Z}_{=0}$ | $\mathbb{Z}_{>0}$ | $\mathbb{Z}$ |
| $\mathbb{Z}_{>0}$ | $\mathbb{Z}$ | $\mathbb{Z}_{>0}$ | $\mathbb{Z}_{>0}$ | $\mathbb{Z}$ |
| $\mathbb{Z}$ | $\mathbb{Z}$ | $\mathbb{Z}$ | $\mathbb{Z}$ | $\mathbb{Z}$ |

### Related Lecture
Lecture 12 — AI Formal Foundations

### Related Exercises
E-02

<hr>


## F-18: Interval Domain Operations

### Addition
$$
[a,b] +^\# [c,d] = [a+c, b+d]
$$

### Subtraction
$$
[a,b] -^\# [c,d] = [a-d, b-c]
$$

### Negation
$$
-^\# [a,b] = [-b, -a]
$$

### Join
$$
[a,b] \sqcup [c,d] = [\min(a,c), \max(b,d)]
$$

### Meet
$$
[a,b] \sqcap [c,d] = 
\begin{cases}
[\max(a,c), \min(b,d)] & \text{if } \max(a,c) \le \min(b,d) \\
\bot & \text{otherwise}
\end{cases}
$$

### Related Lecture
Lecture 14 — Abstract Domains

<hr>


## F-19: Congruence Domain Operations

### Concretization
$$
\gamma(a\mathbb{Z} + b) = \{ ak + b \mid k \in \mathbb{Z} \}
$$

### Negation
$$
-^\# (a\mathbb{Z} + b) = a\mathbb{Z} + (-b)
$$

### Addition
$$
(a\mathbb{Z} + b) +^\# (c\mathbb{Z} + d) = \gcd(a,c)\mathbb{Z} + (b+d)
$$

### Subtraction
$$
(a\mathbb{Z} + b) -^\# (c\mathbb{Z} + d) = \gcd(a,c)\mathbb{Z} + (b-d)
$$

### Multiplication
$$
(a\mathbb{Z} + b) \times^\# (c\mathbb{Z} + d) = \gcd(ac, ad, bc)\mathbb{Z} + bd
$$

### Meet
$$
(a\mathbb{Z} + b) \sqcap (a'\mathbb{Z} + b') = 
\begin{cases}
\bot & \text{if } b \not\equiv b' \pmod{\gcd(a,a')} \\
\operatorname{lcm}(a,a')\mathbb{Z} + b'' & \text{otherwise}
\end{cases}
$$

### Join
$$
(a\mathbb{Z} + b) \sqcup (a'\mathbb{Z} + b') = d\mathbb{Z} + r \quad\text{where } d = \gcd(a,a',|b-b'|),\; r \equiv b \pmod{d}
$$

### Related Lecture
Lecture 14 — Abstract Domains

<hr>


## F-20: Interval Widening

### Formula
$$
[a,b] \nabla [c,d] = 
\begin{cases}
[-\infty, b] & \text{if } c < a \\
[a, +\infty] & \text{if } d > b \\
[a, b] & \text{otherwise}
\end{cases}
$$

### Meaning
Forces unstable bounds to $\pm\infty$, guaranteeing convergence after finitely many iterations.

### Related Lecture
Lecture 14 — Abstract Domains, Lecture 15 — Abstract Analysis

<hr>


# Lecture Summaries

## Lecture 01 — Introduction

### Key Definitions

- **Correctness**: absence of bugs (over-approximation)
- **Incorrectness**: presence of bugs (under-approximation)
- **Soundness**: if analysis says YES, the property holds
- **Completeness**: if property holds, analysis says YES
- **Rice's Theorem**: no automatic, universal, exact analysis

### Key Formulas

- F-01: Collecting semantics
- F-04: HL triple validity
- F-05: IL triple validity

### Key Algorithms
None in this lecture.

### Common Mistakes

- Confusing soundness and completeness
- Thinking testing can prove correctness
- Expecting exact automatic analysis

### Exam Checklist

- [ ] Can explain Rice's Theorem and its consequences
- [ ] Can distinguish over- vs under-approximation
- [ ] Understands the approximation spectrum table

<hr>


## Lecture 02 — Denotational Semantics

### Key Definitions

- **Memory states**: $\Sigma = \{\sigma: X \to \mathbb{Z}\}$
- **Collecting semantics**: $\llbracket c\rrbracket: \wp(\Sigma) \to \wp(\Sigma)$
- **wlp**: $\operatorname{wlp}(c,Q) = \{\sigma \mid \llbracket c\rrbracket\{\sigma\} \subseteq Q\}$
- **wpp**: $\operatorname{wpp}(c,Q) = \{\sigma \mid \llbracket c\rrbracket\sigma \cap Q \neq \emptyset\}$

### Key Formulas

- F-01, F-02, F-03

### Key Algorithms
None (foundational definitions).

### Common Mistakes

- Forgetting $\llbracket c^\star\rrbracket P = \bigcup_{k\ge 0} \llbracket c\rrbracket^k P$
- Not distinguishing wlp and wpp

### Exam Checklist

- [ ] Can compute collecting semantics for simple programs
- [ ] Understands wlp vs wpp
- [ ] Can encode conditionals and loops using guarded commands

<hr>


## Lecture 03 — Hoare Logic

### Key Definitions

- **HL triple**: $\{P\}\ c\ \{Q\} \iff \llbracket c\rrbracket P \subseteq Q$
- **Loop invariant**: property that holds before and after each loop iteration

### Key Formulas

- F-04
- Inference rules (assignment, composition, conditional, while, consequence)

### Key Algorithms
None (proof system).

### Common Mistakes

- Misapplying Hoare's assignment axiom (backward substitution)
- Choosing a loop invariant that is too weak/too strong
- Forgetting the consequence rule

### Exam Checklist

- [ ] Can prove simple programs with HL
- [ ] Can find loop invariants
- [ ] Knows Hoare vs Floyd assignment axioms

<hr>


## Lecture 04 — Total Correctness

### Key Definitions

- **Partial correctness**: $\{P\}\ c\ \{Q\}$ (non-termination allowed)
- **Total correctness**: $[P]\ c\ [Q]$ (must terminate)
- **Variant**: $t$ — expression that decreases each iteration, bounded below

### Key Formulas

- Total correctness while rule with variant $t$

### Common Mistakes

- Confusing total correctness notation with IL notation
- Forgetting to prove the variant decreases and is bounded below

### Exam Checklist

- [ ] Can prove termination using a variant
- [ ] Understands relation between partial and total correctness

<hr>


## Lecture 05 — Incorrectness Logic

### Key Definitions

- **IL triple**: $[P]\ c\ [Q] \iff \llbracket c\rrbracket P \supseteq Q$
- **Principle of Agreement**: IL + HL implies precision
- **Principle of Denial**: IL contradicts HL — bug found

### Key Formulas

- F-05
- IL inference rules (skip, assignment, assume, error, nondet, sequence, choice, consequence — reverse!)

### Common Mistakes

- Using Hoare's assignment axiom in IL (unsound!)
- Reverse direction of consequence rule

### Exam Checklist

- [ ] Can prove bug-finding triples with IL
- [ ] Understands the duality between HL and IL
- [ ] Knows which HL rules are unsound in IL

### Semantics and Grammar

Regular commands with atomic commands:

$$
\begin{aligned}
e &::= \mathsf{skip} \mid x := a \mid b? \\
c &::= e \mid c_1;c_2 \mid c_1 + c_2 \mid c^{\star}
\end{aligned}
$$

Syntactic sugar:

$$
\mathsf{if}\ b\ \mathsf{then}\ c_1\ \mathsf{else}\ c_2 \triangleq (b?;c_1) + (\lnot b?;c_2)
\qquad
\mathsf{while}\ b\ \mathsf{do}\ c \triangleq (b?;c)^{\star};\lnot b?
$$

Collecting semantics $\llbracket c\rrbracket : \wp(\Sigma) \to \wp(\Sigma)$:

$$
\llbracket\mathsf{skip}\rrbracket P \triangleq P
\qquad
\llbracket x := a\rrbracket P \triangleq \{\sigma[v/x] \mid \sigma \in P,\ v = \llbracket a\rrbracket\sigma\}
$$
$$
\llbracket b?\rrbracket P \triangleq \{\sigma \in P \mid \sigma \models b\}
\qquad
\llbracket\mathsf{error}()\rrbracket P \triangleq \emptyset
$$
$$
\llbracket x := \mathsf{nondet}()\rrbracket P \triangleq \{\sigma[v/x] \mid \sigma \in P,\ v \in \mathbb{Z}\}
$$
$$
\llbracket c_1;c_2\rrbracket P \triangleq \llbracket c_2\rrbracket(\llbracket c_1\rrbracket P)
\qquad
\llbracket c_1 + c_2\rrbracket P \triangleq \llbracket c_1\rrbracket P \cup \llbracket c_2\rrbracket P
$$
$$
\llbracket c^{\star}\rrbracket P \triangleq \bigcup_{k \ge 0} \llbracket c^k\rrbracket P
\quad\text{where}\quad
c^k \triangleq c;\dots;c\ (k\ \text{times})
$$

Relational semantics $\llbracket c\rrbracket \subseteq \Sigma \times \Sigma$:

$$
\llbracket\mathsf{skip}\rrbracket \triangleq \{(\sigma,\sigma)\}
\qquad
\llbracket b?\rrbracket \triangleq \{(\sigma,\sigma) \mid \sigma \models b\}
$$
$$
\llbracket x:=a\rrbracket \triangleq \{(\sigma,\sigma[\llbracket a\rrbracket\sigma/x]) \mid \sigma \in \Sigma\}
\qquad
\llbracket\mathsf{error}()\rrbracket \triangleq \emptyset
$$
$$
\llbracket x:=\mathsf{nondet}()\rrbracket \triangleq \{(\sigma,\sigma[v/x]) \mid \sigma \in \Sigma,\ v \in \mathbb{Z}\}
$$

### IL Inference Rules

**Skip:**
$$
[\mathsf{skip}]\quad \dfrac{}{[P]\ \mathsf{skip}\ [P]}
$$

**Floyd's assignment axiom** (same as HL):
$$
[\mathsf{Floyd}]\quad \dfrac{}{[P]\ x:=a\ [\exists x'.\ P[x'/x] \land x = a[x'/x]]}
$$

**Hoare's assignment axiom** (unsound for IL):
$$
[\mathsf{Hoare}]\quad \dfrac{}{[Q[a/x]]\ x:=a\ [Q]}
$$
Counterexample: $[y = 42]\ x:=42\ [y = x]$ is unsound because $\delta = [x \mapsto 3, y \mapsto 3]$ satisfies $y = x$ but is unreachable.

**Assume/Guard:**
$$
[\mathsf{assume}]\quad \dfrac{}{[P]\ b?\ [P \land b]}
$$

**Error:**
$$
[\mathsf{error}]\quad \dfrac{}{[P]\ \mathsf{error}()\ [\mathsf{false}]}
$$

**Nondet:**
$$
[\mathsf{nondet}]\quad \dfrac{}{[P]\ x:=\mathsf{nondet}()\ [\exists x.\ P]}
$$

**Sequence:**
$$
[\mathsf{seq}]\quad \dfrac{[P]\ c_1\ [R]\quad [R]\ c_2\ [Q]}{[P]\ c_1;c_2\ [Q]}
$$

**Choice:**
$$
[\mathsf{choice}]\quad \dfrac{[P]\ c_1\ [Q_1]\quad [P]\ c_2\ [Q_2]}{[P]\ c_1 + c_2\ [Q_1 \lor Q_2]}
$$

**ChoiceL/ChoiceR** (dropping disjuncts):
$$
[\mathsf{choiceL}]\quad \dfrac{[P]\ c_1\ [Q]}{[P]\ c_1 + c_2\ [Q]}
\qquad
[\mathsf{choiceR}]\quad \dfrac{[P]\ c_2\ [Q]}{[P]\ c_1 + c_2\ [Q]}
$$

**Consequence** (reversed from HL):
$$
[\mathsf{cons}]\quad \dfrac{P' \Rightarrow P \quad [P']\ c\ [Q']\quad Q \Rightarrow Q'}{[P]\ c\ [Q]}
$$

In IL we weaken the pre and strengthen the post (opposite of HL).

**Disjunction:**
$$
[\mathsf{disj}]\quad \dfrac{[P_1]\ c\ [Q_1]\quad [P_2]\ c\ [Q_2]}{[P_1 \lor P_2]\ c\ [Q_1 \lor Q_2]}
$$

**Derived if rule:**
$$
[\mathsf{if}]\quad \dfrac{[P \land b]\ c_1\ [Q_1]\quad [P \land \lnot b]\ c_2\ [Q_2]}{[P]\ \mathsf{if}\ b\ \mathsf{then}\ c_1\ \mathsf{else}\ c_2\ [Q_1 \lor Q_2]}
$$

### Loop Rules

**Bounded unrolling:**
$$
[\mathsf{unroll}]\quad \dfrac{[P]\ c;c^{\star}\ [Q]}{[P]\ c^{\star}\ [Q]}
$$

**Iteration zero:**
$$
[\mathsf{iter0}]\quad \dfrac{}{[P]\ c^{\star}\ [P]}
$$

**Backwards variant:**
$$
[\mathsf{iter}]\quad \dfrac{\forall n \in \mathbb{N}.\ [P_n]\ c\ [P_{n+1}]}{[P_0]\ c^{\star}\ [\exists k.\ P_k]}
$$

### Frame Rule for IL

$$
[\mathsf{frame}]\quad \dfrac{[P]\ c\ [Q]}{[P \land R]\ c\ [Q \land R]}
$$

Side condition: assigned variables in $c$ are disjoint from free variables in $R$.

### Principle of Agreement

If $[P']\ c\ [Q']$ and $P' \Rightarrow P$ and $\{P\}\ c\ \{Q\}$ then $Q' \Rightarrow Q$.

Proof: $Q' \subseteq \llbracket c\rrbracket P' \subseteq \llbracket c\rrbracket P \subseteq Q$.

### Principle of Denial

If $[P']\ c\ [Q']$ and $P' \Rightarrow P$ and $\lnot(Q' \Rightarrow Q)$ then $\lnot(\{P\}\ c\ \{Q\})$.

### Duality Summary

| HL | IL |
|:---|:---:|
| $\{P\}\ c\ \{Q\}$ with $\llbracket c\rrbracket P \subseteq Q$ | $[P]\ c\ [Q]$ with $\llbracket c\rrbracket P \supseteq Q$ |
| Over-approximation | Under-approximation |
| Proves correctness | Finds bugs |
| Strengthen pre, weaken post | Weaken pre, strengthen post |
| Conjunction rule sound | Conjunction rule unsound |
| $\{P\}\ c\ \{Q_1 \land Q_2\}$ from premises | $[P]\ c\ [Q_1 \lor Q_2]$ from premises |
| Forget info along path, remember all paths | Remember info along path, forget some paths |

<hr>


## Lecture 06 — Real Incorrectness Logic

### Key Insight

- HL: forget info along a path, remember all paths
- IL: remember info along a path, forget some paths

### Exam Checklist

- [ ] Can handle non-determinism in IL
- [ ] Understands error killing execution

### Exit Conditions

The real IL adds exit conditions $\epsilon \in \{\mathsf{ok},\mathsf{er}\}$ to triples:

$$
[P]\ c\ [\epsilon : Q]
$$

- **ok**: normal (successful) termination
- **er**: erroneous termination

Shorthand: $[P]\ c\ [\mathsf{ok}:Q_1][\mathsf{er}:Q_2]$ stands for $[P]\ c\ [\mathsf{ok}:Q_1]$ and $[P]\ c\ [\mathsf{er}:Q_2]$.

Validity condition: $Q_1 \subseteq \llbracket c\rrbracket_{\mathsf{ok}} P$ and $Q_2 \subseteq \llbracket c\rrbracket_{\mathsf{er}} P$.

### Relational Semantics with Exit Conditions

$$
\llbracket c\rrbracket_{\epsilon} \subseteq \Sigma \times \Sigma \quad\text{for}\ \epsilon \in \{\mathsf{ok},\mathsf{er}\}
$$

Atomic commands:

$$
\llbracket\mathsf{skip}\rrbracket_{\mathsf{ok}} \triangleq \{(\sigma,\sigma)\}
\qquad
\llbracket\mathsf{skip}\rrbracket_{\mathsf{er}} \triangleq \emptyset
$$
$$
\llbracket b?\rrbracket_{\mathsf{ok}} \triangleq \{(\sigma,\sigma) \mid \sigma \models b\}
\qquad
\llbracket b?\rrbracket_{\mathsf{er}} \triangleq \emptyset
$$
$$
\llbracket x:=a\rrbracket_{\mathsf{ok}} \triangleq \{(\sigma,\sigma[\llbracket a\rrbracket\sigma/x]) \mid \sigma \in \Sigma\}
\qquad
\llbracket x:=a\rrbracket_{\mathsf{er}} \triangleq \emptyset
$$
$$
\llbracket\mathsf{error}()\rrbracket_{\mathsf{ok}} \triangleq \emptyset
\qquad
\llbracket\mathsf{error}()\rrbracket_{\mathsf{er}} \triangleq \{(\sigma,\sigma) \mid \sigma \in \Sigma\}
$$
$$
\llbracket x:=\mathsf{nondet}()\rrbracket_{\mathsf{ok}} \triangleq \{(\sigma,\sigma[x \mapsto v]) \mid \sigma \in \Sigma,\ v \in \mathbb{Z}\}
\qquad
\llbracket x:=\mathsf{nondet}()\rrbracket_{\mathsf{er}} \triangleq \emptyset
$$

Composition:

$$
\llbracket c_1;c_2\rrbracket_{\mathsf{ok}} \triangleq \llbracket c_2\rrbracket_{\mathsf{ok}} \circ \llbracket c_1\rrbracket_{\mathsf{ok}}
$$
$$
\llbracket c_1;c_2\rrbracket_{\mathsf{er}} \triangleq \llbracket c_1\rrbracket_{\mathsf{er}} \cup (\llbracket c_2\rrbracket_{\mathsf{er}} \circ \llbracket c_1\rrbracket_{\mathsf{ok}})
$$
$$
\llbracket c_1 + c_2\rrbracket_{\epsilon} \triangleq \llbracket c_1\rrbracket_{\epsilon} \cup \llbracket c_2\rrbracket_{\epsilon}
$$
$$
\llbracket c^{\star}\rrbracket_{\epsilon} \triangleq \bigcup_{k \in \mathbb{N}} \llbracket c^k\rrbracket_{\epsilon}
$$

where $T \circ S \triangleq \{(\sigma_1,\sigma_2) \mid \exists\sigma.\ (\sigma_1,\sigma) \in S \land (\sigma,\sigma_2) \in T\}$.

Error short-circuiting: if $c_1$ fails, $c_2$ is skipped.

### Real IL Inference Rules

**Skip:**
$$
[\mathsf{skip}]\quad \dfrac{}{[P]\ \mathsf{skip}\ [\mathsf{ok}:P][\mathsf{er}:\mathsf{false}]}
$$

**Floyd's assignment:**
$$
[\mathsf{Floyd}]\quad \dfrac{}{[P]\ x:=a\ [\mathsf{ok}:\exists x'.\ P[x'/x] \land x = a[x'/x]][\mathsf{er}:\mathsf{false}]}
$$

**Assume:**
$$
[\mathsf{assume}]\quad \dfrac{}{[P]\ b?\ [\mathsf{ok}:P \land b][\mathsf{er}:\mathsf{false}]}
$$

**Error:**
$$
[\mathsf{error}]\quad \dfrac{}{[P]\ \mathsf{error}()\ [\mathsf{ok}:\mathsf{false}][\mathsf{er}:P]}
$$

**Nondet:**
$$
[\mathsf{nondet}]\quad \dfrac{}{[P]\ x:=\mathsf{nondet}()\ [\mathsf{ok}:\exists x.\ P][\mathsf{er}:\mathsf{false}]}
$$

**Sequence:**
$$
[\mathsf{seq}]\quad \dfrac{[P]\ c_1\ [\mathsf{ok}:R]\quad [R]\ c_2\ [\epsilon:Q]}{[P]\ c_1;c_2\ [\epsilon:Q]}
$$
$$
[\mathsf{seq\_sc}]\quad \dfrac{[P]\ c_1\ [\mathsf{er}:Q]}{[P]\ c_1;c_2\ [\mathsf{er}:Q]}
$$

**Choice:**
$$
[\mathsf{choiceL}]\quad \dfrac{[P]\ c_1\ [\epsilon:Q]}{[P]\ c_1 + c_2\ [\epsilon:Q]}
\qquad
[\mathsf{choiceR}]\quad \dfrac{[P]\ c_2\ [\epsilon:Q]}{[P]\ c_1 + c_2\ [\epsilon:Q]}
$$

**Frame:**
$$
[\mathsf{frame}]\quad \dfrac{[P]\ c\ [Q]}{[P \land R]\ c\ [Q \land R]}
$$

### Division and Undefined Expressions

Define $\mathsf{def}(a)$ for arithmetic expressions:

$$
\mathsf{def}(n) \triangleq \mathsf{true}
\qquad
\mathsf{def}(x) \triangleq \mathsf{true}
\qquad
\mathsf{def}(a_1 + a_2) \triangleq \mathsf{def}(a_1) \land \mathsf{def}(a_2)
$$
$$
\mathsf{def}(a_1 / a_2) \triangleq \mathsf{def}(a_1) \land \mathsf{def}(a_2) \land a_2 \neq 0
$$

For boolean expressions:

$$
\mathsf{def}(a_1 \le a_2) \triangleq \mathsf{def}(a_1) \land \mathsf{def}(a_2)
\qquad
\mathsf{def}(b_1 \land b_2) \triangleq \mathsf{def}(b_1) \land \mathsf{def}(b_2)
$$

Atomic rules with division:

$$
[P]\ x:=a\ [\mathsf{ok}:\exists x'.\ P[x'/x] \land \mathsf{def}(a[x'/x]) \land x = a[x'/x]]
$$
$$
[P]\ x:=a\ [\mathsf{er}:P \land \lnot\mathsf{def}(a)]
$$
$$
[P]\ b?\ [\mathsf{ok}:P \land \mathsf{def}(b) \land b]
$$
$$
[P]\ b?\ [\mathsf{er}:P \land \lnot\mathsf{def}(b)]
$$

### Weakest Precondition in IL

In HL, for any $c$ and $Q$ there exists a weakest precondition $P = \operatorname{wlp}(c,Q)$ such that $\{P\}\ c\ \{Q\}$.

In IL, a weakest precondition $P$ such that $[P]\ c\ [Q]$ may **not** exist. Example: there is no $P$ such that $[P]\ x:=42\ [\mathsf{true}]$ because $[\mathsf{true}]\ x:=42\ [\mathsf{true}]$ is valid but a weaker precondition cannot exist (any $P$ makes $[P]\ x:=42\ [\mathsf{true}]$ valid trivially, but there is no unique weakest).

### Procedural Abstraction

HL over-approximation for procedures:

```c
void foo() { // presumes {x >= 0}
    x := x + 1; // achieves {x > 0}
}
```

With HL, client code can use the spec compositionally because $\{x > 0\} \Rightarrow \{x \ge 0\}$.

IL under-approximation for procedures:

```c
void foo() { // presumes [x >= 0]
    x := x + 1; // achieves [x > 0]
}
```

With IL, client code **cannot** weaken the precondition: $[x > 0] \not\Rightarrow [x \ge 0]$. Under-approximations cannot be weakened, so compositional reasoning is more constrained.

<hr>


## Lecture 07 — More IL: Non-termination and Control

### Key Concepts

- Non-termination analysis via over- and under-approximation
- Guarded commands and nondeterministic choice

### Exam Checklist

- [ ] Understands how IL handles loops (bounded unrolling)

### Soundness of IL

**Theorem.** Any derivable IL triple is valid.

Proof by induction on the derivation tree. It suffices to show local soundness of each rule.

Sample case [seq]: Assume premises valid, i.e., $\llbracket c_1\rrbracket P \supseteq R$ and $\llbracket c_2\rrbracket R \supseteq Q$. Then:

$$
\llbracket c_1;c_2\rrbracket P = \llbracket c_2\rrbracket(\llbracket c_1\rrbracket P) \supseteq \llbracket c_2\rrbracket R \supseteq Q
$$

Sample case [choice]: Assume $\llbracket c_1\rrbracket P \supseteq Q_1$ and $\llbracket c_2\rrbracket P \supseteq Q_2$. Then:

$$
\llbracket c_1 + c_2\rrbracket P = \llbracket c_1\rrbracket P \cup \llbracket c_2\rrbracket P \supseteq Q_1 \cup Q_2
$$

Sample case [unroll]: Assume $\llbracket c;c^{\star}\rrbracket P \supseteq Q$. Then:

$$
\llbracket c^{\star}\rrbracket P = \bigcup_{k=0}^{\infty} \llbracket c^k\rrbracket P \supseteq \bigcup_{k=1}^{\infty} \llbracket c^k\rrbracket P = \llbracket c;c^{\star}\rrbracket P \supseteq Q
$$

### Relative Completeness of IL

**Theorem.** Any valid IL triple can be derived, assuming an oracle to decide implications.

Proof sketch: Show $[P]\ c\ [\llbracket c\rrbracket P]$ is derivable for any $c$ and $P$, by structural induction on $c$. Then for any valid triple $[P]\ c\ [Q]$ we have $\llbracket c\rrbracket P \supseteq Q$, and we derive it using [cons]:

$$
\dfrac{[P]\ c\ [\llbracket c\rrbracket P] \quad \llbracket c\rrbracket P \Rightarrow Q}{[P]\ c\ [Q]}
$$

For Kleene star, use Pn ≜ [[c^n]]P and instantiate [iter]:

$$
\dfrac{\forall n.\ [[c^n]]P\ c\ [[c^{n+1}]]P}{[P]\ c^{\star}\ [\exists k.\ [[c^k]]P]}
$$

### Minimal Set of Rules

$$
[\mathsf{atom}]\quad \dfrac{}{[P]\ e\ [\llbracket e\rrbracket P]}
\qquad
[\mathsf{seq}]\quad \dfrac{[P]\ c_1\ [R]\quad [R]\ c_2\ [Q]}{[P]\ c_1;c_2\ [Q]}
$$
$$
[\mathsf{choice}]\quad \dfrac{\forall i \in \{1,2\}.\ [P]\ c_i\ [Q_i]}{[P]\ c_1 + c_2\ [Q_1 \cup Q_2]}
\qquad
[\mathsf{iter}]\quad \dfrac{\forall n \ge 0.\ [P_n]\ c\ [P_{n+1}]}{[P_0]\ c^{\star}\ [\exists k.\ P_k]}
$$
$$
[\mathsf{cons}]\quad \dfrac{P' \Rightarrow P \quad [P']\ c\ [Q']\quad Q \Rightarrow Q'}{[P]\ c\ [Q]}
$$

Auxiliary rules: $[\mathsf{disj}]$, $[\mathsf{iter0}]$, $[\mathsf{unroll}]$, $[\mathsf{frame}]$, $[\mathsf{stren}]$, $[\mathsf{weak}]$.

### Mixed HL+IL Exercises

**Exercise 1:** Is the following mixed rule sound?

$$
\dfrac{[P]\ c\ [\mathsf{ok}:P \land \lnot b] \qquad \{P \land b\}\ c\ \{P\}}{[P]\ \mathsf{while}\ b\ \mathsf{do}\ c\ [\mathsf{ok}:P \land \lnot b]}
$$

Answer: Yes, the conclusion is always valid, because the HL premise ensures correctness while the IL premise ensures reachability.

**Exercise 2:** Is the following mixed rule sound?

$$
\dfrac{[P \land b]\ c\ [\mathsf{ok}:P] \qquad \{P\}\ \mathsf{while}\ b\ \mathsf{do}\ c\ \{P \land \lnot b\}}{[P]\ \mathsf{while}\ b\ \mathsf{do}\ c\ [\mathsf{ok}:P \land \lnot b]}
$$

Answer: No. Counterexample: $P = b = (x > 0)$, $c = x := x - 1$. The IL premise $[x > 0]\ x:=-1\ [\mathsf{ok}:x > 0]$ is valid, but the HL premise $\{x > 0\}\ \mathsf{while}\ x>0\ \mathsf{do}\ x:=x-1\ \{x \le 0\}$ is not valid because the loop might not terminate (or the post is $\{x \le 0\}$ which doesn't hold for all executions).

### Backward Analysis

Weakest possible precondition ($\operatorname{wpp}$), also called backward semantics:

$$
\llbracket c\rrbracket^{\mathsf{op}} \delta \triangleq \{\sigma \mid \delta \in \llbracket c\rrbracket\sigma\}
\qquad
\llbracket c\rrbracket^{\mathsf{op}} Q \triangleq \bigcup_{\delta \in Q} \llbracket c\rrbracket^{\mathsf{op}} \delta
$$

$\sigma \in \llbracket c\rrbracket^{\mathsf{op}} \delta \iff \delta \in \llbracket c\rrbracket\sigma$. Hoare called this the "weakest possible precondition," distinct from $\operatorname{wlp}$.

Example: $c \triangleq (z := x) + (z := y)$, $Q \triangleq (z = 0)$.

- $\operatorname{wlp}(c, Q) = (x = 0 \land y = 0)$ (both branches must give $z = 0$)
- $\llbracket c\rrbracket^{\mathsf{op}} Q = (x = 0 \lor y = 0)$ (at least one branch can give $z = 0$)

### Necessary Conditions (NC) Logic

NC triple: $(P)\ c\ (Q)$ means "any state $\sigma$ that admits at least one non-erroneous execution of $c$ ending in $Q$ is in $P$."

$$
(P)\ c\ (Q) \iff \llbracket c\rrbracket^{\mathsf{op}} Q \subseteq P
$$

NC is an **over-approximation** (backward) logic. It expresses necessary preconditions for correctness: if $\sigma \notin P$, then all executions either diverge or reach only bad states.

$$
G(\sigma) \ne \emptyset \implies \sigma \in P \qquad \sigma \notin P \implies (I(\sigma) = \emptyset \implies B(\sigma) \ne \emptyset \land G(\sigma) = \emptyset)
$$

**NC Consequence rule:**

$$
\dfrac{P' \Rightarrow P \qquad (P')\ c\ (Q') \qquad Q \Rightarrow Q'}{(P)\ c\ (Q)}
$$

Weaken the pre and strengthen the post (same direction as HL).

### HL vs NC Relation

$$
\{P\}\ c\ \{Q\} \iff (\lnot P)\ c\ (\lnot Q)
$$

Proof: Assume $\llbracket c\rrbracket P \subseteq Q$. Want $\llbracket c\rrbracket^{\mathsf{op}}(\lnot Q) \subseteq \lnot P$. Take $\sigma \in \llbracket c\rrbracket^{\mathsf{op}}(\lnot Q)$. Then $\exists \delta \in \lnot Q$ with $\sigma \in \llbracket c\rrbracket^{\mathsf{op}} \delta$, i.e., $\delta \in \llbracket c\rrbracket\sigma$. If $\sigma \in P$, then $\delta \in \llbracket c\rrbracket\sigma \subseteq \llbracket c\rrbracket P \subseteq Q$, contradicting $\delta \notin Q$. Thus $\sigma \notin P$, i.e., $\sigma \in \lnot P$.

### Four-Logic Comparison

| | Forward | Backward |
|:---|:---:|:---:|
| **Over** | HL: $\{P\}\ c\ \{Q\}$, $\llbracket c\rrbracket P \subseteq Q$ | NC: $(P)\ c\ (Q)$, $\llbracket c\rrbracket^{\mathsf{op}} Q \subseteq P$ |
| **Under** | IL: $[P]\ c\ [Q]$, $\llbracket c\rrbracket P \supseteq Q$ | SIL: $\langle P\rangle\ c\ \langle Q\rangle$, $\llbracket c\rrbracket^{\mathsf{op}} Q \supseteq P$ |

<hr>


## Lecture 08 — Symbolic Incorrectness Logic (SIL)

### Key Concepts

- SIL extends IL with symbolic execution and path conditions
- Under-approximate reasoning with symbolic states

### Exam Checklist

- [ ] Understands SIL triples as under-approximation
- [ ] Knows the SIL guard axiom condition: $P \subseteq b$ for soundness

### SIL Definition

SIL (Sufficient Incorrectness Logic) is a **backward under-approximation** logic. SIL triple:

$$
\langle P\rangle\ c\ \langle Q\rangle
$$

Validity: $P \subseteq \llbracket c\rrbracket^{\mathsf{op}} Q$, i.e., $\forall \sigma \in P.\ \exists \delta \in Q.\ \delta \in \llbracket c\rrbracket\sigma$.

Meaning: any state in $P$ can lead to an error in $Q$. This characterizes **sufficient conditions for incorrectness** — it finds initial states that cause errors.

**Manifest errors**: An error is manifest if it occurs independently of context.
$$
\langle\mathsf{true}\rangle\ c\ \langle Q\rangle\ \text{is valid} \iff Q\ \text{is a manifest error}
$$

### SIL Inference Rules

**Hoare-style assignment (backward):**
$$
\langle\mathsf{Hoare}\rangle\quad \dfrac{}{\langle Q[a/x]\rangle\ x:=a\ \langle Q\rangle}
$$

**Assume/Guard (backward):**
$$
\langle\mathsf{assume}\rangle\quad \dfrac{}{\langle Q \land b\rangle\ b?\ \langle Q\rangle}
$$
Note: if $Q$ contradicts $b$, the precondition is empty (e.g., $\langle\emptyset\rangle\ (x>0)?\ \langle x = -42\rangle$).

**Choice (backward):**
$$
\langle\mathsf{choice}\rangle\quad \dfrac{\langle P_1\rangle\ c_1\ \langle Q\rangle \quad \langle P_2\rangle\ c_2\ \langle Q\rangle}{\langle P_1 \lor P_2\rangle\ c_1 + c_2\ \langle Q\rangle}
$$

**Iteration (backward):**
$$
\langle\mathsf{iter}\rangle\quad \dfrac{\forall n \ge 0.\ \langle Q_{n+1}\rangle\ c\ \langle Q_n\rangle}{\langle\exists k.\ Q_k\rangle\ c^{\star}\ \langle Q_0\rangle}
$$

**Empty/Cons' (dropping disjuncts):**
$$
\langle\mathsf{cons'}\rangle\quad \dfrac{\langle P\rangle\ c\ \langle Q\rangle}{\langle P \lor R\rangle\ c\ \langle Q\rangle}
$$

Note: this is the opposite of dropping in IL: in SIL we can enlarge the pre (since it is backward, a larger pre means more states that can reach the error).

### Soundness and Completeness

**Soundness:** All provable SIL triples are valid. Proof by induction on derivation.

**Completeness:** All valid SIL triples are provable (using core rules).

### SIL vs IL vs HL

Given specification $Q \triangleq \{z = 42\}$ for the program:

```
if even(x) {
    if odd(y) { z := 42; }
}
```

- **HL**: $\{z = 42\}\ c\ \{z = 42\}$ (trivial, doesn't rule out $z = 42$ already holding)
- **IL**: $[z = 11]\ c\ [z = 42 \land \mathsf{odd}(y) \land \mathsf{even}(x)]$ (postcondition is reachable)
- **SIL**: $\langle z = 11 \land \mathsf{odd}(y) \land \mathsf{even}(x)\rangle\ c\ \langle z = 42\rangle$ (precondition that leads to error)

### SIL vs HL for Deterministic Programs

If $c$ is deterministic and terminating, SIL is equivalent to HL:

$$
\langle P\rangle\ c\ \langle Q\rangle \iff \{P\}\ c\ \{Q\}
$$

### Unsoundness of $\langle\mathsf{conj}\rangle$ in SIL

The rule $\langle P_1\rangle\ c\ \langle Q_1\rangle,\ \langle P_2\rangle\ c\ \langle Q_2\rangle \vdash \langle P_1 \land P_2\rangle\ c\ \langle Q_1 \land Q_2\rangle$ is unsound.

Counterexample: $\langle x=0\rangle\ x:=1\ \langle x=0\rangle$ and $\langle x=0\rangle\ x:=1\ \langle x=1\rangle$ are both valid, but $\langle x=0\rangle\ x:=1\ \langle x=0 \land x=1\rangle = \langle x=0\rangle\ x:=1\ \langle\mathsf{false}\rangle$ is not valid.

### SIL Guard Axiom Exercise

Is $\langle P\rangle\ b?\ \langle P \land b\rangle$ valid? No. Counterexample: $\langle x \ge 0\rangle\ (x > 1)?\ \langle x \ge 2\rangle$ is not valid because $x = 0$ cannot reach $x \ge 2$.

### Taxonomy and Consequence Rules

| | Forward | Backward |
|:---|:---:|:---:|
| **Over** | HL: $\{P\}\ c\ \{Q\}$, $\llbracket c\rrbracket P \subseteq Q$ | NC: $(P)\ c\ (Q)$, $P \supseteq \llbracket c\rrbracket^{\mathsf{op}} Q$ |
| **Under** | IL: $[P]\ c\ [Q]$, $\llbracket c\rrbracket P \supseteq Q$ | SIL: $\langle P\rangle\ c\ \langle Q\rangle$, $P \subseteq \llbracket c\rrbracket^{\mathsf{op}} Q$ |

Consequence rules per logic:

- **HL**: $P \Rightarrow P',\ \{P'\}\ c\ \{Q'\},\ Q' \Rightarrow Q \vdash \{P\}\ c\ \{Q\}$ (strengthen pre, weaken post)
- **NC**: $P' \Rightarrow P,\ (P')\ c\ (Q'),\ Q \Rightarrow Q' \vdash (P)\ c\ (Q)$ (weaken pre, strengthen post)
- **IL**: $P' \Rightarrow P,\ [P']\ c\ [Q'],\ Q \Rightarrow Q' \vdash [P]\ c\ [Q]$ (weaken pre, strengthen post)
- **SIL**: $P \Rightarrow P',\ \langle P'\rangle\ c\ \langle Q'\rangle,\ Q' \Rightarrow Q \vdash \langle P\rangle\ c\ \langle Q\rangle$ (strengthen pre, weaken post)

<hr>


## Lecture 09 — Separation Logic

### Key Definitions

- **Heap model**: stack $(\sigma)$ + heap $(h)$
- **Separating conjunction**: $P \star Q$ — disjoint heap regions
- **Magic wand**: $P \mathrel{-\!\!*} Q$ — adjoint of $\star$

### Key Formulas

- Frame rule: $\{P\}\ c\ \{Q\} \vdash \{P \star R\}\ c\ \{Q \star R\}$

### Exam Checklist

- [ ] Can reason about heap-manipulating programs with SL
- [ ] Understands the frame rule and its soundness condition

### Heap Model

Stores: $s : X \to \mathbb{Z}$ (variables to values)
Heaps: $h : \mathbb{N} \rightharpoonup \mathbb{Z}_{\bot}$ (locations to values, $\bot = \mathsf{null} = -1$ for deallocated)
States: $\sigma = \langle s, h\rangle \in \Sigma \triangleq S \times H$

Domain of a heap: $\mathsf{dom}(h)$ is the set of defined locations.

**Disjoint heap composition**: $h_1 \# h_2 \iff \mathsf{dom}(h_1) \cap \mathsf{dom}(h_2) = \emptyset$
$h_1 \bullet h_2$ is the union of functions with disjoint domains (undefined if $\lnot(h_1 \# h_2)$).

Heap update: $h[x \mapsto n]$ is $h$ with $x$ mapped to $n$.

### Assertion Language

$$
P ::= \mathsf{true} \mid \mathsf{false} \mid a_1 < a_2 \mid a_1 = a_2 \mid \dots \quad\text{(pure assertions)}
\mid \lnot P \mid P_1 \land P_2 \mid \exists x.\ P \mid \dots
\mid \mathsf{emp} \mid a_1 \mapsto a_2 \mid P_1 \star P_2 \quad\text{(structural assertions)}
$$

Abbreviations:
$$
a \mapsto \_ \triangleq \exists v.\ a \mapsto v \quad\text{(for $v$ fresh)}
\qquad
a_1 \doteq a_2 \triangleq (a_1 = a_2) \land \mathsf{emp}
$$
$$
a \mapsto \langle a_0,\dots,a_k\rangle \triangleq (a \mapsto a_0) \star \dots \star (a + k \mapsto a_k)
$$

### Satisfaction Relation

$\langle s, h\rangle \models P$ means the assertion holds for state $\langle s, h\rangle$.

Classical:

- $\langle s, h\rangle \models a_1 < a_2$ iff $s \models a_1 < a_2$ (heap irrelevant)
- $\langle s, h\rangle \models P_1 \land P_2$ iff $\langle s, h\rangle \models P_1$ and $\langle s, h\rangle \models P_2$
- $\langle s, h\rangle \models \forall x.\ P$ iff $\forall v \in \mathbb{Z}.\ \langle s[x \mapsto v], h\rangle \models P$

Structural:

- $\langle s, h\rangle \models a_1 \mapsto a_2$ iff $\mathsf{dom}(h) = \{\llbracket a_1\rrbracket s\}$ and $h(\llbracket a_1\rrbracket s) = \llbracket a_2\rrbracket s$
- $\langle s, h\rangle \models \mathsf{emp}$ iff $h$ is the empty map
- $\langle s, h\rangle \models P_1 \star P_2$ iff $\exists h_1, h_2.\ \langle s, h_1\rangle \models P_1$ and $\langle s, h_2\rangle \models P_2$ and $h = h_1 \bullet h_2$

### Properties of $\star$

- $x \mapsto v \star y \mapsto w \not\Rightarrow x \mapsto v$ (separating conjunction requires disjoint heaps)
- $x \mapsto v \land y \mapsto w \Rightarrow x \mapsto v$ (classical conjunction is weaker)
- $x \mapsto v \star x \mapsto w \equiv \mathsf{false}$ (a cell cannot be split)
- $(x = y) \star (x = y) \equiv (x = y)$ (pure assertions are duplicable)
- $P \star \mathsf{emp} \equiv P$ (empty heap is unit of $\star$)

### Small/Local Axioms

**Write:**
$$
\{\mathsf{write}\}\quad \dfrac{}{\{a_1 \mapsto \_\}\ [a_1] := a_2\ \{a_1 \mapsto a_2\}}
$$

**Read:**
$$
\{\mathsf{read}\}\quad \dfrac{}{\{y \mapsto v\}\ x := [y]\ \{x = v \land y \mapsto v\}}
$$

**Allocation:**
$$
\{\mathsf{alloc}\}\quad \dfrac{}{\{\mathsf{emp}\}\ x := \mathsf{alloc}()\ \{x \mapsto \_\}}
$$
$$
\{\mathsf{cons}\}\quad \dfrac{}{\{x \doteq x'\}\ x := \mathsf{cons}(a_1,\dots,a_k)\ \{x \mapsto \langle a_1[x'/x],\dots,a_k[x'/x]\rangle\}}
$$

**Dispose:**
$$
\{\mathsf{dispose}\}\quad \dfrac{}{\{a \mapsto \_\}\ \mathsf{free}(a)\ \{\mathsf{emp}\}}
$$

### Frame Rule

$$
\{\mathsf{frame}\}\quad \dfrac{\{P\}\ c\ \{Q\}}{\{P \star R\}\ c\ \{Q \star R\}}
$$

Side condition: $\mathsf{mod}(c) \cap \mathsf{fv}(R) = \emptyset$ (variables modified by $c$ are disjoint from free variables in $R$).

The frame rule enables **local reasoning**: the specification can concentrate on accessed cells; other cells remain unchanged.

### Footprint Recipe

1. Derive the specification of $c$ using local axioms.

2. Apply the frame rule to extend the specification with idle resources.

Example:
$$
\dfrac{\{x \mapsto \_\}\ [x] := 1\ \{x \mapsto 1\}}{\{x \mapsto \_ \star R\}\ [x] := 1\ \{x \mapsto 1 \star R\}}
$$
with $R \equiv (y \mapsto \_ \star z \mapsto \_)$.

### Inductive Predicates for Lists

Precise list segment $\mathsf{ls}(a_1, a_2)$:

$$
\mathsf{ls}(a_1, a_2) \triangleq (a_1 = a_2 \land \mathsf{emp}) \lor (a_1 \ne a_2 \land \exists\ell.\ a_1 \mapsto \ell \star \mathsf{ls}(\ell, a_2))
$$

Full list: $\mathsf{list}(a) \triangleq \mathsf{ls}(a, \mathsf{nil})$.

Imprecise list segment $\mathsf{ils}(a_1, a_2)$:

$$
\mathsf{ils}(a_1, a_2) \triangleq (a_1 = a_2 \land \mathsf{emp}) \lor (\exists v.\ a_1 \mapsto v \star \mathsf{ils}(v, a_2))
$$

$\mathsf{ils}(a_1, a_2) \not\equiv \mathsf{ls}(a_1, a_2)$. For example, $\mathsf{ils}(42, 42)$ is satisfied by $\mathsf{dom}(h) = \{42\},\ h(42) = 42$, but $\mathsf{ls}(42, 42)$ requires $\mathsf{emp}$ for the $a_1 = a_2$ case.

### List Reversal Example

Full invariant for in-place list reversal:

$$
\mathsf{inv} \triangleq \exists\alpha,\beta.\ \mathsf{ls}(\alpha, p) \star \mathsf{ls}(\beta, q) \land \alpha_0 = \alpha^{\dagger} \cdot \beta
$$

where $\alpha^{\dagger}$ is the reverse of $\alpha$, and $\alpha_0$ is the original list. The separating conjunction $\star$ ensures the two list segments are disjoint. The inductive reachability predicate prevents overlap:

$$
(p, q) \triangleq p = q \lor \exists v, t.\ p \mapsto \langle v, t\rangle \land (t, q)
$$

The invariant ensures $p$ points to the remaining fragment and $q$ to the already reversed fragment.

### Correctness Theorem

**Theorem.** If $\{P\}\ c\ \{Q\}$ is provable in SL, then $\llbracket c\rrbracket P \subseteq Q$.

Proof by induction on the derivation. The key lemma is the frame property: if $\{P\}\ c\ \{Q\}$ holds for a local specification, extending with $\star R$ preserves correctness because $c$ does not touch cells in $R$.

### Incompleteness and the Footprint Theorem

**Theorem (Incompleteness).** There exist valid SL triples that are not provable.

The issue is the **footprint** — the frame rule can be too weak when allocation produces a location that aliases with the frame. For example:

$$
\{y \mapsto \_\}\ x := \mathsf{alloc}(); \mathsf{free}(x)\ \{y \mapsto \_ \land y \ne x\}
$$

should be valid but cannot be derived in basic SL because the information that $x$ is fresh is lost after $\mathsf{free}(x)$.

### Satisfaction Exercises

**Exercise 1:** Find a state satisfying $(x \doteq y) \star x \mapsto y$.
Answer: $x = y$, $\mathsf{dom}(h) = \{s(x)\}$, $h(s(x)) = s(y)$. Since $x \doteq y$ is pure, $\star$ requires no heap from it.

**Exercise 2:** Show a state satisfying $(x \mapsto y) \star \lnot(x \mapsto y)$.
Answer: $\mathsf{dom}(h) = \{11\}$, $s(x) = 11$, $h(11) = 42$, $s(y) = 42$. Split $h$ into two parts: $h_1$ with $\mathsf{dom}(h_1) = \{11\}$ gives $x \mapsto y$, $h_2$ empty gives $\lnot(x \mapsto y)$.

<hr>


## Lecture 10 — ISL and SepSIL

### Key Concepts

- ISL: under-approximate reasoning + separation logic
- SepSIL: symbolic execution with separation logic for bug finding

### Exam Checklist

- [ ] Knowledge of ISL triple structure

### ISL Definition

ISL (Incorrectness Separation Logic) combines IL (under-approximate bug finding) with SL (local heap reasoning).

$$
[P]\ c\ [\epsilon : Q]
$$

ISL adds the frame rule for separation logic to IL:

$$
[\mathsf{frame}]\quad \dfrac{[P]\ c\ [\epsilon : Q]}{[P \star R]\ c\ [\epsilon : Q \star R]}
$$

Side condition: $\mathsf{mod}(c) \cap \mathsf{fv}(R) = \emptyset$.

### ISL Regular Commands

Atomic commands with heap operations:

$$
e ::= \mathsf{skip} \mid b? \mid x := a \mid x := [y]\ \text{(read)} \mid [x] := y\ \text{(write)} \mid x := \mathsf{alloc}() \mid \mathsf{free}(x) \mid \mathsf{error}()
$$

### ISL Local Axioms with Error Tracking

**Write:**
$$
[x \mapsto v]\ [x] := y\ [\mathsf{ok} : x \mapsto y]
\qquad
[x = \mathsf{nil}]\ [x] := y\ [\mathsf{er} : x = \mathsf{nil}]
$$

**Read:**
$$
[y \mapsto v]\ x := [y]\ [\mathsf{ok} : x = v \land y \mapsto v]
\qquad
[y = \mathsf{nil}]\ x := [y]\ [\mathsf{er} : y = \mathsf{nil}]
$$

**Allocation:**
$$
[x \doteq x']\ x := \mathsf{alloc}()\ [\mathsf{ok} : x \mapsto \_]
$$

**Dispose (first try, problematic):**
$$
[x \mapsto v]\ \mathsf{free}(x)\ [\mathsf{ok} : \mathsf{emp}]
\qquad
[x = \mathsf{nil}]\ \mathsf{free}(x)\ [\mathsf{er} : x = \mathsf{nil}]
$$

### Unsound Frame Rule with Free

The frame rule with the simple dispose axiom is **unsound**:

$$
\dfrac{[x \mapsto v]\ \mathsf{free}(x)\ [\mathsf{ok} : \mathsf{emp}]}{[x \mapsto v \star x \mapsto v]\ \mathsf{free}(x)\ [\mathsf{ok} : \mathsf{emp} \star x \mapsto v]}
$$

By [cons]: $[\mathsf{false}]\ \mathsf{free}(x)\ [\mathsf{ok} : x \mapsto v]$. The only sound under-approximation from an inconsistent pre is false.

### Solution: The $\mathsf{x} /\!\!\mapsto$ Predicate

Add $x /\!\!\mapsto$ to the assertion language to track deallocated locations:

- $\langle s, h\rangle \models x /\!\!\mapsto$ iff $\mathsf{dom}(h) = \{s(x)\}$ and $h(s(x)) = \bot$
- $x /\!\!\mapsto$ records that location $x$ has been freed

Properties:

- $x \mapsto v \star x /\!\!\mapsto \equiv \mathsf{false}$ (cannot be both allocated and deallocated)
- $x /\!\!\mapsto \star x /\!\!\mapsto \equiv \mathsf{false}$ (a cell cannot be doubly deallocated)
- $y \mapsto v \star x /\!\!\mapsto \equiv y \mapsto v \star x /\!\!\mapsto \land x \ne y$ (free and alloc on different cells)

### Corrected Local Axioms with $x /\!\!\mapsto$

**Dispose (corrected):**
$$
[x \mapsto v]\ \mathsf{free}(x)\ [\mathsf{ok} : x /\!\!\mapsto]
\qquad
[x = \mathsf{nil}]\ \mathsf{free}(x)\ [\mathsf{er} : x = \mathsf{nil}]
$$

Now resources cannot shrink: $x \mapsto v$ is replaced by $x /\!\!\mapsto$, preserving the footprint.

**Additional error axioms (use-after-free, double-free):**
$$
[x /\!\!\mapsto]\ [x] := y\ [\mathsf{er} : x /\!\!\mapsto]
\qquad
[y /\!\!\mapsto]\ x := [y]\ [\mathsf{er} : y /\!\!\mapsto]
$$
$$
[x /\!\!\mapsto]\ \mathsf{free}(x)\ [\mathsf{er} : x /\!\!\mapsto]
\qquad
[y /\!\!\mapsto]\ x := \mathsf{alloc}()\ [\mathsf{ok} : x \mapsto v \land x = y]
$$

### Full ISL Inference Rules

**Skip:**
$$
[\mathsf{Skip}]\quad \dfrac{}{[\mathsf{emp}]\ \mathsf{skip}\ [\mathsf{ok} : \mathsf{emp}]}
$$

**Assign:**
$$
[\mathsf{Assign}]\quad \dfrac{}{[x = x']\ x := e\ [\mathsf{ok} : x = e[x'/x]]}
$$

**Assume:**
$$
[\mathsf{Assume}]\quad \dfrac{}{[\mathsf{emp}]\ \mathsf{assume}(B)\ [\mathsf{ok} : B]}
$$

**Seq1 (error short circuit):**
$$
[\mathsf{Seq1}]\quad \dfrac{[P]\ C_1\ [\mathsf{er}(l) : Q]}{[P]\ C_1;C_2\ [\mathsf{er}(l) : Q]}
$$

**Seq2:**
$$
[\mathsf{Seq2}]\quad \dfrac{[P]\ C_1\ [\mathsf{ok} : R]\quad [R]\ C_2\ [\epsilon : Q]}{[P]\ C_1;C_2\ [\epsilon : Q]}
$$

**Choice:**
$$
[\mathsf{Choice}]\quad \dfrac{[P]\ C_i\ [\epsilon : Q]\ \text{(for some $i \in \{1,2\}$)}}{[P]\ C_1 + C_2\ [\epsilon : Q]}
$$

**Error:**
$$
[\mathsf{Error}]\quad \dfrac{}{[\mathsf{emp}]\ l:\mathsf{error}\ [\mathsf{er}(l) : \mathsf{emp}]}
$$

**Loop1 (zero iterations):**
$$
[\mathsf{Loop1}]\quad \dfrac{}{[P]\ C^{\star}\ [\mathsf{ok} : P]}
$$

**Loop2 (unroll):**
$$
[\mathsf{Loop2}]\quad \dfrac{[P]\ C^{\star};C\ [\epsilon : Q]}{[P]\ C^{\star}\ [\epsilon : Q]}
$$

**Disj:**
$$
[\mathsf{Disj}]\quad \dfrac{[P_1]\ C\ [\epsilon : Q_1]\quad [P_2]\ C\ [\epsilon : Q_2]}{[P_1 \lor P_2]\ C\ [\epsilon : Q_1 \lor Q_2]}
$$

**Cons (reversed consequence):**
$$
[\mathsf{Cons}]\quad \dfrac{P' \Rightarrow P \quad [P]\ C\ [\epsilon : Q]\quad Q \Rightarrow Q'}{[P']\ C\ [\epsilon : Q']}
$$

**Havoc:**
$$
[\mathsf{Havoc}]\quad \dfrac{}{[x = x']\ x := \star\ [\mathsf{ok} : x = v]}
$$

**Local:**
$$
[\mathsf{Local}]\quad \dfrac{[P]\ C\ [\epsilon : Q]}{[\exists x.\ P]\ \mathsf{local}\ x\ \mathsf{in}\ C\ [\epsilon : \exists x.\ Q]}
$$

**Exists:**
$$
[\mathsf{Exists}]\quad \dfrac{[P]\ C\ [\epsilon : Q]}{[\exists x.\ P]\ C\ [\epsilon : \exists x.\ Q]}
$$

**Subst:**
$$
[\mathsf{Subst}]\quad \dfrac{[P]\ C\ [\epsilon : Q]}{[P[y/x]]\ C[y/x]\ [\epsilon : Q[y/x]]}
$$

**Alloc1:**
$$
[\mathsf{Alloc1}]\quad \dfrac{}{[x = x']\ x := \mathsf{alloc}()\ [\mathsf{ok} : x \mapsto \_]}
$$

**Alloc2:**
$$
[\mathsf{Alloc2}]\quad \dfrac{}{[x = x' \star y /\!\!\mapsto]\ x := \mathsf{alloc}()\ [\mathsf{ok} : x = y \star y \mapsto \_]}
$$

**Free:**
$$
[\mathsf{Free}]\quad \dfrac{}{[x \mapsto e]\ l:\mathsf{free}(x)\ [\mathsf{ok} : x /\!\!\mapsto]}
$$

**FreeEr:**
$$
[\mathsf{FreeEr}]\quad \dfrac{}{[x /\!\!\mapsto]\ l:\mathsf{free}(x)\ [\mathsf{er}(l) : x /\!\!\mapsto]}
$$

**FreeNull:**
$$
[\mathsf{FreeNull}]\quad \dfrac{}{[x = \mathsf{null}]\ l:\mathsf{free}(x)\ [\mathsf{er}(l) : x = \mathsf{null}]}
$$

**Load:**
$$
[\mathsf{Load}]\quad \dfrac{}{[x = x' \star y \mapsto e]\ l:x := [y]\ [\mathsf{ok} : x = e[x'/x] \star y \mapsto e[x'/x]]}
$$

**LoadEr:**
$$
[\mathsf{LoadEr}]\quad \dfrac{}{[y /\!\!\mapsto]\ l:x := [y]\ [\mathsf{er}(l) : y /\!\!\mapsto]}
$$

**LoadNull:**
$$
[\mathsf{LoadNull}]\quad \dfrac{}{[y = \mathsf{null}]\ l:x := [y]\ [\mathsf{er}(l) : y = \mathsf{null}]}
$$

**Store:**
$$
[\mathsf{Store}]\quad \dfrac{}{[x \mapsto e]\ l:[x] := y\ [\mathsf{ok} : x \mapsto y]}
$$

**StoreEr:**
$$
[\mathsf{StoreEr}]\quad \dfrac{}{[x /\!\!\mapsto]\ l:[x] := y\ [\mathsf{er}(l) : x /\!\!\mapsto]}
$$

**StoreNull:**
$$
[\mathsf{StoreNull}]\quad \dfrac{}{[x = \mathsf{null}]\ l:[x] := y\ [\mathsf{er}(l) : x = \mathsf{null}]}
$$

**Frame:**
$$
[\mathsf{Frame}]\quad \dfrac{[P]\ C\ [\epsilon : Q]}{[P \star R]\ C\ [\epsilon : Q \star R]}
$$

### ISL Relational Semantics

$$
\llbracket\mathsf{skip}\rrbracket_{\mathsf{ok}} \triangleq \{(\sigma,\sigma)\}
\qquad
\llbracket\mathsf{skip}\rrbracket_{\mathsf{er}} \triangleq \emptyset
$$
$$
\llbracket b?\rrbracket_{\mathsf{ok}} \triangleq \{(\sigma,\sigma) \mid \sigma = \langle s,h\rangle \land s \models b\}
$$
$$
\llbracket\mathsf{error}()\rrbracket_{\mathsf{ok}} \triangleq \emptyset
\qquad
\llbracket\mathsf{error}()\rrbracket_{\mathsf{er}} \triangleq \{(\sigma,\sigma)\}
$$
$$
\llbracket x := [y]\rrbracket_{\mathsf{ok}} \triangleq \{(\langle s,h\rangle, \langle s[x \mapsto v], h\rangle) \mid v = h(s(y)) \in \mathbb{Z}\}
$$
$$
\llbracket x := [y]\rrbracket_{\mathsf{er}} \triangleq \{(\langle s,h\rangle, \langle s,h\rangle) \mid s(y) = \mathsf{nil} \lor h(s(y)) = \bot\}
$$
$$
\llbracket [x] := y\rrbracket_{\mathsf{ok}} \triangleq \{(\langle s,h\rangle, \langle s,h[s(x) \mapsto s(y)]\rangle) \mid h(s(x)) \in \mathbb{Z}\}
$$
$$
\llbracket [x] := y\rrbracket_{\mathsf{er}} \triangleq \{(\langle s,h\rangle, \langle s,h\rangle) \mid s(x) = \mathsf{nil} \lor h(s(x)) = \bot\}
$$
$$
\llbracket x := \mathsf{alloc}()\rrbracket_{\mathsf{ok}} \triangleq \{(\langle s,h\rangle, \langle s[x \mapsto n], h[n \mapsto v]\rangle) \mid v \in \mathbb{Z} \land (n \notin \mathsf{dom}(h) \lor h(n) = \bot)\}
$$
$$
\llbracket \mathsf{free}(x)\rrbracket_{\mathsf{ok}} \triangleq \{(\langle s, h \bullet [s(x) \mapsto v]\rangle, \langle s, h \bullet [s(x) \mapsto \bot]\rangle) \mid s(x) \in \mathbb{N} \land v \in \mathbb{Z}\}
$$
$$
\llbracket \mathsf{free}(x)\rrbracket_{\mathsf{er}} \triangleq \{(\langle s,h\rangle, \langle s,h\rangle) \mid s(x) = \mathsf{nil} \lor h(s(x)) = \bot\}
$$

### Footprint Holds in ISL

The footprint that failed in SL is now derivable in ISL:

$$
\dfrac{[\mathsf{emp}]\ x := \mathsf{alloc}()\ [\mathsf{ok} : x \mapsto v] \qquad [x \mapsto v]\ \mathsf{free}(x)\ [\mathsf{ok} : x /\!\!\mapsto]}{[y \mapsto \_ \star \mathsf{emp}]\ x := \mathsf{alloc}(); \mathsf{free}(x)\ [\mathsf{ok} : y \mapsto \_ \star x /\!\!\mapsto]}
$$

using [seq], [frame], [cons] to obtain $[y \mapsto \_]\ x := \mathsf{alloc}(); \mathsf{free}(x)\ [\mathsf{ok} : y \mapsto \_ \land y \ne x]$.

### ISL Correctness Theorem

**Theorem.** If $[P]\ c\ [\epsilon : Q]$ is provable, then $Q \subseteq \llbracket c\rrbracket_{\epsilon}(P)$.

Proof by induction on the derivation.

**Theorem (Footprint).** Any valid ISL triple $[\sigma_P]\ c\ [\epsilon : \sigma_Q]$ can be derived (relative completeness). See CAV 2020 paper for details.

### SepSIL Definition

SepSIL (Separation SIL) combines SIL (backward under-approximation) with SL (separation logic):

$$
\langle P\rangle\ c\ \langle Q\rangle
$$

SepSIL extends SIL with the frame rule for separation logic:

$$
\langle\mathsf{frame}\rangle\quad \dfrac{\langle P\rangle\ c\ \langle Q\rangle}{\langle P \star R\rangle\ c\ \langle Q \star R\rangle}
$$

### SepSIL Local Axioms

**Write:** $\langle x \mapsto \_\rangle\ [x] := y\ \langle x \mapsto y\rangle$

**Read:** $\langle y \mapsto v \land (v = x')\rangle\ x := [y]\ \langle y \mapsto v \land (x = x')\rangle$

**Allocation:** $\langle\mathsf{emp}\rangle\ x := \mathsf{alloc}()\ \langle x \mapsto \_\rangle$

**Dispose:** $\langle x \mapsto \_\rangle\ \mathsf{free}(x)\ \langle x /\!\!\mapsto\rangle$

### SepSIL Correctness and Completeness

**Theorem (Correctness).** If $\langle P\rangle\ c\ \langle Q\rangle$ is provable, then $P \subseteq \llbracket c\rrbracket^{\mathsf{op}} Q$.

**Theorem (Completeness).** Any valid SepSIL triple $\langle P\rangle\ c\ \langle Q\rangle$ can be derived. See OOPSLA 2025 paper.

### ISL vs SepSIL

| ISL | SepSIL |
|:---|:---:|
| Forward under-approximation | Backward under-approximation |
| $[P]\ c\ [\epsilon : Q]$, $Q \subseteq \llbracket c\rrbracket_{\epsilon} P$ | $\langle P\rangle\ c\ \langle Q\rangle$, $P \subseteq \llbracket c\rrbracket^{\mathsf{op}} Q$ |
| Finds reachable error states | Finds initial states leading to errors |
| Stronger guarantees for postconditions | More succinct postconditions |
| Frame rule $[P \star R]\ c\ [Q \star R]$ | Frame rule $\langle P \star R\rangle\ c\ \langle Q \star R\rangle$ |

<hr>


## Lecture 11 — Abstract Interpretation: Basic Ideas

### Key Definitions

- **Abstract interpretation**: framework for designing sound static analyses
- **Abstraction**: selecting a property of interest
- **Concretization**: $\gamma(a)$ — set of states satisfying $a$
- **Best abstraction**: most precise over-approximation

### Key Formulas

- Compositionality: $\llbracket c_1; c_2\rrbracket^\# = \llbracket c_2\rrbracket^\# \circ \llbracket c_1\rrbracket^\#$
- Choice: $\llbracket c_1 + c_2\rrbracket^\# = \llbracket c_1\rrbracket^\# \sqcup \llbracket c_2\rrbracket^\#$

### Geometric Abstraction Examples

The concrete domain for 2D points is $\wp(\mathbb{R}^2)$. Program commands operate on points $(x,y)$:

- **init(R):** nondeterministically picks a state in region $R$
- **translate(u,v):** $(x,y) \mapsto (x+u, y+v)$
- **rotate(u,v,$\theta$):** rotate by angle $\theta$ around center $(u,v)$
- **Sequence:** $p_1; p_2$
- **Choice:** $\{p_1\}$ or $\{p_2\}$
- **Iteration:** $\texttt{iter}\{p\}$

### Concretization Visualizations

Each abstract element $a$ denotes a set $\gamma(a)$ of concrete states:

**Signs abstraction:**
$$
\gamma([x \le 0, y \ge 0]) = \{(x,y) \mid x \le 0, y \ge 0\}
$$

**Intervals abstraction:**
$$
\gamma([1 \le x \le 4,\ 1 \le y \le 3]) = \{(x,y) \mid 1 \le x \le 4,\ 1 \le y \le 3\}
$$

**Convex Polyhedra abstraction:**
$$
\gamma(c_1 x + c_2 y \le c) = \{(x,y) \mid c_1 x + c_2 y \le c\}
$$

### Convex Polyhedra Abstraction

Abstract elements are conjunctions of linear inequality constraints:
$$
c_1 x + c_2 y \le c
$$

- More expressive than intervals (any interval is also a convex polyhedron)
- Relational: captures dependencies between variables (e.g., $x \le y$)
- No best abstraction always exists (e.g., for non-convex shapes like discs)
- Used when intervals are insufficiently precise

### Best Abstraction

An abstract element $a$ is the **best abstraction** of a set of points $S$ iff:

1. **Over-approximation:** $S \subseteq \gamma(a)$
2. **Most precise:** $\forall b.\ S \subseteq \gamma(b) \implies \gamma(a) \subseteq \gamma(b)$

The best abstraction exists only when the abstract domain is closed under meets (Moore family).

### Abstract Semantics Compositionality

**Analysis function:** $\texttt{analysis}(p, a)$ maps an abstract pre-state to an abstract post-state.

For atomic commands:

- $\texttt{analysis}(\texttt{init}(R), a)$ = best abstraction of $R$
- $\texttt{analysis}(\texttt{translate}(u,v), a)$ = abstraction containing $\gamma(a)$ translated by $(u,v)$
- $\texttt{analysis}(\texttt{rotate}(u,v,\theta), a)$ = abstraction containing $\gamma(a)$ rotated

For compound commands:

- **Sequence:** $\texttt{analysis}(p_0; p_1, a) = \texttt{analysis}(p_1, \texttt{analysis}(p_0, a))$
- **Choice:** $\texttt{analysis}(\{p_0\}\ \texttt{or}\ \{p_1\}, a) = \texttt{analysis}(p_0, a) \sqcup \texttt{analysis}(p_1, a)$
- **Iteration:** fixpoint computation: $R_0 = a$, $R_{k+1} = R_k \sqcup \texttt{analysis}(p, R_k)$ until stabilization

### Compositionality Principle

Compute a sound analysis of a program by computing sound abstract semantics of the program's components:
$$
\llbracket c_1; c_2\rrbracket^\# = \llbracket c_2\rrbracket^\# \circ \llbracket c_1\rrbracket^\#
\qquad
\llbracket c_1 + c_2\rrbracket^\# = \llbracket c_1\rrbracket^\# \sqcup \llbracket c_2\rrbracket^\#
$$
$$
\llbracket c^\star\rrbracket^\# = \operatorname{lfp}^\#\ \lambda X.\ \llbracket c\rrbracket^\#(X) \sqcup \text{initial}
$$

### Common Mistakes

- Thinking abstraction = omission (it's selection)
- Forgetting that soundness is the opposite for bug-finding

### Exam Checklist

- [ ] Understands the abstraction-concretization paradigm
- [ ] Knows the soundness diagram
- [ ] Can explain why Rice's Theorem forces approximation

<hr>


## Lecture 12 — Abstract Interpretation: Formal Foundations

### Key Definitions

- **Galois connection**: $(\alpha, \gamma)$ with $\alpha(c) \sqsubseteq a \iff c \subseteq \gamma(a)$
- **Complete lattice**: $(L, \sqsubseteq, \bot, \top, \sqcup, \sqcap)$
- **Soundness**: $\alpha \circ \llbracket c\rrbracket \sqsubseteq \llbracket c\rrbracket^\# \circ \alpha$

### Key Formulas

- F-06 (Galois connection), F-07 (soundness)
- Sign domain operations (F-17)

### Factorial Example: Full Sign Analysis

Program computing $k!$ (factorial of initial $n$):

```
(1) m := 1;
(2) while n > 0 do {
(3)     m := m * n;
(4)     n := n - 1
(5=2) }
(6) // end
```

**CFG:**
```
(1) m := 1  -->  (2=5)
                   |
              [n > 0]? --yes--> (3) m := m*n --> (4) n := n-1 --> (2=5)
                   |
              [n <= 0]? --yes--> (6) end
```

**Sign analysis with domain $A = \{\emptyset, \mathbb{Z}_{<0}, \mathbb{Z}_{>0}, \mathbb{Z}\}$:**

At each program point, abstract state is a pair $(m, n) \in A \times A$:

| Point | Abstract State |
|-------|---------------|
| (1)   | $m = \mathbb{Z},\ n = \mathbb{Z}$ |
| (2=5) | $m = \mathbb{Z}_{>0},\ n = \mathbb{Z}$ |
| (3)   | $m = \mathbb{Z}_{>0},\ n = \mathbb{Z}_{>0}$ |
| (4)   | $m = \mathbb{Z}_{>0},\ n = \mathbb{Z}_{>0}$ |
| (5=2) | $m = \mathbb{Z}_{>0},\ n = \mathbb{Z}$ |
| (6)   | $m = \mathbb{Z}_{>0},\ n = \mathbb{Z}_{\le 0}$ |

**Abstract transfer functions:**

- $F_2^\#(m,n) = (\mathbb{Z}_{>0}, n)$ (assignment $m := 1$)
- $F_4^\#(m,n) = (m \times^\# n, n)$ with $\mathbb{Z}_{>0} \times^\# \mathbb{Z}_{>0} = \mathbb{Z}_{>0}$
- $F_5^\#(m,n) = (m,\ n -^\# 1)$ with $\mathbb{Z}_{>0} -^\# 1 = \mathbb{Z}$
- $F_7^\#(m,n) = (m,n)$ (guard $n \le 0$)
- $F_3^\#(m,n) = (m,n)$ if $n = \mathbb{Z}_{>0}$, else $(\bot, \bot)$ (guard $n > 0$)

### Precision Loss Demonstration

For the variant with guard $n > 1$:
```
(1) m := 1;
(2) while n > 1 do {
(3)     m := m * n;
(4)     n := n - 1
(5=2) }
(6) // end
```
With input $\{n > 0\}$:

- At (6): $n = \mathbb{Z}$ (precision loss — we cannot infer $n \le 1$ because $n$ may enter the loop with value 1)
- The sign domain cannot distinguish $n = 1$ from $n > 1$ after the loop

### Domain Refinement Sequence

**Basic sign domain** $A_1 = \{\emptyset, \mathbb{Z}_{<0}, \mathbb{Z}_{>0}, \mathbb{Z}\}$:

```
           ℤ
         /   \
      ℤ<0   ℤ>0
         \   /
           ∅
```

**Refined sign domain** $A_2$ adding $\mathbb{Z}_{\ge 0}$ and $\mathbb{Z}_{\le 0}$:
```
           ℤ
        /      \
    ℤ≤0       ℤ≥0
    /  \      /  \
 ℤ<0   ℤ=0  ℤ=0 ℤ>0
    \   |    |   /
         ∅
```

**Further refined** $A_3$ adding $\mathbb{Z}_{=0}$:
```
           ℤ
        /      \
    ℤ≤0       ℤ≥0
    /  \      /  \
 ℤ<0  ℤ=0  ℤ=0 ℤ>0
    \   |    |   /
         ∅
```

**CFG for refined domain $A_2$:**
```
(1) m := 1 → [m=ℤ>0, n=ℤ]
                |
           (2=5) [m=ℤ>0, n=ℤ]
              /         \
    [n > 0]?           [n ≤ 0]?
        |                   |
   (3) m:=m*n          (6) end
    [m=ℤ>0, n=ℤ>0]    [m=ℤ>0, n=ℤ≤0]
        |
   (4) n:=n-1
    [m=ℤ>0, n=ℤ≥0]
        |
      (2=5)
```

With $A_3$, the loop invariant for the factorial program with guard $n > 0$ becomes:

- At (6): $n = \mathbb{Z}_{=0},\ m = \mathbb{Z}_{>0}$ (maximum precision!)

### Key Algorithms

- Kleene fixpoint iteration (A-01)

### Common Mistakes

- Forgetting monotonicity of $\alpha$ and $\gamma$
- Confusing $\sqsubseteq$ direction in soundness condition

### Exam Checklist

- [ ] Can define a Galois connection
- [ ] Can prove soundness of abstract operations
- [ ] Knows the Sign domain operations tables

<hr>


## Lecture 13 — Galois Connections (Advanced)

### Key Definitions

- **Galois insertion**: $\alpha \circ \gamma = \text{id}$ (no redundancy)
- **Closure operator**: monotone, extensive, idempotent
- $\alpha$ preserves joins, $\gamma$ preserves meets

### Key Formulas

- F-06, F-10 (insertion)
- $\alpha(\bigsqcup X) = \bigsqcup \alpha(X)$
- $\gamma(\bigsqcap Y) = \bigsqcap \gamma(Y)$

### Order Theory Foundations

**Partially ordered set (poset):** $(P, \sqsubseteq)$ with reflexive, antisymmetric, transitive $\sqsubseteq$.

**Join (lub):** $x \sqcup y$ is the least upper bound of $x$ and $y$ (if exists).
**Meet (glb):** $x \sqcap y$ is the greatest lower bound of $x$ and $y$ (if exists).

**Chain:** a totally ordered subset $x_1 \sqsubseteq x_2 \sqsubseteq \dots$

**Complete partial order (CPO):** every chain has a lub.

**Ascending Chain Condition (ACC):** every ascending chain stabilizes: $x_1 \sqsubseteq x_2 \sqsubseteq \dots \implies \exists k.\ x_k = x_{k+1} = \dots$

**Finite height:** the longest chain has finite length.

### Complete Lattices

A **complete lattice** $(L, \sqsubseteq, \bot, \top, \sqcup, \sqcap)$:

- $\bot$: least element
- $\top$: greatest element
- Every subset $X \subseteq L$ has a lub $\bigsqcup X$ and glb $\bigsqcap X$

**Examples of complete lattices:**

1. **Powerset lattice** $(\wp(S), \subseteq, \emptyset, S, \cup, \cap)$ — always complete
2. **Interval lattice** extended: $[a,b]$ with $a \in \mathbb{Z} \cup \{-\infty\}$, $b \in \mathbb{Z} \cup \{+\infty\}$, $a \le b$, plus $\bot$ — complete
3. **Sign domain** $(\{\emptyset, \mathbb{Z}_{<0}, \mathbb{Z}_{=0}, \mathbb{Z}_{>0}, \mathbb{Z}_{\le 0}, \mathbb{Z}_{\ge 0}, \mathbb{Z}\}, \sqsubseteq)$ — complete (finite lattice)
4. **Divisibility lattice** $(\mathbb{N}^+, \mid, 1, 0, \gcd, \operatorname{lcm})$ — complete where $\gcd$ is meet and $\operatorname{lcm}$ is join
5. **Linear inequalities** (convex polyhedra) — complete lattice with $\sqsubseteq$ as reverse inclusion

**Tarski Fixpoint Theorem:** For a monotone function $F: L \to L$ on a complete lattice:

- $\operatorname{lfp}(F) = \bigsqcap\{x \mid F(x) \sqsubseteq x\}$ (least fixpoint)
- $\operatorname{gfp}(F) = \bigsqcup\{x \mid x \sqsubseteq F(x)\}$ (greatest fixpoint)
- The set of fixpoints is itself a complete lattice

### Moore Families and Closure

A **Moore family** is a set $M \subseteq \wp(\Sigma)$ closed under arbitrary intersections:
$$
\forall \mathcal{X} \subseteq M.\ \bigcap_{X \in \mathcal{X}} X \in M
$$

- Every Moore family forms a complete lattice (with $\bigsqcap = \cap$, $\bigsqcup$ as the Moore-closure of $\cup$)
- The image of a Galois connection's concretization is always a Moore family

A **closure operator** $\rho: \wp(\Sigma) \to \wp(\Sigma)$ satisfies:

1. **Monotone:** $X \subseteq Y \implies \rho(X) \subseteq \rho(Y)$
2. **Extensive:** $X \subseteq \rho(X)$
3. **Idempotent:** $\rho(\rho(X)) = \rho(X)$

The set of closed elements $\{X \mid \rho(X) = X\}$ forms a Moore family.

### Chain Conditions Summary

| Domain | ACC? | Finite Height? | Widening Needed? |
|:---|---|:---:|:---:|
| Sign (finite) | Yes | Yes | No |
| Intervals (extended) | No | No | Yes |
| Congruence | No (infinite) | No | Yes |
| Convex Polyhedra | No | No | Yes |
| Powerset of finite set | Yes | Yes | No |
| Constant propagation | Yes ($\mathbb{Z} \cup \{\top\}$) | No (infinite $\mathbb{Z}$) | No (but uses $\top$) |

### Common Mistakes

- Thinking every GC is a Galois insertion
- Forgetting that $\gamma \circ \alpha$ is a closure operator

### Exam Checklist

- [ ] Can prove GC properties (extensivity, reductivity, monotonicity)
- [ ] Understands when no best abstraction exists
- [ ] Can distinguish GC from GI

<hr>


## Lecture 14 — Abstract Numerical Domains

### Key Definitions

- **Sign domain**: $\{\emptyset, <0, =0, >0, \le 0, \ge 0, \mathbb{Z}\}$
- **Interval domain**: $[a,b]$ with $a \le b$
- **Congruence domain**: $a\mathbb{Z} + b$
- **Widening**: $\nabla$ operator for convergence

### Key Formulas

- F-17 (Sign operations), F-18 (Interval operations), F-19 (Congruence operations), F-20 (Interval widening)
- BCA: $F^A = \alpha \circ F \circ \gamma$ (F-08)

### BCA Composition Theorem

For a sequence $c = c_1; c_2$, the BCA of the composition is:

$$
\llbracket c_1; c_2\rrbracket^A = \alpha \circ \llbracket c_2\rrbracket \circ \gamma \circ \alpha \circ \llbracket c_1\rrbracket \circ \gamma = (\alpha \circ \llbracket c_2\rrbracket \circ \gamma) \circ (\alpha \circ \llbracket c_1\rrbracket \circ \gamma)
$$

**BUT** this equals $\llbracket c_2\rrbracket^A \circ \llbracket c_1\rrbracket^A$ only if $\gamma \circ \alpha = \text{id}$ (i.e., the abstract domain is a Moore family). In general:

$$
\llbracket c_1;c_2\rrbracket^A \sqsubseteq \llbracket c_2\rrbracket^A \circ \llbracket c_1\rrbracket^A
$$

**Counterexample:** $c_1: y := x$, $c_2: x := \text{random}()$, with sign domain. The BCA of the sequence loses the relation between $x$ and $y$ that $\gamma \circ \alpha$ discards.

### Product Domains

**Cartesian product:** $(A_1 \times A_2, \sqsubseteq_\times)$ where:

- $(a_1,a_2) \sqsubseteq_\times (b_1,b_2) \iff a_1 \sqsubseteq_1 b_1 \land a_2 \sqsubseteq_2 b_2$
- $\bot_\times = (\bot_1,\bot_2)$, $\top_\times = (\top_1,\top_2)$
- $(a_1,a_2) \sqcup_\times (b_1,b_2) = (a_1 \sqcup_1 b_1, a_2 \sqcup_2 b_2)$
- $\alpha_\times(S) = (\alpha_1(S), \alpha_2(S))$
- $\gamma_\times(a_1,a_2) = \gamma_1(a_1) \cap \gamma_2(a_2)$

**Reduced product:** quotient of the product domain by identifying pairs with identical concretizations. Equivalent to taking the Moore family generated by $\{\gamma_1(a_1) \cap \gamma_2(a_2)\}$.

**Example:** Reduced product of intervals and parity yields better precision: interval $[2,4]$ with parity $even$ gives $[2,4] \cap even = \{2,4\}$.

### Pointwise Lifting

Given a concrete domain $C \cong \Sigma \to \wp(\Sigma)$ (functions), lift an abstract domain $A$ for $\wp(\Sigma)$:

$$
A \to A \text{ (functions ordered pointwise): } f \sqsubseteq g \iff \forall a.\ f(a) \sqsubseteq g(a)
$$

**Smashed pointwise lifting:** functions that map $\bot$ to $\bot$ (strict). Used for abstract transfer functions.

### Abstract Stores

For programs with multiple variables, the abstract domain is a **lifted product**:

$$
A_{\text{store}} = \prod_{x \in X} A_{\text{val}}
$$

Each variable maps independently to an abstract value. This is **non-relational**: no relation between variables is tracked.

**Example:** With interval domain $A_{\text{val}}$, an abstract store $\sigma^\#(x) = [1,5],\ \sigma^\#(y) = [0,10]$ means $x \in [1,5]$ and $y \in [0,10]$, independently.

### Domain Exercises

**Pirahã domain:** $A = \{\bot, a, b, c, \top\}$ with $a \sqsubseteq b$, $a \sqsubseteq c$, $b$ and $c$ incomparable.

- Join table: $b \sqcup c = \top$, $b \sqcup a = b$, $c \sqcup a = c$
- Meet table: $b \sqcap c = a$, $b \sqcap a = a$, $c \sqcap a = a$
- $\alpha$ of concrete set $S$: map to least abstract element containing $S$
- Exercise: compute BCA for $c = (x := x+1)$ with different $\sigma^\#(x)$

**Pirandello domain:** Non-lattice poset: $A = \{\bot, p, q, r, \top\}$ with $p \sqsubseteq r$, $q \sqsubseteq r$, $p$ and $q$ incomparable, but $p \sqcap q$ does not exist.

- Not a lattice because meets are not defined for all pairs
- Exercise: define $\gamma$ and $\alpha$ such that soundness holds
- Show that fixpoint computation may fail due to missing meets

**Constant domain (simple but useful):** $A = \{\bot\} \cup \mathbb{Z} \cup \{\top\}$, ordered by $x \sqsubseteq y \iff x = y \lor x = \bot \lor y = \top$. Used for constant propagation.

### Key Algorithms

- Interval widening (A-05)

### Common Mistakes

- Thinking intervals have ACC (they don't — need widening!)
- Forgetting that $\gamma$ is not injective for congruence domain
- Applying widening too aggressively

### Exam Checklist

- [ ] Can define $\gamma$ and $\alpha$ for any abstract domain
- [ ] Can compute BCA for a given domain
- [ ] Knows which domains have ACC and which need widening
- [ ] Understands product and reduced product domains

<hr>


## Lecture 15 — Abstract Analysis

### Key Definitions

- **Correctness**: $F^\# \sqsupseteq \alpha \circ F \circ \gamma = F^A$
- **Completeness**: $F^\# \circ \alpha = \alpha \circ F$

### Key Formulas

- F-07 (Soundness), F-08 (BCA), F-14 (Fixpoint approximation), F-15 (Abstract iteration), F-16 (Correctness condition)

### Formal Abstract Denotational Semantics

**Concrete semantics** (collecting semantics):
$$
\llbracket c\rrbracket: \wp(\Sigma) \to \wp(\Sigma)
$$

**Abstract semantics**:
$$
\llbracket c\rrbracket^\#: A \to A
$$

**Soundness condition (diagram commuting up to approximation):**
$$
\alpha \circ \llbracket c\rrbracket \sqsubseteq \llbracket c\rrbracket^\# \circ \alpha
$$

Equivalently:
$$
\llbracket c\rrbracket \circ \gamma \sqsubseteq \gamma \circ \llbracket c\rrbracket^\#
$$

**Monotonicity requirement:** $\llbracket c\rrbracket^\#$ must be monotone on $A$.

### Accelerated Abstract Interpreter

The standard Kleene iteration:
$$
x_0 = \bot, \quad x_{k+1} = x_k \sqcup F^\#(x_k)
$$
terminates only if $A$ has ACC.

**Widening iteration:**
$$
y_0 = \bot, \quad y_{k+1} = y_k \nabla F^\#(y_k)
$$

Properties:

1. $y_k \sqsubseteq F^\#(y_k) \implies y_{k+1} = y_k \nabla F^\#(y_k) \sqsupseteq y_k$ (ascending)
2. The sequence stabilizes after finitely many steps
3. The limit $y_\star$ is a post-fixpoint: $F^\#(y_\star) \sqsubseteq y_\star$

**Widening + Narrowing:** After widening stabilizes, run narrowing to improve precision:
$$
z_0 = y_\star, \quad z_{k+1} = z_k \mathbin{\triangle} F^\#(z_k)
$$

A **narrowing operator** $\triangle$ satisfies:

1. $z \mathbin{\triangle} w \sqsubseteq z$ (decreasing)
2. If $F^\#(z) \sqsubseteq z$ then $z \mathbin{\triangle} F^\#(z) \sqsupseteq \operatorname{lfp}(F^\#)$ (still sound)

### Completeness and Correctness Definitions

**Correctness (Soundness):** $F^\#$ is correct iff:
$$
F^\# \sqsupseteq \alpha \circ F \circ \gamma = F^A
$$

**Completeness:** $F^\#$ is complete iff:
$$
F^\# \circ \alpha = \alpha \circ F
$$

Completeness means no precision loss: abstract analysis gives exactly the abstraction of the concrete result.

**Fixpoint Approximation Theorem:**
If $F^\#$ is correct (i.e., $F^\# \sqsupseteq F^A$), then:
$$
\operatorname{lfp}(F^\#) \sqsupseteq \alpha(\operatorname{lfp}(F))
$$

Proof: $\alpha(\operatorname{lfp}(F))$ is a post-fixpoint of $F^\#$ because:
$$
F^\#(\alpha(\operatorname{lfp}(F))) \sqsupseteq \alpha(F(\gamma(\alpha(\operatorname{lfp}(F))))) \sqsupseteq \alpha(F(\operatorname{lfp}(F))) = \alpha(\operatorname{lfp}(F))
$$
The least fixpoint of $F^\#$ approximates the abstraction of the concrete least fixpoint.

### Interval Analysis Example

Program:
```
(1) x := 0;
(2) while x < 100 do {
(3)     x := x + 1
(4=2) }
(5) // end
```

**Abstract domain:** $A = \{[a,b] \mid a \le b,\ a \in \mathbb{Z} \cup \{-\infty\},\ b \in \mathbb{Z} \cup \{+\infty\}\} \cup \{\bot\}$

**Abstract transfer functions:**

- $F_2^\#(x) = [0,0]$ (assignment $x:=0$)
- $F_4^\#(x) = [x.\text{lo}+1, x.\text{hi}+1]$ (assignment $x:=x+1$)
- $F_3^\#(x) = x \sqcap [-\infty, 99]$ (guard $x < 100$)
- $F_5^\#(x) = x \sqcap [100, \infty]$ (guard $x \ge 100$)

**Kleene iteration without widening:**

- $x_0 = \bot$
- $x_1 = [0,0]$
- $x_2 = [0,0] \sqcup ([0,0] \sqcap [-\infty,99] + [1,1]) = [0,1]$
- $x_3 = [0,2]$
- $x_4 = [0,3]$
- ...

- Never stabilizes! (interval domain has no ACC)

**With widening $\nabla$:**

- $x_0 = \bot$
- $x_1 = [0,0]$
- $x_2 = [0,0] \nabla ([0,1]) = [0, \infty]$ (upper bound jumps to $\infty$ because $0 < 1$)
- $x_3 = [0,\infty] \nabla ([1,\infty] \sqcap [-\infty,99] + [1,1]) = [0,\infty] \nabla [1,100] = [0, \infty]$
- Stabilized at $[0, \infty]$

**Narrowing to improve precision:**

- $z_0 = [0, \infty]$
- $z_1 = [0, \infty] \triangle ([1,\infty] \sqcap [-\infty, 99] + [1,1]) = [0, \infty] \triangle [1, 100]$
  With narrowing: $[0, \infty] \triangle [1, 100] \sqsubseteq [0, \infty]$ but $ \sqsupseteq \operatorname{lfp}$
  Standard narrowing: $[0, \infty] \triangle [1,100] = [0, 100]$

- $z_2 = [0,100] \triangle ([1,100] \sqcap [-\infty,99] + [1,1]) = [0,100] \triangle [1,100] = [0,100]$
- Stabilized at $[0,100]$

**Concrete vs Abstract Equivalence:**

Two programs are **concretely equivalent** if they produce the same output for the same input.

Two programs are **abstractly equivalent** if they produce the same abstract result.

Important: concrete equivalence does NOT imply abstract equivalence!

Example:

- $P_1: x := x + 1; x := x + 1$
- $P_2: x := x + 2$

Concretely equivalent, but with sign domain $x := x+2$ gives $\mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ (via addition table), while $x:=x+1; x:=x+1$ gives different intermediate results.

### Key Algorithms

- Worklist algorithm (A-03)
- Abstract fixpoint with widening (A-02)

### Common Mistakes

- Confusing abstract with concrete equivalence
- Forgetting that concrete equivalence $\not\Rightarrow$ abstract equivalence

### Exam Checklist

- [ ] Can compute abstract fixpoints
- [ ] Understands the three-stage approach
- [ ] Knows when to use widening

<hr>


## Lecture 16 — Local Completeness Logic

### Key Definitions

- **Global completeness**: $\forall P.\ A(\llbracket c\rrbracket P) = \llbracket c\rrbracket^\# A(P)$
- **Local completeness**: $\mathbb{C}_P(e): A(\llbracket e\rrbracket P) = A(\llbracket e\rrbracket A(P))$
- **LCL triple**: $\vdash_A [P]\ c\ [Q]$ with $Q \subseteq \llbracket c\rrbracket P \subseteq A(Q)$

### Key Formulas

- F-09 (Completeness equation), F-11 (LCL triple), F-12 (Local completeness), F-13 (Iteration rule)

### Galois Insertion as Closures Formalism

A **Galois insertion** $(\alpha, \gamma)$ can be represented equivalently by the **closure operator** $\rho = \gamma \circ \alpha$:

$$
\rho: \wp(\Sigma) \to \wp(\Sigma)
$$

Properties:

1. $\rho$ is monotone, extensive, idempotent
2. The image of $\rho$ is $\{Y \mid Y = \rho(Y)\}$ — the set of abstract (closed) sets
3. $A \cong \{\rho(Y) \mid Y \in \wp(\Sigma)\}$ — abstract elements correspond bijectively to closed sets
4. $\alpha(S) \cong \rho(S)$ — abstraction is closure

**Key insight:** In a Galois insertion, $\gamma$ is injective, so abstract elements ARE closed sets. This means:

- $\gamma \circ \alpha = \rho$ (closure on concrete)
- $\alpha \circ \gamma = \text{id}_A$ (no redundancy in the abstract domain)

### Completeness Revisited

**Completeness equation:**
$$
\llbracket c\rrbracket^\# \circ A = A \circ \llbracket c\rrbracket
$$

This means: analyzing the abstracted input gives the same result as abstracting the concrete output.

**Local completeness for atomic command $e$:**
$$
\mathbb{C}_P(e): A(\llbracket e\rrbracket P) = A(\llbracket e\rrbracket A(P))
$$

The abstraction of executing $e$ on $P$ equals the abstraction of executing $e$ on the abstraction of $P$.

**Only atomic commands can be incomplete.** For compound commands:

- Composition: if $\mathbb{C}_R(c_1)$ and $\mathbb{C}_{\llbracket c_1\rrbracket P}(c_2)$ then $\mathbb{C}_P(c_1;c_2)$
- Choice: if $\mathbb{C}_P(c_1)$ and $\mathbb{C}_P(c_2)$ then $\mathbb{C}_P(c_1 + c_2)$
- Iteration: if $\mathbb{C}_{A(P)}(c)$ and $\mathbb{C}_{A(P)}(c^{\star})$ then $\mathbb{C}_P(c^{\star})$

### BCA Completeness Condition

The **Best Correct Abstraction** $F^A = \alpha \circ F \circ \gamma$ is the most precise sound abstraction.

$F^\#$ is **complete** iff $F^\# = F^A$. The difference between $F^\#$ and $F^A$ measures incompleteness.

**Incompleteness sources:**

1. **Domain choice:** abstract domain cannot express the needed property
2. **Transfer function design:** $F^\#$ is coarser than $F^A$
3. **Non-relational loss:** product domains lose correlations between variables

### Verification Problem Statement

Given:

- Program $c$
- Specification: pre/post-condition pair $(Spec, Q)$
- Abstract domain $A$ with abstraction function $A = \gamma \circ \alpha$

**Verification:** Check whether $c$ satisfies the specification with respect to $A$.

**Approach using LCL:**

1. Prove $\vdash_A [Spec]\ c\ [Q']$ for some $Q'$ such that $Q' \subseteq \llbracket c\rrbracket(Spec) \subseteq A(Q')$
2. Check $Q' \subseteq Q$ (under-approximation: all real behaviors reach $Q'$)
3. Check $Q \subseteq \llbracket c\rrbracket(Spec)$ (over-approximation: the specification is achievable)

**Local completeness proof** ensures that inferences about incomplete atomic commands are identified and handled.

### LCL Inference Rules

**Basic rules:**
$$
[\mathsf{assume}]\quad \dfrac{\mathbb{C}_P(b?)\quad P \land b \subseteq A(P)}{A \vdash [P]\ b?\ [P \land b]}
\qquad
[\mathsf{choice}]\quad \dfrac{A \vdash [P]\ c_1\ [Q_1]\quad A \vdash [P]\ c_2\ [Q_2]}{A \vdash [P]\ c_1 + c_2\ [Q_1 \cup Q_2]}
$$

$$
[\mathsf{seq}]\quad \dfrac{A \vdash [P]\ c_1\ [R]\quad A \vdash [R]\ c_2\ [Q]}{A \vdash [P]\ c_1;c_2\ [Q]}
\qquad
[\mathsf{iter}]\quad \dfrac{\forall n.\ A \vdash [P_n]\ c\ [P_{n+1}]}{A \vdash [P_0]\ c^{\star}\ [\exists k.\ P_k]}
$$

**Relax rule:**
$$
[\mathsf{relax}]\quad \dfrac{A \vdash [P]\ c\ [Q]\quad A(P') = A(P)}{A \vdash [P']\ c\ [Q]}
$$

**Consequence (adjusted for LCL):**
$$
[\mathsf{cons}]\quad \dfrac{Q \subseteq \llbracket c\rrbracket P \subseteq A(Q) \quad A \vdash [P]\ c\ [Q]}{A \vdash [P]\ c\ [Q']\ \text{if } Q \subseteq Q' \subseteq A(Q)}
$$

### Applications and Examples

**Example 1:** Sign domain analysis of $x := x + 1$:

- $P = \{x = 5\}$ (concrete singleton)
- $A(P) = \mathbb{Z}_{>0}$
- $\mathbb{C}_P(x := x + 1)$ holds because $A(\llbracket x:=x+1\rrbracket \{5\}) = \mathbb{Z}_{>0} = A(\llbracket x:=x+1\rrbracket \mathbb{Z}_{>0})$
- Since $P \subseteq A(P)$ ($\{5\} \subseteq \mathbb{Z}_{>0}$), the assume rule gives $\vdash_A [\{x=5\}]\ x:=x+1\ [\{x=6\}]$

**Example 2:** Interval domain analysis of $x := x \bmod 2$:

- $P = [0,100]$
- $A(P) = [0,100]$
- $\mathbb{C}_P(x := x \bmod 2)$ fails because $\llbracket x:=x \bmod 2\rrbracket[0,100] = [0,1]$ but $A(\llbracket x:=x \bmod 2\rrbracket[0,100]) = [0,1] \ne [0,1] \cap [0,100] = [0,1]$ — actually this IS locally complete since $A([0,1]) = [0,1]$
- Counterexample: $P = [1,3]$, $A([1,3]) = [1,3]$, $\llbracket x:=x \bmod 2\rrbracket[1,3] = \{0,1\}$, $A(\{0,1\}) = [0,1]$, $\llbracket x:=x \bmod 2\rrbracket[1,3] \cap [1,3] = \{1\}$, $A(\{1\}) = [1,1] \ne [0,1]$
- Therefore $\mathbb{C}_{[1,3]}(x := x \bmod 2)$ fails — the interval domain loses parity information

### Key Algorithms
None new (uses previous fixpoint algorithms).

### Common Mistakes

- Thinking LCL is just HL or just IL
- Forgetting the Relax rule condition $A(P') = A(P)$
- Not understanding that incomplete atomic commands are the only source of incompleteness

### Exam Checklist

- [ ] Can derive LCL triples
- [ ] Understands local vs global completeness
- [ ] Knows the verification theorem
- [ ] Understands sources of incompleteness

<hr>


## Lectures 17–22 — Control Flow Analysis (FUN)

### Key Definitions

- **CFA**: statically approximates which functions may be called at each call site
- **0-CFA**: monovariant (one abstract value per program point)
- **$k$-CFA**: context-sensitive with call strings of length $k$
- **CPA (Cartesian Product Algorithm)**: context-sensitive with argument tuples as contexts
- **Acceptability relation**: $(\hat{C}, \hat{\rho}) \models e$
- **Syntax-directed CFA ($\models_s$)**: analyses function bodies at definition time
- **Constraint-based CFA ($C^*[\![e]\!]$)**: generates finite set of (conditional) constraints
- **Flow logic**: constraint-based formulation of CFA
- **Moore family**: set of acceptable analyses closed under $\sqcap$ (greatest lower bound)
- **Least solution**: most precise CFA exists (intersection of all acceptable analyses)
- **Constraint graph**: nodes ($C(\ell), r(x)$) + edges (direct and conditional)

### Key Formulas

- Constraint generation rules (A-04)
- Order on analyses: $(\hat{C}_1, \hat{\rho}_1) \sqsubseteq (\hat{C}_2, \hat{\rho}_2)$ iff $\forall \ell.\ \hat{C}_1(\ell) \subseteq \hat{C}_2(\ell)$ and $\forall x.\ \hat{\rho}_1(x) \subseteq \hat{\rho}_2(x)$
- Conditional constraint form: $\{t\} \subseteq rhs' \Rightarrow lhs \subseteq rhs$

### Key Algorithms

- 0-CFA constraint generation (A-04)
- Syntax-directed CFA (A-06)
- $k$-CFA call string (A-07)
- Constraint solving via least fixed point

### Common Mistakes

- Confusing $\subseteq$ direction in constraints (result flows forward, arguments flow into $\hat{\rho}$)
- Forgetting that 0-CFA loses precision by merging call contexts
- Thinking $k$-CFA is always worth the cost (exponential blowup)
- Not handling the conditional constraint correctly

### Exam Checklist

- [ ] Can label expressions for CFA
- [ ] Can generate constraints for 0-CFA
- [ ] Can explain the difference between 0-CFA and $k$-CFA
- [ ] Understands soundness vs precision in CFA
- [ ] Can extend CFA with DFA for data properties
- [ ] Can prove existence of least solution via Moore family

<hr>


## Lectures 23–24 — CFA for $\pi$-Calculus

### Key Definitions

- **Name mobility**: channels can be transmitted as values (unlike CCS)
- **Abstract environment** $\rho: \text{Var} \to \wp(\text{Const})$: maps variables to possible constants
- **Abstract channel environment** $\kappa: \text{Var} \to \wp(\text{Const})$: maps channels to possible communicated values
- **Acceptable guess**: $(\rho, \kappa) \models_P P$ satisfying all validation clauses
- **Oblivious analysis**: matching, restriction, and replication are treated optimistically (over-approximate)
- **Subject reduction**: if $(\rho, \kappa) \models_P P$ and $P \to Q$, then $(\rho, \kappa) \models_P Q$
- **Canonical names**: $\lfloor n \rfloor$ is the equivalence class of $n$ (disciplined $\alpha$-renaming)
- **Polyadic $\pi$-calculus**: tuples of values, arity checking, $\psi$ for arity mismatches

### Key Formulas

- Output clause: $\forall n \in \rho(u): \rho(v) \subseteq \kappa(n)$
- Input clause: $\forall n \in \rho(u): \kappa(n) \subseteq \rho(x)$
- Substitution lemma: $(\rho, \kappa) \models_P \lfloor P[m/x] \rfloor$ provided $\lfloor m \rfloor \subseteq \rho(x)$
- Prefix clause: $(\rho, \kappa) \models_P \pi.P \iff (\rho, \kappa) \models_A \pi \land (\rho, \kappa) \models_P P$
- Parallel clause: $(\rho, \kappa) \models_P P_1 \mid P_2 \iff (\rho, \kappa) \models_P P_1 \land (\rho, \kappa) \models_P P_2$
- Match* (refined): $\rho(x) \cap \rho(y) \neq \emptyset \Rightarrow (\rho, \kappa) \models_P P$
- Polyadic output: $\forall n \in \rho(u): \rho(v_1) \times \dots \times \rho(v_k) \subseteq \kappa(n)$
- Polyadic input: $\forall n \in \rho(u): \kappa(n) \subseteq \rho(x_1) \times \dots \times \rho(x_k)$

### Key Algorithms

- Validation clause checking (systematic verification of $(\rho, \kappa) \models_P P$)
- Constraint generation and solving for $\pi$-calculus
- Least solution via Moore family intersection (same principle as CFA for FUN)

### Common Mistakes

- Forgetting $\rho(n) = \{n\}$ for constants (extension rule)
- Confusing $\rho$ (variable bindings) with $\kappa$ (channel contents)
- Thinking restriction creates fresh names — analysis treats all names as global
- Using the basic match clause when a refined version would give better precision
- Forgetting that 0-CFA for $\pi$-calculus is context-insensitive (like 0-CFA for FUN)
- Not distinguishing between $\pi$-calculus with and without arity in polyadic version

### Exam Checklist

- [ ] Can write $\pi$-calculus processes with actions and prefixes
- [ ] Can define $\rho$ and $\kappa$ for a given process
- [ ] Can verify $(\rho, \kappa) \models_P P$ by checking all clauses
- [ ] Understands why restriction is treated obliviously
- [ ] Can apply the refined match clause
- [ ] Understands subject reduction and why it implies soundness
- [ ] Can explain the role of canonical names


- [ ] Knows that a least solution always exists (Moore family)
- [ ] Can describe the polyadic extension with $\kappa$ and $\psi$
- [ ] Understands the limitations of 0-CFA for $\pi$-calculus

# Cross-Reference Index

## Formulas by Lecture

| Formula | Lecture | Domain |
|:---|:---:|:---:|
| F-01 | 02 | Semantics |
| F-02 | 02 | wlp |
| F-03 | 02 | wpp |
| F-04 | 03 | HL |
| F-05 | 05 | IL |
| F-06 | 12,13 | Galois |
| F-07 | 12 | Soundness |
| F-08 | 14 | BCA |
| F-09 | 16 | Completeness |
| F-10 | 13 | GI |
| F-11 | 16 | LCL |
| F-12 | 16 | LCL |
| F-13 | 16 | LCL |
| F-14 | 15 | Fixpoint |
| F-15 | 15 | Iteration |
| F-16 | 15 | Correctness |
| F-17 | 12 | Sign |
| F-18 | 14 | Interval |
| F-19 | 14 | Congruence |
| F-20 | 14,15 | Widening |

## Exercises by Topic

| Topic | Exercises |
|:---|:---|
| HL / IL / NC / SIL axioms | E-01 |
| Galois Connections | E-02, E-05 |
| Abstract Domains | E-02 |
| BCA / Completeness | E-02 |
| 0-CFA / 1-CFA / Constraints | E-03, E-06 |
| CFA + DFA Integration | E-06 |
| Separation Logic (ISL) | E-04 |

## Algorithms by Topic

| Topic | Algorithms |
|:---|:---|
| Fixpoint computation | A-01, A-02 |
| Abstract interpretation | A-03 |
| CFA | A-04, A-06, A-07 |
| Interval analysis | A-05 |

<hr>


# Validation Report

## LaTeX Validation

- All formulas use $...$ for inline and $$...$$ for display mathematics
- Set notation uses `\{` and `\}` throughout
- Semantic brackets use `\llbracket` and `\rrbracket`
- Lattice symbols use `\sqsubseteq`, `\sqcup`, `\sqcap`, `\bot`, `\top`
- Quantifiers use `\forall`, `\exists`
- No LaTeX environment blocks that might break
- No fenced ```latex blocks
- $\pi$-calculus notation uses standard operators: $\overline{u}\langle v\rangle$, $u(x)$, $\Sigma$, $\mid$, $(\nu n)P$, $!P$, $\models_P$, $\models_A$
- Polyadic extension notation uses $\vec{v}$, $\vec{x}$, $\psi$
- All $\kappa$ and $\rho$ references use consistent $\wp(\text{Const})$ notation

## Content Completeness

- [x] All 23+ lectures covered
- [x] Definitions extracted
- [x] Formulas extracted with full metadata (20 formulas)
- [x] Theorems and lemmas included
- [x] Inference rules for all logics (HL, IL, NC, SIL, SL, ISL, LCL)
- [x] Algorithms extracted with structured format (7 algorithms)
- [x] Exercises collected with solutions (6 exercises)
- [x] Cross-references built
- [x] Lecture summaries with exam checklists (per lecture)
- [x] Exam preparation guide
- [x] Final cheat sheet
- [x] Formula handbook (enhanced with meaning, variables, intuition, usage)
- [x] Validation report

## Known Gaps

- Exercise E-04 (ISL), E-05 (Galois), E-06 (CFA+DFA) have **generated** solutions (not official) — clearly marked
- Exercise PDFs may contain more exercises beyond text extraction
- NC and SIL full proof systems not detailed beyond guard axioms
- Polyadic $\pi$-calculus CFA with $\psi$ (arity mismatch) is sketched but not covered in full depth
- No formal soundness proof for $\pi$-calculus CFA is included (subject reduction theorem stated without proof)
