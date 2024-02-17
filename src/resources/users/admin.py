from flask_smorest import Blueprint, abort
from flask.views import MethodView
from controllers.user.user_controller import UserController
from config.constants import authorization_bearer

blp = Blueprint("Admin", __name__, description="Admin operations")



@blp.route('/users/<int:userId>')
class RemoveUserById(MethodView):
    @blp.doc(parameters=authorization_bearer)
    def delete(self, userId):
        user_access_object = UserController()
        return user_access_object.remove_user_by_username(userId)


@blp.route('/users/<string:username>')
class RemoveUserByUsername(MethodView):
    @blp.doc(parameters=authorization_bearer)
    def delete(self, username):
        user_access_object = UserController()
        return user_access_object.get_user_details_by_username(username)