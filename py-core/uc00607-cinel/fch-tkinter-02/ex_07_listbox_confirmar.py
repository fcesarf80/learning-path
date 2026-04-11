"""
Exercício 07 - Listbox confirmar
Enunciado: Utilizando a interface anterior, utilize a biblioteca messagebox para criar popup de confirmação se pretende remover ou não o item selecionado.
"""

def remover():
    posicoes = lstbox.curselection() # devolve uma tupla de valores
    posicoes = posicoes[::-1] # inverte a tupla para apagar de baixo para cima
    for pos in posicoes:
        lstbox.delete(pos)

from tkinter import *
from tkinter.messagebox import showinfo


cidades = sorted(["Porto", "Lisboa", "Maia", "Viana", "Viseu"])

jan = Tk()
jan.title("Exercício 07")
jan.geometry("300x300")
jan.iconbitmap("icone.ico")

lstbox = Listbox(jan, width=30, selectmode="extended")
lstbox.pack()
for nome in cidades:
    lstbox.insert("end", nome)

botao = Button(jan, text="Remover", command=remover)
botao.pack()

jan.mainloop()


