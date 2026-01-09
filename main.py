import sys
from task import Task
from tasks import Tasks

command_with_txt = {"add"}
command_with_id_and_txt = {"remove","done"}

def main():
    
    cmd = []

    if len(sys.argv) == 1:
        cmd = input("insert command, 'quit' to close the program:  ").split()
        
        if len(cmd) > 1:
            return print("Use: <cmd> ")
        
        cmd = cmd[0]
        
        if cmd == "quit":
            return

        if cmd in command_with_txt:
            name = input("task:  ")

        elif cmd in command_with_id_and_txt:
            name = input("task or id:  ")
        
        else:
            name = None

        tasks = Tasks()
        Tasks.execute_command(tasks,cmd,name)

    else:
        cmd = sys.argv[1]
        name = ' '.join(sys.argv[2:])

        if cmd == "quit":
            return
    
        if name == '':
            if cmd in command_with_txt:
                name = input("task:  ")
        
            elif cmd in command_with_id_and_txt:
                name = input("task or id:  ")

            else:
                name = None

        tasks = Tasks()
        Tasks.execute_command(tasks,cmd,name)
    fetch(tasks)
    return

def fetch(tasks):

    cmd,*name = input("insert command, 'quit' to close the program:  ").split()

    name = ' '.join(name)
    if name == '':
        if cmd == "quit":
            return
        else:
            if cmd in command_with_txt:
                name = input("task:  ")

            elif cmd in command_with_id_and_txt:
                name = input("task or id:  ")
                
            else:
                name = None

    Tasks.execute_command(tasks,cmd,name)
    fetch(tasks)
    return

if __name__ == "__main__":
    main()