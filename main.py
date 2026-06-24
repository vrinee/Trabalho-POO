import controlFuncs
from Admin import Admin
from User import User
from Comida import Comida
from Bebida import Bebida
from Item import Item
from Combo import Combo


admins = []
usuarios = []
faturamento = 0
items = []
combos = []
menu = []
admins.append(Admin("Root","1234"))
usuarios.append(User("Default","100.200.300-40","email@email.com","48-98765-4321","01/01/2001","123abc"))
items.append(Item("Genérico","lorem ipsum dolor sit amet, não lembro o resto",5,9.99))
items.append(Comida("Yummers","yummyyyyyyyyyyyyyyyyyyyyyyy",10,5.99,"Nenhum, a não ser que seja alérgico a diversão :P"))
items.append(Bebida("Leite","Muito proteico e sla mais oq, mas o arthur não tolera, em pleno 2026",10000,2.59,250))
combos.append(Combo("404 not found","não encontrou nada só placeholder :P",17.98,6))
combos[0].add_item(items[0],2)
combos[0].add_item(items[1],1)
combos[0].add_item(items[2],2)
menu.append(items[0])
menu.append(items[1])
menu.append(items[2])
menu.append(combos[0])

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
                        faturamento = controlFuncs.user_menu(usuarios,user,menu,faturamento)
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
                    controlFuncs.adm_menu(admins, usuarios, adm, items, combos, menu, faturamento)
                    break
                print("Senha incorreta")
        if not logou:
            print("Login incorreto.")
    
    elif op == "3":
        print("Encerrando programa...")
        exit(0)

    else: 
        print("Opção inválida!! Tente novamente.")
    