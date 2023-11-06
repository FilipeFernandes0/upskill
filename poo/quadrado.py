class Quadrado:
    def __init__(self, c):

        self.__comprimento = c
    
    def lercomprimento(self):
        return self.__comprimento
    

    def area_do_quadrado(self):
        area = self.__comprimento * self.__comprimento

        return area
    
class Retangulo(Quadrado):
    def __init__(self,c, largura):
        super().__init__(c)
        self.__comprimento = c
        self.__largura = largura

    def lerlargura(self):
        return self.__largura
    def dimensoes(self):
        return f"{self.lerlargura()} {self.lercomprimento()}"
    def area(self):
        return self.lercomprimento() * self.lerlargura()
    

       
    

lado = Quadrado(2)
angulo = Retangulo(12,24)

print(angulo.dimensoes())
print(angulo.area())



    
