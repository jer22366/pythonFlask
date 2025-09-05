from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from extensions import db
class CompanyInfo(db.Model):
    __tablename__ = 'company_info'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 基本資料
    name = db.Column(db.String(255), nullable=False)          # 公司全名
    short_name = db.Column(db.String(100), nullable=True)     # 公司簡稱或英文名
    tax_id = db.Column(db.String(50), nullable=True)          # 統一編號 / 稅號
    logo_url = db.Column(db.String(255), nullable=True)       # 公司LOGO圖片URL
    address = db.Column(db.String(255), nullable=True)        # 公司地址
    phone = db.Column(db.String(50), nullable=True)           # 公司電話
    email = db.Column(db.String(100), nullable=True)          # 公司官方信箱
    website = db.Column(db.String(255), nullable=True)        # 官方網站

    # 其他設定
    founded_date = db.Column(db.Date, nullable=True)          # 公司成立日期
    industry = db.Column(db.String(100), nullable=True)       # 行業類別
    size = db.Column(db.String(50), nullable=True)            # 公司規模
    timezone = db.Column(db.String(50), nullable=True)        # 時區
    language = db.Column(db.String(50), nullable=True)        # 系統語系

    # 系統欄位
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f"<CompanyInfo {self.name}>"
