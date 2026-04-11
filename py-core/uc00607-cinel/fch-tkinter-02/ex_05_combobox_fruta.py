"""
Exercício 05 - Combobox fruta
Enunciado: Desenvolva uma pequena interface, usando combobox, para escolher a fruta preferida de uma lista inserida ao seu gosto.
"""

from tkinter import *
from tkinter.ttk import Combobox # Corrigido: importação correta

frutas = ("Maçã", "Banana", "Morango", "Uva") # Corrigido: nomes por frutas
jan = Tk()
jan.title("Exercício 05")
jan.geometry("300x300")
jan.iconbitmap("icone.ico")
# jan.iconbitmap("logo.ico") # Nota: certifique-se de que o arquivo existe ou comente esta linha

combo = Combobox(jan, values=frutas, state="readonly") # Corrigido: nome da variável
combo.set("Selecione uma fruta")
combo.pack(pady=20)

jan.mainloop()
