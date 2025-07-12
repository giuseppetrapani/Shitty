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

# --- Fix per problemi di sgranatura su Windows (DPI awareness) ---
# Questo codice forza la modalità DPI-aware per evitare che la GUI appaia sfocata su schermi ad alta risoluzione.
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass


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
    font_cascadia = tkfont.Font(family="Cascadia Mono", size=11, weight="normal")

    # --- BARRA PERSONALIZZATA ---
    barra = tk.Frame(root, height=14, bg="#181818")
    barra.pack(side="top", fill="x")

    # =====================
    # 1. FUNZIONI TEMA
    # =====================
    def set_tema_chiaro():
        text_area.config(bg="#f5f5f5", fg="#222222", insertbackground="#222222")
        barra.config(bg="#f5f5f5")
        luna.config(bg="#f5f5f5", fg="#222222", activebackground="#e0e0e0", activeforeground="#222222")
        menu_temi.config(bg="#f5f5f5", fg="#222222", activebackground="#e0e0e0", activeforeground="#222222")
        menu_impostazioni.config(bg="#f5f5f5", fg="#222222", activebackground="#e0e0e0", activeforeground="#222222")
        aggiorna_menu_font()

    def set_tema_scuro():
        text_area.config(bg="#181818", fg="#ffffff", insertbackground="#ffffff")
        barra.config(bg="#181818")
        luna.config(bg="#181818", fg="#ffffff", activebackground="#222222", activeforeground="#ffffff")
        menu_temi.config(bg="#181818", fg="#ffffff", activebackground="#222222", activeforeground="#ffffff")
        menu_impostazioni.config(bg="#181818", fg="#ffffff", activebackground="#222222", activeforeground="#ffffff")
        aggiorna_menu_font()

    def set_tema_gruvbox():
        text_area.config(bg="#282828", fg="#ebdbb2", insertbackground="#ebdbb2")
        barra.config(bg="#282828")
        luna.config(bg="#282828", fg="#ebdbb2", activebackground="#3c3836", activeforeground="#ebdbb2")
        menu_temi.config(bg="#282828", fg="#ebdbb2", activebackground="#3c3836", activeforeground="#ebdbb2")
        menu_impostazioni.config(bg="#282828", fg="#ebdbb2", activebackground="#3c3836", activeforeground="#ebdbb2")
        aggiorna_menu_font()

    def set_tema_shades_of_purple():
        text_area.config(bg="#2d2b55", fg="#fad000", insertbackground="#fad000")
        barra.config(bg="#2d2b55")
        luna.config(bg="#2d2b55", fg="#fad000", activebackground="#5e4b8b", activeforeground="#fad000")
        menu_temi.config(bg="#2d2b55", fg="#fad000", activebackground="#5e4b8b", activeforeground="#fad000")
        menu_impostazioni.config(bg="#2d2b55", fg="#fad000", activebackground="#5e4b8b", activeforeground="#fad000")
        aggiorna_menu_font()

    # =====================
    # 2. FUNZIONI FONT
    # =====================
    def set_font_size(size):
        font_cascadia.configure(size=size)
        aggiorna_menu_font()

    def aggiorna_menu_font():
        # Aggiorna i colori del menu_font e dei sottomenu in base al tema
        # Aggiorna i colori della tendina e delle voci
        menu_font.config(
            bg=menu_temi.cget('bg'),
            fg=menu_temi.cget('fg'),
            activebackground=menu_temi.cget('activebackground'),
            activeforeground=menu_temi.cget('activeforeground'),
            bd=0,
            relief="flat"
        )
        end_index = menu_font.index('end')
        if end_index is not None:
            for i in range(end_index+1):
                # Aggiorna anche la label per la dimensione attuale
                label = menu_font.entrycget(i, 'label')
                size = int(label.split()[0]) if label.split()[0].isdigit() else None
                new_label = f"{size} pt" + ("  (attuale)" if size == font_cascadia['size'] else "") if size else label
                menu_font.entryconfig(i,
                    label=new_label,
                    background=menu_temi.cget('bg'),
                    foreground=menu_temi.cget('fg'),
                    activebackground=menu_temi.cget('activebackground'),
                    activeforeground=menu_temi.cget('activeforeground')
                )


    # =====================
    # 3. MENU TEMI E IMPOSTAZIONI
    # =====================
    # Inizializzazione dei menu e applicazione del tema di default
    # Questo garantisce che tutti i menu (inclusa la tendina del font) siano già adattati al tema all'avvio
    menu_temi = tk.Menu(barra, tearoff=0)
    menu_temi.add_command(label="Chiaro", command=set_tema_chiaro)
    menu_temi.add_command(label="Scuro", command=set_tema_scuro)
    menu_temi.add_command(label="Gruvbox", command=set_tema_gruvbox)
    menu_temi.add_command(label="Shades of Purple", command=set_tema_shades_of_purple)

    menu_impostazioni = tk.Menu(barra, tearoff=0)
    menu_font = tk.Menu(menu_impostazioni, tearoff=0)
    for size in range(8, 25, 2):
        menu_font.add_command(label=f"{size} pt" + ("  (attuale)" if font_cascadia['size']==size else ""), command=lambda s=size: set_font_size(s))
    menu_impostazioni.add_cascade(label="Grandezza font", menu=menu_font)


    # =====================
    # 5. TEXT AREA TERMINALE
    # =====================
    global input_start_index, text_area
    text_area = tk.Text(
        root,
        bg="#181818",
        fg="#ffffff",
        padx=5, pady=5,
        font=font_cascadia,
        insertbackground="#ffffff",
        wrap="word"
    )
    text_area.pack(expand=True, fill="both")

    # =====================
    # 4. BOTTONI BARRA
    # =====================
    def mostra_menu_temi(event=None):
        x = luna.winfo_rootx()
        y = luna.winfo_rooty() + luna.winfo_height()
        menu_temi.tk_popup(x, y)

    def mostra_menu_impostazioni(event=None):
        x = impostazioni.winfo_rootx()
        y = impostazioni.winfo_rooty() + impostazioni.winfo_height()
        menu_impostazioni.tk_popup(x, y)
        # Rimuove l'hover dal bottone quando il menu viene chiuso
        menu_impostazioni.grab_release()
        impostazioni.config(state="normal")

    luna = tk.Button(barra, text="🌙", bg="#181818", fg="#ffffff", bd=0, font=("Segoe UI Emoji", 14), activebackground="#222222", activeforeground="#ffffff", command=mostra_menu_temi, cursor="hand2")
    luna.pack(side="right", padx=8, pady=2)

    impostazioni = tk.Button(barra, text="⚙️", bg="#181818", fg="#ffffff", bd=0, font=("Segoe UI Emoji", 14), activebackground="#222222", activeforeground="#ffffff", command=mostra_menu_impostazioni, cursor="hand2")
    impostazioni.pack(side="left", padx=8, pady=2)

    # Applica il tema scuro di default (così tutti i menu sono già adattati)
    set_tema_scuro()

    # =====================
    # 6. PROMPT E EVENTI
    # =====================
    prompt = f"{os.getcwd()} -> "
    text_area.insert("end", prompt)
    input_start_index = text_area.index("end-1c")
    text_area.focus_set()
    text_area.mark_set("insert", "end")
    text_area.bind("<Return>", on_enter)
    text_area.bind("<Key>", on_key_press)

    root.mainloop()


if __name__ == '__main__':
    main()