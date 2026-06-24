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
    
    def add_item(self,item,qntd):
        for i in self.itens:
            if i[0] == item:
                i[1] += qntd
                return
        self.itens.append([item,qntd])
        print("Item adicionado com sucesso")

    def remove_item(self,item,qntd):
        for i in self.itens:
            if i[0] == item:
                if i[1] - qntd < 0:
                    print("Quantidade inválida")
                    return
                if i[1] - qntd == 0:
                    self.itens.remove(i)
                    print("Item removido com sucesso")
                    return
                i[1] = i[1] - qntd
                print("Quantidade deduzida com sucesso")
                return

    
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
        result = result + f"Subtotal: {self.subtotal()}"
        return result


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

    def show_carrinho(self):
        if len(self.carrinho.itens) == 0:
        print(self.carrinho)

    def get_carrinho_subtotal(self):
        return self.carrinho.subtotal()

    def add_item(self,itens):
        nome = input("Digite o nome do item a adicionar: ")
        qntd = int(input("Digite a quantidade: "))

        for i in itens:
            if nome == i.get_nome():
                if i.get_disponivel(qntd):
                    self.carrinho.add_item(i,qntd)
                    return
                print("Não há estoque suficiente.")
        print("Item não foi encontrado")

    def remove_item(self,itens):
        nome = input("Digite o item a deletar: ")
        qntd = int(input("Digite a quantidade: "))

        for i in itens:
            if i.get_nome() == nome:
                self.carrinho.remove_item(i,qntd)
                return
    
    def comprar_carrinho(self):
        return self.carrinho.vender()

    def excluir_user(self,users):
        for user in users:
            if user.get_cpf() == self.cpf:
                users.remove(user)
                print("Usuário excluído com sucesso!")
                return
    
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}, Telefone: {self.telefone}, Data de Nascimento: {self.dataNasc}"