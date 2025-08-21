from flask import Flask, render_template
from datetime import datetime
from app.database.table.users.models import db, User
from sqlalchemy import extract
def dashboard_logic():
     # KPI
    total_users = User.query.filter_by(deleted_at=None).count()
    new_users_today = User.query.filter(
        User.deleted_at == None,
        db.func.date(User.created_at) == datetime.today().date()
    ).count()

    stats = {
        "total_users": total_users,
        "new_users_today": new_users_today,
        "revenue": 12000,
        "pending_tasks": 8
    }

    # 每月用戶成長
    monthly_users = []
    for month in range(1, 13):
        count = User.query.filter(
            User.deleted_at == None,
            extract('month', User.created_at) == month
        ).count()
        monthly_users.append(count)

    # 用戶來源比例（模擬資料）
    user_sources = {"網站": 60, "社群": 30, "廣告": 10}

    return render_template('dashboard.html',
                           stats=stats,
                           monthly_users=monthly_users,
                           user_sources=user_sources)