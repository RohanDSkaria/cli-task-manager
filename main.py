import json

db_path = "db/tasks.json"

def write_task(task):
    with open(db_path,'w') as f:
        json.dump(task, f, indent=4)

def read_tasks():
    with open(db_path, 'r') as f:
        return json.load(f)

def main():

    print("\nWelcome to your CLI Task Manager!")
    print("Please Type \"help\" to see the available commands\n")

    while True:
        command = input()

        if(command == "exit"): break

        elif(command == "help"):
            print("\nAvailable commands:")
            print("exit - Exit the program")
            print("add - Add a new task")
            print()

        elif(command == "list"):
            tasks = read_tasks()
            print("\n")
            for task in tasks:
                print(f'{task["id"]} {task["description"]}')

        elif(command[:3] == "add"):
            description = command[4:]
            tasks = read_tasks()
            task = {
                "id" : len(tasks)+1,
                "description" : description,
                "status" : False
            }
            tasks.append(task)
            write_task(tasks)
        
        elif(command == "delete all"):
            write_task([])

        elif(command[:6] == "delete"):
            id = int(command[7:])
            tasks = read_tasks()
            newTasks = []
            foundId = False

            for task in tasks:
                if(task["id"] == id): foundId = True
                else:
                    if(foundId): task["id"] -= 1
                    newTasks.append(task)

            write_task(newTasks)

if __name__ == "__main__":
    main()