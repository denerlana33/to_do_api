from sqlalchemy.orm import Session
from app import schemas, models

def criar_tarefa(db: Session, tarefa: schemas.TarefaCreate):
    nova_tarefa = models.Tarefa(**tarefa.dict())
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa
