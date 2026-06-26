from User import User
from Admin import Admin
from Combo import Combo

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

def listar_menu(menu,user):
    menuSemRec = menu[:]
    rec = user.get_recomendado()
    if rec != None:
        for i in menu:
            if isinstance(i,Combo):
                if i.has_item(rec):
                    rec = i
                    break
        menuSemRec.remove(rec)
        print(">"*25,"Especial para você","<"*25)
        print(rec)
        print("="*70)



    for i in menuSemRec:
        print()
        print(i)

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


def menu_loja(current_user,menu,faturamento):
    while True:
        print("\nMenu da loja:")
        print("1. Mostrar o cardápio")
        print("2. Adicionar item ao carrinho")
        print("3. Retirar item do carrinho")
        print("4. Mostrar carrinho")
        print("5. Finalizar compra")
        print("6. Sair")
        print()
        op = input("Digite a opção desejada: ")
        if op == "1":
            listar_menu(menu,current_user)
        elif op == "2":
            current_user.add_item(menu)
        elif op == "3":
            current_user.remove_item(menu)
        elif op == "4":
            current_user.show_carrinho()
        elif op == "5":
            faturamento += current_user.comprar_carrinho()
            print("Compra finalizada!")        
        elif op == "6":
            print("Saindo do menu da loja: ")
            break
        else:
            print("Opção inválida! Tente novamente")


def adm_menu(admins,users,current_admin,items=[],combos=[],menu=[],faturamento=0):
    while True:
        print("\n" + "="*50)
        print("MENU DO ADMIN")
        print("="*50)
        print("\n--- USUÁRIOS ---")
        print("1. Cadastrar usuário")
        print("2. Excluir usuário")
        print("3. Editar usuário")
        print("4. Listar usuários")
        print("\n--- ITENS ---")
        print("5. Adicionar item")
        print("6. Editar item")
        print("7. Excluir item")
        print("8. Listar itens")
        print("\n--- COMBOS ---")
        print("9. Adicionar combo")
        print("10. Editar combo")
        print("11. Excluir combo")
        print("12. Listar Ccombos")
        print("\n--- MENU ---")
        print("13. Criar menu")
        print("14. Editar menu")
        print("15. Listar menu")
        print("\n--- FATURAMENTO ---")
        print("16. Ver faturamento")
        print("\n--- ADMIN ---")
        print("17. Cadastrar admin")
        print("18. Excluir admin")
        print("19. Sair")
        print("="*50)
        print()
        op = input("Digite a opção desejada: ")
        
        if op == "1":
            current_admin.add_user(users)
        elif op == "2":
            current_admin.excluir_user(users)
        elif op == "3":
            cpf = input("Digite o CPF do usuário que deseja editar: ")
            for user in users:
                if user.get_cpf() == cpf:
                    mudar_info_user(user)
                    break
            else:
                print("Usuário não encontrado!")
        elif op == "4":
            listar_users(users)
        elif op == "5":
            current_admin.add_item(items)
        elif op == "6":
            current_admin.editar_item(items)
        elif op == "7":
            current_admin.excluir_item(items)
        elif op == "8":
            if len(items) == 0:
                print("Não há itens")
            else:
                for i in items:
                    print()
                    print(i)
        elif op == "9":
            current_admin.add_combo(combos, items)
        elif op == "10":
            current_admin.editar_combo(combos)
        elif op == "11":
            current_admin.excluir_combo(combos)
        elif op == "12":
            if len(combos) == 0:
                print("Não há combos")
            else:
                for i in combos:
                    print()
                    print(i)
        elif op == "13":
            novo_menu = current_admin.add_menu(items, combos)
            menu.clear()
            menu.extend(novo_menu)
        elif op == "14":
            current_admin.editar_menu(menu, items, combos)
        elif op == "15":
            listar_menu(menu)
        elif op == "16":
            current_admin.ver_faturamento(faturamento)
        elif op == "17":
            admins.append(cadastrar_admin())
        elif op == "18":
            excluir_admin(admins, current_admin)
            print("Saindo do menu do admin...")
            break
        elif op == "19":
            print("Saindo do menu do admin...")
            break
        else:
            print("Opção inválida! Tente novamente.")


def user_menu(users,current_user,menu,faturamento):
    while True:
        print("\nMenu do Usuário:")
        print("1. Editar informações")
        print("2. Exibir informações")
        print("3. Excluir conta")
        print("4. Menu da loja")
        print("5. Sair")
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
            faturamento = menu_loja(current_user,menu,faturamento)
        elif op == "5":
            print("Saindo do menu do usuário...")
            break
        else:
            print("Opção inválida! Tente novamente.")
    return faturamento

