

class Avo:
    def __init__(self, nome_avo):
        self.__nomeavo = nome_avo


    def lernomeavo(self):
        return self.__nomeavo
    
    def imp(self):
        return f"eu sou o avo {self.lernomeavo()}"
    
class Filho(Avo):
    def __init__(self, nome_avo, nome_filho):
        super().__init__(nome_avo)
        self.__nome_filho = nome_filho

    def lerfilho(self):
        return self.__nome_filho
    def imp(self):
        return f"eu sou o avo {self.lernomeavo()} e o meu filho é {self.lerfilho()}"
    
    
class Filha(Avo):
    def __init__(self, nome_avo, nome_filha):
        super().__init__(nome_avo)

        self.__nome_filha = nome_filha

    def lerfilha(self):
        return self.__nome_filha
    
    def imp(self):
        return f"eu sou o avo {self.lernomeavo()} e a minha filha é {self.lerfilha()}"
    
class Neto(Filho,Avo):

    def __init__(self, nome_avo,nome_filho,nome_neto):
        super().__init__(nome_avo,nome_filho)
        self.__nome_neto = nome_neto
        
        

    def imp(self):
        print(f"eu sou o {self.lernomeavo()}")
        print(f"eu sou o pai {self.lerfilho()} do filho {self.__nome_neto}")
        #print(f"eu sou o pai {self.__nome_filha} do filho {self.__nome_neto}")
        print(f"eu sou o {self.__nome_neto} neto do {self.lernomeavo()} avo ")


    
rui = Avo("rui")
print(rui.imp())
joao = Filho("rui","joao")
print(joao.imp())
maria = Filha("rui","maria")
print(maria.imp())
filipe = Neto("Rui","joao","Filipe")
filipe.imp()


