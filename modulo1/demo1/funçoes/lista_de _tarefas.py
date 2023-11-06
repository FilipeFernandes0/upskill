# Considere um script que permita manter uma lista de tarefas a executar. 
#Deverá criar uma lista de dicionários, em que para cada entrada deverão ser considerados os seguintes atributos: 
# id (chave da tarefa, incrementada automaticamente); 
# designação; 
# data e hora de conclusão (prevista e efetiva, quando a tarefa seja concluída); 
# categorias (tupla com a designação das categorias); 
# importância (prioritária, normal, não prioritária); 
# tempo gasto (número real para representar as horas gastas até ao momento) 
# concluída (True ou False). 
# Deverá ser implementada a funcionalidade básica, a saber: 
# 1 - Gestão de Tarefas: 
# (C) - Criar: create_task(list, task);  
# (R) - Obter: indicando o id;  
# (U) - Atualizar:  os campos aplicáveis (não posso mexer no tempo gasto e no campo concluído);  
# (D) - Eliminar: não posso eliminar tarefas iniciadas (tempo gasto > 0) nem concluídas. 
# 2 - Manutenção de Tarefas:   
# (A) - Adicionar tempo: add_time_to_task(task, time);  
# (C) - Concluir tarefa. 
# 3 - Listagens:  
# (TC) - Tarefas concluídas;  
# (TI) - Tarefas iniciadas (tempo gasto > 0);  
# (TP) - Tarefas prioritárias;  
# (TNC) - Tarefas não concluídas, por ordem não decrescente de data e hora prevista de conclusão. 
from datetime import datetime
#list = []
dicionario = {}
list = []
def create_task():
    
    #id = len(dicionario)+1
    designacao = input("designação da tarefa: ")
    ano = int(input("ano previsto: "))
    mes = int(input("mês previsto: "))
    dia = int(input("dia previsto: "))
    hora = int(input("hora previsto: "))
    min = int(input("minutos previstos: "))
    dt = datetime(ano,mes,dia,hora,min)
    print(dt)
    ano1 = int(input("ano de conclusão: "))
    mes1 = int(input("mês de conclusão : "))
    dia1 = int(input("dia de conclusão: "))
    hora1 = int(input("hora de conclusão: "))
    min1 = int(input("minutos de conclusão: "))
    dt1 = datetime(ano1,mes1,dia1,hora1,min1)
    print(dt1)
    categorias = input("qual a categoria da tarefa: ")
    importancia = input("qual a importância (prioritária, normal, não prioritária): ")
    concluida = input("tarefa concluida True or False: ")
    if concluida == True:
        print("A tarefa foi concluida")
    elif concluida == False:
        print("A tarefa não foi concluida")
        
    diferenca = dt1 - dt
    tempo_gasto_em_horas = (diferenca.days * 24) + (diferenca.seconds // 3600)
    lista = [designacao,dt,dt1,(categorias,),importancia,tempo_gasto_em_horas, concluida]
    dicionario[id] = lista

def obter_task():
        
        id = int(input("qual é o id que queres obter: "))
        
        if id in  dicionario.keys():
            print(dicionario[id])


def atualizar_tasks():
    menu = int(input("o que queres atualizar\n1-designação:\n2-data da previsão:\n3-data da conclusão\n4-categorias\n5-importancia\n"))
    if menu == 1:
        nova_designacao = input("qual é a nova designação: ")
        for lista in dicionario.values():
            del lista[0]
            lista.insert(0 , nova_designacao)
            print(lista)
            print(dicionario)
    if menu == 2:
        novo_ano = int(input("novo ano previsto: "))
        novo_mes = int(input("novo mês previsto: "))
        novo_dia = int(input("novo dia previsto: "))
        nova_hora = int(input("nova hora prevista: "))
        novo_min = int(input("novos minutos previstos: "))
        novo_dt = datetime(novo_ano,novo_mes,novo_dia,nova_hora,novo_min)
        for lista in dicionario.values():
            del lista[1]
            lista.insert(1, novo_dt)
            print(dicionario)
    if menu == 3:
        novoano1 = int(input("novo ano de conclusão: "))
        novomes1 = int(input("novo mês de conclusão : "))
        novodia1 = int(input("novo dia de conclusão: "))
        novahora1 = int(input("nova hora de conclusão: "))
        novomin1 = int(input("novos minutos de conclusão: "))
        novadt1 = datetime(novoano1,novomes1,novodia1,novahora1,novomin1)
        for lista in dicionario.values():
            del lista[2]
            lista.insert(2, novadt1)
            print(dicionario)
    if menu == 4:
        nova_categoria = input("Qual é a nova categoria: ")
        for lista in dicionario.values():
            del lista[3]
            lista.insert(3, (nova_categoria,))
            print(dicionario)
    if menu == 5:
        nova_importancia = input("Qual é a nova importancia: ")
        for lista in dicionario.values():
            del lista[4]
            lista.insert(4, nova_importancia)
            print(dicionario)
def eliminar_tasks():
    menu = int(input("o que queres eliminar\n1-designação:\n2-categorias\n3-importancia\n"))
    if menu == 1:
        for lista in dicionario.values():
            del lista[0]
            print(dicionario)
    if menu == 2:
        for lista in dicionario.values():
            del lista[3]
            print(dicionario)
    if menu == 3:
        for lista in dicionario.values():
            del lista[4]
            print(dicionario)
    



            
        
        

   
        

    
           

                    
    
        
    
    


    

    













































while True:
    basic_function = int(input("1 - Gestão de Tarefas \n2 - Manutenção de Tarefas \n3 - Listagens \n"))

    if basic_function == 1:
        gestão_de_tarefas = input("(C) - criar \n(R) - Obter \n(U) - Atualizar \n(D) - Eliminar \n")
        if gestão_de_tarefas == "c":
            id = len(dicionario)+1
            create_task()
            print(dicionario)
        if gestão_de_tarefas == "r":
            obter_task()
        if gestão_de_tarefas == "u":
            atualizar_tasks()
        if gestão_de_tarefas == "d":
            eliminar_tasks()

            
           
