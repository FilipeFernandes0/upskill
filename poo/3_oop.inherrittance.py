# herança em classe, criar uma "subclasse"/"childclasse" que vai buscar apenas alguns dos atributos da classe
# Parent class (super class)
class Animal: 
    def __init__(self,name):
        self.name = name
    
    def make_sound(self):
        print("Animal sound!")


#subclasse que continua a ser da class animal 
#Child Class
class Dog(Animal):

    def __init__(self,name,breed):
        super().__init__(name) ## estamos a ir buscar a super class que definimos em cima (Animal), com a definção inicial (__init__) e depois o atributo (name) , esta linha sõ para dizer que o name é o mesmo do de cima da super class
        self.breed = breed
    
    def make_sound(self):
        print("AuAu! Woof!")

   
my_dog = Dog("Beethoven","Labradoodle")
print(my_dog.name)
print(my_dog.breed)
my_dog.make_sound()  # aqui vai buscar a segunda porque alteramos