from flask import request, jsonify, Blueprint
from app.database.table.employeePayroll.models import db, Employee
from app.Services.EmployeesService.EmployeesService import (
    add_employee_logic, 
    list_employees_logic,
    update_employee_logic,
    delete_employee_logic
)

employees_bp = Blueprint('employees', __name__, url_prefix='/api/employees')

@employees_bp.route('/create', methods=['POST'])
def add_employee():
    return add_employee_logic()


@employees_bp.route('/getEmployees', methods=['GET'])
def get_employees():
    return list_employees_logic()
   

@employees_bp.route('/update/<int:id>', methods=['PUT'])
def update_employee(id):
    return update_employee_logic(id)
    

@employees_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_employee(id):
    return delete_employee_logic(id)