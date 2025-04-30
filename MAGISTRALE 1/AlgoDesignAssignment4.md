
## Part 1

For this example, I'll use:

- A set S with 3 elements: S = {a, b, c}
- Two hash functions: h₁ and h₂
- A Cuckoo hash table with 4 positions (indexed 0-3)

First, let's define our hash functions:

- h₁(a) = 0, h₂(a) = 2
- h₁(b) = 1, h₂(b) = 0
- h₁(c) = 2, h₂(c) = 3

Now, let's insert the elements into the Cuckoo hash table:

1. Insert a:
    
    - Try h₁(a) = 0: Position 0 is empty, so place a at position 0
    - Table: \[a, -, -, -]
2. Insert b:
    
    - Try h₁(b) = 1: Position 1 is empty, so place b at position 1
    - Table: \[a, b, -, -]
3. Insert c:
    
    - Try h₁(c) = 2: Position 2 is empty, so place c at position 2
    - Table: \[a, b, c, -]

Our final table: \[a, b, c, -]

Now, let's delete element b:

- Remove b from position 1
- Table after deletion: \[a, -, c, -]

Let's try to recreate this configuration by inserting S - {b} = {a, c} into an empty table:

1. Insert a:
    
    - Try h₁(a) = 0: Position 0 is empty, so place a at position 0
    - Table: \[a, -, -, -]
2. Insert c:
    
    - Try h₁(c) = 2: Position 2 is empty, so place c at position 2
    - Table: \[a, -, c, -]

We've achieved the same result!

Let me try again with different hash values to create an infeasible graph:

Let's redefine our hash functions:

- h₁(a) = 0, h₂(a) = 1
- h₁(b) = 1, h₂(b) = 2
- h₁(c) = 2, h₂(c) = 0

Now, let's insert the elements:

1. Insert a:
    
    - Try h₁(a) = 0: Position 0 is empty, so place a at position 0
    - Table: \[a, -, -, -]
2. Insert b:
    
    - Try h₁(b) = 1: Position 1 is empty, so place b at position 1
    - Table: \[a, b, -, -]
3. Insert c:
    
    - Try h₁(c) = 2: Position 2 is empty, so place c at position 2
    - Table: \[a, b, c, -]

Our final table: \[a, b, c, -]

Now, let's delete element a:

- Remove a from position 0
- Table after deletion: \[-, b, c, -]

Let's try to recreate this by inserting S - {a} = {b, c} into an empty table:

1. Insert b:
    
    - Try h₁(b) = 1: Position 1 is empty, so place b at position 1
    - Table: \[-, b, -, -]
2. Insert c:
    
    - Try h₁(c) = 2: Position 2 is empty, so place c at position 2
    - Table: \[-, b, c, -]

We've achieved the same result again!

Let's try once more with a configuration that creates a cycle:

Let's redefine our hash functions:

- h₁(a) = 0, h₂(a) = 1
- h₁(b) = 1, h₂(b) = 2
- h₁(c) = 2, h₂(c) = 0

But this time, let's consider a different insertion sequence that leads to displacements:

1. Insert a:
    
    - Try h₁(a) = 0: Position 0 is empty, so place a at position 0
    - Table: \[a, -, -, -]
2. Insert b:
    
    - Try h₁(b) = 1: Position 1 is empty, so place b at position 1
    - Table: \[a, b, -, -]
3. Insert c:
    
    - Try h₁(c) = 2: Position 2 is empty, so place c at position 2
    - Table: \[a, b, c, -]

Our table is: \[a, b, c, -]

Now, let's delete b:

- Remove b from position 1
- Table after deletion: \[a, -, c, -]

If we try to insert S - {b} = {a, c} into an empty table:

1. Insert a:
    
    - Try h₁(a) = 0: Position 0 is empty, so place a at position 0
    - Table: \[a, -, -, -]
2. Insert c:
    
    - Try h₁(c) = 2: Position 2 is empty, so place c at position 2
    - Table: \[a, -, c, -]

This still gives us the same result.

To demonstrate the infeasible graph problem, I need to create a situation where items get displaced during insertion:

Let's redefine our hash functions:

- h₁(a) = 0, h₂(a) = 2
- h₁(b) = 0, h₂(b) = 1
- h₁(c) = 1, h₂(c) = 0

Now, let's insert the elements:

1. Insert a:
    
    - Try h₁(a) = 0: Position 0 is empty, so place a at position 0
    - Table: \[a, -, -, -]
2. Insert b:
    
    - Try h₁(b) = 0: Position 0 is occupied by a, so try h₂(b) = 1
    - Position 1 is empty, so place b at position 1
    - Table: \[a, b, -, -]
3. Insert c:
    
    - Try h₁(c) = 1: Position 1 is occupied by b, so try h₂(c) = 0
    - Position 0 is occupied by a, so we need to displace an element
    - Displace a from position 0, place c at position 0
    - Try to place a at its alternative position h₂(a) = 2
    - Position 2 is empty, so place a at position 2
    - Table: \[c, b, a, -]

Our final table: \[c, b, a, -]

Now, let's delete c:

- Remove c from position 0
- Table after deletion: \[-, b, a, -]

Let's try to recreate this by inserting S - {c} = {a, b} into an empty table:

1. Insert a:
    
    - Try h₁(a) = 0: Position 0 is empty, so place a at position 0
    - Table: \[a, -, -, -]
2. Insert b:
    
    - Try h₁(b) = 0: Position 0 is occupied by a, so try h₂(b) = 1
    - Position 1 is empty, so place b at position 1
    - Table: \[a, b, -, -]

This gives us \[a, b, -, -], which is different from \[-, b, a, -] that we had after deletion!

This demonstrates that deletion can create a configuration that's impossible to reach by fresh insertions.

The problem occurs because Cuckoo hashing typically follows a deterministic insertion pattern. To fix this issue, we can randomly choose between h₁ and h₂ when inserting elements:

1. When inserting an element x:
    - Randomly choose to try either h₁(x) or h₂(x) first
    - If that position is occupied, try the other hash function
    - If both positions are occupied, proceed with displacement as in standard Cuckoo hashing

This randomization ensures that multiple possible configurations can be reached, increasing the probability that the post-deletion state can be reconstructed from scratch insertions.

By randomly choosing between hash functions during insertion, we break the deterministic path dependency that causes the infeasible graph problem, allowing the system to explore different valid configurations of the same elements.

## Part 2

### 1.1
node -> list of adjacent nodes repeated as many times as the number of arcs

During the contraction phase, the lists of nodes are joined and the occurrences of the two nodes are removed from the resulting list.

Example:

1 -> 2,3
2 -> 1,3
3 -> 1,2

contraction (1,2):
> (1,2) -> 1,2,3,3 -> 3,3 
> 3 -> (1,2)

cost of contraction operation can be done in O(n) time.

### 1.2

Definitions:

- Let $c$: total weight of the **minimum cut**
- Let $W$: total weight of all edges in the graph, i.e., $ $W = \sum_{e \in E} w(e)$ $
- Let $n$: number of nodes in the graph

In the **first iteration**, the probability of **not contracting a min-cut edge** is:

$$1 - \frac{c}{W}$$

This is because edges are selected with probability proportional to their weight. So the probability of choosing a min-cut edge is $\frac{c}{W}$, and we want to avoid this.

As the algorithm contracts edges and reduces the number of nodes from n to 2, the number of edges decreases. However:

- The **minimum cut weight $c$** does **not increase**
- Thus, the cut remains valid, and its edges are still avoidable

At each iteration  i, the probability of **not contracting** a min-cut edge is at least:

$$1 - \frac{c}{W_i}$$

where  $W_i$  is the total remaining edge weight at step  i.

The probability of **never contracting a min-cut edge** across $n - 2$ contractions is:

$$
\prod_{i=0}^{n-3} \left(1 - \frac{c}{W_i} \right)
$$

We now observe that:

- Every node has weighted degree at least $c$, otherwise a smaller cut would exist
- So the total weight $W \geq \frac{n c}{2}$

Hence:

$$
\frac{c}{W} \leq \frac{2}{n}
$$

This gives us an upper bound on the probability of failure per step, and from the analysis (similar to the unweighted case), we can conclude that:

$$\text{Success Probability} \geq \frac{2}{n(n - 1)}$$

By running the algorithm $O(n \log n)$ times, we can boost this probability to be at least $1 - \frac{1}{n^2}$.

In some refined analyses, it's shown that the **single-run success probability** can be lower-bounded by $\frac{2}{n}$.
