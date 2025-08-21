from flask import Flask, request, jsonify
from app.database.table.users.models import db, User

def delete_user_logic(user_id):
    user = User.query.filter_by(id=user_id, deleted_at=None).first()
    if not user:
        return jsonify({"error": "用戶不存在或已刪除"}), 404

    user.soft_delete()
    db.session.commit()
    return jsonify({"status": "success",
                    "message": f"用戶 {user.username} 已軟刪除"}), 200

