 
from flask import request, jsonify
from app.database.table.reportSetting.models import ReportExportLog
from datetime import datetime
from extensions import db

def create_log_logic():
    data = request.get_json()
    log = ReportExportLog(
        template_id=data.get("template_id"),
        schedule_id=data.get("schedule_id"),
        run_by=data.get("run_by"),
        params=data.get("params", {}),
        output_format=data["output_format"],
        status=data.get("status", "queued"),
        file_path=data.get("file_path"),
        error_message=data.get("error_message"),
        started_at=datetime.utcnow()
    )
    db.session.add(log)
    db.session.commit()
    return jsonify({"message": "ReportExportLog created", "id": log.id}), 201

def list_logs_logic():
    logs = ReportExportLog.query.order_by(ReportExportLog.started_at.desc()).all()
    return jsonify([{
        "id": l.id,
        "template_id": l.template_id,
        "schedule_id": l.schedule_id,
        "status": l.status,
        "file_path": l.file_path,
        "started_at": l.started_at.isoformat(),
        "finished_at": l.finished_at.isoformat() if l.finished_at else None
    } for l in logs]), 200

def update_log_logic(log_id):
    log = ReportExportLog.query.get_or_404(log_id)
    data = request.get_json()
    log.status = data.get("status", log.status)
    log.file_path = data.get("file_path", log.file_path)
    log.error_message = data.get("error_message", log.error_message)
    if "finished" in log.status and not log.finished_at:
        log.finished_at = datetime.utcnow()
    db.session.commit()
    return jsonify({"message": "ReportExportLog updated"}), 200

def delete_log_logic(log_id):
    log = ReportExportLog.query.get_or_404(log_id)
    db.session.delete(log)
    db.session.commit()
    return jsonify({"message": "ReportExportLog deleted"}), 200

