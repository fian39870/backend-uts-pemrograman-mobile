from app import db
   
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    email = db.Column(db.String(255), unique=True, nullable=False)
    picture = db.Column(db.String(255))
    rating = db.Column(db.Numeric(3, 2))
    username = db.Column(db.String(255), unique=True, nullable=False)