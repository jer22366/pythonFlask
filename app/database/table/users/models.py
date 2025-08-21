from app import db
from datetime import datetime
import enum
class LevelEnum(enum.Enum):
    admin = "admin"
    staff = "staff"
    manager = "manager"
    finance = "finance"
    HR = "HR"
class User(db.Model):
    __tablename__ = 'users'  # 明確指定表名

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    address = db.Column(db.String(200), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    level = db.Column(db.Enum(LevelEnum), nullable=False, default=LevelEnum.staff)
    def __repr__(self):
        return f'<User {self.username}>'
    
    def soft_delete(self):
        """執行軟刪除"""
        self.deleted_at =  datetime.now()

