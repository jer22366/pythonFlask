from flask import Blueprint
from app.Services.ReportSettingService.reportRecipientsService import (
    create_recipient_logic,
    update_recipient_logic,
    list_recipients_logic,
    delete_recipient_logic
)

recipients_bp = Blueprint("report_recipients", __name__, url_prefix="/api/report-recipients")

# Create
@recipients_bp.route("/create", methods=["POST"])
def create_recipient():
    return create_recipient_logic()

# Read all
@recipients_bp.route("/getRecipients", methods=["GET"])
def list_recipients():
    return list_recipients_logic()
    
# Update
@recipients_bp.route("/update/<int:recipient_id>", methods=["PUT"])
def update_recipient(recipient_id):
    return update_recipient_logic(recipient_id)
    

# Delete
@recipients_bp.route("/delete/<int:recipient_id>", methods=["DELETE"])
def delete_recipient(recipient_id):
    return delete_recipient_logic(recipient_id)
    
