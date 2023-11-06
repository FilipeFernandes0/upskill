#Crie um programa que crie uma lista com os 100 primeiros números pares positivos.
#a. Imprima todos os elementos;
#b. Imprima apenas o segundo elemento;
#c. Imprima o comprimento da lista;
#d. Imprima os números de 20 a 40;
#e. Imprima os números a partir de 50;
#f. Imprima os números até de 30 (inclusive);


'''lista = []
for i in range(0,100):
    if i % 2 == 0:
        lista.append(i)


print("numeros pares:", lista[15:])'''

#Crie uma lista com as equipas da 1ª divisão de futebol.
#a. Acrescente à lista três equipas à sua escolha;
#b. Insira o clube FC de Lamelas na posição 2 da lista;
#c. Retire da lista o Benfica;
#d. Retire o elemento da 5 posição;
#e. Se pretender apagar todos os elementos como procederia.


'''listam = ["FC_Porto", "Sporting", "Vitória_SC", "Belenenses", "SC_Braga", "Marítimo", "Rio_Ave", "Paços de Ferreira", "SC Covilhã"]

listam.insert(10, "guarda desportiva")
listam.insert(11, "benfica")
listam.insert(1, "lamelas")
print(listam)'''

#for clube in listam:
    #print(clube)


'''lista_2 = lista + listam
print(lista_2)'''


#Crie um programa com as seguintes condições:
#a. Crie uma lista vazia com o nome numeros;
#b. Acrescente à lista os primeiros mil números positivos;
#c. Apresente os números;
#d. Calcule a soma de todos os números;

'''numeros = []
soma = 0
for numero in range(1, 1001):    
    numeros.append(numero)
    soma += numero
    
print(soma)'''

#Crie uma lista com as letra do alfabeto.
#a. Apresente os valores
#b. Troque a letra A pela palavra A-INÍCIO
#c. Troque a letra Z pela palavra Z-FIM

'''lista_1 =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","y","u","v","x","w","z"]

#for palavra in lista_1:
   #lista_1.append(palavra)

lista_1[0] = "Inicio"
lista_1[25] = "Fim"
print(lista_1)
'''
#Considere a lista [1,4,2,5,6,2,3,7,9,8,10], crie um programa que utilize o algoritmo
#bublesort para ordenar os números. Deverá comentar devidamente todo o código.

'''lista = [1,4,2,5,6,2,3,7,9,8,10]

n = len(lista)

for i in range(n-1):


    for j in range(n-1-i):

       if lista[j] > lista[j+1]:
           lista[j], lista[j+1] = lista[j+1], lista[j] 

print(lista)'''

'''#Crie um programa com o algoritmo bublesort que permita ao utilizador:
#a. Inserir o número de elementos que pretende ordenar;
#b. Inserir os elementos a ordenar;
#c. Apresente os valores ordenados.

num = int(input("numero de elementos: "))
#num_1 = int(input("quais são os numeros que pretendes ordenar: "))

lista = []

for i in range(num):
    elemento= int(input(f"digite o elemento{i+1}: "))
    lista.append(elemento)

n = len(lista)


for i in range(n-1):


    for j in range(n-1-i):

       if lista[j] > lista[j+1]:
           lista[j], lista[j+1] = lista[j+1], lista[j] 
           
print("valores ordenados: ", lista)'''


'''# Solicitar ao usuário o número de elementos
num_elementos = int(input("Digite o número de elementos a ordenar: "))

# Criar uma lista vazia para armazenar os elementos
elementos = []

# Solicitar ao usuário os elementos e adicioná-los à lista
for i in range(num_elementos):
    elemento = int(input(f"Digite o elemento {i+1}: "))
    elementos.append(elemento)

# Bubble Sort para ordenar os elementos
n = len(elementos)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if elementos[j] > elementos[j + 1]:
            elementos[j], elementos[j + 1] = elementos[j + 1], elementos[j]

# Apresentar os valores ordenados
print("Valores ordenados:", elementos)
'''
#Considere a lista minha_lista1 = [1, 5, 12, 144, 23, 25, 46, 85], utilize o método sort
#para ordená-la e apresente-a.
#a. Crie um programa que calcule o valor máximo 

minha_lista1 = [1, 5, 12, 144, 23, 25, 46, 85]

w = len(minha_lista1)

for i in minha_lista1:
    minha_lista1.sort()
    i == w
print(minha_lista1)
print(i)

#Crie um programa com uma lista lista_a todos os meses do ano.
#a. Apresente os valores em ordem inversa;
#b. Apresente por ordem inversa um mês por linha;
#c. Verifique se setembro pertence à lista;
#d. Verifique se Outono pertence à lista
#e. Crie uma cópia da lista_a;

