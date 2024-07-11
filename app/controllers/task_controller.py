from flask import Blueprint, jsonify, request, send_from_directory
from app import db
from app.model.task_model import Task

tasks_bp = Blueprint('tasks', __name__)
@tasks_bp.route('/tasks', methods=['GET'])
def get_all_tasks():
    try:
        tasks = Task.query.all()
        
        tasks_list = []
        base_url = current_app.config['BASE_URL']
        for task in tasks:
            picture_url = task.user.picture.strip()
            image_url = task.image.strip()
            tasks_list.append({
                'id': task.id,
                'user_id': task.user_id,
                'date': task.date,
                'description': task.description,
                'location': task.location,
                'reward': float(task.reward),  # Konversi ke float untuk JSON
                'status': task.status,
                'title': task.title,
                'image': f"http://{base_url} :5000/static/images/{image_url}",
                'user': {
                    'id': task.user.id,
                    'created_at': task.user.created_at.strftime('%Y-%m-%d %H:%M:%S'),  # Format tanggal sesuai kebutuhan
                    'email': task.user.email,
                    'picture': f"{base_url}/static/images/{picture_url}",
                    'rating': float(task.user.rating) if task.user.rating is not None else None,
                    'username': task.user.username
                }
            })
        return jsonify({'tasks': tasks_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

