#!/usr/bin/env python3
"""
5. API Security and Authentication Techniques
"""
from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'
auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verifies the password for Basic Auth"""
    if username in users and \
            check_password_hash(users[username]['password'], password):
        return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Route protected by Basic Auth"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login route to generate JWT token"""
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 401

    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)
    return jsonify({"message": "Bad username or password"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Route protected by JWT"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Route accessible only by admins"""
    claims = get_jwt()
    if claims.get('role') != 'admin':
        abort(403)
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing Authorization header"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle needs fresh token"""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
