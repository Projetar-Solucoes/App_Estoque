from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session 
from database import Base, engine, get_db
from models import *
from schemas.produto import Produto
from repositorios.repositorio_produto import RepositorioProduto

app = FastAPI()

Base.metadata.create_all(bind=engine) #cria as tabelas quando executamos

@app.post("/produtos")
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    novo_produto = RepositorioProduto(db).criar_produto(produto)
    return novo_produto




