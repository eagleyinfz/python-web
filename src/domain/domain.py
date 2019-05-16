from db import db_session
from db.models import *


def get_user_info(pk):
    user = db_session.query(UserModel).get(pk)
    return user
