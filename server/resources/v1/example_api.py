from flask_restx import Resource, Namespace
from server.services.example_service import ExampleService
from server.utils.logger import logger


example_resource = Namespace(
    name="example", description="Example Resource", path="/example"
)
__example_service = ExampleService()


@example_resource.route("/currencies")
class CurrenciesApiGet(Resource):

    def get(self):
        return __example_service.get_currencies()


@example_resource.route("/ping")
class Ping(Resource):
    def get(self):
        logger.info("something")
        return {"message": "pong!"}
