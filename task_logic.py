from db.db_handler import read_tasks, write_task

def help():
    print("\nAvailable commands:")
    print("exit  - Exit the program")
    print("list  - List all Pending tasks")
    print("list all  - List all tasks")
    print("list done  - List all Completed tasks")
    print("add <your-task>  - Add a new task (you'll be asked for priority: 'h' for High, 'm' for Medium and 'l' for Low)")
    print("delete all  - Delete all tasks")
    print("delete <task-id>  - Delete a specific task by its ID")
    print("mark <task-id> <1/0>  -  Mark task as done/pending")
    print()

def list(type: str):
    print(type)
    tasks = read_tasks()
    if not tasks:
        print("No tasks found")
        return
    
    print(f"{'ID':<5} {'Description':<60} {'Status':<9} {'Priority':<8}")
    print("-" * 86)

    isDone = False
    isPending = False
    for i,task in enumerate(tasks,0):
        status = "Done" if task["status"] else "Pending"
        if(type == "done" and not task["status"]): continue
        if(type == "" and task["status"]): continue
        if(type == "done"): isDone = True
        if(type == ""): isPending = True
        print(f'{i:<5} {task["description"]:<60} {status:<9} {task["priority"]:<8}')

    if(not isDone and type == "done"): print("No Completed tasks found")
    if(not isPending and type == ""): print("No Pending tasks found")


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
    else: print("Invalid ID")
    write_task(tasks)

def mark(id_val: str):
    id, val = map(int, id_val.split(" "))
    tasks = read_tasks()
    tasks[id]["status"] = val
    write_task(tasks)