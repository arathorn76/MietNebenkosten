import tkinter as tk
from tkinter import ttk

def select_text(texts):
    elv = tk.Tk()
    elv.title("Textauswahl")

    # Erstellen der Auswahlliste
    text_var = tk.StringVar()
    text_var.set(texts[0])
    text_select = ttk.Combobox(elv, textvariable=text_var, values=texts)
    text_select.pack()

    # Button, um Auswahl zu bestätigen
    submit_button = ttk.Button(elv, text="Auswahl bestätigen", 
                               command=lambda: elv.destroy())
    submit_button.pack()

    # Mainloop, um GUI anzuzeigen
    elv.mainloop()
    return text_var.get()

if __name__ == '__main__':
    texts = ["Dies ist Text 1", "Dies ist Text 2", "Dies ist Text 3"]
    selected_text = select_text(texts)
    selected_index = texts.index(selected_text)
    print(f"Ausgewählter Text: {selected_text}, Index: {selected_index}")
