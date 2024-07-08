from flask import Blueprint, jsonify, request
from app import db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    tasks_ref = db.collection('tasks')
    tasks = tasks_ref.stream()

    task_list = []
    for task in tasks:
        task_dict = task.to_dict()
        task_dict['id'] = task.id 
        task_list.append(task_dict)

    return jsonify(task_list), 200