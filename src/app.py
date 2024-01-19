from flask import Flask
from resources.user import blp as UserRoute
from resources.blog import blp as BlogRoute
from resources.blogger import blp as BloggerOperationRoute
from flask_smorest import Api

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

api.register_blueprint(UserRoute)
api.register_blueprint(BlogRoute)
api.register_blueprint(BloggerOperationRoute)

if __name__ == "__main__":
    app.run(debug=True)
