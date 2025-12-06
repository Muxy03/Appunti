
# 15/9/25

big tech intership

![[Introduction.pdf]]

# 16/9/25

![[16:9:25.pdf]]

# 23/9/25

![[Pearls 2025.pdf]]

## Linear Time Sliding Window Maximum

```rust
use std::collections::VecDeque;

fn linear(nums: &Vec<i32>, k: usize) -> Vec<i32> {
    let n = nums.len();

    if k > n { 
        return Vec::<i32>::new();
    }

    let mut q: VecDeque<usize> = VecDeque::new();
    let mut maxs: Vec<i32> = Vec::with_capacity(n - k + 1);

    for i in 0..k {
        while (!q.is_empty()) && nums[i] > nums[*q.back().unwrap()] {
            q.pop_back();
        }
        q.push_back(i);
    }
    maxs.push(nums[*q.front().unwrap()]);

    for i in k..n {
        while !q.is_empty() && q.front().unwrap() + k <= i {
            // more idiomatic while let Some(&(p,_)) = q.front()
            q.pop_front();
        }

        while (!q.is_empty()) && nums[i] > nums[*q.back().unwrap()] {
            q.pop_back();
        }
        q.push_back(i);
        maxs.push(nums[*q.front().unwrap()]);

    }
    maxs
}
```


### Overview

The algorithm maintains a deque (double-ended queue) that stores **indices** of array elements in a specific order: indices are arranged so that their corresponding values are in decreasing order from front to back. This allows the function to always have the maximum value of the current window at the front of the deque.

### Function Signature

```rust
fn linear(nums: &Vec<i32>, k: usize) -> Vec<i32>
```

- **Input**: A reference to a vector of integers and a window size `k`
- **Output**: A vector of integers representing the maximum value in each window of size `k`

### Step-by-Step Breakdown

#### Input Validation

```rust
let n = nums.len();
if k > n { 
    return Vec::<i32>::new();
}
```

If the window size exceeds the array length, return an empty vector since no valid windows exist.

#### Initialization

```rust
let mut q: VecDeque<usize> = VecDeque::new();
let mut maxs: Vec<i32> = Vec::with_capacity(n - k + 1);
```

- A deque `q` is created to store indices (not values)
- A result vector `maxs` is pre-allocated with capacity `n - k + 1`, which is the number of windows

#### First Window Processing

```rust
for i in 0..k {
    while (!q.is_empty()) && nums[i] > nums[*q.back().unwrap()] {
        q.pop_back();
    }
    q.push_back(i);
}
maxs.push(nums[*q.front().unwrap()]);
```

Process the first window of size `k`:

1. For each element, remove indices from the back of the deque whose values are smaller than the current element (these will never be maximums)
2. Add the current index to the back
3. After processing all `k` elements, the front of the deque contains the index of the maximum, which is added to the results

#### Remaining Windows

```rust
for i in k..n {
    while !q.is_empty() && q.front().unwrap() + k <= i {
        q.pop_front();
    }
    while (!q.is_empty()) && nums[i] > nums[*q.back().unwrap()] {
        q.pop_back();
    }
    q.push_back(i);
    maxs.push(nums[*q.front().unwrap()]);
}
```

For each subsequent element from index `k` to `n-1`:

1. **Remove outdated indices**: Pop from the front while the index is no longer within the current window (indices outside `[i-k+1, i]`)
2. **Remove smaller elements**: Pop from the back while the current value is greater than values at the back indices
3. **Add current index**: Push the current index to the back
4. **Record maximum**: The front element's value is the maximum for this window

### Why It Works

The deque maintains indices in a specific invariant: if index `j` is in the deque before index `i`, then `j > i` (it comes later) or `nums[j] > nums[i]`. This ensures:

- The maximum of the current window is always at the front
- Old indices that fall outside the window are removed
- Smaller values that could never be maximums are discarded

### Detailed Step-by-Step Concrete Example

Array: `[3, 2, 5, 1, 4, 3]`, `k = 3`

We want to find the maximum in each sliding window of size 3.

#### Expected Windows and Their Maxima

- Window `[3, 2, 5]` → max = `5`
- Window `[2, 5, 1]` → max = `5`
- Window `[5, 1, 4]` → max = `5`
- Window `[1, 4, 3]` → max = `4`

#### Phase 1: Process First Window (i = 0, 1, 2)

##### i = 0 (element = 3, index = 0)

```
Current element: nums[0] = 3
Deque before: []
```

- Deque is empty, so skip the while loop
- Push index 0 to back: `q = [0]`
- Deque state: `[0]` (values: `[3]`)

##### i = 1 (element = 2, index = 1)

```
Current element: nums[1] = 2
Deque before: [0]
```

- Check: Is `nums[1]=2 > nums[q.back()]=nums[0]=3`? **No**
- Push index 1 to back: `q = [0, 1]`
- Deque state: `[0, 1]` (values: `[3, 2]`)

##### i = 2 (element = 5, index = 2)

```
Current element: nums[2] = 5
Deque before: [0, 1]
```

- Check: Is `nums[2]=5 > nums[q.back()]=nums[1]=2`? **Yes** → Pop index 1
    - Deque: `[0]`
- Check: Is `nums[2]=5 > nums[q.back()]=nums[0]=3`? **Yes** → Pop index 0
    - Deque: `[]`
- Push index 2 to back: `q = [2]`
- Deque state: `[2]` (values: `[5]`)

**Add maximum to results**: `maxs.push(nums[q.front()]) = nums[2] = 5`

- Result so far: `[5]`
#### Phase 2: Process Remaining Elements (i = 3, 4, 5)

##### i = 3 (element = 1, index = 3)

```
Current element: nums[3] = 1
Deque before: [2]
Window boundaries: indices must be in range [3-3+1, 3] = [1, 3]
```

**Step 1: Remove outdated indices**

- Check: Is `q.front() + k <= i`? Is `2 + 3 <= 3`? Is `5 <= 3`? **No**
- No indices removed

**Step 2: Remove smaller elements**

- Check: Is `nums[3]=1 > nums[q.back()]=nums[2]=5`? **No**
- Don't pop

**Step 3: Add current index**

- Push index 3 to back: `q = [2, 3]`
- Deque state: `[2, 3]` (values: `[5, 1]`)

**Add maximum to results**: `maxs.push(nums[q.front()]) = nums[2] = 5`

- Result so far: `[5, 5]`
##### i = 4 (element = 4, index = 4)

```
Current element: nums[4] = 4
Deque before: [2, 3]
Window boundaries: indices must be in range [4-3+1, 4] = [2, 4]
```

**Step 1: Remove outdated indices**

- Check: Is `q.front() + k <= i`? Is `2 + 3 <= 4`? Is `5 <= 4`? **No**
- No indices removed

**Step 2: Remove smaller elements**

- Check: Is `nums[4]=4 > nums[q.back()]=nums[3]=1`? **Yes** → Pop index 3
    - Deque: `[2]`
- Check: Is `nums[4]=4 > nums[q.back()]=nums[2]=5`? **No**
- Stop popping

**Step 3: Add current index**

- Push index 4 to back: `q = [2, 4]`
- Deque state: `[2, 4]` (values: `[5, 4]`)

**Add maximum to results**: `maxs.push(nums[q.front()]) = nums[2] = 5`

- Result so far: `[5, 5, 5]`
##### i = 5 (element = 3, index = 5)

```
Current element: nums[5] = 3
Deque before: [2, 4]
Window boundaries: indices must be in range [5-3+1, 5] = [3, 5]
```

**Step 1: Remove outdated indices**

- Check: Is `q.front() + k <= i`? Is `2 + 3 <= 5`? Is `5 <= 5`? **Yes** → Pop index 2
    - Deque: `[4]`
    - Why? Index 2 was in window `[0, 2]`, now we're at window `[3, 5]`. Index 2 is outside!
- Check again: Is `q.front() + k <= i`? Is `4 + 3 <= 5`? Is `7 <= 5`? **No**
- Stop popping

**Step 2: Remove smaller elements**

- Check: Is `nums[5]=3 > nums[q.back()]=nums[4]=4`? **No**
- Don't pop

**Step 3: Add current index**

- Push index 5 to back: `q = [4, 5]`
- Deque state: `[4, 5]` (values: `[4, 3]`)

**Add maximum to results**: `maxs.push(nums[q.front()]) = nums[4] = 4`

- Result so far: `[5, 5, 5, 4]`
#### Final Result

**Output**: `[5, 5, 5, 4]` ✓

This matches our expected windows perfectly!
#### Key Observations

1. **Dominated elements are removed**: When we saw `5` at index 2, it immediately dominated the smaller `3` and `2` that came before it. They were discarded and never examined again.
    
2. **Outdated elements are purged**: When we reached index 5, index 2 (which contained the old maximum `5`) was no longer in the window, so it was removed from the front.
    
3. **Decreasing invariant maintained**: At every step, reading the deque from front to back gives decreasing values: `[5]` → `[5,1]` → `[5,4]` → `[4,3]`.
    
4. **Each element processed once**: Despite `k=3` windows, we only examined each element a constant number of times (once for insertion, at most once for removal from back, at most once for removal from front).

### Time and Space Complexity

- **Time**: O(n) — Each element is added to the deque once and removed at most once
- **Space**: O(k) — The deque stores at most `k` indices at any time
# 29/9/25

![[29:9:25.pdf]]

# 30/9/25

![[PDF/COMPETITIVE PROGRAMMING/30:9:25.pdf|30:9:25]]

# 6/10/25

https://pages.di.unipi.it/rossano/blog/2023/binarysearch/

# 7/10/25

https://pages.di.unipi.it/rossano/blog/2023/sweepline

## Maximum Overlapping Intervals - Code Explanation

### Overview

This Rust function calculates the **maximum number of intervals that overlap at any point in time**. It's a classic algorithm used in scheduling, resource allocation, and timeline analysis problems.

```rust
#[derive(PartialOrd, Ord, PartialEq, Eq, Debug)]
enum Event {
    Begin,
    End,
}

pub fn max_overlapping(intervals: &[(usize, usize)]) -> usize {
    let mut pairs: Vec<_> = intervals
        .iter()
        .flat_map(|&(b, e)| [(b, PointKind::Begin), (e, PointKind::End)])
        .collect();

    pairs.sort_unstable();

    pairs
        .into_iter()
        .scan(0, |counter, (_, kind)| {
            if kind == Event::Begin {
                *counter += 1;
            } else {
                *counter -= 1;
            }
            Some(*counter)
        })
        .max()
        .unwrap()
}
```
### What Does It Do?

Given a list of intervals represented as tuples `(start, end)`, the function returns the largest count of overlapping intervals at any moment.

### Code Breakdown

#### 1. Enum Definition

```rust
#[derive(PartialOrd, Ord, PartialEq, Eq, Debug)]
enum Event {
    Begin,
    End,
}
```

This enum marks whether a point represents the start or end of an interval. The derived traits allow comparison and ordering, with `Begin` typically sorting before `End` when times are equal (useful for handling edge cases).

#### 2. Function Signature

```rust
pub fn max_overlapping(intervals: &[(usize, usize)]) -> usize
```

- **Input**: A reference to a slice of tuples, where each tuple contains `(start, end)` of an interval
- **Output**: A `usize` representing the maximum number of overlapping intervals

#### 3. Algorithm Steps

##### Step 1: Create Events

```rust
let mut pairs: Vec<_> = intervals
    .iter()
    .flat_map(|&(b, e)| [(b, PointKind::Begin), (e, PointKind::End)])
    .collect();
```

Convert each interval into two events:

- One event for the beginning at time `b` with type `Begin`
- One event for the end at time `e` with type `End`

Result: A flat list of all events with their types.

##### Step 2: Sort Events

```rust
pairs.sort_unstable();
```

Sort all events by their time coordinate. Events at the same time are ordered by their `Event` type. Since `Begin` is defined first in the enum, it sorts before `End` when times are equal. This ensures that if an interval ends exactly when another begins, we count them as separate intervals.

##### Step 3: Count Overlaps

```rust
pairs
    .into_iter()
    .scan(0, |counter, (_, kind)| {
        if kind == Event::Begin {
            *counter += 1;
        } else {
            *counter -= 1;
        }
        Some(*counter)
    })
    .max()
    .unwrap()
```

Process events in chronological order:

- **scan**: Maintains a running counter (starting at 0) that represents active intervals
    - When encountering a `Begin` event: increment the counter (interval starts)
    - When encountering an `End` event: decrement the counter (interval ends)
    - Yield the counter value after each update
- **max()**: Find the maximum counter value seen during the process
- **unwrap()**: Extract the maximum value (safe because we have at least the initial 0)

### Concrete Example

#### Input

```
intervals = [(1, 3), (2, 6), (5, 7), (4, 5)]
```

#### Step 1: Create Events

```
Events: [(1, Begin), (3, End), (2, Begin), (6, End), (5, Begin), (7, End), (4, Begin), (5, End)]
```

#### Step 2: Sort Events

```
Sorted: [(1, Begin), (2, Begin), (3, End), (4, Begin), (5, Begin), (5, End), (6, End), (7, End)]
        
Note: At time 5, Begin comes before End due to enum ordering
```

#### Step 3: Count Overlaps

Processing each event and tracking the counter:

| Time | Event | Counter | Explanation                      |
| ---- | ----- | ------- | -------------------------------- |
| 1    | Begin | 1       | Interval [1,3) starts. Active: 1 |
| 2    | Begin | 2       | Interval [2,6) starts. Active: 2 |
| 3    | End   | 1       | Interval [1,3) ends. Active: 1   |
| 4    | Begin | 2       | Interval [4,5) starts. Active: 2 |
| 5    | Begin | 3       | Interval [5,7) starts. Active: 3 |
| 5    | End   | 2       | Interval [4,5) ends. Active: 2   |
| 6    | End   | 1       | Interval [2,6) ends. Active: 1   |
| 7    | End   | 0       | Interval [5,7) ends. Active: 0   |

**Maximum overlaps: 3**

This occurs at time 5, where intervals \[2,6), \[5,7), and \[4,5) all overlap.

### Time and Space Complexity

- **Time Complexity**: O(n log n) due to sorting, where n is the number of intervals
- **Space Complexity**: O(n) for storing the events

This is much more efficient than a brute-force O(n²) approach of checking every pair of intervals.

### Visual Representation

```
Time:    1   2   3   4   5   6   7
         |   |   |   |   |   |   |
[1,3)    |---|
[2,6)        |-----------|
[5,7)                |-------|
[4,5)            |-|

Overlaps:   1   2   1   2   3   2   1
                            ↑ Maximum
```
## Closest Pair of Points Algorithm

### Overview

This Rust implementation finds the closest pair of points in a 2D plane and returns the squared Euclidean distance between them. It uses a divide-and-conquer approach optimized with a sweep line algorithm.

```rust
pub fn distance_squared(p: (i64, i64), q: (i64, i64)) -> i64 {
    (p.0 - q.0).pow(2) + (p.1 - q.1).pow(2)
}

use std::collections::BTreeSet;
use std::ops::Bound::Included;

// Returns the (squared) Euclidean distance between the closest pair of 
// points in `points`
pub fn closest_pair(points: &mut [(i64, i64)]) -> Option<i64> {
    if points.len() < 2 {
        return None;
    }

    points.sort_unstable_by_key(|p| (p.1, p.0)); // sort by y

    let min_y = points[0].1;
    let max_y = points.last()?.1;

    let mut delta = distance_squared(points[0], points[1]);

    let mut set: BTreeSet<(i64, i64)> = BTreeSet::new();
    for &point in points.iter() {
        // Search by x and select the points with too small y-coordinate that we remove
        // to not touch them again in the future
        let to_delete: Vec<_> = set
            .range((
                Included(&(point.0 - delta, min_y)),
                Included(&(point.0 + delta, max_y)),
            ))
            .filter(|p| p.1 < point.1 - delta)
            .cloned()
            .collect();

        // Remove those points
        for p in to_delete {
            set.remove(&p);
        }

        // Search again and compute the distances with survived points.
        // Update delta if needed.
        delta = set
            .range((
                Included(&(point.0 - delta, min_y)),
                Included(&(point.0 + delta, max_y)),
            ))
            .fold(delta, |acc, &p| acc.min(distance_squared(point, p)));

        set.insert(point);
    }

    Some(delta)
}
```
### Helper Function: `distance_squared`

```rust
pub fn distance_squared(p: (i64, i64), q: (i64, i64)) -> i64 {
    (p.0 - q.0).pow(2) + (p.1 - q.1).pow(2)
}
```

This function calculates the squared Euclidean distance between two points `p` and `q`. For points `p = (x₁, y₁)` and `q = (x₂, y₂)`, it computes `(x₁ - x₂)² + (y₁ - y₂)²`. Using squared distance avoids floating-point arithmetic and is sufficient for comparison purposes.

### Main Algorithm: `closest_pair`

#### Purpose

The algorithm finds the minimum squared distance between any two distinct points in an unordered set of points.

#### Time Complexity

**O(n log n)**: Sorting takes O(n log n), and the sweep line process with BTreeSet operations takes O(n log n) overall.

#### Key Insight

Instead of checking all O(n²) pairs naively, the algorithm uses a **sweep line** that moves from bottom to top (by increasing y-coordinate). It maintains a set of "active" points within a horizontal band of height `sqrt(delta)` around the current point. This dramatically reduces comparisons.

### Step-by-Step Logic

#### 1. **Initial Checks**

```rust
if points.len() < 2 {
    return None;
}
```

Returns `None` if fewer than 2 points exist (no pair to compare).

#### 2. **Sort by Y-Coordinate**

```rust
points.sort_unstable_by_key(|p| (p.1, p.0));
```

Sort points primarily by y-coordinate, with x-coordinate as tiebreaker. This enables the sweep line to process points in order from bottom to top.

#### 3. **Initialize Variables**

```rust
let min_y = points[0].1;
let max_y = points.last()?.1;
let mut delta = distance_squared(points[0], points[1]);
let mut set: BTreeSet<(i64, i64)> = BTreeSet::new();
```

- `min_y` and `max_y`: The y-range of all points
- `delta`: The squared distance of the current closest pair (initially the first two points)
- `set`: A BTreeSet maintaining active points sorted by coordinates (enabling range queries)

#### 4. **Sweep Line Processing**

```rust
for &point in points.iter() {
```

For each point in y-sorted order:

##### Step 4a: Remove Outdated Points

```rust
let to_delete: Vec<_> = set
    .range((
        Included(&(point.0 - delta, min_y)),
        Included(&(point.0 + delta, max_y)),
    ))
    .filter(|p| p.1 < point.1 - delta)
    .cloned()
    .collect();

for p in to_delete {
    set.remove(&p);
}
```

Since we're processing points in ascending y-order, we can safely remove any point whose y-coordinate is too far below the current point (more than `sqrt(delta)` below it). These points can never form a closer pair with the current point or any future point.

The range query filters by x-coordinate first (efficient due to BTreeSet), then filters by y-coordinate.

##### Step 4b: Check Remaining Points

```rust
delta = set
    .range((
        Included(&(point.0 - delta, min_y)),
        Included(&(point.0 + delta, max_y)),
    ))
    .fold(delta, |acc, &p| acc.min(distance_squared(point, p)));
```

Among remaining active points, only those within a horizontal band of width `2*sqrt(delta)` are candidates. Compute distances to all such points and update `delta` if a closer pair is found.

##### Step 4c: Add Current Point

```rust
set.insert(point);
```

Add the current point to the active set for future comparisons.
### Concrete Example

Let's trace through with these points: `(0, 0)`, `(3, 1)`, `(2, 3)`, `(5, 2)`, `(4, 4)`

#### Initial State

```
Points (unordered): (0,0), (3,1), (2,3), (5,2), (4,4)
```

#### Step 1: Sort by Y

```
Sorted: (0,0), (3,1), (5,2), (2,3), (4,4)
         y=0   y=1   y=2   y=3   y=4
```

#### Step 2: Initialize

```
delta = distance_squared((0,0), (3,1)) = 9 + 1 = 10
set = {}
min_y = 0, max_y = 4
```

#### Step 3: Process (0,0)

```
Remove points: None (set is empty)
Check points: None (set is empty)
delta = 10
set = {(0,0)}
```

#### Step 4: Process (3,1)

```
Range query: x in [3 - sqrt(10), 3 + sqrt(10)] ≈ [0.16, 5.84]
           y in [0, 4]
           And y < 1 - sqrt(10) ≈ -2.16? 
           → (0,0) has y=0, not less than -2.16, so keep it

Check distances:
  distance_squared((3,1), (0,0)) = 9 + 1 = 10
  delta = min(10, 10) = 10

set = {(0,0), (3,1)}
```

#### Step 5: Process (5,2)

```
Range query: x in [5 - sqrt(10), 5 + sqrt(10)] ≈ [1.84, 8.16]
           y in [0, 4]
           Remove if y < 2 - sqrt(10) ≈ -1.16?
           → (0,0) has y=0, not less than -1.16, keep it
           → (3,1) has y=1, not less than -1.16, keep it

Check distances:
  distance_squared((5,2), (0,0)) = 25 + 4 = 29
  distance_squared((5,2), (3,1)) = 4 + 1 = 5
  delta = min(10, 29, 5) = 5

set = {(0,0), (3,1), (5,2)}
```

#### Step 6: Process (2,3)

```
Range query: x in [2 - sqrt(5), 2 + sqrt(5)] ≈ [0.76, 3.24]
           y in [0, 4]
           Remove if y < 3 - sqrt(5) ≈ 0.76?
           → (0,0) has y=0 < 0.76, remove it
           → (3,1) has y=1, not less than 0.76, keep it
           → (5,2) has y=2, not less than 0.76, keep it

After removal: set = {(3,1), (5,2)}

But (5,2) is at x=5, outside range [0.76, 3.24], so not checked
Check distances:
  distance_squared((2,3), (3,1)) = 1 + 4 = 5
  delta = min(5, 5) = 5

set = {(3,1), (5,2), (2,3)}
```

#### Step 7: Process (4,4)

```
Range query: x in [4 - sqrt(5), 4 + sqrt(5)] ≈ [1.76, 6.24]
           y in [0, 4]
           Remove if y < 4 - sqrt(5) ≈ 1.76?
           → (3,1) has y=1 < 1.76, remove it
           → (5,2) has y=2, not less than 1.76, keep it
           → (2,3) has y=3, not less than 1.76, keep it

After removal: set = {(5,2), (2,3)}

Check distances:
  distance_squared((4,4), (5,2)) = 1 + 4 = 5
  distance_squared((4,4), (2,3)) = 4 + 1 = 5
  delta = min(5, 5, 5) = 5

set = {(5,2), (2,3), (4,4)}
```

#### Final Result

```
Minimum squared distance: 5
Closest pairs: (3,1)-(5,2), (2,3)-(4,4), (4,4)-(5,2) all have squared distance 5
```

### Why This Works

The key optimization is that within a band of height `sqrt(delta)` and width `2*sqrt(delta)`, there can only be a limited number of points. Specifically, you can fit at most a constant number of points in this band without some pair being closer than `delta`. This bounds the comparisons per point to O(1) on average, giving O(n log n) total time when combined with the BTreeSet's O(log n) operations.

### Edge Cases

- **Less than 2 points**: Returns `None`
- **All points identical**: Returns 0 (distance to itself)
- **Only 2 points**: Returns their squared distance
- **Very large coordinates**: Works correctly with `i64` as long as `(max_coord - min_coord)²` fits in `i64`
# 13/10/25

https://pages.di.unipi.it/rossano/blog/2023/prefixsums/

# 14/10/25

https://pages.di.unipi.it/rossano/blog/2023/fenwick/

## Fenwick Tree (Binary Indexed Tree) Implementation

This is a Fenwick Tree, also known as a Binary Indexed Tree, a data structure that efficiently handles two operations: updating elements and computing prefix sums in a range.

```rust
#[derive(Debug)]
pub struct FenwickTree {
    tree: Vec<i64>,
}

impl FenwickTree {
    pub fn with_len(n: usize) -> Self {
        Self {
            tree: vec![0; n + 1],
        }
    }

    pub fn len(&self) -> usize {
        self.tree.len() - 1
    }

    /// Indexing is 0-based, even if internally we use 1-based indexing
    pub fn add(&mut self, i: usize, delta: i64) {
        let mut i = i + 1; 
        assert!(i < self.tree.len());

        while i < self.tree.len() {
            self.tree[i] += delta;
            i = Self::next_sibling(i);
        }
    }

    /// Indexing is 0-based, even if internally we use 1-based indexing
    pub fn sum(&self, i: usize) -> i64 {
        let mut i = i + 1;  

        assert!(i < self.tree.len());
        let mut sum = 0;
        while i != 0 {
            sum += self.tree[i];
            i = Self::parent(i);
        }

        sum
    }

    pub fn range_sum(&self, l: usize, r: usize) -> i64 {
        self.sum(r) - if l == 0 { 0 } else { self.sum(l - 1) }
    }

    fn isolate_trailing_one(i: usize) -> usize {
        if i == 0 {
            0
        } else {
            1 << i.trailing_zeros() // `trailing_zeros()` counts how many zeros are at the **right end** (the least significant bits) of a number's binary representation.
        }
    }

    fn parent(i: usize) -> usize {
        i - Self::isolate_trailing_one(i)
    }

    fn next_sibling(i: usize) -> usize {
        i + Self::isolate_trailing_one(i)
    }
}
```
### Core Logic

The Fenwick Tree uses a clever bit manipulation technique to maintain cumulative information. Instead of storing individual elements, it stores partial sums at strategic positions determined by the binary representation of indices.

**Key Insight:** For each index `i`, the tree stores the sum of elements in a range whose size is determined by the lowest set bit in `i`'s binary representation.

#### The Three Helper Functions

These functions manipulate indices using bit operations:

- **`isolate_trailing_one(i)`**: Extracts the lowest set bit. For example, `i = 12 (binary: 1100)` returns `4 (binary: 0100)`. This is computed as `1 << i.trailing_zeros()`.
    
- **`parent(i)`**: Removes the lowest set bit, moving up the tree conceptually. For `i = 12`, it returns `12 - 4 = 8`. This operation helps traverse backwards when computing prefix sums.
    
- **`next_sibling(i)`**: Adds the lowest set bit, moving to the next position that needs updating. For `i = 12`, it returns `12 + 4 = 16`.
    

#### Main Operations

- **`add(i, delta)`**: Adds `delta` to position `i`. It converts to 1-based indexing (`i + 1`), then repeatedly moves to the next sibling using bit manipulation, updating all affected positions. Time: O(log n).
    
- **`sum(i)`**: Computes the prefix sum from index 0 to i. It converts to 1-based indexing, then repeatedly moves to the parent, accumulating values. Time: O(log n).
    
- **`range_sum(l, r)`**: Returns the sum of elements in range `[l, r]` using the formula `sum(r) - sum(l-1)`.
    

### Concrete Example

Let's build a Fenwick Tree with 8 elements, all initially 0, then perform operations.

#### Initial Setup

```
Array (0-based):  [0, 0, 0, 0, 0, 0, 0, 0]
Tree (1-based):   [_, 0, 0, 0, 0, 0, 0, 0, 0]  (index 0 unused)
```

#### Step 1: `add(0, 5)` - Add 5 to position 0

Convert to 1-based: `i = 1`

- **i = 1** (binary: 0001): `tree[1] += 5` → `tree[1] = 5`. Next sibling: `1 + 1 = 2`
- **i = 2** (binary: 0010): `tree[2] += 5` → `tree[2] = 5`. Next sibling: `2 + 2 = 4`
- **i = 4** (binary: 0100): `tree[4] += 5` → `tree[4] = 5`. Next sibling: `4 + 4 = 8`
- **i = 8** (binary: 1000): `tree[8] += 5` → `tree[8] = 5`. Next sibling: `8 + 8 = 16` (out of bounds, stop)

**Tree after step 1:** `[_, 5, 5, 0, 5, 0, 0, 0, 5]`

#### Step 2: `add(2, 3)` - Add 3 to position 2

Convert to 1-based: `i = 3`

- **i = 3** (binary: 0011): `tree[3] += 3` → `tree[3] = 3`. Next sibling: `3 + 1 = 4`
- **i = 4** (binary: 0100): `tree[4] += 3` → `tree[4] = 8`. Next sibling: `4 + 4 = 8`
- **i = 8** (binary: 1000): `tree[8] += 3` → `tree[8] = 8`. Next sibling: `8 + 8 = 16` (stop)

**Tree after step 2:** `[_, 5, 5, 3, 8, 0, 0, 0, 8]`

#### Step 3: `sum(2)` - Get prefix sum from 0 to 2

Convert to 1-based: `i = 3`

- **i = 3** (binary: 0011): `sum += tree[3]` → `sum = 3`. Parent: `3 - 1 = 2`
- **i = 2** (binary: 0010): `sum += tree[2]` → `sum = 8`. Parent: `2 - 2 = 0`
- **i = 0**: Stop

**Result:** `sum(2) = 8` (which is 5 + 3 + 0 = 8, the sum of first three elements)

#### Step 4: `range_sum(0, 2)` - Get sum of range \[0, 2\]

`range_sum(0, 2) = sum(2) - sum(-1)`

But since `l = 0`, we use `0` instead: `8 - 0 = 8`

**Result:** `8` ✓

### Why It Works

The bit-manipulation-based structure ensures that each index's chain of updates/lookups visits only O(log n) tree nodes. The lowest bit tells you exactly which "power-of-2 sized block" an index belongs to, enabling efficient prefix sum queries without needing to traverse all elements.
# 20/10/25

https://pages.di.unipi.it/rossano/blog/2023/fenwick/

# 21/10/25

## SEGMENT TREE
# 27/10/25

## SEGMENT TREE APPLICATION

# 3/11/25
## LAZY PROPAGATION
# 4/11/25

https://pages.di.unipi.it/rossano/blog/2023/mosalgorithm/

![[Mos 2025.pdf]]
## MO's Algorithm - Complete Explanation

### Overview

This is an implementation of **MO's Algorithm** (also known as the square root decomposition technique), a powerful offline query processing technique. It efficiently answers multiple range queries on an array by sorting them in a specific order to minimize pointer movements.

```rust
pub fn three_or_more(a: &[usize], queries: &[(usize, usize)]) -> Vec<usize> {
    let mut counters: Vec<usize> = vec![0; a.len()];
    let mut answers = Vec::with_capacity(queries.len());

    let mut cur_l = 0;
    let mut cur_r = 0; // here right endpoint is excluded
    let mut answer = 0;

    for &(l, r) in queries {
        let mut add = |i| {
            counters[a[i]] += 1;
            if counters[a[i]] == 3 {
                answer += 1
            }
        };
        while cur_l > l {
            cur_l -= 1;
            add(cur_l);
        }
        while cur_r <= r {
            add(cur_r);
            cur_r += 1;
        }
        let mut remove = |i| {
            counters[a[i]] -= 1;
            if counters[a[i]] == 2 {
                answer -= 1
            }
        };
        while cur_l < l {
            remove(cur_l);
            cur_l += 1;
        }
        while cur_r > r + 1 {
            cur_r -= 1;
            remove(cur_r);
        }
        answers.push(answer);
    }
    answers
}

pub fn mos(a: &[usize], queries: &[(usize, usize)]) -> Vec<usize> {
    // Sort the queries by bucket and get the permutation induced by this sorting.
    // The latter is needed to permute the answers back to the original ordering
    let mut sorted_queries: Vec<_> = queries.iter().cloned().collect();
    let mut permutation: Vec<usize> = (0..queries.len()).collect();

    let sqrt_n = (a.len() as f64) as usize + 1;
    sorted_queries.sort_by_key(|&(l, r)| (l / sqrt_n, r));
    permutation.sort_by_key(|&i| (queries[i].0 / sqrt_n, queries[i].1));

    let answers = three_or_more(a, &sorted_queries);

    let mut permuted_answers = vec![0; answers.len()];
    for (i, answer) in permutation.into_iter().zip(answers) {
        permuted_answers[i] = answer;
    }

    permuted_answers
}
```

#### The Problem

Given an array `a` and multiple queries of the form `(l, r)`, count how many distinct elements appear **3 or more times** in each range `a[l..=r]`.
### Algorithm Components

#### 1. **The `mos` Function** - Orchestrator

```rust
pub fn mos(a: &[usize], queries: &[(usize, usize)]) -> Vec<usize>
```

**Purpose:** Sorts queries efficiently and manages the answer permutation.

**Key Steps:**

1. **Calculate bucket size:** `sqrt_n = sqrt(array_length)`
2. **Sort queries** by `(bucket, right_endpoint)` where `bucket = left / sqrt_n`
3. **Track permutation** to restore original query order
4. **Process sorted queries** with the main algorithm
5. **Permute answers** back to match original query ordering

**Why sort?** Moving the window left/right pointer takes O(n) time. By sorting queries to minimize pointer movement, we reduce redundant work.

#### 2. **The `three_or_more` Function** - Core Algorithm

```rust
pub fn three_or_more(a: &[usize], queries: &[(usize, usize)]) -> Vec<usize>
```

**Purpose:** Efficiently answer all queries by maintaining a sliding window with a frequency counter.

**Key Data Structures:**

- `counters`: frequency array where `counters[value] = count of value in current window`
- `cur_l`, `cur_r`: current window boundaries (right is exclusive)
- `answer`: count of distinct elements appearing ≥3 times

**Algorithm:** Two-pointer sliding window

- Expand/contract the window to match each query's range
- Update the frequency counter incrementally
- Track when elements cross the threshold of 3 occurrences
### Step-by-Step Logic

#### Moving the Left Pointer

```rust
while cur_l > l {
    cur_l -= 1;
    add(cur_l);  // Include element at cur_l-1
}
while cur_l < l {
    remove(cur_l);  // Exclude element at cur_l
    cur_l += 1;
}
```

#### Moving the Right Pointer

```rust
while cur_r <= r {
    add(cur_r);  // Include element at cur_r
    cur_r += 1;
}
while cur_r > r + 1 {
    cur_r -= 1;
    remove(cur_r);  // Exclude element at cur_r
}
```

#### The `add` Function

```rust
let mut add = |i| {
    counters[a[i]] += 1;
    if counters[a[i]] == 3 {
        answer += 1  // Element just reached 3 occurrences
    }
};
```

Increments the counter. When an element's count reaches exactly 3, increment the answer.

#### The `remove` Function

```rust
let mut remove = |i| {
    counters[a[i]] -= 1;
    if counters[a[i]] == 2 {
        answer -= 1  // Element dropped below 3 occurrences
    }
};
```

Decrements the counter. When an element's count drops to 2, decrement the answer.
### Concrete Example

#### Input

```
Array a = [1, 2, 1, 3, 1, 2, 2, 3, 3, 3]
Queries = [(0, 3), (2, 6), (4, 9), (2, 4)]
```

#### Step 1: Calculate sqrt_n

```
sqrt_n = floor(sqrt(10)) + 1 = 3 + 1 = 4
```

#### Step 2: Sort Queries

Original queries with indices:

```
(0, 3) -> index 0
(2, 6) -> index 1
(4, 9) -> index 2
(2, 4) -> index 3
```

Sort by `(left / sqrt_n, right)`:

```
(0, 3) -> bucket 0/4=0, right=3  -> index 0
(2, 4) -> bucket 2/4=0, right=4  -> index 3
(2, 6) -> bucket 2/4=0, right=6  -> index 1
(4, 9) -> bucket 4/4=1, right=9  -> index 2
```

**Sorted order:** \[(0, 3), (2, 4), (2, 6), (4, 9)] with permutation \[0, 3, 1, 2]

#### Step 3: Process Sorted Queries

##### Query 1: (0, 3)

Initial state: `cur_l=0, cur_r=0, answer=0`

Expand right to 3:

- Add index 0: `a[0]=1`, counters\[1]→1
- Add index 1: `a[1]=2`, counters\[2]→1
- Add index 2: `a[2]=1`, counters\[1]→2
- Add index 3: `a[3]=3`, counters\[3]→1

Result: counters = \[0, 2, 1, 1], **answer = 0** (no element ≥ 3)

##### Query 2: (2, 4)

Current: `cur_l=0, cur_r=4`

Move left from 0 to 2:

- Remove index 0: `a[0]=1`, counters[1]→1
- Remove index 1: `a[1]=2`, counters[2]→0

Current state: `cur_l=2, cur_r=4, counters=[0, 1, 0, 1]`

Result: **answer = 0** (no element ≥ 3)

##### Query 3: (2, 6)

Current: `cur_l=2, cur_r=4`

Expand right to 6:

- Add index 4: `a[4]=1`, counters\[1\]→2
- Add index 5: `a[5]=2`, counters\[2\]→1
- Add index 6: `a[6]=2`, counters\[2\]→2

Current state: `cur_l=2, cur_r=7, counters=[0, 2, 2, 1]`

Result: **answer = 0** (no element ≥ 3)

##### Query 4: (4, 9)

Current: `cur_l=2, cur_r=7`

Move left from 2 to 4:

- Remove index 2: `a[2]=1`, counters\[1\]→1
- Remove index 3: `a[3]=3`, counters\[3\]→0

Current state: `cur_l=4, cur_r=7, counters=[0, 1, 2, 0]`

Expand right to 9:

- Add index 7: `a[7]=3`, counters\[3\]→1
- Add index 8: `a[8]=3`, counters\[3\]→2
- Add index 9: `a[9]=3`, counters\[3\]→3, **answer += 1** ✓

Current state: `cur_l=4, cur_r=10, counters=[0, 1, 2, 3]`

Result: **answer = 1** (element 3 appears ≥ 3 times)

#### Step 4: Unpermute Answers

Sorted answers: \[0, 0, 0, 1\] Permutation: \[0, 3, 1, 2\]

Unpermute:

```
permuted_answers[0] = answers[0] = 0
permuted_answers[3] = answers[1] = 0
permuted_answers[1] = answers[2] = 0
permuted_answers[2] = answers[3] = 1
```

**Final Output:** \[0, 0, 1, 0\]

This corresponds to:

- Query (0, 3) → 0 ✓
- Query (2, 6) → 0 ✓
- Query (4, 9) → 1 ✓
- Query (2, 4) → 0 ✓
### Time Complexity

- **Sorting queries:** O(q log q) where q = number of queries
- **Processing queries:** O((n + q) × √n)
    - Each element is visited O(√n) times across all queries
    - Each query processes O(√n) window movements

**Overall:** O(q log q + (n + q) × √n)

This is significantly faster than naive O(q × n) approach for large datasets.

### Space Complexity

- O(n) for the counters array
- O(q) for storing queries and permutations
- **Overall:** O(n + q)
# 10/11/25

![[Rmq 2025.pdf]]

# 11/11/25

Dynamic Programming: Fibonacci numbers, Rod cutting, and Shortest path on a DAG

![[DynamicProgramming.pdf]]

```rust
type Matrix = [[i64; 2]; 2];

// Multiply two 2x2 matrices
fn multiply(a: &Matrix, b: &Matrix) -> Matrix {
    [
        [
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ],
        [
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ],
    ]
}

// Binary exponentiation for 2x2 matrix
fn matrix_power(mut base: Matrix, mut n: u64) -> Matrix {
    let mut result: Matrix = [[1, 0], [0, 1]]; // Identity matrix

    while n > 0 {
        if n & 1 == 1 {
            result = multiply(&result, &base);
        }
        base = multiply(&base, &base);
        n >>= 1;
    }

    result
}

// Compute nth Fibonacci number
fn fibonacci(n: u64) -> i64 {
    if n == 0 {
        return 0;
    }

    let fib_matrix: Matrix = [[1, 1], [1, 0]];
    let result = matrix_power(fib_matrix, n - 1);

    result[0][0] // This is F(n)
}

fn main() {
    let n = 50;
    println!("Fibonacci({}) = {}", n, fibonacci(n));
}
```
# 17/11/25

Dynamic Programming: Minimum cost path and Longest common subsequence

![[DynamicProgramming.pdf]]

# 18/11/25

Dynamic Programming: 0/1 Knapsack, Fractional knapsack, and Subset sum.

![[DynamicProgramming.pdf]]

# 24/11/25

Dynamic Programming: Longest increasing subsequence and Coin change

![[DynamicProgramming.pdf]]

# 1/12/25

Greedy algorithms: Activity Selection, Job sequencing, and Fractional knapsack problem. Dynamic Programming: Longest bitonic subsequence, and Largest independent set on trees

![[04-greedy.pdf]]

# 2/12/25

Greedy Algorithms: Boxes and Hero (section 7.4)

![[04-greedy.pdf]]