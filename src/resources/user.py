import requests
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort

blp = Blueprint("User", __name__, description="User operations")


@blp.route('/signup')
class UserSignUp(MethodView):
    def post(self):
        return {"message": "Signed up successfully"}


@blp.route('/login')
class UserLogin(MethodView):
    def post(self):
        return {"message": "Signed in successfully"}


@blp.route('/logout')
class UserLogout(MethodView):
    def post(self):
        return {"message": "Signed out successfully"}


@blp.route('/personal')
class GetUserData(MethodView):
    def get(self):
        return {"message": "Personal data of the user"}


@blp.route('/users/<string:userId>')
class GetUserDataFromId(MethodView):
    def get(self, userId):
        return {"message": f"User details of {userId}"}


@blp.route('/users/<string:userId>/blogs')
class GetUserBlogsFromId(MethodView):
    def get(self, userId):
        return {"message": f"{userId} Watch Imitation Game"}


@blp.route('/users/<string:userId>/blogs')
class GetUserBlogById(MethodView):
    def get(self, userId):
        blogId = requests.args.get('blogId')
        return {"message": f"Blog with id {blogId} by userId {userId}"}
