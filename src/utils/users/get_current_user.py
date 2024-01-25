from flask_jwt_extended import verify_jwt_in_request, get_jwt


class GetCurrentUser:
    @staticmethod
    def get_user_name():
        verify_jwt_in_request()
        claims = get_jwt()
        return claims["username"]

    @staticmethod
    def get_user_role():
        verify_jwt_in_request()
        claims = get_jwt()
        return claims["role"]
