from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
migrate = Migrate()
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)   
    migrate.init_app(app, db)
    db.init_app(app)
    from app.controllers.task_controller import tasks_bp
    app.register_blueprint(tasks_bp)
    return app