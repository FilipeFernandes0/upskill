'''def scope_test(x):
    x = 123

scope_test(x)
print(x)'''

##################

#2 variables, different scopes same name

'''def my_function():
    global var
    var = 2 
    #var = 3
    print("do i know that variable?", var)

var = 1
my_function()
print(var)'''


#####

def my_function(n):#variavel n é dentro da funçao é local
    print("i got", n)
    n += 1
    global var
    var = n
    print("i have", n)

var = 1 #esta variavel é global
my_function(var)
print(var)

#######

a = 1
def fun():
    global a #como tem global a variavel dentro da funçao torna-se a maior, se nao tivesse global a = 3
    a = 2
    print(a)
a = 3
fun()
print(a)