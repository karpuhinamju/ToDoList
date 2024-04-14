from datetime import datetime, timedelta


class Task:
    DATETIME_FORMAT_INPUT = "%d/%m/%Y %H:%M"
    DATETIME_FORMAT_PRINT = "%d %b %Y %H:%M"

    counter = 0

    def __init__(self, name, description, deadline):
        self.id = Task.counter
        self.name = name
        self.description = description
        self.deadline = deadline
        self.is_done = False
        Task.counter += 1

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.description}). deadline: {self.deadline.strftime(Task.DATETIME_FORMAT_PRINT)} (left: {timedelta_str(self.deadline - datetime.now())}),done={self.is_done}"


def timedelta_str(delta: timedelta):
    s = ""
    if delta.days != 0:
        s += f"{delta.days} days "

    hours = delta.seconds // 3600
    minutes = (delta.seconds - 3600 * hours) // 60
    s += f"{hours}h {minutes}m"
    return s
def handle_add_task(task_array):
    name = input("Enter the task's name: ")
    description = input("Enter the task's description: ")
    deadline_str = input("Enter the task's deadline. Format: (dd/mm/yyyy HH:MM)")
    deadline = datetime.strptime(deadline_str, Task.DATETIME_FORMAT_INPUT)
    task = Task(name, description, deadline)
    task_array.append(task)


tasks = []
tasks.append(Task("n1", "d1", datetime(2024, 1, 24, 12, 30)))
tasks.append(Task("n2", "d2", datetime(2024, 4, 14, 11, 30)))
tasks.append(Task("n3", "d3", datetime(2024, 11, 14, 12, 30)))
while True:
    command = input("Enter command: ")
    match command:
        case "add_task" | "a":
            handle_add_task(tasks)
        case "help" | "h":
            print("this is help")
        case "exit" | "q":
            break
        case "show_tasks" | "s":
            for task in tasks:
                print(task)
        case "delete_by_id" | "d":
            i = 0
            iddel = int(input("Введите id задачи: "))
            while i < len(tasks):
                if tasks[i].id == iddel:
                    del tasks[i]
                    break
                i += 1
        case "resolve_task" | "rt":
            i = 0
            id = int(input("Введите id задачи"))
            while i < len(tasks):
                if tasks[i].id == id:
                    tasks[i].is_done = True
                    break
                i += 1
        case "delete_resolved" | "dr":
            i = 0
            isd_tasks = []
            while i < len(tasks):
                if tasks[i].is_done:
                    isd_tasks.append(tasks[i])
                    del tasks[i]
                    i -= 1
                i += 1
                for task in isd_tasks:
                    print("the task with id", task.id, "has been deleted")
            print(len(isd_tasks), "task(s) have been deleted")
        case "show_unresolved" | "su":
            unr_tasks = []
            i = 0
            while i < len(tasks):
                if tasks[i].is_done == False:
                    unr_tasks.append(tasks[i])
                i += 1
            for task in unr_tasks:
                print(task)
        case _:
            print("unknown command")
