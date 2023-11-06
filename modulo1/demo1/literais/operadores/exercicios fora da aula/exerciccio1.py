 

'''num = float(input("escreve um numero: "))

if num >= 1.0 and num < 1.9:
    print("o numero está dentro do intervalo")
else:
    print("o numero nao está dentro do intervalo")'''


'''quantidade = float(input("quantia em €: "))
mercadoria = float(input("valor da mercadoria em €: "))
troco = quantidade - mercadoria


if quantidade < mercadoria:
    print("o valor que introduziu não é suficiente")
elif mercadoria != quantidade:
    print("o valor do troco é:", troco,"€")
    print("pagamento efetuado")
#elif quantidade < mercadoria:
    #print("o valor que introduziu não é suficiente")
else:
    print("o valor do dinheiro está correto nao é preciso troco")'''

#exercicio 3

import random 

#user = input("qual a chave secreta: ")
num_secreto = random.randint(0,200)
count = 0
choiches = 5

while choiches > count:
    user = int(input("qual a chave secreta: "))
    if user == num_secreto:
        print("congrats you have guessed the word :D", num_secreto)
        break
    elif user > num_secreto:
        print("your guess is too high")
    else:
        print("your guess is too low")
    count += 1

if count == choiches:
    print("you have run out of choiches unlucky :c")


    
