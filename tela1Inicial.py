from cProfile import label
from tkinter import *
from tkinter import messagebox
import time
from bancoDeDadosP import *

banco = Banco()


class Tela1:
    def __init__(self):
        self.janela1 = Tk()
        self.janela1.title("Amilton Carvalho")
        self.janela1.geometry("430x600")
        self.janela1.config(bg="black")

        banco.createTabelas()

        self.frame1 = Frame(self.janela1, bg="black")
        self.frame1.pack(padx=60, pady=20)

        self.logo = PhotoImage(file="Imagens\\amiltonCarvalhoLogo.png")
        self.fotoLogo = Label(self.frame1, image=self.logo, bd=0)
        self.fotoLogo.grid(row=0, pady=20)

        self.frame2 = Frame(self.frame1, bg="black")
        self.frame2.grid(row=1, column=0)

        self.txtUsuario = Label(self.frame2, text="Usuario:", font=(
            "Calibri", 15, "bold"), bg="black", fg="white")
        self.txtUsuario.grid(row=1, sticky="w", pady=5)

        self.digUsuario = Entry(self.frame2, font=("Calibri", 15), width=30)
        self.digUsuario.grid(row=2, pady=5)

        self.txtSenha = Label(self.frame2, text="Senha:", font=(
            "Calibri", 15, "bold"), bg="black", fg="white")
        self.txtSenha.grid(row=3, sticky="w", pady=5)

        self.digSenha = Entry(self.frame2, show="*",
                              font=("Calibri", 15), width=30)
        self.digSenha.grid(row=4, pady=5)
        self.digSenha.bind('<Return>', self.verificaSenhaCaller)

        self.botaoEntrar = Button(self.frame2, text="Entrar", command=self.verificaSenha, bg="red", fg="white", font=(
            "Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=10)
        self.botaoEntrar.grid(row=5, sticky="w", pady=40)

        self.carro = PhotoImage(file="Imagens\\carro.png")
        self.fotoCarro = Label(self.janela1, image=self.carro, bd=0)
        self.fotoCarro.place(x=210, y=435)

        mainloop()

    def verificaSenhaCaller(self, event):
        return self.verificaSenha()

    def verificaSenha(self):
        usuario = self.digUsuario.get()
        senha = self.digSenha.get()
        if usuario == "admin" and senha == "123":
            self.janela1.destroy()
            time.sleep(0.1)
            from tela2Gerente import Tela2
            Tela2()
        elif usuario == "mec" and senha == "123":
            self.janela1.destroy()
            time.sleep(0.1)
            from tela3Mecanico import Tela3
            Tela3()
        elif usuario == "recep" and senha == "123":
            self.janela1.destroy()
            time.sleep(0.1)
            from tela4Recepcionista import Tela4
            Tela4()
        else:
            self.digSenha.delete(0, END)
            messagebox.showwarning("Error", "senha e/ou usuário Ínvalidos")


Tela1()
