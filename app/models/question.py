"""
Question class for the Quiz App
"""
from app.models.base_model import BaseModel
from app import db


class Questions(BaseModel):
    """
    Args:
        question: Question
        answer: answer to question
        options: Options stored as a list
        admin_id: A relationship key, which points to the admin that wrote the question
        subject_id: A relationship key, which points to the subjeect the question belongs to
        year: The Year the question is for, also a relationship
    Usage:
        We have to first get the external keys: 
            `admin = Admin.get(username=<admin username>)`
            `sub = Subject.get(name=<'name of subject'>)`
            `year = Year.get(name=<'name of year'>)`
        Then we populate db:
            `que = Questions(question=<The question>,answer=<the answer>,options=[<op1>,<op2>,<op3>,<op4>],author=admin,subject=subject,year=year)`
        We then check that answer is in options:
            `que.check_answer_in_option()` ~ Returns True or False    
    """
    question = db.Column(db.String(255), nullable=False, unique=True)
    answer = db.Column(db.String(255), nullable=False)
    options = db.Column(db.JSON, nullable=False)
    admin_id = db.Column(db.String(126), db.ForeignKey('admin.id'))
    subject_name = db.Column(db.String(255), db.ForeignKey('subject.name'))
    year_ = db.Column(db.String(255), db.ForeignKey('year.name'))
    quiz_id = db.Column(db.String(255), db.ForeignKey('quiz.id'))
    # quiz = db.relationship('Quiz', backref='question')



    def answer_in_option(self):
        if type(self.options) is dict:
            return self.answer in self.options.values()
        if type(self.options) is list:
            return self.answer in self.options

    def __repr__(self):
        return '<Question {}>'.format(self.id)
