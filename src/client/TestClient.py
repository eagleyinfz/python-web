import requests
from settings import logger
from requests.exceptions import RequestException
from utils.ResponseUtil import decodeResponse
from utils.LogUtil import logFormat

PYTHON_URL = "https://docs.python.org"

def getPythonPage():
    global PYTHON_URL
    url = PYTHON_URL + "/3/"
    # payload = {'quantity': num}
    try:
        # response = requests.post(url, params=payload, verify=False)
        response = requests.get(url, verify=False)
        result = decodeResponse(response)
        if response.status_code == 200:
            logger.info(logFormat("getPythonPage", "NA", "SUCCESS", str(response.status_code), url))
            return result
        else :
            logger.error(logFormat("getPythonPage", "NA", result, str(response.status_code), url))
            return None
    except RequestException as e:
        logger.error(logFormat("getPythonPage", "NA", repr(e), "NA", url))
        return None
    except Exception as ex:
        logger.error(logFormat("getPythonPage", "NA", repr(ex), "NA", url))
        return None