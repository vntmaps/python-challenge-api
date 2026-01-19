from app.models import Task

class TaskService:
    @staticmethod
    def get_tasks(status_filter=None):
        query = Task.query
        if status_filter:
            query = query.filter_by(status=status_filter)
        return query.all()