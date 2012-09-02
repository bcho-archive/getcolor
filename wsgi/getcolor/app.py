#coding: utf-8

from flask import Flask

from getcolor.database import db
from getcolor.utils import register_blueprint

#: init app
app = Flask(__name__)
app.config.from_pyfile('config.py')

#: init database
db.init_app(app)
db.app = app

#: register blueprints
blueprints = ['color']

for blueprint in blueprints:
    register_blueprint(app, blueprint)
