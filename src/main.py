
"""
Shitty Terminal - Un semplice terminale grafico in Tkinter

Funzionalità:
- Prompt personalizzato ( -> )
- Esecuzione di comandi di shell
- Pulizia terminale con 'cls'
- Protezione del prompt e delle righe precedenti
- Font monospaziato per migliore leggibilità

Note:
- Il terminale non è una shell reale, ma simula l'esperienza base.
"""

# Spiegazione di alcune notazioni Tkinter:
# 'end-1c' -> indice alla fine del contenuto di text meno un carattere (cioè subito prima della fine)
# <Return> -> evento tasto Invio

import tkinter as tk
import os
import subprocess
import tkinter.font as tkfont
import random


def command(comando: str):
    # Se il comando è 'cls', pulisci il terminale personalizzato
    if comando.strip() == "cls" or comando.strip() == "clear":
        text_area.delete("1.0", "end")  # Cancella tutto il contenuto
        # Prompt con percorso corrente
        prompt = f"{os.getcwd()} -> "
        text_area.insert("end", prompt)
        # Aggiorna input_start_index per permettere la scrittura dopo la pulizia
        global input_start_index
        input_start_index = text_area.index("end-1c")
        text_area.mark_set("insert", "end")
        return None

    if comando.strip() == "ls":
        output = subprocess.run("dir", shell=True, capture_output=True, text=True)
        if output.returncode == 0:
            return output.stdout
        else:
            return output.stderr

    if comando.strip().startswith("random"):
        # args contiene solo la parte numerica del comando, senza la parola 'random' e senza virgolette:
        # - .replace('random', '') rimuove la parola 'random' dalla stringa
        # - .replace('"', '') rimuove tutte le virgolette doppie
        # - .strip() elimina eventuali spazi all'inizio e alla fine
        args = comando.replace('random', '').replace('"', '').strip()
        if '-' in args:
            min_value, max_value = args.split('-')
            min_v = int(min_value.strip())
            max_v = int(max_value.strip())
            numero_random = random.randint(min_v, max_v)
            return str(numero_random)
        else:
            return 'Uso: random "min - max"'
    

    # Esegui il comando di shell normalmente
    output = subprocess.run(comando, shell=True, capture_output=True, text=True)
    # output.stdout contiene l'output
    # output.stderr contiene eventuali errori
    # output.returncode è il codice di uscita

    if output.returncode == 0:
        return output.stdout
    elif output.returncode == 1:
        return output.stderr


def on_key_press(event):
    global input_start_index, text_area
    # Impedisci la scrittura/cancellazione prima del prompt
    if text_area.compare("insert", "<", input_start_index):
        text_area.mark_set("insert", "end")  # Sposta il cursore alla fine
        return "break"
    # Impedisci la cancellazione del prompt
    if event.keysym == "BackSpace" and text_area.compare("insert", "<=", input_start_index):
        return "break"


def on_enter(event):
    global input_start_index, text_area

    # Prendi il comando digitato dall'utente dopo il prompt
    comando = text_area.get(input_start_index, "end-1c").strip()

    # Esegui il comando e ottieni l'output
    output = command(comando)

    # Se il comando era 'cls', non aggiungere output
    if output is None:
        return "break"

    # Inserisci l'output e un nuovo prompt con percorso corrente
    prompt = f"{os.getcwd()} -> "
    text_area.insert("end", "\n" + output + "\n" + prompt)

    # Aggiorna l'indice di inizio input dopo il nuovo prompt
    input_start_index = text_area.index("end-1c")
    text_area.see("end")
    text_area.mark_set("insert", "end")  # Cursore alla fine
    return "break"



def main():
    # Crea la finestra principale
    root = tk.Tk()
    root.title('Shitty')
    root.geometry("1000x600")  # Dimensioni della finestra

    # Font monospaziato per simulare un terminale vero
    font_cascadia = tkfont.Font(family="Cascadia Mono", size=11)

    global input_start_index, text_area
    # Crea l'area di testo principale (il "terminale")
    # Colori blu notte e testo azzurro chiaro
    text_area = tk.Text(
        root,
        bg="#181818", # nero meno intenso (grigio molto scuro)
        fg="#ffffff",  # testo bianco
        padx=5, pady=5, #padding
        font=font_cascadia, #font
        insertbackground="#ffffff",  # cursore nero
        wrap="word"  # va a capo automaticamente
    )
    text_area.pack(expand=True, fill="both")

    # Inserisci il primo prompt con percorso corrente
    prompt = f"{os.getcwd()} -> "
    text_area.insert("end", prompt)
    input_start_index = text_area.index("end-1c")

    # Focus subito pronto per scrivere
    text_area.focus_set()
    text_area.mark_set("insert", "end")

    # Collega gli eventi principali
    text_area.bind("<Return>", on_enter)  # Invio esegue il comando
    text_area.bind("<Key>", on_key_press) # Protegge il prompt

    root.mainloop()


if __name__ == '__main__':
    main()