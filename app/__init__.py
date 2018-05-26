#app/__init__.py: Flask application instance

# app is a instance of Flask
# __name__ is flask's predefine variable name.

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

login = LoginManager(app)
login.login_view = 'login'