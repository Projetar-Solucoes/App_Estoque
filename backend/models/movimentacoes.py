from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Movimentacoes(Base):
    __tablename__ = "movimentacoes"

    id = Column(Integer, primary_key=True, index=True)

    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    tipo = Column(String(20), nullable=False)
    quantidade = Column(Float, nullable=False)

    produto = relationship("Product", back_populates="movimentacoes")
    usuario = relationship("Usuario", back_populates="movimentacoes")