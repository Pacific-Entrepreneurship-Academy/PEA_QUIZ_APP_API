from app.models.base_model import BaseModel
from app import db
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
    count = db.Column(db.Integer,nullable=False)
    questions = db.relationship('Questions', backref='quiz')
    quiz_records = db.relationship('QuizRecord',backref='quiz')
    def __repr__(self):
        return f'{self.id}:\n{list(self.questions)}'
