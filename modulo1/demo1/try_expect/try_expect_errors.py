# try:


#     value = int(input("enter a Natural number: "))
#     print("the reciprocal of",value, "is", 1/value)

# except ValueError:
#     print("i do not know what to do")

# except ZeroDivisionError:
#     print("division by zero is not allowed in our universe")

# except:
#       print("something strange has happened here...sorry")


temperature = float(input("enter current temperature: "))

if temperature > 0:
     print("Above zero")
elif temperature < 0:
     print("below zero")
else:
     print("Zero")

