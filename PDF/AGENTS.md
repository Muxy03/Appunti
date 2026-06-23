# AGENTS.md

## Objective

Create a single comprehensive study guide for the Program Analysis course by collecting, organizing, and synthesizing all theory, formulas, definitions, theorems, algorithms, questions, exercises, solutions, and examples from the available PDFs.

The final document must be self-contained and suitable for exam preparation without requiring the original lecture notes.

---

# Source Discovery

## Official Lecture Material

All files matching:

ProgramAnalysis-XX-Y.pdf

are official lecture sources.

Where:

* XX = lecture number
* Y = lecture name/title

Examples:

* ProgramAnalysis-01-Introduction.pdf
* ProgramAnalysis-02-CollectingSemantics.pdf
* ProgramAnalysis-03-AbstractInterpretation.pdf

The value of Y defines the lecture topic and must be used to organize the final document.

---

## Additional Exercise Material

Also process every PDF contained in:

/home/muxy/Documents/Notes/PDF/PROGRAM ANALYSIS/Exercises

These files may contain:

* exercise sheets
* homework assignments
* solved exercises
* unsolved exercises
* mock exams
* past exams
* supplementary examples

Treat these as secondary sources that enrich the lecture material.

---

# Source Priority

When information overlaps:

1. Official lecture PDFs
2. Official solved exercises
3. Official exercise statements
4. Generated explanations
5. Generated solutions

Never replace official material with generated content.

Generated content should only supplement missing explanations.

---

# Lecture-Based Organization

Create one chapter per lecture.

Example:

# Lecture 01 — Introduction

# Lecture 02 — Collecting Semantics

# Lecture 03 — Abstract Interpretation

Within each lecture include:

1. Theory
2. Definitions
3. Theorems
4. Algorithms
5. Formulas
6. Worked examples
7. Related exercises
8. Common exam questions
9. Summary

---

# Theory Extraction

Extract all relevant theoretical content.

Include:

* definitions
* observations
* propositions
* lemmas
* theorems
* proofs
* proof sketches
* semantic rules
* inference rules
* soundness results
* completeness results
* correctness results
* collecting semantics
* denotational semantics
* Hoare Logic
* Incorrectness Logic
* Separation Logic
* Abstract Interpretation
* Galois Connections
* Abstract Domains
* Fixpoint Theory
* CFA
* π-calculus analyses
* any examinable material

Do not omit material because it appears obvious.

---

# Formula Extraction

Extract every mathematical formula.

For each formula include:

## Formula

$$
\text{formula}
$$

## Meaning

Explain what the formula represents.

## Variables

Explain every symbol.

## Intuition

Explain why the formula exists.

## Usage

Explain where it is used.

## Related Lecture

Reference the lecture.

## Related Exercises

Reference exercises that use it.

---

# Algorithm Extraction

For each algorithm include:

* purpose
* inputs
* outputs
* pseudocode
* complexity
* correctness intuition
* common mistakes
* exam relevance

---

# Exercise Collection

Collect exercises from:

* lecture PDFs
* exercise PDFs

---

## Exercise Metadata

For each exercise include:

* source file
* lecture topic
* page number (if available)
* difficulty
* tags

Example:

Tags:

* abstract interpretation
* lattices
* fixpoint computation

---

## Exercise Structure

### Statement

Include the complete exercise.

### Official Solution

Include whenever available.

### Generated Solution

If no official solution exists:

Clearly mark:

Generated Solution

### Key Concepts

List:

* formulas used
* theorems used
* algorithms used
* lecture references

### Typical Exam Insight

Explain what the exercise tests.

---

# Deduplication Rules

When duplicates appear:

1. Keep the most complete explanation.
2. Merge complementary explanations.
3. Preserve unique examples.
4. Remove exact duplicates.

---

# Lecture Summaries

At the end of every lecture provide:

## Key Definitions

## Key Formulas

## Key Algorithms

## Common Mistakes

## Exam Checklist

The checklist should state what a student must know after studying the lecture.

---

# Cross-Referencing

Build references throughout the guide.

Examples:

* See Lecture 05
* See Formula F-12
* See Exercise E-34

Every formula should reference exercises.

Every exercise should reference theory.

Every theorem should reference applications.

---

# Complete Formula Handbook

After all lectures create a dedicated handbook.

For every formula include:

* formula
* meaning
* variables
* intuition
* usage
* related lectures
* related exercises

---

# Complete Exercise Collection

Group exercises by:

* topic
* lecture
* difficulty

Structure:

## Easy

## Medium

## Hard

---

# Exam Preparation Guide

Create a section containing:

* recurring exercise patterns
* common proof strategies
* common lattice constructions
* common fixpoint computations
* common CFA questions
* frequently tested concepts

---

# Final Cheat Sheet

Generate a condensed revision section.

Include:

* definitions
* formulas
* algorithms
* theorem summaries
* proof techniques
* common exam tricks

Target length:

10–20 pages.

---

# Mathematical Formatting Requirements

All mathematics must be valid LaTeX.

---

## Inline Mathematics

Use:

$\alpha : C \to A$

---

## Display Mathematics

Use:

$$
\alpha(c) \sqsubseteq_A a
\iff
c \sqsubseteq_C \gamma(a)
$$

Never use fenced latex blocks.

Do NOT write:

```latex
...
```

Use display math directly.

---

## Set Notation

Always use escaped braces.

Correct:

$$
\Sigma \triangleq {\sigma : X \to \mathbb{Z}}
$$

$$
\wp(\Sigma)
===========

{P \mid P \subseteq \Sigma}
$$

$$
{(\sigma,\delta)\mid \delta \in \llbracket c \rrbracket \sigma}
$$

Never use:

$$
{\sigma : X \to \mathbb{Z}}
$$

or similar malformed set notation.

---

## Semantic Brackets

Always use:

$$
\llbracket c \rrbracket
$$

Examples:

$$
\llbracket c \rrbracket :
\wp(\Sigma)
\to
\wp(\Sigma)
$$

$$
\llbracket c \rrbracket(P)
==========================

\bigcup_{\sigma \in P}
\llbracket c \rrbracket(\sigma)
$$

---

## Hoare Logic Notation

Always write:

$$
{P}\ c\ {Q}
$$

Never use textual approximations.

---

## Incorrectness Logic Notation

Always write:

$$
[P]\ c\ [Q]
$$

---

## Quantifiers

Always use:

$$
\forall
$$

and

$$
\exists
$$

Never replace them with plain text.

---

## Standard Operators

Use:

$$
\operatorname{wlp}
$$

$$
\operatorname{wpp}
$$

$$
\operatorname{lfp}
$$

instead of plain-text names when typesetting formulas.

Example:

$$
\operatorname{wlp}(c,Q)
=======================

{
\sigma
\mid
\llbracket c \rrbracket(\sigma)
\subseteq Q
}
$$

---

## Lattice Symbols

Always use:

$$
\sqsubseteq
\quad
\sqsupseteq
\quad
\sqcup
\quad
\sqcap
\quad
\bot
\quad
\top
$$

Never use ASCII approximations.

---

# Validation Pass

Before generating the final PDF:

1. Verify all formulas compile as LaTeX.
2. Verify all sets use { and }.
3. Verify all semantic brackets use \llbracket and \rrbracket.
4. Verify all display formulas are enclosed by $$ ... $$.
5. Verify no ```latex blocks remain.
6. Verify no malformed braces exist.
7. Verify all theorem and formula references resolve correctly.
8. Verify no duplicated exercises remain.
9. Verify generated solutions are explicitly labeled.
10. Verify the PDF renders all formulas correctly.

---

# Output Files

Generate:

* Program_Analysis_Complete_Study_Guide.md
* Program_Analysis_Complete_Study_Guide.pdf

The usage of this command is recommended: 

```bash
pandoc Program_Analysis_Complete_Study_Guide.md \
  -o Program_Analysis_Complete_Study_Guide.pdf \
  --pdf-engine=xelatex \
  --from markdown+tex_math_dollars \
  --toc \
  --number-sections
```

The PDF is the primary deliverable.
