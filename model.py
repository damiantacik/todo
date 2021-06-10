from datetime import datetime, timedelta
from pprint import pprint as pp
from helpers import generate_id



todos = [
    {
        "id": 1,
        "title": "learn python",
        "status": False,
        "duration": 10,
        "created_date": datetime.now() - timedelta(days=3)
    },
    {
        "id": 5,
        "title": "learn python",
        "status": False,
        "duration": 10,
        "created_date": datetime.now() - timedelta(days=6)
    }
]


def add_todo(tasks, title, duration=60):
    todo = {
        "id": generate_id(tasks),
        "title": title,
        "status": False,
        "duration": duration,
        "created_date": datetime.now()
    }
    tasks.append(todo)


def find_todo_by_id(tasks, idx):
    for task in tasks:
        if task["id"] == idx:
            return task


def toggle_status(tasks, idx):
    task = find_todo_by_id(tasks, idx)
    task["status"] = not task["status"]


def delete_todo(tasks, idx):
    task = find_todo_by_id(tasks, idx)
    tasks.remove(task)  # works in lists, remove one task


def get_todos_with_status(tasks, status):
    tasks_with_status = []

    for task in tasks:
        if task["status"] == status:
            tasks_with_status.append(task)

    return tasks_with_status


def get_todos_by_date(tasks, order="asc"):
    order_bool = True if order == "des" else False
    return sorted(tasks, key=lambda task: task["created_date"], reverse=order_bool)


add_todo(todos, "cut")
add_todo(todos, "abc")
add_todo(todos, "cde", 120)
# toggle_status(todos, 5)
# toggle_status(todos, 6)
# delete_todo(todos, 5)
# pp(get_todos_with_status(todos, True))
# pp(find_todo_by_id(todos, 6))
pp(get_todos_by_date(todos, "des"))

