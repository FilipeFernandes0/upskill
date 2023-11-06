numbers = [10, 5, 6, 4, 2]
print(numbers)

numbers[0] = 112 #alterar numero na lista o zero significa a posiçao na lista
print(numbers)

numbers[1] = numbers [4] #igualar os numeros na lista 
print(numbers)

print(len(numbers))#len é o comprimento da lista 

numbers.append(12) #acrescenta um numero á lista
print(numbers)

numbers.extend([12,1,454,6]) #acrescenta vários numeros á lista
print(numbers)

del numbers[1] #elimina os numeros na lista 
print(numbers)

numbers.insert(3, "teste")
print (numbers)

my_list = [1,2,3,4,5]
inverted_list = my_list [:: -2] #inverte de dois em dois se for positivo é igual mas nao inverte
print(inverted_list)

my_list = [1,2,3,4,5]
my_list[0] = my_list[3]
print(my_list)
my_list[3] = my_list[0]
print(my_list)

inverted_list = my_list[::-1]
print(inverted_list)
my_list.reverse()
print(my_list)
print(my_list)
print(my_list[2:3])#apagar posiçoes [0:3:1]

my_list_2 = [1,2,3,3,2,4,5,6,2]
print(my_list_2)
my_list_2.remove(2) #remove o numero 2 mas só o primeiro que encontra 
print(my_list_2)

my_list_2.sort(reverse=True) #poe a lista por ordem descendente
print(my_list_2)

my_list_3 = [1,2,3,3,2,4,5,6,2]
sorted_my_list_3 = sorted(my_list_3, reverse=True)
print(my_list_3,"\n", sorted_my_list_3) #o sorted organiza a lista 

#exercicio1
#1. Criar uma listas de strings através de inputs e retornar a lista filtrada apenas com palavras que comecem por vogais.
#2. Filtrar uma lista e manter apenas strings com a letra 'b'
# que contenham a letra a
# que contenham a letra b



