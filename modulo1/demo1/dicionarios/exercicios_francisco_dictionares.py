#Write a function merge_dicts(dict1, dict2) that takes two dictionaries as input and 
#returns a new dictionary that combines the key-value pairs from both dictionaries. 

# def merge_dicts(dict1, dict2):
   
   
#    merge_dict = dict1.copy()
#    merge_dict.update(dict2)
#    return merge_dict


# dict1 = {"a":1, "b":2}
# dict2 = {"c":1, "d":2}

# result = merge_dicts(dict1,dict2)
# print(result)

##################################################################################


#Write a function anagram_groups(words) that takes a list of words as input and returns a dictionary 
#where the keys are sorted strings of letters representing anagrams, and the values are lists of words that are anagrams of each other. 

def anagram_groups(words):
    anagram_words = {}
    for word in words:
        sorted_words = " ".join(sorted(word)) #.join unir a string vazia, sorted afasta as palavras cat fica c-a-t
        if sorted_words in anagram_words:
            anagram_words[sorted_words].append(word)
        else:
            anagram_words[sorted_words] = [word]
    return anagram_words




words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
result = anagram_groups(words)
print(result)

#######################################################################


#Nested Dictionary Manipulation 
#Consider a dictionary representing a company's employee structure. 
#Each employee has a name and a department. 
#Write a function get_department_size(company, department) that takes the company dictionary and a department name as input. 
#The function should return the number of employees in the specified department. 

def get_department_size(company, department):
    count = 0

    for name in company.values():
        if name["department"] == department:
            count+=1
    return count
        
company = {
    'Alice': {'name': 'Alice', 'department': 'Sales'},
    'Bob': {'name': 'Bob', 'department': 'Sales'},
    'Charlie': {'name': 'Charlie', 'department': 'Marketing'},
    'David': {'name': 'David', 'department': 'Human Resources'},
    'Eve': {'name': 'Eve', 'department': 'Sales'},
}

department = "Sales"
result = get_department_size(company, department)
print(result)



#Dictionary Inversion 

#Write a function invert_dictionary(dictionary) that takes a dictionary 
#as input and returns a new dictionary where the keys and values are swapped. 

def invert_dictionary(dictionary):
    dictionary = {"a":1,"b":2}
    print("initial dictionary : ", str(dictionary))
    inv_dict_1 = {v:k for k,v in dictionary.items()}
    #v = dictionary.values()
    #k = dictionary.keys()
    print("inverse mapped dictionary : ", str(inv_dict_1))





dictionary = {"a":1,"b":2}
result = invert_dictionary(dictionary)
print(result)
  #dictionary = {"a":1,"b":2}

