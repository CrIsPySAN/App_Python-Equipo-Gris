from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
csrf = CSRFProtect()

def create_app(config_class="instance.config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    csrf.init_app(app)
    CORS(app)  # Protege contra ataques Cross-Origin Resource Sharing
    
    from .views import main_bp
    app.register_blueprint(main_bp)

    return app

@app.after_request
def apply_security_headers(response):
    response.headers["X-Frame-Options"] = "DENY"
    return response
