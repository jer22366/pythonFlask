from flask import Blueprint

from app.Services.ReportSettingService.reportSchedulesService import (
    create_schedule_logic,
    list_schedules_logic,
    get_schedule_logic,
    update_schedule_logic,
    delete_schedule_logic
)
re_schedules_bp = Blueprint("report_schedules", __name__, url_prefix="/api/report-schedules")

# Create
@re_schedules_bp.route("/create", methods=["POST"])
def create_schedule():
    return create_schedule_logic()
    

# Read all
@re_schedules_bp.route("/getSchedules", methods=["GET"])
def list_schedules():
    return list_schedules_logic()

# Read one
@re_schedules_bp.route("/getSchedules/<int:schedule_id>", methods=["GET"])
def get_schedule(schedule_id):
    return get_schedule_logic(schedule_id)
    

# Update
@re_schedules_bp.route("/update/<int:schedule_id>", methods=["PUT"])
def update_schedule(schedule_id):
    return update_schedule_logic(schedule_id)

# Delete
@re_schedules_bp.route("/delete/<int:schedule_id>", methods=["DELETE"])
def delete_schedule(schedule_id):
    return delete_schedule_logic(schedule_id)
