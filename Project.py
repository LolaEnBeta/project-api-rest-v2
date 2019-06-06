
class Project(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_json(self):
        return {
            "name": self.name,
            "id": self.id,
            "tasks": self.tasks
        }
