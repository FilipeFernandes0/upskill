

def check_password_strenght(password):
    
    password_strenght = 0
    if len(password) >= 8:
        password_strenght += 1
    for char in password:
        if char.lower():
           password_strenght +=1
        if char.upper():
            password_strenght += 1
        if char.isdigit():
            password_strenght += 1
        if char.isalnum():
           password_strenght =+ 1
    #password_strenght = 0
    return password_strenght

password = input("enter a password: ")
password_strenght = check_password_strenght(password)
print("password strenght: ", password_strenght)



