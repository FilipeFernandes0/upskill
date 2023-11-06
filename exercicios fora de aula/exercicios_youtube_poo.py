#bank system

# class User:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def user_details(self):
#         print("User Details \n")
        
#         print("Name", self.name)
#         print("Age", self.age)
#         print("Gender", self.gender)    

# class Bank(User):
#     def __init__(self, name, age,gender):
#         super().__init__(name,age,gender)
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         return self.balance
#         #print("Account balance has been updated: €", self.balance)

#     def withdraw(self,amount):
#         self.amount = amount
#         if self.amount > self.balance:
#             print("insuficient funds, you can't withdraw that amount of money", self.balance)
#         else:
#             self.balance = self.balance - self.amount
#             print("you have sucessfully withdraw th amount of money, your balance is", self.balance)

#     def view_balance(self):
#         self.user_details()
#         print("your current balance is:", self.balance)

# filipe = Bank("Filipe", 21, "men")
# joao = Bank("Joao",30,"men")
# maria =  Bank("maria",27,"mulher")
# bruno = Bank("bruno",23,"men")

# filipe.user_details()
# joao.user_details()

# bruno.user_details()

# filipe.deposit(5000)
# joao.deposit(2000)
# bruno.deposit(60000)
# filipe.view_balance()
# bruno.view_balance()


###################################################################################################################



