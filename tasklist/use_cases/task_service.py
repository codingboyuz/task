from tasklist.infrastructure.repositories.task_repository import TaskRepository
from tasklist.core.entities import Task

class TaskUseCase:
    def __init__(self,repository:TaskRepository):
        self.repository = repository


    def create_task(self,title,description,status,priority,due_date):
        task = Task(title=title,description=description,status=status,priority=priority,due_date=due_date)
        self.repository.save(task)
        return task