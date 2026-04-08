"""
Exercício 02 - Interface dados
Enunciado: Crie um interface gráfico em Tkinter com os campos Nome e Morada,
botões Ler Dados, Limpar e Sair, e uma área de saída com o texto
“Os dados lidos são:”.
O botão “Ler Dados” deverá ler o conteúdo das caixas de texto e mostrar
os valores em labels criadas para esse efeito.
O botão “Limpar” deverá limpar o conteúdo das caixas de texto.
O botão “Sair” deverá abandonar a aplicação.
"""

import tkinter as tk
import os


# =========================
# FUNÇÕES
# =========================
def ler_dados():
    nome = ent_nome.get()
    morada = ent_morada.get()

    lbl_nome_resultado.config(text=f"Nome: {nome}")
    lbl_morada_resultado.config(text=f"Morada: {morada}")


def limpar_dados():
    ent_nome.delete(0, tk.END)
    ent_morada.delete(0, tk.END)

    lbl_nome_resultado.config(text="")
    lbl_morada_resultado.config(text="")

    ent_nome.focus()


def sair():
    janela.destroy()


# =========================
# JANELA PRINCIPAL
# =========================
janela = tk.Tk()
janela.title("1ª janela")
janela.geometry("500x320")
janela.resizable(False, False)


# =========================
# FONTES
# =========================
fonte_label = ("Arial", 12)
fonte_botao = ("Arial", 11, "bold")
fonte_saida = ("Arial", 12, "bold")


# =========================
# LABELS E ENTRIES
# =========================
lbl_nome = tk.Label(janela, text="Nome:", font=fonte_label)
lbl_nome.place(x=40, y=30)

ent_nome = tk.Entry(janela, width=35, font=fonte_label)
ent_nome.place(x=120, y=30)

lbl_morada = tk.Label(janela, text="Morada:", font=fonte_label)
lbl_morada.place(x=40, y=70)

ent_morada = tk.Entry(janela, width=35, font=fonte_label)
ent_morada.place(x=120, y=70)


# =========================
# BOTÕES
# =========================
btn_ler = tk.Button(
    janela,
    text="Ler Dados",
    width=10,
    font=fonte_botao,
    bg="lightgray",
    command=ler_dados
)
btn_ler.place(x=70, y=120)

btn_limpar = tk.Button(
    janela,
    text="Limpar",
    width=10,
    font=fonte_botao,
    bg="lightgray",
    command=limpar_dados
)
btn_limpar.place(x=200, y=120)

btn_sair = tk.Button(
    janela,
    text="Sair",
    width=10,
    font=fonte_botao,
    bg="red",
    fg="white",
    command=sair
)
btn_sair.place(x=330, y=120)


# =========================
# ÁREA DE SAÍDA
# =========================
lbl_saida = tk.Label(janela, text="Os dados lidos são:", font=fonte_saida)
lbl_saida.place(x=40, y=190)

lbl_nome_resultado = tk.Label(janela, text="", font=fonte_label)
lbl_nome_resultado.place(x=40, y=230)

lbl_morada_resultado = tk.Label(janela, text="", font=fonte_label)
lbl_morada_resultado.place(x=40, y=260)


# =========================
# FOCO INICIAL
# =========================
ent_nome.focus()


# =========================
# IMAGEM
# =========================
caminho_imagem = os.path.join(os.path.dirname(__file__), "img-charliebrown.png")

try:
    imagem = tk.PhotoImage(file=caminho_imagem)

    lbl_imagem = tk.Label(janela, image=imagem, bg=janela["bg"])

    janela.update_idletasks()

    largura = janela.winfo_width()
    altura = janela.winfo_height()

    largura_img = 73
    altura_img = 110

    lbl_imagem.place(x=395, y=200)

except Exception as erro:
    print("Erro ao carregar imagem:", erro)

# Loop principal
janela.mainloop()