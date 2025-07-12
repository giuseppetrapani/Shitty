# Shitty Terminal - Documentazione Completa

## Indice
- [Descrizione generale](#descrizione-generale)
- [Funzionalità principali](#funzionalità-principali)
- [Struttura del codice](#struttura-del-codice)
- [Gestione dei temi](#gestione-dei-temi)
- [Gestione del font](#gestione-del-font)
- [Gestione dei menu](#gestione-dei-menu)
- [Gestione del prompt e input](#gestione-del-prompt-e-input)
- [Esecuzione dei comandi](#esecuzione-dei-comandi)
- [Personalizzazioni e dettagli UI](#personalizzazioni-e-dettagli-ui)
- [Note tecniche e consigli](#note-tecniche-e-consigli)

---

## Descrizione generale

**Shitty Terminal** è un terminale grafico minimale scritto in Python con Tkinter. L'obiettivo è simulare un terminale testuale, ma con alcune comodità grafiche e personalizzazioni, mantenendo la semplicità e la leggibilità del codice.

---

## Funzionalità principali
- Prompt personalizzato che mostra il percorso corrente
- Esecuzione di comandi di shell (Windows)
- Comando `cls`/`clear` per pulire il terminale
- Comando `ls` (alias di `dir` su Windows)
- Comando custom `random "min - max"` per generare numeri casuali
- Protezione del prompt e delle righe precedenti (non modificabili)
- Cambio tema (chiaro, scuro, Gruvbox, Shades of Purple)
- Cambio dimensione font tramite menu a tendina
- Interfaccia moderna con barra personalizzata e bottoni

---

## Struttura del codice

- **main.py** contiene tutto il codice.
- La funzione principale è `main()`, che crea la finestra, i widget e collega tutte le funzionalità.
- Le funzioni sono raggruppate per tema, font, menu, gestione eventi.
- Tutte le variabili globali (come `text_area` e `input_start_index`) sono dichiarate dove necessario.

---

## Gestione dei temi

Sono disponibili 4 temi:
- Chiaro
- Scuro (default)
- Gruvbox
- Shades of Purple

Ogni tema modifica:
- Colori di sfondo e testo della text_area
- Colori della barra superiore
- Colori dei bottoni e dei menu (inclusa la tendina del font)

Le funzioni `set_tema_chiaro`, `set_tema_scuro`, `set_tema_gruvbox`, `set_tema_shades_of_purple` applicano i colori a tutti i componenti.

> **Nota:** Il tema viene applicato all'avvio dopo la creazione di tutti i widget, così tutto è coerente da subito.

---

## Gestione del font

- Il font usato è "Cascadia Mono", monospaziato, ideale per terminali.
- La dimensione del font può essere cambiata dal menu impostazioni, scegliendo tra valori predefiniti (8-24 pt).
- La voce attuale viene evidenziata con la dicitura `(attuale)`.
- Il menu del font si adatta sempre al tema attivo (colori coerenti).

---

## Gestione dei menu

- **Menu Temi:** accessibile dal bottone 🌙, permette di cambiare tema al volo.
- **Menu Impostazioni:** accessibile dal bottone ⚙️, contiene la tendina per la grandezza del font.
- I menu sono realizzati con `tk.Menu` e sono completamente adattivi al tema.
- Quando si chiude il menu impostazioni, l'effetto hover sul bottone viene rimosso per evitare bug visivi.

---

## Gestione del prompt e input

- Il prompt mostra sempre il percorso corrente (`os.getcwd()`), seguito da `->`.
- L'utente può scrivere solo dopo il prompt: le righe precedenti sono protette.
- Il cursore viene sempre riportato alla fine se si tenta di scrivere/cancellare prima del prompt.
- Il tasto Invio esegue il comando e mostra l'output, seguito da un nuovo prompt.

---

## Esecuzione dei comandi

- I comandi vengono eseguiti tramite `subprocess.run`.
- Comandi speciali:
    - `cls`/`clear`: pulisce il terminale e mostra solo il prompt
    - `ls`: mostra il contenuto della cartella (alias di `dir` su Windows)
    - `random "min - max"`: genera un numero casuale tra min e max
- Tutti gli altri comandi vengono passati alla shell di sistema.
- L'output (stdout o stderr) viene mostrato subito dopo il prompt.

---

## Personalizzazioni e dettagli UI

- Barra superiore personalizzata con Frame, bottoni a destra (🌙) e sinistra (⚙️)
- Tutti i colori sono coerenti con il tema attivo
- La text_area è una `tk.Text` con padding e word wrap
- I menu sono senza bordo e con effetto flat
- Tutti i widget sono creati in ordine logico per evitare errori di variabile non definita

---

## Note tecniche e consigli

- Il codice è pensato per essere facilmente estendibile: puoi aggiungere altri temi, altre voci di menu o comandi custom
- Se vuoi cambiare il tema di default, basta cambiare la chiamata a `set_tema_scuro()` dopo la creazione dei widget
- Tutte le funzioni di tema/font/menu sono modulari e riutilizzabili
- Se aggiorni la struttura, mantieni l'ordine di creazione dei widget per evitare errori di variabile non definita
- Per aggiungere nuove impostazioni, usa il menu impostazioni e aggiorna la funzione corrispondente

---

## Esempio di flusso di esecuzione
1. Avvio: viene creata la finestra, la barra, i menu, la text_area, i bottoni
2. Viene applicato il tema scuro di default
3. L'utente può cambiare tema o font in qualsiasi momento
4. L'utente scrive un comando dopo il prompt e preme Invio
5. Il comando viene eseguito e l'output mostrato, seguito da un nuovo prompt
6. Tutto resta sempre coerente con il tema scelto

---

## Modifiche rapide
- Per aggiungere un nuovo tema: crea una nuova funzione `set_tema_nome()` e aggiungi una voce in `menu_temi`
- Per aggiungere nuove impostazioni: aggiungi voci a `menu_impostazioni` e la logica corrispondente
- Per cambiare il font di default: modifica la riga di creazione di `font_cascadia`

