#app/__init__.py: Flask application instance

# app is a instance of Flask
# __name__ is flask's predefine variable name.

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes