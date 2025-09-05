from flask import Blueprint
from app.Services.ReportSettingService.reportLogService import (
    create_log_logic,
    list_logs_logic,
    update_log_logic,
    delete_log_logic
)
report_export_logs_bp = Blueprint("report_export_logs", __name__, url_prefix="/api/report-export-logs")

# Create
@report_export_logs_bp.route("/create", methods=["POST"])
def create_log():
    return create_log_logic()

# Read all
@report_export_logs_bp.route("/getLogs", methods=["GET"])
def list_logs():
    return list_logs_logic()
   
# Update (e.g., mark finished)
@report_export_logs_bp.route("/update/<int:log_id>", methods=["PUT"])
def update_log(log_id):
    return update_log_logic(log_id)

# Delete
@report_export_logs_bp.route("/delete/<int:log_id>", methods=["DELETE"])
def delete_log(log_id):
    return delete_log_logic(log_id)
