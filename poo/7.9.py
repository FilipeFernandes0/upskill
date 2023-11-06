from oop_exercicios import EstudanteInf


if __name__=="__main__": 

    E=EstudanteInf("Ana Paiva", 18, 12) 
    

    B=EstudanteInf("Filipe", 7, 8) 

    C=EstudanteInf("Uirá", 10, 9) 

    D=EstudanteInf("Bruno", 8, 1) 


    def contagem_final(CF):
        count = 0
        if CF > 14:
            count += 1
            return count
        else:
            count = 0
            return count
    print(f"{'Nome':^15}{'Teste 1':^10}{'Teste 2':^10}{'Classif. Final':^15} {'contagem final':^15}") 

    print(f"{E.get_name():<15}{E.get_teste1():^10}{E.get_teste2():^8}{E.class_final():^16}{contagem_final(E.class_final()):^16} ") 

    print(f"{C.get_name():<15}{C.get_teste1():^10}{C.get_teste2():^8}{C.class_final():^16}{contagem_final(B.class_final()):^16}") 

    print(f"{B.get_name():<15}{B.get_teste1():^10}{B.get_teste2():^8}{B.class_final():^16}{contagem_final(C.class_final()):^16}") 

    print(f"{D.get_name():<15}{D.get_teste1():^10}{D.get_teste2():^8}{D.class_final():^16}{contagem_final(D.class_final()):^16}") 

 
            
            
        