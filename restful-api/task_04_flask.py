#!/usr/bin/env python3
"""
4. Develop a Simple API using Python with Flask
"""
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """
    Root endpoint.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """
    Returns a list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Status endpoint to check if the API is running.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Returns the full object corresponding to the provided username.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handles POST requests to add a new user.
    Validates JSON format, checks for 'username', and prevents duplicates.
    """
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
