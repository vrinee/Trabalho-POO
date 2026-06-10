#inserir outras classes que serão manipuladas pelo admin

class Admin:
    def __init__(self,nome,senha):
        self.nome = nome
        self.senha = senha

    def get_nome(self):
        return self.nome
    
    def get_senha(self):
        return self.senha
    
    def add_user(self,users):
        from controlFuncs import cadastrar_usuario
        user = cadastrar_usuario()
        users.append(user)
        print("Usuário cadastrado com sucesso!")

    def excluir_user(self,users):
        cpf = input("Digite o CPF do usuário que deseja excluir: ")
        for user in users:
            if user.get_cpf() == cpf:
                users.remove(user)
                print("Usuário excluído com sucesso!")
                return
        print("Usuário não encontrado!")

    def __str__(self):
        return f"Nome: {self.nome} Senha: {self.senha}"
