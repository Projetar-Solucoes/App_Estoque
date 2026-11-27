from fastapi import FastAPI
from database import Base, engine
from models import *
app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/nome")
def ola():
    return {"mensagem": "Olá mundo"}




