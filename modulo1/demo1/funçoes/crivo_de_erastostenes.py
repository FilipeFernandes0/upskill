def primos(n):
    nums = []
    if n < 2:
        return nums
    vals = [True for i in range(n)]
    vals[0] = vals[1] = False
    for i in range(2,n):
        if vals[i]:
            nums += [i]
            for j in range(i*i,n,i):
                vals[j] = False
    return nums
num = int(input("numero primo: "))
while num > 0:
    print("primos: ", primos(num))
    num = int(input("novo número(0 para terminar): "))








    
        

