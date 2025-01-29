from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from utils.db import db
import logging

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))  

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        logging.info(f"Contraseña establecida para el usuario {self.username}")
        logging.info(f"Hash generado: {self.password_hash}")

    def check_password(self, password):
        if not self.password_hash:
            logging.error(f"No hay hash de contraseña almacenado para el usuario {self.username}")
            return False
        result = check_password_hash(self.password_hash, password)
        logging.info(f"Verificación de contraseña para {self.username}: {'exitosa' if result else 'fallida'}")
        logging.info(f"Hash almacenado: {self.password_hash}")
        logging.info(f"Contraseña proporcionada: {password}")
        return result

    def __repr__(self):
        return f'<User {self.username}>'

