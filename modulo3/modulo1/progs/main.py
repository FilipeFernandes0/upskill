

from sys import path

path.append("C:\\Users\\filip\\Desktop\\upskill\\modulo3\\modulo1\\modulo")


import module 

lista = ["diogo", "daniel", "filipe", "banana","morango"]


# print("o valor que vai ser recebido é o uirá", lista_append(lista, lista_apend))

# print("o valor que vai ser eliminado é: ", lista_del(lista, 0))

# print("o valor que vai ser lido é: ", lista_read(lista, 4))


while True:
    menu = int(input("Qual é a funçao que queres realizar 1, 2 ou 3 "))
    if menu == 1:
        lista_apend = input("qual é o item a introduzir: ")
        #lista_apend = item
        print("o valor que vai ser recebido é o uirá", module.lista_append(lista, lista_apend))
        
        break
    if menu == 2:
        list_del = int(input("qual é o item que vai ser eliminado: "))
        print("o valor que vai ser eliminado é: ", module.lista_del(lista, list_del))
        
        break
    if menu == 3:
        list_read = int(input("qual é o valor que vai ser lido: "))
        print("o valor que vai ser lido é: ", module.lista_read(lista, list_read))
        
        break
       
    #print("o valor que vai ser recebido :" lista_append(lista, item))


