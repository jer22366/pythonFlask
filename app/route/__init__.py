from .user_route import user_bp
from .department_route import organ_bp
from .position_route import position_bp
from .leaveType_route import leaveType_bp
from .reportTemplates_route import template_bp
from .report_field_route import field_bp
from .reportRecipients_route import recipients_bp
from .reportExportLogs_route import report_export_logs_bp
from .reportSchedules_route import re_schedules_bp
blueprints = [
    user_bp,
    organ_bp,
    position_bp,
    leaveType_bp,
    template_bp,
    field_bp,
    recipients_bp,
    report_export_logs_bp,
    re_schedules_bp
]