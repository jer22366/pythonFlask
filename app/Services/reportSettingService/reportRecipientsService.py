from flask import Blueprint, request, jsonify
from app.database.table.reportSetting import models
from extensions import db

def create_recipient_logic():
    data = request.get_json()
    r = models.ReportRecipient(
        schedule_id=data["schedule_id"],
        channel=data.get("channel", "in_app"),
        email=data.get("email"),
        user_id=data.get("user_id")
    )
    db.session.add(r)
    db.session.commit()
    return jsonify({"message": "ReportRecipient created", "id": r.id}), 201

def list_recipients_logic():
    recipients = models.ReportRecipient.query.all()
    return jsonify([{
        "id": r.id,
        "schedule_id": r.schedule_id,
        "channel": r.channel,
        "email": r.email,
        "user_id": r.user_id
    } for r in recipients]), 200

def update_recipient_logic(recipient_id):
    r = models.ReportRecipient.query.get_or_404(recipient_id)
    data = request.get_json()
    r.channel = data.get("channel", r.channel)
    r.email = data.get("email", r.email)
    r.user_id = data.get("user_id", r.user_id)
    db.session.commit()
    return jsonify({"message": "ReportRecipient updated"}), 200

def delete_recipient_logic(recipient_id):
    r = models.ReportRecipient.query.get_or_404(recipient_id)
    db.session.delete(r)
    db.session.commit()
    return jsonify({"message": "ReportRecipient deleted"}), 200