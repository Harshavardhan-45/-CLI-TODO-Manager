import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"desc": description, "done": False})
    save_tasks(tasks)

def complete_task(idx):
    tasks = load_tasks()
    if 0 < idx <= len(tasks):
        tasks[idx-1]["done"] = True
        save_tasks(tasks)

def delete_task(idx):
    tasks = load_tasks()
    if 0 < idx <= len(tasks):
        tasks.pop(idx-1)
        save_tasks(tasks)
