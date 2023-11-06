#stack - a abordagem ao objeto

class Stack: # Defining the Stack class
    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val # return self.__stack.pop()

    def erase(self):
        self.__stack.clear()

    def top(self):
        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0
    
    def reverse_stack(stack):
        new_stack = Stack()
        while not stack.is_empty():
            new_stack.push(stack.pop())
        return new_stack
    
    
def bracket_match(string):
    stack = Stack()
    open_brackets = ["(","[", "{"]
    close_brackets = [")","]", "}"]

    for char in string:
        if char in open_brackets:
            stack.push(char)
        elif char in close_brackets:
            if stack.is_empty():
                return False
            if open_brackets.index(stack.peek()) == close_brackets.index(char):
                stack.pop()
            else:
                return False
    return stack.is_empty()

if __name__ == '__main__':
    my_stack_object = Stack()   # Instantiating an object
    print(my_stack_object.is_empty())
    my_stack_object.push('A')
    print(my_stack_object.is_empty())
    my_stack_object.push('B')
    my_stack_object.push('C')
    print(my_stack_object.pop())
    print(my_stack_object.pop())
    print(my_stack_object.pop())