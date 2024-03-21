# task.py

from datetime import datetime, date, timedelta


class Task(object):
    def __init__(self, title, due_date, task_type, frequency=None, occurrences=None):
        assert isinstance(due_date, date), f"Due date must be a date object ({type(due_date)} was given)."

        self.title = title
        self.due_date = due_date
        self.task_type = task_type  # 'once' or 'periodic'
        self.completed = False
        self.completion_date = None

        if task_type == 'periodic':
            assert isinstance(occurrences, int), f"Occurrences must be an integer ({type(occurrences)} was given)."
            self.occurrences = occurrences

            if isinstance(frequency, str):
                assert frequency in ['daily', 'monthly', 'yearly'], f"Invalid frequency: {frequency}"
                if frequency == 'daily':
                    self.frequency = 1
                elif self.frequency == 'monthly':
                    self.frequency = 30  # Simplification
                elif self.frequency == 'yearly':
                    self.frequency = 365  # Simplification
            elif isinstance(frequency, int):
                self.frequency = frequency
            else:
                raise ValueError("Frequency must be a string or integer.")
        elif task_type == 'once':
            self.occurrences = None
            self.frequency = None
        else:
            raise ValueError(f"Task type must be 'once' or 'periodic' ('{task_type}' was given).")

    def __str__(self):
        return f"{self.title} - Due: {self.due_date} - Completed: {self.completed}"

    def __repr__(self):
        return f"Task('{self.title}', '{self.due_date}', '{self.task_type}', '{self.frequency}', {self.completed})"

    def mark_completed(self):
        self.completed = True
        self.completion_date = datetime.now().date()
        if self.task_type == 'periodic' and self.occurrences:
            self.occurrences -= 1  # Decrement occurrences
            if self.occurrences > 0:
                self.calculate_next_due()
            else:
                self.task_type = 'once'  # Effectively stops the task from recurring

    def calculate_next_due(self):
        if self.task_type == 'periodic':
            assert isinstance(self.frequency, int), f"Frequency must be an integer ({type(self.frequency)} was given)."
            self.due_date += timedelta(days=self.frequency)
            self.completed = False
        else:
            raise ValueError("Only periodic tasks can calculate next due date.")
