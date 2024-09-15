from sqlalchemy.orm import Session

from services.db.model.task_model import TaskModel
from app.schemas.task_schema import TaskCreate


def create_task(db: Session, task: TaskCreate):
    db_task = TaskModel(title=task.title, description=task.description, completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()



def update_task(db: Session, task_id: int, task_data: TaskCreate):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task:
        db_task.title = task_data.title
        db_task.description = task_data.description
        db_task.completed = task_data.completed
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def delete(db: Session, task_id: int):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False