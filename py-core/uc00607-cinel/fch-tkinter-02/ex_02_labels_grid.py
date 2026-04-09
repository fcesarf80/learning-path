"""
Exercício 02 - Labels grid
Enunciado: Utilizando o método de apresentação GRID, elabore uma janela
idêntica à apresentada no enunciado, com labels coloridas distribuídas
em diferentes linhas e colunas.
"""
"""
Exercício 02 - Labels grid
Enunciado: Utilizando o método de apresentação GRID, elabore uma janela
idêntica à apresentada no enunciado, com labels coloridas distribuídas
em diferentes linhas e colunas.
"""
import tkinter as tk

# Janela principal
janela = tk.Tk()
janela.title("Grid com Labels")
janela.resizable(False, False)

# Tamanho da janela
largura_janela = 500
altura_janela = 220

# Centralizar no ecrã
largura_ecra = janela.winfo_screenwidth()
altura_ecra = janela.winfo_screenheight()

pos_x = (largura_ecra // 2) - (largura_janela // 2)
pos_y = (altura_ecra // 2) - (altura_janela // 2)

janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Ícone
try:
    janela.iconbitmap("icone.ico")
except:
    print("Ícone não encontrado.")

# Configuração das colunas
for coluna in range(6):
    janela.grid_columnconfigure(coluna, weight=1)

# Labels
lbl1 = tk.Label(
    janela,
    text="Label 1",
    bg="red",
    fg="white",
    width=18,
    height=2,
    font=("Arial", 11, "bold")
)
lbl1.grid(row=0, column=0, columnspan=2, sticky="nsew")

lbl2 = tk.Label(
    janela,
    text="Label 2",
    bg="green",
    fg="white",
    width=18,
    height=2,
    font=("Arial", 11, "bold")
)
lbl2.grid(row=0, column=2, columnspan=2, sticky="nsew")

lbl3 = tk.Label(
    janela,
    text="Label 3",
    bg="blue",
    fg="white",
    width=18,
    height=2,
    font=("Arial", 11, "bold")
)
lbl3.grid(row=0, column=4, columnspan=2, sticky="nsew")

lbl4 = tk.Label(
    janela,
    text="Label 4",
    bg="brown",
    fg="white",
    width=18,
    height=2,
    font=("Arial", 11, "bold")
)
lbl4.grid(row=1, column=2, columnspan=4, sticky="nsew")

lbl5 = tk.Label(
    janela,
    text="Label 5",
    bg="lightblue",
    fg="white",
    width=18,
    height=2,
    font=("Arial", 11, "bold")
)
lbl5.grid(row=2, column=0, columnspan=4, sticky="nsew")

lbl6 = tk.Label(
    janela,
    text="Label 6",
    bg="orange",
    fg="white",
    width=18,
    height=4,
    font=("Arial", 11, "bold")
)
lbl6.grid(row=2, column=4, columnspan=2, rowspan=2, sticky="nsew")

lbl7 = tk.Label(
    janela,
    text="Label 7",
    bg="lightgreen",
    fg="white",
    width=18,
    height=2,
    font=("Arial", 11, "bold")
)
lbl7.grid(row=3, column=0, columnspan=4, sticky="nsew")

# Loop principal
janela.mainloop()