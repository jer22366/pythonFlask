from flask import Blueprint, request, jsonify
from app import db
from datetime import datetime
from app.database.table.employeePayroll.models import Employee

def add_employee_logic():
    data = request.json
    emp = Employee(
        employee_code=data['employee_code'],
        name=data['name'],
        department=data.get('department'),
        position=data.get('position'),
        hire_date=datetime.strptime(data['hire_date'], "%Y-%m-%d")
    )
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "Employee added", "id": emp.id}), 201
    
    
def list_employees_logic():
    employees = Employee.query.all()
    result = []
    for e in employees:
        result.append({
            "id": e.id,
            "employee_code": e.employee_code,
            "name": e.name,
            "department": e.department,
            "position": e.position,
            "hire_date": e.hire_date.strftime("%Y-%m-%d")
        })
    return jsonify(result)

def update_employee_logic(id):
    employee = Employee.query.get(id)
    if employee:
        data = request.json
        employee.employee_code = data.get('employee_code', employee.employee_code)
        employee.name = data.get('name', employee.name)
        employee.department = data.get('department', employee.department)
        employee.position = data.get('position', employee.position)
        employee.hire_date = datetime.strptime(data.get('hire_date', employee.hire_date.strftime("%Y-%m-%d")), "%Y-%m-%d")
        db.session.commit()
        return jsonify({"message": "Employee updated"})
    return jsonify({"message": "Employee not found"}), 404

def delete_employee_logic(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({"message": "Employee deleted"})
    return jsonify({"message": "Employee not found"}), 404