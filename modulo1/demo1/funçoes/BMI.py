#BMI = (peso (kg)/altura^2(m))
#2 variaveis = height e weight
#function name bmi

'''def bmi(height, weight):
    return weight/height**2
    #print("the BMI is: ", bmi)

#weight = int(input("qual o peso em kg: "))
#height = float(input("qual a altura em m: "))
print(bmi(1.79, 59))'''

##### m = ft * 0.3048 + inches * 0.0254
##### kg = lb * 0.45359237 

def feet_to_meters(feet,inches):
    return feet * 0.3048 + inches * 0.0254
    

def lb_to_kg(lb):
    return lb * 0.45359237
   

def bmi(weight, height): 
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200: #\ significa separador de linha
        return None 
    return weight / height ** 2 

print(bmi(lb_to_kg(176),feet_to_meters(5,7)))



