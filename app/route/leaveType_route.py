from flask import Blueprint
from app.Services.LeaveTypeService.createLeave import create_leave_type_logic
from app.Services.LeaveTypeService.getLeave import get_leave_type_logic
from app.Services.LeaveTypeService.getLeaveById import get_leave_type_by_id_logic
from app.Services.LeaveTypeService.updateLeave import update_leave_type_logic
from app.Services.LeaveTypeService.deleteLeave import delete_leave_type_logic
leaveType_bp = Blueprint('leaveType', __name__, url_prefix='/api/leaveType')

@leaveType_bp.route('/create', methods=['POST'])
def create_leave_type():
   return create_leave_type_logic()

@leaveType_bp.route('/getLeaveType', methods=['GET'])
def get_leave_type():
   return get_leave_type_logic()

@leaveType_bp.route('/getLeaveType/<int:id>', methods=['GET'])
def get_leave_type_id(id):
   return get_leave_type_by_id_logic(id)

@leaveType_bp.route('/update/<int:id>', methods=['PUT'])
def update_leave_type(id):
   return update_leave_type_logic(id)

@leaveType_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_leave_type(id):
   return delete_leave_type_logic(id)