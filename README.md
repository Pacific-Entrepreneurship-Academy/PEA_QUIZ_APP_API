# Pacific-Ent-Academy-Api

Documentation coming soon ....

# Docs

-   Documentation for API Endpoints
    -------------------------------

    ### Admins

    #### POST /admins

    -   Create a new admin user.
    -   **Request Method:** POST
    -   **Request Body:** JSON
        -   `username` (string): Admin's username
        -   `email` (string): Admin's email
        -   `password` (string): Admin's password
    -   **Response:**
        -   `data` (list of admin objects): Created admin users
        -   `status` (string): "created"
    -   Example Request:

        json

    -   `{
          "username": "admin1",
          "email": "admin1@example.com",
          "password": "securepassword"
        }`

    #### GET /admins

    -   Retrieve a list of all admin users.
    -   **Request Method:** GET
    -   **Response:**
        -   `data` (list of admin objects): List of admin users
    -   Example Response:

        json

    -   `{
          "data": [
            {
              "username": "admin1",
              "email": "admin1@example.com"
            },
            {
              "username": "admin2",
              "email": "admin2@example.com"
            }
          ]
        }`

    #### GET /get-admin/query

    -   Retrieve admin information based on query parameters.
    -   **Request Method:** GET
    -   **Query Parameters:**
        -   `username` (string, optional): Admin's username
        -   `email` (string, optional): Admin's email
        -   `id` (string, optional): Admin's ID
    -   **Response:**
        -   `data` (admin object): Admin information
    -   Example Request:
        -   `/get-admin/query?username=admin1`
        -   `/get-admin/query?email=admin1@example.com`
        -   `/get-admin/query?id=12345`
    -   Example Response:

        json

    -   `{
          "message": "success",
          "data": {
            "username": "admin1",
            "email": "admin1@example.com"
          }
        }`

    #### POST /admin/login

    -   Log in an admin user.
    -   **Request Method:** POST
    -   **Request Body:** JSON
        -   `username` (string): Admin's username
        -   `email` (string, optional): Admin's email
        -   `password` (string): Admin's password
    -   **Response:**
        -   `message` (string): "Logged in"
        -   `status` (string): "success"
    -   Example Request:

        json

    -   `{
          "username": "admin1",
          "password": "securepassword"
        }`

    ### Students

    #### POST /students

    -   Create a new student.
    -   **Request Method:** POST
    -   **Request Body:** JSON
        -   `firstname` (string): Student's first name
        -   `lastname` (string): Student's last name
        -   `email` (string): Student's email
        -   `password` (string): Student's password
        -   `year` (string): Student's year
    -   **Response:**
        -   `data` (list of student objects): Created student users
        -   `status` (string): "created"
    -   Example Request:

        json

    -   `{
          "firstname": "John",
          "lastname": "Doe",
          "email": "john@example.com",
          "password": "securepassword",
          "year": "three"
        }`

    #### GET /students

    -   Retrieve a list of all student users.
    -   **Request Method:** GET
    -   **Response:**
        -   `data` (list of student objects): List of student users
    -   Example Response:

        json

    -   `{
          "data": [
            {
              "firstname": "John",
              "lastname": "Doe",
              "email": "john@example.com",
              "year": "one"
            },
            {
              "firstname": "Jane",
              "lastname": "Smith",
              "email": "jane@example.com",
              "year": "two"
            }
          ]
        }`

    #### GET /get-student/query

    -   Retrieve student information based on query parameters.
    -   **Request Method:** GET
    -   **Query Parameters:**
        -   `firstname` (string, optional): Student's first name
        -   `lastname` (string, optional): Student's last name
        -   `email` (string, optional): Student's email
        -   `id` (string, optional): Student's ID
    -   **Response:**
        -   `data` (student object): Student information
    -   Example Request:
        -   `/get-student/query?firstname=John`
        -   `/get-student/query?email=john@example.com`
        -   `/get-student/query?id=12345`
    -   Example Response:

        json

    -   `{
          "message": "success",
          "data": {
            "firstname": "John",
            "lastname": "Doe",
            "email": "john@example.com",
            "year": "eleven"
          }
        }`

    #### POST /student/login

    -   Log in a student user.
    -   **Request Method:** POST
    -   **Request Body:** JSON
        -   `email` (string): Student's email
        -   `password` (string): Student's password
    -   **Response:**
        -   `message` (string): "Logged in"
        -   `status` (string): "success"
    -   Example Request:

        json

    -   `{
          "email": "john@example.com",
          "password": "securepassword"
        }`

    ### Questions

    #### POST /questions

    -   Create a new question.
    -   **Request Method:** POST
    -   **Request Body:** JSON
        -   `username` (string): Admin's username
        -   `subject` (string): Question subject
        -   `year` (string): Question year
        -   `options` (list or dictionary): Question options
        -   `answer` (string): Question answer
        -   `question` (string): The question itself
    -   **Response:**
        -   `data` (list of question objects): Created questions
        -   `status` (string): "created"
    -   Example Request:

        json

    -   `{
          "username": "admin1",
          "subject": "math",
          "year": "seven",
          "options": ["A", "B", "C", "D"],
          "answer": "A",
          "question": "What is 2 + 2?"
        }`

    #### GET /questions

    -   Retrieve a list of all questions.
    -   **Request Method:** GET
    -   **Response:**
        -   `data` (list of question objects): List of questions
    -   Example Response:

        json

    -   `{
          "data": [
            {
              "subject": "math",
              "year": "ten",
              "options": ["A", "B", "C", "D"],
              "answer": "A",
              "question": "What is 2 + 2?"
            },
            {
              "subject": "science",
              "year": "twelve",
              "options": ["A", "B", "C", "D"],
              "answer": "C",
              "question": "What is the capital of France?"
            }
          ]
        }`

    #### GET /questions/query

    -   Retrieve question information based on query parameters.
    -   **Request Method:** GET
    -   **Query Parameters:**
        -   `id` (string, required): Question's ID
    -   **Response:**
        -   `data` (question object): Question information
    -   Example Request:
        -   `/questions/query?id=12345`
    -   Example Response:

        json

    -   `{
          "message": "success",
          "data": {
            "subject": "math",
            "year": "ten",
            "options": ["A", "B", "C", "D"],
            "answer": "A",
            "question": "What is 2 + 2?"
          }
        }`

    #### PUT /questions/query

    -   Update question information based on query parameters.
    -   **Request Method:** PUT
    -   **Query Parameters:**
        -   `id` (string, required): Question's ID
    -   **Request Body:** JSON
        -   `subject` (string, optional): Updated question subject
        -   `year` (string, optional): Updated question year
        -   `options` (list or dictionary, optional): Updated question options
        -   `answer` (string, optional): Updated question answer
        -   `question` (string, optional): Updated question itself
    -   **Response:**
        -   `data` (question object): Updated question information
        -   `message` (string): "Successfully updated question"
    -   Example Request:
        -   `/questions/query?id=12345`

        json

    -   `{
          "subject": "math",
          "options": ["A", "B", "C"],
          "answer": "B"
        }`

        -   Example Response:

        json

    -   `{
          "data": {
            "subject": "math",
            "year": "five",
            "options": ["A", "B", "C"],
            "answer": "B",
            "question": "What is 2 + 2?"
          },
          "message": "Successfully updated question"
        }`

    #### DELETE /questions/query

    -   Delete a question based on query parameters.
    -   **Request Method:** DELETE
    -   **Query Parameters:**
        -   `id` (string, required): Question's ID
    -   **Response:**
        -   `message` (string): "Successfully deleted Question"
    -   Example Request:
        -   `/questions/query?id=12345`
    -   Example Response:

        json

    `{
      "message": "Successfully deleted Question"
    }`
