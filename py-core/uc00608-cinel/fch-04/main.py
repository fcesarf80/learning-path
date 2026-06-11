import tkinter as tk

janela = tk.Tk()

janela.title("Gestor de Biblioteca")
janela.geometry("1200x700")
janela.configure(bg="white")


# MENU LATERAL
frame_menu = tk.Frame(
    janela,
    width=300,
    bg="#F5F7F7"
)

frame_menu.pack(
    side="left",
    fill="y"
)

titulo = tk.Label(
    frame_menu,
    text="📚 Biblioteca",
    font=("Segoe UI", 16, "bold"),
    bg="#F5F7F7"
)

titulo.pack(
    pady=20
)

menus = [
    "Dashboard",
    "Livros",
    "Utilizadores",
    "Empréstimos",
    "Devoluções",
    "Ativos",
    "Histórico",
    "CSV",
    "Estatísticas"
]

for item in menus:
    botao = tk.Button(
        frame_menu,
        text=item,
        anchor="w",
        relief="flat",
        bg="#F5F7F7",
        padx=15
    )

    botao.pack(
        fill="x",
        pady=2
    )


# ÁREA PRINCIPAL
frame_conteudo = tk.Frame(
    janela,
    bg="white"
)

frame_conteudo.pack(
    side="right",
    expand=True,
    fill="both"
)

cabecalho = tk.Frame(
    frame_conteudo,
    bg="white",
    height=80
)

cabecalho.pack(
    fill="x"
)

titulo_dashboard = tk.Label(
    cabecalho,
    text="Dashboard",
    font=("Segoe UI", 20, "bold"),
    bg="white"
)

# DASHBOARD

titulo_dashboard.pack(
    anchor="w",
    padx=30,
    pady=20
)

frame_cards = tk.Frame(
    frame_conteudo,
    bg="white"
)

frame_cards.pack(
    fill="x",
    padx=30,
    pady=20
)

frame_cards = tk.Frame(
    frame_conteudo,
    bg="white"
)

frame_cards.pack(
    anchor="w",
    padx=30,
    pady=20
)

criar_card(frame_cards, "128", "Livros")
criar_card(frame_cards, "56", "Utilizadores")
criar_card(frame_cards, "18", "Empréstimos")
criar_card(frame_cards, "325", "Histórico")



def criar_card(parent, numero, texto):

    card = tk.Frame(
        parent,
        bg="white",
        bd=1,
        relief="solid",
        width=180,
        height=100
    )

    card.pack_propagate(False)

    card.pack(
        side="left",
        padx=10
    )

    lbl_numero = tk.Label(
        card,
        text=numero,
        font=("Segoe UI", 20, "bold"),
        bg="white"
    )

    lbl_numero.pack(
        pady=(15, 5)
    )

    lbl_texto = tk.Label(
        card,
        text=texto,
        font=("Segoe UI", 10),
        bg="white"
    )

    lbl_texto.pack()

janela.mainloop()