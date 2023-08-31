from app.models.base_model import BaseModel
from app import db

class QuizRecord(BaseModel):
    student_id = db.Column(db.String(255), db.ForeignKey('student.id'), nullable=False)
    quiz_id = db.Column(db.String(255), db.ForeignKey('quiz.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    
    student = db.relationship('Student', backref='quiz_records')
    quiz = db.relationship('Quiz', backref='quiz_records')
