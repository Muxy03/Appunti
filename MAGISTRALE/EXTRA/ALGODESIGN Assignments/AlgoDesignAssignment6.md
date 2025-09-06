# Author: Andrea Mussari
# 1)

The diameter of a graph is the length of the longest shortest path between any two vertices. In other words, it's the maximum distance between any pair of vertices when traveling along the shortest paths.

$A^1[i][j]$ tells us if there's a direct edge from i to j
$A^2[i][j]$ tells us the number of distinct 2-step walks from i to j
In general, $A^k[i][j]$ tells us the number of distinct k-step walks from i to j

For finding the shortest paths (which is what we need for diameter), we use the min-plus matrix multiplication instead of regular multiplication:

- $D^1[i][j]$ = direct edge weight (or 1 for unweighted graphs)
- $D^2[i][j]$ = shortest path of length at most 2 from i to j
- $D^k[i][j]$ = shortest path of length at most k from i to j

## Example

Graph:

```
    A --- B --- C
    |           |
    D --- E --- F
```

Adjacency matrix: (1 indicates a direct edge and 0 indicates no direct edge)

```
    A B C D E F
A   0 1 0 1 0 0
B   1 0 1 0 0 0
C   0 1 0 0 0 1
D   1 0 0 0 1 0
E   0 0 0 1 0 1
F   0 0 1 0 1 0
```


the distance matrix $D^1$:

- $D^1[i][j]$ = 1 if there's a direct edge
- $D^1[i][j] = $\infty$$ if there's no direct edge ($i\neq j$)
- $D^1[i][i]$ = 0 (distance to self is 0)


  A  B  C  D  E    F
A   0  1  $\infty$  1  $\infty$  $\infty$
B   1  0  1  $\infty$  $\infty$  $\infty$
C   $\infty$  1  0  $\infty$  $\infty$  1
D   1  $\infty$  $\infty$  0  1  $\infty$
E   $\infty$  $\infty$  $\infty$  1  0  1
F   $\infty$  $\infty$  1  $\infty$  1  0


The min-plus product of two matrices A and B is defined as: $$(A \times B)[i][j] = \min\{A[i][k] + B[k][j] \text{ | } \forall{k}\}$$
Let's compute $D^2$ = $D^1 \times D^1$:

For example, to compute $D^2[A][C]$:

- $D^1[A][A] + D^1[A][C]$ = 0 + $\infty$ = $\infty$
- $D^1[A][B] + D^1[B][C]$ = 1 + 1 = 2
- $D^1[A][C] + D^1[C][C]$ = $\infty$ + 0 = $\infty$
- $D^1[A][D] + D^1[D][C]$ = 1 + $\infty$ = $\infty$
- $D^1[A][E] + D^1[E][C]$ = $\infty$ + $\infty$ = $\infty$
- $D^1[A][F] + D^1[F][C]$ = $\infty$ + 1 = $\infty$
- The minimum is 2, so $D^2[A][C]$ = 2

Computing all entries of $D^2$, we get:

```
    A  B  C  D  E  F
A   0  1  2  1  2  3
B   1  0  1  2  3  2
C   2  1  0  3  2  1
D   1  2  3  0  1  2
E   2  3  2  1  0  1
F   3  2  1  2  1  0
```

Now $D^2[i][j]$ represents the shortest path length between i and j using at most 2 edges.

For our small example, we can see that the maximum value in $D^2$ is 3 (like $D^2[A][F]$), which means the diameter is 3.

For larger graphs, we would use binary search to find the diameter efficiently.

## Example Binary Search

Let's compute the diameter of our example graph step by step using the binary search approach:

1. Initialize the binary search range: L = 1, U = 5 (n-1)

2. First iteration:    
    - mid = (1 + 5) / 2 = 3
    - Compute connectivity within distance 3
    - We need to check if $C^3[i][j]$ = true for all i,j

3. Computing $C^3$:
    - We compute $C^1$, then $C^2$, then $C^3$
    - For our graph, $C^3$ shows that all vertices are connected within 3 steps
    - So we update U = mid - 1 = 2

4. Second iteration:
    - mid = (1 + 2) / 2 = 1.5 → 1
    - Check if all vertices are connected within distance 1
    - This is just checking the adjacency matrix
    - Not all vertices are connected in 1 step, so L = mid + 1 = 2

5. Third iteration:
    - mid = (2 + 2) / 2 = 2
    - Check if all vertices are connected within distance 2
    - We compute $C^2$ and find that not all vertices are connected
    - So L = mid + 1 = 3
6. Now L > U, so the diameter is L = 3

# 2)

Let me ex_plain why BFS gives a 2-approximation of the graph diameter using a simple example.

**Graph Diameter (D)**: The longest shortest path between any two nodes in the graph
**BFS Height (h)**: The maximum distance from our starting node to any other node
## Simple Example: Path Graph

Let's consider a simple path graph with 7 nodes:

```
A --- B --- C --- D --- E --- F --- G
```

The diameter of this graph is 6, which is the distance between A and G (you have to traverse 6 edges to go from A to G).
### Case 1: BFS from the middle

If we run BFS starting from node D (the middle):

- Distance from D to A: 3
- Distance from D to G: 3
- Maximum distance = 3

In this case, BFS height h = 3, which is exactly D/2 = 6/2 = 3.

### Case 2: BFS from an end

If we run BFS starting from node A:

- Distance from A to B: 1
- Distance from A to C: 2
- ...
- Distance from A to G: 6
- Maximum distance = 6

Here, BFS height h = 6, which equals D (the true diameter).

### Case 3: BFS from elsewhere

If we run BFS from node B:

- Distance from B to A: 1
- Distance from B to G: 5
- Maximum distance = 5

Here, BFS height h = 5, which is greater than D/2 = 3.

## Why This Works

The key insight is based on the triangle inequality:

For any three nodes in a graph (including the two nodes u and v that create the diameter), we have: d(u,v) $\leq$ d(u,s) + d(s,v)

Where s is our BFS starting node.

Since the diameter D = d(u,v), we get: D $\leq$ d(u,s) + d(s,v)

Both d(u,s) and d(s,v) are at most h (the BFS height), so: D $\leq$ h + h = 2h

Therefore: h $\geq$ D/2 .

# 3)

The 2-sweep algorithm:

1. Select a random starting vertex r
2. Find vertex a that is farthest from r
3. Find vertex b that is farthest from a
4. Return the distance d(a,b)

In this graph, we have:

- A 3×7 grid forming the main structure
- Multiple vertices at the top (labeled $x_1$ through $x_p$)
- One vertex at the bottom (labeled y)
- Connections from all x vertices to the top row of the grid
- A connection from y to the center of the bottom row

Let me analyze why the 2-sweep algorithm gives a lower bound that can be arbitrarily far from the true diameter:

The true diameter of this graph is the maximum distance between any two vertices. Based on the structure, this would be the distance between $x_1$ and $x_p$ (the leftmost and rightmost vertices at the top).

To calculate this diameter:
- From $x_1$ to $x_p$, we need to go down to the grid, across the entire width, and back up
- This gives us a path length of approximately 2 + (width of grid) = 2 + 6 = 8

Let's trace through the execution of the 2-sweep algorithm:

1. We start with a random vertex r
2. If r happens to be in the central region of the grid, the farthest vertex from r will be either one of the x vertices or y
3. Let's say the algorithm selects a = $x_1$ (the leftmost top vertex)
4. Now, finding the farthest vertex from $x_1$, the algorithm will likely select b = y (the bottom vertex)

The distance d($x_1$, y) is approximately:
- 1 step from x_1 to the grid
- About 3 steps down through the grid
- 1 step to reach y
- Total: about 5 steps

But the true diameter (distance between x_1 and x_p) is about 8, as we calculated above.

The issue becomes even more pronounced if we increase the number of x vertices and spread them further apart. If we make p larger and space the x vertices wider, the true diameter increases, but the 2-sweep algorithm still returns the same value d($x_1$, y).

This means the ratio between the true diameter and the 2-sweep result can be arbitrarily poor. In mathematical terms:
- As p increases and the x vertices spread wider, the true diameter D increases
- But the 2-sweep result remains constant at d($x_1$, y)
- Therefore, D/d($x_1$, y) can grow without bound

The fundamental issue is that the 2-sweep algorithm relies on the assumption that if we find the farthest vertex from any starting point, and then find the farthest vertex from that point, we'll end up with two vertices that are at or near the diameter distance from each other.

However, this graph is constructed specifically to violate this assumption. The vertex y creates a "false signal" that attracts the algorithm away from the true diameter path between $x_1$ and $x_p$.