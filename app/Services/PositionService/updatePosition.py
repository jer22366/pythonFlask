from app import db
from app.database.table.positions import models
from flask import jsonify,request

def update_position_logic(position_id):
        data = request.get_json()
        pos = models.Position.query.get_or_404(position_id)
        if "name" in data: pos.name = data["name"]
        if "code" in data: pos.code = data["code"]
        if "level" in data: pos.level = data["level"]
        if "department_id" in data: pos.department_id = data["department_id"]
        if "status" in data: pos.status = data["status"]
        db.session.commit()
        return jsonify({"message": "Position updated"})