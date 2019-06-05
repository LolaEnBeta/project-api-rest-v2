
class Project(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_json(self):
        return {
            "name": self.name,
            "id": self.id
        }
