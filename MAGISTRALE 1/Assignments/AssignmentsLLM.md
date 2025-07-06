Ecco le soluzioni dettagliate a tutti gli esercizi presenti in "Assignments", presentate in formato Markdown come richiesto.

---

## **Problema 1 (Pagina 1): Gioco di Divisione del Denaro**

**Descrizione del Gioco:**
Due persone nominano un numero intero tra . Ci sono $10 a disposizione.

*   **Caso 1: Somma <= 10.** Ogni persona riceve l'ammontare nominato. Il resto del denaro viene distrutto.
*   **Caso 2: Somma > 10.**
    *   Se gli ammontari sono diversi: la persona che ha nominato l'ammontare minore riceve tale ammontare, l'altra persona riceve il denaro restante.
    *   Se gli ammontari sono uguali: ciascuna persona riceve $5.

**Obiettivo:** Trovare gli equilibri di Nash utilizzando la funzione di migliore risposta.

**Modello del Gioco:**
*   **Giocatori:** Persona 1 (G1), Persona 2 (G2).
*   **Azioni:** Per ogni giocatore `i`, l'azione `a_i` è un numero intero `x_i ∈ `.
*   **Funzione di Payoff (u_i):**
    Sia `x` la scelta di G1 e `y` la scelta di G2.

    *   **Se x + y <= 10:**
        *   `u1(x,y) = x`
        *   `u2(x,y) = y`
    *   **Se x + y > 10:**
        *   **Se x != y:**
            *   Se `x < y`: `u1(x,y) = x`, `u2(x,y) = 10 - x`
            *   Se `x > y`: `u1(x,y) = 10 - y`, `u2(x,y) = y`
        *   **Se x = y:**
            *   `u1(x,y) = 5`
            *   `u2(x,y) = 5`

**Analisi delle Migliori Risposte:**

Cerchiamo la migliore risposta per G1 per ogni scelta `y` di G2. Per simmetria, la migliore risposta per G2 sarà analoga.

*   **Migliore Risposta di G1 (BR1(y)):**
    1.  **Consideriamo `y < 5`:**
        *   Se G1 sceglie `x` tale che `x + y <= 10` (ovvero `x <= 10 - y`), G1 riceve `x`. Per massimizzare, G1 vorrebbe `x = 10 - y`. Payoff di G1: `10 - y`.
        *   Se G1 sceglie `x` tale che `x + y > 10` e `x != y`, G1 riceve `10 - y`.
        *   Se G1 sceglie `x = y`, (il che implicherebbe `x > 5` dato `y < 5`, quindi `x+y > 10` e `x=y` è possibile solo se `y > 5` nel caso di 5$ a testa), ma dato `y < 5`, `x=y` non è una buona opzione.
        *   Dato che `y < 5`, `10 - y > 5`. Quindi il payoff `10 - y` è il migliore possibile.
        *   La scelta `x = 10 - y` produce `x + y = 10` (se `x = 10 - y` e `y > 0`) o `x+y < 10` (se `x < 10-y`), dando a G1 `x`. O se `x = 10-y` e `x+y > 10` (non possibile), o `x=y` (non possibile).
        *   **BR1(y) = 10 - y** (payoff `10 - y`).
            *   Esempio: Se `y = 0`, G1 sceglie `x = 10`. Payoff `(10,0)`.
            *   Esempio: Se `y = 4`, G1 sceglie `x = 6`. Payoff `(6,4)`.

    2.  **Consideriamo `y = 5`:**
        *   Se G1 sceglie `x <= 5` (quindi `x + y <= 10`), G1 riceve `x`. Il massimo in questo intervallo è `x = 5`, con payoff `5`.
        *   Se G1 sceglie `x > 5` (quindi `x + y > 10` e `x != y`), G1 riceve `10 - y = 10 - 5 = 5`.
        *   Se G1 sceglie `x = y = 5`, G1 riceve `5` (payoff `5`).
        *   Tutte le scelte `x ∈ [1, 2]` danno un payoff di `5`. Le scelte `x < 5` danno un payoff minore di `5`.
        *   **BR1(5) = `x ∈ [1, 2]`** (payoff `5`).

    3.  **Consideriamo `y > 5`:**
        *   Se G1 sceglie `x` tale che `x + y <= 10` (ovvero `x <= 10 - y`), G1 riceve `x`. Poiché `y > 5`, `10 - y < 5`. Quindi il massimo payoff da questa opzione è `10 - y`, che è minore di 5.
        *   Se G1 sceglie `x` tale che `x + y > 10` e `x != y`, G1 riceve `10 - y`, che è minore di 5.
        *   Se G1 sceglie **`x = y`**, G1 riceve `5`.
        *   Confrontando i payoff, `5` è il valore più alto.
        *   **BR1(y) = y** (payoff `5`).
            *   Esempio: Se `y = 6`, G1 sceglie `x = 6`. Payoff `(5,5)`.
            *   Esempio: Se `y = 10`, G1 sceglie `x = 10`. Payoff `(5,5)`.

**Riepilogo delle Funzioni di Migliore Risposta:**
*   **BR1(y):**
    *   `10 - y` se `y < 5`
    *   `[1, 2]` se `y = 5`
    *   `y` se `y > 5`
*   **BR2(x):** (Simmetrica a BR1(y))
    *   `10 - x` se `x < 5`
    *   `[1, 2]` se `x = 5`
    *   `x` se `x > 5`

**Equilibri di Nash (NE):**
Un profilo di azioni `(x,y)` è un equilibrio di Nash se `x ∈ BR1(y)` e `y ∈ BR2(x)`.

1.  **Caso `y < 5` (e quindi `x = 10 - y`):**
    *   Dato che `y < 5`, `x = 10 - y > 5`.
    *   Dalla funzione BR2(x) per `x > 5`, G2 dovrebbe scegliere `y = x`.
    *   Sostituendo `x = 10 - y` in `y = x`, otteniamo `y = 10 - y`, quindi `2y = 10`, `y = 5`.
    *   Questo contraddice l'assunzione `y < 5`. **Nessun NE in questo intervallo.**

2.  **Caso `y = 5`:**
    *   BR1(5) = `x ∈ [1, 2]`.
    *   Controlliamo i valori di `x` in questo intervallo:
        *   Se `x = 5`: `x ∈ BR1(5)` è vero. Dalla BR2(5), `y ∈ [1, 2]`, quindi `y=5` è una migliore risposta per G2.
        *   **`(5,5)` è un NE.** Payoff `(5,5)`.
        *   Se `x ∈ (5, 10]` (cioè `x > 5`): `x ∈ BR1(5)` è vero. Dalla BR2(x) per `x > 5`, G2 dovrebbe scegliere `y = x`. Per avere un NE, `y` dovrebbe essere `5` (perché siamo nel caso `y=5`) e `x` dovrebbe essere `5` (perché `y=x`). Questo contraddice `x > 5`. **Nessun altro NE in questo intervallo.**

3.  **Caso `y > 5` (e quindi `x = y`):**
    *   Dalla funzione BR2(x) per `x > 5`, G2 dovrebbe scegliere `y = x`.
    *   Questa condizione (`y = x`) è già soddisfatta dall'assunzione.
    *   Quindi, ogni profilo di azione **`(x,x)` dove `x > 5` è un NE.**
    *   Questo include i profili: `(6,6), (7,7), (8,8), (9,9), (10,10)`.
    *   Per tutti questi equilibri, poiché `x = y` e `x+y > 10`, il payoff per entrambi i giocatori è **`(5,5)`**.

**Conclusioni sugli Equilibri di Nash:**
Gli equilibri di Nash per questo gioco sono:
*   **`(5,5)`**
*   **`(6,6)`**
*   **`(7,7)`**
*   **`(8,8)`**
*   **`(9,9)`**
*   **`(10,10)`**

In tutti questi equilibri, entrambi i giocatori ricevono un payoff di 5.

---

## **Problema 2 (Pagina 1): Nuova Legislazione sulla Responsabilità dei Giudici**

**Situazione:**
Una nuova legge rende i giudici personalmente responsabili per i loro errori, consentendo agli accusati di citarli in giudizio e farli punire in caso di errore.

**Obiettivo:** Dimostrare formalmente la correttezza o l'erroneità di questa legge, attingendo ai concetti di teoria dei giochi e scelta razionale.

**Analisi dal punto di vista della Teoria della Scelta Razionale e dei Giochi:**

Questa situazione può essere modellata come un gioco in cui le parti interessate (giudici e accusati) agiscono in base alle proprie preferenze per massimizzare il proprio "payoff".

*   **Giocatori:**
    *   **Giudice (G):** Il decisore incaricato di emettere una sentenza.
    *   **Accusato (A):** La parte in causa che può subire le conseguenze della sentenza e, con la nuova legge, può agire contro il giudice.

*   **Azioni (e loro implicazioni prima e dopo la legge):**
    *   **Giudice:**
        *   `S` (Sentenza corretta/secondo la legge e le prove): Idealmente, il giudice desidera emettere sentenze corrette per professionalità, integrità e per evitare ribaltamenti in appello.
        *   `I` (Sentenza scorretta/errata): Il giudice potrebbe emettere una sentenza errata per negligenza, bias o pressione.
    *   **Accusato:**
        *   `C` (Citare in giudizio il giudice): Questa azione è disponibile solo con la nuova legge, in caso di percepito errore. L'accusato desidera ottenere giustizia, compensazione o annullare una sentenza sfavorevole.
        *   `NC` (Non citare in giudizio il giudice): L'accusato accetta la sentenza o cerca altre vie di ricorso (es. appello classico).

*   **Payoff e Incentivi:**

    1.  **Prima della legge:**
        *   Il giudice ha un incentivo primario a emettere sentenze corrette. Le conseguenze di una sentenza errata sono principalmente professionali (reputazione, carriera) o procedurali (annullamento in appello). Il payoff del giudice è massimo per sentenze corrette.
        *   L'accusato valuta il costo/beneficio dell'appello.

    2.  **Dopo la legge (introduzione della responsabilità personale):**
        *   **L'obiettivo del Giudice** ora diventa prioritariamente **evitare di essere citato in giudizio e subire una punizione personale**. Questa è una motivazione molto forte per un decisore razionale, come illustrato dal concetto di preferenza e massimizzazione dell'utilità .

        *   **Analisi delle conseguenze (confrontando payoff):**
            *   **Scenario Ideale (e irrealistico):** Il giudice emette una sentenza corretta (`S`). L'accusato non ha motivo di citare in giudizio (`NC`). Entrambi sono in una situazione "buona" (giustizia è fatta, giudice non punito).
            *   **Scenario con Rischio (dopo la legge):**
                *   Se il giudice deve prendere una decisione `S` **difficile o controversa**, che potrebbe essere *percepita* come un errore (anche se legalmente corretta) da una delle parti, si trova di fronte a un dilemma.
                *   La **paura della citazione in giudizio e della punizione personale** diventa un fattore dominante. Un giudice razionale potrebbe optare per una sentenza `I` (scorretta) che minimizzi il rischio personale, anche se non è la più giusta o legalmente solida. Questo è un esempio di **incentivo perverso**             *   **Esempi di comportamenti perversi:**
                    *   **Aversione al rischio:** I giudici potrebbero evitare di prendere decisioni audaci o innovative, anche se necessarie, preferendo sentenze "sicure" (es. che seguono strettamente precedenti o che favoriscono parti meno propense a citare in giudizio), anche se ciò porta a risultati meno equi.
                    *   **Aumento delle denunce:** La legge incentiva gli accusati a citare in giudizio i giudici, anche per motivi futili, come tattica intimidatoria o per puro dispetto, sapendo che la semplice minaccia di un procedimento personale può influenzare il comportamento del giudice.
                    *   **Effetto di "raffreddamento" (Chilling Effect):** I giudici potrebbero essere meno disposti a emettere sentenze che vanno contro l'opinione pubblica o interessi forti, per evitare di diventare bersaglio di cause legali. Questo mina l'indipendenza e l'imparzialità della magistratura.
                    *   **Deterioramento della qualità della magistratura:** La prospettiva di responsabilità personale e contenziosi costanti potrebbe scoraggiare i migliori professionisti legali dall'intraprendere la carriera di giudice, portando a una diminuzione della qualità complessiva della magistratura.

**Conclusione Formale sulla Legge:**

Basandosi sulla teoria della scelta razionale , un decisore (il giudice) cercherà di massimizzare il proprio payoff e minimizzare i propri costi/rischi. La legge proposta introduce un **costo personale significativo** (punizione, citazione in giudizio) per l'errore percepito. Questo altera l'insieme delle preferenze e degli incentivi del giudice, spostando il focus dalla "giustizia legale" alla "sicurezza personale".

La legge è **scorretta** nel raggiungere il suo probabile obiettivo di migliorare la giustizia. Invece di incentivare la correttezza, essa crea:
*   **Incentivi perversi:** Spinge i giudici a comportamenti volti a minimizzare il rischio personale piuttosto che a massimizzare la giustizia.
*   **Aumento della litigiosità:** Incoraggia un eccesso di cause contro i giudici, sovraccaricando il sistema giudiziario.
*   **Deterioramento dell'indipendenza e qualità:** Rende la carriera giudiziaria meno attraente e mina la capacità dei giudici di operare imparzialmente.

Analogamente al "Dilemma del Prigioniero"  o al "Gioco dell'Inquinamento" , dove l'azione razionale individuale porta a un risultato collettivamente subottimale, in questo caso l'azione razionale del giudice (evitare la punizione) porta a un sistema giudiziario meno efficiente e meno giusto per la società nel suo complesso.

---

## **Problema 3 (Pagina 1): Gioco di Contribuzione a un Fondo**

**Descrizione del Gioco:**
Un'agenzia di investimento propone un contratto a un gruppo di `N` persone per raccogliere denaro per un progetto. Ogni membro può liberamente decidere di:
*   Contribuire con 100 euro (`C`).
*   Non contribuire (mantenendo il denaro nel proprio portafoglio) (`NC`).
Indipendentemente dalla scelta, dopo un anno, il fondo verrà ricompensato con un interesse del 50% e ridistribuito uniformemente tra tutti gli `N` membri del gruppo.

**Obiettivo:** Descrivere il gioco e trovare l'equilibrio di Nash.

**Modello del Gioco:**
*   **Giocatori:** Gli `N` membri del gruppo, indicati da `i = 1, ..., N`.
*   **Azioni per ogni giocatore `i`:** `A_i = {Contribuire (C), Non Contribuire (NC)}`.
*   **Profilo di Azioni:** Una combinazione di scelte per tutti gli `N` giocatori, `(a_1, a_2, ..., a_N)`.
*   **Funzione di Payoff (u_i):**
    Sia `k` il numero totale di giocatori che scelgono di `Contribuire (C)`.

    *   **Totale raccolto nel fondo:** `k * 100` euro.
    *   **Valore totale del fondo dopo interesse (50%):** `(k * 100) * 1.50 = 150k` euro.
    *   **Importo ricevuto da ciascun membro (ridistribuzione uniforme):** `(150k) / N` euro.

    *   **Payoff del giocatore `i`:**
        *   **Se il giocatore `i` sceglie `C` (Contribuisce):** Il costo iniziale è 100 euro.
            `u_i(C) = (150k / N) - 100`
        *   **Se il giocatore `i` sceglie `NC` (Non Contribuisce):** Nessun costo iniziale.
            `u_i(NC) = (150k / N)`

**Analisi dell'Equilibrio di Nash:**

Per trovare l'equilibrio di Nash, dobbiamo determinare la migliore risposta di un giocatore generico `i` in base alle azioni degli altri `N-1` giocatori.
Sia `k_altri` il numero di altri giocatori che contribuiscono.
Quindi, il numero totale di contributori `k` sarà:
*   `k = k_altri` se il giocatore `i` sceglie `NC`.
*   `k = k_altri + 1` se il giocatore `i` sceglie `C`.

Confrontiamo i payoff per il giocatore `i`:

*   **Payoff se `i` sceglie `NC`:** `u_i(NC) = (150 * k_altri) / N`
*   **Payoff se `i` sceglie `C`:** `u_i(C) = (150 * (k_altri + 1)) / N - 100`

Il giocatore `i` sceglierà `NC` se `u_i(NC) > u_i(C)`.
` (150 * k_altri) / N > (150 * (k_altri + 1)) / N - 100 `
` (150 * k_altri) / N > (150 * k_altri) / N + (150 / N) - 100 `
` 0 > (150 / N) - 100 `
` 100 > 150 / N `
` 100N > 150 `
` N > 1.5 `

**Due casi possibili per `N`:**

1.  **Se `N >= 2` (caso tipico di un gruppo):**
    *   Poiché `N` è un numero intero, `N > 1.5` è sempre vero per `N >= 2`.
    *   Questo significa che, per qualsiasi numero di altri contributori `k_altri`, il payoff per il giocatore `i` è sempre maggiore se sceglie `NC` piuttosto che `C`.
    *   **`NC` è una strategia dominante** per ogni giocatore `i` se `N >= 2`.
    *   L'unico equilibrio di Nash si verifica quando **tutti i giocatori scelgono `NC`**.
    *   In questo equilibrio, `k = 0` (nessuno contribuisce), e il payoff di ogni giocatore è `(150 * 0) / N = 0`.
    *   Questo è un classico **problema del free-rider** , in cui la scelta razionale individuale porta a un risultato collettivamente subottimale. Se tutti avessero contribuito (il che non è un NE), il payoff di ciascuno sarebbe stato `(150N / N) - 100 = 150 - 100 = 50` euro.

2.  **Se `N = 1` (un solo giocatore):**
    *   Questa è una situazione degenerata in cui non c'è interazione strategica.
    *   Se il giocatore sceglie `NC`: `k = 0`, payoff `0`.
    *   Se il giocatore sceglie `C`: `k = 1`, payoff `(150 * 1 / 1) - 100 = 50`.
    *   La migliore risposta è `C`. L'equilibrio di Nash è **`(C)`**.

**Conclusione:**

Per un gruppo di `N >= 2` persone, l'equilibrio di Nash di questo gioco è che **tutti i membri scelgono di non contribuire (NC)**. In questo equilibrio, nessuno riceve alcun guadagno dal fondo, e il progetto non viene finanziato. Questo scenario è un esempio di come le scelte individualmente razionali possano portare a un risultato collettivamente inefficiente, simile al Dilemma del Prigioniero o al Gioco dell'Inquinamento .

---

## **Problema 1 (Pagina 2): Sasso, Carta, Forbice**

**Descrizione del Gioco:**
Sasso, carta, forbice è un gioco per due giocatori in cui si sceglie simultaneamente una delle tre gestualità: Sasso (pugno chiuso), Carta (mano aperta), Forbice (due dita estese).
*   Sasso rompe Forbice (Sasso vince).
*   Carta copre Sasso (Carta vince).
*   Forbice taglia Carta (Forbice vince).
*   Se entrambi i giocatori scelgono la stessa gestualità, è un pareggio, e si rigioca (per semplicità, consideriamo il pareggio come un payoff di 0 per entrambi).
*   Vittoria: +1, Sconfitta: -1, Pareggio: 0.

**Obiettivo:**
1.  Costruire la matrice dei payoff.
2.  Trovare gli equilibri di Nash in strategie pure.
3.  Trovare un equilibrio di Nash in strategie miste.
4.  Calcolare il payoff atteso per un giocatore (il gioco è simmetrico).

**1. Matrice dei Payoff:**
Siano G1 (giocatore 1) e G2 (giocatore 2). I payoff sono (payoff G1, payoff G2).

| G1 \ G2 | Sasso (R) | Carta (P) | Forbice (S) |
| :------ | :-------- | :-------- | :---------- |
| **Sasso (R)** | (0,0)     | (-1,1)    | (1,-1)      |
| **Carta (P)** | (1,-1)    | (0,0)     | (-1,1)      |
| **Forbice (S)** | (-1,1)    | (1,-1)    | (0,0)       |

**2. Equilibri di Nash (Strategie Pure):**
Un profilo di strategie (azione G1, azione G2) è un equilibrio di Nash se nessun giocatore può migliorare unilateralmente il proprio payoff cambiando la propria azione, data la scelta dell'altro giocatore.
Analizziamo ogni cella della matrice:

*   **(R,R):** Se G2 gioca R, G1 preferisce P (1 vs 0). Non è NE.
*   **(R,P):** Se G2 gioca P, G1 preferisce P (0 vs -1). Non è NE.
*   **(R,S):** Se G2 gioca S, G1 preferisce R (1 vs -1). G2 gioca S, G1 gioca R. Se G1 gioca R, G2 preferisce P (1 vs -1). Non è NE.
*   **(P,R):** Se G1 gioca P, G2 preferisce P (0 vs -1). Non è NE.
*   **(P,P):** Se G2 gioca P, G1 preferisce S (1 vs 0). Non è NE.
*   **(P,S):** Se G2 gioca S, G1 preferisce S (0 vs -1). G2 gioca S, G1 gioca P. Se G1 gioca P, G2 preferisce S (1 vs -1). Non è NE.
*   **(S,R):** Se G1 gioca S, G2 preferisce R (0 vs -1). G1 gioca S, G2 gioca R. Se G1 gioca S, G2 preferisce R (1 vs -1). Non è NE.
*   **(S,P):** Se G2 gioca P, G1 preferisce R (1 vs -1). Non è NE.
*   **(S,S):** Se G2 gioca S, G1 preferisce R (1 vs 0). Non è NE.

**Conclusione: Non esistono equilibri di Nash in strategie pure** per Sasso, Carta, Forbice. Questo è tipico dei giochi puramente conflittuali o "strettamente competitivi" .

**3. Equilibrio di Nash (Strategie Miste):**
Una strategia mista è una distribuzione di probabilità sulle strategie pure di un giocatore. In un NE di strategie miste, ogni giocatore deve essere indifferente tra tutte le strategie pure giocate con probabilità positiva. Ciò significa che il payoff atteso di ciascuna strategia pura deve essere uguale.

Sia `p_R, p_P, p_S` le probabilità con cui G1 gioca R, P, S (`p_R + p_P + p_S = 1`).
Sia `q_R, q_P, q_S` le probabilità con cui G2 gioca R, P, S (`q_R + q_P + q_S = 1`).

**Payoff Atteso per G1 (EP1):**
*   EP1(R | q_R, q_P, q_S) = `0*q_R + (-1)*q_P + 1*q_S = -q_P + q_S`
*   EP1(P | q_R, q_P, q_S) = `1*q_R + 0*q_P + (-1)*q_S = q_R - q_S`
*   EP1(S | q_R, q_P, q_S) = `(-1)*q_R + 1*q_P + 0*q_S = -q_R + q_P`

Per l'indifferenza di G1, i payoff attesi devono essere uguali:
1.  `-q_P + q_S = q_R - q_S`  =>  `q_R + q_P = 2q_S`
2.  `q_R - q_S = -q_R + q_P`  =>  `2q_R = q_P + q_S`

Sappiamo anche che `q_R + q_P + q_S = 1`.
Sostituendo `q_P + q_S = 2q_R` (dalla eq. 2) nell'equazione di somma:
`q_R + 2q_R = 1` => `3q_R = 1` => **`q_R = 1/3`**.

Dalla eq. 2: `2*(1/3) = q_P + q_S` => `q_P + q_S = 2/3`.
Dalla eq. 1: `q_R + q_P = 2q_S` => `1/3 + q_P = 2q_S` => `1/3 = 2q_S - q_P`.

Abbiamo un sistema:
`q_P + q_S = 2/3`
`-q_P + 2q_S = 1/3`
Sommando le due equazioni: `3q_S = 1` => **`q_S = 1/3`**.
Sostituendo `q_S = 1/3` in `q_P + q_S = 2/3`: `q_P + 1/3 = 2/3` => **`q_P = 1/3`**.

Quindi, per rendere G1 indifferente, G2 deve giocare ciascuna delle sue strategie pure con probabilità **(1/3, 1/3, 1/3)**.

Poiché il gioco è simmetrico, per rendere G2 indifferente, G1 deve giocare ciascuna delle sue strategie pure con probabilità **(1/3, 1/3, 1/3)**.

**Equilibrio di Nash in Strategie Miste:**
Entrambi i giocatori giocano Sasso, Carta e Forbice con probabilità **1/3 ciascuno**.
(G1: (1/3, 1/3, 1/3), G2: (1/3, 1/3, 1/3)).

**4. Calcolo del Payoff Atteso per un Giocatore:**
Poiché in un NE di strategie miste un giocatore è indifferente tra le sue strategie pure (giocate con probabilità positiva), il payoff atteso complessivo è uguale al payoff atteso di una qualsiasi di quelle strategie pure.
Calcoliamo il payoff atteso per G1 quando G2 gioca (1/3, 1/3, 1/3):
EP1(R) = `-q_P + q_S = -1/3 + 1/3 = 0`.
Quindi, il payoff atteso per G1 è `0`.
Per simmetria, il payoff atteso per G2 è anch'esso `0`.

**Il payoff atteso per entrambi i giocatori nell'equilibrio di Nash in strategie miste è 0.**

---

## **Problema 2 (Pagina 2): Gioco Hawk-Dove (Auto sul Ponte)**

**Descrizione del Gioco:**
Due auto si trovano su lati opposti di un lungo ponte stretto, dove solo una macchina può passare alla volta. Se entrambe tentano di attraversare, si scontrano e rimangono bloccate per ore. In alternativa, ciascun conducente può decidere di prendere una strada secondaria più lunga ma sicura.

**Obiettivo:**
1.  Modellare la situazione come un gioco.
2.  Trovare gli equilibri di Nash.
3.  Discutere una possibile strategia mista.

**1. Modellare il Gioco:**
Questo è un classico esempio di "Chicken Game" o "Hawk-Dove Game".

*   **Giocatori:** Auto 1 (A1), Auto 2 (A2).
*   **Azioni:**
    *   `A` (Attraversare il ponte)
    *   `S` (Prendere la strada secondaria)

*   **Payoff:** (Payoff A1, Payoff A2)
    *   **Entrambe Attraversano (A,A):** Scontro e ore di blocco. Questo è l'esito peggiore. Assegniamo un payoff di **(-10, -10)**.
    *   **A1 Attraversa, A2 Secondaria (A,S):** A1 passa velocemente, A2 impiega più tempo ma evita il blocco. Questo è l'esito migliore per A1 e accettabile per A2. Assegniamo **(5, -1)**.
    *   **A1 Secondaria, A2 Attraversa (S,A):** Simmetrico al precedente. Assegniamo **(-1, 5)**.
    *   **Entrambe Secondaria (S,S):** Entrambe impiegano molto tempo, ma evitano il rischio. È un esito accettabile, ma peggiore rispetto al caso in cui una delle due avesse attraversato da sola. Assegniamo **(-2, -2)**.

**Matrice dei Payoff:**

| A1 \ A2 | A (-10) | S (-1) |
| :------ | :------ | :----- |
| **A** (+5) | (-10,-10) | (5,-1) |
| **S** (-1) | (-1,5) | (-2,-2) |

**2. Equilibri di Nash (Strategie Pure):**

Identifichiamo le migliori risposte:

*   **Per A1:**
    *   Se A2 gioca `A` (Attraversa): A1 confronta (-10) per `A` e (-1) per `S`. La migliore risposta di A1 è **`S`**.
    *   Se A2 gioca `S` (Secondaria): A1 confronta (5) per `A` e (-2) per `S`. La migliore risposta di A1 è **`A`**.

*   **Per A2:** (Per simmetria, le migliori risposte di A2 sono analoghe)
    *   Se A1 gioca `A` (Attraversa): A2 confronta (-10) per `A` e (-1) per `S`. La migliore risposta di A2 è **`S`**.
    *   Se A1 gioca `S` (Secondaria): A2 confronta (5) per `A` e (-2) per `S`. La migliore risposta di A2 è **`A`**.

Identifichiamo gli equilibri di Nash:

*   **(A,A):** A1 non sta giocando la sua migliore risposta a A2 che gioca A (BR1(A) = S). Non è NE.
*   **(A,S):** A1 sta giocando la sua migliore risposta a A2 che gioca S (BR1(S) = A). A2 sta giocando la sua migliore risposta a A1 che gioca A (BR2(A) = S). **(A,S) è un Equilibrio di Nash.** Payoff (5,-1).
*   **(S,A):** A1 sta giocando la sua migliore risposta a A2 che gioca A (BR1(A) = S). A2 sta giocando la sua migliore risposta a A1 che gioca S (BR2(S) = A). **(S,A) è un Equilibrio di Nash.** Payoff (-1,5).
*   **(S,S):** A1 non sta giocando la sua migliore risposta a A2 che gioca S (BR1(S) = A). Non è NE.

**Conclusione: Ci sono due equilibri di Nash in strategie pure: (A,S) e (S,A).** Questi equilibri riflettono una situazione in cui i giocatori non riescono a coordinarsi per un esito specifico, ma preferiscono che l'altro "ceda" mentre loro ottengono il massimo vantaggio.

**3. Possibile Strategia Mista:**

Poiché ci sono due NE in strategie pure, è probabile che esista anche un NE in strategie miste.
Sia `p` la probabilità con cui A1 gioca `A`, e `1-p` la probabilità con cui A1 gioca `S`.
Sia `q` la probabilità con cui A2 gioca `A`, e `1-q` la probabilità con cui A2 gioca `S`.

**Payoff Atteso per A1 (EP1):**
*   EP1(A | q) = `(-10)*q + 5*(1-q) = -10q + 5 - 5q = 5 - 15q`
*   EP1(S | q) = `(-1)*q + (-2)*(1-q) = -q - 2 + 2q = q - 2`

Perché A1 sia indifferente tra le sue strategie pure (condizione per un NE in strategie miste), i payoff attesi devono essere uguali:
`5 - 15q = q - 2`
`7 = 16q`
**`q = 7/16`**.
Quindi A2 deve giocare `A` con probabilità `7/16` e `S` con probabilità `9/16`.

**Payoff Atteso per A2 (EP2):** (Il gioco è simmetrico)
*   EP2(A | p) = `(-10)*p + 5*(1-p) = 5 - 15p`
*   EP2(S | p) = `(-1)*p + (-2)*(1-p) = p - 2`

Perché A2 sia indifferente, i payoff attesi devono essere uguali:
`5 - 15p = p - 2`
`7 = 16p`
**`p = 7/16`**.
Quindi A1 deve giocare `A` con probabilità `7/16` e `S` con probabilità `9/16`.

**Equilibrio di Nash in Strategie Miste:**
Entrambi i giocatori scelgono di Attraversare con probabilità **7/16** e di prendere la strada Secondaria con probabilità **9/16**.
(A1: (7/16, 9/16), A2: (7/16, 9/16)).

**Discussione:**
Questo equilibrio di Nash in strategie miste suggerisce che, in assenza di coordinazione esplicita, i giocatori non si impegnano in una sola strategia. La probabilità che entrambi attraversino (`(7/16)*(7/16) = 49/256`) porta al peggior esito per entrambi. La probabilità che entrambi prendano la strada secondaria (`(9/16)*(9/16) = 81/256`) porta a un esito accettabile ma non ottimo. I due equilibri puri (A,S) e (S,A) sono preferiti a (S,S) ma richiedono che uno dei giocatori "ceda", cosa che il gioco in strategie miste non garantisce. La strategia mista riflette l'incertezza e il conflitto di interessi in questo tipo di giochi.

---

## **Problema 3 (Pagina 2): Algoritmo per l'Assegnazione di Asili Nido**

**Descrizione del Problema:**
Il Comune deve implementare un algoritmo per l'assegnazione dei bambini agli asili nido, considerando la capienza massima e due regole di welfare:
1.  Se un bambino ha già un fratello/sorella che frequenta una certa scuola, il fratello/sorella minore è assegnato alla stessa scuola.
2.  Le famiglie monoparentali hanno priorità per le scuole vicine al luogo di lavoro.
La capienza massima non può essere superata in nessun caso.

**Obiettivo:** Descrivere l'algoritmo di assegnazione.

**Approccio all'Algoritmo:**
Il problema richiede un algoritmo che rispetti vincoli di capacità e applichi regole di priorità. Un approccio greedy (avido) basato sulla priorità delle regole è appropriato. Le regole devono essere applicate in ordine decrescente di priorità.

**Assunzioni:**
*   Disponiamo di un elenco di bambini da assegnare, con informazioni su famiglia, fratelli/sorelle (e la loro scuola attuale se già assegnati), stato monoparentale, e luogo di lavoro del genitore.
*   Disponiamo di un elenco di scuole con le loro capacità massime e posizioni.
*   Possiamo calcolare la "vicinanza" di una scuola a un luogo di lavoro (es. distanza geografica, tempo di viaggio).

**Strutture Dati:**
*   `Bambini`: Lista di oggetti bambino, ciascuno con `ID`, `ID_Famiglia`, `ID_Scuola_Fratello` (se applicabile, inizialmente `null`), `Monoparentale` (booleano), `Posizione_Lavoro_Genitore`, `Assegnato` (booleano, inizialmente `false`).
*   `Scuole`: Dizionario o lista di oggetti scuola, ciascuno con `ID_Scuola`, `Capacita_Massima`, `Posizione`.
*   `Capacita_Corrente_Scuole`: Dizionario che mappa `ID_Scuola` alla `Capacita_Massima` rimanente, inizializzato con le capacità massime.
*   `Assegnazioni`: Lista vuota per registrare le assegnazioni `(ID_Bambino, ID_Scuola)`.

**Algoritmo di Assegnazione (Prioritario):**

1.  **Fase di Preparazione:**
    *   Inizializza `Capacita_Corrente_Scuole` con le capacità massime di tutte le scuole.
    *   Crea una lista `Bambini_Non_Assegnati` che è una copia modificabile della lista iniziale `Bambini`.
    *   **Pre-elaborazione fratelli:** Se non già fatto, per ogni bambino, identifica se ha un fratello già assegnato a una scuola specifica e imposta `ID_Scuola_Fratello`. Questo potrebbe richiedere un ordinamento per `ID_Famiglia`.

2.  **Fase 1: Applicazione della Regola 1 (Priorità Fratello/Sorella):**
    *   Itera su tutti i bambini nella lista `Bambini_Non_Assegnati`.
    *   **Per ogni bambino `b`:**
        *   Se `b.ID_Scuola_Fratello` non è `null`:
            *   Sia `scuola_fratello = b.ID_Scuola_Fratello`.
            *   **Verifica capacità:** Se `Capacita_Corrente_Scuole[scuola_fratello] > 0`:
                *   Assegna `b` a `scuola_fratello`.
                *   Decrementa `Capacita_Corrente_Scuole[scuola_fratello]` di 1.
                *   Aggiungi `(b.ID, scuola_fratello)` a `Assegnazioni`.
                *   Marca `b.Assegnato = true`.
            *   Altrimenti (la scuola del fratello è piena):
                *   Il bambino non può essere assegnato a quella scuola. Rimane in `Bambini_Non_Assegnati` per essere considerato nelle fasi successive senza questa priorità specifica (poiché la capienza non può essere superata).

3.  **Fase 2: Applicazione della Regola 2 (Priorità Famiglie Monoparentali):**
    *   Crea una lista temporanea dei bambini ancora non assegnati: `temp_non_assegnati = [b for b in Bambini_Non_Assegnati if not b.Assegnato]`.
    *   Itera su `temp_non_assegnati`.
    *   **Per ogni bambino `b`:**
        *   Se `b.Monoparentale` è `true`:
            *   Trova la scuola disponibile (`Capacita_Corrente_Scuole[scuola] > 0`) che è "più vicina" a `b.Posizione_Lavoro_Genitore`.
            *   Se una tale scuola viene trovata:
                *   Assegna `b` a questa scuola.
                *   Decrementa `Capacita_Corrente_Scuole[scuola]` di 1.
                *   Aggiungi `(b.ID, scuola)` a `Assegnazioni`.
                *   Marca `b.Assegnato = true`.
            *   Altrimenti (nessuna scuola vicina e disponibile):
                *   Il bambino rimane in `Bambini_Non_Assegnati`.

4.  **Fase 3: Assegnazione Generale (Bambini Rimanenti):**
    *   Crea una lista temporanea dei bambini ancora non assegnati: `temp_non_assegnati = [b for b in Bambini_Non_Assegnati if not b.Assegnato]`.
    *   Itera su `temp_non_assegnati`.
    *   **Per ogni bambino `b`:**
        *   Trova una qualsiasi scuola disponibile (`Capacita_Corrente_Scuole[scuola] > 0`). L'ordine potrebbe essere casuale, la prima disponibile, o quella più vicina al domicilio del bambino (se l'informazione è disponibile e non in conflitto con altre regole implicite).
        *   Se una scuola disponibile viene trovata:
            *   Assegna `b` a questa scuola.
            *   Decrementa `Capacita_Corrente_Scuole[scuola]` di 1.
            *   Aggiungi `(b.ID, scuola)` a `Assegnazioni`.
            *   Marca `b.Assegnato = true`.
        *   Altrimenti (nessuna scuola disponibile):
            *   Il bambino non può essere assegnato e resterà nella lista dei non assegnati.

**Output:**
*   La lista `Assegnazioni` contenente le assegnazioni effettuate.
*   La lista dei bambini che non sono stati assegnati (se ce ne sono, ad esempio per mancanza di posti).

**Considerazioni Aggiuntive:**
*   **Gestione della "vicinanza":** Sarà necessaria una funzione per calcolare la distanza o il costo di trasporto tra la posizione del luogo di lavoro e le scuole.
*   **Ottimizzazione:** Questo è un algoritmo greedy. Non garantisce di massimizzare il numero totale di bambini assegnati o di ottimizzare qualche altra metrica (es. minimizzare la distanza media) al di fuori delle priorità esplicite.
*   **Ambiguità sulla Regola 1:** La frase "granted the same school" (assegnato alla stessa scuola) in caso di fratello/sorella implica una forte priorità. Tuttavia, la successiva frase "maximum capacity limit cannot be exceeded under any circumstances" (la capienza massima non può essere superata in nessun caso) crea un conflitto. La soluzione sopra assume che la capienza sia un vincolo rigido che *non può* essere violato, anche per la regola 1. Se la regola 1 dovesse sovrascrivere la capienza, l'algoritmo dovrebbe modificare le capacità o spostare altri bambini. Data l'istruzione "cannot be exceeded under any circumstances", l'interpretazione del rispetto rigoroso della capienza è la più logica.

---

## **Problema 1 (Pagina 3): Cuckoo Hashing e Eliminazione**

**Descrizione del Problema:**
Considerare l'operazione di eliminazione in Cuckoo Hashing.
1.  Costruire un esempio in cui l'eliminazione non produce un grafo fattibile, il che significa che non esiste una sequenza di sola inserzione che possa portare a quel grafo. Scegliere `S` (suggerimento: `|S|=3`); inserire le chiavi di `S` nella tabella di Cuckoo Hash; scegliere `x` in `S` ed eliminarlo; mostrare che l'inserimento da zero di `S-{x}` in una tabella vuota di Cuckoo Hash non produce lo stesso risultato dei passaggi precedenti.
2.  Mostrare come risolvere questo problema scegliendo casualmente tra `h_1` e `h_2` durante l'inserimento.

**Contesto di Cuckoo Hashing:**
Cuckoo Hashing utilizza due funzioni hash, `h1` e `h2`. Ogni chiave `k` può essere memorizzata in `T[h1(k)]` o `T[h2(k)]`. L'inserimento di una chiave `k` verifica prima `T[h1(k)]`. Se è libero, `k` viene inserito lì. Se `T[h1(k)]` è occupato, `k` prova `T[h2(k)]`. Se è libero, `k` viene inserito lì. Se entrambi sono occupati, `k` sposta la chiave esistente in una delle due posizioni (di solito `T[h1(k)]`), e la chiave spostata `y` diventa la nuova chiave "senza casa" che deve essere inserita. Questo processo continua formando una catena di spostamenti. Se si verifica un ciclo o la catella diventa troppo lunga, si esegue una ri-hash completa [7, 8].

**1. Esempio di Eliminazione che non produce un Grafo Fattibile (Stato Inaspettato):**

Il problema si basa sull'idea che la *configurazione* specifica delle chiavi nelle posizioni della tabella in Cuckoo Hashing dipende dalla *storia* delle inserzioni. Una eliminazione può lasciare la tabella in uno stato che non sarebbe raggiungibile con una sequenza di sole inserzioni delle chiavi rimanenti, se l'algoritmo di inserimento segue una strategia deterministica (es. prova sempre `h1` prima di `h2`).

*   **Setup:**
    *   Dimensione della tabella `m = 4`.
    *   Funzioni hash:
        *   `h1(k) = k mod 4`
        *   `h2(k) = (k / 4) mod 4` (assumendo `k` è un intero)
        *   Scegliamo chiavi che creino conflitti. Useremo valori arbitrari per chiarezza, non necessariamente un hash semplice.
    *   Chiavi `S = {x1, x2, x3}`.
        *   `x1`: `h1(x1) = 0`, `h2(x1) = 2`
        *   `x2`: `h1(x2) = 1`, `h2(x2) = 3`
        *   `x3`: `h1(x3) = 0`, `h2(x3) = 1` (Questo è il "cuore" del conflitto. `x3` può andare in 0 o 1).

*   **Algoritmo di Inserimento Deterministico (Strategia: Prova sempre `h1(k)` prima di `h2(k)`):**
    1.  **Tabella iniziale:** `[ -, -, -, - ]` (tutte le posizioni vuote)
    2.  **Inserisci `x1`:**
        *   `h1(x1) = 0` è libero. Inserisci `x1` in `T`.
        *   Tabella: `[x1, -, -, -]`
    3.  **Inserisci `x2`:**
        *   `h1(x2) = 1` è libero. Inserisci `x2` in `T[9]`.
        *   Tabella: `[x1, x2, -, -]`
    4.  **Inserisci `x3`:**
        *   `h1(x3) = 0` è occupato da `x1`.
        *   `h2(x3) = 1` è occupato da `x2`.
        *   `x3` prova `h1(x3)=0`, quindi **sposta `x1`**. `x3` va in `T`. `x1` diventa senza casa.
        *   Tabella: `[x3, x2, -, -]` (e `x1` è "homeless")
        *   Ora inserisci `x1` (precedentemente spostato):
            *   `h1(x1) = 0` è occupato da `x3`.
            *   `h2(x1) = 2` è libero. Inserisci `x1` in `T[10]`.
        *   Tabella finale dopo le inserzioni: `[x3, x2, x1, -]` (dove `T=x3`, `T[9]=x2`, `T[10]=x1`).

*   **Operazione di Eliminazione:**
    *   **Eliminiamo `x2`** (che si trova in `T[9]`).
    *   Tabella dopo eliminazione: `[x3, -, x1, -]` (dove `T=x3`, `T[9]=empty`, `T[10]=x1`).
    *   Questo è lo stato che vogliamo verificare.

*   **Inserisci `S' = {x1, x3}` da zero in una tabella vuota (con la stessa strategia deterministica):**
    1.  **Tabella iniziale:** `[ -, -, -, - ]`
    2.  **Inserisci `x1`:**
        *   `h1(x1) = 0` è libero. Inserisci `x1` in `T`.
        *   Tabella: `[x1, -, -, -]`
    3.  **Inserisci `x3`:**
        *   `h1(x3) = 0` è occupato da `x1`.
        *   `h2(x3) = 1` è libero. Inserisci `x3` in `T[9]`.
        *   Tabella finale: `[x1, x3, -, -]` (dove `T=x1`, `T[9]=x3`).

*   **Confronto dei Risultati:**
    *   Stato dopo eliminazione: `[x3, -, x1, -]`
    *   Stato dopo reinserimento da zero: `[x1, x3, -, -]`
    *   **I due stati della tabella sono diversi.**
    *   Questo dimostra che l'eliminazione ha lasciato la tabella in uno stato che non sarebbe stato prodotto da una semplice inserzione delle chiavi rimanenti, seguendo la stessa strategia deterministica. Ciò accade perché `x1` era stato "forzato" nella sua posizione `h2(x1)=2` durante l'inserimento iniziale (a causa del conflitto con `x3` in `h1(x1)=0`), ma dopo l'eliminazione di `x2`, la posizione `h2(x3)=1` di `x3` è diventata la sua scelta deterministica per l'inserimento da zero.

**2. Come Risolvere il Problema Scegliendo Casualmente tra `h1` e `h2` durante l'Inserimento:**

Il problema deriva dalla rigidità della strategia di inserimento. Se si introduce casualità, la dipendenza dalla storia specifica si attenua.

*   **Strategia di Inserimento Migliorata (con Randomizzazione):**
    Quando si inserisce una chiave `k`:
    1.  **Se `T[h1(k)]` è libero E `T[h2(k)]` è libero:**
        *   Scegli **casualmente** tra `h1(k)` e `h2(k)` per posizionare `k`. [11]
    2.  **Se solo una delle due posizioni è libera:**
        *   Inserisci `k` nella posizione libera (nessuna casualità necessaria qui).
    3.  **Se entrambe le posizioni sono occupate:**
        *   Scegli **casualmente** una delle due posizioni (`h1(k)` o `h2(k)`) da cui spostare la chiave esistente. La chiave spostata diventa la nuova "senza casa".

*   **Spiegazione della Soluzione:**
    Introducendo la casualità nella scelta della posizione quando entrambe le posizioni sono disponibili, o nella scelta della chiave da spostare, si rende meno probabile che una chiave venga "forzata" in una delle sue posizioni in modo tale che, dopo un'eliminazione, quello stato non sia più raggiungibile da un'inserzione da zero.
    Questa casualità rende la configurazione finale della tabella meno dipendente dall'ordine specifico delle inserzioni e dalle decisioni deterministiche prese in precedenza. Invece di avere una singola "storia" che porta a una configurazione specifica, si hanno molteplici storie possibili, e la tabella tende a raggiungere stati che sono più "genericamente" fattibili per il set di chiavi attuale.
    Questo si allinea con l'idea di Cuckoo Hashing di sfruttare la casualità delle funzioni hash e delle posizioni per garantire prestazioni attese migliori (es. `O(1)` tempo atteso per lookup e insert) [7, 8].

---

## **Problema 1 (Pagina 4): Algoritmo di Min-Cut Randomizzato**

**Descrizione del Problema:**
Abbiamo visto che l'algoritmo di min-cut randomizzato (tipo Karger) ha una probabilità di successo di almeno `2/n`, dove `n` è il numero di vertici.
1.  Descrivere come implementare l'algoritmo quando il grafo è rappresentato tramite liste di adiacenza e analizzarne il tempo di esecuzione. In particolare, un passo di contrazione può essere fatto in `O(n)` tempo.
2.  Un grafo pesato ha un peso `w(e)` su ogni arco `e`. Il min-cut in questo caso è inteso come il taglio pesato minimo, dove la somma dei pesi degli archi nel taglio è minima. Descrivere come estendere l'algoritmo ai grafi pesati e mostrare che la probabilità di successo è ancora `>= 2/n`.

**Contesto Min-Cut (Karger's Algorithm):**
L'algoritmo di Karger per il min-cut funziona contraendo ripetutamente archi scelti casualmente fino a quando rimangono solo due supernodi. Il taglio minimo è dato dagli archi rimanenti tra questi due supernodi. La probabilità di successo per una singola esecuzione è `2/(n*(n-1))` (o circa `2/n^2`) [12, 13]. Per garantire alta probabilità di trovare il min-cut, l'algoritmo viene eseguito `O(n^2 * log n)` volte e si prende il taglio più piccolo trovato.

**1. Implementazione e Analisi del Tempo per Liste di Adiacenza (Grafo Non Pesato):**

**Rappresentazione del Grafo:**
Utilizziamo liste di adiacenza: `Adj[u]` è una lista di vertici `v` adiacenti a `u`. Per gestire i multi-archi (bordi paralleli tra due vertici), `v` può apparire più volte nella lista `Adj[u]`.
Una struttura alternativa che è più efficiente per le contrazioni:
*   `Adj[u]`: Una lista di coppie `(v, count)` dove `count` è la molteplicità dell'arco `(u,v)`.
*   Un elenco globale di tutti gli archi `EdgeList = [(u1,v1), (u2,v2), ...]`.

**Algoritmo `GuessMinCut(G)`:**

1.  **Fase di Inizializzazione:**
    *   Mantieni `n_current = |V|`.
    *   Mantieni una mappa `NodeMap`: `vecchio_id_nodo -> attuale_super_id_nodo`. Inizialmente `NodeMap[v] = v` per ogni `v \in V`.
    *   Costruisci `EdgeList`: una lista contenente tutte le `M` coppie `(u,v)` che rappresentano gli archi del grafo. Questa lista permette una selezione casuale in `O(1)` dopo la costruzione. Costo: `O(N+M)`.

2.  **Ciclo di Contrazione:**
    *   **`while n_current > 2:`**
        a.  **Scegli un arco casuale `(u, v)` da `EdgeList`:**
            *   Scegli un indice `idx` casuale tra `0` e `|EdgeList|-1`.
            *   Sia `(u_original, v_original) = EdgeList[idx]`.
            *   Trova i "supernodi" attuali a cui appartengono `u_original` e `v_original`: `u_super = NodeMap[u_original]`, `v_super = NodeMap[v_original]`.
            *   Assicurati che `u_super != v_super` (non stiamo scegliendo un arco auto-loop). Se lo è, riprova (sebbene con la strategia di rimozione degli auto-loop, questo dovrebbe essere raro o nullo).
            *   Costo: `O(1)` per selezione dell'indice, `O(1)` per lookup in `NodeMap`.

        b.  **Contrai l'arco `(u_super, v_super)`:** (Assumiamo di unire `v_super` in `u_super`).
            *   **Aggiornamento `NodeMap`:** Per ogni nodo `x` che era mappato a `v_super`, ora mappa `x` a `u_super`. Questo è il passo più costoso se fatto con una scansione completa di `NodeMap` o di tutti i nodi originali. Tuttavia, l'istruzione dice che un passo di contrazione può essere fatto in `O(N)` tempo.
                *   Per fare questo in `O(N)`: è necessario mantenere una lista di nodi "originali" per ogni supernodo. Quando `v_super` viene unito in `u_super`, la lista dei nodi originali di `v_super` viene appesa a quella di `u_super`. Successivamente, tutti gli archi che avevano un endpoint in `v_super` devono essere aggiornati per puntare a `u_super`.
                *   Una implementazione efficiente userebbe puntatori per unire liste di adiacenza (es. `Adj[v_super]` in `Adj[u_super]`), e poi itererebbe su tutti i nodi originali e aggiornerebbe i loro puntatori al supernodo (se `O(N)`).
            *   **Rimozione Auto-loop:** Se un arco `(u_super, v_super)` diventa un auto-loop (`u_super` e `v_super` sono lo stesso dopo la contrazione di un altro arco), deve essere rimosso da `EdgeList`. Questo può essere fatto mantenendo un set di archi "validi" o marcando gli archi come "invalido".
            *   `n_current = n_current - 1`.
            *   Costo: Come da istruzione, `O(N)`.

3.  **Fase Finale:**
    *   Quando `n_current == 2`, `EdgeList` conterrà solo gli archi tra i due supernodi finali.
    *   **Restituisci la dimensione del taglio:** Conta gli archi rimanenti in `EdgeList` (quelli che non sono stati eliminati o auto-loop).
    *   Costo: `O(M)` (o `O(1)` se si mantiene un contatore).

**Analisi del Tempo di Esecuzione:**
*   **Precomputazione:** `O(N+M)`.
*   **Ciclo di Contrazione:** Il ciclo si esegue `N-2` volte.
*   **Costo per iterazione:** `O(N)` per la contrazione dell'arco e l'aggiornamento dei riferimenti. La selezione dell'arco è `O(1)` se `EdgeList` è mantenuta in modo che gli archi auto-loop siano rimossi efficientemente (es. con un array dinamico o una lista linkata che permette rimozione `O(1)` una volta trovato l'elemento).
*   **Tempo Totale per una singola esecuzione:** `O(N * N) = O(N^2)`.
*   Per ottenere un'alta probabilità di successo, l'algoritmo viene ripetuto `O(N^2 * log N)` volte [12].
*   **Tempo Totale per l'esecuzione completa (con alta probabilità):** `O(N^2 * (N^2 * log N)) = O(N^4 * log N)`.

**2. Estensione ai Grafi Pesati e Probabilità di Successo:**

**Definizione del Min-Cut Pesato:**
In un grafo pesato `G=(V,E,w)`, dove `w(e)` è il peso dell'arco `e`, un taglio `(S, V\S)` ha un costo pari alla somma dei pesi di tutti gli archi che lo attraversano. L'obiettivo è trovare un taglio con il costo minimo.

**Adattamento dell'Algoritmo:**

1.  **Rappresentazione del Grafo:**
    *   Liste di adiacenza: `Adj[u]` conterrà coppie `(v, w_uv)` dove `w_uv` è il peso dell'arco `(u,v)`. Se ci sono multi-archi, i loro pesi si sommano implicitamente per formare un unico arco "logico" con peso combinato.
    *   `EdgeList`: dovrebbe contenere gli archi, e la selezione dovrebbe tenere conto dei pesi.

2.  **Scelta di un Arco Casuale Pesato:**
    *   Invece di scegliere un arco uniformemente a caso, si sceglie un arco `e=(u,v)` con una probabilità **proporzionale al suo peso `w(e)`**.
    *   **Implementazione:**
        *   Calcolare `W_total = Sum_{e in E} w(e)` (somma totale dei pesi di tutti gli archi).
        *   Generare un numero casuale `r` uniformemente tra `0` e `W_total`.
        *   Scorrere gli archi (es. da `EdgeList`) sommando i pesi cumulativamente, finché la somma cumulativa supera `r`. L'arco raggiunto è quello selezionato.
        *   Costo: `O(M)` (o `O(N)` se `EdgeList` è organizzata in modo intelligente per l'accesso pesato).

3.  **Contrazione di Archi Pesati:**
    *   Quando si contrae `(u,v)` in un nuovo supernodo `uv`:
        *   Per ogni vicino `x` di `u` o `v`:
            *   Se `x` era collegato a `u` con peso `w_ux` e a `v` con peso `w_vx`, il nuovo arco `(uv,x)` avrà peso `w_ux + w_vx`.
            *   Gli auto-loop (archi tra `u` e `v` stessi che si uniscono) sono rimossi e i loro pesi vengono scartati dal calcolo del taglio.
    *   Il costo di contrazione rimane `O(N)` se implementato in modo efficiente per grafi pesati.

**Probabilità di Successo `P(n) >= 2/n` (o `2/(n(n-1))`)**

L'argomento chiave per la probabilità di successo dell'algoritmo di Karger si estende ai grafi pesati.

*   Sia `K` il peso del min-cut (la somma dei pesi degli archi nel taglio minimo).
*   Considera un qualsiasi vertice `v` nel grafo. Il peso totale degli archi incidenti a `v` (il suo grado pesato, `deg(v)`) deve essere **almeno `K`**.
    *   Motivo: se `deg(v) < K`, un taglio che separa `v` dal resto del grafo avrebbe un costo `deg(v) < K`, il che contraddirebbe la definizione di `K` come min-cut. [14, 15]
*   La somma dei gradi pesati di tutti i vertici è `Sum_{v in V} deg(v) = 2 * W_total` (dove `W_total` è la somma totale dei pesi di tutti gli archi nel grafo).
*   Poiché `deg(v) >= K` per ogni `v`, allora `2 * W_total = Sum_{v in V} deg(v) >= N * K`.
*   Quindi, `W_total >= (N * K) / 2`.
*   Ora, consideriamo la probabilità di scegliere un arco che **appartiene al min-cut** `C_min`. Ci sono archi con peso totale `K` in `C_min`.
*   La probabilità di selezionare un arco dal min-cut `C_min` in un singolo passo è `(Peso totale di C_min) / (Peso totale di tutti gli archi) = K / W_total`.
*   Sostituendo il limite inferiore per `W_total`: `K / W_total <= K / ((N * K) / 2) = 2 / N`.
*   Pertanto, la probabilità di selezionare un arco che *non* appartiene al min-cut `C_min` è `1 - (K / W_total) >= 1 - 2 / N`.
*   Questa è la probabilità che il min-cut venga preservato in un singolo passo. Per `n-2` passi, la probabilità che il min-cut venga preservato in tutti i passi (e quindi trovato dall'algoritmo) è il prodotto di queste probabilità:
    `P(n) = Prod_{i=3 to n} (1 - 2/i) = 2 / (n * (n-1))`. [12]
*   **Conclusione:** La probabilità di successo dell'algoritmo di min-cut randomizzato di Karger si mantiene **`>= 2 / (n * (n-1))`** (che è circa `2/n^2` per grandi `n`) anche per i grafi pesati, grazie alla selezione degli archi proporzionale al loro peso.

---

## **Problema 1 (Pagina 5): Count-Min Sketch con Incrementi e Decrementi**

**Descrizione del Problema:**
Considerare il Count-Min Sketch (CMS) in cui sono consentiti sia incrementi che decrementi. Abbiamo visto che per gli incrementi-soli, la garanzia è `F[i] <= F_tilde[i] <= F[i] + epsilon ||F||_1` con probabilità `1-delta`. Con decrementi, la garanzia è `|F[i] - F_tilde[i]| <= 2 * epsilon * ||F||_1`.

1.  Considerare l'alternativa in cui il CMS con soli incrementi è utilizzato su due contatori per elemento `i`: `F+[i]` (incrementi) e `F-[i]` (decrementi). Il conteggio reale è `F[i] = F+[i] - F-[i]`.
2.  Definire un contatore approssimato come `F_tilde[i] = F_tilde+[i] - F_tilde-[i]` e mostrare che non può garantire la condizione `|F[i] - F_tilde[i]| <= epsilon ||F||_1`.
3.  Indicare alcune condizioni sul numero di incrementi e decrementi affinché la condizione `|F[i] - F_tilde[i]| <= epsilon ||F||_1` sia soddisfatta (con una costante moltiplicativa).

**Contesto CMS:**
Il Count-Min Sketch è una struttura dati probabilistica per stimare le frequenze degli elementi in un flusso dati, garantendo una stima superiore (per soli incrementi) o un errore limitato (per incrementi/decrementi usando la mediana) [16-19].

**1. Alternativa CMS con `F+[i]` e `F-[i]`:**

*   **Conteggio Reale:** Per un elemento `i`, la sua frequenza netta reale è `F[i] = F+[i] - F-[i]`, dove `F+[i]` è il numero totale di incrementi per `i` e `F-[i]` è il numero totale di decrementi per `i`.
*   **Implementazione dell'Approximator:**
    *   Si usano **due tabelle CMS separate**:
        *   `T_plus`: Per gli incrementi. Quando un elemento `i` viene incrementato, si aggiorna `T_plus`.
        *   `T_minus`: Per i decrementi. Quando un elemento `i` viene decrementato, si aggiorna `T_minus` (trattando i decrementi come incrementi di valori assoluti).
    *   Le tabelle `T_plus` e `T_minus` usano le stesse funzioni hash (`h_j`) e dimensioni (`r x c`).
    *   **Stima Approssimata:**
        *   `F_tilde+[i] = min_{j} (T_plus[j][h_j(i)])` (stima degli incrementi totali per `i`).
        *   `F_tilde-[i] = min_{j} (T_minus[j][h_j(i)])` (stima dei decrementi totali per `i`).
    *   **Contatore Approssimato:** `F_tilde[i] = F_tilde+[i] - F_tilde-[i]`.

**2. Mostrare che non può garantire `|F[i] - F_tilde[i]| <= epsilon ||F||_1`:**

Per le tabelle `T_plus` e `T_minus` (che gestiscono solo incrementi), valgono le seguenti garanzie con probabilità `1-delta` [18]:
*   `F+[i] <= F_tilde+[i] <= F+[i] + epsilon ||F+||_1`
*   `F-[i] <= F_tilde-[i] <= F-[i] + epsilon ||F-||_1`

Dove `||F+||_1 = Sum_k F+[k]` è il numero totale di incrementi nel flusso (la somma dei valori in `T_plus`), e `||F-||_1 = Sum_k F-[k]` è il numero totale di decrementi nel flusso (la somma dei valori in `T_minus`).

Ora, sostituiamo queste disuguaglianze in `F_tilde[i] = F_tilde+[i] - F_tilde-[i]`:

*   **Limite Inferiore per `F_tilde[i]`:**
    `F_tilde[i] >= F+[i] - (F-[i] + epsilon ||F-||_1)`
    `F_tilde[i] >= (F+[i] - F-[i]) - epsilon ||F-||_1`
    `F_tilde[i] >= F[i] - epsilon ||F-||_1`

*   **Limite Superiore per `F_tilde[i]`:**
    `F_tilde[i] <= (F+[i] + epsilon ||F+||_1) - F-[i]`
    `F_tilde[i] <= (F+[i] - F-[i]) + epsilon ||F+||_1`
    `F_tilde[i] <= F[i] + epsilon ||F+||_1`

Combinando i due limiti:
`F[i] - epsilon ||F-||_1 <= F_tilde[i] <= F[i] + epsilon ||F+||_1`

Questa disuguaglianza implica che l'errore assoluto è limitato da:
`|F[i] - F_tilde[i]| <= epsilon * max(||F+||_1, ||F-||_1)`

**Perché questa non garantisce `|F[i] - F_tilde[i]| <= epsilon ||F||_1`:**

La garanzia desiderata `|F[i] - F_tilde[i]| <= epsilon ||F||_1` (dove `||F||_1 = Sum_k F[k]` è la somma delle frequenze *nette correnti*) non è soddisfatta perché `max(||F+||_1, ||F-||_1)` può essere **significativamente più grande** di `||F||_1`.

**Esempio:**
Supponiamo un elemento `i` venga incrementato 1000 volte e poi decrementato 999 volte.
*   `F+[i] = 1000`, `F-[i] = 999`.
*   La frequenza netta reale è `F[i] = 1000 - 999 = 1`.
*   Supponiamo che il flusso contenga solo questo elemento per semplicità. Allora `||F+||_1 = 1000`, `||F-||_1 = 999`. La somma delle frequenze *nette correnti* `||F||_1 = 1`.

Con la nostra stima `F_tilde[i] = F_tilde+[i] - F_tilde-[i]`, l'errore è limitato da:
`|F[i] - F_tilde[i]| <= epsilon * max(1000, 999) = 1000 * epsilon`.

Ma la garanzia desiderata richiederebbe un errore limitato da:
`epsilon * ||F||_1 = epsilon * 1 = epsilon`.

Chiaramente, `1000 * epsilon` è molto più grande di `epsilon`. Pertanto, questa costruzione **non fornisce la garanzia desiderata** quando ci sono molte oscillazioni (molti incrementi e decrementi che si annullano a vicenda) che rendono `||F+||_1` o `||F-||_1` molto più grandi di `||F||_1`.

**3. Condizioni affinché la condizione sia soddisfatta:**

Affinché la garanzia `|F[i] - F_tilde[i]| <= C * epsilon * ||F||_1` (con una costante `C` adeguata, idealmente `C=1`) sia soddisfatta con questa costruzione, la quantità `max(||F+||_1, ||F-||_1)` deve essere dello stesso ordine di grandezza di `||F||_1`.

Questo avviene se il flusso dati non ha molte oscillazioni che si annullano.
**Condizioni necessarie:**
*   Il numero totale di incrementi (`||F+||_1`) non deve essere significativamente maggiore della somma delle frequenze nette correnti (`||F||_1`).
*   Il numero totale di decrementi (`||F-||_1`) non deve essere significativamente maggiore della somma delle frequenze nette correnti (`||F||_1`).

In altre parole, il flusso dati deve essere tale che `||F+||_1 ≈ ||F||_1` e `||F-||_1 ≈ ||F||_1`. Questo è vero solo se il numero di operazioni di incremento e decremento non è molto più grande del numero di elementi attualmente presenti nel sistema. Se, ad esempio, un elemento viene aggiunto e rimosso molte volte, ma la sua frequenza netta rimane bassa, questa condizione non sarà soddisfatta.
In pratica, questa costruzione semplice funziona bene solo quando il flusso è dominato dagli incrementi o quando le frequenze non subiscono annullamenti significativi. Per un controllo più robusto dell'errore con incrementi e decrementi, il CMS con mediana (come descritto nelle fonti [19]) è il metodo preferito.

---

## **Problema 1 (Pagina 6): Prova di Fallimento di 2-Sweep su Grafi Specifici**

**Descrizione del Problema:**
Dimostrare che l'algoritmo 2-Sweep, che si comporta abbastanza bene in pratica, fornisce un valore arbitrariamente inferiore rispetto al diametro `D` del grafo fornito nell'immagine.

**Algoritmo 2-Sweep:**
1.  Scegli un nodo `r` casuale nel grafo.
2.  Calcola `a`, il nodo più lontano da `r` (tramite BFS).
3.  Calcola `b`, il nodo più lontano da `a` (tramite BFS).
4.  Restituisci `d(a,b)` (la distanza tra `a` e `b`).
L'algoritmo restituisce una stima del diametro, ma non è garantito che sia il diametro effettivo. Per grafi generici, può essere arbitrariamente lontano dal valore reale [20, 21].

**Analisi del Grafo Specifico nell'Immagine (Pagina 6 dell'Assignment):**

Il grafo è una griglia quadrata di dimensioni `M x K` (diciamo `M=4` righe, `K` colonne) dove ogni nodo `(i,j)` è collegato a `(i+1,j)` e `(i,j+1)`. Inoltre, ci sono due nodi esterni, chiamiamoli `T` (Top) e `B` (Bottom).
*   `T` è collegato a tutti i nodi della prima riga (`(1,j)` per `j=1...K`).
*   `B` è collegato a tutti i nodi dell'ultima riga (`(M,j)` per `j=1...K`).

**Calcolo del Diametro Reale (`D`):**

Il diametro `D` di un grafo è la distanza massima tra qualsiasi coppia di nodi.
Consideriamo le distanze in questo grafo:
1.  **Distanza tra `T` e `B`:** `T` può raggiungere qualsiasi nodo `(1,j)` in 1 passo. `(1,j)` può raggiungere `(M,j)` in `M-1` passi (attraversando le righe). `(M,j)` può raggiungere `B` in 1 passo. Quindi, `d(T,B) = 1 + (M-1) + 1 = M+1`. Per `M=4`, `d(T,B) = 5`.
2.  **Distanza tra due nodi qualsiasi `(i1,j1)` e `(i2,j2)` all'interno della griglia:** Il percorso più breve è `|i1-i2| + |j1-j2|`. La distanza massima interna alla griglia sarebbe tra `(1,1)` e `(M,K)` (se `M` e `K` sono grandi), ovvero `(M-1) + (K-1)`.
3.  **Distanza tra un nodo esterno (`T` o `B`) e un nodo interno della griglia:** Per esempio, `d(T, (i,j)) = 1 + (i-1)` (via un nodo della prima riga). Max `d(T, (M,K)) = 1 + (M-1) + (K-1)`.
4.  **Confronto:**
    *   Se `K` (numero di colonne) è piccolo (es. `K=1`), il diametro sarebbe `M+1` (cioè `5`).
    *   Se `K` è grande (es. `K=100`), la distanza massima tra due nodi agli angoli opposti della griglia, ad esempio `(1,1)` e `(4,K)`, sarebbe `(4-1) + (K-1) = 3 + K - 1 = K+2`.
    *   La distanza `d(T,B)` è sempre `M+1 = 5`.
    *   Il diametro `D` sarà il massimo tra queste distanze. Se `K` è grande, allora `D = K+2`.
    *   Per esempio, se `M=4` e `K=100`, `D = 102`.

**Analisi del Fallimento dell'Algoritmo 2-Sweep:**

L'algoritmo 2-Sweep fallisce quando il primo passo (`a = farthest node from r`) non identifica un nodo che è effettivamente un "punto estremo" del diametro globale del grafo.

Consideriamo di scegliere un nodo `r` specifico per dimostrare il fallimento:
*   Scegliamo `r` come un nodo nella **metà della griglia**, diciamo `r = (2, K/2)` (un nodo intermedio in una riga intermedia).

1.  **Trova `a` (il nodo più lontano da `r`):**
    *   Da `r = (2, K/2)`, la distanza massima a un altro nodo della griglia è tra `(2, K/2)` e `(1,1)` o `(1,K)` o `(M,1)` o `(M,K)`. La distanza a `(1,1)` è `(2-1) + (K/2 - 1) = K/2`.
    *   Ma dobbiamo considerare anche `T` e `B`.
    *   `d(r, T) = d((2, K/2), T)`: `T` è collegato a tutta la riga 1. Quindi `d(T, (1, K/2)) = 1`. `d((2, K/2), (1, K/2)) = 1`. Quindi `d(r, T) = 1 + 1 = 2`.
    *   `d(r, B) = d((2, K/2), B)`: `B` è collegato a tutta la riga `M=4`. `d(B, (4, K/2)) = 1`. `d((2, K/2), (4, K/2)) = 2`. Quindi `d(r, B) = 1 + 2 = 3`.
    *   In questo caso, il nodo `a` più lontano da `r=(2, K/2)` è `B`. La distanza `d(r,a) = 3`.

2.  **Trova `b` (il nodo più lontano da `a=B`):**
    *   `a` è il nodo `B` (quello più in basso).
    *   Il nodo più lontano da `B` in questo grafo è `T` (quello più in alto).
    *   `d(B, T) = 5`.
    *   Quindi l'algoritmo restituisce **`d(a,b) = 5`**.

**Confronto e Conclusione:**

*   **Diametro Reale `D`:** Se `K` è grande (es. `K=100`), il diametro `D = K+2 = 102`.
*   **Valore restituito dall'algoritmo 2-Sweep:** `5`.

Il valore restituito dall'algoritmo 2-Sweep (`5`) è **arbitrariamente inferiore** rispetto al diametro reale (`102` nell'esempio), e questa differenza cresce all'aumentare di `K`. Questo dimostra il fallimento dell'algoritmo 2-Sweep nel fornire una buona approssimazione del diametro per questo tipo di grafo specifico. L'algoritmo si "inganna" scegliendo un nodo intermedio (`r`), che porta a identificare come `a` un nodo "verticalmente" lontano (`B`), ma poi `B` stesso ha come nodo più lontano solo `T`, non catturando la grande distanza orizzontale della griglia.

---

## **Problema 2 (Pagina 6): Campionamento Kpnasack**

**Descrizione del Problema:**
1.  Utilizzare lo schema di programmazione dinamica DP1 visto in classe per contare le soluzioni `FATTIBILI` nel problema dello zaino (solo pesi, senza valori).
2.  Mostrare come campionare una di queste soluzioni `uniformemente` a caso.
3.  Scrivere lo pseudocodice e analizzare il costo temporale.
4.  **[OPZIONALE]** Usando una variazione dello schema DP1, è possibile campionare una delle soluzioni `OTTIMALI` (fattibile e con valore ottimale) uniformemente a caso?

**Contesto Knapsack (0-1, solo pesi):**
Dati `n` elementi, ciascuno con un peso `w_i`, e una capacità massima `W`. Si vuole selezionare un sottoinsieme di elementi la cui somma dei pesi non superi `W`.

**1. DP1 per Contare le Soluzioni Fattibili:**

Sia `Count[i][w]` il numero di sottoinsiemi di elementi presi dai primi `i` elementi che hanno un peso totale **esattamente** `w`.

*   **Stato della DP:** `Count[i][w]`
*   **Relazione di ricorrenza:**
    `Count[i][w] = Count[i-1][w]` (non includere l'elemento `i`)
    `+ Count[i-1][w - w_i]` (includere l'elemento `i`, se `w >= w_i`)
*   **Casi base:**
    *   `Count = 1` (un modo per ottenere peso 0 con 0 elementi: scegliere l'insieme vuoto).
    *   `Count[w] = 0` per `w > 0`.
*   **Dimensioni della tabella:** `(n+1) x (W+1)`.
*   **Costo temporale:** `O(n * W)` per riempire la tabella [22].

Il numero totale di soluzioni fattibili (con peso totale `<= W`) è `Sum_{j=0 to W} Count[n][j]`.

**2. Campionamento Uniforme di una Soluzione Fattibile:**

L'idea per campionare uniformemente si basa sulla conoscenza dei conteggi ottenuti con la DP. Partiamo dall'ultimo elemento (`n`) e dalla capacità totale `W`. Per ogni elemento, decidiamo se includerlo o meno in base alle proporzioni dei conteggi che ciascuna scelta (includere o non includere) produce per il resto del problema.

Per facilitare il campionamento, è utile precalcolare i "somme prefisse" dei conteggi:
Sia `PrefixCount[i][w] = Sum_{j=0 to w} Count[i][j]`. Questo rappresenta il numero di sottoinsiemi dai primi `i` elementi con peso totale `<= w`.

*   **Fase di Precalcolo:**
    1.  Riempire la tabella `Count[i][w]` come descritto sopra (`O(n*W)`).
    2.  Calcolare la tabella `PrefixCount[i][w]` (`O(n*W)`):
        `PrefixCount[i][w] = PrefixCount[i][w-1] + Count[i][w]`
        `PrefixCount[i] = Count[i]`

*   **Algoritmo di Campionamento:**
    Si procede dall'ultimo elemento `i=n` fino al primo `i=1`. Ad ogni passo, si decide se includere l'elemento `i` nel sottoinsieme campionato.

**Pseudocodice per Campionamento Uniforme di Soluzioni Fattibili:**

```python
def knapsack_sample_feasible(n, W_max, weights):
    # weights: lista dei pesi degli elementi, weights non usato, weights[i] per l'elemento i

    # --- FASE DI PRECALCOLO: Costruzione della tabella DP (Count) ---
    # Count[i][w]: numero di modi per ottenere peso w usando i primi i elementi.
    Count = [ * (W_max + 1) for _ in range(n + 1)]
    Count = 1 # Un modo per ottenere peso 0 con 0 elementi (l'insieme vuoto)

    for i in range(1, n + 1):
        for w in range(W_max + 1):
            # Opzione 1: Non includere l'elemento i
            Count[i][w] = Count[i-1][w]
            
            # Opzione 2: Includere l'elemento i (se la capacità lo permette)
            if w >= weights[i]:
                Count[i][w] += Count[i-1][w - weights[i]]

    # --- FASE DI PRECALCOLO: Costruzione della tabella PrefixCount ---
    # PrefixCount[i][w]: numero di modi per ottenere peso <= w usando i primi i elementi.
    PrefixCount = [ * (W_max + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        PrefixCount[i] = Count[i]
        for w in range(1, W_max + 1):
            PrefixCount[i][w] = PrefixCount[i][w-1] + Count[i][w]

    # --- FASE DI CAMPIONAMENTO ---
    selected_items = []
    current_W = W_max
    
    # Il numero totale di soluzioni fattibili per la capacità W_max
    total_feasible_solutions = PrefixCount[n][W_max]

    if total_feasible_solutions == 0:
        return "Nessuna soluzione fattibile."

    # Scegli un numero casuale r tra 1 e il numero totale di soluzioni
    import random
    r = random.randint(1, total_feasible_solutions)

    # Scorre gli elementi dal più grande al più piccolo
    for i in range(n, 0, -1):
        # Numero di soluzioni se NON includiamo l'elemento i
        # Queste sono le soluzioni che usano i primi (i-1) elementi con peso <= current_W
        solutions_if_not_i = PrefixCount[i-1][current_W]

        # Numero di soluzioni se includiamo l'elemento i
        # Queste sono le soluzioni che usano i primi (i-1) elementi con peso <= (current_W - weights[i])
        solutions_if_i = 0
        if current_W >= weights[i]:
            solutions_if_i = PrefixCount[i-1][current_W - weights[i]]

        # Decisione: Se r cade nel range delle soluzioni che NON includono i
        if r <= solutions_if_not_i:
            # Non includere l'elemento i
            # current_W rimane invariato
            pass
        else:
            # Includere l'elemento i
            selected_items.append(i)
            # Riduci la capacità rimanente
            current_W -= weights[i]
            # Aggiorna r per riflettere il sotto-problema:
            # r ora rappresenta il "rank" della soluzione all'interno del sottoinsieme di soluzioni
            # che includono l'elemento i
            r -= solutions_if_not_i

    # Gli elementi vengono aggiunti in ordine inverso, quindi li ordiniamo per chiarezza
    return sorted(selected_items)

```

**Analisi del Costo Temporale:**

*   **Fase di Precalcolo (Count e PrefixCount):** Entrambe le tabelle vengono riempite con due cicli annidati `n` e `W_max`. Ogni operazione all'interno dei cicli è `O(1)`. Quindi, il costo di questa fase è **`O(n * W_max)`**.
*   **Fase di Campionamento:** Il ciclo scorre `n` volte. All'interno del ciclo, tutte le operazioni (accessi alla tabella `PrefixCount`, sottrazioni, aggiunte alla lista) sono `O(1)`. Quindi, il costo di questa fase è **`O(n)`**.

**Costo Temporale Totale:** La complessità dominante è la fase di precalcolo. Quindi, il costo temporale totale è **`O(n * W_max)`**.

**4. [OPZIONALE] Campionare Soluzioni Ottimali Uniformemente a Caso:**

Questa è una sfida più complessa. Lo schema DP1 discusso conta solo le soluzioni fattibili (in base al peso), non quelle che massimizzano un valore. Per campionare soluzioni `ottimali` (quelle che massimizzano il valore entro la capacità), la DP dovrebbe prima calcolare il valore massimo raggiungibile e poi contare il numero di modi per raggiungere quel valore massimo.

**Approccio:**
1.  **Trovare il Valore Ottimale (OPT_value):** Utilizzare una variante della DP per il problema dello zaino (con valori). Ad esempio, `dp[i][w]` potrebbe essere il valore massimo ottenibile usando i primi `i` elementi con peso `<= w`. Oppure `dp[i][val]` potrebbe essere il peso minimo per ottenere valore `val` usando i primi `i` elementi. Il `OPT_value` sarebbe il valore massimo che non supera `W`.
2.  **Contare le Soluzioni Ottimali:** Questa è la parte più difficile. La tabella DP deve essere estesa per contare il numero di modi in cui `OPT_value` può essere raggiunto con peso `<= W`. Questo potrebbe richiedere una tabella `count_opt[i][w]` che memorizza il numero di sottoinsiemi che raggiungono `dp[i][w]`.
    *   Le sfide sorgono quando più sottoinsiemi hanno lo stesso valore e peso. È necessario assicurarsi che il conteggio sia corretto e non sovra-conti soluzioni logicamente diverse.
    *   La sorgente stessa avverte: "Quando gli insiemi di soluzioni si sovrappongono parzialmente, questo metodo di conteggio non funziona in quanto può sovraccontare." e "Pertanto, il campionamento funziona quando lo schema di programmazione dinamica corrispondente non sovrappone le soluzioni." [23, 24]. Mentre gli insiemi di elementi sono distinti, la loro traduzione in peso/valore potrebbe non esserlo.
3.  **Campionamento:** Una volta che i conteggi delle soluzioni ottimali sono disponibili, si può applicare un approccio simile a quello del campionamento fattibile, procedendo a ritroso nella tabella DP per decidere quali elementi includere.

**Difficoltà e Limiti:**
*   La complessità dello schema DP per contare le soluzioni ottimali può essere molto più alta rispetto a `O(n*W_max)` se i valori o i pesi sono molto grandi (dipendendo da `Max_Value` o `Max_Weight` se usati come dimensione della DP).
*   Garantire l'uniformità esatta del campionamento per le soluzioni ottimali in scenari complessi richiede tecniche avanzate (es. MCMC o algoritmi basati su FPRAS - Fully Polynomial Randomized Approximation Scheme per il conteggio approssimato, come menzionato nelle fonti [25-27], ma non per il campionamento esatto e uniforme delle soluzioni ottimali). Le fonti fornite non dettagliamo un algoritmo per il campionamento esatto e uniforme di soluzioni ottimali.

In sintesi, mentre la domanda è concettualmente possibile, la sua implementazione è più complessa e richiede tecniche più avanzate rispetto a quelle coperte direttamente dalle fonti per il campionamento uniforme *esatto* di soluzioni ottimali.

---

## **Problema 3 (Pagina 6): 2-Approssimazione Randomizzata di MAX-CUT**

**Descrizione del Problema:**
1.  Progettare un semplice algoritmo randomizzato in tempo polinomiale per il problema MAX-CUT nei grafi non pesati e non orientati. Suggerimento: assegnare ogni nodo casualmente a uno dei due insiemi (cioè, colorazione casuale a 2 colori).
2.  Dimostrare che questo fornisce una 2-approssimazione in aspettativa. Suggerimento: utilizzare variabili indicatrici casuali.
3.  Migliorare la probabilità di errore ripetendo l'algoritmo `N` volte e usando le bound di Chernoff.

**Contesto MAX-CUT:**
Il problema MAX-CUT consiste nel suddividere i vertici di un grafo `G=(V,E)` in due insiemi `S` e `V\S` in modo da massimizzare il numero di archi che attraversano il taglio (cioè, con un estremo in `S` e l'altro in `V\S`). È un problema NP-hard [28-30].

**1. Semplice Algoritmo Randomizzato in Tempo Polinomiale:**

L'idea è di assegnare casualmente ciascun nodo a uno dei due insiemi del taglio.

*   **Algoritmo `RandomizedMaxCut(G)`:**
    1.  Crea due insiemi vuoti: `S_1` e `S_2`.
    2.  Per ogni nodo `u` nel grafo `V`:
        *   Lancia una moneta (o genera un numero casuale `x` in `[0,1)`).
        *   Se la moneta è "testa" (o `x < 0.5`), aggiungi `u` a `S_1`.
        *   Altrimenti (se "croce" o `x >= 0.5`), aggiungi `u` a `S_2`. [31, 32]
    3.  Calcola la dimensione del taglio risultante: conta tutti gli archi `(u,v) ∈ E` tali che `u` appartiene a `S_1` e `v` appartiene a `S_2` (o viceversa).
    4.  Restituisci la dimensione del taglio.

*   **Analisi del Tempo di Esecuzione:**
    *   L'assegnazione dei nodi a `S_1` o `S_2` richiede `O(|V|)` tempo (un passo per ogni nodo).
    *   Il calcolo della dimensione del taglio richiede di scorrere tutti gli archi e verificare le assegnazioni dei loro estremi, il che richiede `O(|E|)` tempo.
    *   Il tempo totale di esecuzione è **`O(|V| + |E|)`**, che è polinomiale.

**2. Dimostrare che fornisce una 2-Approssimazione in Aspettativa:**

Sia `X` la variabile casuale che rappresenta la dimensione del taglio trovata dall'algoritmo. Sia `OPT` la dimensione massima possibile del taglio (il valore ottimale). Vogliamo dimostrare che `E[X] >= OPT / 2`.

*   Sia `m = |E|` il numero totale di archi nel grafo. Sappiamo che `OPT <= m` (il taglio massimo non può essere più grande del numero totale di archi).
*   Definiamo una variabile indicatrice per ogni arco `e = (u,v) ∈ E`:
    *   Sia `X_e = 1` se l'arco `e` attraversa il taglio (cioè, `u` e `v` sono assegnati a insiemi diversi).
    *   Sia `X_e = 0` altrimenti (cioè, `u` e `v` sono assegnati allo stesso insieme).
*   La dimensione totale del taglio `X` è la somma di tutte queste variabili indicatrici: `X = Sum_{e ∈ E} X_e`.
*   Per la proprietà di linearità dell'aspettativa [10]: `E[X] = E[Sum X_e] = Sum_{e ∈ E} E[X_e]`.
*   Calcoliamo l'aspettativa di una singola variabile indicatrice `E[X_e]` per un arco `e=(u,v)`:
    *   `E[X_e] = 1 * Pr[X_e = 1] + 0 * Pr[X_e = 0] = Pr[X_e = 1]`.
    *   `Pr[X_e = 1]` è la probabilità che `u` e `v` siano in insiemi diversi.
    *   Ci sono quattro possibili assegnazioni equiprobabili per la coppia `(u,v)` (ogni nodo viene assegnato a `S_1` o `S_2` con probabilità 1/2, indipendentemente dall'altro):
        1.  `u ∈ S_1` e `v ∈ S_1` (probabilità `1/2 * 1/2 = 1/4`)
        2.  `u ∈ S_1` e `v ∈ S_2` (probabilità `1/2 * 1/2 = 1/4`)
        3.  `u ∈ S_2` e `v ∈ S_1` (probabilità `1/2 * 1/2 = 1/4`)
        4.  `u ∈ S_2` e `v ∈ S_2` (probabilità `1/2 * 1/2 = 1/4`)
    *   L'arco `e` attraversa il taglio nei casi 2 e 3.
    *   Quindi, `Pr[X_e = 1] = 1/4 + 1/4 = 1/2`. [31, 32]
*   Sostituendo questo risultato nell'espressione per `E[X]`:
    `E[X] = Sum_{e ∈ E} (1/2) = m / 2`.
*   Poiché `OPT <= m`, abbiamo `m / 2 >= OPT / 2`.
*   **Conclusione:** `E[X] >= OPT / 2`. L'algoritmo è una **2-approssimazione in aspettativa.** [29, 33].

**3. Migliorare la Probabilità di Errore (Boosting) usando le Bound di Chernoff:**

Il risultato precedente è un'approssimazione *in aspettativa*, il che significa che il valore medio del taglio trovato è almeno la metà dell'ottimale. Per garantire che l'algoritmo trovi un taglio vicino a questo valore con alta probabilità, possiamo ripetere l'esecuzione.

*   **Idea:** Esegui l'algoritmo `RandomizedMaxCut(G)` `N` volte in modo indipendente. Sia `X_k` la dimensione del taglio trovata nell'esecuzione `k`.
*   Il risultato finale sarà `X_max = max(X_1, X_2, ..., X_N)`. Questo è perché vogliamo massimizzare il taglio, quindi prendiamo il migliore tra i risultati delle diverse esecuzioni.

*   **Uso delle Bound di Chernoff:**
    Le bound di Chernoff forniscono limiti stretti per la probabilità che una somma di variabili casuali indipendenti (o debolmente dipendenti) si discosti significativamente dalla sua aspettativa [34, 35].
    Sia `X` la variabile casuale per la dimensione del taglio in una singola esecuzione. Abbiamo `E[X] = m/2`.
    Vogliamo che `X` sia almeno `(1-epsilon) * E[X]` (o `(1-epsilon) * OPT / 2`).
    La bound di Chernoff per la coda inferiore è:
    `Pr[X < (1 - delta) * E[X]] <= exp(-E[X] * delta^2 / 2)` [35].
    Sostituendo `E[X] = m/2`:
    `Pr[X < (1 - delta) * m/2] <= exp(-(m/2) * delta^2 / 2) = exp(-m * delta^2 / 4)`.

    Sia `P_fail_single = exp(-m * delta^2 / 4)` la probabilità che una singola esecuzione non produca un taglio abbastanza grande.
    Se eseguiamo l'algoritmo `N` volte in modo indipendente, la probabilità che *tutte* le `N` esecuzioni falliscano (cioè, `X_max` sia ancora troppo piccolo) è `(P_fail_single)^N`.
    Vogliamo che questa probabilità complessiva di fallimento sia al massimo `delta_overall` (una probabilità di errore che desideriamo sia piccola).
    ` (P_fail_single)^N <= delta_overall `
    ` (exp(-m * delta^2 / 4))^N <= delta_overall `
    ` exp(-N * m * delta^2 / 4) <= delta_overall `

    Prendendo il logaritmo naturale di entrambi i lati:
    `-N * m * delta^2 / 4 <= ln(delta_overall)`
    `N * m * delta^2 / 4 >= -ln(delta_overall) = ln(1/delta_overall)`
    `N >= (4 * ln(1/delta_overall)) / (m * delta^2)`

*   **Conclusione per il Boosting:**
    Per ottenere una 2-approssimazione (cioè, un taglio di dimensione almeno `(1-delta) * OPT / 2`) con una probabilità di errore `delta_overall`, dobbiamo ripetere l'algoritmo `N` volte, dove `N` è `O((1/(m * delta^2)) * log(1/delta_overall))`. Poiché `m` è il numero di archi, `N` è polinomiale in `m` e `log(1/delta_overall)`.
    Il costo totale dell'algoritmo migliorato sarà:
    `O(N * (|V| + |E|)) = O( (log(1/delta_overall) / (m * delta^2)) * (|V| + |E|) )`.
    Questo rende l'algoritmo **Monte Carlo** , che è garantito per avere un tempo di esecuzione polinomiale ma fornisce una soluzione approssimata con una probabilità di errore controllata.

---
