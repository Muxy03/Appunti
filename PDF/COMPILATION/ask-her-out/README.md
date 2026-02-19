# 💕 Ask Her Out - Progetto Svelte Romantico

Un modo speciale e interattivo per chiedere a qualcuno di uscire, con un design romantico ed elegante.

## ✨ Caratteristiche

- Design romantico con petali di rose che cadono
- Animazioni fluide e interattive
- Pulsante "No" che scappa quando ci passi sopra 😄
- Celebrazione con cuori quando dice "Sì"
- Completamente responsive
- Deploy facile su GitHub Pages

## 🚀 Setup Locale

### Prerequisiti
- Node.js (versione 16 o superiore)
- Git

### Installazione

1. Clona o scarica questo repository
2. Installa le dipendenze:
```bash
npm install
```

3. Avvia il server di sviluppo:
```bash
npm run dev
```

4. Apri il browser su `http://localhost:5173`

## 📦 Deploy su GitHub Pages

### Passaggio 1: Crea un Repository GitHub

1. Vai su [GitHub](https://github.com) e accedi
2. Clica su "New repository"
3. Dai un nome al repository (es: `ask-her-out`)
4. Scegli se renderlo pubblico o privato
5. **NON** aggiungere README, .gitignore o license (li abbiamo già)
6. Clica "Create repository"

### Passaggio 2: Aggiorna la Configurazione

Nel file `vite.config.js`, cambia la riga:
```javascript
base: '/ask-her-out/',
```

Sostituisci `ask-her-out` con il **nome esatto** del tuo repository GitHub.

### Passaggio 3: Carica il Codice su GitHub

Nella cartella del progetto, esegui:

```bash
# Inizializza git (se non già fatto)
git init

# Aggiungi tutti i file
git add .

# Fai il primo commit
git commit -m "Initial commit: romantic ask out page"

# Collega il repository remoto (SOSTITUISCI con il tuo username e nome repo)
git remote add origin https://github.com/TUO-USERNAME/NOME-REPO.git

# Carica su GitHub
git push -u origin main
```

**Nota**: Se GitHub usa `master` invece di `main`, usa:
```bash
git branch -M main
git push -u origin main
```

### Passaggio 4: Deploy

Esegui il comando di deploy:

```bash
npm run deploy
```

Questo comando:
1. Compila il progetto per la produzione
2. Crea un branch `gh-pages`
3. Carica i file compilati su GitHub

### Passaggio 5: Attiva GitHub Pages

1. Vai su GitHub nel tuo repository
2. Clicca su "Settings"
3. Nel menu laterale, clicca su "Pages"
4. In "Source", seleziona "gh-pages" branch
5. Clicca "Save"

Dopo qualche minuto, il tuo sito sarà disponibile su:
```
https://TUO-USERNAME.github.io/NOME-REPO/
```

## 🎨 Personalizzazione

### Cambiare i Colori

Nel file `src/app.css`, modifica le variabili CSS:

```css
:root {
  --color-rose: #ff6b9d;        /* Rosa principale */
  --color-deep-rose: #c9184a;   /* Rosa scuro */
  --color-blush: #ffb3c6;       /* Rosa chiaro */
  --color-cream: #fff8f0;       /* Sfondo crema */
  --color-gold: #d4af37;        /* Oro per decorazioni */
  --color-midnight: #1a1423;    /* Testo scuro */
}
```

### Cambiare i Testi

Apri `src/App.svelte` e modifica:

- Il titolo iniziale (cerca `<h1 class="title">`)
- La domanda (cerca `<h2 class="big-question">`)
- Il messaggio di celebrazione (cerca `.celebration-title`)

### Cambiare i Font

Nel file `src/app.css`, alla riga 1, puoi cambiare i Google Fonts importati.

## 📱 Build per Produzione

Per creare una build ottimizzata:

```bash
npm run build
```

I file pronti per il deploy saranno nella cartella `dist/`.

## 🔄 Aggiornamenti

Dopo aver fatto modifiche:

```bash
# Aggiungi i file modificati
git add .

# Fai un commit
git commit -m "Descrizione delle modifiche"

# Carica su GitHub
git push

# Rideploya
npm run deploy
```

## 🛠️ Comandi Disponibili

- `npm run dev` - Avvia server di sviluppo
- `npm run build` - Crea build di produzione
- `npm run preview` - Anteprima build locale
- `npm run deploy` - Deploy su GitHub Pages

## 💡 Consigli

1. **Privacy**: Se vuoi che il sito sia privato prima della proposta, usa un repository privato
2. **Custom Domain**: Puoi configurare un dominio personalizzato nelle impostazioni GitHub Pages
3. **Mobile**: Testa sempre su mobile prima di condividere il link!
4. **Browser**: Funziona meglio su Chrome, Firefox e Safari moderni

## ⚠️ Troubleshooting

### Il sito non si carica
- Verifica che il `base` in `vite.config.js` corrisponda al nome del repository
- Controlla che GitHub Pages sia attivato nel branch `gh-pages`
- Aspetta qualche minuto dopo il primo deploy

### Errori durante il deploy
- Assicurati di aver eseguito `npm install`
- Verifica di avere i permessi sul repository
- Controlla che l'URL remoto sia corretto: `git remote -v`

### Il pulsante "No" non si muove
- Potrebbe essere un problema di JavaScript disabilitato
- Prova su un altro browser

## 📄 Licenza

Sentiti libero di usare, modificare e condividere questo progetto per le tue proposte romantiche! 💕

---

Creato con ❤️ e Svelte
