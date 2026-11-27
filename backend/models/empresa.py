from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Empresa(Base):
    __tablename__ = "empresa"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

    usuarios = relationship("Usuario", back_populates="empresa")
    categorias = relationship("Categoria", back_populates="empresa")
    produtos = relationship("Produto", back_populates="empresa")