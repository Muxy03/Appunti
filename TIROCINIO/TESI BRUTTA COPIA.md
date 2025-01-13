# 0. REFERENCES
- https://www.dmi.unict.it/barba/PROG-LANG/PROGRAMMI-TESTI/READING-MATERIAL/intro-prolog-II.pdf
- https://en.wikipedia.org/wiki/Horn_clause
- https://en.wikipedia.org/wiki/Prolog#History
- https://lpn.swi-prolog.org/lpnpage.php?pagetype=html&pageid=lpn-htmlse1

# 1. TECNOLOGIE USATE

Durante il tirocinio ho lavorato usando Prolog e C come linguaggi di programmazione.

Prolog è un linguaggio di programmazione dichiarativo, nello specifico a paradigma logico, creato nel 1972 da Alain Colmerauer e Philip Roussel.

I due creatori di Prolog si basarono sul lavoro di Robert Kowalski riguardo l'interpretazione procedurale delle clausole di Horn. Una clausola di Horn in calcolo proposizionale è una disgiunzione di letterali con al più un letterale non negato, questa forma specifica di proposizione permette tramite poche trasformazioni logiche di ottenere implicazioni dove la premessa è una congiunzione di letterali non negati e la conclusione è un singolo letterale non negato. La clausola di Horn infatti è alla base della definizione di Regole in Prolog come spiegheremo successivamente. 

ESEMPIO:
$$
\begin{aligned}
&0) &\neg A \lor \neg B \lor C \\
&1) &\neg(A \land B) \lor C \\
&2) &(A \land B) \Rightarrow C 

\end{aligned}
$$


In Prolog esistono 3 costrutti base: Fatti; Regole e  Queries, un programma in Prolog consiste in un insieme di Fatti e Regole che compongono la Knowledge base con cui interagiamo tramite le Queries.

Un Fatto in Prolog è in termini di logica un assioma, ovvero è una proposizione che si assume sia sempre vera. Questo costrutto viene utilizzato principalmente per definire il caso base di per una soluzione induttiva.

```prolog
madre(tiziana, andrea).
padre(riccardo, andrea).
```

Una regola in Prolog è un espressione riconducibile al caso di una clausola di Horn. La sintassi di questo costrutto  consiste in "testa :- corpo" :
- la testa della regola rappresenta una proposizione 
- il corpo della regola rappresenta una congiunzione di proposizioni
in termini di logica possiamo vedere questa relazione come $corpo \Rightarrow testa$, grazie alle caratteristiche delle clausole di Horn spiegate precedentemente.

Questo costrutto permette di definire relazioni all'interno della Knowledge base per risolvere queries più complicate.

```prolog
madre(tiziana, andrea).
padre(riccardo, andrea).

genitore(Genitore,Figlio) :- madre(Genitore,Figlio).
genitore(Genitore,Figlio) :- padre(Genitore,Figlio).
```

Il Backtracking è un meccanismo fondamentale che permette a Prolog di trovare tutte le risposte che soddisfano una determinata query basandosi sulla knowledge base. Il nome derivano dal fatto che se durante l'esplorazione Prolog incontra un fallimento può tornare indietro lungo l'albero delle possibilità per continuare ad vagliare le altre possibili soluzioni.