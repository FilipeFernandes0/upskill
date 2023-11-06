from propriedade3 import Propriedade

class Apartamento(Propriedade):

    def __init__(self, nomeprop, NF,T,A):
        super().__init__(nomeprop, NF)

        self.__tipo = T
        self.__area = A
        

    @property

    def tipo(self):
        return self.__tipo

    @tipo.setter

    def tipo(self,T):
        self.__tipo = T  

    @property
    def area(self):
        return self.__area
    
    @area.setter

    def area(self,A):

        self.__area = A
