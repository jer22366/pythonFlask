from flask import request, jsonify
from app import db
from app.database.table.employeePayroll.models import Deduction
def add_deduction_logic():
    data = request.json
    deduction = Deduction(
        payroll_id=data['payroll_id'],
        type=data['type'],
        amount=data['amount']
    )
    db.session.add(deduction)
    db.session.commit()
    return jsonify({"message": "Deduction created", "id": deduction.id})

def get_deductions_logic():
    deductions = Deduction.query.all()
    result = []
    for d in deductions:
        result.append({
            "id": d.id,
            "payroll_id": d.payroll_id,
            "type": d.type,
            "amount": d.amount
        })
    return jsonify(result)

def update_deduction_logic(id):
    data = request.json
    deduction = Deduction.query.get_or_404(id)
    deduction.type = data.get('type', deduction.type)
    deduction.amount = data.get('amount', deduction.amount)
    db.session.commit()
    return jsonify({"message": "Deduction updated"})

def delete_deduction_logic(id):
    deduction = Deduction.query.get_or_404(id)
    db.session.delete(deduction)
    db.session.commit()
    return jsonify({"message": "Deduction deleted"})