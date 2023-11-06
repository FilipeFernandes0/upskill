# import random
# count = 4
# computer = random.randint(1, 20)
# while True:
#     #user = (input(f"qual é o numero que queres tens {count} tentativas"))
    
#     count -= 1
#     #count = 3
#     user = int((input(f"qual é o numero que queres tens {count} tentativas: ")))
#     #user = (input("qual é o numero que queres tens", count, "tentativas"))
#     #computer = random.randint(1, 20)
#     if count == 0:
#         print("excedeste as tentativas campeão o numero era:", computer)
#         break
#     #user = int((input(f"qual é o numero que queres tens {count} tentativas: ")))
#     if user >= 1 and user <= 20:
#         if user == computer:
#             print("acertaste o numero era: ", computer)
#             break
#         elif user < computer:
#             print("o numero inserido é mais baixo campeão")
#         elif user > computer:
#             print("o numero inserido é mais alto campeão")
#         elif count == 0:
#             print("excedeste as tentativas campeão o numero era:", computer)
#             break
#     else:
#         print("o numero nao pode ser mais alto que 1 e 20!!!")


from datetime import datetime, date

# data = datetime(2023,5,26)

# print(data)

#agora = datetime.now()

# print(agora)


# data_1 = datetime(2020,9,5)
# data_2 = datetime(1994,5,3)

# data_3 = data_1 - data_2

# print(data_3)^
#nascimento = datetime(2001,9,5)

# data_4 = (date.today())

# #print(ano)    
# #nascimento = int(input("qual foi o ano que nasceste: "))

# #diferenca = ano - nascimento
# #print(diferenca)
# ano = data_4.year
# dia = data_4.day
# mes = data_4.month

# nascimento = int(input("qual foi o ano que nasceste: "))
# nascimento_1 = int(input("qual foi o mes que nasceste: "))
# nascimento_2 = int(input("qual foi o dia que nasceste: "))




# # diferenca_1 = nascimento_1 
# # diferenca_2 = dia - nascimento_2
# # diferenca = ano - nascimento
# # #print(diferenca_1)
# # #print(diferenca_2)
# # print(diferenca_1,diferenca_2,diferenca)^

# tirar = ano - nascimento_2/365 - nascimento_1/12 - nascimento
# #tirar_1 = mes*4 - nascimento_1
# #tirar_3 = dia*30 - nascimento_2
# idade = int(tirar)
# print(idade) #tirar_1, #tirar_3



# data_nascimento_str = "2001-09-05"
# # formato = "%y-%m-%D"
# # hora_str = "14:30:45"^
# # formato_hora = "%h:%m:%S"

# year = datetime.strftime(data_nascimento_str,"%Y")
# print("year", year)

from platform import python_implementation, python_version_tuple

print(python_implementation())
for atr in python_version_tuple():
    print(atr)

