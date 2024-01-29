from flask.views import MethodView
from config.flags import Flag
from models.user.user_model import User

from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required

from flask_smorest import Blueprint, abort
from schemas.authentication_schema import SignUpSchema, LoginSchema
from controllers.authentication.user.user_login_controller import UserLogin
from controllers.authentication.user.user_signup_controller import UserSignUp
from controllers.user.user_controller import UserController

blp = Blueprint("User", __name__, description="User operations")


@blp.route('/signup')
class UserSignUpRoute(MethodView):
    @blp.arguments(SignUpSchema)
    def post(self, user_data):
        auth_val = UserSignUp.sign_up(user_data['username'], user_data['password'], user_data['email'])

        if auth_val == Flag.ALREADY_EXISTS.value:
            abort(409, message="Already exists")
        elif isinstance(auth_val, User):
            return {"message": "Blogger registered successfully!"}, 201


@blp.route('/login')
class UserLoginRoute(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, user_data):
        auth_val = UserLogin.sign_in(user_data['username'], user_data['password'])
        if auth_val == Flag.INVALID_USERNAME.value:
            abort(400, message="Invalid username")
        elif auth_val == Flag.DOES_NOT_EXIST.value:
            abort(404, message="User not found")
        elif not auth_val:
            abort(401, message="Wrong password")
        elif auth_val:
            access_token = create_access_token(identity=user_data['username'], fresh=True,
                                               additional_claims={"username": user_data['username']})
            refresh_token = create_refresh_token(identity=user_data['username'],
                                                 additional_claims={"username": user_data['username']})
            return {"access_token": access_token, "refresh_token": refresh_token}, 200
        abort(404, message="User not found")


@blp.route('/logout')
class UserLogoutRoute(MethodView):
    def post(self):
        return {"message": "Signed out successfully"}


@blp.route('/personal')
class GetUserData(MethodView):
    @jwt_required()
    def get(self):
        user_access_object = UserController()
        return user_access_object.get_self_details()


@blp.route('/users/<string:userId>')
class GetUserDataFromId(MethodView):
    def get(self, userId):
        return {"message": f"User details of {userId}"}



