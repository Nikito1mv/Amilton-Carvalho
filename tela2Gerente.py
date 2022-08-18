from tkinter import *
from time import *


class Tela2:
    def __init__(self):

        self.janela2 = Tk()
        self.janela2.title("Amilton Carvalho")
        self.janela2.geometry("300x530")
        self.janela2.config(bg="black")

        self.frame1 = Frame(self.janela2, bg="black")
        self.frame1.pack()

        self.logo = PhotoImage(file="Imagens\\logoGerente.png")
        self.foto = Label(self.frame1, image=self.logo, bd=0)
        self.foto.grid(row=0)

        self.botao1 = Button(self.frame1, text="Funcionários", command=self.irFuncionarios, bg="red", fg="white", font=(
            "Calibri", 15, "bold"), relief=RAISED, overrelief=RIDGE, width=15)
        self.botao1.grid(row=1, padx=10, pady=15)

        self.botao2 = Button(self.frame1, text="Orçamentos",   command=self.irOrcamentos,   bg="red", fg="white", font=(
            "Calibri", 15, "bold"), relief=RAISED, overrelief=RIDGE, width=15)
        self.botao2.grid(row=2, padx=10, pady=15)

        self.botao3 = Button(self.frame1, text="Serviços",     command=self.irServicos,     bg="red", fg="white", font=(
            "Calibri", 15, "bold"), relief=RAISED, overrelief=RIDGE, width=15)
        self.botao3.grid(row=3, padx=10, pady=15)

        mainloop()

    def irFuncionarios(self):
        from tela21Funcionarios import Tela21
        return Tela21()

    def irOrcamentos(self):
        from tela22Orcamentos import Tela22
        Tela22()

    def irServicos(self):
        from tela23Servicos import Tela23
        Tela23()


#minhaTela = Tela2()
