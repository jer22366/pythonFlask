from app import db

class Department(db.Model):
    __tablename__ = 'department'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)  # 部門名稱
    code = db.Column(db.String(20), nullable=True, unique=True)    # 部門代碼
    parent_id = db.Column(db.BigInteger, db.ForeignKey('department.id'), nullable=True)  # 上級部門
    level = db.Column(db.Integer, default=1)  # 部門層級（1=總部, 2=子部門）
    manager_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)  # 部門主管
    description = db.Column(db.Text, nullable=True)  # 部門說明
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    is_active = db.Column(db.Boolean, default=True)  # 是否啟用

    # 建立關聯（自我關聯）
    children = db.relationship('Department', backref=db.backref('parent', remote_side=[id]), lazy='dynamic')
    positions = db.relationship("Position", back_populates="department", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Department {self.name}>"

from app.database.table.positions.models import Position