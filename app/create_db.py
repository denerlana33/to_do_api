from app.database import Base, engine
from app import models  # importa os modelos para registrar as tabelas

Base.metadata.create_all(bind=engine)

print("Banco de dados criado com sucesso!")
