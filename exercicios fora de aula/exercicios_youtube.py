#word replacement


# def replace_word():
    

#     str = "ola tudo bem, ola,ola,ola"
#     word_replace = input("enter the word you want to replace: ")
#     word_replacement = input("what word you want to replace with: ")

#     print(str.replace(word_replace,word_replacement))

# replace_word()

###########################################################################################

#basic calculator

# def add(a,b):
#     answer = a+b
#     print(str(a) + "+" + str(b) + "=" + str(answer))

# def sub(a,b):
#     answer = a-b
#     print(str(a) + "-" + str(b) + "=" + str(answer))

# def multiplication(a,b):
#     answer = a*b
#     print(str(a) + "*" + str(b) + "=" + str(answer))
# def division(a,b):
#     answer = a/b
#     print(str(a) + "/" + str(b) + "=" + str(answer))


# while True:
#     print("A : addition")
#     print("B : subtraction")
#     print("C : multiplication")
#     print("D : division")

#     question = input("enter your choice: ")
#     if question == "a" or question == "A":
#        a = int(input("what is your first number: "))
#        b = int(input("what is your second number: "))
#        add(a,b)
#     elif question == "b" or question == "B":
#          a = int(input("what is your first number: "))
#          b = int(input("what is your second number: "))
#          sub(a,b)
#     elif question == "c" or question == "C":
#          a = int(input("what is your first number: "))
#          b = int(input("what is your second number: "))
#          multiplication(a,b)
#     elif question == "d" or question == "D":
#          a = int(input("what is your first number: "))
#          b = int(input("what is your second number: "))
#          division(a,b)

######################################################################

#email slicer

# def main():
#     print(" welcome to the email slicer ")
#     print("")

#     email_input = input("enter your email adress: ")

#     (username , domain) = email_input.split("@")
#     (domain, extension) = domain.split(".")
#     print("username: ", username)
#     print("domain: ", domain)
#     print("extension: ", extension)

# main()

######################################################################

#binary search

# def binary_search(list, element):
#     start = 0
#     end = len(list)
#     middle = 0

#     while (start <= end):
#         #print(list[start:end+1])
        
#         middle = (start + end) //2
#         if element == list[middle]:
#             return middle
#         if element < list[middle]:
#             end = middle -1 
            
#         if element > list[middle]:
#             start = middle + 1
#             print(list[start:end+1])
#     return -1
            

    
    

# list=[1,2,3,4,5,6,7,8,9,10]
# target = 6

# binary_search(list,target)

###########################################################################################

#quiz program


# quiz = {
#     "question1" : {
#         "question": "what is the capital of France", 
#         "answer" : "paris"
#         },
#     "question2" : {
#         "question": "what is the capital of Spain", 
#         "answer" : "Madrid"
#         },
#     "question3" : {
#         "question": "what is the capital of Angola", 
#         "answer" : "Luanda"
#         },
#     "question4" : {
#         "question": "what is the capital of Portugal", 
#         "answer" : "Lisboa"
#         },
#     "question5" : {
#         "question": "what is the capital of England", 
#         "answer" : "londres"
#         },
#     "question6" : {
#         "question": "what is the capital of Austria", 
#         "answer" : "viena"
#         },
#     "question7" : {
#         "question": "what is the capital of Brasil", 
#         "answer" : "Brasilia"
#         },
#     "question8" : {
#         "question": "what is the capital of Australia", 
#         "answer" : "camberra"
#         },
#         }

# score = 0

# for key,value in quiz.items():
#     print(value["question"])
#     answer = input("Answer: ")
#     if answer.lower() == value["answer"].lower():
#         print("you are correct")
#         score += 1
#         print("your score is: ", score)
#     else:
#         print("you missed")
#         print("the answer was", value["answer"])
#         print("your score is", score)

        

# print("you got", score, "out of 8 questions correctly")
# print("your percentage is", int(score/8*100),"%")

##############################################################################

#Qr code

# import qrcode

# def generate_qrcode(text):


#     qr = qrcode.QRCode(
#         version=1,
#         error_correction= qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4
#     )

#     qr.add_data(text)
#     qr.make(fit = True)
#     img = qr.make_image(fill_color = "black", back_color = "white")
#     img.save("qrcode.png")



# url = "https:\\www.youtube.com/"

# generate_qrcode(url)

##############################################################################
#monthly loan calculator

# def main():
#     print("welcome to the loan calculator")
#     print("")


#     principal = float(input("enter the amount of money: "))
#     apr = float(input("what is the apr: "))
#     years = int(input("enter the amount of years: "))

#     monthly_interest_rate = apr /1200
#     amount_of_months = years * 12
#     monthly_payment = principal * monthly_interest_rate / (1-(1+monthly_interest_rate)**(-amount_of_months))

#     print("the monthly payment for the loan is: %.2f" % monthly_payment)


# main()

##############################################################################
#generate random password

# import string
# import random

# characters = list(string.ascii_letters + string.digits + "!#$%&/()")

# def generate_password():
#     password_lenght = int(input("what is your password lenght: "))

#     #random.shuffle(characters)
#     password = []

#     for x in range(password_lenght):
#         password.append(random.choice(characters))
    
#     #random.shuffle(password)

#     password = "".join(password)

#     print(password)


# generate_password()

##############################################################################

#roll dice
# import random
# def roll_dice():

#     roll = input("do you want to roll the dice (yes/no)")
#     while roll == "yes".lower():
#         dice1 = random.randint(1,6)
#         dice2 = random.randint(1,6)
#         print("you roled a", dice1, dice2)
#         roll = input("do you want to roll the dice again (yes/no)")
    
# roll_dice()


##############################################################################
#site connectivity checker
# import urllib.request as urllib

# def main(url):
#     print("checking connectivity  ")
#     response = urllib.urlopen(url)
#     print("connected to", url, "succesfully")
#     print("the response was", response.getcode())

# print("this is a site conectivity tester")
# input_url = input("input the url of the site you want to check: ")

# main(input_url)

##############################################################################
#currency converter

# def main():
#     print("this program converts US dollars to pounds")
#     print()

#     dollars = eval(input("amount of dollars you want to convert: "))
#     #convert_to_pounds=  dollars * 0.85

#     pounds = convert_to_pounds(dollars)

#     print("that is", pounds, "dollars")



# convert_to_pounds=  lambda dollars: dollars * 0.85
# #dollars = eval(input("amount of dollars you want to convert: "))
# main()

####################################################################################

#rock,paper,scissors game

# import random

# computer_points = 0
# user_points = 0
# exit = False

# while exit == False:
#     game = ["rock","paper","scissors"]
#     computer_input = random.choice(game)
#     user_input = input("what are you going to chose: rock,paper,scissors,exit: ")
    
#     if user_input == "exit":
#         print("the game ended")
#         print("the computer score was: ", computer_points)
#         print("the user score was: ", user_points)
#         exit = True
        

#     if user_input == "rock":
#         if computer_input == "rock":
#             print("the user chose rock")
#             print("the computer chose rock")
#             print("It's a tie")
#         if computer_input == "paper":
#             print("the user chose rock")
#             print("the computer chose paper")
#             print("the computer won")
#             computer_points += 1
#         if computer_input == "scissors":
#             print("the user chose rock")
#             print("the computer chose scissors")
#             print("the user won")
#             user_points +=1

#     elif user_input == "paper":
#         if computer_input == "rock":
#             print("the user chose paper")
#             print("the computer chose rock")
#             print("the user won")
#             user_points +=1
#         if computer_input == "paper":
#             print("the user chose paper")
#             print("the computer chose paper")
#             print("it's a tie")
            
#         if computer_input == "scissors":
#             print("the user chose paper")
#             print("the computer chose scissors")
#             print("the computer won")
#             computer_points +=1

#     elif user_input == "scissors":
#         if computer_input == "rock":
#             print("the user chose scissors")
#             print("the computer chose rock")
#             print("the computer won")
#             computer_points +=1
#         if computer_input == "paper":
#             print("the user chose scissors")
#             print("the computer chose paper")
#             print("the user won")
#             user_points +=1
            
#         if computer_input == "scissors":
#             print("the user chose scissors")
#             print("the computer chose scissors")
#             print("it's a tie")
#     elif user_input != "rock" or user_input != "paper" or user_input != "scissors" or user_input != "exit":
#         print("invalid keyword try again")

#######################################################################################################################

            
    


