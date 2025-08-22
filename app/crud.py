from sqlalchemy.orm import Session
from app import models, schemas

# Buscar uma tarefa por ID
def get_todo(db: Session, todo_id: int):
    return db.query(models.ToDoItem).filter(models.ToDoItem.id == todo_id).first()

# Listar todas as tarefas (com paginação opcional)
def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ToDoItem).offset(skip).limit(limit).all()

# Criar uma nova tarefa
def create_todo(db: Session, todo: schemas.ToDoItemCreate):
    db_todo = models.ToDoItem(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
