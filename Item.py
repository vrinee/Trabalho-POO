class Item:
    def __init__(self,nome,descricao,estoque,preco):
        self.nome = nome
        self.descricao = descricao
        self.estoque = estoque
        self.preco = preco

    def set_nome(self.nome):
        self.nome = nome

    def set_descricao(self,descricao):
        self.descricao = descricao

    def set_preco(self,preco):
        self.preco = preco

    def set_estoque(self,estoque):
        self.estoque = estoque

    def get_nome(self):
        return self.nome
    
    def get_descricao(self):
        return self.descricao

    def get_estoque(self):
        return self.estoque

    def get_preco(self):
        return self.preco

    def vender(self,qntd):
        self.estoque -= qntd
        return self.preco*qntd

    def __str__(self):
        return f"{self.nome}: \n * {self.descricao}\nPor {self.preco}R$"
