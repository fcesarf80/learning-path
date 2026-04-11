"""
Exercício 03 - Radiobutton genero
Enunciado: Crie uma janela em Tkinter com radiobuttons para permitir
ao utilizador escolher o seu género. Deve existir um botão para ler
a opção selecionada e apresentar o resultado num label.
"""

#Desenvolva uma pequena interface, usando radiobutton,
# para escolher o género de uma pessoa.
from tkinter import *
from tkinter.messagebox import showinfo

def ler():
    # Mostra a opção escolhida
    showinfo(title="Opção escolhida...", 
             message=f"O valor associado ao botão Radio é {genero.get()}")

# Inicialização da janela
jan = Tk()
jan.title("Exercício 3")
jan.geometry("300x200")
jan.iconbitmap("icone.ico")

# Label Frame
lfgenero = LabelFrame(jan, text="Escolha o género...", padx=10, pady=10)
lfgenero.pack(padx=20, pady=20)

# Variável que armazena a escolha
genero = StringVar()
genero.set("Nenhum") # Define um valor inicial padrão

# Radiobuttons (Removida a duplicação de 'variable')
rMasc = Radiobutton(lfgenero, text="Masculino", variable=genero, value="Masculino", command=ler)
rFem = Radiobutton(lfgenero, text="Feminino", variable=genero, value="Feminino", command=ler)
rOutro = Radiobutton(lfgenero, text="NS/NR", variable=genero, value="Outro", command=ler)

# Posicionamento
rFem.grid(row=0, column=0, sticky=W)
rMasc.grid(row=1, column=0, sticky=W)
rOutro.grid(row=2, column=0, sticky=W)

jan.mainloop()
