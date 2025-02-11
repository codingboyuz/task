from tasklist.infrastructure.models import TaskModel


class TaskRepository:
    @staticmethod
    def save(task):
        task_obj, created = TaskModel.objects.update_or_create(
            id=task.id,
            defaults={
                "title": task.title,
                "description": task.description,
                "status": task.status.value,
                "priority": task.priority.value,
                "due_date": task.due_date,
                "updated_at": task.updated_at
            }
        )
        return task_obj

    @staticmethod
    def get_by_id(task_id):
        return TaskModel.objects.filter(id=task_id).first()

    @staticmethod
    def get_all():
        return TaskModel.objects.all()

    @staticmethod
    def delete(task_id):
        TaskModel.objects.filter(id=task_id).delete()
