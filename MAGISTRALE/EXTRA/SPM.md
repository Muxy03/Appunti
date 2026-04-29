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

## 8-Metrics_and_Laws.pdf
## 9-TypesOfParallelism.pdf

## 12-WorkloadBalancing.pdf
## 13-ModelsOfComputation.pdf

## 15-ThreadAffinity.pdf
## 16-OpenMP1.pdf

## 17-OpenMP2.pdf

## Formulario

| Formula                             | Descrizione                                                                   | Legenda                                                                                            |
| :---------------------------------- | :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| $S_p = \frac{T_1}{T_p}$             | **Speedup**: Misura di quanto il programma è più veloce con $p$ processori.   | $T_1$: Tempo sequenziale; $T_p$: Tempo con $p$ processori.                                         |
| $E_p = \frac{S_p}{p}$               | **Efficienza**: Frazione di utilizzo dei processori.                          | $p$: Numero di processori.                                                                         |
| $S_p = \frac{1}{f + \frac{1-f}{p}}$ | **Legge di Amdahl**: Limite dello speedup basato sulla parte sequenziale.     | $f$: Frazione di codice non parallelizzabile ($0 \leq f \leq 1$).                                  |
| $T_{step} = w + hg + l$             | **Costo Superstep BSP**: Tempo totale di un passo di calcolo e comunicazione. | $w$: Lavoro locale; $h$: Dati scambiati; $g$: Costo unitario comm.; $l$: Latenza/Sincronizzazione. |
| $C = R \cdot L$                     | **Legge di Little**: Relazione tra concorrenza, throughput e latenza.         | $C$: Concorrenza; $R$: Throughput (rate); $L$: Latenza.                                            |
| $\gamma = \alpha / \beta$           | **Rapporto Calcolo/Comm.**: Misura il bilanciamento tra lavoro e overhead.    | $\alpha$: Peso del calcolo; $\beta$: Peso della comunicazione.                                     |

