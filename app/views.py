from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from app.forms import LoginForm
from flask_jwt_extended import create_access_token

main_bp = Blueprint('main', __name__)

@main_bp.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:  # Deberías usar hashing para las contraseñas
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        return jsonify(message="Invalid credentials"), 401
    return jsonify(message="Bad request"), 400
