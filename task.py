# task.py

from datetime import date, timedelta


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
            self.occurrences = occurrences  # Total occurrences
            self.completed_occurrences = 0  # Initialize completed occurrences

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
            self.completed_occurrences = None
            self.frequency = None
        else:
            raise ValueError(f"Task type must be 'once' or 'periodic' ('{task_type}' was given).")

    def __str__(self):
        return f"{self.title} - Due: {self.due_date} - Completed: {self.completed}"

    def __repr__(self):
        return f"Task('{self.title}', '{self.due_date}', '{self.task_type}', '{self.frequency}', {self.completed})"

    def mark_completed(self):
        # Mark the task as completed
        self.completed = True
        self.completion_date = date.today()
        if self.task_type == 'periodic':
            self.completed_occurrences += 1
            # Calculate the next due date if there are more occurrences left
            if self.completed_occurrences < self.occurrences:
                self.calculate_next_due()

    def calculate_next_due(self):
        if self.task_type == 'periodic':
            assert isinstance(self.frequency, int), f"Frequency must be an integer ({type(self.frequency)} was given)."
            self.due_date += timedelta(days=self.frequency)
            self.completed = False
        else:
            raise ValueError("Only periodic tasks can calculate next due date.")
