from tkinter import *
from time import *


class Tela4:
    def __init__(self):
        self.janela4 = Tk()
        self.janela4.title("Amilton Carvalho")
        self.janela4.geometry("300x530")
        self.janela4.config(bg="black")

        self.frame1 = Frame(self.janela4, bg="black")
        self.frame1.pack()

        self.logo = PhotoImage(file="Imagens\\logoRecepcionista.png")
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
        from tela41Orcamentos import Tela41
        Tela41()

    def irServicos(self):
        from tela42Servicos import Tela42
        Tela42()

# Tela4()
