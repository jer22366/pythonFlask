from flask import Blueprint
from app.Services.BonusesService.bonuseService import (
    add_bonus_logic,
    get_bonus_logic,
    update_bonus_logic,
    delete_bonus_logic
    )
bonuses_bp = Blueprint('bonuses', __name__, url_prefix='/api/bonuses')

@bonuses_bp.route('/create', methods=['POST'])
def add_bonus():
    return add_bonus_logic()
    

# 查詢獎金
@bonuses_bp.route('/getBonuses', methods=['GET'])
def get_bonus():
    return get_bonus_logic()
   
# 修改獎金
@bonuses_bp.route('/update/<int:id>', methods=['PUT'])
def update_bonus(id):
    return update_bonus_logic(id)
    
# 刪除獎金
@bonuses_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_bonus(id):
    return delete_bonus_logic(id)
    
