# main.py

import sys
from datetime import datetime, timedelta
from time import sleep
from task_manager import TaskManager
import ui

PASSWORD = "password123"


def check_password(_input_password):
    return _input_password == PASSWORD


def main_loop(_task_manager):
    start_time = datetime.now()

    while True:
        current_time = datetime.now()
        if (current_time - start_time) > timedelta(hours=16):
            print("Application has been running for more than 16 hours. Exiting...")
            break

        ui.clear_screen()  # Clear screen at the beginning of each loop iteration
        print("Welcome to your Task Manager!")
        print("\nMain Menu:")
        print("1. Add a new task")
        print("2. View tasks for today")
        print("3. Mark a task as completed")
        print("4. Exit")
        print("5. Delete a task")
        print("6. Edit a task")

        choice = input("Choose an option: ")

        if choice == "1":
            ui.clear_screen()
            title = input("Enter task title: ")
            due_date = datetime.strptime(input("Enter due date (DD MM YYYY): "), "%d %m %Y").date()
            task_type = input("Enter task type (once/periodic): ").lower()
            assert task_type in ["once", "periodic"], \
                f"Task type must be 'once' or 'periodic' ('{task_type}' was given)."
            frequency = None
            if task_type == "periodic":
                frequency = int(input("Enter frequency (in days e.g. 2 for every other day or daily/monthly/yearly): "))
                occurrences = int(input("Enter the number of occurrences (or 0 for indefinite): "))
            else:
                frequency = None
                occurrences = None
            _task_manager.add_task(title, due_date, task_type, frequency, occurrences)
            print("Task added successfully.")
            sleep(2)  # Give user time to read the message

        elif choice == "2":
            ui.clear_screen()
            tasks = _task_manager.get_tasks_for_today()
            completed_tasks = _task_manager.get_completed_tasks_for_today()
            print("Tasks for Today:")
            ui.list_tasks(tasks)
            if completed_tasks:
                print("\nCompleted Tasks for Today:")
                ui.list_tasks(completed_tasks)
            input("Press Enter to return to the main menu...")

        elif choice == "3":
            ui.clear_screen()
            tasks = _task_manager.get_tasks_for_today()  # Use a different method if you want to select from all tasks
            print("Select a task to mark as completed:")
            ui.list_tasks(tasks)
            selection = int(input("Enter the number of the task: ")) - 1
            if 0 <= selection < len(tasks):
                selected_task = tasks[selection]
                _task_manager.complete_task(selected_task.title)
                print(f"Task '{selected_task.title}' marked as completed.")
            else:
                print("Invalid selection.")
            sleep(2)

        elif choice == "4":
            ui.clear_screen()
            print("Exiting...")
            break

        elif choice == "5":
            ui.clear_screen()
            title = input("Enter the title of the task to delete: ")
            _task_manager.delete_task(title)
            print(f"Task '{title}' deleted.")
            sleep(2)

        elif choice == "6":
            ui.clear_screen()
            original_title = input("Enter the original title of the task to edit: ")
            # Example edit process for the title; extend as needed for other attributes
            new_title = input("Enter new title (leave blank to keep unchanged): ").strip()
            updates = {}
            if new_title:
                updates['title'] = new_title
            # Add prompts and updates handling for other task attributes as needed
            _task_manager.edit_task(original_title, **updates)
            print(f"Task '{original_title}' updated.")
            sleep(2)

        else:
            print("Invalid choice, please try again.")
            sleep(2)


if __name__ == "__main__":
    input_password = input("Enter your password to access the Task Manager: ")
    if check_password(input_password):
        task_manager = TaskManager()
        main_loop(task_manager)
    else:
        sleep(2)
        print("Incorrect password. Exiting...")
        sys.exit(1)
