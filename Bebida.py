from Item import Item

class Bebida(Item):
    def __init__(self,nome,descricao,estoque,preco,tamanho):
        super().__init__(nome,descricao,estoque,preco)
        self.tamanho = tamanho

    def set_tamanho(self,tamanho):
        self.tamanho = tamanho
    
    def get_tamanho(self)
        return tamanho

    def __str__(self)
    string = super().__str__()
    string = string.removesuffix(f"\nPor {self.preco}R$")
    string = string + f"Tamanho: {self.tamanho}ml \nPor {self.preco}R$"
    return string