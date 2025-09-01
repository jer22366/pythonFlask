from flask import Blueprint, request, jsonify
from app import db
from app.database.table.department import models

def get_department_logic():
    departments = models.Department.query.all()
    result = [
        {
            "id": d.id,
            "name": d.name,
            "code": d.code,
            "parent_id": d.parent_id,
            "level": d.level,
            "manager_id": d.manager_id,
            "description": d.description,
            "is_active": d.is_active,
        }
        for d in departments
    ]
    return jsonify(result)