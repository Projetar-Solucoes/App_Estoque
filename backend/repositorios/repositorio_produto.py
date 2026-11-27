from schemas.produto import Produto
from models.produto import Product
from sqlalchemy.orm import Session

class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db

    def criar_produto(self, dados: Produto):
        novo_produto = Product(id = dados.id, name = dados.nome, preco = dados.preco, quantidade = dados.quantidade, empresa_id = dados.empresa_id, categoria_id = dados.categoria_id)

        self.db.add(novo_produto)
        self.db.commit()
        self.db.refresh(novo_produto)

        return novo_produto


