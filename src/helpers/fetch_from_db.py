from datetime import datetime

from src.common import prompts
from src.helpers import take_input
from src.controllers.blog import Blog
from src.common.sql_query import Sql
from src.controllers.authentication import Authentication
from src.controllers.user import User
from src.common.flags import Flag
from src.common.roles import Role

from src.models import database


def get_username(user_id):
    username = database.get_item(Sql.GET_USERNAME_BY_USERID.value, (user_id,))[0]
    return username

