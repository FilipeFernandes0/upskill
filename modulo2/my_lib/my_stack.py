

#stack = []

def push(stack,val):
    stack.append(val)
    

def pop(stack):
    return stack.pop()


def erase(stack):
    del stack

def top(stack):
    return stack[-1]


def is_empty(stack):
    return len(stack) == 0