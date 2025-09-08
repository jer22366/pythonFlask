from app.database.table.positions import models
from flask import jsonify

def get_position_by_id_logic(position_id):
    positions = models.Position.query.filter_by(department_id=position_id, status="active").all()
    return jsonify([p.to_dict() for p in positions])  