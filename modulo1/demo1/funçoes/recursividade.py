'''def sum_of_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remainig_digits = n // 10
    return last_digit + sum_of_digits(remainig_digits)




print(sum_of_digits(12345))'''

'''def sum_of_numbers(n):
#convert to string
    num_str = str(n)
#if number has only one digit return as integer
    if len(num_str) == 1:
        return int(num_str)
    #recursive case sum of all numbers and loop again
    return int(num_str[0]) + sum_of_numbers(int(num_str[1:]))
print(sum_of_numbers(12345))'''


'''soma = 0
n = 32431341324
num_str = str(n)

for i in range(0, len(num_str)):
    soma += int(num_str[i])
    print(soma)'''




