# mostrar classe, atributos e metodos

class Circle:
    def __init__(self,radius):  # atributo radius
        self.radius = radius
    
    def calculate_area(self):   # metodo calcular area ( )
        return 3.14 * self.radius ** 2  # usar o self, serve para dizer que é para usar o que está na classe em cima descrito 
    
my_circle = Circle(5)
print(my_circle.calculate_area())



class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.heigth = height

    def calculate_area(self):
        return self.width * self.heigth

my_rectangle = Rectangle(4,5)   # criar o objecto(my_rectangle), de seguida a classe(Rectangle) e os atributos(4,5) que são necessarios
print(my_rectangle.calculate_area()) # aqui é usado o método (calculate_area)
