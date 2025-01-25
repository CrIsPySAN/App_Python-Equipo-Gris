from flask import Flask
from flask_login import LoginManager
from utils.db import db, init_db
from models.user import User
import logging
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'  

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

init_db(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login_route'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from routes.login import login as login_blueprint
app.register_blueprint(login_blueprint)

