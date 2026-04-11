"""
Exercício 04 - Checkbutton carros
Enunciado: Desenvolva uma pequena interface, usando checkbutton, para escolher quais as marcas de automóveis que mais gosta.
"""
from tkinter import * 

def selecionar():
    # Altera o estado de todas as variáveis para True (marcado)
    m1V.set(True)
    m2V.set(True)
    m3V.set(True)
    m4V.set(True)
    m5V.set(True)

jan = Tk()
jan.title("Exercicio 4")
jan.iconbitmap("icone.ico")

# Variáveis de controle
m1V = BooleanVar()
m2V = BooleanVar()
m3V = BooleanVar()
m4V = BooleanVar()
m5V = BooleanVar()

# Checkbuttons (usando 'jan' como pai)
marca1 = Checkbutton(jan, text="Mercedes", variable=m1V)
marca2 = Checkbutton(jan, text="Audi", variable=m2V)
marca3 = Checkbutton(jan, text="VW", variable=m3V)
marca4 = Checkbutton(jan, text="BMW", variable=m4V)
marca5 = Checkbutton(jan, text="Seat", variable=m5V)

# Botão corrigido
botao = Button(jan, text="Selecionar todas", command=selecionar)

# Layout
marca1.grid(row=1, column=0, sticky=W)
marca2.grid(row=2, column=0, sticky=W)
marca3.grid(row=3, column=0, sticky=W)
marca4.grid(row=4, column=0, sticky=W)
marca5.grid(row=5, column=0, sticky=W)
botao.grid(row=6, column=0, pady=10)

jan.mainloop()
