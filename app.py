import subprocess
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def tocal():
    data = request.json
    return subprocess.run(
        [
            "tocal",
            "+{}".format(data["offset"]),
            "/{}".format(data["duration"]),
            data["summary"],
        ],
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8")
