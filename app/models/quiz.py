from app.models.base_model import BaseModel
from app import db
from app.models.student import student_score
"""
Subject class for the Quiz App
"""

class Quiz(BaseModel):
    """
    Args:
        name: Quiz uid in integer
        questions: all questions for the quiz
    Usage:
        We only have to do : `Quiz(name=<'name of subject'>)`
    """
    name = db.Column(db.Integer, autoincrement=True, unique=True)
    questions = db.relationship('Question', backref='quiz')
    
    def __repr__(self):
        return f'{self.name}:\n{list(self.questions)}'
