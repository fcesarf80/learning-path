import tkinter as tk

janela = tk.Tk()

janela.title("Turma da Edna Krabappel")
janela.geometry("1366x768")

label = tk.Label(
    janela,
    text="Tkinter funcionando!",
    font=("Arial", 24)
)

label.pack(pady=50)

janela.mainloop()