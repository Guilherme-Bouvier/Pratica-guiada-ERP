from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.controllers import (produtos_controller, categoria_controller)

web_db = Blueprint("web", __name__)

@web_db.route("/")
def index ():
    return redirect(url_for("web.listar_produtos_view"))


@web_db.route ("/produtos")
def listar_produtos_view():
        
        produtos = produtos_controller.listar_todos_produtos()
        return render_template("produtos/listar.html", produtos=produtos)


@web_db.route("/produto/novo", methods=["GET", "POST"])
def novo_produto_view():
      
      categorias = categoria_controller.listar_todas_categorias()

      if request.method == "POST":
            nome = request.form.get("nome")
            preco = float(request.form.get("preco", 0))
            categoria_id = int(request.form.get("categoria_id", 0))

            sucesso, msg = produtos_controller.salvar_produtos(nome, preco, categoria_id)
            flash(msg, "Sucesso" if sucesso else " danger")

            if sucesso:
                  return redirect(url_for("web.listar_produtos_view"))
            
      return render_template("produtos/form.html", produto=None, categorias=categorias)


@web_db.route("/produto/excluir/<int:id>", methods=["DELETE"])
def exlcuir_produto_view(id):
      pass


# ROTAS DE CATEEGORIA

@web_db.route("/categorias")
def listar_categorias_view():
      categorias = categoria_controller.listar_todas_categorias()
      return render_template("categorias/listar.html", categorias=categorias)

@web_db.route("/categorias/novo", methods=["GET", "POST"])
def nova_categoria_view():
      if request.method == "POST":
            nome = request.form.get("nome_categoria")

            sucesso, msg = categoria_controller.salvar_categoria(nome)

            flash(msg, "success" if sucesso else "danger")

            if sucesso:
                  return redirect(url_for('web.listar_categoria_view'))

      return render_template("categorias/form.html", categoria=None)

@web_db.route("/categoria/excluir/<int:id>", methods=["DELETE"])
def exlcuir_categoria_view(id):
      pass
