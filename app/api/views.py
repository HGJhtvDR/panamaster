from flask import jsonify
from flask_restful import Resource
from . import api

class HealthCheckResource(Resource):
    def get(self):
        return {
            'status': 'ok',
            'message': 'API is running'
        }

api.add_resource(HealthCheckResource, '/health') 