from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models import Usuario

def listar_todos_usuarios():
    return Usuario.query.order_by(Usuario.id.desc()).all()

def obter_usuario(usuario_id):
    return Usuario.query.get_or_404(usuario_id)

def salvar_usuario(nome, email, senha=None, usuario_id=None):
    if not nome or not email:
        return False, "Nome e E-mail são campos obrigatórios."

    try:
        if usuario_id:
            usuario = obter_usuario(usuario_id)
            usuario.nome = nome
            usuario.email = email

        if senha and senha.strip():
            usuario.set_senha(senha)

            mensagem = "Usuario atualizado com sucesso!"

        else: 
            if not senha:
                usuario = Usuario(nome=nome, email=email)
                usuario.set_senha(senha)
                db.session.add(usuario)
                mensagem = "Usuario cadastrado com sucesso!"

        db.session.commit()
        return True, mensagem
   
    except IntegrityError:
        db.session.rollback()
        return False, "Erro: este E-mail ja está cadastrado!"
    
    except Exception as e:
        db.session.rollback()
        return False, f"Erro interno {str(e)}"
    
def excluir_usuario(usuario_id):
    usuario = obter_usuario(usuario_id)
    try:
        db.session.delete(usuario)
        db.session.commit()
        return True, "Usuário excluido com sucesso!"
    except Exception as e:
        return False, f"Erro ao excluir usuário {str(e)}"