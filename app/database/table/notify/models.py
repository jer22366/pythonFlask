from app import db

class NotificationSetting(db.Model):
    __tablename__ = "notification_settings"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id"), nullable=True)   # 個人設定
    role_id = db.Column(db.BigInteger, db.ForeignKey("roles.id"), nullable=True)   # 群組設定
    event_type = db.Column(db.String(50), nullable=False)
    channel = db.Column(
        db.Enum("email", "system", "push", name="notificationchannelenum"),
        nullable=False
    )
    is_enabled = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()
    )

    def __repr__(self):
        return f"<NotificationSetting {self.event_type} - {self.channel}>"
