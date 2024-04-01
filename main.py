import datetime
class Task:
    counter = 0
    def __init__(self, name, description, deadline):
        self.id = Task.counter
        self.name = name
        self.description = description
        self.deadline = deadline
        Task.counter += 1
    def __str__(self):
        return f"id={self.id},name={self.name},desc={self.description},dl={self.deadline}"
def handle_add_task(task_array):
    name = input("Enter the task's name: ")
    description = input("Enter the task's description: ")
    deadline = input("Enter the task's deadline: ")
    task = Task(name, description, deadline)
    task_array.append(task)
tasks = []
while True:
    tasks.append(Task("n1", "d1", "dl1"))
    tasks.append(Task("n2", "d2", "dl2"))
    tasks.append(Task("n3", "d3", "dl3"))
    command = input("Enter command: ")
    match command:
        case "add_task":
            handle_add_task(tasks)
        case "help":
            print("this is help")
        case "exit":
            break
        case "show_tasks":
            for task in tasks:
                print(task)
        case _:
            print("unknown command")