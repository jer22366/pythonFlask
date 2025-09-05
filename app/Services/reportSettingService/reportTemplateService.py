from flask import Blueprint, request, jsonify
from app.database.table.reportSetting.models import db, ReportTemplate
from datetime import datetime

def create_template_logic():
    data = request.get_json()
    template = ReportTemplate(
        code=data.get("code"),
        name=data.get("name"),
        description=data.get("description"),
        query_engine=data.get("query_engine", "sql"),
        sql_text=data.get("sql_text"),
        handler_name=data.get("handler_name"),
        default_params=data.get("default_params", {}),
        default_format=data.get("default_format", "xlsx"),
        is_active=data.get("is_active", True),
        created_by=data.get("created_by"),
        updated_by=data.get("created_by")
    )
    db.session.add(template)
    db.session.commit()
    return jsonify({"message": "ReportTemplate created", "id": template.id}), 201

def list_templates_logic():
    templates = ReportTemplate.query.all()
    result = []
    for t in templates:
        result.append({
            "id": t.id,
            "code": t.code,
            "name": t.name,
            "description": t.description,
            "query_engine": t.query_engine,
            "is_active": t.is_active,
            "default_format": t.default_format,
            "created_at": t.created_at.isoformat()
        })
    return jsonify(result), 200

def get_template_logic(template_id):
    template = ReportTemplate.query.get_or_404(template_id)
    return jsonify({
        "id": template.id,
        "code": template.code,
        "name": template.name,
        "description": template.description,
        "query_engine": template.query_engine,
        "sql_text": template.sql_text,
        "handler_name": template.handler_name,
        "default_params": template.default_params,
        "default_format": template.default_format,
        "is_active": template.is_active,
        "created_at": template.created_at.isoformat(),
        "updated_at": template.updated_at.isoformat() if template.updated_at else None
    }), 200

def update_template_logic(template_id): 
    template = ReportTemplate.query.get_or_404(template_id)
    data = request.get_json()

    template.name = data.get("name", template.name)
    template.description = data.get("description", template.description)
    template.query_engine = data.get("query_engine", template.query_engine)
    template.sql_text = data.get("sql_text", template.sql_text)
    template.handler_name = data.get("handler_name", template.handler_name)
    template.default_params = data.get("default_params", template.default_params)
    template.default_format = data.get("default_format", template.default_format)
    template.is_active = data.get("is_active", template.is_active)
    template.updated_by = data.get("updated_by", template.updated_by)
    template.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify({"message": "ReportTemplate updated"}), 200

def delete_template_logic(template_id):
    template = ReportTemplate.query.get_or_404(template_id)
    db.session.delete(template)
    db.session.commit()
    return jsonify({"message": "ReportTemplate deleted"}), 200