import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask('__main__')
db= SQLAlchemy(app)
db.app = app
login_manager = LoginManager(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY']= os.environ['FLASK_SECRET']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'