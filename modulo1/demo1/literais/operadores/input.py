'''var1 = input("Introduza o valor ")
var2 = int(input("Introduza um valor inteiro: "))
var3 = float(input("introduza um valor float "))
print(var1, type(var1), var2, type(var2), var3, type(var3))'''

'''var1 = float(input("numero 1: " ))
var2 = float(input("numero 2: " ))

resultado = var1 + var2
resultado2 = var1 * var2
resultado3 = var1 - var2
resultado4 = var1 / var2
resultado5 = var1 ** var2
resultado6 = var1 % var2
print(resultado , resultado2, resultado3, resultado4, resultado5, resultado6, sep=" \n " )

print(f"soma = {var1} + {var2} = {resultado}")
print(f"soma = {var1} - {var2} = {resultado3}")
print(f"soma = {var1} * {var2} = {resultado2}")
print(f"soma = {var1} / {var2} = {resultado4}")
print(f"soma = {var1} ** {var2} = {resultado5}")
print(f"soma = {var1} % {var2} = {resultado6}")'''

'''x  = float(input("enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / x))) 

print("y = " , y)'''


hour = int(input("starting time(hours): "))
min = int(input("starting time(min): "))
dura = int(input("event duration(minutes): "))

min = min + dura #descobrir o total dos minutos
hour = hour + min // 60 #descobrir o numero de horas escondido nos minutos
min = min % 60 #minutos certos dentro do 0...59
hour = hour % 24 # hora certa dentro das horas 0..13

print(hour, ":", min, sep=" ")
