import tkinter as tk

janela = tk.Tk()
janela.title("Teste PNG")

try:
    img = tk.PhotoImage(file="img-milhouse.png")
    lbl = tk.Label(janela, image=img)
    lbl.pack()
    print("PNG carregado com sucesso!")
except Exception as erro:
    print("Erro:", erro)

janela.mainloop()