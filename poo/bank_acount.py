#Exercise 1 Bank Account class 
#Create a Python class called BankAccount which represents a bank account, having as attributes: 
#accountNumber (numeric type), name (name of the account owner as string type), balance. 
#Create a constructor with parameters: accountNumber, name, balance. 
#Create a Deposit() method which manages the deposit actions. 
#Create a Withdrawal() method  which manages withdrawals actions. 
#Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account. 
#Create a display() method to display account details. 
#Give the complete code for the  BankAccount class. 


class BankAccount:
    def __init__(self, accountNumber,name,balance):

        self.__accountNumber = accountNumber
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance =  (amount + self.__balance)
        self.__balance = self.__balance - self.bankfees
        return f"your deposit is {self.__balance}"
        
    def Withdrawal(self,amount):
        if self.__balance < amount:
            return f"you have insuficient funds in your acount. you have {self.__balance}"
        else:
            self.__balance = self.__balance - amount - self.bankfees
            return f"withdrawal successful! Balance now is {self.__balance}"
        
    @property

    def bankfees(self):
        fee = 0.05 * self.__balance
        return fee
       
    

    def display(self):

        print("welcome to Filipe's bank")
        print(f"your acount number is:{self.__accountNumber}")
        print(f"your name is:{self.__name}")
        print(f"your Balance is:{self.__balance}")


criar = BankAccount(12345,"Filipe",0)
criar.display()
criar.bankfees
print(criar.deposit(200))
print(criar.Withdrawal(150))





        
