from flask import Flask
from resources.user import blp as UserRoute
from resources.blog import blp as BlogRoute
from resources.comment import blp as CommentRoute
from flask_smorest import Api

from flask_jwt_extended import JWTManager

from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.app_context().push()

app.config["API_TITLE"] = "Blogging Platform API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config[
    "OPENAPI_SWAGGER_UI_URL"
] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["PROPAGATE_EXCEPTIONS"] = True

api = Api(app)
app.config["JWT_SECRET_KEY"] = "235911244572190182537651959146582626518"
jwt = JWTManager(app)

api.register_blueprint(UserRoute)
api.register_blueprint(BlogRoute)
api.register_blueprint(CommentRoute)

from enum import Enum
from flask.json.provider import DefaultJSONProvider, JSONProvider
from werkzeug.exceptions import HTTPException


# class CustomJSONEncoder(DefaultJSONProvider):
#     def default(self, obj):
#         if isinstance(obj, Enum):
#             return obj.value
#         elif isinstance(obj, HTTPException):
#             return obj.description
#         return super().default(obj)


# app.json = CustomJSONEncoder(app)
# app.json_provider_class = CustomJSONEncoder

if __name__ == "__main__":
    app.run(debug=True)
