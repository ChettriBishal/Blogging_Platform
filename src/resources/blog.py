import requests
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint('Blog', __name__, description='Operations on blogs')
