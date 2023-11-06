#Deverá ser implementada a funcionalidade básica, a saber: 
#1 - Manutenção de Países => (C) - Criar, (R) - Obter, (U) - Atualizar e (D) - Eliminar 
#2 - Manutenção de Capitais =>  (C) - Criar, (R) - Obter, (U) - Atualizar e (D) - Eliminar 
#3 - Listar => Países e Capitais 

paises_capital = {"teste":"ola"}

while True:
    funcionalidade_basica = int(input("1 - Manutenção de Países, 2 - Manutenção de Capitais, 3 - Listar: "))
    if funcionalidade_basica == 1:
       manutencao1 = str(input( "Manutenção de Países => (C) - Criar, (R) - Obter, (U) - Atualizar e (D) - Eliminar " ))
       if manutencao1 == "C":
            criar1 = str(input("que país queres criar: "))
            if criar1 not in paises_capital:
                paises_capital[criar1] = ""
                print(paises_capital)
       if manutencao1 == "R":
            obter1 = str(input("qual é o país que queres obter: "))
            if obter1 in paises_capital:
                print(paises_capital)
       if manutencao1 == "U":
            atualizar1 = str(input("qual é o pais que queres atualizar: "))
            if atualizar1 in paises_capital:
                paises_capital.pop(atualizar1)
                atualizar1 = str(input("qual é o nome do país novo? "))
                paises_capital[atualizar1] = ""
                print(paises_capital)
            
       if manutencao1 == "D":
            eliminar1 = str(input("Qual é o pais que queres eliminar? "))
            if eliminar1 in paises_capital:
                paises_capital.pop(eliminar1)
            print(paises_capital)
    if funcionalidade_basica == 2:
        manutencao2 = str(input("Manutenção de Capitais =>  (C) - Criar, (R) - Obter, (U) - Atualizar e (D) - Eliminar "))
        if manutencao2 == "C":
            criar2 = str(input("Qual é a capital que queres Criar: "))
            if criar2 not in paises_capital.values():
                paises_capital[criar1] = criar2
            print(paises_capital)                
        if manutencao2 == "R":
            obter2 = str(input("qual é a capital que queres obter: "))
            if obter2 in paises_capital.values():
                print(obter2)
                
        if manutencao2 == "U":
            obter_pais = str(input("tem de existir o país que queres atualizar: "))
            if obter_pais in paises_capital.keys():
                atualizar2 = str(input("qual é a capital que queres atualizar? "))
                if atualizar2 == paises_capital[obter_pais]:
                    atualizar2 = str(input("qual é o nome da capital nova? "))
                    paises_capital[obter_pais] = atualizar2
                print(paises_capital)
        
        if manutencao2 == "D":
            eliminar_pais = str(input("tem de existir o país que queres eliminar: "))
            if eliminar_pais in paises_capital.keys():
                eliminar2 = str(input("Qual é a capital que queres eliminar? "))
            if eliminar2 == paises_capital[eliminar_pais]:
                del paises_capital[eliminar_pais]
                
            print(paises_capital)
    if funcionalidade_basica == 3:
        #str(input("Listar => Países e Capitais "))
        #for value in paises_capital.values():
            #print(value)
        
        print(paises_capital)
        

#print(paises_capital)