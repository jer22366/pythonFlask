from app import db
from app.database.table.positions import models
from flask import jsonify

def get_position_by_id_logic(self, position_id):
    pos = models.Position.query.get_or_404(position_id)
    return jsonify(models.Position.to_dict(pos))