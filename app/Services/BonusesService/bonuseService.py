from flask import request, jsonify
from app import db
from app.database.table.employeePayroll.models import Bonus

def add_bonus_logic():
    data = request.json
    bonus = Bonus(
        payroll_id=data['payroll_id'],
        type=data['type'],
        amount=data['amount']
    )
    db.session.add(bonus)
    db.session.commit()
    return jsonify({"status": "success", "message": "Bonus created", "data": bonus}), 201

def get_bonus_logic():
    bonuses = Bonus.query.all()
    result = []
    for b in bonuses:
        result.append({
            "id": b.id,
            "payroll_id": b.payroll_id,
            "type": b.type,
            "amount": b.amount
        })
    return jsonify(result)

def update_bonus_logic(id):
    data = request.json
    bonus = Bonus.query.get_or_404(id)
    bonus.type = data.get('type', bonus.type)
    bonus.amount = data.get('amount', bonus.amount)
    db.session.commit()
    return jsonify({"status": "success", "message": "Bonus updated", "data": bonus}), 200

def delete_bonus_logic(id):
    bonus = Bonus.query.get_or_404(id)
    db.session.delete(bonus)
    db.session.commit()
    return jsonify({"status": "success", "message": "Bonus deleted"}), 200