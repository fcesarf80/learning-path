from tkinter import *
from tkinter.messagebox import *
import ligacao as liga

###########################
#Variaveis
fonte = ("Arial", 14)

###########################
##Funções

def entrar():
    con = liga.ligacao()
    if not con:
        showerror("Error, " \
        "message:Não foi ossivel ligar o servidorde bds")

        return
    cursos = con.curso()
    cursos.execute("use login;")
    nome = enome.get()
    nome = epass.get()
    sql = f"""

            selct *
            from utilizador
            where none = '{nome}' and senha = {senha}";
        """
    cursor.execute(sql)
   

    resposta = cursos.fetchone()
    if resposta:
        showinfo(title:"Informação",
        message:f"Username
        print(resposta)
    else:
        print("Não existe utilizadores registrados com essas credenciais")

def novo(): 

    def gravar():
        pass
    
    jan2 = Toplevel()
    lnome2 = Label(jan2, text="Username:", font=fonte)
    lnome2 = Label(jan2, text="Password:", font=fonte)
    enome2 = Entry(jan2, font=fonte)
    enome2 = Entry(jan2, font=fonte)
    bgravar = Button(jan2, text="Gravar", font=font, command=gravar)

    jan2 = Toplevel()
    lnome2.grid(row=0, column=0)
    lnome2.grid(row=0, column=1)
    enome2.grid(row=0, column=2)
    enome2.grid(row=0, column=3)



###########################
jan = Tk()
jan.title("Sistema de login")
jan.geometry("400x300")
jan.iconbitmap("cinel.ico")

frame = Frame(jan)
frame.pack(expand=True)

#frame
lnome = label(frame, text="Username:", font=fonte)
lpass = label(frame, text="Password:", font=fonte)
enome = Entry(frame, font=fonte)
epass = Entry(frame, font=fonte, show="●")

lnome.grid(row=0, colum=0,pady=10)
lpass.grid(row=1, colum=0)
enome.grid(row=0, colum=1)
epass.grid(row=1, colum=1)
enome.focus()


blogin = Button(frame,
                text="Login",
                font=fonte,
                bg="grenn",
                fg='white',
                width=7,
                bd=4, 
                command=entrar
                )

bsair = Button(frame,
               text="Login",font=fonte,bg="red",
               fg='white',
               width=7,
               bd=4,
               command=lambda:jan.destroy
               )

blogin.grid(row=2, column=0, pad=10)
bsair.grid(row=2, column=1)



jan.mainloop()