from flask import request, jsonify
from app import db
from app.database.table.leaveType.models import LeaveType

def create_leave_type_logic():
    data = request.get_json()
    leave = LeaveType(
        name=data.get("name"),
        is_paid=data.get("is_paid", True),
        annual_quota=data.get("annual_quota"),
        description=data.get("description")
    )
    db.session.add(leave)
    db.session.commit()
    return jsonify({"message": "Leave type created", "id": leave.id}), 201