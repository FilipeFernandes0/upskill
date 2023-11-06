from propriedade3 import Propriedade

class Moradia(Propriedade):

    def __init__(self, nomeprop, NF, L):
        super().__init__(nomeprop, NF)

        self.__local = L
        if L == "Lisboa":
            cat = "A"
        elif L == "Porto":
            cat = "B"
        elif L =="Coimbra":
            cat = "C"
        else:
            cat = "D"
        self.__categoria = cat
    @property

    def local(self):
        return self.__local
    
    @local.setter

    def local(self,l):

        self.__local = l

    @property

    def categoria(self):
        return f"{self.__categoria}"

    @categoria.setter

    def categoria(self, C):
        self.__categoria =  C

    def Rendaminimamor(self):
        renda_minima = 0

        if self.__categoria =="A":
            renda_minima = 1000

        elif self.__categoria =="B":
            renda_minima = 700

        elif self.__categoria == "C":
            renda_minima = 500
        else:
            renda_minima = 400

        return renda_minima
            
        
    
