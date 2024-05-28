from datetime import datetime, timedelta
import pickle
import os
from diary import Diary
from util import *
from task import Task

SAVE_FILE_NAME = 'save_file'
BACKUP_PATH = 'backups'
if not os.path.exists(SAVE_FILE_NAME):
    save_to_file(SAVE_FILE_NAME, [])

if not os.path.isdir(BACKUP_PATH):
    os.makedirs(BACKUP_PATH)

diary = Diary([])
diary.load(None)
while True:
    command = input("Enter command: ")
    match command:
        case "backup" | "b":
            now = datetime.now()
            name = BACKUP_PATH + "/backup_" + now.strftime(Task.DATETIME_FORMAT_BACKUP)
            save_to_file(name, diary.tasks)
            # создать файл рез. копии массива tasks с именем backup_<дата-время>
            # например backup_25042024_19-30-00
        case "load_backup" | "lb":
            filename = BACKUP_PATH + "/" + input("Enter file's name")
            diary.load(filename)

            print("your tasks have been loaded")
            # считать с клавиатуры имя файла и загрузить из него массив tasks
            # загрузку из файла вытащить в отдельную функцию
        case "save" | "s":
            save_to_file(SAVE_FILE_NAME, diary.tasks)
        case "add_task" | "a":
            name = input("Enter the task's name: ")
            description = input("Enter the task's description: ")
            deadline_str = input("Enter the task's deadline. Format: (dd/mm/yyyy HH:MM)")
            diary.create_task(name, description, deadline_str, Task.DATETIME_FORMAT_INPUT)
        case "help" | "h":
            print("this is help")
        case "exit" | "q":
            s = input("Save? Y/N")
            if s.lower() == 'y':
                save_to_file(SAVE_FILE_NAME, diary.tasks)
            break
        case "show_tasks" | "st":
            for task in diary.tasks:
                print(task)
        case "delete_by_id" | "d":
            iddel = int(input("Введите id задачи: "))
            diary.delete_by_id(iddel)
        case "resolve_task" | "rt":
            id = int(input("Введите id задачи"))
            diary.resolve_task(id)
        case "delete_resolved" | "dr":
            deleted = diary.delete_resolved()
            for task in deleted:
                print("the task with id", task.id, "has been deleted")
            print(len(deleted), "task(s) have been deleted")

        case "show_unresolved" | "su":
            unr_tasks = diary.show_unresolved()
            for task in unr_tasks:
                print(task)
        case "show_on_fire" | "sf":
            days = int(input("Введите дни:"))
            hours = int(input("Введите часы:"))
            minutes = int(input("Введите минуты:"))
            delta = timedelta(days=days, hours=hours, minutes=minutes)
            res = diary.show_on_fire(delta)
            for task in res:
                print(task)
        case "show_expired" | "se":
            res = diary.show_expired()
            for task in res:
                print(task)
        case "delete_expired" | "de":
            diary.delete_expired()
            print("All expired tasks were deleted")
        case "search_task"|"search":
            search = input("Enter part of task's name")
            res = diary.search_task(search)
            for task in res:
                print(task)
        case "edit_tasks"|"et":
            id = int(input("Enter task's id"))
            if not diary.has_task_with_id(id):
                print(f"no task with id {id}")
            else:
                imya = input("Enter the task's name: ")
                opisanie = input("Enter the task's description: ")
                srock = input("Enter the task's deadline. Format: (dd/mm/yyyy HH:MM)")
                diary.change_task(id, imya, opisanie, srock)
        case _:
            print("unknown command")