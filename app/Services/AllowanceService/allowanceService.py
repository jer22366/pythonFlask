from flask import Blueprint, request, jsonify
from app import db
from app.database.table.employeePayroll.models import Allowance

def add_allowance_logic():
    data = request.json
    allowance = Allowance(
        payroll_id=data['payroll_id'],
        type=data['type'],
        amount=data['amount']
    )
    db.session.add(allowance)
    db.session.commit()
    return jsonify({"status": "success", "message": "Allowance created", "data": allowance}), 201

def get_allowances_logic():
    allowances = Allowance.query.all()
    result = []
    for a in allowances:
        result.append({
            "id": a.id,
            "payroll_id": a.payroll_id,
            "type": a.type,
            "amount": a.amount
        })
    return jsonify(result)

def update_allowance_logic(id):
    data = request.json
    allowance = Allowance.query.get_or_404(id)
    allowance.type = data.get('type', allowance.type)
    allowance.amount = data.get('amount', allowance.amount)
    db.session.commit()
    return jsonify({"status": "success", "message": "Allowance updated", "data": allowance}), 200


def delete_allowance_logic(id):
    allowance = Allowance.query.get_or_404(id)
    db.session.delete(allowance)
    db.session.commit()
    return jsonify({"status": "success", "message": "Allowance deleted"}), 200