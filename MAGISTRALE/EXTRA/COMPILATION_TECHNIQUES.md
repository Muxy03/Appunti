# Summary of Compilation Techniques Sources

### Cap 1: IntroMio (Introduction to the Course)
A compiler is a program designed to translate source code written in a high-level language into a target language, typically the instruction set of a specific architecture or another human-oriented language in source-to-source translators. Unlike an **interpreter**, which translates and executes code line-by-line at runtime, a compiler translates the entire program before execution, resulting in faster performance and all errors being reported at once. Modern compilation can happen **Ahead-Of-Time (AOT)** or **Just-In-Time (JIT)**, where the latter optimizes frequently executed parts during runtime. 

Compilers are generally structured into three parts: the **Front End**, which handles scanner and parser tasks to produce an **Intermediate Representation (IR)**; the **Optimizer (Middle End)**, which transforms IR to improve performance; and the **Back End**, which handles instruction selection, scheduling, and register allocation.

---

### Cap 2: LinguaggiI (Formal Languages)
A language is a set of strings over a finite alphabet. Languages are classified according to the **Chomsky Hierarchy**, which includes (from least to most expressive) **Regular (Type 3)**, **Context-Free (Type 2)**, **Context-Sensitive (Type 1)**, and **Unrestricted (Type 0)** grammars. 

**Regular languages** can be characterized equivalently by regular grammars, **Deterministic Finite Automata (DFA)**, **Non-deterministic Finite Automata (NFA)**, and **Regular Expressions (RE)**. While NFAs can have multiple transitions for the same input, they do not expand the class of accepted languages beyond what a DFA can recognize. To prove a language is not regular, the **Pumping Lemma** is used.

**Exercise 1.5: Determine the DFA equivalent to a given NFA.**
*   **Text:** Given an NFA $M = \langle Q, \Sigma, \delta, q_0, F \rangle$, find the equivalent DFA $M'$.
*   **Solution:** The DFA states correspond to the power set of the NFA states. The new transition function $\delta'$ is defined as the union of transitions for all states in a given set: $\delta'(P, a) = \bigcup_{p \in P} \delta(p, a)$. A DFA state is final if it contains at least one NFA final state. Unreachable states in the resulting DFA should be eliminated to minimize the automaton.

---

### Cap 3: Lexer (Lexical Analysis)
The **scanner** (or lexer) is the first phase of the front end, responsible for mapping a stream of characters into a sequence of **tokens**—pairs consisting of a part of speech and a **lexeme**. Lexical analysis handles the "microsyntax" of a language, such as keywords, identifiers, and numbers. 

Scanners are implemented by converting a **Regular Expression** into an **NFA**, then into a **DFA**, which is eventually minimized and turned into code. Implementations can be **table-driven**, using a skeleton recognizer and transition tables, or **direct-coded**, where the DFA transitions are implemented via jumps and comparisons.

**Exercise: Implement a `NEXT_TOKEN()` function.**
*   **Text:** Write a lexer that tokenizes assignments like `sum = a1 + 23`.
*   **Solution:** The function must: 1. Skip whitespace. 2. Look ahead at the current character. 3. Match the longest valid token (e.g., an identifier starts with a letter followed by alphanumeric characters). 4. Consume the characters. 5. Return the token or report an error.

---

### Cap 4: ParsingMio (Introduction to Parsing)
Parsing is the process of discovering a derivation for a sentence based on a **Context-Free Grammar (CFG)**. A derivation consists of a series of rewrite steps from the start symbol to the sentence. **Leftmost derivations** replace the leftmost non-terminal first, while **rightmost derivations** do the opposite. 

Grammars can be **ambiguous** if they allow more than one leftmost or rightmost derivation for a single sentence. **Top-down parsers** (like recursive descent) build the parse tree from root to leaves but cannot handle **left-recursive** grammars, which lead to non-termination. To be predictive and backtrack-free, a grammar must satisfy the **LL(1) condition**, meaning $FIRST^+$ sets for alternative productions must be disjoint.

---

### Cap 5: Bottom_up_Parsing (Bottom-up Parsing)
**Bottom-up parsers** build a rightmost derivation in reverse, starting from the leaves and growing toward the root. The parser repeatedly identifies a **handle**—a substring of the current sentential form that matches the right-hand side of a production—and replaces it with the left-hand side. 

Most bottom-up parsers use the **shift-reduce paradigm**, which utilizes a stack and four actions: **Shift** (push input to stack), **Reduce** (replace handle on stack top with its LHS), **Accept**, and **Error**. **LR(1)** parsers are table-driven and utilize one word of lookahead and internal states to encode left context for handle recognition.

---

### Cap 6: TableConstruction (LR Table Construction)
Constructing an **LR(1)** parser involves building a canonical collection of sets of **LR(1) items**. An item is a production with a "•" indicating the current position in the RHS and a lookahead symbol $[A \rightarrow \beta \cdot \delta, a]$. 

Two primary functions are used: `closure(s)`, which adds items to a state based on productions of non-terminals following the "•", and `goto(s, X)`, which computes the state reached after recognizing symbol $X$. Conflicts in the **ACTION table**, such as shift/reduce or reduce/reduce errors, indicate that the grammar is not LR(1).

**Exercise: Construct the canonical collection for a given grammar.**
*   **Text:** Start $\rightarrow S$; $S \rightarrow A a$; $A \rightarrow B C | B C f$; $B \rightarrow b$; $C \rightarrow c$.
*   **Solution:** Begin with the closure of $[Start \rightarrow \cdot S, EOF]$. Systematically apply `goto` for all terminal and non-terminal symbols to generate new states until a fixed point is reached.

---

### Cap 7: ContextsensitiveAnalysisv (Context-Sensitive Analysis)
CFGs are insufficient for verifying properties like **type consistency** or **parameter counts**, which require context-sensitive analysis. This is often handled through **Attribute Grammars (AG)** or, more practically, **Ad-hoc Syntax-Directed Translation (SDT)**, where code snippets are associated with productions. 

During parsing, the compiler builds an **Intermediate Representation (IR)**, which can be **structural** (like an Abstract Syntax Tree), **linear** (like three-address code/ILOC), or **hybrid**. For bottom-up parsers, attributes can be stored directly on the stack alongside states and symbols.

---

### Cap 8: TheProcedureAbstraction (The Procedure Abstraction)
Procedures provide essential abstractions like **information hiding**, independent **name spaces**, and **uniform interfaces**. To implement these, the compiler must manage **control abstractions** (entry/exit), **clean name spaces** (scoping), and **external interfaces** (parameter passing). While linkage design occurs at compile time, the actual linkages and procedure bodies execute at run time.

---

### Cap 9: IntroCodeGeneration (Introduction to Code Generation)
The **Back End** translates the IR into target machine code through **instruction selection**, **instruction scheduling**, and **register allocation**. There are two major memory models: **register-to-register** (standard for RISC), which ignores register limits during IR generation, and **memory-to-memory**. 

**Code shape** refers to the strategy chosen to implement high-level constructs; the choice significantly affects performance. For example, loops can be implemented with various pre-test or post-test structures to hide latency.

---

### Cap 10: OptimizationI (Introduction to Optimization)
**Optimization** (or code improvement) transforms the IR to reduce running time, code space, or power consumption. To be correct, transformations must be **safe** (preserve meaning) and should only be applied if they are **profitable**. Typical optimizations include discovering constant values, moving computations out of loops (**loop-invariant code motion**), and removing unreachable or redundant code.

---

### Cap 11: Dataflow (Data-Flow Analysis)
**Data-flow analysis** is used by optimizers to discover context-sensitive facts about the entire program rather than single statements. It typically operates on a **Control Flow Graph (CFG)**, where nodes represent basic blocks and edges represent possible execution paths. By solving data-flow equations, the compiler identifies properties like **live variables** or **reaching definitions**, enabling transformations like register allocation and dead code elimination.

Would you like me to create flashcards for these parsing and optimization concepts?
