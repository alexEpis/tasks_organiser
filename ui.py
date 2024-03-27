# ui.py

import os
import platform


def clear_screen():
    """Clears the command line screen."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def list_tasks(tasks):
    """Lists tasks with an index for easy selection and displays completion info for periodic tasks."""
    for index, task in enumerate(tasks, start=1):
        if task.task_type == "once":
            display_str = f"{index}. {task.title} <1>"
        else:
            display_str = f"{index}. {task.title} <{task.completed_occurrences}/{task.occurrences}>"
        print(display_str)
    print()  # Add a newline for better formatting
