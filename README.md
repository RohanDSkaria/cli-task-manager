# CLI Task Manager

A simple and efficient command-line task manager that helps you organize your tasks with priority levels and completion status tracking.

## Features

- Add tasks with priority levels (High, Medium, Low)
- List all tasks or filter by status (Pending/Completed)
- Mark tasks as done or pending
- Delete individual tasks or clear all tasks
- Tasks are automatically sorted by priority
- Persistent storage using JSON

## Installation

1. Clone the repository:
```bash
git clone https://github.com/RohanDSkaria/cli-task-manager.git
cd cli-task-manager
```

## Usage

Run the program:
```bash
python3 main.py
```

### Available Commands

- `help` - Display all available commands
- `list` - List all pending tasks
- `list all` - List all tasks (both pending and completed)
- `list done` - List all completed tasks
- `add <your-task>` - Add a new task
  - You'll be prompted to enter priority:
    - `h` for High
    - `m` for Medium
    - `l` for Low
- `delete all` - Delete all tasks
- `delete <task-id>` - Delete a specific task by its ID
- `mark <task-id> <1/0>` - Mark task as done (1) or pending (0)
- `exit` - Exit the program

### Example Usage

```
Welcome to your CLI Task Manager!
Please Type "help" to see the available commands

> add Buy groceries
Enter your priority : h

> list
ID    Description                                                    Status    Priority
--------------------------------------------------------------------------------------
0     Buy groceries                                                 Pending   h

> mark 0 1

> list done
ID    Description                                                    Status    Priority
--------------------------------------------------------------------------------------
0     Buy groceries                                                 Done      h
```