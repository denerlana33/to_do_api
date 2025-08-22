from pydantic import BaseModel
from typing import Optional

class ToDoItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False

class ToDoItemCreate(ToDoItemBase):
    pass

class ToDoItem(ToDoItemBase):
    id: int

    class Config:
        orm_mode = True
