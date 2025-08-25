from flask import Flask, request, jsonify
from app.database.table.users.models import db, User
from sqlalchemy import func, extract

def get_user_chart_logic():
    # 查詢每個月會員數量
    results = db.session.query(
        extract('month', User.created_at).label('month'),
        func.count(User.id).label('count')
    ).group_by('month').order_by('month').all()

    # 轉成 labels 和 values
    month_map = {1:"1月", 2:"2月", 3:"3月", 4:"4月", 5:"5月", 6:"6月",
                 7:"7月", 8:"8月", 9:"9月", 10:"10月", 11:"11月", 12:"12月"}

    labels = []
    values = []
    for month, count in results:
        labels.append(month_map[int(month)])
        values.append(count)

    return jsonify({
        "labels": labels,
        "values": values
    })
