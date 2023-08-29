# Pacific-Ent-Academy-Api

Documentation coming soon ....

# Docs

## Admins

<hr>

### Get all Admin
    Endpoint: GET /admins
    Description: Retrieve all admin users.
    Required Parameters:
    - None

### Create Admin
    Endpoint: POST /admins
    Description: Creates a new admin user.
    Required Parameters:
    - username (string): The username of the admin.
    - email (string): The email address of the admin.
    - password (string): The password for the admin account.
#### Example request:
```
{
  "username": "admin123",
  "email": "admin@example.com",
  "password": "secretpassword"
}

```
### Get Single Admin
    Endpoint: GET /get-admin/query
    Description: Get Admin either by username or email.
    Required Parameters:
        Either:
           - username (string): The username of the admin.
                            or            
           - email (string): The email address of the admin.
#### Example Request:
```
    {
      "username": "admin123",
      "password": "secretpassword"
    }
```
    
## Students
Create Student

    Endpoint: POST /students
    Description: Creates a new student user.
    Required Parameters:
        firstname (string): The first name of the student.
        lastname (string): The last name of the student.
        email (string): The email address of the student.
        password (string): The password for the student account.
        year (string): The academic year of the student.
    Example Request:

    json

    {
      "firstname": "John",
      "lastname": "Doe",
      "email": "john@example.com",
      "password": "studentpassword",
      "year": "2023"
    }

    Response:
        Status: 201 Created
        Data: A list of all student users including the newly created one.

Student Login

    Endpoint: POST /student/login
    Description: Handles student user login.
    Required Parameters:
        email (string): The email address of the student.
        password (string): The password for the student account.
    Example Request:

    json

    {
      "email": "john@example.com",
      "password": "studentpassword"
    }

    Response:
        Status: 200 OK
        Data: Message indicating successful login.

Questions
Create Question

    Endpoint: POST /questions
    Description: Creates a new question.
    Required Parameters:
        username (string): The username of the admin creating the question.
        subject (string): The subject of the question.
        year (string): The academic year associated with the question.
        options (array or object): The answer options for the question.
        answer (string): The correct answer for the question.
        question (string): The question text.
    Example Request:

    json

{
  "username": "admin123",
  "subject": "Math",
  "year": "2023",
  "options": ["A", "B", "C", "D"],
  "answer": "B",
  "question": "What is 2 + 2?"
}

Response:

    Status: 201 Created
    Data: A list of all questions including the newly created one.