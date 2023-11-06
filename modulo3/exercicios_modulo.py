from math import fsum 

reslt = sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])

result = fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
print(reslt,result)
########################################################
import random

random_num = random.randint(1,10)
print(random_num)

########################################################
import datetime

data = datetime.datetime.now()
print(data)
########################################################
import os

pastas_ficheiros = os.listdir()
for item in pastas_ficheiros:
    print(item)
########################################################
# import calendar

# ano = int(input("qual é o ano: "))
# mes = int(input("qual e o mes: "))

# calendar.month(ano,mes)

# print(calendar.month(ano,mes))
########################################################
import csv


data = [
    ["nome", "idade","salário"],
    ["jose", 32, 4000],
    ["john",25,2000],
    ["Roberto",44,4000],
    ["Mark", 19, 23000],
]
with open("data.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

def read_csv_data(file_path):
    data= []
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
        return data
def calc_average(data):
    values = [float(row[1]) for row in data]
    average = sum(values) / len(values)
    return average
def find_max_values(data):
    values = [float(row[1]) for row in data]
    maximum = max(values)
    return maximum
def filter_data(data, condition):
    filtered_data = [row for row in data if condition(row)]
    return filtered_data
file_path = "data.csv"
data = read_csv_data(file_path)

average = calc_average(data)
print("media: ",average)
max_value = find_max_values(data)
print("valor maximo", max_value)

filtered_data = filter_data(data, lambda row: float(row[2]) > 3000)
print("dados esperados:", filtered_data)





# data = [
#     ["nome", "idade","país"],
#     ["jose","32","portugal"],
#     ["john","25","USA"],
#     ["Roberto","44","México"],
#     ["Mark","19","UK"],
# ]

# with open("data.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# # #reading csv

# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:        
#         print(row)


import json

data = {
    "nome":"João",
    "idade": 32,
    "país":"Espanha"
}

with open("data.json", "w") as file:
    json.dump(data, file)


with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

