from tkinter import *
from tkinter.ttk import Treeview
from posicao import centralizar
import csv

jan = Tk()

jan.iconbitmap("cinel.ico")

jan.title("Gestão de clientes")
jan.geometry(centralizar(jan, 700, 400))
jan.resizable(0, 0)

f1 = Frame(jan)
f1.pack()

f2 = Frame(jan)
f2.pack()


# ==========================================================
# F1 - Treeview + Scroll vertical
# ==========================================================

tree = Treeview(
    f1,
    columns=("Nome", "Morada", "Zona"),
    show="headings"
)

tree.grid(row=0, column=0)

# Criar as colunas
tree.heading("Nome", text="Nome")
tree.heading("Morada", text="Morada")
tree.heading("Zona", text="Zona")

# Largura das colunas
tree.column("Nome", width=180)
tree.column("Morada", width=300)
tree.column("Zona", width=180)


# Scroll vertical
scroll = Scrollbar(
    f1,
    orient=VERTICAL,
    command=tree.yview
)

scroll.grid(row=0, column=1, sticky=NS)

tree.configure(
    yscrollcommand=scroll.set
)


# ==========================================================
# FUNÇÕES DOS BOTÕES
# ==========================================================

# Botão 1 - Carregar dados
def carregar_dados():

    tree.delete(*tree.get_children())

    with open("dados.csv", "r", encoding="utf-8-sig", newline="") as ficheiro:

        leitor = csv.DictReader(ficheiro)

        for linha in leitor:

            tree.insert(
                "",
                END,
                values=(
                    linha["Nome"],
                    linha["Morada"],
                    linha["Zona"]
                )
            )


# Botão 2 - Limpar tudo
def limpar_tudo():

    tree.delete(*tree.get_children())


# Botão 3 - Eliminar registro selecionado
def eliminar_registro():

    selecionados = tree.selection()

    for item in selecionados:
        tree.delete(item)


# ==========================================================
# F2 - Botões
# ==========================================================

bcarrega = Button(
    f2,
    text="Carrega\nDados",
    command=carregar_dados
)

blimpa = Button(
    f2,
    text="Limpar\nTudo",
    command=limpar_tudo
)

bapaga = Button(
    f2,
    text="Elimina\nRegistro",
    command=eliminar_registro
)

bcarrega.grid(
    row=0,
    column=0,
    padx=10
)

blimpa.grid(
    row=0,
    column=1,
    padx=10
)

bapaga.grid(
    row=0,
    column=2,
    padx=10
)


jan.mainloop()