#inserir outras classes que serão manipuladas pelo admin
from Item import Item
from Comida import Comida
from Bebida import Bebida
from Combo import Combo

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

    def add_item(self, items):
        print("\nEscolha o tipo de item que deseja adicionar:")
        print("1. Item normal")
        print("2. Comida")
        print("3. Bebida")
        tipo = input("Digite a opção desejada: ")

        nome = input("Digite o nome do item: ")
        descricao = input("Digite a descrição do item: ")
        estoque = int(input("Digite a quantidade em estoque(em ml caso for bebida): "))
        preco = float(input("Digite o preço do item: "))

        if tipo == "1":
            item = Item(nome, descricao, estoque, preco)
            items.append(item)
            print("Item normal adicionado com sucesso!")
        elif tipo == "2":
            alergenico = input("Digite os alérgenos (ou pressione Enter se não houver): ")
            if alergenico == "":
                alergenico = None
            item = Comida(nome, descricao, estoque, preco, alergenico)
            items.append(item)
            print("Comida adicionada com sucesso!")
        elif tipo == "3":
            tamanho = int(input("Digite o tamanho da bebida em ml: "))
            item = Bebida(nome, descricao, estoque, preco, tamanho)
            items.append(item)
            print("Bebida adicionada com sucesso!")
        else:
            print("Opção inválida! Item não foi adicionado.")

    def excluir_item(self, items):
        nome = input("Digite o nome do item que deseja excluir: ")
        for item in items:
            if item.get_nome() == nome:
                items.remove(item)
                print("Item excluído com sucesso!")
                return
        print("Item não encontrado!")

    def add_combo(self, combos, items):
        nome = input("Digite o nome do combo: ")
        descricao = input("Digite a descrição do combo: ")
        preco = float(input("Digite o preço do combo: "))
        limite_diario = int(input("Digite o limite diário de vendas do combo: "))
        
        combo = Combo(nome, descricao, preco, limite_diario)
        
        print("\nAdicionando itens ao combo:")
        while True:
            print("\nItens disponíveis:")
            for i, item in enumerate(items):
                print(f"{i}. {item.get_nome()} - R${item.get_preco()}")
            
            opcao = input("\nDigite o índice do item a adicionar (ou 'sair' para finalizar): ")
            
            if opcao.lower() == "sair":
                break
            
            try:
                idx = int(opcao)
                if 0 <= idx < len(items):
                    quantidade = int(input(f"Digite a quantidade de '{items[idx].get_nome()}' no combo: "))
                    combo.get_itens().append([items[idx], quantidade])
                    print(f"'{items[idx].get_nome()}' adicionado ao combo com sucesso!")
                else:
                    print("Índice inválido! Tente novamente.")
            except ValueError:
                print("Entrada inválida! Tente novamente.")
        
        if len(combo.get_itens()) > 0:
            combos.append(combo)
            print(f"\nCombo '{nome}' adicionado com sucesso!")
        else:
            print("\nCombo não foi criado pois nenhum item foi adicionado.")

    def excluir_combo(self, combos):
        nome = input("Digite o nome do combo que deseja excluir: ")
        for combo in combos:
            if combo.get_nome() == nome:
                combos.remove(combo)
                print("Combo excluído com sucesso!")
                return
        print("Combo não encontrado!")

    def editar_item(self, items):
        nome = input("Digite o nome do item que deseja editar: ")
        for item in items:
            if item.get_nome() == nome:
                while True:
                    print("\nMenu de edição do item:")
                    print("1. Editar nome")
                    print("2. Editar descrição")
                    print("3. Adicionar estoque")
                    print("4. Editar preço")
                    
                    if isinstance(item, Comida):
                        print("5. Editar alérgenos")
                        print("6. Voltar")
                    elif isinstance(item, Bebida):
                        print("5. Editar tamanho")
                        print("6. Voltar")
                    else:
                        print("5. Voltar")
                    
                    opcao = input("Digite a opção desejada: ")
                    
                    if opcao == "1":
                        novo_nome = input("Digite o novo nome: ")
                        item.set_nome(novo_nome)
                        print("Nome atualizado com sucesso!")
                    elif opcao == "2":
                        nova_descricao = input("Digite a nova descrição: ")
                        item.set_descricao(nova_descricao)
                        print("Descrição atualizada com sucesso!")
                    elif opcao == "3":
                        quantidade = int(input("Digite a quantidade de estoque a adicionar: "))
                        item.set_estoque(item.get_estoque() + quantidade)
                        print(f"Estoque aumentado para {item.get_estoque()} com sucesso!")
                    elif opcao == "4":
                        novo_preco = float(input("Digite o novo preço: "))
                        item.set_preco(novo_preco)
                        print("Preço atualizado com sucesso!")
                    elif opcao == "5":
                        if isinstance(item, Comida):
                            novo_alergenico = input("Digite os novos alérgenos (ou pressione Enter para remover): ")
                            if novo_alergenico == "":
                                novo_alergenico = None
                            item.set_alergenico(novo_alergenico)
                            print("Alérgenos atualizado com sucesso!")
                        elif isinstance(item, Bebida):
                            novo_tamanho = int(input("Digite o novo tamanho em ml: "))
                            item.set_tamanho(novo_tamanho)
                            print("Tamanho atualizado com sucesso!")
                        else:
                            print("Voltando ao menu anterior...")
                            return
                    elif opcao == "6":
                        if isinstance(item, (Comida, Bebida)):
                            print("Voltando ao menu anterior...")
                            return
                        else:
                            print("Opção inválida! Tente novamente.")
                    else:
                        print("Opção inválida! Tente novamente.")
        print("Item não encontrado!")

    def editar_combo(self, combos):
        nome = input("Digite o nome do combo que deseja editar: ")
        for combo in combos:
            if combo.get_nome() == nome:
                while True:
                    print("\nMenu de edição do combo:")
                    print("1. Editar nome")
                    print("2. Editar descrição")
                    print("3. Editar preço")
                    print("4. Editar limite diário")
                    print("5. Voltar")
                    opcao = input("Digite a opção desejada: ")
                    
                    if opcao == "1":
                        novo_nome = input("Digite o novo nome: ")
                        combo.set_nome(novo_nome)
                        print("Nome atualizado com sucesso!")
                    elif opcao == "2":
                        nova_descricao = input("Digite a nova descrição: ")
                        combo.set_descricao(nova_descricao)
                        print("Descrição atualizada com sucesso!")
                    elif opcao == "3":
                        novo_preco = float(input("Digite o novo preço: "))
                        combo.set_preco(novo_preco)
                        print("Preço atualizado com sucesso!")
                    elif opcao == "4":
                        novo_limite = int(input("Digite o novo limite diário: "))
                        combo.set_limite_diario(novo_limite)
                        print("Limite diário atualizado com sucesso!")
                    elif opcao == "5":
                        print("Voltando ao menu anterior...")
                        return
                    else:
                        print("Opção inválida! Tente novamente.")
        print("Combo não encontrado!")

    def add_menu(self, items, combos):
        menu = []
        print("\nAdicionando itens ao menu:")
        while True:
            print("\nO que deseja adicionar?")
            print("1. Item")
            print("2. Combo")
            print("3. Finalizar")
            opcao = input("Digite a opção desejada: ")
            
            if opcao == "1":
                nome_item = input("Digite o nome do item a adicionar: ")
                for item in items:
                    if item.get_nome() == nome_item:
                        menu.append(item)
                        print(f"Item '{nome_item}' adicionado ao menu!")
                        break
                else:
                    print("Item não encontrado!")
            
            elif opcao == "2":
                nome_combo = input("Digite o nome do combo a adicionar: ")
                for combo in combos:
                    if combo.get_nome() == nome_combo:
                        menu.append(combo)
                        print(f"Combo '{nome_combo}' adicionado ao menu!")
                        break
                else:
                    print("Combo não encontrado!")
            
            elif opcao == "3":
                break
            else:
                print("Opção inválida! Tente novamente.")
        
        if len(menu) > 0:
            print(f"\nMenu criado com sucesso com {len(menu)} item(ns)!")
            return menu
        else:
            print("\nMenu vazio não foi criado.")
            return []

    def editar_menu(self, menu, items, combos):
        if not menu:
            print("Menu vazio! Nada para editar.")
            return
        
        while True:
            print("\nEditando menu:")
            print("1. Adicionar item")
            print("2. Remover item")
            print("3. Listar itens")
            print("4. Voltar")
            opcao = input("Digite a opção desejada: ")
            
            if opcao == "1":
                print("\nDeseja adicionar um item ou combo?")
                print("1. Item")
                print("2. Combo")
                tipo = input("Digite a opção: ")
                
                if tipo == "1":
                    nome_item = input("Digite o nome do item a adicionar: ")
                    for item in items:
                        if item.get_nome() == nome_item:
                            menu.append(item)
                            print(f"Item '{nome_item}' adicionado ao menu!")
                            break
                    else:
                        print("Item não encontrado!")
                
                elif tipo == "2":
                    nome_combo = input("Digite o nome do combo a adicionar: ")
                    for combo in combos:
                        if combo.get_nome() == nome_combo:
                            menu.append(combo)
                            print(f"Combo '{nome_combo}' adicionado ao menu!")
                            break
                    else:
                        print("Combo não encontrado!")
            
            elif opcao == "2":
                nome = input("Digite o nome do item/combo a remover: ")
                removido = False
                for item in menu:
                    if item.get_nome() == nome:
                        menu.remove(item)
                        print(f"'{nome}' removido do menu!")
                        removido = True
                        break
                if not removido:
                    print("Item/Combo não encontrado no menu!")
            
            elif opcao == "3":
                print("\nItens e Combos no menu:")
                if menu:
                    for i, item in enumerate(menu, 1):
                        print(f"{i}. {item.get_nome()}")
                else:
                    print("Menu vazio!")
            
            elif opcao == "4":
                print("Voltando ao menu anterior...")
                return
            else:
                print("Opção inválida! Tente novamente.")

    def ver_faturamento(self, faturamento):
        print("\n" + "="*50)
        print("FATURAMENTO TOTAL")
        print("="*50)
        print(f"Valor total faturado: R${faturamento:.2f}")
        print("="*50)

    def __str__(self):
        return f"Nome: {self.nome} Senha: {self.senha}"
