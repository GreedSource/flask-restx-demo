import requests
from flask_restx import Resource, Namespace
from server.services.example_service import ExampleService


example_resource = Namespace("example", "Example Resource")


@example_resource.route("/ping")
class Ping(Resource):
    def get(self):
        return {"message": "pong"}


@example_resource.route("/currencies")
class Ping(Resource):

    def get(self):
        __example_service = ExampleService()
        return __example_service.get_currencies()
