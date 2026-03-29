"""
Exercício 14 - Entrada de Dados
Enunciado: Crie um interface idêntico ao seguinte:
a. O botão “Ler Dados” deverá ler o que foi escrito nas caixas
   de texto (Entry) e mostrar os seus conteúdos nos 2 rótulos (Label)
   abaixo da expressão “Os dados lidos são:”, criados para o efeito.
b. O Botão “Limpar” deverá limpar o conteúdo das caixas de texto.
c. O Botão “Sair” deverá abandonar a aplicação.
  → Explicação: Coloque uma caixa de texto na sua janela.
""" 


from tkinter import *
from posicao import *

##DEFS
def limpar():
    enome.delete(0,END)
    emorada.delete(0,END)
    enome.focus()

def ler():
    nome = enome.get()
    morada = emorada.get()
    ltxtnome["text"] = nome
    ltxtmorada.conigure(text=morada,font=("Arial",11))
jan = Tk()
jan.iconbitmap("logo.ico")
jan.geometry(centrar(jan,350,400))
jan.title("1º janela")

#Criar ZONAS (Frfames)
f1 = Frame(jan).pack()
f1.pack()
f2 = Frame(jan).pack()
f3.pack()
f3 = Frame(jan).pack()
f3.pack()

#F1
lnome = Label(f1, text="Nome:")
lmorada = Label(f1, text="Norada:")
enome = Label(f1)
emorada = Label(f1)

lnome.grid(row=0, column=0)
lmorada.grid(row=1, column=0)
enome.grid (row=0, column=1)
emorada.grid(row=1, column=1)

#F2
bler = Button(f2, text="Ler Dados", width=10, db=4,command=lambda:limpar())
blimpar = Button(f2, text="Limpar", width=10, db=4,command=limpar,command=lambda:limpar())
bsair =Button(f2, text="Sair", width=4, db="red",command = jan.destroy)

bler.pack(side="left",padx=5)
Packblimpar.pack(side="left",padx=5)
bsair.pack(side="left",padx=5)

enome.focus()
jan.mainloop()

#F3
ltexto = Label(f3,text="os dados lidos são:")
ltxtnome = Label(f1, text="Nome:")
ltxtmorada = Label(f1, text="Norada:")
enome = Label(f1)
emorada = Label(f1)

ltxto.pack(padx=5)
l.pack(side="left",padx=5)
bsar.pack(side="left",padx=5)