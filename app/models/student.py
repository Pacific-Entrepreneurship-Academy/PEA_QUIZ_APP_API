"""
Student user class for the Quiz App
"""
from app.models.base_model import BaseModel
from app import db
from werkzeug.security import check_password_hash, generate_password_hash


student_subject = db.Table(
    'student_subject',
    db.Column('student_name', db.String(255), db.ForeignKey('student.email')),
    db.Column('subject_name', db.String(255), db.ForeignKey('subject.name'))
)

# student_score = db.Table(
#     'student_score',
#     db.Column('student_name', db.String(255), db.ForeignKey('student.email')),
#     db.Column('score', db.Integer, db.ForeignKey('score.value')),
#     db.Column('quiz', db.Integer, db.ForeignKey('quiz.name'))
# )


class Student(BaseModel):
    """
    Args:
        firstname: FirstName of student 
        lastname: LastName of the student
        email: Student email
        password_hash: a hashed value of the student's password
        year_: The year(form) of the student
        subjects: The student's subjects
    Usage:
        We firstly do: `var = Student(firstname=,lastname=,email=,year_=<Year.get(name=year given)>)`
        then `var.set_password(password)`
        To add subjects we do `var.subjects.append(Subject.get(name=subject_name))
    """
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    year_ = db.Column(db.String(255), db.ForeignKey('year.name'))
    subjects = db.relationship(
        'Subject', overlaps="student,subject",secondary=student_subject, backref='student',lazy='dynamic')
    # quizzes = db.relationship(
        # 'Quiz', overlaps="score,student",secondary=student_score, backref='quiz',lazy='dynamic')
    quiz_records = db.relationship('QuizRecord',backref='student')


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Student {}>'.format(self.id)


