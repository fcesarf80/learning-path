"""
Exercício 06 - Listbox cidades
Enunciado: Desenvolva uma interface gráfica onde é criada uma listbox com 5 nomes de cidades. A aplicação deverá permitir apagar a cidade selecionada.
"""

from tkinter import *
from tkinter import messagebox

def remover():
    # Pega o índice do item selecionado
    selecao = listbox.curselection()
    
    if not selecao:
        messagebox.showerror(title="Erro", message="Selecione uma cidade primeiro")
    else:
        # Remove da interface (listbox)
        listbox.delete(selecao)

cidades = sorted(["Porto", "Lisboa", "Maia", "Viana", "Viseu"])

jan = Tk()
jan.title("Exercício 06")
jan.geometry("300x350")
jan.iconbitmap("icone.ico")

# Criação da Listbox conforme o enunciado
listbox = Listbox(jan)
for cidade in cidades:
    listbox.insert(END, cidade)
listbox.pack(pady=10)

# Botão para remover chamando a função correta
botao = Button(jan, text="Remover Cidade", command=remover)
botao.pack(pady=5)

# Botão para sair
botao_sair = Button(jan, text="Sair", command=jan.destroy)
botao_sair.pack(pady=5)

jan.mainloop()
