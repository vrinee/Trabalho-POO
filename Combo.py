

class Combo:
    def __init__(self,nome,descricao,valor,limiteDiario):
        self.nome = nome
        self.descricao = descricao
        self.preco = valor
        self.limiteDiario = limiteDiario
        self.itens = []

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_preco(self):
        return self.valor

    def set_preco(self, valor):
        self.preco = valor

    def get_limite_diario(self):
        return self.limiteDiario

    def get_disponivel(self,qntd):
        if self.limiteDiario < qntd:
            return False
        if self.get_estoque_itens():
            return True
        return False

    def set_limite_diario(self, limiteDiario):
        self.limiteDiario = limiteDiario

    def get_itens(self):
        return self.itens

    def set_itens(self, itens):
        self.itens = itens

    def get_estoque_itens(self,qntd = 1):
        for i in self.itens:
            if i[0].get_estoque() < i[1]*qntd:
                return False
        return True

    def add_item(self,item,qntd):
        self.itens.append([item,qntd])

    def vender(self,qntd):
        self.limiteDiario -= qntd
        for i in itens:
            i[0].set_estoque(i[0].get_estoque() - (qntd*i[1]))
        return self.valor * qntd


    def __str__(self):
        return f"{self.nome}: \n * {self.descricao}\nPor {self.valor}R$"