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


## 21-MPI3.pdf

![[Pasted image 20260521152326.png]]

![[Pasted image 20260521152337.png]]

![[Pasted image 20260521152413.png]]

![[Pasted image 20260521152428.png]]

![[Pasted image 20260521152441.png]]

![[Pasted image 20260521152449.png]]

![[Pasted image 20260521152458.png]]

![[Pasted image 20260521152512.png]]

![[Pasted image 20260521152525.png]]

![[Pasted image 20260521152537.png]]

![[Pasted image 20260521152603.png]]

![[Pasted image 20260521152614.png]]

![[Pasted image 20260521152625.png]]

![[Pasted image 20260521152636.png]]

![[Pasted image 20260521152647.png]]

![[Pasted image 20260521152658.png]]

![[Pasted image 20260521152709.png]]

![[Pasted image 20260521152719.png]]

![[Pasted image 20260521152729.png]]

![[Pasted image 20260521152743.png]]


## 22-StructuredParallelProgramming.pdf

![[Pasted image 20260521152842.png]]

![[Pasted image 20260521152853.png]]

![[Pasted image 20260521152904.png]]

![[Pasted image 20260521152912.png]]

![[Pasted image 20260521152922.png]]

![[Pasted image 20260521152936.png]]

![[Pasted image 20260521163308.png]]

![[Pasted image 20260521163322.png]]

![[Pasted image 20260521163333.png]]

![[Pasted image 20260521163349.png]]

![[Pasted image 20260521180027.png]]

![[Pasted image 20260521180039.png]]

![[Pasted image 20260521180101.png]]

![[Pasted image 20260521180113.png]]

![[Pasted image 20260521180123.png]]

![[Pasted image 20260521180131.png]]

![[Pasted image 20260521180140.png]]

![[Pasted image 20260521180149.png]]

![[Pasted image 20260521180159.png]]

![[Pasted image 20260521180208.png]]

![[Pasted image 20260521180219.png]]

![[Pasted image 20260521180232.png]]

![[Pasted image 20260521180243.png]]

![[Pasted image 20260521180252.png]]

![[Pasted image 20260521180303.png]]

![[Pasted image 20260521180313.png]]

![[Pasted image 20260521180324.png]]

![[Pasted image 20260521180332.png]]

![[Pasted image 20260521180342.png]]

![[Pasted image 20260521180351.png]]

![[Pasted image 20260521180359.png]]

![[Pasted image 20260521180411.png]]

![[Pasted image 20260521180420.png]]

![[Pasted image 20260521180431.png]]

![[Pasted image 20260521180444.png]]

![[Pasted image 20260521180500.png]]

![[Pasted image 20260521180511.png]]

![[Pasted image 20260521180523.png]]

![[Pasted image 20260521180534.png]]

![[Pasted image 20260521180549.png]]

![[Pasted image 20260521180601.png]]

![[Pasted image 20260521180613.png]]

![[Pasted image 20260521180743.png]]

![[Pasted image 20260521180755.png]]

![[Pasted image 20260521180804.png]]

![[Pasted image 20260521180817.png]]

![[Pasted image 20260521180827.png]]

![[Pasted image 20260521180836.png]]

![[Pasted image 20260521180850.png]]

![[Pasted image 20260521180900.png]]

![[Pasted image 20260521180908.png]]

![[Pasted image 20260521180919.png]]

## C++

![[10-C++Essentials.pdf]]

![[11-C++ConcurrencyBasics.pdf]]

![[14-C++LockFreeProgramming.pdf]]

![[C++-PSTL.pdf]]

![[C++-Ranges.pdf]]


---

## Answers

BOH?:
- [ ] Control Parallelism
- [ ] Task Parallelism

Latency = time spent for executing a single task in a computation.

Completion Time = time spent since the beginning of the execution of the first task through the end of the last task.

Throughput = amount of tasks computed per unit of time.

Service Time = the duration required to produce the results of a task within a sequence, starting immediately after the results of the preceding task have been delivered. (no wating time)

>Data Parallelism:
>
>Data Parallelism is achieved by dividing an initial task into subtasks, whose partial results are then combined to produce the final outcome.
>
>The same operation (or kernel function) is applied to data elements (or blocks of data elements) in parallel on multiple Workers.
>
>partition the task + merge the partial results = computational overhead.
>
>The main challenge of this approach lies in balancing the time spent splitting tasks and managing parallel execution against the performance gains from parallelism.

>Stream Parallelism:
>
>Stream Parallelism involves the parallel execution of tasks from an input stream, where tasks become available at different times. The interarrival time between tasks significantly impacts the potential for parallel computation. If there are no dependencies between tasks, the computation becomes embarrassingly parallel. Stream Parallelism doesn’t reduce the execution time of individual tasks but increases the overall throughput of the application, which in turn reduces the total completion time. It’s important to note that the stream of tasks can be infinite.
>
>not all tasks are available simultaneously.
>
>input stream = continuous, ordered sequence of computational or operational units (called tasks) of the same type that are processed one after the other.

>Data vs Stream:
>
>Data Parallelism reduces the execution time (latency) of a task by breaking it down into smaller subtasks, each processing a portion of the input data in parallel. In contrast, Stream Parallelism does not reduce the latency of individual tasks. Instead, it improves the overall throughput of the application by executing multiple independent tasks concurrently when available, thereby reducing the total completion time of the application.

>Structured Programming vs Unstructured:
>
>Structured Programming refers to models where parallelism is achieved using well-established patterns that represent common parallel computations (e.g. the building blocks in FastFlow or constructs in OMP). In contrast, Unstructured Programming relies on lower-level abstractions like threads, processes, and communication or synchronization primitives, requiring the programmer to manage parallel execution man- ually(e.g. the std::thread library).
>
>![[Pasted image 20260522020936.png]]
>
>Structured Parallel Programs offer several benefits: they are easier to design and implement, as many parallelism-related responsibilities are shifted from the programmer to the tools. This allows for the possibility of automatic tuning and optimization. Additionally, structured parallel programs provide better portability, ensuring consistent functionality and performance across different systems to a certain extent.

Shapes = patterns

>Stream Parallel Patterns:
>
>Stream Parallel Shapes are used to process streams of tasks. Formally, a stream is defined as < x1, x2, . . . , xn, xn+1, . . . >, where each task xi becomes available at different points in time. Streams can also be infinite, continuously producing items over time.
>
>>Pipeline:
>>Pipeline parallelism is a parallel design pattern that enhances computational efficiency by dividing a computation into a sequence of stages, where each stage processes data and passes its output to the next stage. The stages operate concurrently, enabling overlapping computation and improved throughput.
>>
>>![[Pasted image 20260522022100.png]]
>
>>Farm:
>>a Farm is a computing pattern that enhances computational efficiency by replicating the same (stateless) function F k times. Each function replica is executed by a stage called Worker.
>>
>>![[Pasted image 20260522022337.png]]

>Data Parallelism Patterns:
>All Data Parallel Shapes operate on an input ”data collection” to produce a result, typically derived from the results of subcomputations performed on partitions of the data. It is possible for the input collection to have overlapping elements.
>
>>Map:
>>A map is a data-parallel pattern in which a single function F can be applied independently to each element of an input collection, producing an output collection of the same cardinality.
>>
>>![[Pasted image 20260522022622.png]]
>
>>Reduce:
>>A reduce is a data-parallel pattern that combines the elements of an input collection into a single output using an associative binary operator.
>>
>>![[Pasted image 20260522023331.png]]
>
>>Prefix:
>>computes the vector of the m partial ”sums” of a collection with m items, using a usually associative and commutative binary function.
>>
>>prefix(+,<1,2,3,4>) = <1,1+2,1+2+3,1+2+3+4>
>
>>Stencil:
>>this operation takes two functions, f and g, and applies them to a collection of items, producing an isomorphic output collection.
>>
>>stencil(f, g, ⟨x1,..., xm⟩) = ⟨f (g(1, ⟨x1, . . . , xm⟩)),..., f (g(m, ⟨x1,..., xm⟩))⟩
>>
>>where g(i, ⟨x1,..., xm⟩) computes the neighborhood set for the ith item in the input collec- tion, and f applies a function to the elements of this neighborhood.
>
>>Divide & Conquer:
>> computes a result by dividing the input task in subtasks, computing per each subtask a partial result which will be combined into the final result.

>Map vs Farm:
>Map and Farm are both parallel shapes, but they differ in structure and application. Map is a data-parallel shape, where a function f is applied to each element of a given collection C. The result, map(f, C), is a new collection C′ that is isomorphic to the original. The parallelism in the Map pattern arises from computing the function on distinct elements of the collection concurrently. The Farm pattern is a stream-parallel shape. It applies a function f to all items in an input stream. The output does not need to preserve the ordering or structure of the input collection. Farms can be parallelized when the processing of distinct elements is independent, allowing for concurrent execution of tasks without dependencies between them.

>Number of Workers in Farm (using Service Time):
>
>>Farm as three-stage pipeline:
>>Te = Service Time of Emitter
>>nw = \#Workers
>>Tw = the time that each Collector spends for computing a single task
>>Tc = Service Time of Collector
>>
>>ServiceTime(Farm) = max(Te,$\frac{Tw}{nw}$,Tc)
>>
>>![[Pasted image 20260522162721.png]]
>
>>Farm as Client-Server (Emitter,Collecort = Clients | Workers = servers):
>>InterarrivalTime = the time between the arrivals of two con- secutive clients or requests at the server. In other words, it measures how frequently new requests (clients) arrive.
>>
>>DepartureTime = he time at which a client or request finishes receiving service from the server and leaves the system. In other words, it is the time when the server has completed processing the request and the client has departed.
>>
>>UtilizationFactor = he utilization factor in a client-server setting, particularly for an input queue, is a measure of how much of the server’s capacity is being used to process client requests. It helps determine whether the server is under-utilized, optimally utilized, or overloaded.
>>
>>Tea = InterarrivalTime Emitter send tasks to the Workers
>>Tep = DepartureTime Emitter = Tea (1 Emitter => sequential exec)
>>
>>(Assuming use Round Robin for send tasks to Workers)
>>
>>$p_i = \frac{1}{n_w}$ = prob of Worker i receives a task
>>
>>$Ta = n_w \times Tea$ = InterarrivalTime of a Worker
>>
>>$p=\frac{Tw}{n_w \times Tea}$ = Utilization Factor of the input queue
>>
>>![[Pasted image 20260522163841.png]]


![[Pasted image 20260522164028.png]]


>Which techniques for distributing the workload have we seen?
>
>![[Pasted image 20260522215114.png]]
>
>![[Pasted image 20260522215245.png]]
>
>![[Pasted image 20260522215415.png]]
>
>![[Pasted image 20260522215540.png]]
>
>![[Pasted image 20260522215705.png]]

>What is the Cache Coherency Protocol?
>
>![[Pasted image 20260522222709.png]]
>
>![[Pasted image 20260522222822.png]]
>
>![[Pasted image 20260522222839.png]]
>
>![[Pasted image 20260522222855.png]]


>What is False Sharing?
>
>![[Pasted image 20260522231141.png]]
>
>![[Pasted image 20260522231241.png]]
>
>A possible solution employed by Cache Coherency Protocols to False Sharing?
>![[Pasted image 20260522232716.png]]


>What states the Amdahl’s Law?
>
>Amdahl's Law = that the amount of non-parallelizable work in an application deter- mines the maximum speedup we may achieve in parallelizing the application.
>
>s = percent of total work is sequential.
>p = (1-s) = percent of total works that can be parallelized.
>Assume the whole application sequentially completes in $T_s$ unit of time. 
>
>![[Pasted image 20260523001041.png|626]]
>
>What are the limitations of Amdahl’s Law?
>
>The Amdahl’s Laws functions only in situations where the problem size is constant and the number of processors varies (strong scalability). When dealing with cases where the data size grows as more parallel resources are added (weak scalability), the time spent in the parallelizable part $(1 − f ) \times T_s$may grow faster in comparison to the non-parallelized part $f \times T_s$. For this reason Gustafsson introduced its law and the concept of Scaled Speedup.

>What states the Gustafsson’s Law?
>
>![[Pasted image 20260523001334.png]]
>
>![[Pasted image 20260523001348.png]]

>Scaled Speedup (generalization of the Gustafsson’s Law):
>$$\frac{T(1)}{T(n)} = \frac{p+(1-p)\times n}{1} = p+n+n\times p = n-(n-1)\times p$$

![[Pasted image 20260523001918.png]]

![[Pasted image 20260523002006.png]]

![[Pasted image 20260523002034.png]]

![[Pasted image 20260523002617.png]]

![[Pasted image 20260523003553.png]]

>C++ Memory Models:
>
>![[Pasted image 20260523003718.png]]
>
>![[Pasted image 20260523003750.png]]
>
>![[Pasted image 20260523003806.png]]

![[Pasted image 20260523003952.png]]

>What are the memory ordering options provided by atomic operations?
>
>The memory ordering options are passed as parameters for the atomic operations. By providing a memory ordering options you enforce the Memory Model ordering associated to that ordering option on that operations. 
>
>Sequentially Consistent Ordering -> memory order seq cst (default option).
>
>Acquire-Release Ordering:
>>memory order consume: its all about data dependencies, introducing data dependency nuances to the inter-thread happens-before relationships (FROM THE C++17 STANDARD ONWARD ITS SAID TO NOT USE IT).
>
>>memory order acquire: can synchronize with a memory order release operation done on the same shared variable.
>
>>memory order release: can synchronize with a memory order acquire operation done on the same shared variable.
>
>>memory order acq rel: read-modify-write operations behave as both an acquire and a release, so a prior store can synchronize with such an operation, and it can syn- chronize with a subsequent load.
>
>Relaxed Ordering -> memory order relaxed: employs a Relaxed Ordering Memory Model (all synchro- nizations and consistent memory order goes a PUTTANE).

![[Pasted image 20260523005310.png]]

![[Pasted image 20260523005414.png]]


>What theoretical computer models for Shared Memory Architectures have we seen?
>
>A theoretical computer model is a idealized architecture that does not consider many charac- teristics of real computer systems (i.e. memory access time, caches, etc. . . ). In this way when designing algorithms using a theoretical computer model we can focus only on the parallel as- pects of the computation, without needing to overcome any technological limitations.
>
>>PRAM (Parallel Random Access Machine):
>>
>>The theoretical architecture consists of n identical processors Pi.i ∈ [0, n − 1] operation in lock-steps. For each step a processor Pi execute an instruction cycle composed of three phases:
>>
>>>Read Phase: each processor can simultaneously read a single data item from a distinct shared memory cell and store it in a local register.
>>>
>>>Compute Phase: each processor can perform a fundamental operation on its local data and store the result in a register.
>>>
>>>Write Phase: each processor can simultaneously write a data item to a shared memory cell. The Exclusive Write PRAM variant allows writing only distinct cells. The Concurrent Write PRAM variant allows processors to write on the same location, which could lead to race conditions.
>>>
>>
>>Three-phase PRAM instructions are executed synchronously. Communication in PRAM is implemented in terms of reading and writing to shared memory. The shard memory ca be accessed in a uniform way s.t. each processor has access to any memory location in a unito of time.
>>
>>![[Pasted image 20260523010159.png]]
>
>>BSP (Bulk Synchronous Parallel):
>>
>>This theoretical architecture consists of 3 parts:
>>
>>![[Pasted image 20260523010342.png]]
>>
>>BSP(p, r, g, l):
>>
>>p = number of processors in the network
>>r = computational ratio (FLOPS)
>>g = cost of communicating a data world
>>l = global synchronization cost
>>
>>![[Pasted image 20260523010645.png]]
>
>>Work-Span Model:
>>
>>his theoretical architecture abstract the parallel application into several components s.t. each is a sequential portion of the application. Then we represent the application as a graph s.t. each node is a component (i.e. sequential portion) and the arcs describe dependencies between them. Given two components A and B s.t. A → B is a dependecy read as: A produces some data that is needed by B.
>>
>>Work = total amount of time spent executing the application.
>>
>>Span = he total amount of work needed to complete the longest chain of compo- nents from the input component (those with no input dependencies) and the output component (those that do not need to satisfy other component dependencies). The ”longest” chain is the chain of components from input to output that requires the longest time to compute. The time spenti compute the Span is declared as $t_{\infty}$.
>>
>>![[Pasted image 20260523010859.png]]
>
>>Data-Flow and Macro Data-Flow:
>>
>>is a general approach to parallelism based on data dependencies among the programs operations. It is interpreter as a Graph where each node is an instruction and edges represent data dependencies (i.e. read-after-write dependencies) among those instructions. Macro Data-Flow is a Data-Flow where instead of interpreting the nodes as single instructions, they are represented as entire sequential functions or block of code.


>Difference regarding speedup between the Work Span Model and the Am- dahl’s Law:
>
>The Work Span Model is more pessimistic than Amdahl’s Law, since it further limits possibilities for parallel execution beyond serial fraction.


FLOPS = Floating Point Operations Per Second = how many floating-point arithmetic operations (such as addition, subtraction, multiplication, and division of real numbers) a system can perform in one second.

>Brent's Lemma:
>
>![[Pasted image 20260523011226.png]]

![[Pasted image 20260523011323.png]]

![[Pasted image 20260523011358.png]]

