from flask import jsonify
from datetime import datetime
from app.database.table.users.models import db, User

def get_user_stats_logic():
    try:
        # 總用戶數
        total_users = db.session.query(User).count()

        # 取得指定用戶的 level
        user = db.session.query(User).filter(User.id == id).first()
        if not user:
            user_level = None
        elif hasattr(user.level, "name"):  # Enum
            user_level = user.level.name
        else:  # String or int
            user_level = str(user.level)

        # 今天新增用戶數
        today = datetime.utcnow().date()
        new_users_today = db.session.query(User).filter(
            db.func.date(User.created_at) == today
        ).count()

        stats = {
            "total_users": total_users,
            "new_users_today": new_users_today,
            "revenue": 48000,
            "pending_tasks": 7,
            "attendance_rate": "92%",
            "server_health": "正常",
            "level": user_level,
        }

        return jsonify(stats)

    except Exception as e:
        import traceback
        print("❌ get_user_stats_logic error:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
