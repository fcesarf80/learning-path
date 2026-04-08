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

# =========================
# CRIAÇÃO DA JANELA
# =========================
janela = tk.Tk()

# Título da janela
janela.title("Primeira janela em Tk")

# Cor de fundo
janela.config(bg="orange")

# Tamanho da janela + posição inicial
# 400x330 = largura x altura
# +300+500 = distância da esquerda e do topo
janela.geometry("400x330+300+500")

# Impedir redimensionamento
janela.resizable(False, False)

# Fonte pedida no enunciado
fonte = ("Comic Sans MS", 14, "bold")

# Ícone da janela
# Coloque um ficheiro .ico na mesma pasta do programa
# Exemplo: icone.ico
try:
    janela.iconbitmap("icone.ico")
except:
    print("Ícone não encontrado. Coloque um ficheiro 'icone.ico' na mesma pasta do programa.")

# =========================
# COMPONENTES DA JANELA
# =========================

# Label
lbl_ola = tk.Label(
    janela,
    text="Olá Python",
    font=fonte,
    bg="orange"
)
lbl_ola.pack(pady=20)

# Caixa de texto
entrada = tk.Entry(
    janela,
    font=fonte,
    width=20
)
entrada.pack(pady=10)

# Função para sair
def sair():
    janela.destroy()

# Botão sair
btn_sair = tk.Button(
    janela,
    text="Sair",
    font=fonte,
    bg="lightblue",
    bd=4,
    command=sair
)
btn_sair.pack(pady=20)

# =========================
# LOOP PRINCIPAL
# =========================
janela.mainloop()