from flask import request, jsonify
from app import db
from app.database.table.leaveType.models import LeaveType

def get_leave_type_by_id_logic(id):
    leave_type = LeaveType.query.get(id)
    if not leave_type:
        return jsonify({"message": "Leave type not found"}), 404
    return jsonify(leave_type.to_dict()), 200