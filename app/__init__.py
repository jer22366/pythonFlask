from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # 注意加上 app. 前綴

    db.init_app(app)
    migrate.init_app(app, db)

    from .route.user_route import user_bp

    app.register_blueprint(user_bp)
    return app