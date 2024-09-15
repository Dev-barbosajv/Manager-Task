from fastapi import APIRouter, Depends, Form, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session

from app.schemas.task_schema import TaskResponse, TaskCreate
from app.controllers.add_controller import create_task, get_task, update_task, delete
from services.db.engine import get_db
from services.db.model.task_model import TaskModel

router = APIRouter()


@router.post("/add/", response_model=TaskResponse)
def create_task(
    title:  str = Form(...),
    description: str = Form(""),
    completed: bool = Form(False),
    db: Session = Depends(get_db)
):
    task = TaskCreate(title=title, description=description, completed=completed)
    instance = create_task(db, task)
    return instance

@router.get("/tesk/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.put("/task/{task_id}", response_model=TaskResponse)
def update_existing_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = update_task(db, task_id, task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_task


@router.delete("/task/{task_id}")
def excluided_task(task_id: int, db: Session = Depends(get_db)):
    success = delete(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"Task deleted successfully"}