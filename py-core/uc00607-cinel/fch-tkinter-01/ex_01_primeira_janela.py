"""
Exercício 01 - Primeira janela
Enunciado: Crie uma janela em Tkinter com o título “Primeira janela em Tk”,
fundo laranja, dimensões 400x330 píxeis, sem redimensionamento.
Defina uma variável “fonte” com "Comic Sans MS", tamanho 14 e negrito.
Altere o ícone da janela para um ficheiro .ico à sua escolha.
Defina o posicionamento inicial da janela para 300 píxeis da esquerda
e 500 píxeis abaixo do topo do ecrã.
Coloque um rótulo com o texto “Olá Python”, uma caixa de texto
e um botão “Sair”, programado para fechar a aplicação.
Mude a cor de fundo do botão e aplique uma pequena borda.
"""

import tkinter as tk

# 1) Criação da janela
janela = tk.Tk()

# 2) Título da janela
janela.title("Primeira janela em Tk")

# 3) Cor de fundo
janela.config(bg="orange")

# 4) Tamanho da janela + posição inicial
# 400x330 = largura x altura
# +300+500 = distância da esquerda e do topo
janela.geometry("400x330+300+500")

# 5) Impedir redimensionamento
janela.resizable(False, False)

# 6) Fonte pedida no enunciado
fonte = ("Comic Sans MS", 14, "bold")

# 7) Ícone da janela
try:
    janela.iconbitmap("icone.ico")
except:
    print("Ícone não encontrado. Coloque um ficheiro 'icone.ico' na mesma pasta do programa.")

# 9) Label com o texto "Olá Python"
lbl_ola = tk.Label(
    janela,
    text="Olá Python",
    font=fonte,
    bg="orange"
)
lbl_ola.pack(pady=20)

# 11) Caixa de texto
entrada = tk.Entry(
    janela,
    font=fonte,
    width=20
)
entrada.pack(pady=10)

# 12) Função para sair
def sair():
    janela.destroy()

# 13) Botão sair
btn_sair = tk.Button(
    janela,
    text="Sair",
    font=fonte,
    bg="lightblue",
    bd=4,
    command=sair
)
btn_sair.pack(pady=20)

# Bónus: imagem png no canto inferior esquerdo
try:
    imagem = tk.PhotoImage(file="img-milhouse.png")
    lbl_imagem = tk.Label(janela, image=imagem, bg="orange")
    lbl_imagem.place(x=5, y=220)
except Exception as erro:
    print("Erro ao carregar imagem:", erro)

janela.mainloop()