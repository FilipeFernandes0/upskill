
#Crie um algoritmo que apresente os 50 primeiros números inteiros positivos.

'''for i in range(1,51):
    print(i, sep=", ", end=" ")'''

#Crie um ciclo que apresente os 500 primeiros números inteiros pares positivos. 

'''var = 0
count = 0
while var < 500:
    #print(var)
    var += 2
    count += 1
    print(var)'''

#Crie um ciclo que apresente os 500 primeiros números inteiros ímpares positivos. 

'''var = 1
count = 0
while var < 500:
    if var % 2 != 0:
        print(var)
        count +=1
    var += 1
    if var == 121:
        break'''

#Crie um ciclo que apresente os 500 primeiros números inteiros pares positivos e que
#escreva nos valores 100, 200, 300, 400, 500 escreva “Já cheguei aos 100”

'''var = 0
count = 0

while var < 500:
    var += 2
    count +=1
    print(var)
    if var == 100:
        print("ja cheguei ao 100")
    elif var == 200:
        print("ja cheguei aos 200")
    elif var == 300:
        print("ja cheguei aos 300")
    elif var == 400:
        print("ja cheguei aos 400")
    elif var == 500:
        print(" cheguei aos 500")
'''
#Faça o algoritmo de um programa que leia um número inteiro e calcule todos os
#seus múltiplos inferiores a 100. Implemente o algoritmo em linguagem Python.
#while
'''num = int(input("qual  o numero?: "))
multiplo = num

while multiplo < 100:
    print(multiplo)
    multiplo += num'''

#Elabore um programa que determine todos os números pares entre dois
#números inteiros ni e nf (ni<nf).

'''ni = int(input("numero: "))
nf = int(input("nf: "))
print(f"Os números pares entre {ni} e {nf} são: ")
numero = ni
while numero < nf:
    if ni % 2 != 0:
        ni += 1
    numero += 2
    print(numero)'''
    
#Escreva um programa em Python que leia um número inteiro positivo N e calcule
#o maior número par P tal que a soma de todos os números pares até P seja
#inferior a N. Por exemplo, se for dado o valor 57 para N então o resultado será
#P=14 pois 2 + 4 + 6 + 8 + 10 + 12 + 14 = 56 < 57 e 2 + 4 + 6 + 8 + 10 + 12 + 14 + 16
#>= 57.

   
'''n = int(input("numero: "))
count= 0
soma = 0

while soma < n:
    count += 2
    soma += count
    if soma >= n:
        break

print(f"O maior número par P tal que a soma dos números pares até count seja inferior a {n} é: {count}")'''

#Elabore um algoritmo que peça ao utilizador para introduzir um número entre 0
#e 9 e enquanto não seja introduzido um valor válido seja repetida a leitura.

'''n = int(input("escolhe um numero entre 0 e 9: "))

while n < 0 or n > 9:
    n = int(input("escolhe um numero entre 0 e 9: "))
   
print("escolheste o numero certo ")'''

#Faça o algoritmo de um programa que leia números reais até que o utilizador
#introduza um número x[10, 15.5]. Implemente o algoritmo em linguagem
#Python.
'''n = float(input("escreve um numero: "))
while True:
    n = float(input("escreve um numero: "))
    if 10 <= n <= 15.5:
        break'''
#Faça um algoritmo para um programa que leia uma sequência de números
#inteiros positivos e determine quantos números são pares e quantos são
#ímpares. A finalização da sequência de números é indicada introduzindo-se um
#número negativo.


'''num_pares = 0
num_impares = 0

while True:
    n = int(input("numero inteiro: "))
    if n < 0:
        break

    if n % 2 == 0:
        num_pares +=1
    else:
        num_impares += 1

print("introduziu um numero negativo")
print("sao estes numeros pares", num_pares)
print("sao estes numeros impares", num_impares)'''
    
#Elabore um programa que determine os n primeiros múltiplos de um número
#inteiro m.

'''m = int(input("introduza um numero: "))
n = int(input("quantos multiplos queres: "))
count = 0
multiplos = 0
while count < n:
    multiplos += m
    print(multiplos)
    count += 1'''
   



