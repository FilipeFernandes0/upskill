def check_password_strenght(password):
    strenght = 0
    if len(password) >= 8:
        strenght +=1
    if any(char.isupper() for char in password): strenght += 1
    if any(char.islower () for char in password): strenght += 1
    if any(char.isalnum() for char in password): strenght += 1  
    if any(char.isdigit() for char in password): strenght += 1
    return strenght

password = input("enter a password: ")
password_strenght = check_password_strenght(password)
print("password strenght: ", password_strenght)