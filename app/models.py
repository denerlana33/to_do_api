from sqlalchemy import Column, Integer, String
from app.database import Base  # Importa o Base do database.py

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
