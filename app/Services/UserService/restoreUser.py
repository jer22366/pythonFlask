from flask import jsonify
from app.database.table.users.models import User,db

def restore_user_logic(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({"error": "用戶不存在或已復原"}), 404

    user.deleted_at = None
    db.session.commit()
    return jsonify({"status": "success",
                    "message": f"用戶 {user.username} 已復原"}), 200
