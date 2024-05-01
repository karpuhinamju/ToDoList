from datetime import datetime, timedelta
import pickle


FILENAME = 'savefile'
class Task:
    DATETIME_FORMAT_INPUT = "%d/%m/%Y %H:%M"
    DATETIME_FORMAT_PRINT = "%d %b %Y %H:%M"
    DATETIME_FORMAT_BACKUP = "%d%m%Y_%H-%M-%S"

    counter = 0

    def __init__(self, name, description, deadline, is_done = False):
        self.id = Task.counter
        self.name = name
        self.description = description
        self.deadline = deadline
        self.is_done = is_done
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

def save_to_file(filename:str, object):
    with open(filename, 'wb') as f:
        pickle.dump(object, f, protocol=pickle.HIGHEST_PROTOCOL)

with open(FILENAME, 'rb') as f:
    tasks = pickle.load(f)
while True:
    command = input("Enter command: ")
    match command:
        case "backup"|"b":
            now = datetime.now()
            name = "backups/backup_" + now.strftime(Task.DATETIME_FORMAT_BACKUP)
            save_to_file(name, tasks)
            # создать файл рез. копии массива tasks с именем backup_<дата-время>
            # например backup_25042024_19-30-00
        case "load_backup"|"lb":
            filename = "backups/" + input("Enter file's name")
            with open(filename, 'rb') as f:
                tasks = pickle.load(f)
            print("your tasks have been loaded")
            # считать с клавиатуры имя файла и загрузить из него массив tasks
            # загрузку из файла вытащить в отдельную функцию
        case "save" | "s":
            save_to_file(FILENAME, tasks)
        case "add_task" | "a":
            handle_add_task(tasks)
        case "help" | "h":
            print("this is help")
        case "exit" | "q":
            s = input("Save? Y/N")
            if s.lower() == 'y':
                save_to_file(FILENAME, tasks)
            break
        case "show_tasks" | "st":
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
        case "show_on_fire" | "sf":
            res = []
            days = int(input("Введите дни:"))
            hours = int(input("Введите часы:"))
            minutes = int(input("Введите минуты:"))
            now = datetime.now()
            delta = timedelta(days=days, hours=hours, minutes=minutes)
            threshold = now + delta
            for task in tasks:
                if threshold > task.deadline and task.is_done == False:
                    res.append(task)
            for task in res:
                print(task)
        case "show_expired"|"se":
            res = []
            now = datetime.now()
            for task in tasks:
                if now > task.deadline:
                    res.append(task)
            for task in res:
                print(task)
        case "delete_expired"|"de":
            i = 0
            now = datetime.now()
            while i < len(tasks):
                if now > tasks[i].deadline:
                    del tasks[i]
                    i -= 1
                i += 1
            print("All expired tasks were deleted")
        case _:
            print("unknown command")
