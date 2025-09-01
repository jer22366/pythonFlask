from flask import Flask, request, jsonify
from app.database.table.users.models import User
from app.database.table.userActiveLog.models import UserActiveLog, db
from werkzeug.security import check_password_hash
import jwt
import datetime
from app.config import Config 

def loginLogic():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found", "status": "error"}), 404

    if not check_password_hash(user.password, password):
        return jsonify({"message": "Incorrect password", "status": "error"}), 401

    # 登入成功 → 紀錄登入紀錄
    ip = get_client_ip()
    user_agent = request.headers.get('User-Agent')

    log = UserActiveLog(user_id=user.id, ip=ip, user_agent=user_agent, action='login')
    db.session.add(log)
    db.session.commit()

    # ✅ 產生 JWT token
    token_payload = {
        "user_id": user.id,
        "username": user.username,
        "level": user.level.name,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)  # 2 小時過期
    }
    token = jwt.encode(token_payload, Config.SECRET_KEY, algorithm="HS256")

    return jsonify({
        "message": "Login successful",
        "status": "success",
        "dashboard_url": "/pages/dashboard",
        "user_level": user.level.name,
        "ip": ip,
        "token": token  # 回傳 JWT
    }), 200


def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
    else:
        ip = request.remote_addr
    return ip
