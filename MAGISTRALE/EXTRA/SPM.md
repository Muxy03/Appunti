# SPM SUMMARY

Moore’s law = 2X transistors/chip every 1.5 years (transistor count not to performance)

CMP = Chip Multi-Processor -> Processor manufacturers put many processing cores on the microprocessor chip

#TODO: Limits of Single-Chip improvements SLIDE (2)

#TODO: Moving to CMP to reduce power SLIDE (2)

Heterogeneous CMPs integrate different types of processor cores on a single chip (asymmetry) -> CPU,GPU,NPU,DSP

$C = A * B$ -> $c_{ij} = \sum_{k=1}^n a_{ik}*b_{kj}$ ($n = 2^k$)

R_{peak} = Frequenza di clock × Numero di Core × FLOP (Floating Point Operation Per Second) per ciclo -> 1GHz = 1×10^9

JIT compilation -> Whenever some piece of code executes sufficiently frequently, it gets compiled to machine code in real time.

#TODO: Hardware Caches SLIDE (3)

The **cilk_for** loop allows all iterations of the loop to execute in parallel.

Rule of Thumb -> parallelize outer loops rather than inner loops

**cilk_spawn** The child function call is spawned, meaning it may execute in parallel with the parent caller.

**cilk_sync** Control may not pass this point until all spawned children have returned. 

#TODO: Vector Hardware SLIDE (3)

Vectorization flags:
- \-mavx -> Intel AVX vector instructions.
- \-mavx2 -> Intel AVX2 vector instructions.
- \-mfma -> use fused multiply-add vector instructions.
- \-march=<string> -> use whatever instructions are available on the specified architecture.
- \-march=native -> Use whatever instructions are available on the architecture of the machine doing compilation.
- \-ffast-math -> restrictions on floating-point arithmetic

intrinsic instructions -> https://software.intel.com/sites/landingpage/IntrinsicsGuide/

#TODO: Classifying Parallel Architectures SLIDE (4)

Flynn's Taxonomy:
- S = Single, I = Instruction, M = Multiple, D = Data
- SISD -> #TODO: SLIDE
- SIMD -> #TODO: SLIDE
- MISD -> #TODO: SLIDE
- MIMD -> #TODO: SLIDE
#TODO: Flynn's Taxonomy image SLIDE(4)

Memory-based classification (MIMD parallel architecture):
- shared-memory architectures ->multiprocessors
	- uniform (SymmetricMultiProcessor) -> UniformMemoryAccess (All processors/cores have (roughly) equal access time to memory)
	- non-uniform (NonUniformMemoryAccess) -> Non-uniform memory access time, i.e., the memory access time is asymmetric depending on which memory is accessed
- distributed-memory architectures -> multicomputers 
#TODO: Memory-based classification image SLIDE(4)

#TODO: NUMA multicores SLIDE(4)

#TODO: SLIDE 4 PAG 14 to 15

Shared-memory systems:
- key focus: primarily on the memory organization (memory hierarchy, processor-memory interconnections)
- Goals: minimize memory contention and mitigate the von Neumann bottleneck
- Challenges: cache-coherence, memory consistency, thread synchronization

Distributed-memory systems:
- Key focus: primarily on the interconnection network topology
- Goals: reduce communication costs (reducing latency, increasing available bandwidth) 
	- Communications among nodes is a form of I/O for the single node
- Challenges: fast messaging protocols/libraries, message routing and flow control

#TODO: SLIDE 4 PAG 18 to 21

Programming SHM systems:
- Key concept: the primary way to program SHM systems is by exploiting the physical shared memory through thread-level parallelism
- Reference model: Shared Variables programming model (e.g., Pthread, C++ threads, OpenMP)
	- Distict processes on the same node (having disjoint address spaces) may communicate via Shared Memory buffers (e.g., POSIX SHM, Sys V) 
-  Challenges: synchronization issues, memory hierarchy exploitations

Programming DM systems:
- Key concept: the primary way to exploit parallelism is through process-level parallelism, which involves running multiple processes simultaneously on different nodes
- Reference model: Message Passing programming model (e.g., POSIX socket, MPI)
	- There were many attempts to provide a transparent shared-memory abstraction atop distributed memory systems (the so-called SW-DSM – Software-based Distributed Shared Memory). 
	- An example of a modern SW-DSM implementation is CUDA Unified Memory within a single node
- Challenges: hide communication overheads, explicit synchronization via messages

#TODO: SLIDE 4 PAG 18 to 24

#TODO: SLIDE 5 

#TODO: SLIDE 6 PAG 3 to 10

Locality Principle:
- Temporal Locality (data reuse): Temporal locality refers to the property of a program to repeatedly access the same memory locations over a short period of time
- Spatial Locality: Spatial locality refers to the property of a program to access memory locations that are spatially close to each other

If the data the processor requests is present in one block at the closest memory level, it is called a hit. 
Otherwise, it is a miss, and the next memory level is accessed to retrieve the block containing the 
requested data

Cache hit -> data in cache
Cache miss -> data no in cache
Miss penalty -> the time spent transferring a cache line into the first level cache and the requested data to the processor
Miss Rate -> the fraction of memory accesses not found in the cache (\#misses / \#memory access)
Hit Rate -> 1 - MR

$CPU_time = IC * CPI * ClockCycleTime$
$IC = IC_cpu + IC_mem = \text{number of ALU instructions} + \text{number of memory access instructions}$
$CPI = (\frac{IC_cpu}{IC})*CPI_cpu + (\frac{IC_mem}{IC})*CPI_mem$
$CPI_mem = HitRate * CPI_memHit + MissRate*CPI_memMiss$
Instruction Count = number of program instructions executed
CPI = average ClockCycles Per Instruction
$CPI_memHit$ = cycles for a cache hit
$CPI_memMiss$ = cycles for a cache miss

Cache performance has a multiplicative (not additive) impact on execution time. 

#TODO: SLIDE 6 PAG 15 to 18

The working set (WS) of a program, for a given a memory hierarchy, is the collection of data the program actively accesses during a specific time interval.
A program’s working set usually changes over time as it accesses different parts of its data.
The size and composition of the working set depend on the program’s memory access patterns (sequential vs. random access).

#TODO: SLIDE 6 PAG 20 to 26

Cache write policies: (the value in the cache may be inconsistent (the data is not coherent) with the value in main memory.)
- Write-through policy
	- Caches handle this by updating the data in the main memory when it is written to the cache. Always implemented with a store/write buffer
- Write-back policy
	- Caches mark data in the cache as dirty (one extra bit per cache line needed dirty bit). More complex/costly to realize.
	- Modified data (dirty bit = 1) written to memory only when cache line is evicted from the cache
	- A store/write buffer is generally used to reduce the cost of cache accesses

With private caches per core, it is possible to have several copies of shared data in distinct caches, each cache stores a different value for a single address location

#TODO: SLIDE 6 PAG 29 to 37

#TODO: SLIDE 6 PAG 40 to 45

The Roofline model is a visual performance analysis model designed to evaluate the computational 
performance limits of a system by considering the relationship between operational intensity, memory 
bandwidth, and peak computational performance 

#TODO: SLIDE 6 PAG 47 to 57

Explicit SIMD vectorization with Intrinsics -> low level

Automatic Compiler vectorization -> High level

#TODO: SLIDE 7 PAG 3 to 9

#TODO: SLIDE 7 PAG 11 to 22

Array of Structures: store records consecutively in a single array
```cpp
auto xyz = new float[3*n];
```
Structure of Array : uses one array per dimension. Each array only stores the values of the associated element dimension
```cpp
auto x = new float[n];
auto y = new float[n];
auto z = new float[n];
```

from AoS to SoA -> Convert entire array (slow for large data) or Convert on-the-fly in chunks

AoS may still be preferred for compact storage and because some operations benefit from tightly packed vectors

To exploit SIMD anyway, we transpose on the fly from AoS to SoA on blocks of 8 consecutive 3D vectors (using three 256-bit registers)

#TODO:SLIDE 7  PAG 30 to 34

Types of dependencies that may prevent vectorization:
- Read-after-Write: An iteration uses data produced in a previous iteration
- Write-after-Read: An iteration writes to a memory location read in a previous iteration and written in a later iteration
- Write-after-Write: Multiple iterations write to the same memory location (write conflicts across iterations)

With these dependencies, the compiler does not automatically vectorize the loop because it cannot prove it can reorder or execute iterations in parallel without changing semantics

#TODO:SLIDE 7  PAG 36 to 44

#TODO:SLIDE 7  GPU

Latency (L) = time from a request arrives until the response is ready to be delivered
Completion time (T_c) = the total time an application takes to complete all tasks, from start to delivery of all results
Service Time (T_s) = time required by the system to process a task, excluding waiting time
Throughput = the number of tasks completed per unit of time
Inter-arrival time (T_a) = the average time between two consecutive task arrivals at the system

#TODO:SLIDE 8 PAG 5 to 23

Amdahl's Law -> It states that the speedup is fundamentally limited by the fraction of 
sequential code (the portion of the code that cannot be parallelized) -> upper bound on achievable speedup

#TODO:SLIDE 8 PAG 25 to 43

Data parallel patterns:
- Map (N:N)
- Reduce (N:1 or N:M M < N)
- Stencil (N:N)
- Scan (N:N)

#TODO:SLIDE 9 PAG 5

A data stream is a sequence of data elements of the same type made available over time, often in 
real time -> Continuous, Dynamic, Time-sensitive

#TODO:SLIDE 9 PAG 7 to 11

#TODO:SLIDE 12 

Work-Span Model = provides more strict bounds than those offered by the Amdahl’s and Gustafson’s laws 

A parallel program can be represented as a DAG:
- Nodes = tasks -> task = unit of work (arbitrary seq code)
- edges = data dependencies

task can be executed (ready) <=> all its predecessor in DAG are completed

Model assumptions:
- p identical processors, each executing one ready task at a time
- Greedy scheduling, whenever there is a ready task (and an available processor), the task is executed immediately 

T_1 = total work -> measure total computation
T_{\infty} = span (critical path) :
- Longest chain of dependencies with unit task
- The path from the root to on leaf with the highest associated cost
- measures inherent sequential computation 

#TODO:SLIDE 13 PAG 6 to 13

PRAM:
- Read Phase: Each processor can simultaneously read a single data item from a (distinct) shared memory cell and store it in a local register.
- Compute Phase: Each processor can perform a fundamental operation on its local data and store the result in a register.
- Write Phase: Each processor can simultaneously write a data item to a shared memory cell, 
whereby the exclusive write PRAM variant allows writing only distinct cells while the 
concurrent write PRAM variant also allows processors to write to the same location (possible 
race conditions).

each step on the PRAM takes O(1) time

#TODO:SLIDE 13 PAG 15 to 19

scan algo inclusive/exclusive -> no init/with init

#TODO:SLIDE 13 PAG 21  to 38

```cpp

```



