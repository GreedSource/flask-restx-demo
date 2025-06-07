from flask import Flask
from flask_restx import Api
from .v1 import v1_api
from .v2 import v2_api


def register_routes(app: Flask):
    """
    Registers all the API routes for the given API instance.
    """
    # Add the namespace for the v1 API version
    # Replace api_resource and example_resource with your actual namespace classes
    # The path parameter specifies the URL prefix for the namespace. In this case, "/v1" is used.
    # Make sure the Namespace classes are imported correctly and have the necessary methods and decorators.

    # Add the namespace to the API instance

    api = Api(app)

    api.add_namespace(v1_api)
    # app.register_blueprint(v1_api)
    api.add_namespace(v2_api)
    # app.register_blueprint(v2_api)
