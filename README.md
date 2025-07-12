# Shitty Terminal

Un semplice terminale grafico in Tkinter per Windows.

## Esempio di utilizzo

```
python src/main.py

```

---

## Screenshot dei temi

Esempi dei temi disponibili:

### Tema Scuro
<img src="Screenshot%202025-07-12%20165124.png" alt="Tema Scuro" width="500" />

### Tema Gruvbox
<img src="Screenshot%202025-07-12%20165124.png" alt="Tema Gruvbox" width="500" />

### Tema Shades of Purple
<img src="Screenshot%202025-07-12%20165124.png" alt="Tema Shades of Purple" width="500" />

### Tema Chiaro
<img src="Screenshot%202025-07-12%20165124.png" alt="Tema Chiaro" width="500" />

---

## Attenzione

Questo progetto è solo a scopo di prova e sperimentazione.
**Non utilizzare come terminale principale!**



## Funzionalità

- Prompt personalizzato con percorso corrente (`os.getcwd()`)
- Esecuzione di comandi di shell (Windows)
- Comando `cls`/`clear` per pulire il terminale
- Comando `ls` (alias di `dir` su Windows)
- Comando custom `random "min - max"` per generare numeri casuali
- Protezione del prompt e delle righe precedenti (non modificabili)
- Cambio tema (chiaro, scuro, Gruvbox, Shades of Purple) dal menu grafico
- Cambio dimensione font tramite menu a tendina (8-24 pt, con evidenziazione della dimensione attuale)
- Interfaccia moderna con barra personalizzata e bottoni (🌙 per i temi, ⚙️ per le impostazioni)
- Menu e tendine completamente adattivi al tema scelto
- Prompt sempre protetto: puoi scrivere solo dopo il prompt
- Output dei comandi subito dopo il prompt
- Tutto il codice è facilmente estendibile e commentato



