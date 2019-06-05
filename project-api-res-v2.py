from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)
