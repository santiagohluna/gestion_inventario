import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'clave_secreta'  # Cambiar por algo más seguro
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'activos.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
