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
    """Lists tasks with an index for easy selection."""
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.title}")
    print()  # Add a newline for better formatting
