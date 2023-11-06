def calculate_fatorial():
    try:
        number = int(input("introduza um numero: "))
        if number <= 0:
            raise ValueError
        
        factorial = 1
        for i in range(1,number+1):
            factorial *= i

        print(f"o factorial de {number} é {factorial}")

    except ValueError:
       print(f"por favor introduza um inteiro positivo")



calculate_fatorial()