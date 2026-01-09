import sys
from task import Task

class Tasks:
    def __init__(self):
        self.tasks = {}
        self.ids = {}
        self.counter = 0
        self.last_task = ()
        self.comands = {"add": Tasks.add,
                        "ls" : Tasks.ls,
                        "quit": Tasks.quit,
                        "done": Tasks.done,
                        "remove": Tasks.remove}
        return

    def add(self,new_task_name):
        new_task = Task(new_task_name)
        new_id = self.counter

        self.tasks[new_id] = [new_task]
        self.ids[new_task.name] = new_id
        self.last_task = (new_task)
        
        return

    def ls(self,name = None):

        if len(self.tasks) == 0:
            print("No added tasks")
            return
        
        for task_id in self.tasks:
            i_task = self.tasks[task_id]
            if i_task.state == 0:
                print(f"task: {i_task.name}, id: {task_id}. Incomplete")
            else:
                print(f"task: {i_task.name}, id: {task_id}. Done")
        
        return

    def done(self,reference):
        reference = str(reference)
        
        if reference in self.ids:
            reference = self.ids[reference]

        Task.change_state(self.tasks[reference])

        return

    def remove(self,reference):
        reference = str(reference)
        
        if reference in self.ids:
            reference = self.ids[reference]

        self.tasks.pop(reference)        

        return
    
    def execute_comand(self,cmd,name = None):
        self.comands[cmd](name)

        return