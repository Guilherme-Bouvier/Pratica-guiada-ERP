from app.extenssion import db

class Produto(db.Model):
    __tablename__="produtos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=False)

    def to_dict(Self):
        return{
            "id": Self.id,
            "nome": Self.nome,
            "preco": Self.preco,
            "categoria": Self.categoria.nome

        }