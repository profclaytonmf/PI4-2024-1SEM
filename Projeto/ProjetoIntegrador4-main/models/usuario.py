from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    senha_hash = db.Column(db.String(128))
    tipo = db.Column(db.String(80))

    def __init__(self, id, senha, tipo):
        self.id = id
        self.senha_hash = generate_password_hash(senha)
        self.tipo = tipo

    def check_password(self, senha):
        return check_password_hash(self.senha_hash, senha)