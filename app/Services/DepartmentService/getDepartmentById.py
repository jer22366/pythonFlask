from flask import Blueprint, request, jsonify
from app import db
from app.database.table.department import models

def get_department_by_id_logic(department_id):
    department = models.Department.query.get_or_404(department_id)
    return jsonify({
        "id": department.id,
        "name": department.name,
        "code": department.code,
        "parent_id": department.parent_id,
        "level": department.level,
        "manager_id": department.manager_id,
        "description": department.description,
        "is_active": department.is_active,
    })