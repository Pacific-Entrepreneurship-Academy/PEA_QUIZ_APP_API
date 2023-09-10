from app import api
from app.models import *
from flask import jsonify, request
from sqlalchemy import or_, and_
import warnings
from sqlalchemy.exc import SAWarning

warnings.filterwarnings("ignore", category=SAWarning)
def quiz_count():
    return Quiz.query.count() + 1


# Admins
@api.route('/admins', methods=['POST', 'GET'])
def get_all_admin():
    if request.method == 'POST':
        data = request.json
        try:
            username = data['username']
            email = data['email']
            password = data['password']
            condition = and_(Admin.username == username, Admin.email == email)
            if Admin.query.filter(condition).first():
                print(condition)
                return jsonify({"error": "an admin found with given data"}), 406
            admin = Admin(username=username, email=email)
            admin.set_password(password)
            admin.save()
            admins = [x.to_dict() for x in Admin.all()]
            return jsonify({'data': admins, 'status': 'created'}), 201
        except KeyError:
            return jsonify({'error': 'Missing required data', 'status': 'Failed'}), 400
    admins = [x.to_dict() for x in Admin.all()]
    return jsonify(admins), 200

@api.route('/get-admin/query')
def get_admin():
    username = request.args.get('username')
    email = request.args.get('email')
    id = request.args.get('id')
    if id:
        admin = Admin.get(id=id)
        if admin is None:
            return jsonify({"error": "No Admin found with the id specified"}), 404
        return jsonify({'message': 'success', 'data': [admin.to_dict()]}), 200
    if username:
        admin = Admin.get(username=username)
        if admin is None:
            return jsonify({"error": "No admin found with that user name"}), 404
        return jsonify({'message': 'success', 'data': admin.to_dict()}), 200
    if email:
        admin = Admin.get(email=email)
        if admin is None:
            return jsonify({"error": "No admin found with that user name"}), 404
        return jsonify({'message': 'success', 'data': admin.to_dict()}), 200
    return jsonify({'error': 'Parameters missing'}), 400

@api.post('/admin/login')
def admin_login():
    data = request.json
    try:
        username = data['username']
        email = data.get('email')
        password = data['password']
        condition = or_(Admin.username == username, Admin.email == email)
        user = Admin.query.filter(condition).first()
        if not user:
            return jsonify({"error": "No user found with such record", 'status': 'Failed'}), 404
        if user.check_password(password):
            return jsonify({'message': 'Logged in', 'status': 'success'}), 200
        else:
            return jsonify({'error': 'Incorrect password', 'status': 'Failed'}), 403
    except KeyError:
        return jsonify({'error': 'Missing required data', 'status': 'Failed'}), 400

# Students
@api.route('/students', methods=['POST', 'GET'])
def get_all_student():
    if request.method == 'POST':
        data = request.json
        try:
            firstname = data['firstname']
            lastname = data['lastname']
            email = data['email']
            password = data['password']
            year = Year.query.filter_by(name=data['year']).first()
            if year is None:
                return jsonify({"error": "Invalid Year given"}), 400
            if Student.get(email=email):
                return jsonify({"error": "a student found with given email"}), 406
            student = Student(firstname=firstname,
                              lastname=lastname, year=year, email=email)
            student.set_password(password)
            student.save()
            students = [x.to_dict() for x in Student.all()]
            return jsonify({'data': students, 'status': 'created'}), 201
        except KeyError:
            return jsonify({'error': 'Missing or Invalid required data', 'status': 'Failed'}), 400
    students = [x.to_dict() for x in Student.all()]
    return jsonify(students), 200

@api.route('/get-student/query')
def get_student():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    email = request.args.get('email')
    id = request.args.get('id')
    if firstname:
        student = Student.query.filter_by(firstname=firstname).all()
        if student is None:
            return jsonify({"error": "No student found with the firstname given"}), 404
        return jsonify({'message': 'success', 'data': [x.to_dict() for x in student]}), 200
    if id:
        student = Student.get(id=id)
        if student is None:
            return jsonify({"error": "No student found with the id specified"}), 404
        return jsonify({'message': 'success', 'data': [student.to_dict()]}), 200

    if lastname:
        student = Student.query.filter_by(lastname=lastname).all()
        if student is None:
            return jsonify({"error": "No student found with the lastname given"}), 404

        return jsonify({'message': 'success', 'data': [x.to_dict() for x in student]}), 200

    if email:
        student = Student.get(email=email)
        if student is None:
            return jsonify({"error": "No student found with that email"}), 404
        return jsonify({'message': 'success', 'data': student.to_dict()}), 200
    return jsonify({'error': 'Arguments missing or Invalid'}), 400

@api.post('/student/login')
def student_login():
    data = request.json
    try:
        email = data['email']
        password = data['password']
        user = Student.query.filter_by(email=email).first()
        if not user:
            return jsonify({"error": "No user found with such record", 'status': 'Failed'}), 404
        if user.check_password(password):
            return jsonify({'message': 'Logged in', 'status': 'success'}), 200
        else:
            return jsonify({'error': 'Incorrect password', 'status': 'Failed'}), 403
    except KeyError:
        return jsonify({'error': 'Missing required data', 'status': 'Failed'}), 400

# Questions
@api.route('/questions', methods=['POST', 'GET'])
def get_all_questions():
    if request.method == 'POST':
        data = request.json
        try:
            username = Admin.get(username=data['username'])
            subject = Subject.get(name=data['subject'].lower())
            year = Year.get(name=str(data['year']).lower())
            options = data['options']
            answer = data['answer']
            question = data['question']
            if Questions.query.filter_by(question=question).first() is None:
                if not username:
                    return jsonify({"error": f"Admin user not found"}), 404
                if not subject:
                    return jsonify({"error": f"Subject not found in database"}), 404
                if not year:
                    return jsonify({"error": f"Year not found in database"}), 404
                if not Questions.query.filter_by(question=question).first():
                    jsonify({"error": "Question already exists"}), 406
                _question = Questions(question=question, answer=answer,
                                    options=options, author=username, subject=subject, year=year)
                if _question.answer_in_option():
                    _question.save()
                    questions = [x.to_dict() for x in Questions.all()]
                    return jsonify({'data': questions, 'status': 'created'}), 201
                else:
                    return jsonify({"error": "Answer not in options"}), 404
            else:
                return jsonify({'erro':'Question exists'}), 404
        except KeyError:
            return jsonify({'error': 'Missing required data', 'status': 'Failed'}), 400
    questions = [x.to_dict() for x in Questions.all()]
    return jsonify(questions), 200

@api.route('/questions/query', methods=['GET', 'DELETE', 'PUT'])
def question():
    try:
        id = request.args['id']
    except KeyError:
        return jsonify({'error': 'Missing parameter <id>', 'status': 'Failed'}), 400
    if request.method == "DELETE":
        data = Questions.get(id=str(id))
        if data is None:
            return jsonify({"error": "No question found with that id", "method": "delete"}), 404
        data.delete()
        return jsonify({'message': 'Successfully deleted Question', 'status': 'success'})
    if request.method == "PUT":
        ques = Questions.get(id=str(id))
        if ques is None:
            return jsonify({"error": "No question found with that id", "method": "delete"}), 404
        data = request.json
        subject = data.get('subject')
        year = data.get('year')
        question = data.get('question')
        options = data.get('option')
        answer = data.get('answer')  
        if question:
            q = Questions.query.filter_by(question=question).first()
            if q:
                return jsonify({'error':'Question exists, cannot update'}), 400
            ques.question = question  
        if subject:
            sub = Subject.get(name=subject.lower())
            if not sub:
                return jsonify({'error':'No subject found as such'}), 404
            ques.subject = sub
        if year:
            yer = Year.get(name=year.lower())
            if not yer:
                return jsonify({'error':'No year found as such'}), 404
            ques.year = yer
        if options:
            if isinstance(options,list) or isinstance(options,dict):
                ques.options = options
            else:
                return jsonify({'error':'Option is not a list or dictionary, cannot update'}), 400
        if answer:
            ques.answer = answer
        if ques.answer_in_option():
            ques.save()
            return jsonify({'data':ques.to_dict(),'message':'Successfully updated question'}), 201
        else:
            return jsonify({"error":"Answer not in options"}), 404
    data = Questions.get(id=str(id))
    if data is None:
        return jsonify({"error": "No question found with that id", "method": "get"}), 404
    return jsonify({'message': 'success', 'data': data.to_dict()}), 200

# @api.route('/quiz',methods=['GET','POST'])
# def quiz():
#     if request.method == 'POST':
#         data = request.json
#         try:
#             username = data['username']
#             email = data['email']
#             password = data['password']
#             condition = and_(Admin.username == username, Admin.email == email)
#             if Admin.query.filter(condition).first():
#                 print(condition)
#                 return jsonify({"error": "an admin found with given data"}), 406
#             admin = Admin(username=username, email=email)
#             admin.set_password(password)
#             admin.save()
#             admins = [x.to_dict() for x in Admin.all()]
#             return jsonify({'data': admins, 'status': 'created'}), 201
#         except KeyError:
#             return jsonify({'error': 'Missing required data', 'status': 'Failed'}), 400
#     quiz = [x.to_dict() for x in Quiz.all()]
#     return jsonify(quiz), 200