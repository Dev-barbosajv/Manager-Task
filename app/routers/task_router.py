from fastapi import APIRouter, Depends, Form
from typing import Annotated
from sqlalchemy.orm import Session

from app.schemas.task_schema import Task
from app.controllers.add_controller import add_task
from services.db.engine import get_db
from services.db.model.task_model import TaskModel

router = APIRouter()


@router.post("/add/", response_model=Task)
def create_task(
    title:  str = Form(...),
    description: str = Form(""),
    completed: bool = Form(False),
    db: Session = Depends(get_db)
):
    task = Task(title=title, description=description, completed=completed)
    instance = add_task(db, task)
    return instance

