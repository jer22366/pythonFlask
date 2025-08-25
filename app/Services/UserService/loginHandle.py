from flask import Flask, request, jsonify, make_response
from app.database.table.users.models import User
from app.database.table.loginLog.models import loginLog, db
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

    log = loginLog(user_id=user.id, ip=ip, user_agent=user_agent)
    db.session.add(log)
    db.session.commit()

    # 檢查 level 權限
    if user.level.name == 'admin':
        dashboard_url = '/pages/dashboard'
    else:
        dashboard_url = '/payment'

    token = jwt.encode(
        {"user_id": user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)},
        "你的JWT_SECRET",
        algorithm="HS256"
    )

    resp = make_response(jsonify({
        "status": "success",
        "dashboard_url": dashboard_url
    }))
    resp.set_cookie("jwt", token, httponly=True, samesite="Lax")
    return resp

def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
    else:
        ip = request.remote_addr
    return ip
