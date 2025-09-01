from app import db
from app.database.table.positions import models
from flask import jsonify

def get_position_logic():
        positions = models.Position.query.all()
        result = [models.Position.to_dict(p) for p in positions]
        return jsonify(result)