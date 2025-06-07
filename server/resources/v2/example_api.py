from flask_restx import Resource, Namespace
from server.services.example_service import ExampleService


example_resource = Namespace(
    name="example2", description="Example Resource", path="/example2"
)


@example_resource.route("/currencies")
class CurrenciesApiGet(Resource):

    def get(self):
        __example_service = ExampleService()
        return __example_service.get_currencies()


@example_resource.route("/ping")
class Ping(Resource):
    def get(self):
        return {"message": "pong!"}
