#loop finito
'''i = 1
while i <= 10:
    print(i, end=" ")
    i+=1'''
#loop infinito
'''while True:
    print("isto é um loop infinito")
    break'''
####
#loop controlo de sentinela
'''sum = 0
while True:
    num = int(input("Introduza um numero (-1 até ao fim): "))
    if num == -1:
        break
    sum += num
print("Esta soma é", sum )'''

#loop controlado por condiçoes

'''num = int(input("Introduza um número: "))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print("o factorial é", factorial)'''

#nest

'''i = 1 
while i <= 10:
    j = 1
    while j <= 10:
        print(i*j, end="\t")
        j += 1
    print()
    i += 1'''

#pedir numero de 1, 10 funçao while 
'''while True:
   num = int(input("introduza um numero: "))
   if num >= 1 and  num <= 10:
        break
print("O numero é", num)'''

#pedir password ao utilizador 
#comparar password
#se certa "entrou no sistema"
#se errada "tenta novamente
'''password_1 = "és o rei"

while True:
    password = input("Introduza uma password: ")
    if password == password_1:
        break
    else:
        print("tenta novamente")
    
print("entrou no sistema")  ''' 

#secret_number = 777

#secret_number1 = int(input("write an integer nunmber: "))

'''while True:
        secret_number1 = int(input("write an integer nunmber: "))
        if secret_number1 == secret_number:
            print("well done, muggle! you are free now")
            break
        elif secret_number > secret_number1:
            print("youre too low!")
        elif secret_number < secret_number1:
            print("youre too high")
        else:
            print("Ha ha! You're stuck in my loop!")'''

'''Exercício 3: 
Apresente um script que permita calcular a média de números inteiros naturais, introduzidos pelo utilizador, 
sendo considerada a leitura do zero, como condição para terminar a operação de leitura. Para além da média, 
deverá ainda ser apresentado o número de valores lidos. 
Input/Output esperado: 
Teste 1: 
Valor 1: 12 
Valor 2: 15 
Valor 3: 8 
Valor 4: 0 
Média = 11.666666666666666 
   Nº = 3 
Teste 2: 
Valor 1: 0 
Erro: Número de valores > 0 '''


'''count = 0
soma = 0

while True:
 valor = int(input("valor: "))
 if valor == 0:
    break
 soma += valor
 count += 1
 print("valor",count,": ",valor)
 if count == 0:
    print("erro: Numero de valores > 0 ")
 if valor > 0:
  if count == 0:
    print("erro: Numero de valores > 0 ")
  media = soma/count
  #print("erro: numero de valores > 0")
  #media = soma/count
#print("média = ", media) 
#print("Nº", count)
 

print("média = ", media) 
print("Nº", count)'''


'''Um número é, por definição, primo se ele não tiver divisores, exceto 1 e ele próprio. Apresente um script que permita ler um número inteiro positivo não nulo e determinar se é ou não um número primo. 
Input/Output esperado: 
Teste 1: 
Número: 1 
É um número Primo 
Teste 2: 
Número: 125 
Não é um número primo 
Teste 3: 
Número: 86851 
É um número Primo '''

num = int(input("escreva um número: "))
primo = 1

for i in range(2, num):
    if num % i == 0:
        primo = 0

if primo == 1:
    print(num, "é primo")
else:
    print(num, "não é primo")



    












            




