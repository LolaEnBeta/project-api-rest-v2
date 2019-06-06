
class Task(object):
    def __init__(self, id, task_name, description):
        self.id = id
        self.task_name = task_name
        self.description = description
        self.completed = False

    def to_json(self):
        return {
            "task_name": self.task_name,
            "id": self.id,
            "description": self.description,
            "completed": self.completed
        }
