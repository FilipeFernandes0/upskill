#Create a shopping list that allows adding items with their quantities and prices. 
#Calculate the total cost of the items on the list. 
 
def add_item(item, quantity, price):
    shop_list[item] = (quantity * price)
    
    
    
   
def calculate_total_cost():
    total = 0
    for i in shop_list.values():
        total += i
    return total
    

shop_list = {}

add_item("Apples", 5, 1.5)

add_item("Bananas", 3, 0.5) 

add_item("Cereal", 2, 3.75) 
 
print(shop_list)
total_cost = calculate_total_cost()  

print("Total cost:", total_cost) 

 