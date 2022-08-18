from tkinter import *
from time import *


class Tela3:
    def __init__(self):
        self.janela3 = Tk()
        self.janela3.title("Amilton Carvalho")
        self.janela3.geometry("300x530")
        self.janela3.config(bg="black")

        self.frame1 = Frame(self.janela3, bg="black")
        self.frame1.pack()

        self.logo = PhotoImage(file="Imagens\\logoMecanico.png")
        self.foto = Label(self.frame1, image=self.logo, bd=0)
        self.foto.grid(row=0)

        self.botao1 = Button(self.frame1, text="Orçamentos", command=self.irOrcamentos,  bg="red", fg="white", font=(
            "Calibri", 15, "bold"), relief=RAISED, overrelief=RIDGE, width=15)
        self.botao1.grid(row=1, padx=10, pady=15)

        self.botao2 = Button(self.frame1, text="Serviços",   command=self.irServicos,    bg="red", fg="white", font=(
            "Calibri", 15, "bold"), relief=RAISED, overrelief=RIDGE, width=15)
        self.botao2.grid(row=2, padx=10, pady=15)

        mainloop()

    def irOrcamentos(self):
        from tela31Orcamento import Tela31
        Tela31()

    def irServicos(self):
        from tela32Servicos import Tela32
        Tela32()

# Tela3()
