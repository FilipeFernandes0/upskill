
#Exercício 2 Palindrome Checker 
#Write a recursive function called is_palindrome that takes a string text as input and returns True 
#if it is a palindrome (reads the same forwards and backwards), and False otherwise. 
 
def is_palindrome(palindrome):
    #nome = (input("Qual a palavra: "))
    count = 0
    w = len(nome)
    if w < 1 or count >= 1:
        return True
    elif nome[0] == palindrome[-1]:
        count+=1
        return True
    
    else:
        return False
    
        
nome = (input("Qual a palavra: "))      
    










print(is_palindrome(nome))     # Output: True 

#print(is_palindrome("level"))     # Output: True 

#print(is_palindrome("python"))    # Output: False 

#print(is_palindrome("racecar"))   # Output: True 

#print(is_palindrome("hello"))     # Output: False 

#print(is_palindrome("aa"))
#print(is_palindrome("t"))
 