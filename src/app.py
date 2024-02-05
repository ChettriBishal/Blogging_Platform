from flask import Flask
from resources.users.user import blp as UserRoute
from resources.blogs.blog import blp as BlogRoute
from resources.comments.comment import blp as CommentRoute
from resources.blogs.user_blog import blp as UserBlogRoute
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from config.flask_config import FlaskConfig
from utils.tokens.jwt_config_loader import initialise_jwt_config

app = Flask(__name__)
app.app_context().push()
app.config.from_object(FlaskConfig)

api = Api(app)
initialise_jwt_config(app)


api.register_blueprint(UserRoute)
api.register_blueprint(BlogRoute)
api.register_blueprint(CommentRoute)
api.register_blueprint(UserBlogRoute)


if __name__ == "__main__":
    app.run(debug=True)
