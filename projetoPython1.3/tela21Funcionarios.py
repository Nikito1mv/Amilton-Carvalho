from tkinter import *
from tkinter import ttk
from bancoDeDadosP import *
from tkinter import messagebox

banco = Banco()


class Tela21:
    def __init__(self):

        self.janela21 = Tk()

        # "Configurando_Janela=============================================================="

        self.janela21.title("Amilton Carvalho")
        self.janela21.geometry("1366x768")
        self.janela21.config(bg="black")
        self.janela21.state("zoomed")

        # "Tipando_Variáveis=============================================================="

        # Tipando as variaveis

        self.digNome = StringVar()
        self.digUsuario = StringVar()
        self.digTelefone = StringVar()
        self.digEmail = StringVar()
        self.digSenha = StringVar()
        self.digEndereco = StringVar()

        # "Janela_Tkinter=============================================================="

        self.frame1 = Frame(self.janela21, bg="black")
        self.frame1.grid(row=0, column=0, padx=5, sticky="n")

        self.frame2 = Frame(self.janela21, bg="black")
        self.frame2.grid(row=0, column=1)

        # "Frame_Título=============================================================="

        self.titulo = Label(master=self.frame1, text="Gerenciamento de Funcionários",
                            bg="black", fg="white", font=("Calibri", 18, "bold"), width=25)
        self.titulo.grid(row=0, padx=20, pady=10)

        # "Frame_Logo=============================================================="

        #self.imgLogo = PhotoImage(file="amiltonLOGO\\amiltonIMG.png")

        #self.logoIMG = Label(master=self.frame1, image=self.imgLogo, bg="black")
        #self.logoIMG.grid(row=1, column=0, pady=30)

        # "Frame_Dados=============================================================="

        self.frameDados = Frame(master=self.frame1, bg="black")
        self.frameDados.grid(row=2, column=0)

        self.labNome = Label(master=self.frameDados, text="Nome:",
                             bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labNome.grid(row=0, column=0, padx=10, pady=10)

        self.entNome = Entry(master=self.frameDados,
                             textvariable=self.digNome, font=("Calibri", 13))
        self.entNome.grid(row=0, column=1, padx=10, pady=10)

        self.labUsuario = Label(master=self.frameDados, text="Usuário:",
                                bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labUsuario.grid(row=1, column=0, padx=10, pady=10)

        self.entUsuario = Entry(
            master=self.frameDados, textvariable=self.digUsuario, font=("Calibri", 13))
        self.entUsuario.grid(row=1, column=1, padx=10, pady=10)

        self.labTelefone = Label(master=self.frameDados, text="Telefone:",
                                 bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labTelefone.grid(row=2, column=0, padx=10, pady=10)

        self.entTelefone = Entry(
            master=self.frameDados, textvariable=self.digTelefone, font=("Calibri", 13))
        self.entTelefone.grid(row=2, column=1, padx=10, pady=10)

        self.labEmail = Label(master=self.frameDados, text="E-mail:",
                              bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labEmail.grid(row=3, column=0, padx=10, pady=10)

        self.entEmail = Entry(master=self.frameDados,
                              textvariable=self.digEmail, font=("Calibri", 13))
        self.entEmail.grid(row=3, column=1, padx=10, pady=10)

        self.labSenha = Label(master=self.frameDados, text="Senha:",
                              bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labSenha.grid(row=4, column=0, padx=10, pady=10)

        self.entSenha = Entry(master=self.frameDados,
                              textvariable=self.digSenha, font=("Calibri", 13))
        self.entSenha.grid(row=4, column=1, padx=10, pady=10)

        self.labEndereco = Label(master=self.frameDados, text="Endereço:",
                                 bg="black", fg="white", font=("Calibri", 13, "bold"))
        self.labEndereco.grid(row=5, column=0, padx=10, pady=10)

        self.entEndereco = Entry(
            master=self.frameDados, textvariable=self.digEndereco, font=("Calibri", 13))
        self.entEndereco.grid(row=5, column=1, padx=10, pady=10)

        # self.digId = Entry(master=self.frameDados)

        # "Frame_Botões=============================================================="

        self.frameBotoes = Frame(master=self.frame2, bg="black")
        self.frameBotoes.grid(row=0, column=0, pady=30)

        self.botaoProcurar = Button(master=self.frameBotoes, text="Buscar", command=self.buscarFuncionarios, bg="red", fg="white", font=(
            "Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=10)
        self.botaoProcurar.grid(row=0, column=0, padx=10, pady=10)

        self.botaoVer = Button(master=self.frameBotoes, text="Exibir Todos", command=self.exibirTodos, bg="red", fg="white", font=(
            "Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=12)
        self.botaoVer.grid(row=0, column=1, padx=10, pady=10)

        self.botaoInserir = Button(master=self.frameBotoes, text="Adicionar Funcionario", command=self.adicionarFuncionarios,
                                   bg="red", fg="white", font=("Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=20)
        self.botaoInserir.grid(row=0, column=2, padx=10, pady=10)

        self.botaoAtualizar = Button(master=self.frameBotoes, text="Alterar Cadastro", command=self.editarFuncionarios,
                                     bg="red", fg="white", font=("Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=17)
        self.botaoAtualizar.grid(row=0, column=3, padx=10, pady=10)

        self.botaoDeletar = Button(master=self.frameBotoes, text="Remover Funcionario", command=self.deletarFuncionarios,
                                   bg="red", fg="white", font=("Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=20)
        self.botaoDeletar.grid(row=0, column=4, padx=10, pady=10)

        # "Frame_Botão_Limpar=============================================================="

        self.frameLimpar = Frame(master=self.frame1, bg="black")
        self.frameLimpar.grid(row=3, column=0)

        self.botaoLimpar = Button(master=self.frameLimpar, text="Limpar Campos", command=self.limparCampos, bg="red", fg="white", font=(
            "Calibri", 13, "bold"), relief=RAISED, overrelief=RIDGE, width=15)
        self.botaoLimpar.grid(row=1, column=2, padx=10, pady=40)

        # "Frame_Treeview=============================================================="

        self.frameTabela = Frame(master=self.frame2)
        self.frameTabela.grid(row=1, column=0)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=(
            "Calibri", 13), rowheight=50)
        self.style.configure("mystyle.Treeview.Heading",
                             font=("Calibri", 13, "bold"))

        self.tv = ttk.Treeview(master=self.frameTabela, columns=(
            1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")

        self.tv.heading("1", text="ID")
        self.tv.heading("2", text="Nome")
        self.tv.heading("3", text="Usuário")
        self.tv.heading("4", text="Telefone")
        self.tv.heading("5", text="E-mail")
        self.tv.heading("6", text="Senha")
        self.tv.heading("7", text="Endereço")
        self.tv.heading("8", text="")

        self.tv.column("1", width=40)
        self.tv.column("2", width=200)
        self.tv.column("3", width=100)
        self.tv.column("4", width=150)
        self.tv.column("5", width=200)
        self.tv.column("6", width=100)
        self.tv.column("7", width=180)
        self.tv.column("8", width=0)

        self.tv["show"] = "headings"
        self.tv.bind("<1>", self.pegarDados)

        self.tv.grid(row=0, column=0)

        self.scroolTv = Scrollbar(master=self.frameTabela, orient="vertical")
        self.tv.configure(yscroll=self.scroolTv.set)
        self.scroolTv.grid(row=0, column=1)

        self.exibirTodos()
        mainloop()

    def limparCampos(self):
        self.entNome.delete(0, END)
        self.entUsuario.delete(0, END)
        self.entTelefone.delete(0, END)
        self.entEmail.delete(0, END)
        self.entSenha.delete(0, END)
        self.entEndereco.delete(0, END)

    def adicionarFuncionarios(self):
        if (self.entNome.get() == "" or self.entUsuario.get() == "" or self.entTelefone.get() == "" or self.entEmail.get() == "" or self.entSenha.get() == "" or self.entEndereco.get() == ""):
            messagebox.showwarning(
                "Erro na entrada", "Por favor, preencha todos os campos")
        else:
            banco.insertFuncionarios(self.entNome.get(), self.entUsuario.get(), self.entTelefone.get(
            ), self.entEmail.get(), self.entSenha.get(), self.entEndereco.get())
            self.exibirTodos()
            self.limparCampos()

    def exibirTodos(self):
        self.tv.delete(*self.tv.get_children())
        for i in banco.viewFuncionarios():
            self.tv.insert("", END, values=i)

    def pegarDados(self, event):
        # pega a linha da tabela onde o ponteiro do mouse está quando o evento disparado
        #self.linhaSelecionada = self.tv.focus()
        self.linhaSelecionada = self.tv.selection()
        self.limparCampos()
        # pega o item(funcionário) que está nessa linha da tabela e atribue a uma variavel(self.dados)
        self.dados = self.tv.item(self.linhaSelecionada)
        # torna a variavel global para usala futuramente
        self.linha = self.dados["values"]  # valores da linha selecionada
        # self.digId.set(self.linha[0])
        # self.digNome.set(self.linha[1])
        # self.digUsuario.set(self.linha[2])
        # self.digTelefone.set(self.linha[3])
        # self.digEmail.set(self.linha[4])
        # self.digSenha.set(self.linha[5])
        # self.digEndereco.set(self.linha[6])
        self.entNome.insert(INSERT, self.linha[1])
        self.entUsuario.insert(INSERT, self.linha[2])
        self.entTelefone.insert(INSERT, self.linha[3])
        self.entEmail.insert(INSERT, self.linha[4])
        self.entSenha.insert(INSERT, self.linha[5])
        self.entEndereco.insert(INSERT, self.linha[6])
        print(self.linha[1])
        print(self.linha[2])
        print(self.linha[3])
        print(self.linha[4])
        print(self.linha[5])

    def editarFuncionarios(self):
        if (self.entNome.get() == "" or self.entUsuario.get() == "" or self.entTelefone.get() == "" or self.entEmail.get() == "" or self.entSenha.get() == "" or self.entEndereco.get() == ""):
            messagebox.showwarning(
                "Erro na entrada", "Por favor, preencha todos os campos")
        else:
            banco.updateFuncionarios(self.linha[0], self.entNome.get(), self.entUsuario.get(
            ), self.entTelefone.get(), self.entEmail.get(), self.entSenha.get(), self.entEndereco.get())
            self.limparCampos()
            self.exibirTodos()

    def deletarFuncionarios(self):
        banco.deleteFuncionarios(self.linha[0])
        self.limparCampos()
        self.exibirTodos()
        pass

    def buscarFuncionarios(self):
        self.tv.delete(*self.tv.get_children())
        linhas = banco.searchFuncionarios(self.entNome.get(), self.entUsuario.get(
        ), self.entTelefone.get(), self.entEmail.get(), self.entSenha.get(), self.entEndereco.get())
        for i in linhas:
            self.tv.insert("", END, values=i)


    # def execute(self):
#myTela = Tela21()
# return myTela.janela21.mainloop()
