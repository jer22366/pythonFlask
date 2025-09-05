from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum, UniqueConstraint, Index, text
from extensions import db

# ENUM 定義 (會轉為 MySQL ENUM)
ReportFormat = Enum('pdf', 'xlsx', 'csv', name='report_format')
QueryEngine = Enum('sql', 'orm', 'python', name='report_query_engine')
DeliveryChannel = Enum('email', 'in_app', 'webhook', name='report_delivery_channel')
ScheduleStatus = Enum('active', 'paused', 'archived', name='report_schedule_status')
JobStatus = Enum('queued', 'running', 'success', 'failed', name='report_job_status')

class ReportTemplate(db.Model):
    __tablename__ = 'report_templates'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    code = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    query_engine = db.Column(QueryEngine, nullable=False, default='sql')
    sql_text = db.Column(db.Text)
    handler_name = db.Column(db.String(200))
    default_params = db.Column(db.JSON, nullable=False, server_default=text("'{}'"))
    default_format = db.Column(ReportFormat, nullable=False, default='xlsx')
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    created_by = db.Column(db.BigInteger)
    updated_by = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    fields = db.relationship("ReportField", backref="template", cascade="all, delete-orphan")
    schedules = db.relationship("ReportSchedule", backref="template", cascade="all, delete-orphan")

    __table_args__ = (
        Index("ix_report_templates_active", "is_active"),
    )

class ReportField(db.Model):
    __tablename__ = 'report_fields'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    template_id = db.Column(db.BigInteger, db.ForeignKey('report_templates.id', ondelete="CASCADE"), nullable=False)
    key = db.Column(db.String(200), nullable=False)
    label = db.Column(db.String(200), nullable=False)
    dtype = db.Column(db.String(50), nullable=False, default='string')
    visible = db.Column(db.Boolean, nullable=False, default=True)
    sort_order = db.Column(db.Integer, nullable=False, default=0)

    __table_args__ = (
        UniqueConstraint("template_id", "key", name="uq_report_field_template_key"),
        Index("ix_report_fields_template_sort", "template_id", "sort_order"),
    )

class ReportSchedule(db.Model):
    __tablename__ = 'report_schedules'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    template_id = db.Column(db.BigInteger, db.ForeignKey('report_templates.id', ondelete="CASCADE"), nullable=False)

    name = db.Column(db.String(200), nullable=False)
    frequency = db.Column(db.String(50))   # once/daily/weekly/monthly
    day_of_week = db.Column(db.String(20))
    day_of_month = db.Column(db.Integer)
    time_of_day = db.Column(db.String(10))
    cron = db.Column(db.String(120))
    timezone = db.Column(db.String(50), nullable=False, default='UTC')

    params = db.Column(db.JSON, nullable=False, server_default=text("'{}'"))
    output_format = db.Column(ReportFormat, nullable=False, default='xlsx')

    status = db.Column(ScheduleStatus, nullable=False, default='active')
    last_run_at = db.Column(db.DateTime)
    next_run_at = db.Column(db.DateTime)

    created_by = db.Column(db.BigInteger)
    updated_by = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    recipients = db.relationship("ReportRecipient", backref="schedule", cascade="all, delete-orphan")

    __table_args__ = (
        Index("ix_report_schedules_template", "template_id"),
        Index("ix_report_schedules_status_next", "status", "next_run_at"),
    )

class ReportRecipient(db.Model):
    __tablename__ = 'report_recipients'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    schedule_id = db.Column(db.BigInteger, db.ForeignKey('report_schedules.id', ondelete="CASCADE"), nullable=False)
    channel = db.Column(DeliveryChannel, nullable=False, default='in_app')
    email = db.Column(db.String(200))
    user_id = db.Column(db.BigInteger)

    __table_args__ = (
        Index("ix_report_recipients_schedule", "schedule_id"),
    )

class ReportExportLog(db.Model):
    __tablename__ = 'report_export_logs'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    template_id = db.Column(db.BigInteger, db.ForeignKey('report_templates.id', ondelete="SET NULL"))
    schedule_id = db.Column(db.BigInteger, db.ForeignKey('report_schedules.id', ondelete="SET NULL"))
    run_by = db.Column(db.BigInteger)
    params = db.Column(db.JSON, nullable=False, server_default=text("'{}'"))
    output_format = db.Column(ReportFormat, nullable=False)
    status = db.Column(JobStatus, nullable=False, default='queued')
    file_path = db.Column(db.String(500))
    error_message = db.Column(db.Text)

    started_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    finished_at = db.Column(db.DateTime)

    __table_args__ = (
        Index("ix_report_logs_template_started", "template_id", "started_at"),
        Index("ix_report_logs_status", "status"),
    )
