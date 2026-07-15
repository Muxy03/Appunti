# Galois

Abstract Interpretation = a technique to formally reason on approximations

![[Pasted image 20260712175451.png]]

Poset = partial order on a set X (reflexive, anti-symmetric, transitive)

validation = program P satisfying a specification S as the set inclusion $P \subseteq S$

soundness = outputs a result that is coarser than the actual behavior

$a \sqcup b$ = lub of a and b
$a \sqcap b$ = glb of a and b
$\sqcup A$ = lub of A
$\sqcap A$ = glb of A

$(\wp(X), \subseteq) \implies lub=\cup, glb=\cap$

chain = in a poset is a subset that is totally ordered $\forall c,d \in C: (c \sqsubseteq d) \lor (d \sqsubseteq c)$

Una **ascending chain** (catena ascendente) in un poset $(X,\sqsubseteq)$ è una sequenza numerabile di elementi $\{x_i​\}_{i∈N}​$ tale che ogni elemento precede il successivo nell'ordine parziale.

A poset $(X,\sqsubseteq)$ has finite height $n \in \mathbb{N}$ if the cardinality of the longest chain is $n + 1$

A poset $(X,\sqsubseteq)$ satisfies the Ascending Chain Condition (ACC) when each ascending chain converges (i.e., there are no infinite ascending chains)

ACC abstract domains guarantee that the analysis always terminates!

CPO = a poset such that every chain has a lub. ($\sqcup \emptyset = \bot$)

Pointed CPOs = CPOs with bottom $(\bot)$

Lattice $(X,\sqsubseteq,\sqcup,\sqcap)$ = poset such that $\forall a,b \in X:a \sqcup b \; \text{and} \; a \sqcap b$ exists

Complete Lattice $(X,\sqsubseteq,\sqcup,\sqcap,\bot,\top)$ = poset such: $\forall A \subseteq X: \sqcup A \;exists \; \sqcap A \;exists$
$\bot = lub(\emptyset)=glb(X)$
$\top = lub(X)=glb(\emptyset)$

interval lattice = $(\{[a,b] | a,b \in \mathbb{Z}, a \le b\} \cup {\bot}, \subseteq,\sqcup,\cap)$ -> $[a,b] \sqcup [a',b'] = [min(a,a'),max(b,b')]$ (not all lubs exist)

![[Pasted image 20260712181138.png]]

>![[Pasted image 20260712182132.png]]
>Ecco la dimostrazione del fatto che la condizione (1) implica la condizione (2):
>
>1. **Sia $B \subseteq X$ un sottoinsieme arbitrario.** Vogliamo dimostrare che $\sqcap B$ esiste.
>2. **Definiamo l'insieme dei limiti inferiori:** Sia $L = {x \in X \mid \forall b \in B, x \sqsubseteq b}$ l'insieme di tutti gli elementi di $X$ che sono minoranti di $B$.
>3. **Applichiamo l'ipotesi (1):** Per ipotesi, ogni sottoinsieme di $X$ ha un lub. Quindi esiste $g = \sqcup L$.
>4. **Verifichiamo che $g$ sia un minorante:** Poiché ogni elemento $b \in B$ è, per definizione di $L$, un maggiorante dell'intero insieme $L$, e poiché $g$ è il _minimo_ dei maggioranti di $L$, allora deve valere $g \sqsubseteq b$ per ogni $b \in B$. Quindi $g$ è un minorante di $B$.
>5. **Verifichiamo che $g$ sia il massimo dei minoranti:** Ogni altro minorante $x$ di $B$ appartiene per definizione a $L$. Dato che $g = \sqcup L$, allora $x \sqsubseteq g$ per ogni $x \in L$. Questo rende $g$ il **massimo dei minoranti**, ovvero $g = \sqcap B$.
>
>L'implicazione inversa (2 $\implies$ 1) si ottiene in modo identico applicando il **Principio di Dualità**: se ogni sottoinsieme ha un glb, allora $\sqcup A$ può essere definito come il glb dell'insieme dei suoi maggioranti.

lcm = least common multiple
gcd = greatest common divisor

monotonicity = respect the order
continuity   = preserve limits
extensivity  = $\forall a \in A: a \sqsubseteq f(a)$
reductive    = $\forall a \in A: f(a) \sqsubseteq a$

Extensivity is essentially useful when combined with monotonicity to bootstrap iteration: starting from an arbitrary x, we have $x \sqsubseteq f(x)$ by extensivity; then, applying monotonicity $f(x) \sqsubseteq f^2(x)$, etc., so the sequence $\{f^i(x)|i \in N\}$ is increasing.

Abstract Domain = $(A, \sqsubseteq)$ expresses some properties of the concrete values (The order $\sqsubseteq$ on the abstract domain reflects the precision)

Abstract Interpretation = $(C,A,\gamma:A \to C, \alpha: C \to A)$

Concretization $(\gamma:A \to C)$ = a monotone function that maps abstract a into the greatest concrete that it approximates.

$a \in A \; \text{is a sound abstraction of} \;c \in C \iff c \leq \gamma(a)$

![[Pasted image 20260702121954.png]]

Abstraction $(\alpha:C \to A)$ = a monotone function that maps *c* concrete into the most precise abstract element that approximates it.

![[Pasted image 20260702122217.png]]

![[Pasted image 20260702122328.png]]

![[Pasted image 20260712183629.png]]

![[Pasted image 20260702122543.png]]

idempotency = f(f(x)) = f(x)

![[Pasted image 20260702122556.png]]

![[Pasted image 20260712184606.png]]

$A:C \to C$
$A(c) = \gamma(\alpha(c))$ -> closure operator (monotone, extensive, idempotent)
A(c) = set of expressible elements

$F: C \to C$ = concrete operator
$F^\#:A \to A$ = corresponding operator in the abstract domain
$F^\#$ is a **sound abstraction** of *F* if $\forall a \in A: F(\gamma(a)) \subseteq \gamma(F^\#(a))$
$F^\#$ is a **sound abstraction** of *F* if $\forall a \in A: \alpha(F(\gamma(a))) \sqsubseteq F^\#(a)$
$F^\#$ is a **sound abstraction** of *F* if $\forall a \in A: \alpha(F(c)) \subseteq F^\#(\alpha(c))$

![[Pasted image 20260702144442.png]]

$F^A \triangleq \alpha \circ F \circ \gamma$
Given a Galois connection and a concrete operator *F* the best abstraction (bca) of *F* is given by $F^A$

![[Pasted image 20260702144457.png]]

![[Pasted image 20260702144513.png]]

the composition of two GCs is a GC

Piranha domain: $$(N^\infty, \leq), \gamma(\top) = \infty,\gamma(\bot)=3, \alpha(n) = \bot \;(\text{if}\;n \leq 3),\alpha(n) = \top \;(otherwise)$$
Pirandello domain:$$(N^\infty,\leq),\gamma(\top)=\infty,\gamma(1)=1,\gamma(\bot)=0,\alpha(0)=\bot,\alpha(1)=1,\alpha(n)=\top \;(otherwise)$$
Constant domain:$$(\wp(\mathbb{V}),\subseteq),\gamma(\top)=\mathbb{V},\gamma(k_n)={k_n},\gamma(\bot)= \emptyset$$
Constant set domain:$$(\wp(\mathbb{V}),\subseteq),\gamma(\top)=\mathbb{V},\gamma(X^\#)=X^\# \;(\text{if}\; X^\# \subseteq \wp_k(K))$$

BCA for product in $A_{|k|}$:

$X^\sharp \times^\sharp Y^\sharp \triangleq \alpha( \gamma(X^\sharp) \times \gamma(Y^\sharp) )$.

**Case 1: Empty set.** If $X^\sharp = \emptyset$ or $Y^\sharp = \emptyset$, the result is **$\emptyset$**.

**Case 2: Zero element.** If $X^\sharp = {0}$ or $Y^\sharp = {0}$ (and neither is $\emptyset$), the result is **${0}$**. This holds even if the other argument is $\top^\sharp$, as the concrete product of any set with zero is ${0}$.

**Case 3: Unknown information ($\top^\sharp$).** If $X^\sharp = \top^\sharp$ or $Y^\sharp = \top^\sharp$ (and neither is $\emptyset$ or ${0}$), the result is **$\top^\sharp$**.

**Case 4: Bounded sets.** If both arguments are finite sets $X^\sharp, Y^\sharp \subseteq \mathcal{P}_{\le k}(\mathbb{I})$, we first compute the concrete set of products $S = \{x \cdot y \mid x \in X^\sharp, y \in Y^\sharp\}$:
- If $|S| \le k$, the result is **$S$**.
- If $|S| > k$, the result is **$\top^\sharp$**.

This definition ensures that the abstract operation mimics the concrete behavior with no loss of precision beyond what is forced by the domain's size constraint $k$.

adjoint abstraction map $\alpha:\wp(\mathbb{Z}) \to A_{|2|}$:
In the **bounded set domain $A_{|2|}$**, which tracks sets containing at most two integers, the **adjoint abstraction map** $\alpha: \wp(\mathbb{Z}) \to A_{|2|}$ maps a concrete set $S$ to the most precise representation available in the abstract domain.

It is defined as follows:

$$ \alpha(S) \triangleq \begin{cases} S & \text{if } |S| \le 2 \ \top & \text{if } |S| > 2 \end{cases} $$

**Key Characteristics**

- **Precision:** If the concrete set has two or fewer elements (including the empty set $\emptyset$ or singletons), $\alpha$ is **exact**, meaning $\gamma(\alpha(S)) = S$.
- **Over-approximation:** If the set contains more than two elements, the domain lacks a specific representation for it, so it must be abstracted to **$\top$** (representing the entire set $\mathbb{Z}$), which is the smallest sound abstraction available.
- **Galois Insertion:** Because this mapping ensures every abstract element corresponds to a unique concrete set (no redundancy), it forms a **Galois insertion** where $\alpha$ is surjective and $\gamma$ is injective.

Interval domain:
$$(\{[a,b]\;|\; a \in \mathbb{Z} \cup \{+\infty\},\; a \leq b\} \cup \{\bot\},\subseteq,\sqcup,\cap,\bot,[-\infty,+\infty])$$
$$\gamma(\bot)=\emptyset,\gamma([a,b])=\{x \in \mathbb{Z}|a \leq x \leq b\}$$
$$[a,b] \sqsubseteq [c,d] \iff (c \leq a)\land(b \leq d)$$
$$[a,b] \sqcup^\# [c,d] \triangleq [min(a,c),max(b,d)]$$
$$[a,b] \sqcap^\# [c,d] \triangleq [max(a,c),min(b,d)] \; \text{if} \; max(a,c)\leq min(b,d)$$
$$[a,b] \sqcap^\# [c,d] \triangleq \bot \; otherwise$$
$$[a,b] -^\# [c,d] = [a-d,b-c]$$

$$[a,b] +^\# [c,d] = [a+c,b+d]$$


![[Pasted image 20260702154206.png]]

![[Pasted image 20260702154220.png]]

![[Pasted image 20260702155254.png]]

## Convex Polyhedra domain:

![[Pasted image 20260702155140.png]]

![[Pasted image 20260702160030.png]]

## Octagons domain:

![[Pasted image 20260702155200.png]]
## Congruence domain:

![[Pasted image 20260702154934.png]]

![[Pasted image 20260702154945.png]]

Although the domain has an infinite height, there is no infinite strictly increasing chain!

![[Pasted image 20260702155004.png]]

![[Pasted image 20260702155927.png]]

![[Pasted image 20260702155939.png]]

## Product domains

concrete domain = powerset of integers
abstract domain = intervals abstraction x congruence abstraction

![[Pasted image 20260702160353.png]]

![[Pasted image 20260702160411.png]]

![[Pasted image 20260702160437.png]]

![[Pasted image 20260702160725.png]]

![[Pasted image 20260702160750.png]]

![[Pasted image 20260702160802.png]]

![[Pasted image 20260702160821.png]]

![[Pasted image 20260702160901.png]]

![[Pasted image 20260702160910.png]]

## Exercises:

### Classification of the 7-element structure

**Exercise:** Consider the covering relations: $a \lessdot c, a \lessdot e, b \lessdot d, b \lessdot f, c \lessdot g, d \lessdot g, e \lessdot g, f \lessdot g$. Classify the structure.

1. **Poset? Yes.** The transitive closure of these relations satisfies reflexivity, antisymmetry, and transitivity.
2. **CPO? No.** A Complete Partial Order must be "pointed," meaning it must have a least element ($\bot$). This structure has two distinct minimal elements ($a$ and $b$) and no unique bottom.
3. **Lattice? No.** In a lattice, every pair of elements must have a unique least upper bound (lub) and greatest lower bound (glb). Here, the pair ${a, b}$ has no lower bounds at all, so their glb does not exist.
4. **Complete Lattice? No.** A complete lattice requires that _every_ subset has a lub and a glb, which implies the existence of a bottom element ($\bot = \text{lub}(\emptyset)$).

---

### Sound Abstractions in Intervals

**Exercise:** Which intervals offer a sound abstraction for the following sets?

1. **The finite set ${0, 5, 9}$:** The best abstraction is the smallest interval containing all elements, which is **$**.
2. **The set of all powers of 2 ${1, 2, 4, \dots}$:** The lower bound is 1 and it has no upper bound, so the best abstraction is **$[1, \infty]$**.
3. **The set of all even numbers ${\dots, -2, 0, 2, \dots}$:** Since it includes both arbitrarily large positive and negative numbers, the best abstraction is **$[-\infty, \infty]$** (also denoted as $\top$).

---

### Complete Lattice: Lub vs Glb Existence

**Exercise:** Prove that in a poset $(X, \sqsubseteq)$, the property (1) "every subset has a lub" holds if and only if property (2) "every subset has a glb" holds.

1. **Assume (1) holds.** Let $B \subseteq X$ be an arbitrary subset. We wish to show $\sqcap B$ exists.
2. Define $L = {x \in X \mid \forall b \in B, x \sqsubseteq b}$, the set of all lower bounds of $B$.
3. By hypothesis (1), the subset $L$ has a least upper bound $g = \sqcup L$.
4. Since every $b \in B$ is an upper bound for $L$, and $g$ is the _least_ upper bound, then $g \sqsubseteq b$ for all $b \in B$. Thus, $g$ is a lower bound of $B$.
5. By definition of $L$, any other lower bound $x$ of $B$ belongs to $L$. Since $g$ is the lub of $L$, $x \sqsubseteq g$. Thus, $g$ is the greatest lower bound of $B$ ($g = \sqcap B$).
6. The converse $(2) \implies (1)$ follows by the Duality Principle.

---

### Ex. 1: Extensivity of $\gamma \circ \alpha$

**Exercise:** Prove $c \le \gamma(\alpha(c))$ for all $c \in C$ given the Galois Connection (GC) property $c \le \gamma(a) \iff \alpha(c) \sqsubseteq a$.

1. In the property $c \le \gamma(a) \iff \alpha(c) \sqsubseteq a$, let $a = \alpha(c)$.
2. The right side becomes $\alpha(c) \sqsubseteq \alpha(c)$, which is true by reflexivity of the poset $(A, \sqsubseteq)$.
3. Because the equivalence holds, the left side $c \le \gamma(\alpha(c))$ must also be true.

---

### Ex. 2: Reductivity of $\alpha \circ \gamma$

**Exercise:** Prove $\alpha(\gamma(a)) \sqsubseteq a$ for all $a \in A$ given the GC property.

1. In the property $c \le \gamma(a) \iff \alpha(c) \sqsubseteq a$, let $c = \gamma(a)$.
2. The left side becomes $\gamma(a) \le \gamma(a)$, which is true by reflexivity of the poset $(C, \le)$.
3. Because the equivalence holds, the right side $\alpha(\gamma(a)) \sqsubseteq a$ must also be true.

---

### Ex. 3: Monotonicity of $\alpha$

**Exercise:** Prove that if $c_1 \le c_2$, then $\alpha(c_1) \sqsubseteq \alpha(c_2)$.

1. From Ex. 1, we know $c_2 \le \gamma(\alpha(c_2))$.
2. If $c_1 \le c_2$, then by transitivity of $\le$, $c_1 \le \gamma(\alpha(c_2))$.
3. By the GC property $c \le \gamma(a) \iff \alpha(c) \sqsubseteq a$, where $a = \alpha(c_2)$, we conclude $\alpha(c_1) \sqsubseteq \alpha(c_2)$.

---

### Ex. 4: Monotonicity of $\gamma$

**Exercise:** Prove that if $a_1 \sqsubseteq a_2$, then $\gamma(a_1) \le \gamma(a_2)$.

1. From Ex. 2, we know $\alpha(\gamma(a_1)) \sqsubseteq a_1$.
2. If $a_1 \sqsubseteq a_2$, then by transitivity of $\sqsubseteq$, $\alpha(\gamma(a_1)) \sqsubseteq a_2$.
3. By the GC property $c \le \gamma(a) \iff \alpha(c) \sqsubseteq a$, where $c = \gamma(a_1)$, we conclude $\gamma(a_1) \le \gamma(a_2)$.

---

### Ex. 5: Equivalent Definition

**Exercise:** Prove that a pair of maps $(\alpha, \gamma)$ satisfies the GC property iff $\alpha$ and $\gamma$ are monotone, $\gamma \circ \alpha$ is extensive, and $\alpha \circ \gamma$ is reductive.

1. **($\implies$)** proven in Ex. 1, 2, 3, and 4.
2. **($\impliedby$)** Assume monotonicity, extensivity, and reductivity.
3. If $\alpha(c) \sqsubseteq a$, then by monotonicity of $\gamma$, $\gamma(\alpha(c)) \le \gamma(a)$. By extensivity, $c \le \gamma(\alpha(c))$, so by transitivity $c \le \gamma(a)$.
4. If $c \le \gamma(a)$, then by monotonicity of $\alpha$, $\alpha(c) \sqsubseteq \alpha(\gamma(a))$. By reductivity, $\alpha(\gamma(a)) \sqsubseteq a$, so by transitivity $\alpha(c) \sqsubseteq a$.

---

### Ex. 6: Round-trips

**Exercise:** Prove $\gamma \circ \alpha \circ \gamma = \gamma$ and $\alpha \circ \gamma \circ \alpha = \alpha$.

1. **For $\gamma$:** By extensivity (Ex. 1), $\gamma(a) \le \gamma(\alpha(\gamma(a)))$. By reductivity (Ex. 2) and monotonicity of $\gamma$, $\gamma(\alpha(\gamma(a))) \le \gamma(a)$. By antisymmetry, $\gamma(\alpha(\gamma(a))) = \gamma(a)$.
2. **For $\alpha$:** By reductivity, $\alpha(\gamma(\alpha(c))) \sqsubseteq \alpha(c)$. By extensivity and monotonicity of $\alpha$, $\alpha(c) \sqsubseteq \alpha(\gamma(\alpha(c)))$. By antisymmetry, $\alpha(\gamma(\alpha(c))) = \alpha(c)$.

---

### Ex. 7: Idempotency

**Exercise:** Prove that $\gamma \circ \alpha$ and $\alpha \circ \gamma$ are idempotent.

1. For $\gamma \circ \alpha$: $(\gamma \circ \alpha) \circ (\gamma \circ \alpha) = \gamma \circ (\alpha \circ \gamma \circ \alpha) = \gamma \circ \alpha$ (using Ex. 6).
2. For $\alpha \circ \gamma$: $(\alpha \circ \gamma) \circ (\alpha \circ \gamma) = \alpha \circ (\gamma \circ \alpha \circ \gamma) = \alpha \circ \gamma$ (using Ex. 6).

---

### Ex. 8: $\gamma$ induces $\alpha$

**Exercise:** Prove $\alpha(c) = \sqcap { a \mid c \le \gamma(a) }$.

1. By the GC property, $c \le \gamma(a) \iff \alpha(c) \sqsubseteq a$.
2. The set ${ a \mid c \le \gamma(a) }$ is therefore equal to the set ${ a \mid \alpha(c) \sqsubseteq a }$, which is the set of all upper bounds of $\alpha(c)$.
3. The greatest lower bound (glb) of the set of all upper bounds of an element is the element itself. Thus, $\sqcap { a \mid \alpha(c) \sqsubseteq a } = \alpha(c)$.

---

### Ex. 9: $\alpha$ induces $\gamma$

**Exercise:** Prove $\gamma(a) = \vee { c \mid \alpha(c) \sqsubseteq a }$.

1. By the GC property, $\alpha(c) \sqsubseteq a \iff c \le \gamma(a)$.
2. The set ${ c \mid \alpha(c) \sqsubseteq a }$ is therefore equal to the set ${ c \mid c \le \gamma(a) }$, which is the set of all lower bounds of $\gamma(a)$.
3. The least upper bound (lub) of the set of all lower bounds of an element is the element itself. Thus, $\vee { c \mid c \le \gamma(a) } = \gamma(a)$.

---

### Ex. 10: $\alpha$ preserves lubs

**Exercise:** Prove $\alpha(\vee X) = \sqcup { \alpha(x) \mid x \in X }$ whenever the concrete lub $\vee X$ exists.

1. By monotonicity (Ex. 3), for any $x \in X$, $x \le \vee X \implies \alpha(x) \sqsubseteq \alpha(\vee X)$. Thus, $\alpha(\vee X)$ is an upper bound of ${\alpha(x) \mid x \in X}$.
2. Let $a$ be any other upper bound such that $\forall x \in X, \alpha(x) \sqsubseteq a$.
3. By the GC property, this is equivalent to $\forall x \in X, x \le \gamma(a)$.
4. This means $\gamma(a)$ is an upper bound of $X$. Since $\vee X$ is the _least_ upper bound, $\vee X \le \gamma(a)$.
5. Applying the GC property again, $\alpha(\vee X) \sqsubseteq a$. Thus, $\alpha(\vee X)$ is the least upper bound.

---

### Ex. 11: $\gamma$ preserves glbs

**Exercise:** Prove $\gamma(\sqcap Y) = \wedge { \gamma(y) \mid y \in Y }$ whenever the abstract glb $\sqcap Y$ exists.

1. By monotonicity (Ex. 4), for any $y \in Y$, $\sqcap Y \sqsubseteq y \implies \gamma(\sqcap Y) \le \gamma(y)$. Thus, $\gamma(\sqcap Y)$ is a lower bound of ${\gamma(y) \mid y \in Y}$.
2. Let $c$ be any other lower bound such that $\forall y \in Y, c \le \gamma(y)$.
3. By the GC property, this is equivalent to $\forall y \in Y, \alpha(c) \sqsubseteq y$.
4. This means $\alpha(c)$ is a lower bound of $Y$. Since $\sqcap Y$ is the _greatest_ lower bound, $\alpha(c) \sqsubseteq \sqcap Y$.
5. Applying the GC property again, $c \le \gamma(\sqcap Y)$. Thus, $\gamma(\sqcap Y)$ is the greatest lower bound.

---

### Ex. 12: Surjectivity/Injectivity and Galois Insertion

**Exercise:** Prove that in a Galois Connection, $\alpha$ is surjective iff $\gamma$ is injective iff $\alpha \circ \gamma = id_A$.

1. **$\alpha \circ \gamma = id_A \implies \gamma$ is injective:** If $\gamma(a_1) = \gamma(a_2)$, then $\alpha(\gamma(a_1)) = \alpha(\gamma(a_2))$, which means $id_A(a_1) = id_A(a_2) \implies a_1 = a_2$.
2. **$\alpha \circ \gamma = id_A \implies \alpha$ is surjective:** For any $a \in A$, let $c = \gamma(a)$. Then $\alpha(c) = \alpha(\gamma(a)) = a$.
3. **$\gamma$ is injective $\implies \alpha \circ \gamma = id_A$:** From Ex. 6, $\gamma(\alpha(\gamma(a))) = \gamma(a)$. If $\gamma$ is injective, then $\alpha(\gamma(a)) = a$.
4. **$\alpha$ is surjective $\implies \alpha \circ \gamma = id_A$:** For any $a \in A$, there exists $c$ such that $\alpha(c) = a$. Then $\alpha(\gamma(a)) = \alpha(\gamma(\alpha(c))) = \alpha(c) = a$ (using Ex. 6).

---

### Summary of key properties used

- **Definition 2.1:** Poset (reflexive, antisymmetric, transitive).
- **Definition 2.3:** CPO (pointed poset where chains have lubs).
- **Definition 2.4/2.5:** (Complete) Lattice (existence of lubs and glbs).
- **Definition 2.12:** Galois Connection ($c \le \gamma(a) \iff \alpha(c) \sqsubseteq a$).
- **Definition 2.13:** Galois Embedding/Insertion ($\alpha$ is surjective, $\gamma$ is injective, $\alpha \circ \gamma = id$).
- **Theorem 2.3:** Alternate characterization of GC (monotonicity, extensivity, reductivity).
- **Theorem 2.4:** Properties of GC (round-trips, idempotency, induction of adjoints, preservation of limits).

Does this comprehensive walkthrough of the Galois insertion exercises clarify the relationships between the concrete and abstract worlds, or would you like to see a practical application in **Sign Analysis**?

# Abstract Analysis

![[Pasted image 20260702160921.png]]

![[Pasted image 20260702160935.png]]

$F^\#$ is correct on an abstract domain A whenever it returns a correct approximation of the result of the concrete computation

$F^\# \sqsupseteq \alpha \circ F \circ \gamma = F^A$

$F^\#$ is complete on an abstract domain A whenever it returns the best abstraction of the result of the concrete computation

$F^\# \circ \alpha = \alpha \circ F$

$F^\#$ is complete $\implies F^\# = F^A$
$\alpha \circ F = F^\# \circ \alpha \implies F^A = \alpha F \gamma = F^\# \circ \alpha \circ \gamma = F^\#$

if F monotone and $F^\#$ correct then $lfp(F^\#)$ is a correct over-approx of lfp(F)

![[Pasted image 20260702161701.png]]

If F monotone and $F^A$ is complete then $\alpha(lfp(F)) = lfp(F^A)$


![[Pasted image 20260702161728.png]]

![[Pasted image 20260702161743.png]]

$$
(A,\sqsubseteq) \; a \sqsubseteq b \implies \gamma(a) \subseteq \gamma(b)
$$
$$
c \subseteq \gamma(a) \implies \gamma(\alpha(c)) \subseteq \gamma(a)
$$
$$
a_1,a_2 \subseteq a_1 \sqcup a_2 \; (union)
$$

$$
a_1 \sqcup a_2 \sqsubseteq a_1 \nabla a_2 \;(widening)
$$

![[Pasted image 20260712192206.png]]

![[Pasted image 20260702161818.png]]

## Exercises:
### Classification Exercise (Slides 294–296)

**Problem:** Classify whether each abstract property belongs to a **relational** or **non-relational** abstract domain and justify why.

- **(a) Signs:** **Non-relational.** This domain abstracts the set of possible values for each variable independently from others.
- **(b) Parity:** **Non-relational.** Like signs, parity tracks a property (even or odd) of a single variable's value without considering its relationship to other variables.
- **(c) Intervals around 0 ($[-l, r]$):** **Non-relational.** This is a variation of the interval domain that constrains the range of a single variable.
- **(d) Equalities ($c_1 \cdot x = c_2 \cdot y$):** **Relational.** These properties capture numerical constraints and dependencies between two or more variables.
- **(e) Inequalities ($c_1 \cdot x \neq c_2 \cdot y$):** **Relational.** Similar to equalities, these define a specific logical relationship between variables $x$ and $y$.

---

### Completeness 1 (Slide 312)

**Problem:** Given $P \triangleq { -7, 5 }$ and $c \triangleq (x < 0)?; x := -x$, compute the abstract semantics $[[c]]^\#$ on the **Sign** domain for $\alpha_{Sign}(P)$ and compare it with $\alpha_{Sign}([[c]]P)$.

**1. Abstraction of the input:**

- $\alpha_{Sign}({ -7, 5 }) = \mathbb{Z}$. Since the set $P$ contains both a negative and a positive number and the Sign domain does not have a "non-zero" element, the most precise abstraction is **Top** ($\mathbb{Z}$).

**2. Abstract Semantics $[[c]]^\# \mathbb{Z}$:**

- Apply the guard $(x < 0)?^\#$: In the Sign domain, filtering Top with "negative" results in $\mathbb{Z}_{<0}$.
- Apply the assignment $x := -x^\#$: Negating a negative sign results in a positive sign. Thus, $-^\# (\mathbb{Z}_{<0}) = \mathbb{Z}_{>0}$.
- **Result:** $[[c]]^\# \alpha_{Sign}(P) = \mathbb{Z}_{>0}$.

**3. Concrete Semantics and its Abstraction:**

- $[[c]] { -7, 5 }$: The guard $(x < 0)?$ filters the set to ${ -7 }$. The assignment $x := -x$ transforms it to ${ 7 }$.
- $\alpha_{Sign}({ 7 }) = \mathbb{Z}_{>0}$.

**Final Answer:** The abstract transformer is **complete** for this example because $[[c]]^\# \alpha(P) = \alpha([[c]]P) = \mathbb{Z}_{>0}$.

---

### Completeness 2 (Slide 313)

**Problem:** Determine if the Best Correct Approximation (BCA) of $f(x) = x$ if $x \leq 10$ (and a different branch for $x > 10$) is complete on the **Interval** domain.

**Solution:** A function $f$ is complete on the Interval domain if its abstract counterpart matches the abstraction of the concrete result: $\alpha(f(S)) = f^A(\alpha(S))$.

- If the "otherwise" branch makes $f$ **non-monotone** (e.g., $f(11) = 0$), completeness fails.
- **Counterexample:** Let $S = {10, 11}$. Then $\alpha(S) =$.
- $\alpha(f(S)) = \alpha({10, 0}) =$.
- $f^A(\alpha(S)) = \alpha(f()) = \alpha({10, 0}) =$. (In this specific case it might seem complete).
- However, generally, piecewise functions that "break" an interval into non-contiguous sets (like the absolute value $|x|$) are **not complete** on intervals because the interval hull $\alpha$ introduces spurious values that were not in the concrete image.

**Final Answer:** Generally, the BCA of such a piecewise function is **not complete** because the abstraction of the image of an interval often includes values that the concrete function would never reach.

---

### Completeness 3 (Slide 313)

**Problem:** Given the domain $A = { \top, \bot, <0, \ge 0 }$: (a) define $\gamma$ and $\alpha$, and (b) determine if it admits a complete abstract multiplication.

**(a) Formal Definitions:**

- **Concretization ($\gamma$):**
    - $\gamma(\bot) = \emptyset$
    - $\gamma(<0) = { n \in \mathbb{Z} \mid n < 0 }$
    - $\gamma(\ge 0) = { n \in \mathbb{Z} \mid n \ge 0 }$
    - $\gamma(\top) = \mathbb{Z}$
- **Abstraction ($\alpha$):**
    - $\alpha(S) = \bot$ if $S = \emptyset$
    - $\alpha(S) = (<0)$ if $S \neq \emptyset \land S \subseteq { n \mid n < 0 }$
    - $\alpha(S) = (\ge 0)$ if $S \neq \emptyset \land S \subseteq { n \mid n \ge 0 }$
    - $\alpha(S) = \top$ otherwise.

**(b) Multiplication Completeness:** To be complete, $\alpha(n \times m) = \alpha(n) \times^# \alpha(m)$ must hold.

- **Counterexample:** Let $n = -1$ and $m = 0$.
- Concrete: $n \times m = 0$. $\alpha(0) = (\ge 0)$.
- Abstract: $\alpha(-1) = (<0)$ and $\alpha(0) = (\ge 0)$.
- $((<0) \times^# (\ge 0)) = \alpha({ x \cdot y \mid x < 0, y \ge 0 })$.
- The set of products is ${ z \in \mathbb{Z} \mid z \le 0 }$.
- In this domain, the set ${ z \le 0 }$ contains both negative and non-negative (zero) values. Since there is no "non-positive" element, it must be abstracted to **$\top$**.
- **Result:** $\alpha(0) \neq \top$.

**Final Answer:** The domain **does not admit a complete multiplication operator** because it lacks the precision to represent the "non-positive" result ${ z \leq 0 }$ specifically.

Does this clarify the relationship between domain expressiveness and completeness, or should we look at the **Reduced Product** construction next?
# Local Completeness Logic

$A(.) = \gamma(\alpha(.))$

![[Pasted image 20260702162734.png]]

![[Pasted image 20260702162942.png]]

![[Pasted image 20260702162956.png]]

Completeness equation: $\forall P.A([[e]]P) = A([[e]]A(P))$

if a test *b* is complete in A, then *b* and $\lnot \textit{b}$ are expressible in A

Proof:
![[Pasted image 20260702165506.png]]

Let *b* and $\lnot \textit{b}$ be expressible in A.
The test *b* is complete in A $\iff$ the join of any two abstract points below *b* and $\lnot \textit{b}$ is expressible.

Local completeness equation: $A([[c]]P)=A([[c]]A(P))$

We say that e is locally complete in A for input P and write $\mathbb{C}_P^A(e)=A([[c]]P)=[[c]]^\#A(P)$

![[Pasted image 20260702164105.png]]

![[Pasted image 20260702164119.png]]

![[Pasted image 20260702164140.png]]

A LCL triple $\vdash_A [P]c[Q]$ is valid if $Q \subseteq [[c]]P \subseteq A(Q)$

if $\vdash_A [P]c[Q]$ then $Q \subseteq [[c]]P \subseteq A(Q) = [[c]]^\#_A A(P)$

Proof:
By induction on the derivation

if A is complete for any atomic command in *c*, then any valid triple $\vdash_A [P]c[Q]$ can be derived

Proof:
1) derive $\vdash_A [P]c[\;[[c]]P\;]$
2) use \[relax\] with $Q \subseteq [[c]]P$

For any Turing complete language and any non-trivial abstraction A, there are valid triples that cannot be proved

![[Pasted image 20260702164945.png]]

![[Pasted image 20260712234805.png]]
# HL

{P}c{Q} $\iff [[c]]P \subseteq Q$
- P = precondition
- Q = postcondition

Whenever *c* is executed in a state satisfying *P* if the execution of *c* terminates, it terminates in a state satisfying *Q*

We talk about partial correctness because the previous semantic condition does not guarantee that the execution of *c* on states satisfying *P* terminate

*Q* is an over-approximation of the states that can be reached by states in *P*

\[Floyd] forward oriented
\[Hoare] backward oriented

>Soundness:
>Th. Any derivable HL triple is valid
>Proof. By induction on the derivation tree

The variant expresses a general condition that is true for every execution, but is still strong enough to guarantee the desired postcondition when the loop terminates

\[cons] forward/backward strengthening *P* and weakening *Q*

Total correctness = partial correctness + termination

$wlp(c,Q) \triangleq \{\sigma \in \Sigma \;| \;[[c]]\{\sigma\} \subseteq Q\}$

$P \implies wlp(c,Q) \iff [[c]]P \subseteq Q$

if b then c1 else c2 $\triangleq (b?;c_1)+(\lnot b?;c_2)$
while b do c $\triangleq (b?;c)^*;\lnot b?$

![[Pasted image 20260702184239.png]]

![[Pasted image 20260704173157.png]]

## Exercises:

### 1
La dimostrazione della correttezza (soundness) della regola di congiunzione ${conj}$ in Hoare Logic si basa sulla **monotonia** della semantica collettiva $[[ c ]]$.
$$\frac{{P_1} c {Q_1} \quad {P_2} c {Q_2}}{{P_1 \land P_2} c {Q_1 \land Q_2}}$$

#### **Dimostrazione**

1. **Assunzione:** Ipotizziamo che le premesse siano valide. Per definizione di validità in HL, ciò significa che:
    - $[[ c ]] P_1 \subseteq Q_1$
    - $[[ c ]] P_2 \subseteq Q_2$
2. **Proprietà di Monotonia:** La semantica di un comando $[[ c ]]$ è una funzione monotona (se $A \subseteq B \implies [[ c ]] A \subseteq [[ c ]] B$).
3. **Applicazione alla congiunzione:** Consideriamo l'input $P_1 \cap P_2$ (che corrisponde logicamente a $P_1 \land P_2$):
    - Poiché $(P_1 \cap P_2) \subseteq P_1$, per monotonia abbiamo $[[ c ]](P_1 \cap P_2) \subseteq [[ c ]] P_1 \subseteq Q_1$.
    - Poiché $(P_1 \cap P_2) \subseteq P_2$, per monotonia abbiamo $[[ c ]](P_1 \cap P_2) \subseteq [[ c ]] P_2 \subseteq Q_2$.
4. **Conclusione:** Dato che il risultato $[[ c ]](P_1 \cap P_2)$ è contenuto sia in $Q_1$ che in $Q_2$, deve essere contenuto nella loro intersezione: $$[[ c ]](P_1 \cap P_2) \subseteq Q_1 \cap Q_2$$ Questo dimostra che la tripla ${P_1 \land P_2} c {Q_1 \land Q_2}$ è semanticamente valida, rendendo la regola **sound**.

### 2
Show that the following rule for assignment is not sound

$$\frac{}{\{P\}x:=a\{P[a/x]\}}$$
Questa regola non è corretta (**unsound**) perché tenta di applicare la sostituzione sintattica nel "verso sbagliato" rispetto alla semantica dell'assegnamento.

Ecco un **controesempio** per dimostrarne l'invalidità:

1. **Istanza:** Consideriamo $P \triangleq (y = x)$ e il comando $x := 0$.
2. **Applicazione della regola:** La regola produrrebbe la tripla $\{y = x\} x := 0 \{y = 0\}$, poiché sostituendo $0$ al posto di $x$ in $P$ si ottiene $y = 0$.
3. **Verifica semantica:**
    - Partiamo da uno stato iniziale $\sigma = [x \mapsto 1, y \mapsto 1]$. Questo stato soddisfa la pre-condizione ($1 = 1$).
    - Eseguiamo il comando $x := 0$. Il nuovo stato sarà $\delta = [x \mapsto 0, y \mapsto 1]$.
    - Verifichiamo la post-condizione nello stato finale: $y = 1$, quindi l'asserzione $y = 0$ è **falsa**.
4. **Conclusione:** Poiché esiste un'esecuzione che termina in uno stato che non soddisfa la post-condizione, la tripla non è valida e la regola è **unsound**.

Le regole corrette (sound) sono quelle di **Hoare** (orientata all'indietro: ${Q[a/x]} x := a {Q}$) o di **Floyd** (orientata in avanti con quantificatori).

# IL

$[P]c[Q] \iff [[c]]P \supseteq Q$

![[Pasted image 20260702184115.png]]

![[Pasted image 20260702184128.png]]

![[Pasted image 20260702184143.png]]

![[Pasted image 20260710190911.png]]

![[Pasted image 20260710190922.png]]

![[Pasted image 20260710191235.png]]

![[Pasted image 20260702184229.png]]

![[Pasted image 20260710191626.png]]

![[Pasted image 20260710192020.png]]

![[Pasted image 20260702184532.png]]

![[Pasted image 20260702184606.png]]

$[P]c[\epsilon:Q]$
- ok: normal (successful) exec
- er: erroneous exec

![[Pasted image 20260710192732.png]]

\[frame] assigned variables in c are disjoint from free variables in R

![[Pasted image 20260702185501.png]]

![[Pasted image 20260704165228.png]]

![[Pasted image 20260704165249.png]]

>Soundness:
>Th.Any derivable IL triple is valid
>Proof.By induction on the derivation tree

>(Relative) Completeness:
>Th. Any valid IL triple can be derived, provided we have an oracle to decide implications
>Proof sketch. (Assuming an oracle to decide implications.) Solution: we go semantic! P and Q are sets of states, implications is subset inclusion, no issues with finiteness.
>![[Pasted image 20260704165730.png]]
>![[Pasted image 20260704165740.png]]
>![[Pasted image 20260704165825.png]]
>![[Pasted image 20260704165838.png]]

![[Pasted image 20260704173249.png]]
# NC

$[[c]]^{op} \triangleq \{\sigma \; | \; \delta \in [[c]]\sigma\}$ -> weakest possible precondition (wpp)

$\sigma \in [[c]]^{op}\delta \iff \delta \in [[c]]\sigma$

$[[c]]^{op}Q = \bigcup_{\delta \in Q} [[c]]^{op}\delta$

specification = What my code should do and should not do

![[Pasted image 20260704170744.png]]

The idea of NC is to prevent the invocation of the function with arguments that will inevitably lead to some error

$(P)c(Q) \iff [[c]]^{op}Q \subseteq P$

Given Q the set of good final states (the specification), the NC triple means that any states $\sigma$ that admits at least one non-erroneous execution of c is in P

![[Pasted image 20260704171837.png]]

$\sigma \in wlp(c,Q) \implies B(\sigma) = \emptyset$

![[Pasted image 20260704172825.png]]

![[Pasted image 20260704172847.png]]

$\{P\}c\{Q\} \iff (\lnot P)c(\lnot Q)$

$[[c]]P \subseteq Q \iff [[c]]^{op}(\lnot Q) \subseteq \lnot P$

![[Pasted image 20260704173222.png]]

## Other:
![[Pasted image 20260711182642.png]]

In base all'**isomorfismo tra Necessary Condition Logic (NC) e Hoare Logic (HL)**, la validità di una tripla NC $(P)c(Q)$ è equivalente alla validità della tripla di Hoare ${\neg P}c{\neg Q}$.

Ecco l'analisi della validità per i casi da te elencati:

### **1. Triple sempre valide (per ogni $c, P, Q$)**

Queste triple NC sono valide perché i loro equivalenti in HL sono assiomi fondamentali del sistema:

- **(true) $c$ (Q) $\iff$ {false} $c$ {$\neg$Q}**: Questa tripla è **sempre valida**. In HL, una pre-condizione `false` rende la tripla vacuamente vera poiché non esiste alcuno stato iniziale che la soddisfi.
- **(P) $c$ (false) $\iff$ {$\neg$P} $c$ {true}**: Questa tripla è **sempre valida**. In HL, una post-condizione `true` è sempre soddisfatta da qualsiasi stato finale raggiunto dal programma.

### **2. Triple generalmente non valide**

La loro validità dipende dal comportamento specifico del comando $c$ e non può essere garantita a priori:

- **(false) $c$ (Q) $\iff$ {true} $c$ {$\neg$Q}**: È valida solo se il programma $c$, partendo da qualsiasi stato, termina sempre in $\neg Q$ o diverge. Poiché non è vera per ogni $c$, la tripla NC non è universalmente valida.
- **(P) $c$ (true) $\iff$ {$\neg$P} $c$ {false}**: È valida solo se il programma $c$ diverge (va in loop infinito) per ogni stato iniziale in $\neg P$. In caso di terminazione, la post-condizione `false` non sarebbe soddisfatta, rendendo la tripla NC non valida.

**In sintesi:** Mentre in HL è "facile" essere corretti partendo da `false` o arrivando a `true`, in NC la validità universale si ottiene quando la pre-condizione è `true` (perché è sempre possibile trovare un'esecuzione corretta partendo da "ovunque" se la precondizione HL è falsa) o la post-condizione è `false`.

# SIL

![[Pasted image 20260704174515.png]]

$\langle P \rangle c \langle Q\rangle$ is valid when $[[c]]^{op}Q \supseteq P$

$\forall \sigma \in P. \exists \delta \in Q.\delta \in [[c]]\sigma$

A backward under-approximation logic to expose some initial states leading to errors

![[Pasted image 20260704174111.png]]

Q is a manifest error $\iff \langle true \rangle c \langle Q \rangle$ is valid

![[Pasted image 20260704174213.png]]

>Soundness:
>Th. All provable SIL triples are valid

>Completeness:
>Th. All valid triples are provable (using core rules)

# SL

HL + pointers

![[Pasted image 20260704180156.png]]

![[Pasted image 20260704180256.png]]

![[Pasted image 20260704180335.png]]

![[Pasted image 20260704180400.png]]

![[Pasted image 20260704180413.png]]

![[Pasted image 20260704180439.png]]

![[Pasted image 20260704180516.png]]

![[Pasted image 20260704180522.png]]

![[Pasted image 20260704180534.png]]

![[Pasted image 20260704180543.png]]

![[Pasted image 20260704180557.png]]

![[Pasted image 20260704180618.png]]

![[Pasted image 20260704180629.png]]

![[Pasted image 20260704180636.png]]

![[Pasted image 20260704180647.png]]

![[Pasted image 20260704180656.png]]

![[Pasted image 20260704180814.png]]

>Correctness:
>Th. if {P}c{Q} then $[[c]]P \subseteq Q$
>Proof. By induction on the derivation

>Incompleteness:
>Th. There exist valid SL triples that are not provable
>Proof. Footprint

$a \doteq b \triangleq (a=b) \land emp$

>Footprint:
>1. Derive the spec of *c* using local axioms
>2. Apply rule frame to complete the specification

# ISL

ISL = IL + SL

![[Pasted image 20260704182558.png]]

track deallocated locations

![[Pasted image 20260704182837.png]]

![[Pasted image 20260704182624.png]]

>Correctness:
>Th. if $[P]c[\epsilon : Q]$ then $Q \subseteq [[c]]\epsilon(P)$
>Proof. By induction on the derivation

>Footprint:
>Th. Any valid ISL triple $[\sigma_P]c[\epsilon: \sigma_P]$ can be derived

![[Pasted image 20260704183352.png]]

# SepSIL

SepSIL = SIL + IL

![[Pasted image 20260704183430.png]]

![[Pasted image 20260704183500.png]]

![[Pasted image 20260704184006.png]]

>Correctness:
>Th. if $\langle P \rangle c \langle Q \rangle$ then $P \subseteq [[c]]^{op}Q$
>Proof. by induction on the derivation

>Completeness:
>Th. Any valid triple $\langle P \rangle c \langle Q \rangle$ can be derived


# Intro-AI

Abstract interpretation = A powerful framework for designing correct static analyses: simple and eye-opening

The concretization $\gamma(a)$ of an abstract element $a$ is the set of program states that satisfy it.



![[Pasted image 20260704184510.png]]

Abstractions:
- Non-Relational:
	- signs $[x \le 0, y \ge 0]$
	- intervals $[1 \le x, 1 \le y]$ -> more expressive than signs
- Relational:
	- Convex Polyhedra $[c_1x+c_2y \le c]$ -> more expressive than intervals, Computing the best abstraction can be expensive or sometimes not even possible

Compositionality principle:
compute a sound analysis of a program by computing sound abstract semantics of program’s components

![[Pasted image 20260704184943.png]]

![[Pasted image 20260704184954.png]]

![[Pasted image 20260712170801.png]]

![[Pasted image 20260704185017.png]]

![[Pasted image 20260704185035.png]]

Rice’s Theorem: Every non-trivial semantic property of programs is undecidable

Static analysis -> "not YES" means "Don't know"
 
![[Pasted image 20260704185238.png]]

![[Pasted image 20260704185254.png]]

![[Pasted image 20260704185349.png]]

![[Pasted image 20260704185402.png]]

![[Pasted image 20260704185455.png]]

![[Pasted image 20260704185502.png]]

![[Pasted image 20260704185512.png]]

![[Pasted image 20260704185521.png]]

# CFA for FUN

![[Pasted image 20260705002038.png]]

The purpose of Control Flow Analysis (CFA) is to determine which blocks may lead to which other blocks But in modern languages, even building the CFG is not trivial

intraprocedural analysis: → analyze a single function

interprocedural analysis: → analyze the whole program with function calls (tractable when the program has a simple structure → calls have statically known targets)

dynamic dispatch problem = variables can denote functions and which procedure/function gets invoked depends on runtime values

Solution: static analysis 
→ over-approximate the possible targets of each call We cannot know the exact target of a call Control Flow Analysis (CFA):
→ For each function application (call site), compute a safe approximation

Associate for each variable and each expression , a safe over-approximation of the set of functions that they may evaluate to at runtime

0-CFA is a Constraint Based Analysis

specification: describes when the analysis results are acceptable
computation: solving the constraints derived by the specification

![[Pasted image 20260705173615.png]]

$\hat{C}:l \mapsto$ set of function abstractions the sub-expr labelled l may evaluate to

$\hat{\rho}:l \mapsto$ set of function abstractions x may be bound to

for each $(t^{l_1}_1 t^{l_2}_2)^l$ determine the possibile functions for $t_1$ from set of function abstractions $t_2$ may evaluate to

0-CFA means that no context information is considered, e.g., same function set at all call sites

![[Pasted image 20260705174234.png]]

![[Pasted image 20260705174319.png]]

Rules:
- \[con] always true
- \[var] propagates info from vars to program points ($from \; \hat{\rho} \; to \; \hat{C}$)
- \[fn] functional term must be included in $\hat{C}(l)$ (no checks on body)
- \[fun] functional term must be included in $\hat{C}(l)$ (no checks on body)
- \[if] check on sub-exprs, propagates the values produced by sub-exprs $\hat{C}(l_i)$ to the overall expression $\hat{C}(l)$ (merging the possible values from both branches)
- \[op] checks on sub-exprs (no track data values)
- \[let] checks on sub-exprs, propagation of the values:
	- $\hat{C}(l_1) \subseteq \hat{\rho}(x)$ (binding)
	- $\hat{C}(l_2) \subseteq \hat{C}(l)$ (evaluation)
- \[app] (simulate all possible calls):
	- checks on sub-exprs
	- for each function the can be applied:
		- check on body
		- bind argument (via $\hat{\rho}(x)$)
		- propagate results (results merged in $\hat{C}(l)$)

![[Pasted image 20260705180143.png]]

In this way, we analyse the body of a function only if the function may be applied somewhere Unreachable functions are not analysed

Circular dependency => coinduction: assume it holds and verify it is preserved

![[Pasted image 20260705180243.png]]

flow-insensitive: it computes a single abstract value for each variable (or expression) that over-approximates all values it may take during execution, without distinguishing between different program points or execution orders

![[Pasted image 20260713001642.png]]

context-insensitive: the same function is analyzed in the same way at all call sites

![[Pasted image 20260713001704.png]]

![[Pasted image 20260705180348.png]]

![[Pasted image 20260705180400.png]]

![[Pasted image 20260705180451.png]]

![[Pasted image 20260705180523.png]]

Rules:
- \[var] The value of a variable is obtained from the environment
- \[fn] This axiom constructs the appropriate closure, it restricts the environment $\rho$ to the free variables of the abstraction (only free variables are kept)
- \[let] The expression $e_2$ is evaluated in the environment augmented with the new binding
- \[app] This axiom describes the binding of the actual parameter to the formal parameter
- \[bind] The bind construct is evaluated by repeatedly applying $[bind_1]$, The final evaluation result is get by using rule $[bind_2]$

![[Pasted image 20260706141855.png]]

![[Pasted image 20260706141912.png]]

![[Pasted image 20260706142142.png]]

![[Pasted image 20260706142202.png]]

![[Pasted image 20260706142819.png]]

![[Pasted image 20260706142832.png]]

![[Pasted image 20260706142841.png]]

![[Pasted image 20260706142850.png]]

![[Pasted image 20260706142907.png]]

![[Pasted image 20260706142933.png]]

![[Pasted image 20260706143022.png]]

![[Pasted image 20260706143118.png]]

![[Pasted image 20260706143132.png]]

![[Pasted image 20260706143144.png]]

![[Pasted image 20260706143251.png]]

![[Pasted image 20260706143401.png]]

![[Pasted image 20260706143419.png]]

![[Pasted image 20260706143545.png]]

## Syntax directed CFA

![[Pasted image 20260706144213.png]]

![[Pasted image 20260706144232.png]]

Rules:
- \[fn] Function body $e_0$ is now analyzed at definition time, even if the function is never applied
- \[fun] Function body $e_0$ is now analyzed at definition time, even if the function is never applied, checks on the recursive binding for \[fun] is included: self-binding is enforced immediately
- \[app] The body constraints have already been generated by \[fn]
- All other rules are unchanged: just replace ⊧ with $⊧_s$

![[Pasted image 20260706145522.png]]

No circular dependency => no need of coinduction

![[Pasted image 20260706145633.png]]

![[Pasted image 20260706145950.png]]

![[Pasted image 20260706150046.png]]

![[Pasted image 20260706150119.png]]

![[Pasted image 20260706150142.png]]

![[Pasted image 20260706150155.png]]

![[Pasted image 20260706150410.png]]

![[Pasted image 20260706150424.png]]

\[app] guard operand analysis 

![[Pasted image 20260706152047.png]]

## Reachability CFA

![[Pasted image 20260706152103.png]]

Rules:
- \[fn] Function body $e_0$ is analysed at definition time, but only if the function is applied somewhere
- \[var] x is analyzed only if reachable
- \[app] If the function possibly occurs in an application, then this means it is reachable
- All other rules are unchanged: just replace $⊧_s$ with $⊧'_s$

![[Pasted image 20260706152622.png]]

![[Pasted image 20260706152631.png]]

![[Pasted image 20260706152645.png]]

## Constraint Based 0-CFA

![[Pasted image 20260706153017.png]]

![[Pasted image 20260706153044.png]]

Rules:
- \[con] $\emptyset$ constants generate no constraints
- \[var] Variables generate a constraint reflecting a flow from r(x) to C(ℓ)
- \[fn] generate a flow constraint, and, recursively, constraints from the body
- \[fun] generate a flow constraint, and, recursively, constraints from the body (recursive binding: function flows to f)
- \[app] Application generates recursively constraints from its terms plus the body conditional constraints

![[Pasted image 20260706153450.png]]

![[Pasted image 20260706153505.png]]

![[Pasted image 20260706153516.png]]

![[Pasted image 20260706153540.png]]

![[Pasted image 20260706153552.png]]

Constraint graph:
- Nodes
	- a node $C(l)$ for each label $l \in Lab_*$
	- a node $r(x)$ for each variable $x \in Var_*$
- Edges
	- Each constraint $p_1 \subseteq p_2$ adds an initial edge $(p_1,p_2)$ to the graph
	- each constraint $\{t\} \subseteq p \implies p_1 \subseteq p_2$ adds
		- a candidate edge $(p_1,p_2)$, with "trigger" $\{t\} \subseteq p$, and
		- an edge $(p,p_2)$

![[Pasted image 20260706154922.png]]

![[Pasted image 20260706155228.png]]

![[Pasted image 20260706155245.png]]

Constraint solving = graph reachability + propagation

![[Pasted image 20260706155301.png]]

D = current knowledge
E = how knowledge propagates
W = what still needs to be processed

The algo:
1. Initialize all the data structures D, E and W to \[]
2. ![[Pasted image 20260706155852.png]]
3. ![[Pasted image 20260706155906.png]]
4. $\forall l \in Lab_* : \hat{C}(l):= D[C(l)]$
5. $\forall x \in Var_* : \hat{\rho}(x) := D[r(x)]$

Complexity = $O(n^3)$

![[Pasted image 20260706160245.png]]

![[Pasted image 20260706160256.png]]

![[Pasted image 20260706160310.png]]

![[Pasted image 20260706160349.png]]

## CFA + DFA

![[Pasted image 20260706160409.png]]

![[Pasted image 20260706160421.png]]

![[Pasted image 20260706160434.png]]

![[Pasted image 20260706160454.png]]

Rules:
- \[con] We now track data values: the CFA records that $d_c$ is a possible valude of c (Constants introduce abstract data into the analysis)
- \[if] Increased precision: we analyze only those branches consistent with the abstract value of the condition, which now is trackable (control-flow is now filtered by data-flow)
- \[op] we do track data values, This rule applies abstract operators to propagate data-flow information Data-flow is computed locally using abstract operators

![[Pasted image 20260706160640.png]]

![[Pasted image 20260706160653.png]]

![[Pasted image 20260706160703.png]]

![[Pasted image 20260706160711.png]]

![[Pasted image 20260706160737.png]]

Rules:
- \[con] At label l, he abstract data value of must be recorded l tells us which abstract value a constant contributes (Constants inject data-flow information into the analysis)
- \[op] Now, we use the component f (Compute the abstract result of the operation and propagate it to the result label)
- \[if] analyze condition, use abstract boolean value and propagate only analysed branches

![[Pasted image 20260706160952.png]]

![[Pasted image 20260706161008.png]]

![[Pasted image 20260706161026.png]]

## Uniform k-CFA

![[Pasted image 20260706161042.png]]

![[Pasted image 20260706161049.png]]

![[Pasted image 20260706161058.png]]

![[Pasted image 20260706161105.png]]

![[Pasted image 20260706161112.png]]

![[Pasted image 20260706161120.png]]

![[Pasted image 20260706161134.png]]

Rules:
- \[var] We look up in the context where it was bound and propagate it to the current context
	- ce(x) context where x was defined
	- $\delta$ current context (where we use x)
	- A variable carries the context where it was created, but is used in the current context
- \[fn]![[Pasted image 20260706161242.png]]
- \[let] check sub-exprs, ![[Pasted image 20260706161325.png]]
- \[app] both and are bound in the new calling context $\delta_0$ when analyzing the body

![[Pasted image 20260706161413.png]]

![[Pasted image 20260706161426.png]]

![[Pasted image 20260706161437.png]]

![[Pasted image 20260706161446.png]]

![[Pasted image 20260706161453.png]]

![[Pasted image 20260706161501.png]]

## Cartesian Product Algo (CPA)

![[Pasted image 20260706161529.png]]

![[Pasted image 20260706161538.png]]

Rules:
- \[app] each argument flows to its corresponding parameter

![[Pasted image 20260706161640.png]]

![[Pasted image 20260706161648.png]]

![[Pasted image 20260706161707.png]]

![[Pasted image 20260706161717.png]]

# 0-CFA $\pi-calculus$

**Calculus of Communicating Systems (CCS)**

![[Pasted image 20260702174816.png]]

![[Pasted image 20260702174944.png]]

![[Pasted image 20260702175022.png]]

![[Pasted image 20260702175037.png]]

P -> Q = reduction relation (process form state P to state Q after interaction)

![[Pasted image 20260702175144.png]]

![[Pasted image 20260702175155.png]]

![[Pasted image 20260702175215.png]]

These domains can be turned into complete lattices by extending the subset ordering $\subseteq$ on $\wp(Const)$ in a pointwise manner

We extend the abstract env $\rho$ to constants by setting $\rho(n)=\{n\}$

In particular the analysis predicts both possible executions

A guess $(\rho,k)$ is acceptable if it safely over-approximates the runtime behavior

Validation:
check clauses on logical judgements
- for process $(\hat{\rho},\hat{k})\models_P e$
- for actions $(\hat{\rho},\hat{k})\models_A \pi$

![[Pasted image 20260702180404.png]]

The analysis information is a safe description of what will happen during the evaluation of the program, i.e., a sound over-approximation of the runtime behaviour

![[Pasted image 20260702180533.png]]

$\lfloor n \rfloor$ = is the equivalence class corresponding to n (canonical name)

we use a disciplined $\alpha$-renaming => names can only be substituted with names in the same equivalence class

![[Pasted image 20260702180758.png]]

![[Pasted image 20260702180807.png]]

![[Pasted image 20260702180839.png]]

![[Pasted image 20260702180849.png]]

![[Pasted image 20260702180907.png]]

Given a guess $(\rho,k,\Psi)$, we validate whether it is an acceptable CFA A guess is acceptable if it safely over-approximates the runtime behavior

Validation:
check clauses on logical judgements
- for processes $(\hat{\rho},\hat{k}) \models_P e:\Psi$
- for actions $(\hat{\rho},\hat{k}) \models_P \pi:\Psi$

![[Pasted image 20260702181337.png]]

![[Pasted image 20260702181349.png]]

If the process $P_*$ is statically well-behaved then it is also dynamically wellbehaved

![[Pasted image 20260702181557.png]]

![[Pasted image 20260702181618.png]]

![[Pasted image 20260702181626.png]]

If the process $P_*$ is statically well-sorted then it is also dynamically wellsorted

![[Pasted image 20260702181704.png]]

![[Pasted image 20260702181716.png]]

If the process $P_*$ is statically secrecy-preserving then it is also dynamically secrecy-preserving

![[Pasted image 20260702181800.png]]

![[Pasted image 20260702181811.png]]

If the process $P_*$ is statically non-leaking then it is also dynamically non-leaking

![[Pasted image 20260702181906.png]]

![[Pasted image 20260702181917.png]]

If the process $P_*$ is statically taint-safe then it is also dynamically taint-safe

![[Pasted image 20260702182148.png]]


