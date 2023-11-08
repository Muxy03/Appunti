
PC -> Instruction memory -> Workbench -> data memory

SINGLE CYCLE:
- DATAPATH:
	- LDR:
		1. registro sorgente -> Instr 19:16 -> ingresso A1 e uscita RD1
		2. spiazzamento -> Instr 11:0 -> esteso a 32 bit
		3. ALU somma RD1 e lo spiazzamento -> ALUControl = 00 -> indirizzo risultato -> data memory -> ingresso WD3 (scrittura)
		4. registro dest -> Instr 15:12 -> ingresso A3 -> RegWrite ( porta WE3)
		5. PC' = PC+4 o uscita data memory -> PCSrc (0 o 1)
	- STR:
		1. uguale ad LDR da 1 a 3
		2. reg dest -> Instr 15:12 -> ingresso A2 e uscita RD2 -> ingresso WD data memory -> MemWrite
		3. ALUControl = 00 e MemWrite = 1 e RegWrite = 0
	- ADD/SUB/... (indirizzamento immediato) :
		1. immediato da 8 bit non da 12 -> ImmSrc = 0
		2. MemToReg = 0 -> per selezionare il risultato della ALU -> è 1 solo nella LDR
	-  ADD/SUB/... (indirizzamento registro):
		1.  secondo operando Rm -> Instr 3:0
		2.  in A2 entra Rm (per STR entra Rd) -> RegSrc
		3. ALUSrc = 0 per scegliere RD2 (è 1 per scegliere l'immediato)
	- B:
		1. immediato da 24 bit +(PC+8) -> ImmSrc 2 bit -> 00=Imm8; 01=Imm12; 10=Imm24 moltiplicato per 4
		2. PC+8 /15 entra in A1 -> RegSrc = 1, MemtoReg = 0 e PCSrc = 1

- CONTROL UNIT:
	- INPUT: Instr 31:28, Instr 27:26, Instr 25:20, Instr 15:12, ALUflags -> Cond, op, funct, Rd
	- Decoder -> segnali di controllo in base a Instr
		- usa funct per determinare operazione ALU
		- decide se PC deve essere modificato per una b o una scrittura in R15
		- invia: MemtoReg, ALUSrc, ALUControl, ImmSrc$_{1:0}$, RegSrc$_{1:0}$ , MemWrite e RegWrite
		- Decoder Principale ->genera: Branch, RegW, MemW, MemtoReg, ALUSrc, ImmSrc$_{1:0}$, RegSrc$_{1:0}$ -> funct 5:0
		- Decoder ALU -> riceve ALUop dall'altro decoder -> genera: NoWrite, ALUControl, FlagW -> funct 4:0
		- Logica del PC ->  PCS = ((Rd == 15) & RegW)|Branch -> Rd 3:0
		- segnali Branch (istr B o meno) e ALUOp usati all'interno della control unit 
	- Logica condizionale -> mantiene le flag di stato e abilita gli aggiornamenti dello stato architetturale quando ho un instruzione condizionata