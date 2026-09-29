from tkinter import *
from tkinter import ttk

jan = Tk()
jan.title("Exemplo de Treeview")
jan.geometry("700x400")

#criar estrutura
tree = ttk.Treeview(jan, columns=("A", "B", "C"), show="headings")

#criar as colunas
tree.heading("A", text="Nome")
tree.heading("B", text="Morada")
tree.heading("C", text="Zona do país")

#inserir registros
tree.insert("", END, values=("Joaquim","Gondomar","Norte"))
tree.insert("", END, values=("Anabela","Lisboa","Centro"))
tree.insert("", 1, values=("Teixeira","Faro","Sul"))


tree.pack()

def limpar():
    tree.delete(*tree.get_children())

def limpar1():
    print(tree.selection())
    print(tree.get_children())
    print(tree.item(tree.selection())["values"])
    
#Butões:
#Butão 1
b = Button(jan, text="Limpar", command=limpar)
b.pack()

#Butão 2
b1 = Button(jan, text="limpar 1", command=limpar1)
b1.pack()

jan.mainloop()