# ==================================================
# IMPORTS
# ==================================================

import tkinter as tk


# ==================================================
# FUNÇÕES
# ==================================================

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

   # endfuncao

def criar_botao_dashboard(parent, texto):

    botao = tk.Button(
        parent,
        text=texto,
        width=18,
        height=3,
        bg="#E8F5E9",
        relief="solid",
        bd=1
    )

    return botao


# ==================================================
# JANELA PRINCIPAL
# ==================================================

janela = tk.Tk()

janela.title("Gestor de Biblioteca")
janela.geometry("1200x700")
janela.configure(bg="white")

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
# ==================================================
# MENU LATERAL
# ==================================================

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


# ==================================================
# DASHBOARD
# ==================================================

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
    anchor="w",
    padx=30,
    pady=20
)

frame_acesso = tk.Frame(
    frame_conteudo,
    bg="white"
)

frame_acesso.pack(
    anchor="w",
    padx=30
)

# ==================================================
# CARDS
# ==================================================

criar_card(frame_cards, "128", "Livros")
criar_card(frame_cards, "56", "Utilizadores")
criar_card(frame_cards, "18", "Empréstimos")
criar_card(frame_cards, "325", "Histórico")

# ==================================================
# DASHBOARD - CABEÇALHO
# ==================================================



# ==================================================
# DASHBOARD - ACESSO RÁPIDO
# ==================================================

titulo_acesso = tk.Label(
    frame_conteudo,
    text="Acesso Rápido",
    font=("Segoe UI", 14, "bold"),
    bg="white"
)

titulo_acesso.pack(
    anchor="w",
    padx=30,
    pady=(20,10)
)

linha1 = tk.Frame(
    frame_acesso,
    bg="white"
)

linha1.pack(
    pady=5
)

linha2 = tk.Frame(
    frame_acesso,
    bg="white"
)

linha2.pack(
    pady=5
)


criar_botao_dashboard(linha1, "Adicionar Livro").pack(side="left", padx=5)
criar_botao_dashboard(linha1, "Pesquisar Livro").pack(side="left", padx=5)
criar_botao_dashboard(linha1, "Empréstimo").pack(side="left", padx=5)
criar_botao_dashboard(linha1, "Devolução").pack(side="left", padx=5)

criar_botao_dashboard(linha2, "Utilizadores").pack(side="left", padx=5)
criar_botao_dashboard(linha2, "Ativos").pack(side="left", padx=5)
criar_botao_dashboard(linha2, "Histórico").pack(side="left", padx=5)
criar_botao_dashboard(linha2, "Estatísticas").pack(side="left", padx=5)


# ==================================================
# ATIVIDADE RECENTE
# ==================================================


titulo_atividade = tk.Label(
    frame_conteudo,
    text="Atividade Recente",
    font=("Segoe UI", 14, "bold"),
    bg="white"
)

titulo_atividade.pack(
    anchor="w",
    padx=30,
    pady=(25,10)
)

frame_atividade = tk.Frame(
    frame_conteudo,
    bg="white",
    bd=1,
    relief="solid"
)

frame_atividade.pack(
    fill="x",
    padx=30
)

atividades = [
    "📚 Livro 'O Hobbit' adicionado",
    "👤 Utilizador 'Maria Santos' criado",
    "📤 Empréstimo realizado",
    "📥 Devolução registada"
]

for atividade in atividades:

    lbl = tk.Label(
        frame_atividade,
        text=atividade,
        bg="white",
        anchor="w",
        font=("Segoe UI", 10)
    )

    lbl.pack(
        anchor="w",
        padx=15,
        pady=5
    )


janela.mainloop()