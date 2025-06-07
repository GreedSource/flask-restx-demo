from flask import Blueprint
from flask_restx import Api
from .example_api import example_resource as example_routes


v1_api = Blueprint("v1", __name__, url_prefix="/api/v1")

_api = Api(v1_api)

_api.add_namespace(example_routes)

v1_api.ad
