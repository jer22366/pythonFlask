from flask import Blueprint, request, jsonify
from app import db
from app.database.table.department import models

def delete_department_logic(department_id):
    department = models.Department.query.get_or_404(department_id)
    try:
        db.session.delete(department)
        db.session.commit()
        return jsonify({"message": "部門刪除成功"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400