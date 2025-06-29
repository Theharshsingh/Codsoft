#taskclass
class Task:
    def __init__(self, title, description, due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔️" if self.completed else "❌"
        return f"{status} {self.title} - {self.description} (Due: {self.due_date})"

#ToDoList Class    
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def mark_task_completed(self, task):
        task.mark_completed()

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return
        for task in self.tasks:
            print(task)
