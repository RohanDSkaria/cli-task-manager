from db.db_handler import read_tasks, write_task

def help():
    print("\nAvailable commands:")
    print("exit  - Exit the program")
    print("list  - List all tasks")
    print("add <your-task>  - Add a new task")
    print("delete all  - Delete all tasks")
    print("delete <task-id>  - Delete a specific task by its ID")
    print()

def list():
    tasks = read_tasks()
    print("ID -  Description")
    for task in tasks:
        print(f'{task["id"]}  -  {task["description"]}')

def add(description: str):
    tasks = read_tasks()
    task = {
        "id" : len(tasks),
        "description" : description,
        "status" : False
    }
    tasks.append(task)
    write_task(tasks)

def deleteAll():
    write_task([])

def delete(id: int):
    tasks = read_tasks()
    newTasks = []
    foundId = False

    for task in tasks:
        if(task["id"] == id): foundId = True
        else:
            if(foundId): task["id"] -= 1
            newTasks.append(task)

    write_task(newTasks)