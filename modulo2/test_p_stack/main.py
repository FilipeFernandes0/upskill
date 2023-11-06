
from sys import path

path.append("..\\my_lib")


import my_stack

stack_1 = []
stack_2 = []
my_stack.push(stack_1, 1)
my_stack.push(stack_1, 2)
my_stack.push(stack_1, 3)
print(stack_1)
my_stack.push(stack_2, "A")
my_stack.push(stack_2, "B")
my_stack.push(stack_2, "C")
print(stack_2)
print(my_stack.top(stack_1))
print(my_stack.top(stack_2))

print(my_stack.pop(stack_1))
print(my_stack.pop(stack_1))
print(my_stack.pop(stack_1))
print(my_stack.pop(stack_2))
print(my_stack.pop(stack_2))
print(my_stack.pop(stack_2))


print(my_stack.erase(stack_1))
print(my_stack.erase(stack_2))

print(my_stack.is_empty(stack_1))

print(my_stack.is_empty(stack_2))

