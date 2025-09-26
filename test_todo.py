import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import todo

def test_add_and_list(monkeypatch):
    # Setup
    test_file = "test_tasks.json"
    monkeypatch.setattr(todo, "TASK_FILE", test_file)
    if os.path.exists(test_file):
        os.remove(test_file)
    # Test add
    todo.add_task("Test Task")
    tasks = todo.load_tasks()
    assert tasks[0]["desc"] == "Test Task"
    assert not tasks[0]["done"]
    # Cleanup
    os.remove(test_file)

def test_complete_and_delete(monkeypatch):
    # Setup
    test_file = "test_tasks.json"
    monkeypatch.setattr(todo, "TASK_FILE", test_file)
    tasks = [{"desc": "Task 1", "done": False}]
    todo.save_tasks(tasks)
    # Test complete
    todo.complete_task(1)
    tasks = todo.load_tasks()
    assert tasks[0]["done"]
    # Test delete
    todo.delete_task(1)
    tasks = todo.load_tasks()
    assert len(tasks) == 0
    # Cleanup
    os.remove(test_file)
