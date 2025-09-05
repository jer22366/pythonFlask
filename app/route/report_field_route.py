from flask import Blueprint
from app.Services.reportSettingService.reportFieldService import (
    create_field_logic,
    list_fields_logic,
    get_field_logic,
    update_field_logic,
    delete_field_logic
)

field_bp = Blueprint("report_fields", __name__, url_prefix="/api/report-fields")

# Create
@field_bp.route("/create", methods=["POST"])
def create_field():
    return create_field_logic()
    
# Read all
@field_bp.route("/getField", methods=["GET"])
def list_fields():
    return list_fields_logic()

# Read one
@field_bp.route("/getField/<int:field_id>", methods=["GET"])
def get_field(field_id):
    return get_field_logic(field_id)
    
# Update
@field_bp.route("/updateField/<int:field_id>", methods=["PUT"])
def update_field(field_id):
    return update_field_logic(field_id)

# Delete
@field_bp.route("/delete/<int:field_id>", methods=["DELETE"])
def delete_field(field_id):
    return delete_field_logic(field_id)