from flask import Blueprint
from app.Services.DeductionService.DeductionService import (
    add_deduction_logic,
    get_deductions_logic,
    update_deduction_logic,
    delete_deduction_logic
)

deductions_bp = Blueprint('deductions', __name__, url_prefix='/api/deductions')

@deductions_bp.route('/create', methods=['POST'])
def add_deduction():
    return add_deduction_logic()

# 查詢扣款
@deductions_bp.route('/deductions', methods=['GET'])
def get_deductions():
    return get_deductions_logic()
    

# 修改扣款
@deductions_bp.route('/deductions/<int:id>', methods=['PUT'])
def update_deduction(id):
    return update_deduction_logic(id)

# 刪除扣款
@deductions_bp.route('/deductions/<int:id>', methods=['DELETE'])
def delete_deduction(id):
    return delete_deduction_logic(id)