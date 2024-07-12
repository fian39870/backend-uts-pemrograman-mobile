from app import db
from app.model.user_model import User
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.String(50))
    description = db.Column(db.Text)
    location = db.Column(db.String(255))
    reward = db.Column(db.Numeric(10, 2))
    status = db.Column(db.Enum('assigned', 'completed', name='task_status'), nullable=False)
    title = db.Column(db.String(255))
    image = db.Column(db.String(255))
    image_detail = db.Column(db.String(255))
    user = db.relationship('User', backref='tasks')