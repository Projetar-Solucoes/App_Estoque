from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    empresa_id = Column(Integer, ForeignKey("empresa.id"), nullable=False)

    name = Column(String(100), nullable=False)
    

    empresa = relationship("Empresa", back_populates="categorias")
    produtos = relationship("Produto", back_populates="categorias")