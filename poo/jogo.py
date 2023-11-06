



# class Personagem:
#     def __init__(self,nome,hp,ataque,defesa):

#         self.__nome = nome
#         self.__hp = hp
#         self.__ataque = ataque
#         self.__defesa = defesa

#     @property

#     def nome(self):
#         return self.__nome
    
#     @property

#     def hp(self):
#         return self.__hp
#     @property

#     def ataque(self):
#         return self.__ataque
#     @property

#     def defesa(self):
#         return self.__defesa
    
#     def __str__(self) -> str:
#         return f"nome: {self.nome} hp: {self.hp} ataque: {self.ataque} defesa: {self.defesa}"
    

# class Guerreiro(Personagem):

#     def __init__(self, nome, hp, ataque, defesa, nome_da_espada, tipo_de_espada):
#         super().__init__(nome, hp, ataque, defesa)

#         self.__nome_da_espada = nome_da_espada
#         self.__tipo_de_espada = tipo_de_espada
#     @property

#     def nome_da_espada(self):
#         return self.__nome_da_espada
#     @property

#     def tipo_de_espada(self):
#         return self.__tipo_de_espada
    
#     def __str__(self) -> str:
#         return super().__str__() + f" nome da espada: {self.nome_da_espada} tipo da espada: {self.tipo_de_espada}"

    

# class Mago(Personagem):

#     def __init__(self, nome, hp, ataque, defesa,nome_do_bastao,magia):
#         super().__init__(nome, hp, ataque, defesa)


#         self.__nome_do_bastao = nome_do_bastao
#         self.__magia = magia

#     @property

#     def nome_do_bastao(self):
#         return self.__nome_do_bastao
#     @property

#     def magia(self):
#         return self.__magia
    

# class Arqueiro(Personagem):

#     def __init__(self, nome, hp, ataque, defesa, nome_do_arco,flechas_especiais):
#         super().__init__(nome, hp, ataque, defesa)

#         self.__nome_do_arco = nome_do_arco
#         self.__flechas_especiais = flechas_especiais


    
#     @property

#     def nome_do_arco(self):
#         return self.__nome_do_arco
#     @property

#     def flechas_especiais(self):
#         return self.__flechas_especiais
    


# personagem = Guerreiro("Filipe",20,40,30,"salvador","diamante")

# print(personagem)



#exercicio 1 loja de animais polimorfismo


# class Animal:
#     def __init__(self, nome, raca, idade):
#         self.nome = nome
#         self.raca = raca
#         self.idade = idade

# class Cao(Animal):
#     def __init__(self, nome, raca, idade):
#         super().__init__(nome, raca, idade)

    
#     def emitir_som(self):
#         return "au au"


# class Gato(Animal):
#     def __init__(self, nome, raca, idade):
#         super().__init__(nome, raca, idade)


#     def emitir_som(self):

#         return "miau miau"
    


# animal = Cao("filipe","labrador",20)
# print(animal.emitir_som())
# animal = Gato("bolinhas", "tigre", 20)
# print(animal.emitir_som())

class Banco:
    def __init__(self, id, nome, idade):

        self.__id = id
        self.__nome = nome
        self.__idade = idade
        

    @property

    def id(self):

        return self.__id
    
    @property

    def nome(self):

        return self.__nome
    
    @property

    def idade(self):

        return self.__idade
    
   
    

class ContaCorrente(Banco):
    def __init__(self, id, nome, idade, montante):
        super().__init__(id, nome, idade)

        self.__montante = montante

    @property

    def montante(self):

        return self.__montante
    




    def transferencia_bancaria(self,depositar):

        self.__montante =  self.__montante  + depositar
        #return self.__montante
        return f"o deposito de {depositar} foi concluido com sucesso o seu montante é de {self.montante} "
    

class ContaPoupanca(Banco):

    def __init__(self, id, nome, idade, montante_poupanca):
        super().__init__(id, nome, idade)

        self.__montante_poupanca = montante_poupanca

    @property

    def montante_poupanca(self):

        return self.__montante_poupanca

    

    def transferencia_poupanca(self, depositar):

        self.__montante_poupanca = self.__montante_poupanca  + depositar
        
        return f"o deposito de {depositar} foi concluido com sucesso o seu montante é de {self.montante_poupanca} "
    
    def levantamento_bancario(self,levantar):

        if self.montante_poupanca <= 0:
            return f"O levantamento nao pode ser efetuado"
        elif self.montante_poupanca < levantar:
            return f"o valor que quer levantar é maior que o montante da conta"
        
        else:
           self.__montante_poupanca = (self.__montante_poupanca - levantar) * 0.05
           return f"o valor foi levantado a sua conta poupanca esta a {self.montante_poupanca}"
        


pessoa = ContaCorrente("1","Filipe", 20, 500)
print(pessoa.transferencia_bancaria(1000))

pessoa = ContaPoupanca("1","Filipe", 20, 100000)

print(pessoa.transferencia_poupanca(50000))
print(pessoa.levantamento_bancario(5000))
        




        

        

    


    