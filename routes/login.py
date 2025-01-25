from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from urllib.parse import urlparse, urljoin
from models.user import User
from utils.db import db
from utils.validators import validate_registration
import logging

login = Blueprint('login', __name__)

@login.route('/')
def home():
    return redirect(url_for('login.login_route'))

@login.route('/dashboard',methods=['GET'] )
@login_required
def dashboard():
    return render_template('dashboard.html')

@login.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login.dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        errors = validate_registration(username, email, password, confirm_password)
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('register.html')
        
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        logging.info(f"Nuevo usuario registrado: {username}")
        flash('¡Registro exitoso! Por favor, inicia sesión.', 'success')
        return redirect(url_for('login.login_route'))
    return render_template('register.html')

@login.route('/login', methods=['GET', 'POST'])
def login_route():
    if current_user.is_authenticated:
        return redirect(url_for('login.dashboard'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        logging.info(f"Intento de inicio de sesión para el usuario: {username}")
        
        user = User.query.filter_by(username=username).first()
        if user:
            logging.info(f"Usuario encontrado: {user}")
            if user.check_password(password):
                logging.info("Contraseña válida, iniciando sesión")
                login_user(user, remember=request.form.get('remember_me'))
                next_page = request.args.get('next')
                if not next_page or not is_safe_url(next_page):
                    next_page = url_for('login.dashboard')
                return redirect(next_page)
            else:
                logging.warning("Contraseña inválida para el usuario")
                flash('Contraseña inválida', 'error')
        else:
            logging.warning(f"Usuario no encontrado: {username}")
            flash('Usuario no encontrado', 'error')
    return render_template('login.html')

@login.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('login.login_route'))

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

