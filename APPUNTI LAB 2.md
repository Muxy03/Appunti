[PAGINE MAN](https://linux.die.net/man/)

[PUNTATORI](./PDF/LAB2/Lezione3.pdf)

le stringhe terminano con '\\0'

stdin -> 0
stdout -> 1
stderr -> 2
fopen mode:
1. r -> reading -> Open text file for reading.  The stream is positioned at the beginning of the file.
2.  r+ -> Open for reading and writing.  The stream is positioned at the beginning of the file.
3. w -> Truncate  file  to zero length or create text file for writing.  The stream is positioned at the beginning of the file.
4.  w+ -> Open for reading and writing.  The file is created if it does not exist, otherwise it is  truncated.   The stream is positioned at the beginning of the file.
5. a -> Open for appending (writing at end of file).  The file is created if it does not exist.  The stream is positioned at the end of the file.
6. a+ -> Open for reading and appending (writing at end of file).  The file is created if it does not exist.   Output  is always appended to the end of the file.  POSIX is silent on what the initial read position is when using this mode.  For glibc, the initial file position for reading is at the beginning of  the  file,  but for Android/BSD/MacOS, the initial file position for reading is at the end of the file.

![[Pasted image 20230623022701.png]]

[man fprintf](https://linux.die.net/man/3/fprintf)

fclose() -> flushes the stream pointed to by stream (writing any buffered output data using fflush(3)) and closes the underlying file descriptor.

[man perror](https://linux.die.net/man/3/perror)

[man errno](https://linux.die.net/man/3/errno)

codici sui puntatori -> lezione 7
 "%4s" -> 4 implica la larghezza minima della stringa -> no overflow

![[Pasted image 20230707164751.png]] -> equivalenti

"%-4s" -> left justify

![[Pasted image 20230707164928.png]]

![[Pasted image 20230707170103.png]]

![[Pasted image 20230707170415.png]]

[scanf](./PDF/LAB2/Lezione8.pdf) 

```makefile
# nei comandi associati ad ogni regola:  
#  $@ viene sostituito con il nome del target  
#  $< viene sostituito con il primo prerequisito  
#  $^ viene sostituito con tutti i prerequisiti  
  
# elenco degli eseguibili da creare  
EXECS=listacitta qsortint qsortcap  
  
# primo target: gli eseguibili sono precondizioni  
# quindi verranno tutti creati  
all: $(EXECS)   
  
  
  
# regole per la creazione dei file oggetto x listacitta  
  
# versione con il comando di compilazione dato in   
# maniera esplicita (di solito non si fa)  
listastringhe.o: listastringhe.c listastringhe.h      
    gcc -std=c11 -Wall -g -c listastringhe.c  
  
# versione che usa le variabili (molto piu semplice)  
listacitta.o: listacitta.c listastringhe.h  
    $(CC) $(CFLAGS) -c $<
```

![[Pasted image 20230709182308.png]]

![[Pasted image 20230709182324.png]]

![[Pasted image 20230709182658.png]]

```python
# Pagine per approfondire:  
# https://pytutorial-it.readthedocs.io/it/python3.11/classes.html  
# https://docs.python.org/3/tutorial/classes.html  
# https://docs.python.org/3/reference/datamodel.html  
  
import math  
  
  
class Articolo:  
    articoli_totali = 0  # attributo/variabile di classe, condiviso tra tutte le istanze  
  
    def __init__(self, nome, prezzo, commenti=None): # commenti è un parametro opzionale  
        """  
        Metodo che viene chiamato durante la costruzione di una istanza di  
        Articolo per impostarne lo stato iniziale.  
        """  
        self.nome = nome  
        self.prezzo = prezzo  
        if commenti is None:  
            self.commenti = []  
        else:  
            self.commenti = commenti  
        # ^^^ self.nome, .prezzo, .commenti sono attributi di istanza  
        Articolo.articoli_totali += 1  # modifica dell'attributo di classe  
  
    def valuta(self, utente, stelline):  
        assert 1 <= stelline <= 5, "Stelline non valide"  
        # ^^^ a <= x <= b è una sintassi ammessa in Python (in Java no; in C compila, ma non ha la semantica che ci si aspetta)  
        self.commenti.append((utente, stelline))  
  
    def valutazione_media(self):  
        if len(self.commenti) == 0:  
            return 0  
  
        tot = 0  
        for _, stelline in self.commenti: # _ si usa per convenzione per indicare che un valore (in questo caso l'utente) non ci interessa  
            tot += stelline  
  
        # oppure le tre righe qui sopra si possono semplificare con la seguente espressione  
        # tot = sum(s for _, s in self.commenti)  
        return tot / len(self.commenti)  
  
    def sconta(self, percentuale):  
        assert 0 <= percentuale <= 100, "Percentuale non valida"  
        self.prezzo = self.prezzo - (self.prezzo * percentuale / 100)  
  
    @staticmethod  
    def prezzo_99_cent(prezzo):  
        """  
        Esempio di metodo statico. Nota che non c'è self come argomento.  
        """  
        nuovo_prezzo = math.floor(prezzo)  
        nuovo_prezzo += 0.99  
        return nuovo_prezzo  
  
    def __repr__(self):  
        """  
        Metodo chiamato da repr(oggetto), e dalla console REPL quando si  
        scrive oggetto e si preme invio.  
        Se possibile, l'implementazione deve restituire una stringa che,  
        quando passata a eval(), ricostruisce l'oggetto.  
        """  
        return f"Articolo('{self.nome}', {self.prezzo}, {self.commenti})"  
  
    def __str__(self):  
        """  
        Metodo chiamato da str(oggetto) e da print(oggetto).  
        Solitamente si implementa restituendo una stringa con una   
        rappresentazione informale/leggibile dell'oggetto.  
        """  
        stelline_medie = self.valutazione_media()  
        return f"{self.nome} - {self.prezzo}€ ({stelline_medie}/5)"  
  
    def __eq__(self, altro):  
        """Metodo chiamato dall'espressione oggetto == altro."""  
        return self.nome == altro.nome and self.prezzo == altro.prezzo and self.commenti == altro.commenti  
  
    def __hash__(self):  
        """  
        Metodo chiamato da hash(oggetto). È necessario implementarlo,  
        insieme a __eq__, se si vogliono inserire istanze di Articolo in  
        collezioni basate su funzioni hash, come i dizionari e gli insiemi  
        Python.  
        L'implementazione deve garantire: a == b implica hash(a) == hash(b).  
        """  
        tupla_commenti = tuple(self.commenti) # trasformo la lista dei commenti in una tupla per poterla usare con hash()  
        return hash((self.nome, self.prezzo, tupla_commenti))  
  
    def __lt__(self, altro):  
        """  
        Metodo chiamato dall'espressione oggetto < altro.   
        Viene usato ad esempio da sorted(lista_di_oggetti_Articolo).  
        """  
        return self.nome < altro.nome  
  
  
latte = Articolo("Latte 1LT", 1.20)  
print(latte.prezzo)             # accedere a un attributo di istanza  
latte.valuta("Mario", 5)        # chiamare un metodo di istanza  
latte.valuta("Roberta", 2)  
Articolo.prezzo_99_cent(6.55)   # chiamare un metodo statico  
print(Articolo.articoli_totali) # accedere a un attributo di classe  
  
# ---------------------  
# ESEMPIO DI ALIASING 1  
# ---------------------  
latte2 = latte   
# latte e latte2 ora fanno riferimento allo stesso oggetto, ossia id(latte2) == id(latte)  
latte2.prezzo = 1.50   
# ... quindi qui anche latte.prezzo == 1.50  
  
  
# ---------------------  
# ESEMPIO DI ALIASING 2  
# ---------------------  
def black_friday(articoli):  
    for articolo in articoli:  
        articolo.sconta(30)  
  
cuffie = Articolo("Cuffie Bluetooth", 50)  
pc = Articolo("PC portatile", 1200)  
da_scontare = [cuffie, pc]  
black_friday(da_scontare)  
# ora cuffie e pc sono scontati del 30%  
  
  
# ------------  
# EREDITARIETÀ  
# ------------  
class Film(Articolo):  
    def __init__(self, nome, prezzo, durata, commenti=None):  
        super().__init__(nome, prezzo, commenti)  
        self.durata = durata  
  
    # Per esercitarsi: sovrascrivere __str__, __eq__, __hash__ per includere anche la durata  
  
  
class Videogioco(Articolo):  
    def __init__(self, nome, prezzo, piattaforma, commenti=None):  
        super().__init__(nome, prezzo, commenti)  
        self.piattaforma = piattaforma  
          
    # Per esercitarsi: sovrascrivere __str__, __eq__, __hash__ per includere anche la piattaforma  
  
  
cod = Videogioco("Call of Duty", 59.99, "PC")  
avatar = Film("Avatar 2", 15.99, 120)  
black_friday([cod, avatar])  
  
  
# --------------------  
# OPERATORI ARITMETICI  
# --------------------  
  
class Razionale:  
    """  
    Esempio di classe che definisce operatori artimetici.  
    https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types  
    """  
  
    def __init__(self, numeratore, denominatore):  
        self.numeratore = numeratore  
        self.denominatore = denominatore  
  
    def __add__(self, altro):  
        """Metodo chiamato dall'espressione oggetto + altro."""  
        d = self.denominatore * altro.denominatore  
        n = self.numeratore * altro.denominatore + altro.numeratore * self.denominatore  
        return Razionale(n, d)  
  
    def __mul__(self, altro):  
        """Metodo chiamato dall'espressione oggetto * altro."""  
        n = self.numeratore * altro.numeratore  
        d = self.denominatore * altro.denominatore  
        return Razionale(n, d)  
  
    def __str__(self):  
        return f"{self.numeratore}/{self.denominatore}"  
      
     # Per esercitarsi: implementare __sub__  
  
  
r1 = Razionale(2, 3)  
r2 = Razionale(1, 5)  
print(r1 * r2)
```

![[Pasted image 20230710231419.png]]

![[Pasted image 20230710231330.png]]

![[Pasted image 20230710231345.png]]

![[Pasted image 20230710231701.png]]

![[Pasted image 20230710231717.png]]

![[Pasted image 20230710231824.png]]

![[Pasted image 20230710232538.png]]

![[Pasted image 20230710232928.png]]

pipe -> 0read, 1write

fifo -> named pipe -> scrive solo se qualcuno legge

![[Pasted image 20230710233637.png]]

```C
// ---- semafori POSIX

// IMPORTANTE: i semafori posix sono usati sia da processi che da threads
// Nel caso dei threads, non è opportuno eseguire in caso di errore exit(1)
// in quanto questo fa terminare tutti i thread del processo: bisognerebbe
// chiamare pthread_exit() che fa terminare solo il thread corrente
// (usare pthread_exit per i processi ugualmente non è accettabile 
// perché poi invoca exit(0)). 
// Si potrebbe distinguere thread da processi con gettid(2)

// semafori NAMED
sem_t *xsem_open(const char *name, int oflag, mode_t mode, 
              unsigned int value,  int linea, char *file) {
  sem_t *s = sem_open(name,oflag,mode,value);
  if (s==SEM_FAILED) {
    perror("Errore sem_open");
    fprintf(stderr,"== %d == Linea: %d, File: %s\n",getpid(),linea,file); 
    exit(1);
  }
  return s;
}

int xsem_close(sem_t *s, int linea, char *file)
{
  int e = sem_close(s);
  if(e!=0) {
    perror("Errore sem_close"); 
    fprintf(stderr,"== %d == Linea: %d, File: %s\n",getpid(),linea,file);
    exit(1);
  }
  return e;  
}

int xsem_unlink(const char *name, int linea, char *file)
{
  int e = sem_unlink(name);
  if(e!=0) {
    perror("Errore sem_unlink"); 
    fprintf(stderr,"== %d == Linea: %d, File: %s\n",getpid(),linea,file);
    exit(1);
  }
  return e;  
}

// semafori UNNAMED
int xsem_init(sem_t *sem, int pshared, unsigned int value, int linea, char *file) {
  int e = sem_init(sem,pshared,value);
  if(e !=0) {
    perror("Errore sem_init"); 
    fprintf(stderr,"== %d == Linea: %d, File: %s\n",getpid(),linea,file);
    exit(1);
  }
  return e;
}

int xsem_destroy(sem_t *sem, int linea, char *file) {
  int e = sem_destroy(sem);
  if(e !=0) {
    perror("Errore sem_destroy"); 
    fprintf(stderr,"== %d == Linea: %d, File: %s\n",getpid(),linea,file);
    exit(1);
  }
  return e;
}

// comuni NAMED e UNNAMED
int xsem_post(sem_t *sem, int linea, char *file) {
  int e = sem_post(sem);
  if(e !=0) {
    perror("Errore sem_post"); 
    fprintf(stderr,"== %d == Linea: %d, File: %s\n",getpid(),linea,file);
    exit(1);
  }
  return e;
}

int xsem_wait(sem_t *sem, int linea, char *file) {
  int e = sem_wait(sem);
  if(e !=0) {
    perror("Errore sem_wait"); 
    fprintf(stderr,"== %d == Linea: %d, File: %s\n",getpid(),linea,file);
    exit(1);
  }
  return e;
}


```


![[Pasted image 20230710234706.png]]

![[Pasted image 20230710235038.png]]

[system call](obsidian://open?vault=Appunti&file=PDF%2FLAB2%2FLibrary%20functions%20vs%20System%20Calls.pdf)

[prodcons](obsidian://open?vault=Appunti&file=PDF%2FLAB2%2Fprodcons.pdf)

![[Pasted image 20230710235528.png]]

![[Pasted image 20230711000838.png]]

![[Pasted image 20230711001102.png]]

![[Pasted image 20230711001148.png]]

lezioni 40 in poi
