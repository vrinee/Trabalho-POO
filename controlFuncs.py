from User import User
from Admin import Admin

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    email = input("Digite o email do usuário: ")
    telefone = input("Digite o telefone do usuário: ")
    dataNasc = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
    senha = input("Digite a senha do usuário: ")
    return User(nome, cpf, email, telefone, dataNasc,senha)



def cadastrar_admin():
    nome = input("Digite o nome do admin: ")
    senha = input("Digite a senha do admin: ")
    return Admin(nome, senha)





def excluir_admin(admins,current_admin):
    nome = input("Digite o nome do admin que deseja excluir: ")
    for admin in admins:
        if admin.nome == nome:
            senha = input("Digite a senha do admin que deseja excluir: ")
            if admin.senha == senha:
                senha_atual = input("Digite a senha do admin atual para confirmar a exclusão: ")
                if senha_atual == current_admin.senha:
                    admins.remove(admin)
                    print("Admin excluído com sucesso!")
                    return
                print("Senha do admin atual incorreta! Exclusão cancelada.")
                return
            print("Senha do admin a ser excluído incorreta! Exclusão cancelada.")
            return
    print("Admin não encontrado!")

def listar_users(users):
    if not users:
        print("Nenhum usuário cadastrado.")
    else:
        print("\nLista de usuários:")
        for user in users:
            print(user)



def mudar_info_user(user):
    print("\nMenu de edição de informações do usuário:")
    print("1. Editar nome")
    print("2. Editar email")
    print("3. Editar telefone")
    print("4. Editar senha")
    print("5. Voltar")
    op = input("Digite a opção desejada: ")
    if op == "1":
        novo_nome = input("Digite o novo nome: ")
        user.set_nome(novo_nome)
        print("Nome atualizado com sucesso!")
    elif op == "2":
        novo_email = input("Digite o novo email: ")
        user.set_email(novo_email)
        print("Email atualizado com sucesso!")
    elif op == "3":
        novo_telefone = input("Digite o novo telefone: ")
        user.set_telefone(novo_telefone)
        print("Telefone atualizado com sucesso!")
    elif op == "4":
        nova_senha = input("Digite a nova senha: ")
        user.set_senha(nova_senha)
        print("Senha atualizada com sucesso!")
    elif op == "5":
        print("Voltando ao menu anterior...")
    else:
        print("Opção inválida! Tente novamente.")

def adm_menu(admins,users,current_admin):
    while True:
        print("\nMenu do Admin:")
        print("1. Cadastrar usuário")
        print("2. Excluir usuário")
        print("3. Excluir admin")
        print("4. Cadastrar admin")
        print("5. Editar usuário")
        print("6. Listar usuários")
        print("7. Sair")
        print()
        op = input("Digite a opção desejada: ")
        if op == "1":
            current_admin.add_user(users)
        elif op == "2":
            current_admin.excluir_user(users)
        elif op == "3":
            excluir_admin(admins,current_admin)
            print("Saindo do menu do admin...")
            break
        elif op == "4":
            admins.append(cadastrar_admin())
        elif op == "5":
            cpf = input("Digite o CPF do usuário que deseja editar: ")
            for user in users:
                if user.get_cpf() == cpf:
                    mudar_info_user(user)
                    break
            else:
                print("Usuário não encontrado!")
        elif op == "6":
            listar_users(users)
        elif op == "7":
            print("Saindo do menu do admin...")
            break
        else:
            print("Opção inválida! Tente novamente.")


def user_menu(users,current_user):
    while True:
        print("\nMenu do Usuário:")
        print("1. Editar informações")
        print("2. Exibir informações")
        print("3. Excluir conta")
        print("4. Sair")
        print()
        op = input("Digite a opção desejada: ")
        if op == "1":
            mudar_info_user(current_user)
        elif op == "2":
            print(current_user)
        elif op == "3":
            senha = input("Digite a senha para confirmar a exclusão da conta: ")
            if senha == current_user.get_senha():
                current_user.excluir_user(users)
                print("Saindo do menu do usuário...")
                break
            print("Senha incorreta! Exclusão cancelada.")
        elif op == "4":
            print("Saindo do menu do usuário...")
            break
        else:
            print("Opção inválida! Tente novamente.")

