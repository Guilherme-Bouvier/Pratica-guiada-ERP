from flask import Blueprint,jsonify

from app.models import Categoria, Produto, Usuario

api_bp = Blueprint('api', __name__, url_prefix="/api")

@api_bp.route("/produtos", methods=["GET"])
def get_produto():
    produtos = Produto.query.all()

    listar_json = [produto.to_dict() for produto in produtos]
    return jsonify (listar_json), 200

@api_bp.route("/categorias", methods=["GET"])
def get_categoria():
    categorias = Categoria.query.all()

    listar_json = [categoria.to_dict() for categoria in categorias]
    return jsonify (listar_json), 200

@api_bp.route("/usuarios", methods=["GET"])
def get_usuarios():
    
    usuarios = Usuario.query.all()
    listar_json = [usuario.to_dict() for usuario in usuarios]
    return jsonify (listar_json), 200