from flask_jwt_extended import verify_jwt_in_request, get_jwt
from handlers.user.user_info_handler import UserInfoHandler


class GetCurrentUser:
    @staticmethod
    def get_user_name():
        verify_jwt_in_request()
        claims = get_jwt()
        return claims["username"]

    @staticmethod
    def get_user_id():
        username = GetCurrentUser.get_user_name()
        return UserInfoHandler.get_user_id_by_username(username)[0]

    @staticmethod
    def get_user_role():
        verify_jwt_in_request()
        claims = get_jwt()
        return claims["role"]
