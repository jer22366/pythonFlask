from flask import jsonify
from app.database.table.users.models import User,db

def is_active_logic(user_id):
    user = User.query.get_or_404(user_id)
    user.is_active = not user.is_active
    db.session.commit()
    return jsonify({"status": "success", "is_active": user.is_active})