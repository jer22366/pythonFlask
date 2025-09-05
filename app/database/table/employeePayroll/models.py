from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    employee_code = db.Column(db.String(20), unique=True, nullable=False)  # 員工編號
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50))
    position = db.Column(db.String(50))
    hire_date = db.Column(db.Date, nullable=False)
    # 關聯
    payrolls = db.relationship('Payroll', backref='employee', lazy=True)

class Payroll(db.Model):
    __tablename__ = "payrolls"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    month = db.Column(db.Date, nullable=False)  # 對應薪資月份
    base_salary = db.Column(db.Float, nullable=False, default=0.0)  # 基本薪
    # 總津貼/總獎金/總扣款可計算，也可以拆子表
    total_allowance = db.Column(db.Float, nullable=False, default=0.0)
    total_bonus = db.Column(db.Float, nullable=False, default=0.0)
    total_deduction = db.Column(db.Float, nullable=False, default=0.0)
    net_salary = db.Column(db.Float, nullable=False, default=0.0)  # 實發薪資
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # 關聯
    allowances = db.relationship('Allowance', backref='payroll', lazy=True)
    bonuses = db.relationship('Bonus', backref='payroll', lazy=True)
    deductions = db.relationship('Deduction', backref='payroll', lazy=True)

class Allowance(db.Model):
    __tablename__ = "allowances"
    id = db.Column(db.Integer, primary_key=True)
    payroll_id = db.Column(db.Integer, db.ForeignKey('payrolls.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 交通津貼、加班費等
    amount = db.Column(db.Float, nullable=False, default=0.0)

class Bonus(db.Model):
    __tablename__ = "bonuses"
    id = db.Column(db.Integer, primary_key=True)
    payroll_id = db.Column(db.Integer, db.ForeignKey('payrolls.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 年終、績效獎金
    amount = db.Column(db.Float, nullable=False, default=0.0)

class Deduction(db.Model):
    __tablename__ = "deductions"
    id = db.Column(db.Integer, primary_key=True)
    payroll_id = db.Column(db.Integer, db.ForeignKey('payrolls.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 勞保、健保、罰款等
    amount = db.Column(db.Float, nullable=False, default=0.0)
