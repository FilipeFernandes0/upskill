#Create a dictionary to store information about different cats, such as their names, ages, and favorite toys. 

gatos = {}

lista = []
gatos1 = "nome"
age1 = "idade"
boneco = "boneco"
while True:
    name1 = str(input("qual é o nome do gato? "))
    ages = int(input("qual é a idade do gato? "))
    toys = str(input("qual é o boneco preferido do gato? "))
    gatos.setdefault(gatos1,name1)
    gatos.setdefault(age1,ages)
    gatos.setdefault(boneco,toys)
    lista.append(gatos) 

    print(lista)


        





