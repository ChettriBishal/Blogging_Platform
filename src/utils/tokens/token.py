from models.database import Database
from config.sql_query_mysql import Sql
from handlers.user.user_info_handler import UserInfoHandler
from flask_jwt_extended import create_access_token, create_refresh_token, get_jti


class Token:
    @staticmethod
    def check_token_revoked(jwt_payload):
        jti_access_token = jwt_payload["jti"]

        result = Database.get_item(Sql.GET_TOKEN_STATUS.value, (jti_access_token,))
        if result[0]['token_status'] == "revoked":
            return True
        return False

    @staticmethod
    def revoke_token(jwt_payload):
        jti_access_token = jwt_payload["jti"]

        Database.query_with_params(Sql.UPDATE_TOKEN_STATUS.value, ('revoked', jti_access_token,))

    @staticmethod
    def generate_token(username):
        """To generate a JWT using username"""
        user_additional_claims = {"username": username}
        user_id = UserInfoHandler.get_user_id_by_username(username)[0]
        access_token = create_access_token(identity=user_id, fresh=True,
                                           additional_claims=user_additional_claims)

        jti_access_token = get_jti(access_token)
        refresh_token = create_refresh_token(identity=user_id,
                                             additional_claims=user_additional_claims)

        jti_refresh_token = get_jti(refresh_token)

        Database.insert_item(Sql.INSERT_TOKEN_DETAILS.value,
                             (user_id, jti_access_token, jti_refresh_token))

        return {"access_token": access_token, "refresh_token": refresh_token}
