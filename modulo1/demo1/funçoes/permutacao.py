'''Exercicio Extra – Complexidade avançada (para quem quiser) 
Generate Permutations 

Write a recursive function called generate_permutations that takes a list lst as input and returns a list of all possible permutations of the elements in lst. 

A permutation is an arrangement of elements where the order matters. For example, given the input list [1, 2, 3], the function should return [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. 

Your task is to implement the generate_permutations function using recursion. You may assume that the input list does not contain any duplicate elements. '''
 

def generate_permutations(lst):
    if len(lst) == 0:
        return[[]]
    permutations = []

    comprimento = len(lst)
    for i in range(0,comprimento):
        chosen_element = lst[i]
        remaining_elements = lst[:i] + lst[i+1:]
        sub_permutations = generate_permutations(remaining_elements)

        for sub_permutation in sub_permutations:
            permutations.append([chosen_element] + sub_permutation)
    return permutations


print(generate_permutations([1, 2, 3])) # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] 

 

print(generate_permutations(['a', 'b', 'c'])) # Output: [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]  

 

print(generate_permutations(['x', 'y'])) # Output: [['x', 'y'], ['y', 'x']] 
 
