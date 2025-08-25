from flask import jsonify
from app.database.table.users.models import db, User

def get_user_stats_logic():
    total_users = db.session.query(User).count()  # 計算所有用戶數量

    # 取第一個用戶的 level 並轉成字串
    first_user = db.session.query(User.level).first()
    user_level = str(first_user[0]) if first_user else None  # Enum -> str
    
    user_level = user_level.split('.')[-1] if user_level else None

    stats = {
        "total_users": total_users,
        "new_users_today": 15,       # 可以再改成實際今天新增用戶
        "revenue": 48000,
        "pending_tasks": 7,
        "attendance_rate": "92%",
        "server_health": "正常",
        "level": user_level
    }

    return jsonify(stats)
