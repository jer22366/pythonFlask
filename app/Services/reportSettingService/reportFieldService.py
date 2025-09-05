from flask import Blueprint, request, jsonify
from app.database.table.reportSetting.models import db, ReportField

def create_field_logic():
    data = request.get_json()
    field = ReportField(
        template_id=data["template_id"],
        key=data["key"],
        label=data["label"],
        dtype=data.get("dtype", "string"),
        visible=data.get("visible", True),
        sort_order=data.get("sort_order", 0),
    )
    db.session.add(field)
    db.session.commit()
    return jsonify({"message": "ReportField created", "id": field.id}), 201

def list_fields_logic():
    fields = ReportField.query.all()
    return jsonify([{
        "id": f.id,
        "template_id": f.template_id,
        "key": f.key,
        "label": f.label,
        "dtype": f.dtype,
        "visible": f.visible,
        "sort_order": f.sort_order
    } for f in fields]), 200

def get_field_logic(field_id):
    field = ReportField.query.get_or_404(field_id)
    return jsonify({
        "id": field.id,
        "template_id": field.template_id,
        "key": field.key,
        "label": field.label,
        "dtype": field.dtype,
        "visible": field.visible,
        "sort_order": field.sort_order
    }), 200
    
def update_field_logic(field_id):
    field = ReportField.query.get_or_404(field_id)
    data = request.get_json()
    field.key = data.get("key", field.key)
    field.label = data.get("label", field.label)
    field.dtype = data.get("dtype", field.dtype)
    field.visible = data.get("visible", field.visible)
    field.sort_order = data.get("sort_order", field.sort_order)
    db.session.commit()
    return jsonify({"message": "ReportField updated"}), 200

def delete_field_logic(field_id):
    field = ReportField.query.get_or_404(field_id)
    db.session.delete(field)
    db.session.commit()
    return jsonify({"message": "ReportField deleted"}), 200