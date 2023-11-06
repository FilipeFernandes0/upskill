from sys import path

path.append("C:\\Users\\filip\\Desktop\\upskill\\modulosexercicios\\calculator")


import calculator


num1 = int(input("introduza um numero: "))
num2 = int(input("introduza um numero: "))

print(calculator.soma(num1,num2))
print(calculator.division(num1,num2))
print(calculator.subtratction(num1,num2))
print(calculator.multiplications(num1,num2))