from app import db
from app.database.table.positions import models
from flask import jsonify, request

def create_position_logic():
        data = request.get_json()
        pos = models.Position(
            name=data.get("name"),
            code=data.get("code"),
            level=data.get("level", 1),
            department_id=data.get("department_id"),
            status=data.get("status", "active")
        )
        db.session.add(pos)
        db.session.commit()
        return jsonify({"status": "success", "data": pos.to_dict()}), 201
