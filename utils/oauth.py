import logging
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.consumer import oauth_authorized
from flask_login import login_user
from flask import flash, redirect, url_for, session
from models.user import User
from models.oauth import OAuth
from utils.db import db
from sqlalchemy.orm.exc import NoResultFound
import os
from oauthlib.oauth2.rfc6749.errors import OAuth2Error

logging.basicConfig(level=logging.INFO)

def init_google_oauth(app):
    blueprint = make_google_blueprint(
        client_id=os.getenv('GOOGLE_OAUTH_CLIENT_ID'),
        client_secret=os.getenv('GOOGLE_OAUTH_CLIENT_SECRET'),
        scope=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'],
        reprompt_consent=True,
        storage=SQLAlchemyStorage(
            model=OAuth,
            session=db.session,
            user=User,
            user_required=False
        )
    )
    app.register_blueprint(blueprint, url_prefix='/login')

    @oauth_authorized.connect_via(blueprint)
    def google_logged_in(blueprint, token):
        if not token:
            flash("Error al iniciar sesión con Google.", "error")
            return False

        try:
            resp = blueprint.session.get('/oauth2/v2/userinfo')
            if not resp.ok:
                flash("Error al obtener información del usuario de Google.", "error")
                return False

            google_info = resp.json()
            google_user_id = str(google_info['id'])

            query = OAuth.query.filter_by(
                provider=blueprint.name,
                provider_user_id=google_user_id,
            )
            try:
                oauth = query.one()
            except NoResultFound:
                oauth = OAuth(
                    provider=blueprint.name,
                    provider_user_id=google_user_id,
                    token=token,
                )

            if oauth.user:
                login_user(oauth.user)
                flash("Inicio de sesión con Google exitoso.", "success")
            else:
                email = google_info['email']
                username = email.split('@')[0]
                
                user = User.query.filter_by(email=email).first()
                if not user:
                    user = User(
                        username=username,
                        email=email,
                    )
                    db.session.add(user)
                    db.session.commit()
                
                oauth.user = user
                db.session.add(oauth)
                db.session.commit()
                
                login_user(user)
                flash("Cuenta creada y inicio de sesión exitoso.", "success")

            if 'state' in token:
                session['google_oauth_state'] = token['state']
            elif 'access_token' in token:
                session['google_oauth_state'] = token['access_token']
            else:
                session['google_oauth_state'] = 'no_state'

            logging.info(f"Token recibido: {token}")

            return False

        except OAuth2Error as e:
            if "Scope has changed" in str(e):
                # Manejar el cambio de scope
                logging.warning(f"Cambio de scope detectado: {str(e)}")
                # Puedes optar por borrar el token existente y forzar una nueva autenticación
                token = blueprint.token
                if token:
                    del token
                return redirect(url_for('google.login'))
            else:
                logging.error(f"OAuth2Error: {str(e)}")
                flash("Error en la autenticación de Google. Por favor, intente nuevamente.", "error")
            return False

