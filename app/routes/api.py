from flask import Blueprint, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restful import Api, Resource

bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(bp)
limiter = Limiter(key_func=get_remote_address)


class HealthCheck(Resource):
    @limiter.limit("10 per minute")
    def get(self):
        return jsonify({"status": "healthy", "version": "1.0.0"})


api.add_resource(HealthCheck, "/health")
