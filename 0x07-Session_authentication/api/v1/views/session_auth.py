#!/usr/bin/env python3
""" Module of Session Authentication views
"""
from flask import jsonify, abort, Flask
from flask import request, jsonify, abort
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login_session():
    """POST /api/v1/auth_session/login/
    Creates a Session ID for the User ID
    JSON body:
        - email
        - password
    Return: 
        - dictionary representation of the User
    """
    email = request.form.get("email")
    pwd = request.form.get("password")
    if not email or not len(email):
        return jsonify({ "error": "email missing" }),400
    if not pwd or not len(email):
        return jsonify({ "error": "password missing" }), 400
    
    users = User.search({"email": email})
    if not users:
        return jsonify({ "error": "no user found for this email" }), 404
    for user in users:
        if not user.is_valid_password(pwd):
            return jsonify({ "error": "wrong password" }), 404
    
    session_id = auth.create_session(user.id)
    return User.to_dict()
