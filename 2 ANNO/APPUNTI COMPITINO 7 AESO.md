main memory -> cache for disk(s)

![[Pasted image 20230422173027.png]]

>![[Pasted image 20230422173205.png]]
>![[Pasted image 20230422173218.png]]
>![[Pasted image 20230422173321.png]]

Allocating a Page Frame:
- Select old page to evict (sfrattare)
- Find all page table entries that refer to old page (if page is shared)
- Set each page table entries (Copies of now invalid page table entry)
- Write changes to page to disk, if necessary (if the page had been modified)

>![[Pasted image 20230422173955.png]]
>![[Pasted image 20230422174016.png]]
>![[Pasted image 20230422174027.png]]

Os can emulate a use bit:
- M bit: set all clean pages as read-only
- U bit: set all unused pages as invalid
- On first write (M) or read/write (U), take page fault to kernel
- from info in the core map the kernel knows what to do
	- kernel sets M bit and marks page as read-write
	- Kernel sets U bit and marks p                age as read or read/write

Trashing: the system spends most of the time swapping pages to disk tather than executing application's instructions

Working Set -> set of memory locations that need to be cached for reasonable cache hit rate

Cache replacement policy:
- FIFO -> worst case if Working Set larger than cache memory
- ![[Pasted image 20230422174728.png]]


Second Chance:
- FIFO algorithm with a R bit 
- The page-frames are ordered in a linked list
- if a page is needed check the oldest (head)
	- if R=0 take it as victim
	- Otherwise move it at the end of the list (second chance)
- Keep going until a 0 R bit page is found
- Problem = too many page frame move in the list

Clock Algorithm:
- Basically, Second Chacne implemented with a circular list
- Perodically, sweep through all pages
- if page is unused (R=0), reclaim
- if page is used, mark as unused(R=0) and advance to the next

![[Pasted image 20230422175658.png]]

![[Pasted image 20230422175729.png]]

WS algorithm:
- WS = set of pages referred in the last period T
- each process has a number of physical pages reserved to upload its working set (inherently local)
- Resident set:
	- is the actual set of virtual pages in main memory
	- some of them may be out of the working set
	- Resident set $\not=$ working set
- ![[Pasted image 20230422180629.png]]
- TLR = approximation of the time of last reference to the page
- the pages with age<T are in the WS ad (if possible) are not removed

WSCLOCK:
- ![[Pasted image 20230422180939.png]]

![[Pasted image 20230422181333.png]]

Page allocation algorithms -> Static merda, Dynamic->Page Fault Frequency (PFF)

PFF:
- Dynamically determines the number of physical pages assigned to a process
	- resident set $\ge$ working set
- When frequency of page faults >> "natural frequency"
	- Increases the size of resident set
- When frequency of page faults << "natural frequency"
	- Reduces the size of the resident set

![[Pasted image 20230422181918.png]]

![[Pasted image 20230422182304.png]]

![[Pasted image 20230422182345.png]]

![[Pasted image 20230422182431.png]]

![[Pasted image 20230422182610.png]]

Paging in UNIX BSD:
- ![[Pasted image 20230422182901.png]]

Page Replacement in UNIX BSD:
- PR algorithms:
	- Second chance (global)
	- or variants
- PR executed periodically by the Page Daemon:
	- uses parameters: lostfree, desfree, minfree -> lotsfree > desfree > minfree
- ![[Pasted image 20230422183213.png]]
- ![[Pasted image 20230422183239.png]]

Swapping of processes in Unix:
- ![[Pasted image 20230422183437.png]]
- ![[Pasted image 20230422183447.png]]

Windows page fault management:
- ![[Pasted image 20230422183526.png]]
- ![[Pasted image 20230422183537.png]]
- ![[Pasted image 20230422183549.png]]
- ![[Pasted image 20230422183618.png]]
- ![[Pasted image 20230422183705.png]]


>![[Pasted image 20230423134743.png]]
>![[Pasted image 20230423134815.png]]
>![[Pasted image 20230423134824.png]]
>![[Pasted image 20230423134836.png]]

>![[Pasted image 20230423135019.png]]![[Pasted image 20230423135104.png]] 

File access operations -> read a logical record from file, write logical records on a file

File access can be:
- Sequential 
- Direct
- The access method:
	- independent of the physical device
	- independent of the allocation method of the files on the device

>Sequential:
>![[Pasted image 20230423135508.png]]

>Direct:
>![[Pasted image 20230423135538.png]]

![[Pasted image 20230423135553.png]]

![[Pasted image 20230423135750.png]]

![[Pasted image 20230423135828.png]]

![[Pasted image 20230423135845.png]]

![[Pasted image 20230423140556.png]]

![[Pasted image 20230423140613.png]]

file name ->(directory) file number offset ->(index structure) storage block

![[Pasted image 20230423140808.png]]

| FAT | |
| ----|-----|
| PRO | CONTRO |
|Easy to find free block|FAT size|
|Easy to append to a file| Limited metadata and no protection|
|Easy to delete a file|Random access is slow|
||Fragmentation|

>![[Pasted image 20230423141856.png]]
>![[Pasted image 20230423142019.png]]
>![[Pasted image 20230423142041.png]]


UNIX FFS:
- inode table (i-list) -> analogo FAT table
- inode:
	- Metadata -> file owner, access permissions, access times
	- Set of pointers to data blocks

![[Pasted image 20230423185404.png]]

![[Pasted image 20230423185416.png]]

![[Pasted image 20230423185431.png]]

>![[Pasted image 20230423185852.png]]
>![[Pasted image 20230423185909.png]]


FFS Asymmetric Tree:
- Small files: shallow tree-> EFFICIENT STORAGE FOR SMALL FILES
- Large files: deep tree -> Efficient lookup for random access in large files
- Sparse files: only fill pointers if needed

>![[Pasted image 20230423190303.png]]
>
>![[Pasted image 20230423190339.png]]

>FFS First Fit Block Allocation:
>![[Pasted image 20230423190452.png]]
>
>![[Pasted image 20230423190513.png]]
>
>![[Pasted image 20230423190522.png]]


| FFS | |
| ----|-----|
| PRO | CONTRO |
|Efficient storage for both small and large files|Inefficient for tiny files|
|Locality for both small and large files| Inneficient encoding when file is mostly contigous on disk|
|Locality for metadata and data|Need to reserve 10-20% of free space to prevent fragmentation|


>![[Pasted image 20230425155816.png]]
>![[Pasted image 20230425155858.png]]
>![[Pasted image 20230425155930.png]]
>![[Pasted image 20230425160017.png]]
>![[Pasted image 20230425160039.png]]
>file name offset ->(directory) file number offset ->(index structure) storage block
>![[Pasted image 20230425160200.png]]
> - Hard Link -> multiple directory entries map different name to the same file number
> - Soft link -> a directory entry that maps one name to another name
> ![[Pasted image 20230425160354.png]]

Architettura RAID:
- Realizza un disco virtuale di capacità superiore a quella dei singoli dischi
	- l'interfaccia è quella di un unico disco
- Sfrutta ol parallelismo per ottenere un accesso + veloce
	- i blocchi consecutivi di uno stesso file sono distribuiti sui dischi dell'array in modo da permettere operazioni contemporanee
- Sfrutta la ridondanza per accrescere l'affidabilità
	-  la ridondanza permentte di correggere gli errori di certi classi

![[Pasted image 20230425160815.png]]

Dischi RAID:
- Livello 0 -> Dischi asincroni, nessuna ridondanza (striping)
	- operazioni indipendenti in contemporanea
	- JBOD
- Livello 1 ->Dischi asincroni, disco con copie ridondanti (mirror)
	- operazioni indipendenti contemporanee e correzione errori
- Livello 2 -> Dischi sincroni, i dischi ridondanti contengono codici per la correzzione degli errori
	- NO operazioni indipendenti contemporanee, correzione errori
- Livello 3 -> Dischi sincroni, un solo disco ridondante
	- contiene la parità del contenuto degli altri dischi
	- NO operazioni indipendenti contemporanee, correzione errori
- Livello 4 -> Dischi asincroni, 1 disco ridondante
	- contiene la parità del contenuto degli altri rischi
	- SI operazioni contemporanee indipendenti e correzione errori
	- disco ridodante sovraccarico se si fanno molti aggiornamenti
- Livello 5 -> come livello 4 ma parità distribuita tra tutti i dischi
	- permette un miglior bilanciamento del carico tra i dischi
	- minimo 3 dischi
- Livello 6 -> come livello 5 ma parità doppia distribuita tra tutti i dischi
	- minimo 4 dischi, permette di tollerare fino al fallimento di 2 dischi
- livello 10 -> Dischi asincroni, Mirror di stripes
- Livello 01 -> Dischi asincroni, Stripe di mirror

Dischi asincroni -> vengono distribuite le stripes (singoli settori o sequenze di settori contigui)

![[Pasted image 20230425161934.png]]

Livello 4 -> strip di parità 
Livello 5 -> come 4 ma strip di parità distribuita nei vari dischi
![[Pasted image 20230425162114.png]]


Livello 01 -> Mirror di stripes -> ogni gruppo è un mirror di un RAID 0
Livello 10 -> Stripe di mirror -> ogni gruppo è un RAID 1 -> i gruppi realizzano un RAID 0
![[Pasted image 20230425162319.png]]

>![[Pasted image 20230425162448.png]]
>![[Pasted image 20230425162506.png]]

