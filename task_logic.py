from db.db_handler import read_tasks, write_task

def help():
    print("\nAvailable commands:")
    print("exit  - Exit the program")
    print("list  - List all tasks")
    print("add <your-task>  - Add a new task (you'll be asked for priority: 'h' for High, 'm' for Medium and 'l' for Low)")
    print("delete all  - Delete all tasks")
    print("delete <task-id>  - Delete a specific task by its ID")
    print()

def list():
    tasks = read_tasks()
    print("ID -     Description     -    Priority")
    for i,task in enumerate(tasks,0):
        print(f'{i}  -  {task["description"]}  -  {task["priority"]}')

def add(description: str):
    priority = input("Enter your priority : ")
    while priority not in {'h', 'm', 'l'}:
        if(priority == "exit"): break
        priority = input("Please enter a valid priority (check help for more info) : ")
    if(priority == "exit"): return

    tasks = read_tasks()
    task = {
        "description" : description,
        "status" : False,
        "priority" : priority,
    }
    tasks.append(task)
    tasks.sort(key=lambda t: {'h': 0, 'm': 1, 'l': 2}[t["priority"]])
    write_task(tasks)

def deleteAll():
    write_task([])

def delete(id: int):
    tasks = read_tasks()
    if(0 <= id < len(tasks)): del tasks[id]
    else : print("Invalid ID")
    write_task(tasks)