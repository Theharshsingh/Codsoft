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

#to run the To-Do List application
    def main():
        todo_list = ToDoList()

#loop
        while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("enter an option(1-5):")  

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added.")

        elif choice == '2':
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(todo_list.tasks):
                todo_list.remove_task(todo_list.tasks[task_index])
                print("Task removed.")
            else:
                print("Invalid task number.") 

        elif choice == '4':
            todo_list.display_tasks()


        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()