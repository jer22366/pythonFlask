from flask import Blueprint, jsonify
from app.database.table.users.models import db, User

def get_user_stats_logic():
    total_users = db.session.query(User).count()  # 計算所有用戶數量

    # 其他 KPI 假資料仍然保留
    stats = {
        "total_users": total_users,
        "new_users_today": 15,       # 可以再改成實際今天新增用戶
        "revenue": 48000,
        "pending_tasks": 7,
        "attendance_rate": "92%",
        "server_health": "正常"
    }

    return jsonify(stats)