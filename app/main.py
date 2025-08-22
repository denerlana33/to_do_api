from fastapi import FastAPI
from app.database import engine
from app import models
from app.schemas import ToDoItem

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando!"}
