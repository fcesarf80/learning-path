"""
Exercício 03 - Radiobutton genero
Enunciado: Crie uma janela em Tkinter com radiobuttons para permitir
ao utilizador escolher o seu género. Deve existir um botão para ler
a opção selecionada e apresentar o resultado num label.
"""

import os
import tkinter as tk


# =========================
# FUNÇÃO PARA LER ESCOLHA
# =========================
def mostrar_genero():
    genero_escolhido = genero.get()

    if genero_escolhido == "Masculino":
        lbl_resultado.config(text="Género selecionado: Masculino")
    elif genero_escolhido == "Feminino":
        lbl_resultado.config(text="Género selecionado: Feminino")
    else:
        lbl_resultado.config(text="Nenhum género foi selecionado.")


# =========================
# JANELA PRINCIPAL
# =========================
janela = tk.Tk()
janela.title("Radiobutton - Género")
janela.resizable(False, False)

largura_janela = 350
altura_janela = 220

largura_ecra = janela.winfo_screenwidth()
altura_ecra = janela.winfo_screenheight()

pos_x = (largura_ecra // 2) - (largura_janela // 2)
pos_y = (altura_ecra // 2) - (altura_janela // 2)

janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Ícone
try:
    caminho_icone = os.path.join(os.path.dirname(__file__), "icone.ico")
    janela.iconbitmap(caminho_icone)
except Exception as erro:
    print("Ícone não encontrado:", erro)


# =========================
# VARIÁVEL DO RADIOBUTTON
# =========================
genero = tk.StringVar()
genero.set("")


# =========================
# COMPONENTES
# =========================
lbl_titulo = tk.Label(
    janela,
    text="Escolha o seu género:",
    font=("Arial", 12, "bold")
)
lbl_titulo.pack(pady=15)

rb_masculino = tk.Radiobutton(
    janela,
    text="Masculino",
    variable=genero,
    value="Masculino",
    font=("Arial", 11)
)
rb_masculino.pack(anchor="w", padx=40)

rb_feminino = tk.Radiobutton(
    janela,
    text="Feminino",
    variable=genero,
    value="Feminino",
    font=("Arial", 11)
)
rb_feminino.pack(anchor="w", padx=40)

btn_mostrar = tk.Button(
    janela,
    text="Confirmar",
    font=("Arial", 11, "bold"),
    command=mostrar_genero
)
btn_mostrar.pack(pady=15)

lbl_resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 11)
)
lbl_resultado.pack(pady=10)


# =========================
# LOOP PRINCIPAL
# =========================
janela.mainloop()