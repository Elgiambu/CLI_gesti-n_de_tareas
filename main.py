import sys
from task import Task
from tasks import Tasks

comand_with_txt = {"add"}
comand_with_id_and_txt = {"remove","done"}

def main(quit = False):
    
    cmd = []

    if quit == True:
        return print("bye!")

    if len(sys.argv) == 1:
        cmd = input("insert comand, 'quit' to close the program:  ").split()
        
        if len(cmd) > 1:
            return print("Use: python tasker.py <cmd> <name_task>")
        
        cmd = cmd[0]
        
        if cmd == "quit":
            main(True)

        if cmd in comand_with_txt:
            name = input("task:  ")

        elif cmd in comand_with_id_and_txt:
            name = input("task or id:  ")
        
        else:
            name = None

        Tasks.execute_comand(cmd,name)

    else:
        cmd = sys.argv[1]
        name = ' '.join(sys.argv[2:])

        if cmd == "quit":
                main(True)
    
        if name == ' ':
            if cmd in comand_with_txt:
                name = input("task:  ")
        
            elif cmd in comand_with_id_and_txt:
                name = input("task or id:  ")

            else:
                name = None

        Tasks.execute_comand(cmd,name)
    

if __name__ == "__main__":
    main()