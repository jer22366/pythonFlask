from flask import Blueprint
from app.Services.AllowanceService.allowanceService import (
    add_allowance_logic,
    get_allowances_logic,
    update_allowance_logic,
    delete_allowance_logic
    )
allowance_bp = Blueprint('allowance', __name__, url_prefix='/api/allowance')

@allowance_bp.route('/create', methods=['POST'])
def add_allowance():
    return add_allowance_logic()

# 查詢津貼
@allowance_bp.route('/getAllowances', methods=['GET'])
def get_allowances():
    return get_allowances_logic()
    

# 修改津貼
@allowance_bp.route('/update/<int:id>', methods=['PUT'])
def update_allowance(id):
    return update_allowance_logic(id)

# 刪除津貼
@allowance_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_allowance(id):
    return delete_allowance_logic(id)