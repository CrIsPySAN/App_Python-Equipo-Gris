import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Usa tu base de datos preferida
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # Clave secreta para sesiones y JWT
    JWT_SECRET_KEY = os.urandom(24)  # Clave secreta para JWT
    WTF_CSRF_SECRET_KEY = os.urandom(24)  # Clave secreta para CSRF