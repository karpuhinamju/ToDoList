from datetime import datetime, timedelta
from util import *

class Task:
    DATETIME_FORMAT_INPUT = "%d/%m/%Y %H:%M"
    DATETIME_FORMAT_PRINT = "%d %b %Y %H:%M"
    DATETIME_FORMAT_BACKUP = "%d%m%Y_%H-%M-%S"

    counter = 0

    def __init__(self, name, description, deadline, is_done=False):
        self.id = Task.counter
        self.name = name
        self.description = description
        self.deadline = deadline
        self.is_done = is_done
        Task.counter += 1

    def __str__(self):
        return f"[{self.id}] {self.name} ({self.description}). deadline: {self.deadline.strftime(Task.DATETIME_FORMAT_PRINT)} (left: {timedelta_str(self.deadline - datetime.now())}),done={self.is_done}"