#!/usr/bin/env python3
"""Basic Flask App
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def greeting() -> str:
    """ GET /
    Return:
        - a greeting
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users/", methods=['POST'])
def register_user() -> str:
    """POST /users
    JSON body:
        - email
        - password
    Return:
        - JSON payload
    """
    email = request.form.get("email")
    pwd = request.form.get("password")
    try:
        user = AUTH.register_user(email, pwd)
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """POST /sessions
    Creates a new session for the user and creates a session id cookie
    JSON body:
        - email
        - password
    Return:
        - JSON payload
    """
    email = request.form.get("email")
    pwd = request.form.get("password")
    if AUTH.valid_login(email, pwd):
        s_id = AUTH.create_session(email)
        res = make_response(jsonify({"email": email, "message": "logged in"}))
        res.set_cookie("session_id", s_id)
        return res
    else:
        abort(401)


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """DELETE /sessions
    Destroys a session and redirects the user to GET /
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
