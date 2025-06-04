from task_logic import help, list, add, deleteAll, delete

def main():

    print("\nWelcome to your CLI Task Manager!")
    print("Please Type \"help\" to see the available commands\n")

    while True:
        command = input()
        if(command == "exit"): break
        elif(command == "help"): help()
        elif(command == "list"): list()
        elif(command[:3] == "add"): add(command[4:])
        elif(command == "delete all"): deleteAll()
        elif(command[:6] == "delete"): delete(int(command[7:]))

if __name__ == "__main__":
    main()