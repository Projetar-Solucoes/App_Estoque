from sqlalchemy import (Column,Integer,String,Boolean,Float,ForeignKey)
from sqlalchemy.orm import relationship

from database import Base


class Product(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)

    empresa_id = Column(Integer, ForeignKey("empresa.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=True)

    name = Column(String(120), nullable=False)
    
    preco = Column(Float)

    quantidade = Column(Float)
    

    empresa = relationship("Empresa", back_populates="produtos")
    categoria = relationship("Categoria", back_populates="produtos")
    movimentacoes = relationship("Movimentacoes", back_populates="produtos")