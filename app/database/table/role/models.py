from datetime import datetime
from app import db

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(
        db.Enum("active", "inactive", name="rolestatusenum"),
        default="active"
    )

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()
    )

    # 關聯到通知設定
    notification_settings = db.relationship(
        "NotificationSetting", backref="role", lazy=True
    )

    def __repr__(self):
        return f"<Role {self.code}>"
