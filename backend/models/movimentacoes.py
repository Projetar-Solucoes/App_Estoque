from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Movimentacoes(Base):
    __tablename__ = "movimentacoes"

    id = Column(Integer, primary_key=True, index=True)

    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    tipo = Column(String(20), nullable=False)
    quantidade = Column(Float, nullable=False)

    produto = relationship("Produto", back_populates="movimentacoes")
    usuarios = relationship("Usuario", back_populates="movimentacoes")