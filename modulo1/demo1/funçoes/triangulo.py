'''def is_a_triangle(a,b,c):

    if b >= a + c:
        return False
    elif a >= b + c:
        return False
    elif c >= b+a:
        return False
    else:
        return True
    #return a + b > c and b + c > a and a + c > b forma mais fácil de definir 
    
a = 1
b = 1
c = 1

print(is_a_triangle(a,b,c))'''


#aplicar teorema de pitágoras

#a = float(input("valor de a: "))
#b = float(input("valor de b: "))
#c = float(input("valor de c: "))

'''def triangle(a,b,c):
     return a + b > c and b + c > a and a + c > b

def right_triangle(a,b,c):
     if not triangle(a,b,c):
          return False
     if c > a and c > b:
        return c**2 == b**2 + a**2 
     if a > b and a > c:
          return a**2 == b**2 + c**2
     #if b > a and b > c:
          #return b**2 == a**2 + c**2


print(right_triangle(a,b,c))'''


#área do triangulo

#def area_do_triangulo(a,b,c):
   # s = (a + b + c)/2
    #return (s*(s-a)*(s-b)*(s-c))**0.5
    
#print(area_do_triangulo(a,b,c))


#Fatoriais
#n = int(input("qual o numero: "))
def fatorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return fatorial(n-1)*n

    
    '''resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
      


#print(n, fatorial(n) ,sep="_")
num = int(input("qual o numero: "))
def fatorial_1(num):
    fact = 1 
    while num >= 1:
        fact *= num
        num -= 1
    return fact


print(num, fatorial_1(num))'''


print(fatorial(4))
