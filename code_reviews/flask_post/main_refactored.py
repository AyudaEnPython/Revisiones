"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Ayuda en Python"


@app.route("/post/<id_>", methods=["GET", "POST"])
def post(id_):
    if request.method == "GET":
        return f"Post id: {id_}"
    else:
        return f"This isn't a GET request"


@app.route("/user", methods=["GET", "POST"])
def user():
    return {
        "username": "AyudaEnPython",
        "email": "support@ayudaenpython.com",
    }


if __name__ == "__main__":
    app.run(debug=True)
