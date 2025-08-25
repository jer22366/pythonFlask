from flask import Blueprint, jsonify
from app.database.table.users.models import db, User
from sqlalchemy import func

def get_role_distribution_logic():
   # 查詢 DB，計算每個 level 數量
    results = (
        db.session.query(User.level, func.count(User.id))
        .group_by(User.level)
        .all()
    )

    # 轉換成 dict
    role_map = {level.value: count for level, count in results}  # level.value 因為是 Enum

    # 固定順序
    roles = ["admin", "manage", "finance", "HR", "staff"]
    values = [role_map.get(r, 0) for r in roles]

    return jsonify({
        "labels": roles,
        "values": values
    })