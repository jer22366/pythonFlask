from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from app.database.table.users.models import db, User
def registerLogic():
    if request.method == "POST":
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        if not username or not password or not email:
            return jsonify({"status": False, "message": "Missing fields"}), 400

        # Here you would typically add the user to the database
        new_user = User(
            username=username,
            password=generate_password_hash(password),
            email=email
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"status": 'success', "message": "User registered successfully"}), 201

    return jsonify({"status": 'error', "message": "Invalid request method"}), 405