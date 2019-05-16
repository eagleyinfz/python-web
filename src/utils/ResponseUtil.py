import json
from json import JSONDecodeError

# in order to change the response into same format
def decodeResponse(response):
    try:
        return json.loads(response.text)
    except JSONDecodeError:
        return str(response.text)