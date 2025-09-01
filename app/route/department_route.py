from flask import Flask, redirect, Blueprint
from app.Services.DepartmentService.createDepartment import create_department_logic
from app.Services.DepartmentService.getDepartment import get_department_logic
from app.Services.DepartmentService.getDepartmentById import get_department_by_id_logic
from app.Services.DepartmentService.updateDepartment import update_department_logic
from app.Services.DepartmentService.deleteDepartment import delete_department_logic
organ_bp = Blueprint('department', __name__, url_prefix='/api/department')

@organ_bp.route('/create', methods=['POST'])
def create_department():
   return create_department_logic()

@organ_bp.route('/getDepartment', methods=['GET'])
def get_department():
   return get_department_logic()

@organ_bp.route('/getDepartment/<int:id>', methods=['GET'])
def get_department_id(id):
   return get_department_by_id_logic(id)

@organ_bp.route('/update/<int:id>', methods=['PUT'])
def update_department(id):
   return update_department_logic(id)

@organ_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_department(id):
   return delete_department_logic(id)


