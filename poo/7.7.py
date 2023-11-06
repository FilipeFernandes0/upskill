from oop_exercicios import EstudanteInf

if __name__ == "__main__":

    E=EstudanteInf("Ana Pinto", 14, 15) 
    
    B=EstudanteInf("Rui Pinto", 17, 18) 

    C=EstudanteInf("Carla Silva", 14, 10) 

    D=EstudanteInf("Telmo Gomes", 10, 12) 

    # E.set_name("Ana Maria")
    # E.set_teste1(12)
    # E.set_teste2(20)
    # B.set_name("OLA")
    # B.set_teste1(15)
    # B.set_teste2(20)

    # print(f"{'Nome':^15}{'Teste 1':^10}{'Teste 2':^10}{'Classif. Final':^15}") 

    # print(f"{E.get_name():<15}{E.get_teste1():^10}{E.get_teste2():^8}{E.class_final():^16}") 

    # print(f"{C.get_name():<15}{C.get_teste1():^10}{C.get_teste2():^8}{C.class_final():^16}") 

    # print(f"{B.get_name():<15}{B.get_teste1():^10}{B.get_teste2():^8}{B.class_final():^16}") 

    # print(f"{D.get_name():<15}{D.get_teste1():^10}{D.get_teste2():^8}{D.class_final():^16}")


    a = [E,B,C,D]
    inf = [[E],[B],[C],[D]]
    
    pauta = {}
    
    for i in range(len(inf)):
        for estudante in inf[i]: 
            pauta[estudante.get_name()] = estudante.class_final()
    print(pauta)

    

        


    

