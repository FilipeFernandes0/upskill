'''empty_dictionary = {}



dicionario ={
    "nome": "Filipe",
    "idade": "21",
    "morada": "guarda"
    }

print(dicionario)
print(dicionario["nome"])#saber a quem refere o que estamos a pesquisar


dictionary = {"cat":"chat","dog":"chien",
              "horse":"cheval"}

for key in dictionary.keys(): #apresenta os valores conforme no dicionario
    print(key,"->",dictionary[key])


for key in sorted(dictionary.keys()): #igual ao primeiro exemplo mas deixa os valores em ordem devido ao sorted
    print(key,"->",dictionary[key])

dicionario["nome"] = "Filipe Fernandes"
print(dicionario)
print(dicionario["nome"])

dicionario["idade"] = "32"
dicionario["morada"] = "Covilhã" #consegue atualizar os valores do dicionario

print(dicionario["idade"])
print(dicionario["morada"])
print(dicionario)


dicionario["novakey"] = "novoValue" #adiciona novas keys ao dicionario 
dicionario["key1"] = 12
print(dicionario)

del dicionario["novakey"] #com o del consegue se remover keys do dicionario 

print(dicionario)

dicionario.popitem()#apaga a ultima entrada do dicionario
print(dicionario)'''



'''school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)'''

'''dicionario_1 = {"nota": 10,
                "nota1": 7,
                "nota2": 8}

dicionario_1["nota"] += dicionario_1["nota1"] #ele soma a nota com a nota1 e tambem concateneia strings
print(dicionario_1)

for key in dicionario_1: #o output vai ser só as keys 
    print(key)

for key in dicionario_1.values(): #o output vai ser só as values devido ao .value
    print(key)

for key, values in dicionario_1.items():
    print(key,"->", values)

#verificar numero de entradas
#tamanho do dicionario
print("existem", len(dicionario_1), "entradas")

notas ={
    "filipe": 12,
    "joao": 15,
    "teste":"teste",
    "lista":[1,"teste",5],
    "tuplas":(1,"teste",5) #consegue-se adicionar tuplas e listao ao dicionario
}

print(notas)


#ver o tipo
print("o tipo é:", type(notas))
#forma para copiar o dicionario para um novo dicionario 
novasnotas = notas.copy()
print(notas)
print(novasnotas)'''


'''person = {"name": "John", "age": 30, "city": "new york"}

print(person["name"]) #para chamarmos o valor damos print na key
print(person["age"])
print(person["city"])

person["age"] = 35 # modificar o valor
print(person["age"])

person = {"name": "joe","age":40}
person["city"] = "new york"'''







