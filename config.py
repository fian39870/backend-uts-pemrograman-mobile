import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/task_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_URL = os.getenv('BASE_URL', '127.0.0.1:5000')