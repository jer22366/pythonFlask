from flask import request, jsonify
from app.database.table.users.models import User
from app.database.table.userActiveLog.models import UserActiveLog, db
from app.config import Config
import jwt
import datetime

def logoutLogic():
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"message": "Missing token", "status": "error"}), 401

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired", "status": "error"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token", "status": "error"}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found", "status": "error"}), 404

    # 紀錄登出事件
    ip = get_client_ip()
    user_agent = request.headers.get('User-Agent')

    log = UserActiveLog(
        user_id=user.id,
        ip=ip,
        user_agent=user_agent,
        action='logout',
    )
    db.session.add(log)
    db.session.commit()

    return jsonify({"message": "Logout successful", "status": "success"}), 200


def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
    else:
        ip = request.remote_addr
    return ip
