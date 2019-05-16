from flask import Flask
from flask_cors import *
from flask_restful import Api

from controller.TestController import *

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)

api.add_resource(UserApiView, '/user/<int:pk>')
api.add_resource(HelloView, '/')
api.add_resource(HealthView, '/actuator/health')
api.add_resource(ClientView, '/client')

# Add prometheus wsgi middleware to route /metrics requests
# 
app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    # app.run()
    # below is used for 
    app.run(host='0.0.0.0', port=9000)


