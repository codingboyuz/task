from enum import Enum
from  uuid import uuid4


from  dataclasses import  dataclass
from datetime import datetime


class TaskStatus(Enum):
    PENDING ="pending"
    IN_PROGRESS="in_progress"
    COMPLETED = 'completed'

class TaskPriority(Enum):
    LOW ='low'
    MEDIUM = 'medium'
    HIGH='high'

@dataclass
class Task:
    id:str
    title:str
    description:str
    status:TaskStatus
    priority: TaskPriority
    due_date:datetime
    created_at:datetime
    updated_at: datetime

    def __init__(self,title,description,status,priority,due_date):
        self.id =str(uuid4())
        self.title = title
        self.description = description
        self.status = TaskStatus(status)
        self.priority = TaskPriority(priority)
        self.due_date = due_date,
        self.created_at = datetime.now()
        self.updated_at = datetime.now()





