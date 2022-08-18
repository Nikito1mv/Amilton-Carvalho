import sqlite3

class Banco():

    def connect(self):
        self.conn = sqlite3.connect("bancoDeDados.db")
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def createTabelas(self):
        self.connect()
        # Tabela Funcionarios
        self.cursor.execute("CREATE TABLE IF NOT EXISTS funcionarios (id INTEGER PRIMARY KEY, nome TEXT, usuario TEXT, telefone TEXT, email TEXT, senha TEXT, endereco TEXT)")
        # Tabela Orçamentos
        self.cursor.execute("CREATE TABLE IF NOT EXISTS orcamentos (id INTEGER PRIMARY KEY, nome TEXT, placa TEXT, telefone TEXT, email TEXT, servico TEXT, valor TEXT)")
        # Tabela Serviços
        self.cursor.execute("CREATE TABLE IF NOT EXISTS servicos (id INTEGER PRIMARY KEY, nome TEXT, placa TEXT, telefone TEXT, email TEXT, servico TEXT, status TEXT)")
        self.conn.commit()
        self.disconnect()
    
    def insertFuncionarios(self, nome, usuario, telefone, email, senha, endereco):
        self.connect()
        self.cursor.execute("INSERT INTO funcionarios VALUES (NULL, ?, ?, ?, ?, ?, ?)", (nome, usuario, telefone, email, senha, endereco))
        self.conn.commit()
        self.disconnect()

    def insertOrcamentos(self, nome, placa, telefone, email, servico):
        self.connect()
        self.cursor.execute("INSERT INTO orcamentos VALUES (NULL, ?, ?, ?, ?, ?, NULL)", (nome, placa, telefone, email, servico))
        self.conn.commit()
        self.disconnect()

    def insertServicos(self, nome, placa, telefone, email, servico):
        self.connect()
        self.cursor.execute("INSERT INTO servicos VALUES (NULL, ?, ?, ?, ?, ?, NULL)", (nome, placa, telefone, email, servico))
        self.conn.commit()
        self.disconnect()

    def viewFuncionarios(self):
        self.connect()
        self.cursor.execute("SELECT * FROM funcionarios")
        linhas = self.cursor.fetchall()
        self.disconnect()
        return linhas

    def viewOrcamentos(self):
        self.connect()
        self.cursor.execute("SELECT * FROM orcamentos")
        linhas = self.cursor.fetchall()
        self.disconnect()
        return linhas

    def viewServicos(self):
        self.connect()
        self.cursor.execute("SELECT * FROM servicos")
        linhas = self.cursor.fetchall()
        self.disconnect()
        return linhas

    def searchFuncionarios(self, nome, usuario, telefone, email, senha, endereco):
        self.connect()
        self.cursor.execute("SELECT * FROM funcionarios WHERE nome=? OR usuario=? OR telefone=? OR email=? OR senha=? OR endereco=?", (nome, usuario, telefone, email, senha, endereco))
        linhas = self.cursor.fetchall()
        self.disconnect()
        return linhas

    def searchOrcamentos(self, nome, placa, telefone, email, servico):
        self.connect()
        self.cursor.execute("SELECT * FROM orcamentos WHERE nome=? OR placa=? OR telefone=? OR email=? OR servico=?", (nome, placa, telefone, email, servico))
        linhas = self.cursor.fetchall()
        self.disconnect()
        return linhas

    def searchServicos(self, nome, placa, telefone, email, servico):
        self.connect()
        self.cursor.execute("SELECT * FROM servicos WHERE nome=? OR placa=? OR telefone=? OR email=? OR servico=?", (nome, placa, telefone, email, servico))
        linhas = self.cursor.fetchall()
        self.disconnect()
        return linhas

    def searchOrcamentosM(self, nome, placa, servico):
        self.connect()
        self.cursor.execute("SELECT * FROM orcamentos WHERE nome=? OR placa=? OR servico=?", (nome, placa, servico))
        linhas = self.cursor.fetchall()
        self.disconnect()
        return linhas

    def searchServicosM(self, nome, placa, servico):
        self.connect()
        self.cursor.execute("SELECT * FROM servicos WHERE nome=? OR placa=? OR servico=?", (nome, placa, servico))
        linhas = self.cursor.fetchall()
        self.disconnect()
        return linhas
    
    def updateFuncionarios(self, id, nome, usuario, telefone, email, senha, endereco):
        self.connect()
        self.cursor.execute("UPDATE funcionarios SET nome=?, usuario=?, telefone=?, email=?, senha=?, endereco=? WHERE id=?", (nome, usuario, telefone, email, senha, endereco, id))
        self.conn.commit()
        self.disconnect()

    def updateOrcamentos(self, id, nome, placa, telefone, email, servico):
        self.connect()
        self.cursor.execute("UPDATE orcamentos SET nome=?, placa=?, telefone=?, email=?, servico=? WHERE id=?", (nome, placa, telefone, email, servico, id))
        self.conn.commit()
        self.disconnect()

    def updateServicos(self, id, nome, placa, telefone, email, servico):
        self.connect()
        self.cursor.execute("UPDATE servicos SET nome=?, placa=?, telefone=?, email=?, servico=? WHERE id=?", (nome, placa, telefone, email, servico, id))
        self.conn.commit()
        self.disconnect()

    def updateOrcamentosM(self, id, valor):
        self.connect()
        self.cursor.execute("UPDATE orcamentos SET valor=? WHERE id=?", (valor , id))
        self.conn.commit()
        self.disconnect()

    def updateServicosM(self, id):
        self.connect()
        self.cursor.execute("UPDATE servicos SET status='Concluído' WHERE id=?", (id))
        self.conn.commit()
        self.disconnect()
    
    def deleteFuncionarios(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id, ))
        self.conn.commit()
        self.disconnect()

    def deleteOrcamentos(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM orcamentos WHERE id = ?", (id, ))
        self.conn.commit()
        self.disconnect()

    def deleteServicos(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM servicos WHERE id = ?", (id, ))
        self.conn.commit()
        self.disconnect()

