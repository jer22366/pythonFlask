from flask import request, jsonify
from app import db
from app.database.table.leaveType.models import LeaveType

def get_leave_type_logic():
    leave_types = LeaveType.query.all()
    return jsonify([leave.to_dict() for leave in leave_types]), 200
