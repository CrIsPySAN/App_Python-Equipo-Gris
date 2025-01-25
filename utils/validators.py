from models.user import User

def validate_registration(username, email, password, confirm_password):
    errors = []
    if not username or not email or not password or not confirm_password:
        errors.append('Todos los campos son obligatorios')
    if password != confirm_password:
        errors.append('Las contraseñas no coinciden')
    if User.query.filter_by(username=username).first():
        errors.append('El nombre de usuario ya está en uso')
    if User.query.filter_by(email=email).first():
        errors.append('El correo electrónico ya está en uso')
    return errors

