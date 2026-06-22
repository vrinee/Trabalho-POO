import controlFuncs
from Admin import Admin
from User import User

admins = []
usuarios = []
faturamento = 0
menu = []
admins.append(Admin("Root","1234"))

print(admins[0])
while True:
    print("Inicío: ")
    print("1. Usuário")
    print("2. Admin")
    print("3. Sair")
    print()

    op = input("Digite a opção desejada: ")
    
    if op == "1":
        aux = input("Login(1) ou cadastrar(2): ")
        if aux == "1":
            cpf = input("Digite seu cpf: ")
            senha = input("Digite sua senha: ")
            logou = False
            for user in usuarios:
                if user.get_cpf() == cpf:
                    logou = True
                    if user.get_senha() == senha:
                        controlFuncs.user_menu(usuarios,user,menu,faturamento)
                        break
                    print("Senha incorreta!!")
            if not logou:
                print("Login incorreto.")
        elif aux == "2":
            usuarios.append(controlFuncs.cadastrar_usuario())
            controlFuncs.user_menu(usuarios,usuarios[-1])
        else:
            print("Opção inválida! Tente novamente.")
    
    elif op == "2":
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        logou = False
        for adm in admins:
            if adm.get_nome() == nome:
                logou = True
                if adm.get_senha() == senha:
                    controlFuncs.adm_menu(admins,usuarios,adm)
                    break
                print("Senha incorreta")
        if not logou:
            print("Login incorreto.")
    
    elif op == "3":
        print("Encerrando programa...")
        exit(0)

    else: 
        print("Opção inválida!! Tente novamente.")
    