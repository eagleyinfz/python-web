from domain.domain import *
from client.TestClient import *


def do_user_request(pk):
    if isinstance(pk, int):
        return get_user_info(pk)
    else:
        raise Exception('pk is not int type')

def do_python_page():
    return getPythonPage()