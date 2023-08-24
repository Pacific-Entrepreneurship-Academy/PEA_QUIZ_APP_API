"""
Year class for the Quiz App
"""
from app.models.base_model import BaseModel
from app import db


class Year(BaseModel):
    """
    Args:
        name: Name of class, could be Year one ....
        questions: all questions for the year
        students: all students in the year
    Usage:
        We only need to do : `Year(name=<'name of year'>)`
    """
    name = db.Column(db.String(255), nullable=False, unique=True)
    questions = db.relationship('Questions', backref='year', lazy='dynamic')
    students = db.relationship('Student', backref='year', lazy='dynamic')

    def save(self):
        if not isinstance(self.name, str) and self.name.islower():
            raise TypeError("year name must be a lowercase string")
        super().save()

    def __repr__(self):
        return f'<Year {self.name}>'
