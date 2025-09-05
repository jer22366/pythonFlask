from flask import request, jsonify
from app.database.table.employeePayroll.models import Payroll, db
from datetime import datetime

def add_payroll_logic():
    data = request.json
    payroll = Payroll(
        employee_id=data['employee_id'],
        month=datetime.strptime(data['month'], "%Y-%m-%d"),
        base_salary=data.get('base_salary', 0.0),
        total_allowance=data.get('total_allowance', 0.0),
        total_bonus=data.get('total_bonus', 0.0),
        total_deduction=data.get('total_deduction', 0.0),
    )
    # 計算淨薪資
    payroll.net_salary = payroll.base_salary + payroll.total_allowance + payroll.total_bonus - payroll.total_deduction
    db.session.add(payroll)
    db.session.commit()
    return jsonify({"message": "Payroll created", "id": payroll.id})

def get_payrolls_logic():
    payrolls = Payroll.query.all()
    result = []
    for p in payrolls:
        result.append({
            "id": p.id,
            "employee_id": p.employee_id,
            "month": p.month.strftime("%Y-%m-%d"),
            "base_salary": p.base_salary,
            "total_allowance": p.total_allowance,
            "total_bonus": p.total_bonus,
            "total_deduction": p.total_deduction,
            "net_salary": p.net_salary
        })
    return jsonify(result)

def update_payroll_logic(id):
    data = request.json
    payroll = Payroll.query.get_or_404(id)
    payroll.base_salary = data.get('base_salary', payroll.base_salary)
    payroll.total_allowance = data.get('total_allowance', payroll.total_allowance)
    payroll.total_bonus = data.get('total_bonus', payroll.total_bonus)
    payroll.total_deduction = data.get('total_deduction', payroll.total_deduction)
    payroll.net_salary = payroll.base_salary + payroll.total_allowance + payroll.total_bonus - payroll.total_deduction
    db.session.commit()
    return jsonify({"message": "Payroll updated"})


def delete_payroll_logic(id):
    payroll = Payroll.query.get_or_404(id)
    db.session.delete(payroll)
    db.session.commit()
    return jsonify({"message": "Payroll deleted"})