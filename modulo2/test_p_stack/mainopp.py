from sys import path
path.append("..\\my_lib")


import my_stackopp

class AddingStack(my_stackopp.Stack):
    def __init__(self):
        my_stackopp.Stack.__init__(self)
        self.__sum = 0
    
    def get_sum(self):
        return self.__sum
    
    def push(self, val):
        super().push(val)
        self.__sum+=val
    
    def pop(self):
        val = my_stackopp.Stack.pop(self)
        self.__sum -= val
        return val
    
if __name__ == '__main__':
    adding_stack = AddingStack()

    for i in range(5):
        adding_stack.push(i)
    print('sum =', adding_stack.get_sum())
    print('Is stack empty?', adding_stack.is_empty())

    while(not adding_stack.is_empty()):
        print('value:', adding_stack.pop())
        print('sum =', adding_stack.get_sum())