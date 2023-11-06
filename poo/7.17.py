from propriedade3 import Propriedade 

from apartamento3 import Apartamento
from moradia3 import Moradia


listas = [["jose paiva",14765,"Porto"],["Abel Fama", 12345, "t3",200]]

for i in listas:
    if len(i) == 3:
        ana =Moradia(i[0],i[1],i[2])
        print(ana.impressao(),ana.Rendaminimamor())

    else:
        filipe = Apartamento(i[0],i[1],i[2],i[3])
        print(filipe.impressao(),filipe.rendaminima())



ana = Moradia("adao", 122,"Coimbra")

filipe = Apartamento("filipe",239276710,"T2",200)




