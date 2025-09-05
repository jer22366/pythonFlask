from flask import request, jsonify
from app import db
from app.database.table.leaveType.models import LeaveType

def update_leave_type_logic(id):
    leave = LeaveType.query.get_or_404(id)
    data = request.json
    leave.name = data.get("name", leave.name)
    leave.is_paid = data.get("is_paid", leave.is_paid)
    leave.max_days_per_year = data.get("max_days_per_year", leave.max_days_per_year)
    leave.unit = data.get("unit", leave.unit)
    db.session.commit()
    return jsonify(leave.to_dict())