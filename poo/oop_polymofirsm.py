from abc import ABC, abstractmethod


class Shape(ABC):
     @abstractmethod
     def calculate_area(self):
          pass
     
class Rectangle(Shape):
     def __init__(self, lenght, withd):
          self.width = withd
          self.lenght = lenght

     def calculate_area(self):
          return self.lenght * self.width
     

class Circle(Shape):
     def __init__(self, radius):
          self.radius = radius

     def calculate_area(self):
          return 3.14 * self.radius **2
     


shapes= [Rectangle(4,5),Circle(3)]

for shape in shapes:
     print(shape.calculate_area())
     