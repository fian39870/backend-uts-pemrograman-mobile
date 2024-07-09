from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)   
    db.init_app(app)
    from app.controllers.task_controller import tasks_bp
    app.register_blueprint(tasks_bp)
    return app