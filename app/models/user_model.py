import json
from database import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    roles=db.Column(db.String(50), nullable=False)
    password_hash=db.Column(db.String(128), nullable=False)
    

    def __init__(self, name, email, roles, password):
        self.name=name
        self.email=email
        self.roles=json.dumps(roles)
        self.password_hash=generate_password_hash(password)



    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()
    @staticmethod
    def find_by_username(name):
        return User.query.filter_by(name=name).first()
    
  