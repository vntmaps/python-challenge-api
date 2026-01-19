from flask import Blueprint, request, jsonify
from app.service import TaskService

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['GET'])
def list_tasks():
    status = request.args.get('status')
    tasks = TaskService.get_tasks(status)
    return jsonify([{
        "id": t.id,
        "title": t.title,
        "status": t.status
    } for t in tasks]), 200