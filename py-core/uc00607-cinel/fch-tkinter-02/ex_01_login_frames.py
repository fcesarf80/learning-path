"""
Exercício 01 - Login frames
Enunciado: Crie uma janela com o título “Frames” e altere o ícone ao seu gosto.
Em seguida, crie uma interface semelhante ao enunciado, sabendo que os objetos
gráficos estão dentro de duas frames, uma para os labels e entry e outra para
o botão “Login”. A janela deve ter dimensão 300x100 e deve arrancar centrada
no ecrã. O botão “Login” deverá validar as credenciais “admin” e “admin”
como password. Caso contrário, deverá apresentar uma mensagem de erro
“Credenciais inválidas” utilizando a messagebox.
"""
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

def validar_login():
    utilizador = ent_utilizador.get()
    password = ent_password.get()
    if utilizador == "admin" and password == "admin":
        messagebox.showinfo("Login", "Login efetuado com sucesso!")
    else:
        messagebox.showerror("Erro", "Credenciais inválidas")

# --- Janela principal ---
janela = tk.Tk()
janela.title("Frames")
janela.resizable(False, False)
00000
# Configuração de dimensões e centralização
largura_janela, altura_janela = 300, 150
largura_ecra = janela.winfo_screenwidth()
altura_ecra = janela.winfo_screenheight()
pos_x = (largura_ecra // 2) - (largura_janela // 2)
pos_y = (altura_ecra // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# --- Layout Superior (Login) ---
# Usamos PACK na janela principal
frame_superior = tk.Frame(janela)
frame_superior.pack(pady=10, padx=10, fill="x")

frame_campos = tk.Frame(frame_superior)
frame_campos.pack(side="left")

frame_botao = tk.Frame(frame_superior)
frame_botao.pack(side="right", padx=10)

# Dentro dos frames pequenos, podemos usar GRID à vontade
tk.Label(frame_campos, text="Utilizador:").grid(row=0, column=0, sticky="w", pady=2)
ent_utilizador = tk.Entry(frame_campos, width=20)
ent_utilizador.grid(row=0, column=1, pady=2)

tk.Label(frame_campos, text="Password:").grid(row=1, column=0, sticky="w", pady=2)
ent_password = tk.Entry(frame_campos, width=20, show="*")
ent_password.grid(row=1, column=1, pady=2)

btn_login = tk.Button(frame_botao, text="Login", width=10, command=validar_login)
btn_login.pack(pady=10)

# --- A SERPENTE ANIMADA ---
frames = []
try:
    caminho_gif = os.path.join(os.path.dirname(__file__), "snakepy.gif")
    img_gif = Image.open(caminho_gif)

    # Extrair frames
    try:
        while True:
            frames.append(ImageTk.PhotoImage(img_gif.copy().convert("RGBA")))
            img_gif.seek(len(frames))
    except EOFError:
        pass

    # SOLUÇÃO DO ERRO: Usar PACK em vez de GRID para combinar com o frame_superior
    lbl_snake = tk.Label(janela)
    lbl_snake.pack(side="bottom", pady=20) 

    def animar(quadro):
        lbl_snake.config(image=frames[quadro])
        proximo = (quadro + 1) % len(frames)
        janela.after(100, animar, proximo)

    if frames:
        animar(0)

except Exception as e:
    print(f"Erro na animação: {e}")

# --- Eventos finais ---
janela.bind("<Return>", lambda event: validar_login())
ent_utilizador.focus()
janela.mainloop()
