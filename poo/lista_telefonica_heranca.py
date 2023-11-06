

class Contacto:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property

    def nome(self):
        return self.__nome
    
    @property

    def telefone(self):
        return self.__telefone
    

    def __str__(self):

        return f"nome: {self.nome} telefone: {self.telefone}"
    


class ContactoPessoal(Contacto):
    def __init__(self, nome, telefone, endereco,email):
        super().__init__(nome, telefone)

    
        self.__endereco = endereco
        self.__email = email

    @property 

    def endereco(self):
        return self.__endereco
    
    @property

    def email(self):
        return self.__email
    
    def __str__(self):
        return super().__str__() + f" endereco: {self.endereco} email: {self.email}"
    


class ContactoProfissional(Contacto):
    def __init__(self, nome, telefone,empresa,cargo):
        super().__init__(nome, telefone)
        self.__empresa = empresa
        self.__cargo = cargo


    @property 

    def empresa(self):
        return self.__empresa
    
    @property

    def cargo(self):
        return self.__cargo
    

    def __str__(self):
        return super().__str__() + f" empresa: {self.empresa} cargo: {self.cargo}"
    



contacto = Contacto("filipe", "961512067")

contacto.nome = "diogo"
print(contacto)
# def criar_contacto_pessoal():
#     nome = input("Digite o nome: ")
#     telefone = input("Digite o telefone: ")
#     endereco = input("Digite o endereco: ")
#     email = input("Digite o email: ")
#     return ContactoPessoal(nome, telefone, endereco, email)

# def criar_contacto_profissional():
#     nome = input("Digite o nome: ")
#     telefone = input("Digite o telefone: ")
#     empresa = input("Digite a empresa: ")
#     cargo = input("Digite o cargo: ")
#     return ContactoProfissional(nome, telefone, empresa, cargo)

# def mostrar_menu():
#     print("\nMenu:")
#     print("1. Criar contato pessoal")
#     print("2. Criar contato profissional")
#     print("3. Sair")

# def main():
#     while True:
#         mostrar_menu()
#         escolha = input("Escolha uma opcao (1/2/3): ")

#         if escolha == "1":
#             contato_pessoal = criar_contacto_pessoal()
#             print(f"Contato pessoal criado: {contato_pessoal}")
#         elif escolha == "2":
#             contato_profissional = criar_contacto_profissional()
#             print(f"Contato profissional criado: {contato_profissional}")
#         elif escolha == "3":
#             print("Saindo do programa...")
#             break
#         else:
#             print("Opcao invalida. Tente novamente.")

# if __name__ == "__main__":
#     main()


    
    


    


    
