from flask import Flask, request, jsonify, Blueprint
from app.Services.PayRollsService.payRollsService import (
    add_payroll_logic,
    get_payrolls_logic,
    update_payroll_logic,
    delete_payroll_logic
)

payRolls_bp = Blueprint('payRolls', __name__, url_prefix='/api/payRolls')

@payRolls_bp.route('/create', methods=['POST'])
def add_payroll():
    return add_payroll_logic()

# 4️⃣ 查詢薪資紀錄
@payRolls_bp.route('/getPayRolls', methods=['GET'])
def get_payrolls():
    return get_payrolls_logic()
    

# 5️⃣ 修改薪資紀錄
@payRolls_bp.route('/update/<int:id>', methods=['PUT'])
def update_payroll(id):
    return update_payroll_logic(id)
    

# 6️⃣ 刪除薪資紀錄
@payRolls_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_payroll(id):
    return delete_payroll_logic(id)