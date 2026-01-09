import sys

class Task:
    def __init__(self,name):
        self.name = f"{name}"
        self.state = 0

    def change_state(self):
        self.state = 1
        return
    
    def change_name(self, new_name):
        self.name = new_name
        return
    