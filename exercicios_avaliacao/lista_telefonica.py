


class Contacto:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class ListaTelefonica:
    def __init__(self):
        
        
        self.lista_contacto = []
    def inserir_contacto(self,contacto):
        self.lista_contacto.append(contacto)
        return f"contacto ctiado com sucesso"
    def listar_contactos(self):
        for contacto in self.lista_contacto:
            return f"nome: {contacto.nome} telefone: {contacto.telefone}" 
        
    def eliminar_contacto(self,nome):
            contactos_restantes = [contacto for contacto in self.lista_contacto if contacto.nome != nome]
            if len(contactos_restantes) == len(self.lista_contacto):
                print(f"Contacto {nome} nao encontrado na lista.")
            else:
                self.lista_contacto = contactos_restantes
                print(f"Contacto {nome} removido com sucesso.")

    def atualizar_contactos(self,nome,novo_telefone):

        for contacto in self.lista_contacto:
            if contacto.nome == nome:
                contacto.telefone = novo_telefone
                return f"o telefone foi removido e atualizado pelo novo numero {novo_telefone}"
        return f"nome nao foi encontrado na lista"
            
def display_menu():


    print("\n Lista telefonica")
    print("1.Inserir contacto: ")
    print("2.Atualizar contacto: ")
    print("3.Eliminar contacto: ")
    print("4.Obter contactos: ")
    print("5.Exit")


lista = ListaTelefonica()

while True:
    display_menu()

    escolha = input("escolha uma opcao: ")
    if escolha == "1":
        nome = input("nome do contacto: ")
        telefone = input("numero do contacto: ")
        contacto = Contacto(nome,telefone)
        lista.inserir_contacto(contacto)

    elif escolha == "4":
        print(lista.listar_contactos())
    

    elif escolha == "3":
        nome = input("Nome do contacto a remover: ")
        lista.eliminar_contacto(nome)

    elif escolha == "2":

        nome = input("nome do contacto que quer atualizar: ")
        novo_telefone = input("novo numero de telemovel atualizado: ")
        lista.atualizar_contactos(nome,novo_telefone)

    else:
        escolha == "5"
        print("A sair...")
        break

    









    
    

    
    






################################## MENU MÉDIO ################################################

# def exibir_menu():
#     print("Bem-vindo ao restaurante!")
#     print("Selecione uma opção:")
#     print("1. Ver menu")
#     print("2. Fazer um pedido")
#     print("3. Sair")

# def ver_menu():
#     print("MENU:")
#     print("1. Hambúrguer - R$10.00")
#     print("2. Pizza - R$15.00")
#     print("3. Salada - R$8.00")

# def fazer_pedido():
#     pedido = input("Digite o número do item que deseja pedir: ")
#     # Lógica para processar o pedido

# while True:
#     exibir_menu()
#     opcao = input("Digite o número da opção desejada: ")

#     if opcao == "1":
#         ver_menu()
#     elif opcao == "2":
#         fazer_pedido()
#     elif opcao == "3":
#         print("Obrigado por visitar nosso restaurante!")
#         break
#     else:
#         print("Opção inválida. Por favor, digite novamente.")


################################## MENU BASICO ################################################

# while True:
#     print("Bem-vindo ao Restaurante!")
#     print("Selecione uma opção:")
#     print("1. Ver menu")
#     print("2. Fazer um pedido")
#     print("3. Sair")

#     opcao = input("Digite o número da opção desejada: ")

#     if opcao == "1":
#         print("MENU:")
#         print("1. Hambúrguer - R$10.00")
#         print("2. Pizza - R$15.00")
#         print("3. Salada - R$8.00")
#     elif opcao == "2":
#         pedido = input("Digite o número do item que deseja pedir: ")
#         # Lógica para processar o pedido
#     elif opcao == "3":
#         print("Obrigado por visitar nosso restaurante!")
#         break
#     else:
#         print("Opção inválida. Por favor, digite novamente.")

# ################################## MENU COMPLEXO ################################################

# class Menu:
#     def __init__(self):
#         self.options = {}

#     def add_option(self, key, description, action):
#         self.options[key] = {
#             "description": description,
#             "action": action
#         }

#     def display(self):
#         print("Bem-vindo ao Restaurante!")
#         print("Selecione uma opção:")
#         for key, option in self.options.items():
#             print(f"{key}. {option['description']}")

#     def run(self):
#         while True:
#             self.display()
#             choice = input("Digite o número da opção desejada: ")
#             if choice in self.options:
#                 selected_option = self.options[choice]
#                 selected_option["action"]()
#             else:
#                 print("Opção inválida. Por favor, digite novamente.")


# # Funções para as ações do menu
# def ver_menu():
#     print("MENU:")
#     print("1. Hambúrguer - R$10.00")
#     print("2. Pizza - R$15.00")
#     print("3. Salada - R$8.00")

# def fazer_pedido():
#     pedido = input("Digite o número do item que deseja pedir: ")
#     # Lógica para processar o pedido

# def exibir_promocoes():
#     print("PROMOÇÕES:")
#     print("1. Combo do dia - Hambúrguer, batatas fritas e refrigerante por R$20.00")
#     print("2. Desconto de 10% em pizzas grandes")
#     print("3. Happy hour - 50% de desconto em bebidas das 18h às 20h")

# # Criando o menu
# menu = Menu()

# # Adicionando opções ao menu
# menu.add_option("1", "Ver menu", ver_menu)
# menu.add_option("2", "Fazer um pedido", fazer_pedido)
# menu.add_option("3", "Exibir promoções", exibir_promocoes)
# menu.add_option("4", "Sair", exit)

# # Executando o menu
# menu.run()






