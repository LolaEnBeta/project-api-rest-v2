from flask import Flask, jsonify, abort, make_response
from Project import Project

project_counter_id = 2

projects = [
    {
        "Name": "Project one",
        "id": 1
    },
    {
        "Name": "Project two",
        "id": 2
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

if __name__ == "__main__":
    app.run(debug=True)
