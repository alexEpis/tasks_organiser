# storage.py

from datetime import date
import shelve
from task import Task
from typing import Dict


def save_task(task: Task, db_path="tasks.db"):
    with shelve.open(db_path) as db:
        db[task.title] = task


def delete_task(title, db_path="tasks.db"):
    with shelve.open(db_path) as db:
        if title in db:
            del db[title]


def load_tasks(db_path="tasks.db") -> Dict[str, Task]:
    with shelve.open(db_path) as db:
        return dict(db)


def get_task(title, db_path="tasks.db") -> Task:
    with shelve.open(db_path) as db:
        return db.get(title)


if __name__ == "__main__":
    # The storage module provides functions to save, load, delete, and retrieve tasks from a shelve database.
    task1 = Task("Do the dishes", date(2020, 12, 31), "once")
    task2 = Task("Walk the dog", date(2020, 12, 31), "periodic", "daily", 4)
    save_task(task1)
    save_task(task2)
    print(load_tasks())
    print(get_task("Walk the dog"))
    print(get_task("Walk the cat"))

    # Show the contents of the shelve database
    print("\nContents of the shelve database (before deleting anything):")
    with shelve.open("tasks.db") as db:
        print(dict(db))
        print(f"Task 'Do the dishes': {db.get('Do the dishes')}")
        print(f"Task 'Walk the dog': {db.get('Walk the dog')}")

    # Delete test tasks
    delete_task("Do the dishes")
    delete_task("Walk the dog")

    print("\nContents of the shelve database (after deleting anything):")
    with shelve.open("tasks.db") as db:
        print(dict(db))
        print(f"Task 'Do the dishes': {db.get('Do the dishes')}")
        print(f"Task 'Walk the dog': {db.get('Walk the dog')}")

