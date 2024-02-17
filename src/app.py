from flask import Flask, request
from resources.users.user import blp as UserRoute
from resources.blogs.blog import blp as BlogRoute
from resources.comments.comment import blp as CommentRoute
from resources.blogs.user_blog import blp as UserBlogRoute
from flask_smorest import Api
from config.flask_config import FlaskConfig
from utils.tokens.jwt_config_loader import initialise_jwt_config
from shortuuid import ShortUUID

app = Flask(__name__)
app.app_context().push()
app.config.from_object(FlaskConfig)

api = Api(app)
initialise_jwt_config(app)


@app.before_request
def set_custom_headers():
    request_id = ShortUUID().random(length=10)
    request.environ["X-Request-Id"] = request_id


api.register_blueprint(UserRoute)
api.register_blueprint(BlogRoute)
api.register_blueprint(CommentRoute)
api.register_blueprint(UserBlogRoute)


if __name__ == "__main__":
    app.run(debug=True)
