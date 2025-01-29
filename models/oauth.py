from utils.db import db

class OAuth(db.Model):
    __tablename__ = 'oauth'
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50), nullable=False)
    provider_user_id = db.Column(db.String(256), nullable=False)
    token = db.Column(db.JSON, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref("oauth", cascade="all, delete-orphan"))