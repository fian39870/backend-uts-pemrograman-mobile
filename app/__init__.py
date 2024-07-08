from flask import Flask
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS
import os

firebase_key = os.environ.get('FIREBASE_KEY')
credential = credentials.Certificate(firebase_key)
firebase_admin.initialize_app(credential)
db = firestore.client()

def create_app():
    app = Flask(__name__)
    CORS(app)   
    from app.controllers.user_controller import users_bp
    from app.controllers.task_controller import tasks_bp
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')
    return app