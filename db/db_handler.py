import json
import os
from dotenv import load_dotenv

load_dotenv()
db_path = os.getenv("DB_PATH")

if(db_path is None) : raise ValueError("DB_PATH is not set in .env")

def write_task(task):
    with open(db_path,'w') as f:
        json.dump(task, f, indent=4)

def read_tasks():
    with open(db_path, 'r') as f:
        return json.load(f)