import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/task_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

