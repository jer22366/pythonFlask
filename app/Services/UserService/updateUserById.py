from flask import Flask, request, jsonify
from app.database.table.users.models import db, User

def update_user_by_id_logic(id):
    user = User.query.get_or_404(id)
    data = request.get_json()

    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.birthday = data.get('birthday') or None
    user.phone = data.get('phone')
    user.address = data.get('address')

    db.session.commit()

    return jsonify({'success': True})