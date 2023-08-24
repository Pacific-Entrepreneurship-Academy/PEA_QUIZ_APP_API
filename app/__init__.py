from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
api = Blueprint('api',__name__,url_prefix='/api')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import models 
from app import routes