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
        return f"Task(title={self.title}, description={self.description}, due_date={self.due_date}, completed={self.completed})"