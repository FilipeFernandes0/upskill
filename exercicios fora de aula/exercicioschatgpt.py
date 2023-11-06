#Crie uma função que receba como parâmetro uma lista de números e retorne a soma de todos os elementos dessa lista.


# lista = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# def retornarsum(lista, sum):
#     for num in lista:
#         sum += num 
#         print(sum)

# retornarsum(lista, sum)

#Escreva uma função que receba um dicionário como parâmetro, 
#contendo nomes de pessoas como chaves e suas idades como valores, 
#e retorne o nome da pessoa mais velha.


# dicionario = {"Daniel": 21,
#               "Teixeira" : 22,
#               "Gia": 24,
#               "Filipe": 21,
#               "Diogo": 25,
#               "Uirá": 41
#               }


# def retornar_valor(dicionario):
#     #nome_mais_Velho = " "
#     idade_mais_velho = 0

#     for nome, idade in dicionario.items():
#         if idade > idade_mais_velho:
#             #nome_mais_Velho = nome
#             idade_mais_velho = idade


#     return idade_mais_velho


# print(retornar_valor(dicionario))
        

#Crie uma função que receba uma lista de strings como parâmetro 
#e retorne uma nova lista contendo apenas as strings que começam com a letra "A".

# list = ["ana", "ola", "andre", "ananas"]

# def lista_de_string():
#     nova_lista = []
#     for string in list:
#         if string[0] == "a":
#             nova_lista.append(string)
#     return nova_lista


# #list = ["ana", "ola", "andre", "ananas"]    

# resultado = lista_de_string()
# print(resultado)


#Escreva uma função que receba um dicionário como parâmetro, 
#onde as chaves são nomes de frutas e os valores são as quantidades de cada fruta. 
#A função deve retornar a fruta mais comum (aquela com a maior quantidade).


# def dic_frutas(dicionario):
#     name_bigest_fruit = " "
#     biggest_fruit = 0
#     for name, fruit in dicionario.items():
#         if fruit > biggest_fruit:
#            name_bigest_fruit = name
#            biggest_fruit = fruit
#     return name_bigest_fruit


# dicionario = {"maça": 20,
#               "pera": 1000,
#               "banana": 100000,
#               }

# resultado = dic_frutas(dicionario)
# print(resultado)


#Crie uma função que receba uma lista de números como parâmetro e retorne uma nova lista contendo apenas os números pares.

# def lista_de_numeros(lista):
#     new_list = []
    

#     for number in lista:
#         if number % 2 == 0:
#             new_list.append(number)
#     return new_list

# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# resultado = lista_de_numeros(lista)

# print(resultado)

#Escreva uma função que receba um dicionário como parâmetro, 
#onde as chaves são nomes de países e os valores são suas capitais. 
#A função deve receber o nome de um país e retornar sua capital.

# def retornar_capital(dicionario):

#     pais = input("Qual é o nome do país: ")
#     if pais in dicionario:
#         return dicionario[pais]
#     else:   
#         return "país nao encontrado"
           
# capitais = {"portugal": "lisboa",
#               "franca": "paris",
#               "espanha": "madrid",
#               "inglaterra": "londres"}
# capital = retornar_capital(capitais)
# print("A capital é", capital)


#Crie uma função que receba uma lista de palavras como 
#parâmetro e retorne um dicionário onde as chaves são as palavras e os 
#valores são o número de vezes que cada palavra aparece na lista.

# def retornar_palavras(lista):

#     dicionario = {}

#     for strings in lista:
#         if strings in dicionario:
#             dicionario[strings] +=1
#         else:
#             dicionario[strings] = 1
#     return dicionario
            


# lista = ["Filipe","Filipe","Filipe","Filipe", "Daniel","Daniel","Daniel"]

# resultado = retornar_palavras(lista)
# print(resultado)

#Escreva uma função que receba um dicionário como parâmetro, 
#onde as chaves são nomes de pessoas e os valores são suas alturas. 
#A função deve retornar o nome da pessoa mais alta.

# def retornar_alturas(dicionario):
#     nome_pessoa_alta = None
#     altura_pessoa_alta = 0

#     for nome, altura in dicionario.items():
#         altura > altura_pessoa_alta
#         nome_pessoa_alta = nome
#         altura_pessoa_alta = altura
#     return nome_pessoa_alta
    

# dicionario = {"Filipe": 1.79,
#               "Daniel": 1.73,
#               "Uirá": 1.83,
#               "Pedro": 1.89,
#               "Gonçalo": 1.91
#               }

# resultado = retornar_alturas(dicionario)
# print(resultado)^

#Escreva uma função contar_letras(palavra) que recebe uma palavra como parâmetro e 
#retorna um dicionário com a contagem de cada letra na palavra. 
#Por exemplo, ao chamar a função com a palavra "banana", 
#o resultado seria {'b': 1, 'a': 3, 'n': 2}.

# def contar_letras(palavra):
#     dicionario = {}
#     #count = 0

#     for word in palavra:
#         if word in dicionario:
#             dicionario[word] +=1
#         else:
#             dicionario[word] = 1
#     return dicionario
       
# resultado = contar_letras("banana")
# print(resultado)


#Escreva uma função unir_dicionarios(dicionario1, dicionario2) 
#que recebe dois dicionários como parâmetros e 
#retorna um novo dicionário que é a união dos dois dicionários de entrada.

# def unir_dicionarios(dicionario1, dicionario2):
#     dicionario_novo = dicionario1.copy()
#     dicionario_novo.update(dicionario2)
#     return dicionario_novo


# dicionario1 = {'a': 1, 'b': 2}
# dicionario2 = {'c': 3, 'd': 4}
# resultado = unir_dicionarios(dicionario1, dicionario2)
# print(resultado)


#Escreva uma função remover_duplicatas(lista) que recebe uma 
#lista como parâmetro e retorna uma nova lista contendo apenas os elementos únicos, 
#removendo as duplicatas. A ordem dos elementos na nova lista deve ser preservada.

# def remover_duplicatas(list):
#     new_lista = []

#     for elemento in list:
#         if elemento not in new_lista:
#             new_lista.append(elemento)
#             new_lista.sort()
        
#     return new_lista


# list = [1,2,4,5,6,7,1,2,3,]
# resultado = remover_duplicatas(list)

# print(resultado)


#Escreva uma função maior_palavra(frase) que recebe uma frase 
#como parâmetro e retorna a maior palavra presente na frase. 
#Se houver mais de uma palavra com o mesmo tamanho máximo, 
#a função deve retornar a primeira palavra encontrada.

# def maior_palavra(frase):
#     #frase = "estou fodido pois tenho de fazer o jogo da batalha naval"

#     for word in frase:
#         if word > frase:
#             return word

# frase = "estou fodido pois tenho de fazer o jogo da batalha naval"

# resultado = maior_palavra(frase)

# print(resultado)


#Fatorial: Escreva uma função que calcula o fatorial de um número inteiro não negativo. 
#Desafio: tente implementar a função de forma recursiva.

# def numero_fatorial(fatorial):
#     resultado = 1

#     for i in range(1, fatorial+1):
#         resultado *= i
#     return resultado
    
# resultado = numero_fatorial(4)
# print(resultado)


# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#        return n * fatorial(n -1)

# print(fatorial(4))

#Fibonacci: Escreva uma função que retorna o n-ésimo número da sequência de Fibonacci. 
#A sequência de Fibonacci é formada pela soma dos dois números anteriores, começando por 0 e 1. 
#Por exemplo, os primeiros números da sequência são 0, 1, 1, 2, 3, 5, 8, 13, ...

# def fibonacci(n):
#     if n <= 0:
#         return "o numero tem de ser um inteiro"
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
    
#     else:
#         fib_1 = 1
#         fib_2 = 0
#         fib_current = 0

#         for _ in range(3, n+1):
#             fib_current = fib_1 + fib_2
#             fib_2 = fib_1
#             fib_1 = fib_current
#         return fib_current
    
# print(fibonacci(6))

#Verificação de palíndromo: Escreva uma função que verifica se uma palavra ou frase é um palíndromo, 
#ou seja, se pode ser lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda. 
#Desconsidere espaços em branco e diferenças entre letras maiúsculas e minúsculas. 


# def palindrome_checker(palindrome):
  
#     palindrome = palindrome.replace(" ","").lower()

#     return palindrome == palindrome[::-1]

# print(palindrome_checker("olaaa"))
# def solveMeFirst(a,b):
#     sum = a + b
#     return sum
    

# num1 = int(input("introduz um numero: "))
# num2 = int(input("introduz um numero: "))
# res = solveMeFirst(num1,num2)
# print(res)

#Algoritmo de ordenação: Implemente uma função chamada bubble_sort que recebe uma lista de números 
#como parâmetro e retorna a lista ordenada em ordem crescente usando o algoritmo Bubble Sort.

    
    







