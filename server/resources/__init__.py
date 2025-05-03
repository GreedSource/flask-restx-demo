from flask import Blueprint
from flask_restx import Api
from .v1.api import api_resource  # Import the namespace
from .v1.example_api import example_resource


def register_routes(api: Api):
    """
    Registers all the API routes for the given API instance.
    """
    # Add the namespace for the v1 API version
    # Replace api_resource and example_resource with your actual namespace classes
    # The path parameter specifies the URL prefix for the namespace. In this case, "/v1" is used.
    # Make sure the Namespace classes are imported correctly and have the necessary methods and decorators.

    # Add the namespace to the API instance
    api.add_namespace(api_resource)  # Make sure api_resource is a Namespace
    api.add_namespace(example_resource)  # Make sure example_resource is a Namespace
