from flask import request, jsonify
from app import db
from app.database.table.department.models import Department

def update_department_logic(department_id):
    department = Department.query.get_or_404(department_id)
    data = request.get_json() or {}

    # 允許更新的欄位清單
    updatable_fields = [
        "name", "code", "parent_id", "level",
        "manager_id", "description", "is_active"
    ]

    # 動態更新欄位
    for field in updatable_fields:
        if field in data:
            setattr(department, field, data[field])

    try:
        db.session.commit()
        return jsonify({"status": "success", "message": "部門更新成功", "department": department.id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}), 400
