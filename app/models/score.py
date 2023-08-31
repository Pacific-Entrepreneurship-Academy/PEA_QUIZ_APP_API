# from app.models.base_model import BaseModel
# from app import db
# from app.models.student import Student
# from app.models.quiz import Quiz
# from app.models.student import student_score
# """
# Score class for the Quiz App
# """


# class Score(BaseModel):
#     """
#     Args:
#         value: Score Value
#         quiz_id: Quiz taken
#         student_id: Student who took the quiz
#     Usage:
#         We have to first get the external keys: 
#             `quiz = Quiz.get(id=<quiz id>)`
#             `student = Student.get(id=<'student id'>)`
#         Then we populate db:
#             `score = Score(value=<The score as an int>,)`
#     """
#     value = db.Column(db.Integer, nullable=False)
#     quiz_id = db.Column(db.String(126), db.ForeignKey('quiz.id'))
#     student_id = db.Column(db.String(126), db.ForeignKey('student.id'))
#     student = db.relationship(
#         'Student', overlaps="score,student",secondary=student_score, backref='student',lazy='dynamic')
#     quizzes = db.relationship(
#         'Quiz', overlaps="score,student",secondary=student_score, backref='quiz',lazy='dynamic')
#     def __repr__(self):
#         return f'<Name {Student.get(id=self.student_id).name}\nScore: {self.value}>\nQuiz: {Quiz.get(self.quiz_id).name}'
