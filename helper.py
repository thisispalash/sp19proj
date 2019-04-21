from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask('__main__')
db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)