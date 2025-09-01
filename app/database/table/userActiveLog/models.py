from app import db

class UserActiveLog(db.Model):
    __tablename__ = 'useractive_logs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ip = db.Column(db.String(45), nullable=False)  # 支援 IPv6
    user_agent = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    action = db.Column(db.String(length=50), nullable=True)
    # 關聯 (方便反查 user.logs)
    user = db.relationship("User", backref=db.backref("logs", lazy=True))

    def __repr__(self):
        return f"<UserActive user_id={self.user_id} ip={self.ip}>"