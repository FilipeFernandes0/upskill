


'''numero = int(input("escreve um numero: "))


if numero > 0:
    print("O numero é positivo")
elif numero == 0:
    print("o numero é igual a zero")
else: 
    print("o numero é negativo")

a = int(input("escreve um numero: "))

if a % 2 == 0:
    print("o numero é par")
else:
    print("o numero é impar")'''


'''a = int(input("escreve um numero "))

if a >= 0 and a<= 10:
    print("o numero está dentro de (0,10)")
else:
    print("o numero está fora de (0,10)")'''



'''miles = float(input("How many Miles: "))

if miles < 0:
    print("o numero é negativo")
else:
    km = 1.60934 * miles
    print(f"miles {miles} to {km} is km")'''


# Criar um programa usando um  if para calcular o consumo médio de combustível por quilómetro:

'''a = int(input("distancia percorrida em km: "))
b = int(input("combustivel gasto: "))

if a <= 0 or b <= 0:
    print("o calculo nao pode ser feito")
else:
    consumo_médio = a / b
    print("o consumo médio foi de:", consumo_médio)'''


'''a = int(input("introduza um numero: "))
b = int(input("introduza o segundo numero"))
if a > b:
    print(f"O numero {a} ascende o numero {b}")
elif a < b:
    print(f"o numero {b} ascende o numero {a}")
else:
    print("os numeros nao podem ser iguais")'''


# Um aluno sujeita-se a um exame. Escreva um programa para apresentar no ecrã 
# a classificação qualitativa dessa nota (valor inteiro) segundo os seguintes níveis: 
# 0 <= nota < 8 : mau;  
# 8 <= nota < 10 : insuficiente;  
# 10 <= nota < 14 : suficiente;  
# 14 <= nota < 18 : bom;  
# 18 <= nota <= 20 : excelente. 
# nota: o valor da nota do aluno deve ser introduzido através do teclado e pertencer ao intervalo [0,20]. 


'''nota = int(input("classificação da nota: "))

if nota < 0 or nota > 20:
    print("esta classificaçao está incorreta")
elif nota <= 0 or nota < 8:
    print("A classificaçao da nota é Má")
elif nota <= 8 or nota < 10:
    print("A classificaçao da nota é insuficiente")
elif nota <= 10 or nota < 14:
    print("A classificaçao da nota é suficiente")
elif nota <= 14 or nota < 18:
    print("A classificaçao da nota é bom")
else:
    nota <= 18 or nota <= 20
    print("A classificaçao da nota é excelente")'''

year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the gregorian calendar")
elif year % 4 != 0:
    print("common year")
elif year % 100 != 0:
    print("leap year")
elif year % 400 !=0:
    print("common year")
else:
    print("leap year")



