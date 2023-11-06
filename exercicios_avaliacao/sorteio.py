import random


# alunos = [i for i in range(1,20)]

# random.shuffle(alunos)

# for aluno in alunos[::-1]:
#     continuar = input("continuar (enter) ou terminar(Qualquer tecla)?")
#     if continuar == "":
#         alunos.pop()
#         print(aluno)
#         if len(alunos) == 0:
#             print("sorteio concluido")
#             break
#     else:
#         print("Sorteio concluido")
#         break



print("-----EX 2------")
alunos1 = []

# for i in range(1,20):
#     alunos1.append(utilizador = input("qual é o numero: "))
var = int(input("qual é o numero maximo: "))
#alunos1 = [i for i in range(1,var+1)]


for i in range(1, var+1):
    alunos1.append(var)
    random.shuffle(alunos1)

for aluno in alunos1:
    continuar = input("continuar (1) ou terminar?")
    if continuar == "":
        print(aluno)
    else:
        print("Sorteio concluido")
        break