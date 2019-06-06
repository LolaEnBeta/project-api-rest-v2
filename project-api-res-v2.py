from flask import Flask, jsonify, abort, make_response, request
from Project import Project
from Task import Task

project_counter_id = 3
task_counter_id = 0

projects = []
projects.append(Project(1, "name"))
projects.append(Project(2, "name"))
projects.append(Project(3, "name"))

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/projects", methods=["GET"])
def get_projects():
    project_list = []
    for project in projects:
        project_list.append(project.to_json())
    return jsonify({"projects": project_list})

@app.route("/projects/<int:id>", methods=["GET"])
def get_project_by_id(id):
    for project in projects:
        if project.id == id:
            return jsonify({"project": project.to_json()})
    abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Project not found"}), 404)

@app.route("/projects", methods=["POST"])
def create_a_project():
    global project_counter_id
    if not "name" in request.json:
        abort(400)
    project_counter_id += 1
    name = request.json.get("name")
    project = Project(project_counter_id, name)
    projects.append(project)
    projects_json = [project.to_json() for project in projects]
    return jsonify({"projects": projects_json})

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request"}), 400)

@app.route("/projects/<int:id>", methods=["PUT"])
def modify_project_by_id(id):
    for project in projects:
        if project.id == id:
            project.name = request.json.get("name", project.name)
            return jsonify({"project_modified": project.to_json()})
    abort(404)

@app.route("/projects/<int:id>", methods=["DELETE"])
def delete_project_by_id(id):
    for project in projects:
        if project.id == id:
            projects.remove(project)
            return jsonify({"project": "Deleted"})
    abort(404)

@app.route("/projects/tasks", methods=["GET"])
def get_tasks():
    all_tasks = []
    for project in projects:
        for task in project.tasks:
            all_tasks.append(task.to_json())
    return jsonify({"tasks": all_tasks})

@app.route("/projects/<int:id>/tasks", methods=["GET"])
def get_tasks_from_project_by_id(id):
    task_list = []
    for project in projects:
        if project.id == id:
            for task in project.tasks:
                task_list.append(task.to_json())
            return jsonify({"tasks": task_list})
    abort(404)

@app.route("/projects/<int:id>/tasks", methods=["POST"])
def create_task_in_project(id):
    global task_counter_id
    if not "task_name" in request.json or not "description" in request.json:
        abort(400)
    for project in projects:
        if project.id == id:
            task_counter_id += 1
            task_name = request.json.get("task_name")
            description = request.json.get("description")
            task = Task(task_counter_id, task_name, description)
            project.add_task(task)
            return jsonify({"task_added": task.to_json()})

@app.route("/projects/<int:id>/tasks/<int:task_id>", methods=["DELETE"])
def remove_task_by_id(id, task_id):
    for project in projects:
        if project.id == id:
            for task in project.tasks:
                if task.id == task_id:
                    project.tasks.remove(task)
                    return jsonify({"task": "Deleted"})
    abort(404)

@app.route("/projects/<int:id>/tasks/<int:task_id>", methods=["PUT"])
def modify_task_by_id(id, task_id):
    for project in projects:
        if project.id == id:
            for task in project.tasks:
                if task.id == task_id:
                    task.task_name = request.json.get("task_name", task.task_name)
                    task.description = request.json.get("description", task.description)
                    return jsonify({"task_modified": task.to_json()})

if __name__ == "__main__":
    app.run(debug=True)
