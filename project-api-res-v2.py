from flask import Flask, jsonify, abort, make_response, request
from Project import Project

project_counter_id = 2

projects = [
    {
        "name": "Project one",
        "id": 1,
        "tasks": []
    },
    {
        "name": "Project two",
        "id": 2,
        "tasks": []
    }
]

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/projects", methods=["GET"])
def get_projects():
    return jsonify({"projects": projects})

@app.route("/projects/<int:id>", methods=["GET"])
def get_project_by_id(id):
    for project in projects:
        if project["id"] == id:
            return jsonify({"project": project})
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
    projects.append(project.to_json())
    return jsonify({"projects": projects})

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request"}), 400)

@app.route("/projects/<int:id>", methods=["PUT"])
def modify_project_by_id(id):
    for project in projects:
        if project["id"] == id:
            project["name"] = request.json.get("name", project["name"])
            return jsonify({"project_modify": project})
    abort(404)

@app.route("/projects/<int:id>", methods=["DELETE"])
def delete_project_by_id(id):
    for project in projects:
        if project["id"] == id:
            projects.remove(project)
            return jsonify({"project": "Deleted"})
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)
