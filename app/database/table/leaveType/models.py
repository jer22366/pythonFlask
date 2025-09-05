from extensions import db

class LeaveType(db.Model):
    __tablename__ = 'leave_types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)  # 假別名稱
    is_paid = db.Column(db.Boolean, default=True)  # 是否帶薪
    annual_quota = db.Column(db.Float, nullable=True)  # 每年上限（天數，可為小數）
    description = db.Column(db.String(200), nullable=True)  # 假別說明
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f"<LeaveType {self.name}>"