'''
criar class library
atributos - > name e books (lista de titulos de livros)
metodos addbook() e remove book() e display book() -> mostrar os livros todos

2-

class product
atributos -> name, price, quantity
metodos -> increase_quantity() e calculate_total_price()

3-
class employee
atributos -> name, position, salary
metodos -> apply:raise

4- vehicle Hierarchy:
create a class called vehicle with atributtes brand and model
create two subclasses, car and motorcycle, that inherit from vehicle
implement additional atributes and methods specific to each vehicle type

exercise:
extend the vehicle class to include an abstract method called start_engine().
implement the method in each subclass to display a message indicating
how the engine of the vehicle is started'''

# class Library:
#     def __init__(self,name):
#         self.name = name
#         self.books = []
#     def add_book(self, title_book):
#         self.books.append(title_book)
#     def remove_book(self, title_book):
#         self.books.remove(title_book)
#     def display_book(self):
#         print("books in:", self.name)
#         for book_title in self.books:
#             print(book_title)


# my_library = Library("minha biblioteca")

# my_library.add_book("crime e castigo")

# my_library.add_book("caim")

# my_library.add_book("anjos e demonios")

# my_library.display_book()

# my_library.remove_book("caim")

# my_library.display_book()


# class Product:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def increase_quantity(self, amount):
#         self.quantity += amount
#     def calculate_total_price(self):
#         return self.price * self.quantity
    

# my_product = Product("colgate",12.0, 15)
# print("Name:", my_product.name)
# print("Price:", my_product.price)
# print("Quantity:", my_product.quantity)

# my_product.increase_quantity(5)
# print("new quantity", my_product.quantity)

# print(my_product.calculate_total_price())

# class Employee:
#     def __init__(self,name, position, salary):
#         self.name = name 
#         self.position = position
#         self.salary = salary

#     def apply_raise(self, raise_amount):
#         self.salary += raise_amount


# new_employe = Employee("Filipe", "Programador", 1500)

# new_employe.apply_raise(0.1*new_employe.salary)

# print("employe:", new_employe.salary)


# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
    
# class Car(Vehicle):
#     def __init__(self, brand, model,cost):
#         super().__init__(brand, model)
#         self.cost = cost

#     def engine_start(self):
#         print("woooosh!!")

# class Motorcycle(Vehicle):
#     def __init__(self,brand,model, cost):
#         super().__init__(brand,model)
#         self.cost = cost
#     def engine_start(self):
#         print("vrummmmmm!!")


# car = Car("lamborghini","aventandor",5000000000)
# print(car.brand)
# print(car.model)
# print(car.cost)


# car.engine_start()

# mota = Motorcycle("Kawasaki","Lipão", 50000)
# print(mota.brand)
# print(mota.model)
# print(mota.cost)
# mota.engine_start()



#1 - Blog Management System  
#Create a class called BlogPost that represents a blog post. The BlogPost class should have the following attributes: 
#title: The title of the blog post (string). 
# content: The content of the blog post (string). 
# author: The author of the blog post (string). 
# comments: A list to store the comments on the blog post (list of strings). 
# Implement the following methods for the BlogPost class: 
# add_comment(comment): Adds a comment to the list of comments. 
# get_comments(): Returns the list of comments. 
# display_info(): Displays the information of the blog post, including the title, author, content, and comments. 


# class BlogPost:
#     def __init__(self,title,content,author):

#         self.title = title
#         self.content = content
#         self.author = author
#         self.comments = []


#     def add_comment(self,comment):
        
#         self.comments.append(comment)
#         return self.comments

#     def get_comments(self):

#         return self.comments
    
#     def display_info(self):
#         print(" information about the blogist ")
#         print("")

#         print("Title:" , self.title)
#         print("content:" , self.content)
#         print("author:" , self.author)
#         print("comments")
#         for comment in self.comments:
#             print("-", comment)

# blog = BlogPost("bem vindo", "bananas", "Filipe")

# print(blog.add_comment("que bonito"))
# print(blog.add_comment("uau aprendi muito sobre bananas"))
# print(blog.add_comment("Fantastico"))



# print(blog.get_comments())

# print(blog.display_info())

# Car Rental System  

# Create a car rental system that manages car inventory and reservations. Implement the following functionalities: 
# Create a class called Car that represents a car in the rental system. The Car class should have the following attributes: 
# brand: The brand of the car (string). 
# model: The model of the car (string). 
# available: The availability status of the car (boolean). 
# Implement the following methods for the Car class: 
# reserve(): Reserves the car if it is available. 
# release(): Releases the car if it is not already available. 
# display_info(): Displays the information of the car, including the make, model, and availability status. 

# class Car:
#     def __init__(self, brand, model):

#         self.brand = brand
#         self.model = model
#         self.available = True

#     def reserve(self):
#         if self.available == True:
#             print("this car can be reserve")
#             print("car brand:", self.brand)
#             print("car model:", self.model)
#             self.available = False
#         else:
#             print("this car can't be reserved")

#     def release(self):

#         if not self.available:
#             print("this car has already been released")
#             self.available = True

#         else:
#             print("this car can be reserve")
#             print("car brand:", self.brand)
#             print("car model:", self.model) 

#     def display_info(self):
#         print(" welcome to my car rental ")
#         print("")

#         print("car brand:", self.brand)
#         print("car model:", self.model)
#         print("Availability:", "Available" if self.available else "Not Available")




# costumer = Car("Ferrari","xc700")

# costumer.reserve()

# costumer.release()

# costumer.display_info()


# Bank Loan Management  

# Build a bank loan management system that handles loan applications and approvals.  
# Create a class called Loan that represents a loan in the bank loan management system. The Loan class should have the following attributes: 
# customer_name: The name of the loan customer (string). 
# amount: The loan amount (float). 
# interest_rate: The interest rate of the loan (float). 
# approved: The approval status of the loan (boolean). 
# Implement the following methods for the Loan class: 
# calculate_interest(): Calculates the interest accrued on the loan amount and returns it as a float.(amount * interest rate) 
# approve_loan(): Approves the loan. 
# display_info(): Displays the information of the loan, including the customer name, loan amount, interest rate, and approval status. 


# class Loan:
#     def __init__(self, customer_name, amount, interest_rate):

#         self.customer_name = customer_name
#         self.amount = amount
#         self.interest_rate = interest_rate
#         self.approved = False

#     def calculate_interest(self):

#         print("the amount of the loan is:", float(self.amount * self.interest_rate))

#     def approve_loan(self):

#         if self.approved == True:
#             print("sucess, you're loan was approved", self.approved)
        
#         else: print("you don't have the means to make this loan")


#     def display_info(self):

#         print(" display info from the bank ")
#         print("")

#         print("name of the costumer", self.customer_name)
#         print("you're loan amount is:", self.approve_loan())
#         print("you're interest rate is:", self.interest_rate)
#         print("aproval status", "Available" if self.approved else "Not Available")





# costumer = Loan("Filipe",20000,0.2)

# costumer.calculate_interest()
# costumer.approve_loan()
# costumer.display_info()
            

# Online Ticket Booking System 
# Design an online ticket booking system for a theater that manages available seats and ticket reservations. Implement the following functionalities: 

# Create a class called Theater that represents a theater in the online ticket booking system. The Theater class should have the following attributes: 
# num_rows (integer): The number of rows in the theater. 
# num_seats_per_row (integer): The number of seats per row in the theater. 
# seat_map (2D list): A 2D list to represent the seat map of the theater, where each element represents the availability of a seat (True for available, False for booked). 
# Implement the following methods for the Theater class: 
# book_ticket(row, seat): Books a ticket for a given seat in the theater. If the seat is available, mark it as booked in the seat map. If the seat is already booked or invalid, display an error message. 
# display_seat_map(): Displays the seat map of the theater, showing the availability of each seat. Use 'O' to represent available seats and 'X' to represent booked seats. 
# Usage: 
# theater = Theater(5, 6) 
# theater.display_seat_map() 
# theater.book_ticket(3, 4)  # Book a ticket for Row 3, Seat 4 
# theater.book_ticket(2, 5)  # Book a ticket for Row 2, Seat 5 
# theater.book_ticket(4, 3)  # Book a ticket for Row 4, Seat 3 
# theater.book_ticket(3, 4)  # Attempt to book the same seat again 
# theater.display_seat_map() 
# Output: 
# Row 1: O O O O O O 
# Row 2: O O O O O O 
# Row 3: O O O O O O 
# Row 4: O O O O O O 
# Row 5: O O O O O O 
# Ticket booked successfully! 
# Ticket booked successfully! 
# Ticket booked successfully! 
# Seat already booked! 
# Row 1: O O O O O O 
# Row 2: O O O O O X 
# Row 3: O O O X O O 
# Row 4: O O O O O O 
# Row 5: O O O O O O 

# class Theather:
#     def __init__(self,num_rows,num_seats_per_row):
        
#         self.num_rows = num_rows
#         self.num_seats_per_row = num_seats_per_row
#         self.seat_map = [["O"]*num_seats_per_row for x in range(num_rows)]

#     def book_ticket(self,row,seat):
#         if row <= 0 or row >= self.num_rows and seat <= 0 or seat >= self.num_seats_per_row:
#             print("invalid seat")
#         elif self.seat_map[row-1][seat-1] == "X":
#             print("this seat is already taken")
#         else:
#             self.seat_map[row-1][seat-1] = "X"
#             print("your seat was sucessfully added")
    
#     def display_seat_map(self):
#         row_number = 1
#         for row in self.seat_map:
#             print(row_number, " ".join(row))
#             row_number +=1

# theater = Theather(5, 6) 
# theater.display_seat_map() 
# theater.book_ticket(3, 4)  # Book a ticket for Row 3, Seat 4 
# theater.book_ticket(2, 5)  # Book a ticket for Row 2, Seat 5 
# theater.book_ticket(4, 3)  # Book a ticket for Row 4, Seat 3 
# theater.book_ticket(3, 4)  # Attempt to book the same seat again 
# theater.display_seat_map()


# 5 - Deck of Cards 
# Create a Card class that represents a playing card.
# The class should have the following attributes: rank and suit. 
# The class should also have a method called __str__() that returns a string representation of the card (e.g., "Ace of Spades"). 
# Create a Deck class that represents a deck of cards. 
# The class should have the following attributes: cards. 
# The class should also have the following methods: shuffle(), deal(), and __str__(). 
# The shuffle method should shuffle the deck of cards. The deal method should deal one card from the deck. 
# The __str__ method should return a string representation of the deck. 

# import random

# class Card:
#     def __init__(self, rank,suit):
#         self.rank = rank
#         self.suit = suit

#     def __str__(self):
#         return f"{self.rank} of {self.suit}"

# class Deck:
#     def __init__(self):
#         self.ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
#         self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
#         self.cards = []
#         self.generate_deck()
#     def generate_deck(self):
#         self.cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]
#     def shuffle(self):
#         random.shuffle(self.cards)
#     def deal(self):
#         if self.cards == 0:
#             return None
#         else:
#             return self.cards.pop()

#     def __str__(self):
#         return ", ".join(str(card) for card in self.cards)    
    

# # Create a new deck and shuffle it
# deck = Deck()
# print("Initial deck:")
# print(deck)
# print()

# deck.shuffle()
# print("Shuffled deck:")
# print(deck)
# print()

# # Deal a card from the deck
# card = deck.deal()
# print("Dealt card:")
# print(card)
# print()

# # Print the remaining cards in the deck
# print("Remaining deck:")
# print(deck)


# Exercise 1: Create a class hierarchy with three classes: Animal, Dog, and Cat. 
# Implement a function called check_animal_type() that takes an object as a parameter and checks if it belongs to the Animal, 
# Dog, or Cat class. The function should print the corresponding animal type. 

# class Animal():
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("woof!!")
# class Cat(Animal):
#     def sound(self):
#         print("miauuu!")


# def check_animal_type(obj):
#     if issubclass(Dog,Animal):
#         if issubclass(Animal,Dog):
#             return Dog(Animal)
#         elif issubclass(Animal,Cat):
#             return Cat(Animal)
#         else:
#             print("The object is an Animal.")
#     else:
#         print("The object does not belong to the Animal class hierarchy.")
        
        
    


# animal = Animal("some animal")
# dog = Dog("whiskers")
# cat = Cat("garfield") 
# num = 100       
# check_animal_type(dog.sound())
# check_animal_type(cat.sound())


# Exercise 2: Create a class hierarchy with two classes: Shape and Rectangle. 
# Implement a function called check_shape_relationship() that takes two objects as 
# parameters and checks if the first object is a subclass of the second object. 
# The function should print whether the relationship holds true or not. 


# class Shape:
#     def shape_of_rectangle(self):
#         pass

# class Rectangle(Shape):

#     def shape_of_rectangle(self):
#         return super().shape_of_rectangle()
    

# def check_shape_relationship(obj1,obj2):
#      if issubclass(type(obj1), type(obj2)):
#         return True
#      else:
#         return False
        

# shape = Shape()
# retangulo = Rectangle()

# print(check_shape_relationship(retangulo,shape))
# print(check_shape_relationship(shape,retangulo))


# Exercise 3: Create a class hierarchy with three classes: Vehicle, Car, and Motorcycle. 
# Implement a function called check_vehicle_type() 
# that takes an object as a parameter and checks if it 
# belongs to the Vehicle class or any of its subclasses. 
# The function should print the vehicle type accordingly. 

# class Vehicle():
#     def __init__(self, name):
#         self.name = name
    
# class Car(Vehicle):
#     pass
# class Motorcycle(Vehicle):
#     pass
# def check_vehicle_type(obj):
#     if isinstance(obj, Vehicle):
#         if isinstance(obj, Car):
#             print("the type of the vehicle is a car")
#         elif isinstance(obj, Motorcycle):
#             print("the type of the vehicle is a motorcyle")
#         else:
#             print("its not a bike nor a car")
#     else: 
#         print("its not a vehicle")
# vehicle = Vehicle("normal vehicle")
# car = Car("Ferrari")
# motorcycle = Motorcycle("kawasaki")
# check_vehicle_type(vehicle)
# check_vehicle_type(car)
# check_vehicle_type(motorcycle)
# check_vehicle_type(100)


# Exercise 4 
# Book and Author: 
# Create a class called Author with attributes such as name, age, and nationality. 
# Create a class called Book with attributes such as title, genre, and a composition relationship with the Author class. 
# The Book class should have a method to get the author's information. 


# class Author:
#     def __init__(self, name, age , nationality):
#         self.name = name
#         self.age = age
#         self.nationality = nationality
    
# class Book:
#     def __init__(self,title,genre,author):
#         self.title = title
#         self.genre = genre
#         self.author = author

#     def autho_details(self):
#         return f"author: {self.author.name},age: {self.author.age},nationality: {self.author.nationality}"
#     def __str__(self):
#         return f"Title: {self.title},\ngenre: {self.genre},\n{self.autho_details()}"    
         


# author = Author("Filipe", "18","Portugues")
# book = Book("saramago","ficao",author)
# print(book)

# Exercise 5 
# Car and Engine: 
# Create a class called Engine with attributes such as horsepower and fuel_type. 
# Create a class called Car with attributes such as make, model, and a composition relationship with the Engine class. 
# The Car class should have a method to start the engine. 

# class Engine:
#     def __init__(self, horsepower, fuel_type):
#         self.horsepower = horsepower
#         self.fuel_type = fuel_type
    

# class Car:
#     def __init__(self,make,model,engine):

#         self.make = make
#         self.model = model
#         self.engine = engine
#     def start_engine(self):
#         print("engine started")
#     def get_engine(self):
#         return f"horsepower: {self.engine.horsepower}, fueltype: {self.engine.fuel_type}"
#     def __str__(self):
#         return f"make: {self.make}, model: {self.model}, engine: {self.get_engine()}"


# engine = Engine(200, "diesel")
# car = Car("Ferrari", "xt200",engine)
# print(car)

# car.start_engine()

# Exercise 6 
# Create a class called Department with attributes such as name and faculty. 
# Create a class called University with attributes such as name and a composition relationship with the Department class. 
# The University class should have a method to get the department's information. 


# class Department:
#     def __init__(self, name, faculty):
#         self.name = name
#         self.faculty = faculty

# class University: 
#     def __init__(self, name, department):
#         self.name = name
#         self.department = department

#     def department_information(self):
#         return f"name: {self.name}, department: {self.department.name}"
    
    


# department = Department("servicos academicos", "UBI")

# universidade = University("UBI",department)

# print(universidade.department_information())


# Shopping Cart with Composition 
# Introduction: You have been assigned the task of creating a shopping cart application for an online store. 
# The application should allow customers to add items to their cart, remove items, and calculate the total price of the items in the cart. 
# To implement this functionality, you will be using the concept of composition, where a shopping cart is composed of a customer and a collection of items. 
# Instructions: 
# Implement the Customer class with the following attributes: 
# name (string): representing the name of the customer. 
# email (string): representing the email address of the customer 
# Implement the Item class with the following attributes 
# name (string): representing the name of the item 
# price (float): representing the price of the item. 
# Implement the ShoppingCart class with the following attributes and methods: 
# customer (Customer): representing the customer who owns the shopping cart. 
# items (list): representing the collection of items in the shopping cart. 
# add_item(item): method to add an item to the shopping cart. 
# remove_item(item): method to remove an item from the shopping cart. 
# calculate_total_price(): method to calculate the total price of all the items in the shopping cart. 
# Create instances of the Customer, Item, and ShoppingCart classes. 
# Create a customer object with a name and email address. 
# Create several item objects with different names and prices. 
# Create a shopping cart object with the customer as its composition. 
# Perform the following actions using the shopping cart object: 
# Add items to the shopping cart using the add_item() method. 
# Remove an item from the shopping cart using the remove_item() method. 
# Calculate and display the total price of all the items in the shopping cart using the calculate_total_price() method. 
# Note: Ensure that you use proper composition by associating the customer and item objects with the shopping cart. 



# class Costumer:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#     def __str__(self):
#         return f"costumer name: {self.name}, costumer email: {self.email}"

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def __str__(self):
#         return f"your shopping list is: {self.name}, {self.price} "

# class ShoppingCart:
#     def __init__(self,costumer):
#         self.costumer = costumer
#         self.items = []
    
        
    
#     def add_items(self,item):
#         self.items.append(item)
#     def remove_item(self,item):
#         return self.items.remove(item)
#     def calculate_total_price(self):
#         total = 0
#         for item in self.items:
#             total += item.price
#         return f"your total is: {total}"
#     def __str__(self):
#         item_list = "\n".join([str(item) for item in self.items])
#         return f"\n Items in the shopping cart:\n {item_list}"
    
# costumer = Costumer("Filipe", "filipefernandes50000@gmail.com")
# shoppingcart = ShoppingCart(costumer)



# item1 = Item("computador", 140)
# item2= Item("telefone", 150)
# item3 = Item ("book", 15)

# shoppingcart.add_items(item1)
# shoppingcart.add_items(item2)
# shoppingcart.add_items(item3)


# print(shoppingcart.costumer)
# print(shoppingcart)

# print(shoppingcart.calculate_total_price())

# Exercise: Online Marketplace with Order Processing 

  

# Introduction: 
# You have been assigned the task of building an online marketplace application that facilitates order processing for various products. 
# The application should handle different types of products, such as electronics, clothing, and books, and ensure proper order fulfillment. 
# In this exercise, you will use composition and MRO to design and implement the necessary classes for this online marketplace. 
# Instructions: 
# 1. Define a base class called `Product` with the following attributes: 
# - `name` (string): representing the name of the product. 
# - `price` (float): representing the price of the product. 
# 2. Create three subclasses of `Product` to represent different types of products, such as `Electronics`, `Clothing`, and `Books`. 
# Each subclass should have its own specific attributes and methods related to the type of product. 
# For example, the `Electronics` class may have an additional attribute called `brand`. 
# 3. Define a class called `Order` with the following attributes: 
# - `customer_name` (string): representing the name of the customer placing the order. 
# - `products` (list): representing the collection of products in the order. 
# 4. Implement the following methods in the `Order` class: 
# - `add_product(product)`: method to add a product to the order. 
# - `remove_product(product)`: method to remove a product from the order. 
# - `calculate_total_price()`: method to calculate the total price of all the products in the order. 
# 5. Create instances of the `Electronics`, `Clothing`, and `Books` classes to represent different products. 
# 6. Create an instance of the `Order` class and add the products to the order. 
# 7. Print the order details, including the customer name, product details, and the total price. 
# 8. Ensure that the classes are properly designed using composition, where the `Order` class has a composition relationship with the `Product` classes. 
# 9. Test different scenarios by adding and removing products from the order and calculating the total price. 
# Note: Consider using inheritance to define shared attributes and methods among the product subclasses. Use composition to associate the products with the order. 



# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def __str__(self):
#         return f"Product: {self.name}, Price: {self.price}"

# class Eletronics(Product):
#     def __init__(self, name, price, brand):
#         self.name = name
#         self.price = price
#         self.brand = brand
#     def __str__(self):
#         return f"name: {self.name}, price: {self.price}, brand: {self.brand}"

# class Clothing(Product):
#     def __init__(self, name, price, size):
#         self.name = name
#         self.price = price
#         self.size = size
#     def __str__(self):
#         return f"name: {self.name}, price: {self.price}, size: {self.size}"

# class Books(Product):
#     def __init__(self, name, price, title):
#         self.name = name
#         self.price = price
#         self.title = title
#     def __str__(self):
#         return f"name: {self.name}, price: {self.price}, title: {self.title}"

# class Order:
#     def __init__(self, costumer_name):
#         self.costumer_name = costumer_name
#         self.list = []
    
#     def add_product(self,product):
#         self.list.append(product)

#     def remove_product(self, product):
#         self.list.remove(product)

#     def calculate_total_price(self):
#         total = 0
#         for product in self.list:
#             total += product.price
#         print("the total is:", total)
#     def __str__(self):
#         item_list = "\n".join(str(product) for product in self.list)
#         return f"Customer Name: {self.costumer_name} \nItems in the shopping cart:\n{(item_list)}"

        

# product = Product("robo",12.0)
# eletronics = Eletronics("computador", 135.0, "toshiba")
# clothing = Clothing("tshirt",20.0,"M")
# books = Books("saramago", 30.0,"caim")

# order = Order("Filipe")

# order.add_product(product)
# order.add_product(eletronics)
# order.add_product(clothing)
# order.add_product(books)
# order.remove_product(books)
# print(order)

# order.calculate_total_price()

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def study(self):
#         print(f"{self.name} is studying.")

#     def take_exam(self):
#         print(f"{self.name} is taking an exam.")
        

# class OnlineShopping:
#     def __init__(self, costumer,cart):
#         self.costumer = None
#         self.cart = ShoppingCart()
#     def browse_products(self):
#         pass
#     def addtocart(self,product):
#         self.cart.addproduct(product)

#     def checkout(self):
#         pass

# class Costumer:
#     def __init__(self, nome):
#         self.nome = nome

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def addproduct(self,product):
#         self.items.append(product)

'''+------------------------+
|    Online Shopping     |
+------------------------+
| - customer: Customer   |
| - cart: ShoppingCart  |
+------------------------+
| + browseProducts()     |
| + addToCart(product)   |
| + checkout()           |
+------------------------+

+------------------------+
| customer               |
+------------------------+
| - name: str            |
|                        |
+------------------------+
+------------------------+
|    ShoppingCart        |
+------------------------+
| - items: []            |
|                        |
+------------------------+
| + addproduct()         |
|                        |
+------------------------+'''

###############################################################

# class Librarian:
#     def __init__(self, name):
#         self.naem = name

# class Member:
#     def __init__(self, member):
#         self.member = member

# class LibraryManagement:
#     def __init__(self, name,member):
#         self.name = name
#         self.member = member

#     def addbook(self,book):
#         pass
#     def lendbook(self,book):
#         pass
#     def returnbook(self,book):
#         pass
# class Ticketbookingsystem:
#     def __init__(self,user, event):
#         self.user = user
#         self.event = event

# class user:
#     pass
# class event:
#     pass

# def Searchevents():
#     pass

# def select_events():
#     pass

# def bookticket():
#     pass

#####################################################################################
#estudante de informatica

# class EstudanteInf:
#     def __init__(self, N,t1,t2):
#         self.__Nome = N
#         self.__Teste1 = t1
#         self.__Teste2 = t2
       
       
       

#     def class_final(self):

#         media = (self.__Teste1 + self.__Teste2) / 2
#         return media
#     def get_name(self):
#         return self.__Nome
    
#     def get_teste1(self):
#         return self.__Teste1
    
#     def get_teste2(self):
#         return self.__Teste2
    
#     def set_name(self, nome):
#         self.__Nome = nome

#     def set_teste1(self, teste1):
#         self.__Teste1 = teste1

#     def set_teste2(self,teste2):
#         self.__Teste2 = teste2
    
    
    

# if __name__=="__main__": 

#     E=EstudanteInf("Ana Paiva", 18, 12) 
    

#     B=EstudanteInf("Filipe", 15, 16) 

#     C=EstudanteInf("Uirá", 18, 12) 

#     D=EstudanteInf("Bruno", 10, 11) 

    
 

#     print(f"{'Nome':^15}{'Teste 1':^10}{'Teste 2':^10}{'Classif. Final':^15}") 

#     print(f"{E.get_name():<15}{E.get_teste1():^10}{E.get_teste2():^8}{E.class_final():^16}") 

#     print(f"{C.get_name():<15}{C.get_teste1():^10}{C.get_teste2():^8}{C.class_final():^16}") 

#     print(f"{B.get_name():<15}{B.get_teste1():^10}{B.get_teste2():^8}{B.class_final():^16}") 

#     print(f"{D.get_name():<15}{D.get_teste1():^10}{D.get_teste2():^8}{D.class_final():^16}") 

    

#     E.set_name("Ana Maria")
#     E.set_teste1(12)
#     E.set_teste2(20)
#     B.set_name("OLA")
#     B.set_teste1(15)
#     B.set_teste2(20)

#     print(f"{'Nome':^15}{'Teste 1':^10}{'Teste 2':^10}{'Classif. Final':^15}") 

#     print(f"{E.get_name():<15}{E.get_teste1():^10}{E.get_teste2():^8}{E.class_final():^16}") 

#     print(f"{C.get_name():<15}{C.get_teste1():^10}{C.get_teste2():^8}{C.class_final():^16}") 

#     print(f"{B.get_name():<15}{B.get_teste1():^10}{B.get_teste2():^8}{B.class_final():^16}") 

#     print(f"{D.get_name():<15}{D.get_teste1():^10}{D.get_teste2():^8}{D.class_final():^16}") 

####################################################################################################

#7.10 caderno de exercicios

# class Temperatura():
#     def __init__(self,c):
#         self.c = c
      

#     def transformar_temperatura(self):
#         f = self.c * 1.8 + 32

#         return f
    
# graus = Temperatura(15)

# print(graus.transformar_temperatura())


####################################################################################################


#7.11 caderno de exercicios


# class Produto():
#     Aumento = 0
#     def __init__(self, Des, Quant,Pu):
#         self.__Des = Des
#         self.__Quant = Quant
#         self.__Pu = Pu

#     def valor_produto(self):
#         return self.__Quant * self.__Pu*(1+Produto.Aumento/100)
#     @staticmethod
#     def aumento(subir):
#        Produto.Aumento = subir
#        return subir
#     @staticmethod
#     def Cabecalho():
#         print(f"{'designaçao':^15}{'valor (€)':^10}")

#     def impressao(self):
#         print(f"{self.__Des:<15} {self.valor_produto():^8}")
        
#         return
    

# Prod=(('LP', 100, 10), ('LP2', 200, 10),  ('LP3', 150, 15))
# subir = 5
# Produto.Aumento()
# Produto.Cabecalho()
# for P in Prod:
#     Pr=Produto(P[0], P[1], P[2])
#     Pr.impressao()


# class Produto:
#     Aumento = 0
#     def _init_(self, Des, Quant, Pu):
#         self.__Des = Des
#         self.__Quant = Quant
#         self.__Pu = Pu
#     def ValorProduto(self):
#         return self.__Quant*self.__Pu*(1+Produto.Aumento/100)
#     @staticmethod
#     def AumentoP(Perc):
#         Produto.Aumento=Perc
#         return
#     @staticmethod
#     def Cabecalho():
#         print(f"{'Designação':^15}{'Valor (€)':^10}")
#     def Impressao(self):
#         print(f"{self.__Des:<15} {self.ValorProduto():^8}") 

# if __name__ == "__main__":

#     Prod=(('LP', 100, 10), ('LP2', 200, 10),  ('LP3', 150, 15))
#     Perc = 5
#     Produto.AumentoP(Perc)
#     Produto.Cabecalho()
#     for P in Prod:
#         Pr=Produto(P[0], P[1], P[2])
#         Pr.Impressao()




# 7.12 hierarquia de classes
# classe pessoa encapsula
# duas variaveis de instante, nome e telefone
# construtor
# acessos para ler os valores das variaveis de instante

# subclasse de amigo encapsula
# duas variaveis de instante, local e ano de inicio da amizade 
# construtir
# acessos para ler os valore das variaveis de instante~

# subclasse colega encapsula
# duas variaveis de isntante, local de trabalho e profissao
# construtor
# acessos para ler os valores das variaveis de instante
# 7.13 metodos de impressao para estas tres classes


# class Pessoa:
#     def __init__(self, nome, telefone):
#         self.__nome = nome
#         self.__telefone = telefone


#     @property
#     def nome(self):
#         return self.__nome
#     @property
#     def telefone(self):
#         return self.__telefone
#     def impressao(self):
#         return f"{self.nome} -- {self.telefone}"
    

# class Amigo(Pessoa):
#     def __init__(self, nome, telefone,local,ano):
#         super().__init__(nome, telefone)
#         self.__local = local       
#         self.__ano = ano

#     @property
#     def local(self):
#         return self.__local
#     @property
#     def ano(self):
#         return self.__ano
    
#     def impressaoA(self):
#         print(f"{super().impressao()}--{self.local}--{self.ano}")
#         return
    
# class Colega(Pessoa):
#     def __init__(self, nome, telefone,local_de_trabalho,profissao):
#         super().__init__(nome, telefone)
#         self.__local_de_trabalho = local_de_trabalho
#         self.__profissao = profissao

#     @property
#     def local_de_trabalho(self):
#         return self.__local_de_trabalho

#     @property
#     def profissao(self):
#         return self.__profissao
    
#     def impressaoC(self):
#         print(f"{super().impressao()} -- {self.local_de_trabalho} -- {self.profissao}")
#         return

# filipe = Amigo("Filipe", 961512067, "guarda",2022)
# duarte = Colega("duarte", 964152384,"Lisboa","marketing")
# filipe.impressaoA()
# duarte.impressaoC()


class Propriedade():
    def __init__(self, nomeprop, NF):
        self.__Proprietario = nomeprop
        self.__numero_fiscal = NF

    @property

    def Proprietario(self):

        return self.__Proprietario
    
    @Proprietario.setter
    def Proprietario(self,N):
        self.__Proprietario = N

    @property

    def NFiscal(self):

        return self.__numero_fiscal
    

    @NFiscal.setter

    def NFiscal(self,NF):
        self.__numero_fiscal = NF

    def impressao(self):
        return f"proprietario: {self.Proprietario} numero fiscal: {self.NFiscal}"
    
    def rendaminima(self):
        P1 = 0.2
        P2 = 0.3
        Min = 100

        if self.area < 50:
            renda = Min
        elif self.area < 100:
            renda = Min+P1*self.area
        else:
            renda = Min+P2*self.area
        return int(renda)
        
    
            
class Moradia(Propriedade):

    def __init__(self, nomeprop, NF, L, C):
        super().__init__(nomeprop, NF)

        self.__local = L
        self.__categoria = C

    @property

    def local(self):
        return self.__local
    
    @local.setter

    def local(self,l):

        self.__local = l

    @property

    def categoria(self):
        return f"{self.__categoria}"

    @categoria.setter

    def categoria(self, C):
        self.__categoria =  C


class Apartamento(Propriedade):

    def __init__(self, nomeprop, NF,T,A):
        super().__init__(nomeprop, NF)

        self.__tipo = T
        self.__area = A
        

    @property

    def tipo(self):
        return self.__tipo

    @tipo.setter

    def tipo(self,T):
        self.__tipo = T  

    @property
    def area(self):
        return self.__area
    
    @area.setter

    def area(self,A):

        self.__area = A




ana = Moradia("adao", 122,"guarda", "C")

filipe = Apartamento("filipe",239276710,"T2",200)


     
print(filipe.impressao()) 
print(filipe.rendaminima())
    


        
    



    









    
        
            


 

    










