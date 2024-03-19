import datetime
class Task:
    id = 0
    name = ""
    description = ""
    deadline = datetime.datetime


while True:
    command = input("Enter command: ")
    match command:
        case "add_task":
            print("this is add_task.")
        case "help":
            print("this is help")
        case "exit":
            break
        case _:
            print("unknown command")
