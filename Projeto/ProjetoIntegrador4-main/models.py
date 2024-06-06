from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, senha, tipo, active=True):
        self.id = id
        self.senha = senha
        self.tipo = tipo
        self.active = active

    @property
    def is_active(self):
        return self.active