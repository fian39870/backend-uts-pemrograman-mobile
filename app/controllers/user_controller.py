from flask import Blueprint, jsonify
from app import db

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
    users_ref = db.collection('users')
    users = [doc.to_dict() for doc in users_ref.stream()]

    for user in users:
        task_refs = user.get('tasks_assigned', [])
        tasks_assigned = []

        for task_ref in task_refs:
            task = task_ref.get()
            if task.exists:
                task_dict = task.to_dict()
                task_dict['id'] = task.id
                tasks_assigned.append(task_dict)

        user['tasks_assigned'] = tasks_assigned

    return jsonify(users)
