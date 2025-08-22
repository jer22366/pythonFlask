from flask import Flask, redirect, Blueprint

organ_bp = Blueprint('organization', __name__, url_prefix='/api/organization')

@organ_bp.route('/create', methods=['POST'])
def create_organization():
    # 這裡是創建組織的邏輯
    pass

@organ_bp.route('/getOrgan', methods=['GET'])
def get_organization():
    # 這裡是獲取組織的邏輯
    pass

@organ_bp.route('/getOrgan/<int:id>', methods=['GET'])
def get_organization(id):
    # 這裡是獲取組織的邏輯
    pass

@organ_bp.route('/update/<int:id>', methods=['PUT'])
def update_organization(id):
    # 這裡是更新組織的邏輯
    pass

@organ_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_organization(id):
    # 這裡是刪除組織的邏輯
    pass
