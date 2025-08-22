from flask import Flask, redirect, Blueprint
from app.Services.UserService.loginHandle import loginLogic 
from app.Services.UserService.registerHandler import registerLogic
from app.Services.UserService.getUserById import get_user_by_id_logic
from app.Services.UserService.getUser import get_user_logic
from app.Services.UserService.getDeleteUser import get_deleted_user_logic
from app.Services.UserService.restoreUser import restore_user_logic
from app.Services.UserService.updateUserById import update_user_by_id_logic
from app.Services.UserService.getUserChart import get_user_chart_logic
from app.Services.UserService.isActive import is_active_logic
from app.Services.UserService.deleteUser import delete_user_logic
from app.Services.UserService.resetPassword import reset_password_logic
# from app.Services.UserService.ecPay import ecpay_logic
# from app.Services.UserService.ecPayNotify import ecpay_notify_logic
from app.database.table.users.models import db, User
from flask_migrate import Migrate
from datetime import datetime, date
import requests 

user_bp = Blueprint('user', __name__, url_prefix='/api/user')
# with main_bp.app_context():
#     try:
#         with db.engine.connect() as conn:
#             result = conn.execute(text("SELECT 1"))
#             print("✅ 資料庫連線成功，結果：", result.scalar())  # 通常會印出 1
#     except Exception as e:
#         print("❌ 資料庫連線失敗：", e)

@user_bp.route("/create-user")
def create_user():
    try:
        url = "https://randomuser.me/api/"
        response = requests.get(url)
        if response.status_code != 200:
            return f"❌ 無法取得隨機使用者資料，狀態碼：{response.status_code}"

        data = response.json()
        user_data = data['results'][0]

        birthday_str = user_data['dob']['date']
        if birthday_str.endswith('Z'):
            birthday_str = birthday_str[:-1]

        new_user = User(
            username=user_data['name']['first'] + " " + user_data['name']['last'],
            email=user_data['email'],
            password=user_data['login']['password'],
            birthday=datetime.fromisoformat(birthday_str).date(),
            address=str(user_data['location']['street']['number']) + " " + user_data['location']['street']['name'],
            phone=user_data['phone']
        )
        db.session.add(new_user)
        db.session.commit()
        return "✅ 使用者新增成功"

    except Exception as e:
        db.session.rollback()
        return f"❌ 發生錯誤: {e}"

    finally:
        db.session.close()

@user_bp.route("/login", methods=["POST"])
def login_handler():
    return loginLogic()

@user_bp.route("/register", methods=["POST"])
def register_handler():
    return registerLogic()

@user_bp.route("/getUser", methods=["GET"])
def get_user():
 return get_user_logic()

@user_bp.route("/getUser/<int:id>", methods=["GET"])
def get_user_by_id(id):  
    return get_user_by_id_logic(id)

@user_bp.route("/getDeletedUser", methods=["GET"])
def get_deleted_user():
    return get_deleted_user_logic()

@user_bp.route('/restore/<int:id>', methods=['PUT'])
def restore_user(id):
    return restore_user_logic(id)

@user_bp.route('/update/<int:id>', methods=['POST'])
def update_user_by_id(id):
    return update_user_by_id_logic(id)

@user_bp.route('/delete/<int:id>',methods=['DELETE'])
def delete_user(id):
    return delete_user_logic(id)


@user_bp.route('/resetPassword/<int:id>',methods=['PUT'])
def reset_password(id):
    return reset_password_logic(id)

@user_bp.route('/isActive/<int:id>',methods=['PUT'])
def is_active(id):
    return is_active_logic(id)

@user_bp.route('/getUserChart', methods=['GET'])
def get_user_chart():
    return get_user_chart_logic()

# @main_bp.route("/api/ecPay", methods=["POST"])
# def ecPay():
#     return ecpay_logic()


# @main_bp.route("/api/server/paySuccessful", methods=["GET"])
# def ecpay_notify():
#    return ecpay_notify_logic()
