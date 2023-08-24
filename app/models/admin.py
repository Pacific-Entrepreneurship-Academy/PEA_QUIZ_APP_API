"""
Admin user class for the Quiz App
"""
from app.models.base_model import BaseModel
from app import db
from werkzeug.security import check_password_hash, generate_password_hash


class Admin(BaseModel):
    """
    Args:
        username: Username of admin 
        email: email of admin
        password_hash: a hashed value of the admin's password
        questions: all questions written by admin
    Usage:
        We firstly do: `var = Admin(username=,email=)`
        then `var.set_password(password)`
    """
    
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    questions = db.relationship('Questions', backref='author', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def save(self):
        if not isinstance(self.email, str):
            raise TypeError("Email must be a string")
        super().save()
    def __repr__(self):
        return '<Admin {}>'.format(self.username)