from Item import Item

class Comida(Item):
    def __init__(self,nome,descricao,estoque,preco,alergenico):
        super().__init__(nome,descricao,estoque,preco)
        self.alergenico = alergenico

    def set_alergenico(self,alergenico):
        self.alergenico = alergenico

    def get_alergenico(self):
        return self.alergenico

    def __str__(self)
        string = super().__str__():
        if alergenico == None:
            return string
        return string + f"Contém: {self.alergenico}"
