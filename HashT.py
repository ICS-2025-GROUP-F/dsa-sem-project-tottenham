# Define a Task object to store details like name, deadline, status, and priority
class Task:
    def __init__(self, name, deadline=None, status="pending", priority="normal"):
        self.name = name
        self.deadline = deadline
        self.status = status
        self.priority = priority

    def __repr__(self):
        # This defines how the task appears when printed
        return f"Task(name='{self.name}', status='{self.status}', priority='{self.priority}')"

# ToDoHashTable manages a collection of tasks using a dictionary (hash table)
class ToDoHashTable:
    def __init__(self):
        self.tasks = {}  # Store tasks with task name as the key

    def add_task(self, task):
        # Add or update a task using its name as the key
        self.tasks[task.name] = task

    def get_task(self, name):
        # Retrieve a task by name, or return None if not found
        return self.tasks.get(name)

    def remove_task(self, name):
        # Delete a task if it exists
        if name in self.tasks:
            del self.tasks[name]

    def list_tasks(self):
        # Return a list of all tasks
        return list(self.tasks.values())