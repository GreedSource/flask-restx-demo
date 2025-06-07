from flask import Blueprint
from flask_restx import Api
from .example_api import example_resource as example_routes


v2_api = Blueprint("v2", __name__, url_prefix="/api/v2")

_api = Api(v2_api)

_api.add_namespace(example_routes)
