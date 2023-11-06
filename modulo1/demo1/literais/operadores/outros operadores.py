#a = 10 
#b = 5
#comparison operators


'''print( a==b ) #igualdade
print( a!=b ) #negar a comparaçâo 
print( a<b  ) #menor que
print( a>b  ) #maior que
print( a<=b ) #menor ou igual que
print( a>=b ) #maior ou igual que'''


#c = 3

'''#logical operators 
print(a > b and b > c)#basta um deles ser falso que fica falso
print(b > a or b < a)#basta um deles ser verdadeiro que um deles é verdadeiro
print(not(a > b or b > c))#nand, nor'''


#assignemnt operators 

'''a = 10
a += 5 # a=a+5 // a_agora = a_antes + 5

print(a)


b = 3 # b = b**2
b **= 2
print(b)

a = 0b1010 #representaçao binária de 10
b = 0b1011 #representaçao binária de 12

print(bin(a & b)) #and 1010/1100 = 1000 1/0 = 0 
print(bin(a | b)) #or 1010/1100 = 1110 1/0 = 1
print(bin(a ^ b)) #xor 1010/1100 = 110 1/1 = 0
print(bin(  ~a  ))#not ~a == -a-1
print(bin(a << 2))#shift
print(bin(b >> 1))'''


#identity operators

'''a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is not c) #true porque apesar das listas serem iguais nos numeros sao objetos diferentes por isso que sao diferentes '''


#membership operators

'''a = [1, 2 ,3]
b = 3
print(b in a)
print(4 not in a)


n = int(input("escreve um numero:"))

print(n>=100)
'''

'''largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number'''

a = None
b=None
a=int(input("a value: "))
b=int(input("b value: "))
if a==b: 
    print(f"o valor introduzido para 'a' ({a}) é igual ao valor introduzido para 'b' {b}")
elif a > b:
    print(f"o valor introduzido para 'a' ({a}) é maior que o valor introduzido para 'b' {b}")
else: 
    print(f"o valor introduzido para 'a' ({a}) é menor ao valor introduzido para 'b' {b}")










