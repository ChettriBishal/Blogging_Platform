from flask.views import MethodView
from config.flags import Flag
from models.user.user_model import User
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from schemas.authentication_schema import SignUpSchema, LoginSchema
from controllers.authentication.user.user_login_controller import UserLogin
from controllers.authentication.user.user_signup_controller import UserSignUp
from controllers.user.user_controller import UserController
from config.message import Message
from config.constants import authorization_bearer

blp = Blueprint("User", __name__, description="User operations")


@blp.route('/signup')
class UserSignUpRoute(MethodView):
    @blp.arguments(SignUpSchema)
    def post(self, user_data):
        auth_val = UserSignUp.sign_up(user_data['username'], user_data['password'], user_data['email'])
        return auth_val


@blp.route('/login')
class UserLoginRoute(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, user_data):
        auth_val = UserLogin.sign_in(user_data['username'], user_data['password'])
        return auth_val


@blp.route('/logout')
class UserLogoutRoute(MethodView):
    def post(self):
        return {"message": Message.SIGNED_OUT}


@blp.route('/personal')
class GetUserData(MethodView):
    @jwt_required()
    @blp.doc(parameters=authorization_bearer)
    def get(self):
        user_access_object = UserController()
        return user_access_object.get_self_details()


@blp.route('/users')
class GetAllUsers(MethodView):
    @jwt_required()
    def get(self):
        user_access_object = UserController()
        return user_access_object.get_all_users()


@blp.route('/users/<int:userId>')
class GetUserDataFromId(MethodView):
    def get(self, userId):
        user_access_object = UserController()
        return user_access_object.get_user_details_by_userid(userId)


@blp.route('/users/<string:username>')
class GetUserDataFromName(MethodView):
    def get(self, username):
        user_access_object = UserController()
        return user_access_object.get_user_details_by_username(username)
