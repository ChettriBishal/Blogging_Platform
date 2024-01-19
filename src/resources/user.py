import requests
from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("User", __name__, description="User operations")
