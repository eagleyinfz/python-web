from flask_restful import Resource, fields, marshal_with
from settings import logger
from service.service import *
from utils.LogUtil import logFormat
import uuid
# from prometheus_client import Summary

# Create a metric to track time spent and requests made.
# REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

class HealthView(Resource):
    # Decorate function with metric.
    # @REQUEST_TIME.time()
    def get(self):
        return "for health check only", 200

class HelloView(Resource):
    # Decorate function with metric.
    # @REQUEST_TIME.time()
    def get(self):
        logger.info(logFormat("HelloView", str(uuid.uuid1()), "SUCCESS", '200', ""))
        return "Hello World!", 200

class ClientView(Resource):
    # Decorate function with metric.
    # @REQUEST_TIME.time()
    def get(self):
        try:
            user = do_python_page()
            logger.info(logFormat("ClientView", str(uuid.uuid1()), "SUCCESS", '200', ""))
            return user, 200
        except Exception as e:
            logger.error(logFormat("ClientView", str(uuid.uuid1()), repr(e), '500', ""))
            return repr(e), 500


user_fields = {
    'id': fields.Integer,
    'name': fields.String
}

class UserApiView(Resource):
    @marshal_with(user_fields)
    def get(self, pk):
        try:
            user = do_user_request(pk)
            logger.info(logFormat("UserApiView", str(uuid.uuid1()), "SUCCESS", '200', ""))
            return user, 200
        except Exception as e:
            logger.error(logFormat("UserApiView", str(uuid.uuid1()), repr(e), '500', ""))
            return repr(e), 500



