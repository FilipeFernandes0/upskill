'''
Managment of my tasks
'''

from datetime import datetime
from enum import Enum

class TaskError(RuntimeWarning):
    pass

class Priority(Enum):
    LOW = 0
    NORMAL = 1
    HIGH = 2

class Task:
    __task_num = 0
    def __init__(self, design):
        Task.__task_num += 1
        self.__id = Task.__task_num
        self.__design = design

        
        now = datetime.now()
        self.__conclusion = datetime(now.year, now.month, now.day, hour=23, minute=59)
        self.__timestamps = [] 
        self.__timestamp = None
        self.__elapsed_time = 0.0
        
       

        self.__categories = []
        self.__priority = Priority.NORMAL
        
        # ...
        self.__completed = False
    

    def start(self):
        if self.__timestamp != None:
            raise TaskError('Error: clock is already running')
         
        self.__timestamp = Timestamps()
        self.__timestamps.append(Timestamps(self.__timestamp))
        
    def stop(self):
        if self.__timestamp is None:
            raise TaskError('Error: clock not started')
        self.__timestamp.end(datetime.now())
        self.__elapsed_time += self.__timestamp.secs()

        self.__timestamp = None
    

    def get_id(self):
        return self.__id

    def get_design(self):
        return self.__design       

    def __str__(self):
        return str(self.get_id()) + ' - ' + self.get_design() + ' - ' + str(self.__conclusion) \
        +' - ' + str(self.__categories) \
            + ' - ' + str(self.__priority) + ' - ' + str(self.__completed) + ' - ' + str(self.__elapsed_time)
    
   
    def isClockRunning(self):
        return self.__timestamp != None

    def isCompleted(self):
        return self.__completed
    
    def complete(self):
        if self.isCompleted():
            raise TaskError('Error: Task already completed')
        
        if self.isClockRunning(): self.stop()
        self.__completed = True

    def get_timestamps(self):
        return self.__timestamps[:]

class TaskList:
    def __init__(self):
        self.__tasks = []
    
    def create_task(self, task):
        self.__tasks.append(task)
    
    def on_going_tasks(self):
        on_going = []
        for task in self.__tasks:
            if not task.isCompleted():
                on_going.append(task)
        return on_going
    
    def completed_tasks(self):
        completed = []
        for task in self.__tasks:
            if task.isCompleted():
                completed.append(task)
        return completed

    def retrieve_task(self, id):
        for task in self.__tasks:
            if task.get_id() == id:
                return task
        return None
class Timestamps:
    def __init__(self, begin = datetime.now(), end = None):
        
        self.__begin = begin
        self.__end = end

    def __str__(self):
       return str(self.__begin) +  "->" + str(self.__end)

    def begin(self,moment):
        if self.__end == None or moment >= self.__end:
            raise TaskError("error: begin Time after end Time")
        self.__begin = moment
    def end(self,moment = datetime.now()):
        if self.__begin == None or moment <= self.__begin:
            raise TaskError("error: end Time before begin Time")
        self.__end = moment

    def secs(self):
        if self.__begin == None or self.__end == None:
            raise TaskError("error: None on begin or end time")
        return  (self.__end - self.__begin).total_seconds()


if __name__ == '__main__':
    #import time
    import traceback
    import time
    from random import randrange

    my_tasks = TaskList()
    

    aTask = Task('My first task')
    aTask.start()
    my_tasks.create_task(aTask)
    
    
    aTask = Task("My second task")
    aTask.start()
    my_tasks.create_task(aTask)
    

    aTask = Task("My Third task")
    my_tasks.create_task(aTask)
   

    del aTask

    for task in my_tasks.on_going_tasks():
        print(task)
      
    try:
        aTask = my_tasks.retrieve_task(1)
        
        
    except TaskError:
        print('Task error!!!: Task already running', traceback.format_exc(), sep='\n')

    time.sleep(randrange(1,2))
    
    aTask.stop()
  

    aTask.complete()
    
  

    aTask = my_tasks.retrieve_task(2)
    time.sleep(randrange(1,2))
    aTask.stop()
    

    aTask = my_tasks.retrieve_task(3)
    time.sleep(randrange(1,2))
    
    

   

    print("Ongoing tasks")

    for task in my_tasks.on_going_tasks():
        print(task)

    print("completed tasks")

    for task in my_tasks.completed_tasks():
        print(task)
        print('Timestamps:')
        for timestamp in task.get_timestamps():
            print(timestamp)
    
    print("Ongoing tasks")

    for task in my_tasks.on_going_tasks():
        print(task)
    
    

