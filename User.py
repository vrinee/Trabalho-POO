from datetime import datetime

def calcular_idade(dataNasc):
    dataNasc = datetime.strptime(dataNasc, "%d/%m/%Y")
    hoje = datetime.today()
    idade = hoje - dataNasc
    idade = datetime.fromTimeStamp(idade.total_seconds())
    idade = idade.year - 1970
    return idade
class Carrinho:
    def __init__(self):
        self.itens = []
    
    def subtotal(self):
        sub = 0
        for i in self.itens:
            sub += i[0].get_preco() * i[1]
        return sub
    
    def vender(self):
        valor = 0
        for i in self.itens:
            valor += i[0].vender(i[1])
        self.itens = []
        return valor

    def __str__(self):
        result = ""
        for i in self.itens:
            result = result+ "-"*30 + f"\n{i[1]}x {i[0]}\nPreço subtotal: {i[0].get_preco()*i[1]}\n"


class User:

    def __init__(self,nome,cpf,email,telefone,dataNasc,senha):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.dataNasc = dataNasc
        self.senha = senha
        self.carrinho = Carrinho()

    def set_nome(self,nome):
        self.nome = nome
    
    def set_email(self,email):
        self.email = email
    
    def set_telefone(self,telefone):
        self.telefone = telefone

    def set_senha(self,senha):
        self.senha = senha

    def get_idade(self):
        return calcular_idade(self.dataNasc)
    
    def get_nome(self):
        return self.nome
    
    def get_cpf(self):
        return self.cpf
    
    def get_email(self):
        return self.email

    def get_telefone(self):
        return self.telefone
    
    def get_dataNasc(self):
        return self.dataNasc
    
    def get_senha(self):
        return self.senha

    def excluir_user(self,users):
        for user in users:
            if user.get_cpf() == self.cpf:
                users.remove(user)
                print("Usuário excluído com sucesso!")
                return
    
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}, Telefone: {self.telefone}, Data de Nascimento: {self.dataNasc}"