import json

with open("config.json") as f:
    config = json.load(f)

db_path = config["DB_PATH"]

if(db_path is None): raise ValueError("DB_PATH is not set in config.json")

def write_task(task):
    with open(db_path,'w') as f:
        json.dump(task, f, indent=4)

def read_tasks():
    with open(db_path, 'r') as f:
        return json.load(f)