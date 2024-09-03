from sqlalchemy.orm import Session

from services.db.model.task_model import TaskModel
from app.schemas.task_schema import Task

def add_task(db: Session, task: Task):
    db_task = TaskModel(title=task.title, description=task.description, completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task