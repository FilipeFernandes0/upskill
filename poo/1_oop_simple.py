# criação de classe carros
# defenir o nome da class (car neste caso)
# self para inicializar

class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

my_car = Car("Tesla", "Model 3")

print(my_car.make)
print(my_car.model)