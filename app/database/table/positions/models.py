from app import db
from sqlalchemy import Enum
import enum

class StatusEnum(enum.Enum):
    active = "active"
    inactive = "inactive"

class Position(db.Model):
    __tablename__ = 'positions'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=True)
    level = db.Column(db.Integer, default=1)

    # 部門外鍵
    department_id = db.Column(db.BigInteger, db.ForeignKey("department.id"), nullable=True)

    # 狀態
    status = db.Column(Enum(StatusEnum), default=StatusEnum.active, nullable=False)

    # 時間戳
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)

    # 關聯：每個 Position 屬於一個 Department
    department = db.relationship("Department", back_populates="positions")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "level": self.level,
            "department_id": self.department_id,
            "status": self.status.value if self.status else None,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        
    def __repr__(self):
        return f"<Position {self.name}>"
