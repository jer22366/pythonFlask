from flask import Flask, redirect, Blueprint
from app.Services.PositionService.createPosition import create_position_logic
from app.Services.PositionService.getPosition import get_position_logic
from app.Services.PositionService.getPositionById import get_position_by_id_logic
from app.Services.PositionService.updatePosition import update_position_logic
from app.Services.PositionService.deletePosition import delete_position_logic
position_bp = Blueprint('position', __name__, url_prefix='/api/position')

@position_bp.route('/create', methods=['POST'])
def create_position():
   return create_position_logic()

@position_bp.route('/getPosition', methods=['GET'])
def get_position():
   return get_position_logic()

@position_bp.route('/getPosition/<int:id>', methods=['GET'])
def get_position_id(id):
   return get_position_by_id_logic(id)

@position_bp.route('/update/<int:id>', methods=['PUT'])
def update_position(id):
   return update_position_logic(id)

@position_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_position(id):
   return delete_position_logic(id)


