from flask import Flask, request, jsonify
from app.database.table.users.models import db, User
from werkzeug.security import generate_password_hash

def reset_password_logic(id):
    user = User.query.get_or_404(id)
    data = request.get_json()

    user.password = generate_password_hash(data.get('password', user.password))
    db.session.commit()
    return jsonify({"status": "success", "message": "密碼重置成功"}), 200