"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Index page"


@app.route("/post/<id_>", methods=["POST", "GET"])
def post(id_):
    if request.method == "POST":
        return f"Post id: {id_}"
    else:
        return f"This is a GET request"


@app.route("/user", methods=["POST", "GET"])
def user():
    return {
        "username": "Ayuda en Python",
        "email": "support@ayudaenpython.com",
    }


if __name__ == "__main__":
    app.run(debug=True)
