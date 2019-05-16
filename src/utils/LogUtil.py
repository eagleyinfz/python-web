import json

def logFormat(module, correlation_id, msg, http_code, url):
    data = {"module_name": module, "correlation_id": correlation_id, "message": msg, "http_status": http_code, "url":url}
    return json.dumps(data)