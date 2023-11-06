

#exercicio1
#1. Criar uma listas de strings através de inputs e retornar a lista filtrada apenas com palavras que comecem por vogais.
#2. Filtrar uma lista e manter apenas strings com a letra 'b'
# que contenham a letra a
# que contenham a letra b

'''vogais = ["a","e","i","o","u"]    
list_filt = []
lista = []
n = 0

while n<=5:
    n += 1
    lista.append(input("introduza uma string: "))

for palavra in lista:
    if palavra[0].lower() in vogais:
        list_filt.append(palavra)

print(list_filt)

list_filt = [palavra for palavra in lista if palavra[0].lower() in vogais]
print(list_filt)'''
'''
pal = []
list_filt = []
lista = []
n = 0

while n<=5:
    n += 1
    lista.append(input("introduz uma palavra: "))

for palavra in lista:
    if "b" in palavra:
        pal.append(palavra)
print(pal)
'''
#exercicio 3
#3. Escreva uma função que receba um número inteiro n e retorne uma lista com n números inteiros aleatórios entre 0 e 255.
import random

'''n = int(input("numero: "))
lista = []

for aleatorio in range(0,n):
    lista.append(random.randint(0,255))
print(lista)'''

#exercicio 4
#Escreva uma função que receba uma lista de números inteiros e retorne uma nova lista contendo o OR bit a bit de cada número inteiro com 0x80. 

'''lista_numeros = [10, 20, 30, 40, 50]
resultado = []

for num in lista_numeros:
    resultado.append(num | 0x80)
print(resultado)'''

#Escreva uma função que receba uma lista de números inteiros e retorne uma nova lista contendo o XOR bit a bit de cada número inteiro com 0xFF. 
numeros = [10,20,30,40,50]
resultado = []

for num in numeros:
    resultado.append(num ^ 0xFF)
print(resultado)





