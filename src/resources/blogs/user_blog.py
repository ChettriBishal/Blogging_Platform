import requests
from flask.views import MethodView
from config.flags import Flag
from flask import jsonify
from controllers.user import User

from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt

from flask_smorest import Blueprint, abort
from schemas.authentication_schema import SignUpSchema, LoginSchema
from controllers.authentication.user.user_login_controller import UserLogin
from controllers.authentication.user.user_signup_controller import UserSignUp

blp = Blueprint("User_blog", __name__, description="User blog operations")


@blp.route('/users/<string:userId>/blogs')
class BlogsFromId(MethodView):
    def get(self, userId):
        return {"message": f"{userId} Watch Imitation Game"}

    def post(self, userId):
        return {"message": f"new blog added by {userId}"}


@blp.route('/users/<string:userId>/blogs')
class GetUserBlogById(MethodView):
    def get(self, userId):
        blogId = requests.args.get('blogId')
        return {"message": f"Blog with id {blogId} by userId {userId}"}