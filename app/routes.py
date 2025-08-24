from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/tarefas/", response_model=schemas.Tarefa)
def criar_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(database.get_db)):
    return crud.criar_tarefa(db, tarefa)
