from flask import Flask
from extensions import db, migrate
from app.route import blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # 注意加上 app. 前綴

    db.init_app(app)
    migrate.init_app(app, db)

    for bp in blueprints:
        app.register_blueprint(bp)

    return app