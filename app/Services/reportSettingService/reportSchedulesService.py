from flask import Blueprint, request, jsonify
from extensions import db
from app.database.table.reportSetting.models import ReportSchedule
from datetime import datetime

def create_schedule_logic():
    data = request.get_json()
    schedule = ReportSchedule(
        template_id=data["template_id"],
        name=data["name"],
        frequency=data.get("frequency"),
        day_of_week=data.get("day_of_week"),
        day_of_month=data.get("day_of_month"),
        time_of_day=data.get("time_of_day"),
        cron=data.get("cron"),
        timezone=data.get("timezone", "UTC"),
        params=data.get("params", {}),
        output_format=data.get("output_format", "xlsx"),
        status=data.get("status", "active"),
        created_by=data.get("created_by"),
        updated_by=data.get("created_by")
    )
    db.session.add(schedule)
    db.session.commit()
    return jsonify({"message": "ReportSchedule created", "id": schedule.id}), 201
def list_schedules_logic():
    schedules = ReportSchedule.query.all()
    return jsonify([{
        "id": s.id,
        "template_id": s.template_id,
        "name": s.name,
        "frequency": s.frequency,
        "status": s.status,
        "next_run_at": s.next_run_at.isoformat() if s.next_run_at else None
    } for s in schedules]), 200
    
def get_schedule_logic(schedule_id):
    s = ReportSchedule.query.get_or_404(schedule_id)
    return jsonify({
        "id": s.id,
        "template_id": s.template_id,
        "name": s.name,
        "frequency": s.frequency,
        "day_of_week": s.day_of_week,
        "day_of_month": s.day_of_month,
        "time_of_day": s.time_of_day,
        "cron": s.cron,
        "timezone": s.timezone,
        "params": s.params,
        "output_format": s.output_format,
        "status": s.status,
        "last_run_at": s.last_run_at.isoformat() if s.last_run_at else None,
        "next_run_at": s.next_run_at.isoformat() if s.next_run_at else None
    }), 200
    
def update_schedule_logic(schedule_id):    
    s = ReportSchedule.query.get_or_404(schedule_id)
    data = request.get_json()
    for key in ["name", "frequency", "day_of_week", "day_of_month", "time_of_day",
                "cron", "timezone", "params", "output_format", "status", "updated_by"]:
        if key in data:
            setattr(s, key, data[key])
    s.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify({"message": "ReportSchedule updated"}), 200

def delete_schedule_logic(schedule_id):
    s = ReportSchedule.query.get_or_404(schedule_id)
    db.session.delete(s)
    db.session.commit()
    return jsonify({"message": "ReportSchedule deleted"}), 200