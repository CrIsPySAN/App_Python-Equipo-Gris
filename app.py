from flask import Flask
from flask_login import LoginManager
from utils.db import db, init_db
from models.user import User
import logging
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from utils.oauth import init_google_oauth
from flask_session import Session

# Cargar variables de entorno
load_dotenv()

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # Permite OAuth2 sobre HTTP para desarrollo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

init_db(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login_route'

init_google_oauth(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from routes.login import login as login_blueprint
app.register_blueprint(login_blueprint)