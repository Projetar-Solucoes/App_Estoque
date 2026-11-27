from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Empresa(Base):
    __tablename__ = "empresa"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)

    usuarios = relationship("Usuario", back_populates="empresa")
    categorias = relationship("Categoria", back_populates="empresa")
    produtos = relationship("Product", back_populates="empresa")