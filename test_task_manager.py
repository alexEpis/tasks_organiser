# test_task_manager.py

import unittest
from datetime import datetime, date, timedelta
from task import Task
from task_manager import TaskManager


class TestTask(unittest.TestCase):

    def test_task_creation(self):
        # due_date = datetime.now().date()
        due_date = date.today()
        task = Task("Test Task", due_date, "once")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.due_date, due_date)
        self.assertEqual(task.task_type, "once")

    def test_periodic_task_next_due_daily(self):
        due_date = date.today()
        task = Task("Daily Task", due_date, "periodic", "daily", 4)
        task.calculate_next_due()
        self.assertEqual(task.due_date, due_date + timedelta(days=1))

    def test_periodic_task_next_due_custom_frequency(self):
        due_date = date.today()
        task = Task("Custom Frequency Task", due_date, "periodic", 5, 3)
        task.calculate_next_due()
        self.assertEqual(task.due_date, due_date + timedelta(days=5))

    def test_periodic_task_next_due_custom_frequency_daily(self):
        # due_date = datetime.now().date()
        due_date = date.today()
        task = Task("Custom Frequency Task", due_date, "periodic", 'daily', 3)
        task.calculate_next_due()
        self.assertEqual(task.due_date, due_date + timedelta(days=1))


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()
        self.today = date.today()

    def test_add_task(self):
        self.manager.add_task("Test Task", self.today, "once")
        tasks = self.manager.get_tasks_for_today()
        self.assertTrue(any(task.title == "Test Task" for task in tasks))

    def test_complete_task(self):
        title = "Complete Me"
        self.manager.add_task(title, self.today, "once")
        self.manager.complete_task(title)
        self.assertTrue(self.manager.tasks[title].completed)

    def test_add_task_periodic(self):
        self.manager.add_task("Test Task Periodic", self.today, "periodic", "daily", 4)
        tasks = self.manager.get_tasks_for_today()
        self.assertTrue(any(task.title == "Test Task Periodic" for task in tasks))

    def tearDown(self):
        # Cleanup logic if needed, e.g., deleting test tasks from a test database or file
        self.manager.delete_task("Test Task")
        self.manager.delete_task("Complete Me")
        self.manager.delete_task("Test Task Periodic")


if __name__ == '__main__':
    unittest.main()
