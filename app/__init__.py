from flask import Flask, render_template
import flask_misaka
import os


APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

app=Flask(__name__, static_path=None, static_url_path=None, static_folder='static', template_folder='templates', instance_path=None, instance_relative_config=False)
flask_misaka.Misaka(app=app, renderer=None)

#app.config.from_object('config')

from app import views
