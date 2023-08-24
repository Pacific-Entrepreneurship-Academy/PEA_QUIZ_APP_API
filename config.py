import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET') or 'A random Thing'
    SQLALCHEMY_DATABASE_URI = f'mysql://{os.getenv("username")}:{os.getenv("password")}@{os.getenv("host")}:3306/{os.getenv("dbName")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False