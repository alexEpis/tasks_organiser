# task_manager.py

from datetime import date
import storage
from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = storage.load_tasks()

    def add_task(self, title, due_date, task_type, frequency=None, occurrences=None):
        task = Task(title, due_date, task_type, frequency, occurrences)
        storage.save_task(task)
        self.tasks[title] = task

    def complete_task(self, title):
        task = self.tasks.get(title)
        if task:
            task.mark_completed()

            if task.task_type == 'periodic':
                task.calculate_next_due()

            storage.save_task(task)
        else:
            print(f"Task '{title}' not found.")

    def delete_task(self, title):
        if title in self.tasks:
            storage.delete_task(title)
            del self.tasks[title]

    def edit_task(self, original_title, **updates):
        task = self.tasks.get(original_title)

        if not task:
            raise ValueError(f"Task '{original_title}' not found.")

        if 'title' in updates:
            # Handle changing the title separately since it's the key in self.tasks
            new_title = updates['title']
            storage.delete_task(original_title)  # Delete the old task from storage
            task.title = new_title
            self.tasks[new_title] = task
            del self.tasks[original_title]
        if 'due_date' in updates:
            task.due_date = updates['due_date']
        if 'task_type' in updates:
            task.task_type = updates['task_type']
        if 'frequency' in updates:
            task.frequency = updates['frequency']
        if 'occurrences' in updates:
            new_total_occurrences = updates['occurrences']
            assert new_total_occurrences >= task.completed_occurrences, \
                "New occurrences must not be less than the number of already completed occurrences."
            task.occurrences = new_total_occurrences
        storage.save_task(task)  # Save the updated task

    def get_tasks_for_today(self):
        today = date.today()
        return [task for task in self.tasks.values() if task.due_date <= today and not task.completed]

    def get_completed_tasks_for_today(self):
        today = date.today()
        return [task for task in self.tasks.values() if task.completion_date == today]

    def get_completed_tasks(self):
        return [task for task in self.tasks.values() if task.completed]

    def reload_tasks(self):
        self.tasks = storage.load_tasks()


if __name__ == "__main__":
    task_manager = TaskManager()
    for _task in task_manager.tasks:
        print(f"{_task}: {repr(task_manager.tasks[_task])}")
    print(task_manager.tasks)
