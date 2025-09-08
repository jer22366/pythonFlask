from flask import request, jsonify
from app import db
from app.database.table.leaveType.models import LeaveType

def delete_leave_type_logic(id):
    leave_type = LeaveType.query.get(id)
    if not leave_type:
        return jsonify({"message": "Leave type not found"}), 404
    db.session.delete(leave_type)
    db.session.commit()
    return jsonify({"status": "success"}), 200
