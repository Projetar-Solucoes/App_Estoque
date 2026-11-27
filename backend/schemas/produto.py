from pydantic import BaseModel
from typing import Optional


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    quantidade: int 
    categoria_id: int 
    empresa_id: int 

