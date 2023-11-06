'''def calculate_average_grade(student_grades):
    average_grades = {}
    for student, grades in student_grades.items():
        total_grades = sum(grades)
        average = total_grades / len(grades)
        average_grades[student] = average
    return average_grades

student_grades = {
    "Alice": [80,90,75],
    "Bob" :[85,95,70],
    "charlie":[90,80,85]
}

print(calculate_average_grade(student_grades))'''


#########################################

'''text = "The quick brown lazy fox jumps over the lazy dog jumps quick"

def count_word_frequency(text):
    words = text.split()
    word_frequency = {}
    #words = text.split()
    for word in words:
       if word in word_frequency:
           word_frequency[word] += 1
       else:
           word_frequency[word] = 1 
    return word_frequency
print(count_word_frequency(text))
'''

'''def add_contact(phonebook, name, number):
    phonebook[name] = number
    
    #print(name)
def get_contact(phonebook, name):
    if name in phonebook:
        return phonebook[name]
    else:
        return None
    

def list_contacts(phonebook):
   for name,number in phonebook.items():
       print(f"{name}:{number}")



phonebook = {}
add_contact(phonebook,"alice","123456789")
get_contact(phonebook,"Alice")

list_contacts(phonebook)'''

#######################################################


import random

jokes = { 

    "knock-knock": [ 

        ("Knock, knock.", "Who’s there?", "Lettuce.", "Lettuce who?", "Lettuce in, it's cold out here!"), 

        ("Knock, knock.", "Who’s there?", "Boo.", "Boo who?", "Don't cry, it's just a joke!"), 

        ], 

    "one-liner":[ 

        ("Why don't scientists trust atoms?", "Because they make up everything!"), 

        ("Why don't skeletons fight each other?", "They don't have the guts!"), 

        ] 

} 


def generate_joke(category):
   
    if category == "knock-knock":
        joke =  random.choice(jokes["knock-knock"])
        return joke
    elif category == "one-liner":
        joke = random.choice(jokes["one-liner"])
        return joke
      

        #random.choice(joke)





category = input("enter a joke category(knock-knock or one-liner): ")
joke = generate_joke(category)
print("\n".join(joke))