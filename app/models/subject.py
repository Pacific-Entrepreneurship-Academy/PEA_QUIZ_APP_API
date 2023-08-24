from app.models.base_model import BaseModel
from app import db
from app.models.student import student_subject


"""
Subject class for the Quiz App
"""

class Subject(BaseModel):
    """
    Args:
        name: Name of subject
        questions: all questions for the subject
        students: all students taking the subject
    Usage:
        We only have to do : `Subject(name=<'name of subject'>)`
    """
    name = db.Column(db.String(255), nullable=False, unique=True)
    questions = db.relationship('Questions', backref='subject', lazy='dynamic')
    students = db.relationship(
        'Student', overlaps="student,subjects",secondary=student_subject, backref='subject',lazy='dynamic')

    def __repr__(self):
        return f'<Subject {self.id}\nName: {self.name}>'
