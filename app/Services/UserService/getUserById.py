from flask import Flask, request, jsonify
from app.database.table.users.models import User

def get_user_by_id_logic(id):
    user = User.query.get(id)
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'birthday': user.birthday.isoformat() if user.birthday else None,
            'phone': user.phone,
            'address': user.address
        })
    return jsonify({'error': 'User not found'}), 404