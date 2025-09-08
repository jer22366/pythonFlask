from flask import Blueprint, request, jsonify
from app import db
from app.database.table.department.models import Department

def create_department_logic():
    """
    建立部門 (Department)
    """
    data = request.get_json()

    # 必填欄位檢查
    name = data.get("name")
    if not name:
        return jsonify({"status": "error", "message": "name 欄位必填"}), 400

    # 唯一性檢查
    if Department.query.filter_by(name=name).first():
        return jsonify({"status": "error", "message": "部門名稱已存在"}), 400
    if data.get("code") and Department.query.filter_by(code=data["code"]).first():
        return jsonify({"status": "error", "message": "部門代碼已存在"}), 400

    # 建立部門實例
    department = Department(
        name=name,
        code=data.get("code"),
        parent_id=int(data["parent_id"]) if data.get("parent_id") else None,
        level=int(data.get("level", 1)),
        manager_id=int(data["manager_id"]) if data.get("manager_id") else None,
        description=data.get("description"),
        is_active=bool(data.get("is_active", True))
    )

    db.session.add(department)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "部門建立成功",
        "department": {
            "id": department.id,
            "name": department.name,
            "code": department.code,
            "parent_id": department.parent_id,
            "level": department.level,
            "manager_id": department.manager_id,
            "description": department.description,
            "created_at": department.created_at,
            "updated_at": department.updated_at,
            "is_active": department.is_active
        }
    }), 201
