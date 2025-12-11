# todo_list.py
import datetime

class Task:
    def __init__(self, name, priority="Normal", due_date=None):
        self.name = name
        self.status = "Pending"  # Atributo 2
        self.priority = priority # Atributo 3
        self.due_date = due_date if due_date else datetime.date.today() # Atributo 4

    def mark_completed(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.name} | {self.status} | {self.priority} | {self.due_date}"

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority="Normal", due_date=None):
        new_task = Task(name, priority, due_date)
        self.tasks.append(new_task)
        return f"Task '{name}' added."

    def list_tasks(self):
        if not self.tasks:
            return "No tasks found."
        return [str(task) for task in self.tasks]

    def mark_task_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_completed()
                return f"Task '{task_name}' marked as completed."
        return f"Task '{task_name}' not found."

    def clear_list(self):
        self.tasks = []
        return "List cleared."

    # Funcionalidad extra para el 5to escenario
    def delete_task(self, task_name):
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.name != task_name]
        if len(self.tasks) < initial_count:
            return f"Task '{task_name}' deleted."
        return f"Task '{task_name}' not found."
