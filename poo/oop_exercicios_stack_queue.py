#Stack Reversal  
#Write a function that takes a stack as input and returns a new stack
#with the items reversed. The original stack should remain unchanged. 


# class Stack:
#     def __init__(self):
#         self.stack = [10,9,8,7,5,6,4,2,3,15,67]
        


#     def new_stack(self):
        
#         new_stack = []
        
#         new_stack = self.stack[:]
#         new_stack.reverse()
#         print(self.stack)
#         print(new_stack)
        
# stacknew = Stack()
# stacknew.new_stack()


# class Queue:
#     def __init__(self):
#         queue = []

#     def rever_queue(queue):
#         new_queue = Queue()
#         while not queue.is_empty():
#             new_queue.enqueue(queue.dequeue())
#         return new_queue

# class BrowserHistory:
#     def __init__(self):
#         self.history = ["ola"]
    
#     def visit(self,url):
#         self.history.append(url)


#     def go_back(self):
#         if self.history:
#             return self.history.pop()
#         else:
#             return None
        

# class SupermarketCheckout:
#     def __init__(self):
#         self.queue = []

#     def join_queue(self,costumer):

#         self.queue.append(costumer)

#     def serve_costumer(self):
#         if self.queue:
#             return self.queue.pop(0)
#         else:
#             return None

#Implement a simple task scheduler using a queue. Design a class that supports the following methods: 
#add_task(task): Adds a new task to the scheduler queue. 
#process_tasks(): Processes and executes tasks in the order they were added until the queue is empty.

class Task:
    def __init__(self):
        self.queue = []

    def add_task(self,task):
        self.queue.append(task)

    def process_task(self):

        if self.queue:
            return self.queue.pop()
        

 

#Implement undo/redo functionality in a text editor using a stack. Design a class that supports the following methods: 
#insert(text): Inserts the given text into the document. 
#delete(): Deletes the last inserted text. 
#undo(): Reverts the most recent action (insertion or deletion). 
#redo(): Reapplies the most recently undone action. 

# class TextEditor:
#     def __init__(self):
#         self.stack = []
#         self.redo_stack = []
        
#     def insert(self,text):
#         self.stack.append(text)
#         self.redo_stack = []
#         print(self.stack)

#     def delete(self):
#         if self.stack:
#             deleted_text = self.stack.pop()
#             self.redo_stack.append(deleted_text)
#             print(self.stack)
#             print(self.redo_stack)
#     def undo(self):
#         if self.stack:
#             deleted_text = self.stack.pop()
#             self.redo_stack.append(deleted_text)
            
#     def redo(self):
#         if self.redo_stack:
#             restored_text = self.redo_stack.pop()
#             self.stack.append(restored_text)
           
#             print(self.stack)
            


# text = TextEditor()

# text.insert("ola")
# text.delete()
# text.undo()
# text.redo()




#Implement a message broadcasting system using a queue. Design a class that supports the following methods: 
#broadcast(message): Adds a message to the broadcasting queue. 
#send_messages(): Sends the messages to the recipients in the order they were added to the queue. 


# class Broadcast:
#     def __init__(self):
#         self.queue = []

#     def broadcast(self,message):
#         self.queue.append(message)
#         return self.queue

#     def send_messages(self):
#         while self.queue:
#            messages = self.queue.pop(0)
#            return messages








    
    
            
            

    












    





