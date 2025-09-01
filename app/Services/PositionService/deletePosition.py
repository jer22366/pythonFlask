from app import db
from app.database.table.positions import models
from flask import jsonify

def delete_position_logic(position_id):
    pos = models.Position.query.get_or_404(position_id)
    db.session.delete(pos)
    db.session.commit()
    return jsonify({"message": "Position deleted"})