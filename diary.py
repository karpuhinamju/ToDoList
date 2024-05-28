from datetime import timedelta, datetime
from task import Task
import pickle

class Diary:
    def __init__(self, tasks: list[Task], save_file= "savefile"):
        self.tasks = tasks
        self.save_file = save_file
    def create_task(self, name, description, deadline_str, format):
        deadline = datetime.strptime(deadline_str, format)
        task = Task(name, description, deadline)
        self.tasks.append(task)
    def add_task(self, task):
        self.tasks.append(task)
    def edit_task(self, id, new_name, new_description, new_deadline):
        i = 0
        while i < len(self.tasks):
            if id == self.tasks[i].id:
                break
            i += 1
        if i == len(self.tasks):
            return 1
        else:
            if new_name is not None:
                self.tasks[i].name = new_name
            if new_description is not None:
                self.tasks[i].description = new_description
            if new_deadline is not None:
                self.tasks[i].deadline = new_deadline
    def save(self):
        self.save_to_file(self.save_file, self.tasks)
    def save_to_file(self, filename, object):
        with open(filename, 'wb') as f:
            pickle.dump(object, f, protocol=pickle.HIGHEST_PROTOCOL)

    def show_tasks(self):
        s = ""
        for task in self.tasks:
            s += task.__str__()
        return s
    def load(self, filename):
        with open(self.save_file if filename is None else filename, 'rb') as f:
            self.tasks = pickle.load(f)
            max_id = 0
            for task in self.tasks:
                if task.id > max_id:
                    max_id = task.id
            Task.counter = max_id + 1
    def delete_by_id(self, id):
        i = 0
        while i < len(self.tasks):
            if self.tasks[i].id == id:
                del self.tasks[i]
                break
            i += 1
    def resolve_task(self, id):
        i = 0
        while i < len(self.tasks):
            if self.tasks[i].id == id:
                self.tasks[i].is_done = True
                break
            i += 1
    def delete_resolved(self) -> list[Task]:
        i = 0
        isd_tasks = []
        while i < len(self.tasks):
            if self.tasks[i].is_done:
                isd_tasks.append(self.tasks[i])
                del self.tasks[i]
                i -= 1
            i += 1
        return isd_tasks
    def show_unresolved(self):
        unr_tasks = []
        i = 0
        while i < len(self.tasks):
            if self.tasks[i].is_done == False:
                unr_tasks.append(self.tasks[i])
            i += 1
        return unr_tasks
    def show_on_fire(self, delta):
        res = []
        now = datetime.now()
        threshold = now + delta
        for task in self.tasks:
            if threshold > task.deadline and task.is_done == False:
                res.append(task)
        return res
    def show_expired(self):
        res = []
        now = datetime.now()
        for task in self.tasks:
            if now > task.deadline:
                res.append(task)
        return res
    def delete_expired(self):
        i = 0
        now = datetime.now()
        while i < len(self.tasks):
            if now > self.tasks[i].deadline:
                del self.tasks[i]
                i -= 1

    def has_task_with_id(self, id):
        return id in [task.id for task in self.tasks]
    def  change_task(self, id, new_name, new_description, new_deadline, no_update_str = "-"):
        i = 0
        while i < len(self.tasks):
            if self.tasks[i].id == id:
                break
            i += 1
        if i == len(self.tasks):
            return
        if new_name != no_update_str:
            self.tasks[i].name = new_name
        if new_description != no_update_str:
            self.tasks[i].description = new_description
        if new_deadline != no_update_str:
            self.tasks[i].deadline = new_deadline
    def search_task(self, name_part):
        i = 0
        res = []
        while i < len(self.tasks):
            if name_part in self.tasks[i].name:
                res.append(self.tasks[i])
            i += 1
        return res