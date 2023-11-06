class Propriedade():
    def __init__(self, nomeprop, NF):
        self.__Proprietario = nomeprop
        self.__numero_fiscal = NF

    @property

    def Proprietario(self):

        return self.__Proprietario
    
    @Proprietario.setter
    def Proprietario(self,N):
        self.__Proprietario = N

    @property

    def NFiscal(self):

        return self.__numero_fiscal
    

    @NFiscal.setter

    def NFiscal(self,NF):
        self.__numero_fiscal = NF

    def impressao(self):
        return f"proprietario: {self.Proprietario} numero fiscal: {self.NFiscal}"
    
    def rendaminima(self):
        P1 = 0.2
        P2 = 0.3
        Min = 100

        if self.area < 50:
            renda = Min
        elif self.area < 100:
            renda = Min+P1*self.area
        else:
            renda = Min+P2*self.area
        return int(renda)
        
    