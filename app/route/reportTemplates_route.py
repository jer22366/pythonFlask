from flask import Blueprint
from app.Services.reportSettingService.reportTemplateService import (
    create_template_logic, 
    list_templates_logic, 
    get_template_logic, 
    update_template_logic,
    delete_template_logic
)       
template_bp = Blueprint("report_templates", __name__, url_prefix="/api/report-templates")

# ✅ 建立 (Create)
@template_bp.route("/create", methods=["POST"])
def create_template():
    return create_template_logic()
   
# ✅ 查詢全部 (Read All)
@template_bp.route("/getTemplates", methods=["GET"])
def list_templates():
    return list_templates_logic()
    
# ✅ 查詢單筆 (Read One)
@template_bp.route("/getTemplate/<int:template_id>", methods=["GET"])
def get_template(template_id):
    return get_template_logic(template_id)
    
# ✅ 更新 (Update)
@template_bp.route("/update/<int:template_id>", methods=["PUT"])
def update_template(template_id):
    return update_template_logic(template_id)

# ✅ 刪除 (Delete)
@template_bp.route("/delete/<int:template_id>", methods=["DELETE"])
def delete_template(template_id):
    return delete_template_logic(template_id)
    
