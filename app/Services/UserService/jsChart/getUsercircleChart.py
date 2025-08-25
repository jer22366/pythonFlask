from flask import Flask, jsonify
from datetime import datetime, timedelta
from app.database.table.userActiveLog.models import db, UserActiveLog

def get_circle_chart_logic():
    # 取得過去 7 天日期
    today = datetime.now().date()
    labels = [(today - timedelta(days=i)).isoformat() for i in reversed(range(7))]

    # 查詢各日期登入數
    login_counts = []
    for date in labels:
        count = UserActiveLog.query.filter(
            db.func.date(UserActiveLog.created_at) == date
        ).count()
        login_counts.append(count)

    return jsonify({
        "labels": labels,
        "values": login_counts
    })