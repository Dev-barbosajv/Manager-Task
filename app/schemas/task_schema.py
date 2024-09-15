from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False

    class config:
        orm_mode = True

