## 2-Intro.pdf

![[Pasted image 20260428190637.png]]

![[Pasted image 20260428190715.png]]

Moore's Law -> 2X transistors/chip every 1.5 years (transistor count, not to performance)

![[Pasted image 20260428191515.png]]

Core types: CPU, GPU, NPU, DSP

## 3-MMexample-LeisersonMIT.pdf

![[Pasted image 20260428191828.png]]

![[Pasted image 20260428191924.png]]

- $2.9 \times 10^9$ (Clock Frequency)
- $2$ (Processor Chips)
- $9$ (Processing Cores)
- $16$ (FLOP per cycle): Rappresenta il numero di operazioni in virgola mobile che ogni core può eseguire in un singolo ciclo di clock. Questo valore deriva dalla capacità della Floating-Point Unit di eseguire 8 operazioni in doppia precisione (DP) includendo istruzioni FMA (Fused Multiply-Add). Poiché un'istruzione FMA conta come 2 operazioni (una moltiplicazione e un'addizione eseguite insieme), il calcolo è $8 \text{ istruzioni} \times 2 \text{ FLOP} = 16$ FLOP/ciclo per core.

![[Pasted image 20260428192812.png]]

![[Pasted image 20260428192852.png]]

loop order => different perfomance

![[Pasted image 20260428193019.png]]

matrices are laid out in memory in row-major order.

![[Pasted image 20260428193238.png]]

The *cilk_for* loop allows all iterations of the loop to execute in parallel.

Rule of Thumb = parallelize outer loops rather than inner loops.

![[Pasted image 20260428193630.png]]

![[Pasted image 20260428193755.png]]

IDEA : Tile for every power of 2 simultaneously.

![[Pasted image 20260428193912.png]]

![[Pasted image 20260428193827.png]]

The base case is too small. We must coarsen the recursion to overcome function-call overheads. (n <= THRESHOLD)

![[Pasted image 20260428194213.png]]

![[Pasted image 20260428194244.png]]

Vectorization Flags:
- -maxv: use Intel AVX vector Instructions
- -maxv2: use Intel AVX2 vector Instructions
- -mfma: use fused multiply-add vector Instructions
- -march=\<string\>: use whatever instructions are available on the specified architecture.
- -march=native: use whatever instructions are available on the architecture of the machine doing compilation.
- -ffast-math

Intel provides C-style functions, called intrinsic instructions, that provide direct access to hardware vector operations. (AVX)


## 4-Classification.pdf

![[Pasted image 20260428194924.png]]

### Flynn's Taxonomy:
Classification based on the number of instructions and data streams.

Flynn’s taxonomy is useful to reason about instruction and data parallelism, but it does not capture memory organization or system scalability

![[Pasted image 20260428195243.png]]

#### Single Instruction Single Data:

![[Pasted image 20260428195524.png]]

#### Single Instruction Multiple Data:

![[Pasted image 20260428195538.png]]

#### Multiple Instruction Single Data:

![[Pasted image 20260428195552.png]]

#### Multiple Instruction Multiple Data

![[Pasted image 20260428195609.png]]

### Memory based Classification:

![[Pasted image 20260428195935.png]]

![[Pasted image 20260428201407.png]]

![[Pasted image 20260428201441.png]]

![[Pasted image 20260428201747.png]]

![[Pasted image 20260428201831.png]]

![[Pasted image 20260428201910.png]]

![[Pasted image 20260428201931.png]]

![[Pasted image 20260428202000.png]]

![[Pasted image 20260428202020.png]]

![[Pasted image 20260428201700.png]]

![[Pasted image 20260428201605.png]]

![[Pasted image 20260428202042.png]]

## 5-SLURM.pdf

![[5-SLURM.pdf]]

## 6-Shared-Memory.pdf

![[Pasted image 20260428202622.png]]

![[Pasted image 20260428202701.png]]

![[Pasted image 20260428202734.png]]

![[Pasted image 20260428204124.png]]

![[Pasted image 20260428204200.png]]

![[Pasted image 20260428204320.png]]

![[Pasted image 20260428204341.png]]

![[Pasted image 20260428204404.png]]

cache hit = the data is present in the cache
cache miss = the data is not present in the cache
miss penalty = the time spent trasferring a cache line into the first level cache and the requested data to the processor
miss rate = the fraction of memory accesses not found in the cache
hit rate = 1 - miss rate

$MR = \frac{\#misses}{\text{\# of memory accesses}}$
$HR = 1 - MR$

$CPU_{time} = ClockCycles*ClockCycleTime = IC*CPI*ClockCycleTime$
$IC = IC_{CPU}+IC_{MEM} = \text{\#ALU instructions}+\text{\#memory accesses instructions}$
$CPI=(\frac{IC_{CPU}}{IC})*CPI_{CPU} + ( \frac{IC_{MEM}}{IC})*CPI_{MEM}$
$CPI_{MEM}=HitRate*CPI_{MEM-HIT} + (1-HitRate)*CPI_{MEM- MISS}$

IC = instruction count = number of program instructions executed
CPI = average ClockCycles Per Instruction = $\frac{ClockCycles}{IC}$
CPI_MEM-HIT = cycles for a cache hit (typically 1-2 cycles)
CPI_MEM-MISS = cycles for a cache miss (50-200 cycles for LLC miss (DRAM access))

![[Pasted image 20260428211335.png]]

![[Pasted image 20260428211455.png]]

![[Pasted image 20260428211510.png]]

![[Pasted image 20260428211555.png]]

![[Pasted image 20260428211641.png]]

#TODO GEMM EXAMPLE

![[Pasted image 20260428212344.png]]

![[Pasted image 20260428212443.png]]

![[Pasted image 20260428212504.png]]

![[Pasted image 20260428212516.png]]

![[Pasted image 20260428212531.png]]

![[Pasted image 20260428212800.png]]

![[Pasted image 20260428212815.png]]

![[Pasted image 20260428212919.png]]

![[Pasted image 20260428212932.png]]

![[Pasted image 20260428212946.png]]


![[Pasted image 20260428213539.png]]

![[Pasted image 20260428213700.png]]

![[Pasted image 20260428213802.png]]

![[Pasted image 20260428213814.png]]

![[Pasted image 20260428213841.png]]

![[Pasted image 20260428213859.png]]

![[Pasted image 20260428213952.png]]

![[Pasted image 20260428214004.png]]

![[Pasted image 20260428214019.png]]

![[Pasted image 20260428214107.png]]

![[Pasted image 20260428214134.png]]

![[Pasted image 20260428214146.png]]

![[Pasted image 20260428214158.png]]

![[Pasted image 20260428214258.png]]

![[Pasted image 20260428214317.png]]

![[Pasted image 20260428214334.png]]

![[Pasted image 20260428214401.png]]

## 7-SIMD-on-CPU.pdf, 7-SIMT-on-GPU.pdf

![[Pasted image 20260506033652.png]]

![[Pasted image 20260506033715.png]]

![[Pasted image 20260506033746.png]]

![[Pasted image 20260506033803.png]]

![[Pasted image 20260506033930.png]]

![[Pasted image 20260506033942.png]]

![[Pasted image 20260506034036.png]]

![[Pasted image 20260506034107.png]]

![[Pasted image 20260506034118.png]]

![[Pasted image 20260506034136.png]]

![[Pasted image 20260506034234.png]]

![[Pasted image 20260506034250.png]]

![[Pasted image 20260506170619.png]]

![[Pasted image 20260506170630.png]]

![[Pasted image 20260506170642.png]]

AoS = array of structures -> stores records consecutively in a single array
SoA = Structure of arrays -> ses one array per dimension. Each array only stores the values of the associated element dimension

![[Pasted image 20260506170951.png]]

![[Pasted image 20260506171016.png]]

![[Pasted image 20260506171105.png]]

![[Pasted image 20260506171130.png]]

![[Pasted image 20260506171152.png]]

What is auto-vectorization? A compiler optimization that automatically transforms scalar loops into SIMD instructions

Flags:
- -O3: enables aggressive optimizations including auto-vectorization (-O2 in recent GCC versions also enables it)
- -march=native: enables all instruction-set extensions available on your local CPU (e.g., SSE3, AVX2, …) 
	- Without this option, GCC generates generic instructions to ensure broad compatibility (e.g., only SSE2)
- -ftree-vectorize: explicitly enables vectorization optimizations (enabled by -O3)
- -fopt-info-\<option\>: enables optimization dumps (reports) about why the compiler did or did not vectorize
	- ...-vec-all: prints reports for all vectorization optimizations
	- ...-vec-missed:  prints only the missed opportunity
- -ffast-math: loosens strict IEEE 754 floating-point rules (NOTE: may change numerical behavior)
- fprofile-generate/-fprofile-use: Profile-Guided Optimizations (PGO) the compiler makes informed auto‐vectorization decisions based on runtime data

![[Pasted image 20260506171658.png]]

![[Pasted image 20260506171712.png]]

Loop iteration dependencies:
- True dependencies (Read-After-Write) : An iteration uses data produced in a previous iteration
- Anti dependencies (Write-After-Read) : An iteration uses data produced in a previous iteration
- Output dependencies (Write-After-Write) : Multiple iterations write to the same memory location (write conflicts across iterations)

With these dependencies, the compiler does not automatically vectorize the loop because it cannot prove it can reorder or execute iterations in parallel without changing semantics

![[Pasted image 20260506172510.png]]

![[Pasted image 20260506172540.png]]

![[Pasted image 20260506172603.png]]

![[Pasted image 20260506172636.png]]

![[Pasted image 20260506172656.png]]

![[Pasted image 20260506172709.png]]

---
![[Pasted image 20260506172801.png]]

![[Pasted image 20260506172818.png]]

![[Pasted image 20260506172832.png]]

![[Pasted image 20260506172847.png]]

![[Pasted image 20260506172906.png]]

![[Pasted image 20260506172915.png]]

![[Pasted image 20260506172930.png]]

![[Pasted image 20260506173155.png]]

![[Pasted image 20260506173207.png]]

![[Pasted image 20260506173229.png]]

![[Pasted image 20260506173246.png]]

![[Pasted image 20260506173324.png]]

![[Pasted image 20260506173341.png]]

![[Pasted image 20260506173502.png]]

![[Pasted image 20260506173515.png]]

![[Pasted image 20260506173527.png]]

![[Pasted image 20260506173858.png]]

![[Pasted image 20260506173939.png]]

![[Pasted image 20260506173957.png]]

![[Pasted image 20260506174020.png]]

![[Pasted image 20260506174034.png]]

![[Pasted image 20260506174047.png]]

![[Pasted image 20260506174123.png]]

![[Pasted image 20260506174137.png]]

## 8-Metrics_and_Laws.pdf

![[Pasted image 20260506174252.png]]

![[Pasted image 20260506174314.png]]

![[Pasted image 20260506174334.png]]

![[Pasted image 20260506174343.png]]

![[Pasted image 20260506174358.png]]

![[Pasted image 20260506174411.png]]

![[Pasted image 20260506174453.png]]

![[Pasted image 20260506174514.png]]

#TODO Example's slide

![[Pasted image 20260506175825.png]]

![[Pasted image 20260506175836.png]]

![[Pasted image 20260506175848.png]]

![[Pasted image 20260506175902.png]]

![[Pasted image 20260506175911.png]]

![[Pasted image 20260506175926.png]]

![[Pasted image 20260506175939.png]]

![[Pasted image 20260506175953.png]]

![[Pasted image 20260506180516.png]]

![[Pasted image 20260506180531.png]]

![[Pasted image 20260506180612.png]]

![[Pasted image 20260506180715.png]]

![[Pasted image 20260506180727.png]]

![[Pasted image 20260506180737.png]]

![[Pasted image 20260506180751.png]]

![[Pasted image 20260506180813.png]]

![[Pasted image 20260506180842.png]]

![[Pasted image 20260506180850.png]]

![[Pasted image 20260506180900.png]]

![[Pasted image 20260506180912.png]]

![[Pasted image 20260506180922.png]]

## 9-TypesOfParallelism.pdf

![[Pasted image 20260506181001.png]]

Data parallel patterns (input:output cardinality):
- Map (N:N) -> list of temps from Celsius to Fahrenheit
- Reduce (N:M with $1 \le M \lt N$) -> sum N numbers, or counts per class (M classes)
- Stencil (N:N) -> 2D convultion
- Scan (N:N) -> cumulative sums of N numbers

![[Pasted image 20260506181415.png]]

Data Stream = a sequence of data elements of the same type made available over time, often in real time (Continuous, Dynamic, Time sensitive)

![[Pasted image 20260506181517.png]]

![[Pasted image 20260506181529.png]]

![[Pasted image 20260506181545.png]]

![[Pasted image 20260506181558.png]]

![[Pasted image 20260506181608.png]]

## 12-WorkloadBalancing.pdf

![[Pasted image 20260507014415.png]]

![[Pasted image 20260507014440.png]]

![[Pasted image 20260507014450.png]]

![[Pasted image 20260507014529.png]]

![[Pasted image 20260507014544.png]]

![[Pasted image 20260507014555.png]]

![[Pasted image 20260507014614.png]]

![[Pasted image 20260507014641.png]]

![[Pasted image 20260507014711.png]]

![[Pasted image 20260507014758.png]]

![[Pasted image 20260507014828.png]]

![[Pasted image 20260507014838.png]]

![[Pasted image 20260507014849.png]]

![[Pasted image 20260507014900.png]]

## 13-ModelsOfComputation.pdf

![[Pasted image 20260507015005.png]]

![[Pasted image 20260507015018.png]]

![[Pasted image 20260507015051.png]]

![[Pasted image 20260507015103.png]]

![[Pasted image 20260507015302.png]]

![[Pasted image 20260507015320.png]]

![[Pasted image 20260507015331.png]]

![[Pasted image 20260507015344.png]]

![[Pasted image 20260507015351.png]]

![[Pasted image 20260507015409.png]]

![[Pasted image 20260507015421.png]]

Variants:
- Exclusive Read Exclusive Write: No two processors are allowed to read or write to the same shared memory cell during any cycle.
- Concurrent Read Exclusive Write: Several processors may read data from the same shared memory cell simultaneously. Still, different processors are not allowed to write to the same shared memory cell.
- Concurrent Read Concurrent Write: Both simultaneous reads and writes to the same shared memory cell are allowed. In case of a simultaneous write we further specify which value will actually be stored:
	- Priority CW: Processors have been assigned distinct priorities, and the one with the highest priority succeeds in writing.
	- Arbitrary CW: A randomly chosen processor succeeds in writing its value.
	- Common CW:  If the values are all equal, then this common value is written, otherwise, the memory location is unchanged.
	- Combining CW: All values to be written are combined into a single value by means of an associative binary operation (e.g. sum, product, minimum, logical OR/AND)

![[Pasted image 20260507015827.png]]

![[Pasted image 20260507015929.png]]

Prefix computation usually refers to the inclusive version (`std::inclusive_scan` or `std::exclusive_scan`)

![[Pasted image 20260507020036.png]]

![[Pasted image 20260507020059.png]]

![[Pasted image 20260507020113.png]]

![[Pasted image 20260507020142.png]]

![[Pasted image 20260507020151.png]]

![[Pasted image 20260507020957.png]]

![[Pasted image 20260507021008.png]]

![[Pasted image 20260507021019.png]]

![[Pasted image 20260507021030.png]]

![[Pasted image 20260507021041.png]]

![[Pasted image 20260507021058.png]]

![[Pasted image 20260507021121.png]]

![[Pasted image 20260507021134.png]]

![[Pasted image 20260507021153.png]]

![[Pasted image 20260507021204.png]]

## 15-ThreadAffinity.pdf

![[Pasted image 20260507021239.png]]

![[Pasted image 20260507021249.png]]

![[Pasted image 20260507021258.png]]

![[Pasted image 20260507021333.png]]

![[Pasted image 20260507021344.png]]

![[Pasted image 20260507021409.png]]

![[Pasted image 20260507021419.png]]

## 16-OpenMP1.pdf

![[Pasted image 20260507021448.png]]

![[Pasted image 20260507021458.png]]

![[Pasted image 20260507021516.png]]

![[Pasted image 20260507021527.png]]

![[Pasted image 20260507021542.png]]

![[Pasted image 20260507021552.png]]

![[Pasted image 20260507021603.png]]

![[Pasted image 20260507021617.png]]

![[Pasted image 20260507021627.png]]

![[Pasted image 20260507021643.png]]

![[Pasted image 20260507021712.png]]

![[Pasted image 20260507021724.png]]

![[Pasted image 20260507021757.png]]

![[Pasted image 20260507021820.png]]

![[Pasted image 20260507021829.png]]

![[Pasted image 20260507021841.png]]

![[Pasted image 20260507021854.png]]

![[Pasted image 20260507021912.png]]

![[Pasted image 20260507021926.png]]

![[Pasted image 20260507021959.png]]

![[Pasted image 20260507022012.png]]

![[Pasted image 20260507022031.png]]

![[Pasted image 20260507022039.png]]

![[Pasted image 20260507022049.png]]

![[Pasted image 20260507022130.png]]

![[Pasted image 20260507022216.png]]

![[Pasted image 20260507022229.png]]

![[Pasted image 20260507022241.png]]

![[Pasted image 20260507022250.png]]

![[Pasted image 20260507022303.png]]

![[Pasted image 20260507022312.png]]

## 17-OpenMP2.pdf

![[Pasted image 20260507022408.png]]

![[Pasted image 20260507022417.png]]

![[Pasted image 20260507022429.png]]

![[Pasted image 20260507022442.png]]

![[Pasted image 20260507022454.png]]

#TODO Hello task example

![[Pasted image 20260507022806.png]]

![[Pasted image 20260507022816.png]]

![[Pasted image 20260507022825.png]]

![[Pasted image 20260507023129.png]]

![[Pasted image 20260507023140.png]]

![[Pasted image 20260507023149.png]]

![[Pasted image 20260507023249.png]]

![[Pasted image 20260507023256.png]]

![[Pasted image 20260507023308.png]]

![[Pasted image 20260507023321.png]]

![[Pasted image 20260507023411.png]]

![[Pasted image 20260507023423.png]]

![[Pasted image 20260507023433.png]]

![[Pasted image 20260507023449.png]]

![[Pasted image 20260507023826.png]]

![[Pasted image 20260507023853.png]]

## 18-DistributedSystems-Background.pdf

![[Pasted image 20260507023937.png]]

![[Pasted image 20260507023948.png]]

![[Pasted image 20260507023956.png]]

![[Pasted image 20260507024008.png]]

![[Pasted image 20260507024016.png]]

![[Pasted image 20260507024025.png]]

![[Pasted image 20260507024758.png]]

![[Pasted image 20260507024811.png]]

![[Pasted image 20260507024821.png]]

![[Pasted image 20260507024833.png]]

![[Pasted image 20260507024942.png]]

![[Pasted image 20260507025254.png]]

![[Pasted image 20260507025304.png]]

![[Pasted image 20260507025443.png]]

![[Pasted image 20260507025454.png]]

![[Pasted image 20260507025503.png]]

![[Pasted image 20260507025513.png]]

![[Pasted image 20260507025522.png]]

![[Pasted image 20260507025530.png]]

![[Pasted image 20260507025540.png]]

![[Pasted image 20260507025551.png]]

![[Pasted image 20260507025602.png]]

![[Pasted image 20260507025611.png]]

![[Pasted image 20260507025620.png]]

![[Pasted image 20260507025631.png]]

![[Pasted image 20260507025648.png]]

![[Pasted image 20260507025708.png]]

![[Pasted image 20260507025716.png]]


## 19-MPI1.pdf

![[Pasted image 20260511023713.png]]

![[Pasted image 20260511023722.png]]

![[Pasted image 20260511023734.png]]

![[Pasted image 20260511023745.png]]

![[Pasted image 20260511023756.png]]

![[Pasted image 20260511023806.png]]

![[Pasted image 20260511023822.png]]

![[Pasted image 20260511023832.png]]

![[Pasted image 20260511023842.png]]

![[Pasted image 20260511023852.png]]

![[Pasted image 20260511023908.png]]

![[Pasted image 20260511023922.png]]

![[Pasted image 20260511023941.png]]

![[Pasted image 20260511023955.png]]

![[Pasted image 20260511024004.png]]

![[Pasted image 20260511024012.png]]

![[Pasted image 20260511024020.png]]

![[Pasted image 20260511024030.png]]

![[Pasted image 20260511024041.png]]

![[Pasted image 20260511024051.png]]

![[Pasted image 20260511024059.png]]

![[Pasted image 20260511024107.png]]

![[Pasted image 20260511024117.png]]

![[Pasted image 20260511024130.png]]

![[Pasted image 20260511024138.png]]

![[Pasted image 20260511024149.png]]

![[Pasted image 20260511024158.png]]

![[Pasted image 20260511024208.png]]

![[Pasted image 20260511024216.png]]

![[Pasted image 20260511024253.png]]

![[Pasted image 20260511024301.png]]

![[Pasted image 20260511024314.png]]

![[Pasted image 20260511024324.png]]

![[Pasted image 20260511024333.png]]

![[Pasted image 20260511024341.png]]

![[Pasted image 20260511024357.png]]



## 20-MPI2.pdf

![[Pasted image 20260512214904.png]]

![[Pasted image 20260512214913.png]]

![[Pasted image 20260512214923.png]]

![[Pasted image 20260512214931.png]]

![[Pasted image 20260512214938.png]]

![[Pasted image 20260512214946.png]]

![[Pasted image 20260512215003.png]]

![[Pasted image 20260512220117.png]]

![[Pasted image 20260512220130.png]]

![[Pasted image 20260512220138.png]]

![[Pasted image 20260512220148.png]]

![[Pasted image 20260512220158.png]]

![[Pasted image 20260512220210.png]]

![[Pasted image 20260512220220.png]]

![[Pasted image 20260512220237.png]]

![[Pasted image 20260512220250.png]]

![[Pasted image 20260512220301.png]]

![[Pasted image 20260512220312.png]]

![[Pasted image 20260512220321.png]]

![[Pasted image 20260512220330.png]]


## C++

![[10-C++Essentials.pdf]]

![[11-C++ConcurrencyBasics.pdf]]

![[14-C++LockFreeProgramming.pdf]]

![[C++-PSTL.pdf]]

![[C++-Ranges.pdf]]
