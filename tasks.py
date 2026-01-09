import sys
from task import Task

class Tasks:
    def __init__(self):
        self.tasks = {}
        self.ids = {}
        self.counter = 0
        self.last_task = ()
        self.commands = {"add": Tasks.add,
                        "ls" : Tasks.ls,
                        "done": Tasks.done,
                        "remove": Tasks.remove}
        return

    def add(self, new_task_name):
        new_task = Task(new_task_name)
        new_id = self.counter
        self.counter += 1

        self.tasks[new_id] = new_task
        self.ids[new_task.name] = new_id
        self.last_task = (new_task)
        
        return

    def ls(self):

        if len(self.tasks) == 0:
            print("No added tasks")
            return
        
        for task_id in self.tasks:
            i_task = self.tasks[task_id]
            emoji = "✅" if i_task.state else "❎"
            print(f"📌 task: {i_task.name}, id: {task_id}. {emoji}")
        return

    def done(self, reference):
        reference = str(reference)
        
        if reference in self.ids:
            reference = self.ids[reference]

        Task.change_state(self.tasks[int(reference)])

        return

    def remove(self, reference):
        reference = str(reference)
        
        if reference in self.ids:
            reference = self.ids[reference]

        self.tasks.pop(int(reference))        

        return
    
    def execute_command(self, cmd, name = None):
        if cmd == "ls":
            self.commands[cmd](self)
        else:
            self.commands[cmd](self, name)
        return